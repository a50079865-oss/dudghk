# EP1 1부 — 편집 파이프라인 (실행 가능)
편집 지시서 `../v2026-09-19/27_EP01_PART1_EDIT_SHEET.md`를 **코드로 실행한다.**

```
manifest.json     62컷 타임라인 · 켄번스 · 전환 · 대사 · 앰비언스 · SFX · 침묵 (캐논 문서에서 생성)
build_part1.py    실제 빌드 — 이걸 돌리면 7분짜리 완성본이 나온다
fetch_media.py    소스 일괄 다운로드
```

## 쓰는 법
```bash
pip install imageio-ffmpeg
python3 fetch_media.py --urls urls.json --out ./media     # 소스 확보
python3 build_part1.py --media ./media --out part1.mp4 \
        --subs ../v2026-09-19/subtitles/EP01_part1.ko.srt
```
`--burn-subs` 자막 굽기 · `--draft` 저화질 빠른 확인 · `FIREBIRD_W/H` 해상도 축소

## 미디어 배치
```
media/C001.png … C061.png     C 계층 스틸 20장
media/C002.mp4 … C061.mp4     A·B 계층 42클립 (C027·C031·C035·C041은 립싱크 판)
media/dlg/<id>.mp3            오프스크린 대사 3줄
media/beds/<name>.wav         앰비언스 7종 (선택)
media/sfx/<cut>.wav           SFX 타점 (선택)
```
**없는 파일은 건너뛰고 계속 간다.** 베드가 아직 없어도 그림은 완성되고, 빠진 목록을 끝에 보고한다.

## 스크립트가 실제로 하는 일
1. **켄번스** — 스틸 20장에 지시서 §4의 방향·배율·이징을 건다. 지터를 줄이려 4K로 올린 뒤 zoompan을 걸고 내린다. `hold` 4컷(C028·C034·C056·C062)은 정지
2. **전환** — 기본 하드 컷. 디졸브는 지정된 2곳뿐(C022→C023 0.5s, C038→C039 0.33s). **디졸브는 두 컷을 겹쳐 총 길이를 줄이므로, 나가는 컷에 전환 길이만큼 핸들을 붙여 420초를 지킨다**
3. **오디오 4층** — 립싱크 클립의 대사(4컷) + 오프스크린 대사(3줄) + 앰비언스 베드(구간 길이만큼 루프, 양 끝 0.75s 페이드) + SFX 타점
4. **침묵** — 지시서 §6의 3곳(C019 전체 · C039 흙 소리 이후 14초 · C062)을 게이트로 0으로 누른다
5. **마감** — loudnorm −14 LUFS / TP −1, Rec.709 태그, faststart, 한국어 자막 소프트 트랙(`language=kor`)

## 검증 상태 — 가짜 미디어로 전 구간 실행 완료
62컷 전부를 합성 소스로 돌려 확인했다.

| 항목 | 결과 |
|---|---|
| 길이 | **420.14초 (00:07:00.14)** — 목표 420초 |
| 영상 | h264 High · yuv420p · **bt709** · 24fps |
| 오디오 | AAC 48kHz 스테레오 |
| 자막 | mov_text · **language=kor** |
| 켄번스 20컷 | 통과 |
| 디졸브 2곳 | 통과 (핸들 보정 전 419.27초 → 보정 후 420.14초) |
| 베드 루프 | 통과 (10초 소스로 75초 구간 채움, 평균 −39.4 → −26.8dB) |

## ⛔ 남은 단 하나의 장애물
**미디어를 이 컨테이너로 가져올 수 없다.** `pikaso.cdnpk.net:443` 이 **조직 이그레스 정책**에 막혀 있다 (게이트웨이가 CONNECT 에 403). `creations_deliver` 가 주는 편집용 마스터 주소도 같은 호스트다.

확인된 사실:
- 일반 인터넷은 열려 있다 (PyPI 200)
- ffmpeg 7.0.2 확보 완료 (`pip install imageio-ffmpeg`; apt 는 패키지 인덱스가 깨져 실패)
- 필요한 필터 전부 존재 — zoompan · xfade · acrossfade · adelay · amix · loudnorm · subtitles · tpad
- 막힌 것은 **호스트 하나뿐**이다

→ **환경 네트워크 정책에서 `pikaso.cdnpk.net` 을 허용하면 위 명령 두 줄로 완성본이 나온다.**
→ 또는 62개 소스를 직접 받아 `media/` 에 넣어도 똑같이 동작한다.

## 아직 만들지 않은 소스
앰비언스 베드 7종과 SFX 7종은 생성하지 않았다. `audio_sfx_generate` 로 뽑을 수 있으나, 받아올 수 없는 상태에서 미리 만들 이유가 없어 보류했다. 지시서 §6에 구간별 dB 와 음향 설계가 이미 적혀 있다.
