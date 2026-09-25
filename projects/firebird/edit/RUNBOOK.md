# 1부 완성본 만들기

에이전트 컨테이너는 `pikaso.cdnpk.net` 이 조직 정책으로 막혀 소스를 받을 수 없다.
**GitHub Actions 러너는 인터넷이 열려 있으므로 거기서 빌드한다** — 아무도 로컬에서 뭘 돌리지 않아도 된다.

## ⚠️ 먼저: 이 저장소는 공개다
`a50079865-oss/dudghk` 가 **public** 이다. 두 가지가 걸린다.

1. **서명된 미디어 주소 66건이 히스토리에 들어갔다** (커밋 `72e4e5b`). HEAD 에서는 지웠지만 히스토리는 남는다.
   토큰 만료는 **2026-09-22 00:00 UTC** — 그때까지 주소를 아는 사람은 누구나 영상 소스를 받을 수 있다.
2. **작품 바이블 전체가 공개돼 있다** — 세계관·인물·8부작 서사·대본·자막까지. 미공개 창작물이다.

→ **저장소를 비공개로 돌리는 것을 권한다.** Settings → General → Danger Zone → Change visibility.
  그러면 위 두 가지가 한 번에 정리된다.

## 필요한 것 — 시크릿 하나
공개 저장소에 서명된 주소를 커밋할 수는 없다(그래서 위 실수를 되풀이하지 않는다).
대신 **저장소 시크릿**에 넣으면 워크플로가 읽어 가고, 로그에는 가려져 나온다.

1. `github.com/a50079865-oss/dudghk` → **Settings** → **Secrets and variables** → **Actions**
2. **New repository secret**
3. Name: `MEDIA_URLS`
4. Secret: 받은 **`urls.json` 파일 내용 전체**를 붙여넣기 (`{` 부터 `}` 까지)
5. Add secret

그 다음 에이전트에게 말해 주면 `build/part1` 브랜치를 밀어 빌드를 돌린다.

## 빌드가 하는 일
`.github/workflows/build-part1.yml`
1. 파이썬·ffmpeg 준비
2. 시크릿에서 주소 목록 복원
3. 소스 66건 다운로드
4. `build_part1.py` 로 완성본 생성
5. **`part1.mp4`(소프트 자막) + `part1_burned.mp4`(구운 자막)** 을 아티팩트로 올린다 (14일 보관)

## 결과 받기
Actions 탭 → 해당 실행 → Artifacts → `ep1-part1` 다운로드.
에이전트도 아티팩트 상태를 조회할 수 있으니 진행 상황은 물어보면 된다.

## 토큰이 만료됐다면
`fetch_media.py` 가 전부 실패한다. 말해 주면 주소를 다시 뽑아 준다 — 시크릿만 새로 넣으면 된다.

## 참고 — 로컬에서 돌리고 싶다면
```bash
git clone -b claude/new-session-egku9q https://github.com/a50079865-oss/dudghk.git
cd dudghk/projects/firebird/edit
pip install imageio-ffmpeg
python3 fetch_media.py --urls urls.json --out ./media
python3 build_part1.py --media ./media --out part1.mp4 \
        --subs ../v2026-09-19/subtitles/EP01_part1.ko.srt
```
옵션: `--burn-subs` 자막 굽기 · `--draft` 빠른 확인 · `FIREBIRD_W=960 FIREBIRD_H=540` 저해상도
