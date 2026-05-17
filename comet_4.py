"""
Comet API 채널.
Comet은 OpenAI 호환 형식이라 httpx로 직접 호출하는 게 가장 깔끔하다.
이미지 모델은 환경변수 COMET_IMAGE_MODEL로 주입 (예: flux-pro, sdxl 등 계정에 따라 다름).

시리즈 작업(컷별 이미지 생성 등)을 위한 기능:
- generate_comet: 단일 이미지 생성 (재시도 포함)
- generate_comet_batch: 여러 프롬프트를 동시성 제한하며 병렬 생성
- 모든 호출은 run_dir/_log.jsonl에 누적 기록
"""

import asyncio
import base64
import json
import os
import random
import time
from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

import httpx

COMET_BASE_URL = os.getenv("COMET_BASE_URL", "https://api.cometapi.com/v1")
COMET_API_KEY = os.getenv("COMET_API_KEY")
COMET_MODEL = os.getenv("COMET_IMAGE_MODEL", "flux-pro")
COMET_TIMEOUT = float(os.getenv("COMET_TIMEOUT", "180"))
COMET_RESPONSE_FORMAT = os.getenv("COMET_RESPONSE_FORMAT", "b64_json")  # "b64_json" 권장, "url"도 가능
COMET_MAX_RETRIES = int(os.getenv("COMET_MAX_RETRIES", "4"))
COMET_BACKOFF_BASE = float(os.getenv("COMET_BACKOFF_BASE", "2.0"))  # 초
COMET_BACKOFF_CAP = float(os.getenv("COMET_BACKOFF_CAP", "30.0"))  # 초
COMET_CONCURRENCY = int(os.getenv("COMET_CONCURRENCY", "3"))

# 재시도할 HTTP 상태 코드. 429(rate limit)와 5xx만 재시도한다.
_RETRYABLE_STATUS = {429, 500, 502, 503, 504}


@dataclass
class CometJob:
    """배치 처리용 작업 정의."""
    prompt: str
    filename: str
    size: str = "1024x1024"
    # 자유 메타데이터 (컷 번호, 장면명 등). 로그에 그대로 기록된다.
    meta: dict | None = None


def _backoff_delay(attempt: int) -> float:
    """Exponential backoff with full jitter. attempt는 0부터 시작."""
    raw = COMET_BACKOFF_BASE * (2 ** attempt)
    return random.uniform(0, min(raw, COMET_BACKOFF_CAP))


def _append_log(run_dir: Path, record: dict) -> None:
    """run_dir/_log.jsonl에 한 줄 추가. 동시 호출 안전 (append-only)."""
    log_path = run_dir / "_log.jsonl"
    line = json.dumps(record, ensure_ascii=False, default=str)
    # 짧은 append이므로 동기 IO로 충분. asyncio 이벤트 루프를 길게 막지 않는다.
    with log_path.open("a", encoding="utf-8") as f:
        f.write(line + "\n")


async def _request_with_retry(
    client: httpx.AsyncClient,
    url: str,
    headers: dict,
    json_body: dict,
) -> httpx.Response:
    """429/5xx에 대해서만 재시도. 그 외 4xx는 그대로 반환해 호출부에서 처리."""
    last_exc: Exception | None = None
    for attempt in range(COMET_MAX_RETRIES + 1):
        try:
            r = await client.post(url, headers=headers, json=json_body)
        except (httpx.TimeoutException, httpx.TransportError) as e:
            last_exc = e
            if attempt >= COMET_MAX_RETRIES:
                raise
            await asyncio.sleep(_backoff_delay(attempt))
            continue

        if r.status_code in _RETRYABLE_STATUS and attempt < COMET_MAX_RETRIES:
            # Retry-After 헤더가 있으면 우선 사용
            retry_after = r.headers.get("retry-after")
            if retry_after:
                try:
                    delay = float(retry_after)
                except ValueError:
                    delay = _backoff_delay(attempt)
            else:
                delay = _backoff_delay(attempt)
            await asyncio.sleep(delay)
            continue

        return r

    # 도달 불가지만 타입 안정성을 위해
    raise RuntimeError(f"재시도 한계 초과: {last_exc}")


async def generate_comet(
    prompt: str,
    run_dir: Path,
    filename: str = "comet.png",
    size: str = "1024x1024",
    meta: dict | None = None,
    client: httpx.AsyncClient | None = None,
) -> dict:
    """
    Comet API로 이미지 한 장을 생성해 run_dir/filename으로 저장한다.

    Args:
        prompt: 이미지 생성 프롬프트.
        run_dir: 저장할 디렉토리. 없으면 생성한다.
        filename: 저장 파일명. 시리즈 작업 시 컷별로 다르게 지정 (예: "cut_01.png").
        size: 이미지 크기. 모델별 지원 범위가 다름.
        meta: 로그에 함께 기록할 자유 메타데이터.
        client: 재사용할 httpx.AsyncClient. 없으면 함수 내에서 생성·종료.

    Returns:
        {file, elapsed_sec, model, raw_url} dict.
    """
    if not COMET_API_KEY:
        raise RuntimeError("COMET_API_KEY 환경변수가 없습니다.")

    run_dir.mkdir(parents=True, exist_ok=True)
    out_path = run_dir / filename

    t0 = time.time()
    started_at = datetime.now(timezone.utc).isoformat()
    own_client = client is None
    if own_client:
        client = httpx.AsyncClient(timeout=COMET_TIMEOUT)
    assert client is not None  # 타입 체커용

    image_url: str | None = None
    error_msg: str | None = None

    try:
        r = await _request_with_retry(
            client,
            f"{COMET_BASE_URL}/images/generations",
            headers={"Authorization": f"Bearer {COMET_API_KEY}"},
            json_body={
                "model": COMET_MODEL,
                "prompt": prompt,
                "n": 1,
                "size": size,
                "response_format": COMET_RESPONSE_FORMAT,
            },
        )

        if r.is_error:
            error_msg = f"Comet API error {r.status_code}: {r.text}"
            raise RuntimeError(error_msg)

        data = r.json()
        items = data.get("data") or []
        if not items:
            error_msg = (
                f"Comet API가 빈 응답을 반환했습니다 "
                f"(필터링되었거나 모델 오류일 수 있음): {data}"
            )
            raise RuntimeError(error_msg)

        first = items[0]
        if "b64_json" in first and first["b64_json"]:
            out_path.write_bytes(base64.b64decode(first["b64_json"]))
        elif "url" in first and first["url"]:
            image_url = first["url"]
            img_resp = await client.get(image_url)
            if img_resp.is_error:
                error_msg = (
                    f"이미지 다운로드 실패 {img_resp.status_code}: {image_url}"
                )
                raise RuntimeError(error_msg)
            out_path.write_bytes(img_resp.content)
        else:
            error_msg = f"Comet 응답에 b64_json도 url도 없습니다: {first}"
            raise RuntimeError(error_msg)

    except Exception as e:
        if error_msg is None:
            error_msg = repr(e)
        _append_log(run_dir, {
            "started_at": started_at,
            "elapsed_sec": time.time() - t0,
            "model": COMET_MODEL,
            "filename": filename,
            "size": size,
            "prompt": prompt,
            "meta": meta,
            "status": "error",
            "error": error_msg,
        })
        raise
    finally:
        if own_client:
            await client.aclose()

    elapsed = time.time() - t0
    _append_log(run_dir, {
        "started_at": started_at,
        "elapsed_sec": elapsed,
        "model": COMET_MODEL,
        "filename": filename,
        "size": size,
        "prompt": prompt,
        "meta": meta,
        "status": "ok",
        "file": str(out_path),
        "raw_url": image_url,
    })

    return {
        "file": out_path,
        "elapsed_sec": elapsed,
        "model": COMET_MODEL,
        "raw_url": image_url,
    }


async def generate_comet_batch(
    jobs: Iterable[CometJob],
    run_dir: Path,
    concurrency: int | None = None,
    stop_on_error: bool = False,
) -> list[dict | Exception]:
    """
    여러 프롬프트를 동시성 제한하며 병렬로 생성.

    Args:
        jobs: CometJob 리스트.
        run_dir: 저장 디렉토리.
        concurrency: 동시 요청 수. 기본은 COMET_CONCURRENCY 환경변수.
        stop_on_error: True면 첫 실패가 감지되는 즉시 진행 중이지 않은 후속 작업을
                       건너뛰지만, 이미 완료/진행 중이던 작업의 결과는 보존해
                       반환한다 (시리즈 작업의 비싼 결과 손실 방지). 
                       False면 모든 작업을 끝까지 돌리고 실패는 Exception으로 보존.

    Returns:
        jobs와 같은 순서의 결과 리스트. 성공 시 dict, 실패 시 Exception.
        stop_on_error=True로 중단된 경우, 시작되지 않은 자리에는
        asyncio.CancelledError가 들어간다.
    """
    limit = concurrency if concurrency is not None else COMET_CONCURRENCY
    sem = asyncio.Semaphore(limit)
    run_dir.mkdir(parents=True, exist_ok=True)
    jobs_list = list(jobs)

    # filename 중복 검증 — 시리즈 작업에서 cut_01.png가 두 번 들어가면
    # 한 컷이 조용히 덮어써져 사라지므로 시작 전에 막는다.
    fname_counts = Counter(j.filename for j in jobs_list)
    dups = [f for f, c in fname_counts.items() if c > 1]
    if dups:
        raise ValueError(f"중복된 filename이 있습니다: {dups}")

    async with httpx.AsyncClient(timeout=COMET_TIMEOUT) as client:
        # stop_on_error=True일 때 후속 작업을 건너뛰기 위한 플래그
        stop_flag = asyncio.Event()

        async def _run(job: CometJob) -> dict:
            # 이미 다른 작업이 실패해 stop이 걸렸으면 시작하지 않는다.
            if stop_on_error and stop_flag.is_set():
                raise asyncio.CancelledError(
                    f"이전 실패로 인해 {job.filename} 건너뜀"
                )
            async with sem:
                if stop_on_error and stop_flag.is_set():
                    raise asyncio.CancelledError(
                        f"이전 실패로 인해 {job.filename} 건너뜀"
                    )
                try:
                    return await generate_comet(
                        prompt=job.prompt,
                        run_dir=run_dir,
                        filename=job.filename,
                        size=job.size,
                        meta=job.meta,
                        client=client,
                    )
                except Exception:
                    if stop_on_error:
                        stop_flag.set()
                    raise

        # 항상 return_exceptions=True. stop_on_error 모드에서도
        # 이미 완료된 작업의 결과(비싼 API 호출 결과)를 절대 잃지 않는다.
        return list(await asyncio.gather(
            *(_run(j) for j in jobs_list),
            return_exceptions=True,
        ))
