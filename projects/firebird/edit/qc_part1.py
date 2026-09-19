#!/usr/bin/env python3
"""
완성본 해부 — 들을 수도 볼 수도 없는 쪽이 검수할 수 있게 만든다.

  python3 qc_part1.py --film part1.mp4 --out qc/

만드는 것:
  qc/contact_sheet.jpg   컷마다 한 프레임씩, 격자로 (그림 확인)
  qc/waveform.png        전체 파형 (음악이 어디서 들어오는지)
  qc/spectrogram.png     전체 스펙트로그램 (첼로 드론·무음·습격 구분)
  qc/report.md           무음·검은화면·정지·구간별 라우드니스 측정값

측정은 로그로도 찍는다. 이미지는 저장소에 커밋해 사람 아닌 쪽도 읽게 한다.
"""
import argparse, json, re, subprocess, sys
from pathlib import Path

try:
    import imageio_ffmpeg
    FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
except Exception:
    import shutil
    FFMPEG = shutil.which("ffmpeg") or "ffmpeg"


def ff(args, expect_ok=True):
    r = subprocess.run([FFMPEG, "-hide_banner", *args], capture_output=True, text=True)
    if expect_ok and r.returncode != 0:
        sys.stderr.write(r.stderr[-2000:] + "\n")
        raise SystemExit(f"ffmpeg 실패: {' '.join(args[:8])}")
    return r.stderr


def hhmmss(t):
    return f"{int(t)//60}:{int(t)%60:02d}"


def cut_starts(man):
    """디졸브는 핸들로 보상되므로 누적 시작점은 길이의 단순 합이다."""
    t, rows = 0.0, []
    for e in man["timeline"]:
        rows.append((e["cut"], t, e["dur"], e["kind"]))
        t += e["dur"]
    return rows, t


def analyse_stems(media, used=None):
    """베드와 스코어 원본을 잰다 — 희박한가, 작기만 한가.
    `used` 에 없는 파일은 빌드가 쓰지 않는 것이므로 그렇게 표시한다."""
    rows = []
    for sub in ("beds", "score"):
        d = Path(media) / sub
        if not d.is_dir():
            continue
        for f in sorted(d.iterdir()):
            if f.suffix.lower() not in (".wav", ".mp3", ".m4a", ".ogg"):
                continue
            info = ff(["-i", str(f)], expect_ok=False)
            m = re.search(r"Duration:\s*(\d+):(\d+):([\d.]+)", info)
            dur = (int(m.group(1))*3600 + int(m.group(2))*60
                   + float(m.group(3))) if m else 0.0
            vol = ff(["-i", str(f), "-af", "volumedetect", "-f", "null", "-"],
                     expect_ok=False)
            mean = re.search(r"mean_volume:\s*(-?[\d.]+)", vol)
            peak = re.search(r"max_volume:\s*(-?[\d.]+)", vol)
            # 원본이 얼마나 비어 있는가 — 게인을 올려서 해결될 문제인지 가른다
            sil = ff(["-i", str(f), "-af", "silencedetect=noise=-40dB:d=0.5",
                      "-f", "null", "-"], expect_ok=False)
            gaps = re.findall(r"silence_duration:\s*([\d.]+)", sil)
            quiet = sum(float(g) for g in gaps)
            rows.append((f"{sub}/{f.stem}", dur,
                         mean.group(1) if mean else "?",
                         peak.group(1) if peak else "?",
                         quiet, (quiet / dur * 100) if dur else 0.0,
                         used is None or f.stem in used))
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--film", required=True)
    ap.add_argument("--stems", default=None,
                    help="media 폴더 — 있으면 베드·스코어 원본도 잰다")
    ap.add_argument("--manifest", default=str(Path(__file__).with_name("manifest.json")))
    ap.add_argument("--out", default="qc")
    ap.add_argument("--cols", type=int, default=8)
    a = ap.parse_args()

    film = Path(a.film)
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    # 이전 판이 남아 있으면 새 결과로 오인된다. 먼저 지운다.
    for stale in ("contact_sheet.jpg", "waveform.png", "spectrogram.png", "report.md"):
        (out / stale).unlink(missing_ok=True)
    man = json.loads(Path(a.manifest).read_text())
    rows, total = cut_starts(man)

    # ── 1. 컷별 한 프레임 → 컨택트 시트 ──────────────────────────────
    frames = out / "_frames"; frames.mkdir(exist_ok=True)
    for i, (cut, st, dur, kind) in enumerate(rows):
        at = st + dur / 2.0
        ff(["-y", "-ss", f"{at:.3f}", "-i", str(film), "-frames:v", "1",
            "-vf", "scale=320:-2", "-q:v", "4", str(frames / f"{i:03d}_{cut}.jpg")])
    n = len(rows)
    cols = a.cols
    tile_rows = (n + cols - 1) // cols
    # ffmpeg 의 image2 디먹서는 글롭을 받지 않는다. 순번 파일로만 만든다.
    seq = out / "_seq"; seq.mkdir(exist_ok=True)
    for i, f in enumerate(sorted(frames.glob("*.jpg"))):
        (seq / f"{i:03d}.jpg").write_bytes(f.read_bytes())
    ff(["-y", "-framerate", "1", "-i", str(seq / "%03d.jpg"),
        "-vf", f"tile={cols}x{tile_rows}:margin=6:padding=4:color=#111111",
        "-frames:v", "1", "-q:v", "3", str(out / "contact_sheet.jpg")])

    # ── 2. 파형과 스펙트로그램 ────────────────────────────────────────
    ff(["-y", "-i", str(film), "-filter_complex",
        "[0:a]showwavespic=s=1920x360:colors=#e8d5a8|#a87f4a:split_channels=0[v]",
        "-map", "[v]", "-frames:v", "1", str(out / "waveform.png")])
    ff(["-y", "-i", str(film), "-lavfi",
        "showspectrumpic=s=1920x540:mode=combined:legend=1:gain=3",
        "-frames:v", "1", str(out / "spectrogram.png")])

    # ── 3. 측정 ───────────────────────────────────────────────────────
    sil = ff(["-i", str(film), "-af", "silencedetect=noise=-50dB:d=1.5",
              "-f", "null", "-"], expect_ok=False)
    silences = re.findall(r"silence_start:\s*([\d.]+).*?silence_end:\s*([\d.]+)", sil, re.S)

    blk = ff(["-i", str(film), "-vf", "blackdetect=d=0.5:pix_th=0.05",
              "-an", "-f", "null", "-"], expect_ok=False)
    blacks = re.findall(r"black_start:([\d.]+)\s+black_end:([\d.]+)", blk)

    frz = ff(["-i", str(film), "-vf", "freezedetect=n=-60dB:d=12",
              "-an", "-f", "null", "-"], expect_ok=False)
    freezes = re.findall(r"freeze_start:\s*([\d.]+)", frz)

    eb = ff(["-i", str(film), "-af", "ebur128=framelog=quiet:peak=true",
             "-f", "null", "-"], expect_ok=False)
    def grab(k):
        m = re.search(rf"{k}:\s*(-?[\d.inf]+)", eb)
        return m.group(1) if m else "?"
    lufs, lra, peak = grab("I"), grab("LRA"), grab("Peak")

    # 구간별 평균 레벨 — 스코어 큐가 실제로 그 자리에 있는지
    sections = [("cue_A 재 (0:00-0:45)", 0, 45),
                ("조용한 중반 (1:30-3:00)", 90, 180),
                ("cue_B 철수 (3:30-4:28)", 210, 268),
                ("cue_C 습격 (5:45-6:55)", 345, 415)]
    levels = []
    for name, st, en in sections:
        s = ff(["-ss", str(st), "-t", str(en - st), "-i", str(film),
                "-af", "volumedetect", "-f", "null", "-"], expect_ok=False)
        m = re.search(r"mean_volume:\s*(-?[\d.]+)", s)
        p = re.search(r"max_volume:\s*(-?[\d.]+)", s)
        levels.append((name, m.group(1) if m else "?", p.group(1) if p else "?"))

    streams = ff(["-i", str(film)], expect_ok=False)
    has_subs = "Subtitle:" in streams
    dur_m = re.search(r"Duration:\s*(\d+):(\d+):([\d.]+)", streams)
    dur = (int(dur_m.group(1)) * 3600 + int(dur_m.group(2)) * 60
           + float(dur_m.group(3))) if dur_m else 0.0

    # ── 4. 보고서 ─────────────────────────────────────────────────────
    L = []
    L.append("# EP1 1부 — 완성본 측정\n")
    L.append(f"파일 `{film.name}` · 길이 **{dur:.2f}초** (목표 420초) · "
             f"자막 트랙 **{'있음' if has_subs else '없음'}**\n")

    L.append("\n## 라우드니스\n")
    L.append(f"| 통합 | LRA | 트루피크 |\n|---|---|---|\n| {lufs} LUFS | {lra} LU | {peak} dBTP |\n")
    L.append("\n납품 기준은 -14 LUFS / -1 dBTP.\n")

    L.append("\n## 구간별 레벨 — 스코어가 설계한 자리에 있는가\n")
    L.append("| 구간 | 평균 | 피크 |\n|---|---|---|\n")
    for name, mean, pk in levels:
        L.append(f"| {name} | {mean} dB | {pk} dB |\n")
    L.append("\n습격이 가장 크고, 조용한 중반이 가장 작아야 한다.\n")

    L.append(f"\n## 무음 — 1.5초 이상, -50dB 이하 ({len(silences)}곳)\n")
    if silences:
        L.append("| 시작 | 끝 | 길이 | 해당 컷 |\n|---|---|---|---|\n")
        for st, en in silences:
            st, en = float(st), float(en)
            hit = [c for c, s, d, _ in rows if s <= st < s + d]
            L.append(f"| {hhmmss(st)} | {hhmmss(en)} | {en-st:.1f}s | {hit[0] if hit else '-'} |\n")
    else:
        L.append("없음 — **설계와 어긋난다.** C019 전체와 C039 후반은 무음이어야 한다.\n")

    # C062 는 지시서가 정한 암전 엔드카드다. 검은 것이 정상이므로 경고에서 뺀다.
    BY_DESIGN = {"C062"}
    def cut_at(t):
        hit = [c for c, s, d, _ in rows if s <= t < s + d]
        return hit[0] if hit else "-"
    real = [(s, e) for s, e in blacks if cut_at(float(s)) not in BY_DESIGN]
    okay = [(s, e) for s, e in blacks if cut_at(float(s)) in BY_DESIGN]
    L.append(f"\n## 검은 화면 — 0.5초 이상, 설계된 암전 제외 ({len(real)}곳)\n")
    if real:
        L.append("소스가 빠졌다는 뜻이다.\n\n| 시작 | 끝 | 해당 컷 |\n|---|---|---|\n")
        for st, en in real:
            L.append(f"| {hhmmss(float(st))} | {hhmmss(float(en))} | {cut_at(float(st))} |\n")
    else:
        L.append("없음. 62컷 전부 그림이 들어 있다.\n")
    if okay:
        L.append("\n설계된 암전으로 확인된 것 — 조치 대상이 아니다:\n\n")
        for st, en in okay:
            L.append(f"- {hhmmss(float(st))}~{hhmmss(float(en))} **{cut_at(float(st))}**\n")
    else:
        L.append("\n⚠️ C062 암전이 검출되지 않았다 — 엔드카드가 안 붙었을 수 있다.\n")

    L.append(f"\n## 12초 이상 정지 ({len(freezes)}곳)\n")
    if freezes:
        L.append("의도한 홀드(C004·C028·C039)인지 확인할 것.\n\n| 시작 | 해당 컷 |\n|---|---|\n")
        for st in freezes:
            st = float(st)
            hit = [c for c, s, d, _ in rows if s <= st < s + d]
            L.append(f"| {hhmmss(st)} | {hit[0] if hit else '-'} |\n")
    else:
        L.append("없음.\n")

    if a.stems:
        # 매니페스트가 실제로 참조하는 파일만이 영화에 들어간다.
        # 버려진 파일이 표에 섞이면 고쳐야 할 것처럼 읽힌다.
        used = {b.get("file", b["name"]) for b in man.get("ambience_beds", [])}
        used |= {c["name"] for c in man.get("score", [])}
        st = analyse_stems(a.stems, used)
        live = [r for r in st if r[6]]
        dead = [r for r in st if not r[6]]
        L.append(f"\n## 원본 스템 — 쓰이는 것 ({len(live)}개)\n")
        L.append("| 스템 | 길이 | 평균 | 피크 | 빈 시간 | 비율 |\n|---|---|---|---|---|---|\n")
        for name, dur, mean, pk, quiet, pct, _ in live:
            L.append(f"| {name} | {dur:.1f}s | {mean} dB | {pk} dB | "
                     f"{quiet:.1f}s | **{pct:.0f}%** |\n")
        L.append("\n빈 비율이 높으면 게인을 올려도 채워지지 않는다 — 소재를 다시 뽑아야 한다.\n")
        if dead:
            L.append(f"\n### 쓰이지 않는 파일 ({len(dead)}개) — 조치 대상이 아니다\n\n")
            for name, dur, mean, pk, quiet, pct, _ in dead:
                L.append(f"- `{name}` — {dur:.1f}s · {mean} dB · 빈 시간 {pct:.0f}%\n")

    L.append("\n## 그림\n")
    L.append("- `contact_sheet.jpg` — 62컷 각각의 중간 프레임\n")
    L.append("- `waveform.png` — 파형\n")
    L.append("- `spectrogram.png` — 스펙트로그램\n")

    (out / "report.md").write_text("".join(L))
    print("".join(L))

    import shutil as _sh
    _sh.rmtree(frames, ignore_errors=True)
    _sh.rmtree(out / "_seq", ignore_errors=True)


if __name__ == "__main__":
    main()
