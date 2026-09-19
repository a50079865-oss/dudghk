# 1부 완성본 만들기 — 내 컴퓨터에서 (10분)

에이전트 컨테이너는 `pikaso.cdnpk.net` 이 조직 정책으로 막혀 있어 소스를 받을 수 없다.
**아래 4줄이면 로컬에서 완성본이 나온다.** 스크립트는 62컷 전 구간에서 이미 검증됐다.

## 준비물
- Python 3.9+
- 인터넷 (ffmpeg 은 pip 로 따라온다 — 따로 설치할 필요 없다)

## 실행
```bash
git clone -b claude/new-session-egku9q https://github.com/a50079865-oss/dudghk.git
cd dudghk/projects/firebird/edit
pip install imageio-ffmpeg
python3 fetch_media.py --urls urls.json --out ./media
python3 build_part1.py --media ./media --out part1.mp4 \
        --subs ../v2026-09-19/subtitles/EP01_part1.ko.srt
```

끝나면 `part1.mp4` 가 나온다. **7분 00초 · 1920×1080 · 한국어 자막 트랙 포함.**

## 옵션
| 플래그 | 효과 |
|---|---|
| `--burn-subs` | 자막을 화면에 굽는다 (기본은 소프트 트랙이라 유튜브에서 켜고 끌 수 있다) |
| `--draft` | 저화질 빠른 확인 — 구성만 볼 때 |
| `--keep-work` | 중간 세그먼트 파일을 남긴다 (컷 하나만 다시 손볼 때) |
| `FIREBIRD_W=960 FIREBIRD_H=540` | 해상도를 낮춰 더 빠르게 |

## 확인할 것
- 끝에 찍히는 길이가 **420초 근처**인가
- "빠진 소스" 목록에 **앰비언스 베드 7종만** 있는가 (아직 안 만들었다. 그림은 완성된다)
- 스틸 20컷에 켄번스가 걸려 있는가 · C028·C034·C056·C062 는 **정지**여야 한다

## 소스를 못 받을 때
`fetch_media.py` 가 전부 실패하면 토큰이 만료된 것이다 (**2026-09-22 00:00 UTC**).
말해 주면 주소를 다시 뽑아 준다. `DOWNLOAD_LIST.md` 를 브라우저에서 열어 하나씩 받아도 된다 —
`media/` 아래에 **파일명 그대로** 두면 된다.

## 에이전트 쪽에서 전부 처리하려면
환경 네트워크 정책에서 **`pikaso.cdnpk.net` 하나만 허용**하면 된다.
일반 인터넷은 이미 열려 있고(PyPI 200), ffmpeg 도 확보돼 있다. 막힌 건 그 호스트뿐이다.
