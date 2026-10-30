# WORLD_SHEETS v20261028 — 《불새의 왕국》 (작가 제공 · S23-2 공간 plate ref)

| 파일 | 장소 | 용도 |
|---|---|---|
| AUREVIA_sheet.png | 아우레비아 — 수도 솔라라 · 왕궁 · 불새 신전 · 시장 · 농촌 · **국경 마을** · 강 다리 · 신전 내부 | EP1·6 |
| AUREVIA_solara_hero.png | 솔라라 전경 | EP6 |
| AUREVIA_border_village_before.png | 국경 마을 벨렌(피난 직전, 예배당 종탑) | **파일럿 S02 plate** |
| AUREVIA_refugee_road.png | 피난 행렬 언덕길 | **파일럿 S02·S01 plate** |
| PILOT_burned_chapel_interior.png | 불탄 돌 예배당 내부 | **파일럿 S04~S08 plate** |
| PILOT_village_ash_sky.png | 불타는 마을 + 재 하늘 | **파일럿 S08 plate** |
| PILOT_hill_army_view.png | 언덕 위 군대 조망 | 파일럿 S09 plate (깃발 확인 필요) |
| SKELDRIA_sheet.png / SKELDRIA_skaelhold_hero.png | 스켈드리아 — 수도 스카엘홀드 | EP3 |
| DRAEVOR_sheet.png / DRAEVOR_vaerkar_hero.png | 드라에보르 — 수도 바에르카르 | EP4 |
| LYSARA_sheet.png / LYSARA_nerys_hero.png | 리사라 — 수도 네리스 | EP5 |
| ARCADIA_sheet.png / ARCADIA_ruins_hero.png | 고대 아르카디아 — 재의 왕관 원형실 · 지하 기록보관소 · 불탄 왕좌의 전당 | EP7·8 |

## 정본 명칭·팔레트 (시트 기준으로 바이블 갱신)
| 왕국 | 수도 | 상징 | 팔레트 |
|---|---|---|---|
| 아우레비아 Aurevia | 솔라라 Solara | 황금 불새 | Warm Ivory · Burnt Gold · Deep Crimson · Earth Brown |
| 스켈드리아 Skeldria | 스카엘홀드 Skaelhold | 백색 늑대 → **목에 쇠사슬을 두른 늑대**(차별화) | Charcoal Black · Frost Grey · Midnight Blue · Cold Silver |
| 드라에보르 Draevor | 바에르카르 Vaerkar | 검은 용 | Black Iron · Burnt Umber · Oxblood · Dark Copper |
| 리사라 Lysara | 네리스 Nerys | 은빛 해룡 | Deep Teal · Storm Grey · Weathered Silver · Pale Stone |
| 고대 아르카디아 | — | 원 안의 검/태양 기호 | Pale Stone · Blackened Bronze · Ash Grey · Faded Ivory |

- **스켈드리아 구호 교체(표절 차단):** "THE NORTH ENDURES" 사용 금지 → **"겨울은 끝나지 않지만, 우리는 살아간다."** / "A kingdom built not for beauty, but to survive the winter."
- **에린도르(Eryndor):** 네 왕국과 아르카디아가 있는 **대륙 이름** (사용자 확정 — 아르카디아 시트 'The First Kingdom of Eryndor'와 일치)
- **엘라라의 고향 마을:** **벨렌(Velen)** — 아우레비아 국경 마을, 불탄 돌 예배당 소재 (바렌 가문 성의 어원)
- **룩 노트:** 시트들은 골든아워·채도 높은 컨셉아트 톤. 파일럿 본 생성 시 plate는 **구조·건축 ref**로만 쓰고 색은 global_look(블리치 바이패스·재빛+앰버)로 덮는다.

## plate 사용 규칙 (S23 — 본 생성 시 프롬프트에 강제)
1. **십자가 금지:** 예배당 제단의 십자가·종탑 십자가 → **날개 편 청동 불새 부조 / 불꽃 제단 / 종탑 꼭대기 청동 불새**로 교체. 프롬프트에 `no Christian cross, no crucifix; the altar bears a bronze winged-firebird relief and a stone fire bowl` 상시 주입.
2. **사슴·별 깃발 금지:** `PILOT_hill_army_view.png`는 구도·지형만 참조. 깃발은 **스켈드리아 — 미드나잇 블루 바탕의 은빛 늑대, 목에 쇠사슬**. 프롬프트에 `no stag, no star sigil` 주입.
3. **스켈드리아 문장 공통:** 모든 늑대 문장은 목에 쇠사슬을 두른 형태(차별화 규칙 1 + EP3 셋업).
4. **색:** plate의 골든아워·고채도 색은 무시, global_look(블리치 바이패스 · 재빛+불씨 앰버) 우선.
