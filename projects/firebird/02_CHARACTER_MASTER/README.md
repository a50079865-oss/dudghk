# 02_CHARACTER_MASTER — 캐릭터 마스터 시트 생성 기록

## 규격 (전 시트 공통 · QUALITY 모드)
| 항목 | 값 |
|---|---|
| MODEL | `gpt-2` (gpt-image-2) via Magnific |
| 해상도 | 2k · quality `high` |
| 비율 | 3:2 (가로 클린 그리드) |
| 패널 | **5개** — 정면(대형) · 3/4 · 측면 · 전신 · 표정 3컷 |
| 이미지 내 텍스트 | **패널 헤더만**. hex·콜아웃·리더선·측정치 금지 |
| 단가 | 600 크레딧 / 장 |

> 시트 방식 = **master-sheet-v2**(얼굴 일관성 최우선 · Seedance Element 주입용 클린 시트).
> 7단계 §36이 요구하는 소품 패널(herb satchel · medical knife · firebird mark · costume texture · longsword · wolf insignia)은
> 패널 6개 상한 때문에 이 시트에 넣지 않았다. → **얼굴 확정 후 별도 V1 디테일 시트**로 제작한다.

## v1 (2026-09-19) — 1안 테스트
| 인물 | 결과 |
|---|---|
| ELARA VAREN | https://www.magnific.com/app/creation/u5UaMOhQLD |
| RIVEN SKAEL | https://www.magnific.com/app/creation/ks9q8GO16B |

소비: 1,200 크레딧 (600 × 2). 생성 후 잔액 약 30,352.

> ⚠️ 결과 파일은 CDN 호스트가 이 실행 환경의 네트워크 정책에 막혀 저장소로 내려받지 못했다.
> 링크로 확인하고, 채택본은 사용자가 직접 내려받아 이 폴더에 `ELARA_VAREN_sheet_vN.png` 형식으로 보관한다.

### 적용된 캐논
- `19_VISUAL_PRODUCTION_BIBLE` §07 ELARA IDENTITY LOCK (**머리 = waist-length 확정본**) · §08 ELARA-A 의상
- `19_VISUAL_PRODUCTION_BIBLE` §10 RIVEN IDENTITY LOCK · §11 RIVEN-A 갑옷 · 북방 장검
- §02 NEGATIVE LOCK 전체 + 인물별 추가 금지(글래머 공주 금지 / 거대 늑대 문양 금지 / 왕자 갑옷 과장 금지)
- §35 일관성 우선순위 — 얼굴 > 나이 > 머리 > 체형 > 의상 > 표식 > 소품 > 배경

### 프롬프트 (재현용)
전문은 세션 기록 참조. 핵심 구조:
```
[SUBJECT] 이름/역할 + Appearance(IDENTICAL IN EVERY PANEL) + Main outfit(LOCKED) + Vibe/tone
[PANELS] 5개, 패널 헤더 텍스트만
[STYLE RULES] 포토리얼 / 전 패널 동일 / 헤더만 / 인물별 금지 / 공통 NEGATIVE LOCK
```

## 체크리스트 — 시트 채택 전 확인
- [ ] 5패널 전부에서 **얼굴이 동일 인물**인가
- [ ] **머리 길이가 허리까지**로 일관되는가 (엘라라)
- [ ] 리븐 — **흉터가 왼쪽 눈썹 위**인가, 전 패널 동일 위치인가
- [ ] 리븐 — **오른쪽 눈이 왼쪽보다 미세하게 좁은가**
- [ ] 눈이 **발광하지 않는가** (양쪽)
- [ ] 의상이 **새것처럼 보이지 않는가** — 해진 밑단·얼룩·손바느질·기운 자리
- [ ] 늑대 문양이 **작은가** (흉갑 전체를 덮지 않음)
- [ ] 이미지 내 텍스트가 **패널 헤더만**인가 (글자 깨짐 없는가)
- [ ] 엘라라가 **글래머 판타지 공주로 보이지 않는가**
- [ ] 애니·게임 렌더·현대 헤어·네온 없는가
