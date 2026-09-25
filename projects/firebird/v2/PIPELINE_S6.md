# 6단계 결과물: 스타일 / 세계관 레퍼런스 시트

> **분리 원칙 (master-sheet-v2 교훈 적용):** 이미지 = **보는 기준**, 이 문서 = **읽는 기준**.
> 스펙상 9개 구역 중 텍스트 중심 3개(환경 앵커 · 스타일 고정 · 피해야 할 방향)와 HEX 값은 이미지에 넣지 않는다 — 글자가 깨지고 생성이 실패한다. **여기 문서의 영문 문장들이 앞으로 모든 씬 프롬프트에 붙는다.**

---

## A. 이미지로 만드는 것 — `S6_WORLD_SHEET`

| 구역 | 내용 |
|---|---|
| **1. 메인 세계관** | 재가 눈처럼 내리는 흐린 평원, 진창길을 걷는 피난민 행렬, 연기 오르는 불탄 마을, 먼 산맥. 인물은 **작게**. 신화 없음 — **현실만** |
| **2. 주요 장소 5** | 아우레비아 변방 수용소(EP1) · 스켈드리아 설원과 빈 늑대 신전(EP3) · 드라에보르 화산 협곡과 광산(EP4) · 리사라 바다 위 절벽 도시(EP5) · 재의 평원(콜드오픈·EP7·EP8) |
| **3. 특수 상태** | **일반 화재 vs 아스렌의 불** 좌우 비교 — 신화가 현실을 끊고 들어오는 방식 |
| **4. 상징 5** | 재 위의 금 간 왕관 · 타지 않는 불꽃 문양 · 두 번 묶은 매듭 · 은빛 늑대 밀랍 봉인 · 유리 약병 |
| **5. 색감** | 견본 6칸 (HEX는 아래 문서) |
| **6. 조명 흐름** | 기본 · 전환 · 위기 · 클라이맥스 4칸 |

> **메인 세계관에 신화를 넣지 않은 이유:** 캐논 정의가 *"현실을 드물게 신화가 끊고 들어온다"* 이다. 기본값이 현실이어야 끊고 들어오는 게 보인다. 신화는 **특수 상태 구역에만** 둔다.

---

## B. 문서로 두는 것

### 색감 (HEX)

| 역할 | 이름 | HEX | 쓰임 |
|---|---|---|---|
| **메인** | 재 (Ash) | `#7A7874` | 전 시즌의 연결색. 모든 회차에 재가 있다 |
| **보조** | 강철 (Steel Slate) | `#3E4652` | 스켈드리아 · 리븐 · 갑옷 |
| **강조** | 불씨 (Ember) | `#9C3A22` | 일반 화재 · 피 · 성단의 진홍 |
| **특수** | 흰 열 (Asren White) | `#F1E8D6` | **아스렌의 불 중심에만.** 다른 곳에 쓰지 않는다 |
| **중립** | 진흙 (Mud) | `#4A3F35` | 땅 · 그림자 · 엘라라의 세계 |
| **예약** | 재생의 녹색 (Renewal Green) | `#6F7F5A` | ⛔ **EP8 재생 이후에만.** 그 전 95분간 자연 녹색 금지 |

**캐릭터 시트와의 연결:** 엘라라 시트 = 재·진흙 (EP1 아우레비아) / 리븐 시트 = 강철·재 (EP3 스켈드리아). **두 인물의 색이 두 나라의 색이다.** 둘이 같은 프레임에 들어오면 두 팔레트가 한 화면에서 만난다.

### 환경 앵커 (Environment Anchor) — 모든 씬 프롬프트에 붙인다

```
ENV-1  Late-medieval continent of Kasran, overcast sky, cold diffused daylight, fine grey ash drifting slowly like snow, wet churned mud underfoot.
ENV-2  Weathered pale stone, dark timber, stained canvas, rough wool and linen, blackened steel — nothing new, nothing clean, everything wet, scorched or frayed.
ENV-3  Desaturated ash grey and steel slate with mud-brown shadows; the only warm colour in frame is real firelight. Low-key, real darkness allowed.
ENV-4  When the firebird Asren is present: fire stops moving, ash rises instead of falling, flame cores turn ivory-white, motion slows by half a beat. Nothing glows, nothing sparkles.
ENV-5  Beautiful but brutal medieval reality, interrupted only rarely by overwhelming ancient myth.
```

> `ENV-4` 는 아스렌이 관여한 컷에만 붙인다. 나머지 4개는 **전 컷 공통.**

### 스타일 고정 (Visual Style Lock) — 모든 씬 프롬프트에 붙인다

```
STYLE-1  Photoreal live-action cinema. Not illustration, not anime, not 3D render, not concept painting.
STYLE-2  ARRI Alexa look: fine 35mm grain, black pro-mist, soft halation, crushed blacks, shallow depth of field with clear foreground/midground/background separation.
STYLE-3  Practical light sources only — overcast sky, winter sun, dawn, candle, hearth, oil lamp, narrow window. Low-key by default.
STYLE-4  Epic scale but cold: thriller-noir tension with the intimacy of melodrama. Grand, heavy, never glossy.
STYLE-5  11th–13th century European material culture: mail armour, wool, linen, leather, timber, stone. No plate armour.
```

### 피해야 할 방향 (AVOID) — 네거티브로 붙인다

```
AVOID  neon aura, glowing eyes, particle effects, magic sparkles, HUD or runes, glossy MMO rendering, plastic or plate armour, spikes, engraved ornament, modern hairstyles, superhero poses, decorative fantasy clutter, idol-perfect faces, clean new clothing, centered symmetrical composition, crowds with visible faces, readable in-image text, random letters, logos, watermarks, Japanese text, natural green vegetation (before EP8).
```

### 조명 흐름 — 감정과의 연결

| 구간 | 조명 | 감정 | 대표 회차 |
|---|---|---|---|
| **기본** | 흐린 하늘의 확산광, 그림자 없음 | 무감각 · 견딤 | EP1 전반 · EP2 |
| **전환** | 새벽의 차가운 청색 + 화덕의 주황 한 점 | 흔들림 · 가까워짐 | EP3 · EP5 |
| **위기** | 불빛 역광, 연기, 인물은 실루엣 | 공포 · 결정 | EP4 미드포인트 · EP6 |
| **클라이맥스** | **아스렌의 흰 열 + 상승하는 재** | 인식 · 전복 | EP8 |

---

## C. 이후 모든 씬 프롬프트의 조립 순서

```
[규칙 0-[A] 프리픽스]  →  [씬 내용]  →  [캐릭터: 정면 패널 참조 + 인물 문장]
→  ENV-1·2·3·5 (+ENV-4 해당 시)  →  STYLE-1~5  →  AVOID
```
