# EP1 1부 — 연속성 프롬프트 세트 (축·시선·인서트 소유권)
> 대상: 「재가 내리는 길」 62컷 · 16:9 · 이미지 = Nano Banana 2 (Magnific 웹, **무료**) · 영상 = Kling (1080p 450 / 720p 350, **유료**)
> 상위 문서: `27_EP01_PART1_EDIT_SHEET.md`(타임라인) · `23_EP01_PART1_ANGLE_MAP.md`(화각 배정) · `02_CHARACTER_MASTER/EP01_PART1_GENERATED.md`(생성 기록)
> 캐논 준수: `canon/02`·`canon/03`(외형 락 — **한 글자도 바꾸지 않는다**) · `canon/06`(비주얼) · `canon/07`(카메라) · `canon/11`(연속성 코드)

---

## 0. 이 문서가 고치는 것

사용자 지적: **"컷과 컷 간에 맥락이 없어, 개연성이."**

이 문서가 맡는 원인은 하나다 — **공간이 성립하지 않는다.** 62컷이 각각 독립 생성돼 **공유하는 축이 없다.**

| 증상 | 현재 상태 | 이 문서의 처방 |
|---|---|---|
| 시선이 안 맞는다 | C009↔C010, C017↔C018↔C019, C031↔C032, C035↔C036이 쿨레쇼프 쌍인데 좌우가 정의된 적이 없다 | §1 전역 아이라인 + 5개 축 그룹, §3 표로 못박음 |
| 축 파괴가 지시로 보장됐다 | "아이레벨·정직한 구도 전면 지양" → **정면 아이레벨 0컷**. 화면은 풍부해졌으나 좌우가 사라졌다 | §2에서 **인물 쌍에서만** 되돌린다. 풍경·군중·액션은 그대로 둔다 |
| 프레임 출입이 없다 | 62컷 전부 인물이 이미 자리에 있고 제자리로 끝난다 | §6-1 클린 플레이트·엣지 프레이밍(무료) + §6-3 영상 17클립 · START/END 키프레임 방식(유료 7,650) |
| 인서트가 주인이 없다 | C007·C015·C020이 스케일·각도·광원 연결 없이 자료화면으로 뜬다 | §5 인서트 처방 — 소유자의 신체 일부 + 동일 광원 + 3~4배 스케일 규칙 |

### 0-1. 예산의 비대칭 — 이 문서의 설계 원리

| 자원 | 단가 | 판정 |
|---|---|---|
| **나노 바나나 2 이미지** (Magnific 웹) | **0** | **무료 확정.** 몇 장을 요구해도 비용이 없다 |
| **Kling 영상** | **1080p 450 / 720p 350** | **유료 확정.** 잔액 31,926, 정지컷 영상화에 별도 배정분이 있어 **이 문서 몫은 5,000~10,000 가정** |

이 비대칭이 작업을 둘로 가른다.

> **① 축을 맞추는 일은 전부 이미지로 푼다.** 시선 방향 · 화면 내 위치 · 스케일 · 광원 방향은 **전부 이미지 단계에서 확정된다.** 무한히 시도할 수 있으므로 아끼지 않는다. 마음에 안 들면 다시 뽑는다.
> **② 영상 크레딧은 이미지로 못 푸는 것에만 쓴다.** 프레임 출입, 그리고 동작의 시작과 끝이 서로 다른 컷으로 이어지는 연결 — 그것뿐이다.
> **③ 영상은 반드시 시작·끝 프레임을 이미지로 먼저 뽑아 키프레임으로 물린다.** 이미지가 공짜이므로 한 클립에 2장을 쓰는 것이 **비용상 손해가 전혀 없고**, 대신 모션이 통제되어 **450씩 날아가는 재시도를 줄인다.** i2v 단일 스타트 프레임은 모델이 끝을 지어내므로 프레임 출입이 통제되지 않는다 — 이 문서에서 프레임 출입을 다루는 이상 **키프레임 2장이 기본값**이다.

---

## 1. 축 설계

### 1-0. 전역 마스터 아이라인 — 1부 전체를 지배하는 한 줄

> **리븐은 화면 왼쪽에 서서 오른쪽을 본다. 엘라라는 화면 오른쪽에 서서 왼쪽을 본다.**

두 사람은 1부에서 **한 번도 같은 프레임에 없다.** 그러나 62컷 내내 서로를 향해 보고 있다.
2부 첫 만남(`13_FIRST_MEETING_SCENE`)에서 이 축이 **그대로 맞물린다** — 리븐이 좌에서 들어오고 엘라라가 우에 서 있으면, 관객은 배운 적 없는 공간을 이미 알고 있다.

**이 규칙은 내가 만든 것이 아니라 이미 생성된 화면에서 읽어낸 것이다.**
- C009 — 노파 화면 좌, **엘라라 화면 우에서 좌를 본다** ✅
- C017 — 소년 화면 좌, **엘라라의 러스트레드 숄 어깨가 화면 우 전경** ✅
- C028 — **리븐 화면 좌 끝 / 마을 화면 우 끝** (편집 지시서가 "능선이 둘을 가른다"로 못박은 컷) ✅
- C035 — **리븐 사이드 프로필이 화면 우를 향한다** ✅

→ **네 컷이 이미 같은 말을 하고 있다.** 나머지를 여기에 맞추면 된다. 새 규칙이 아니라 **기존 자산에서 추출한 규칙**이다.

> ⚠️ 집행 전 **§7 거울 검증**을 먼저 돌린다. 기존 대사 클립 6개가 이 표와 반대로 움직이면, 그 그룹의 좌/우를 전부 뒤집어야 한다(프롬프트의 `SCREEN-LEFT`↔`SCREEN-RIGHT`만 치환하면 된다).

### 1-1. 축 그룹 5개

| 축 | 컷 범위 | 180도선의 정의 | 화면 좌 | 화면 우 | 키 광원 방향 |
|---|---|---|---|---|---|
| **AXIS-A 치료소** | C005–C022 (S02·S03) | 천막 아래 **부상자들이 누운 한 줄**. 카메라는 그 줄의 한쪽(남쪽)에만 선다 | 부상자 · 노파 · 소년 | **엘라라** | 새벽 해 — **카메라 좌측 후방 7~8시**, 천막 틈 갓레이 |
| **AXIS-B 능선** | C023–C028 (S04) | **능선 마루선**(좌→우). 카메라는 능선의 마을 쪽 사면에 있다 | **리븐** · 북방 기병대 · 북쪽 | 마을 · 저지대 · 브리스 | 차가운 아침 해 — **카메라 우측 낮게 4시** |
| **AXIS-C 초소** | C029–C039 (S05) | 무너진 **초소 담장선** | **리븐**(서 있음) | 브리스 · **요란**(땅에 누움) | 같은 아침 해 — **카메라 우측 4시**(AXIS-B와 동일 방향 유지 = 같은 아침) |
| **AXIS-D 예배당** | C040–C043 (S06) | **1점 투시 중심선**(좌우가 아니라 **깊이**가 축) | 벽화가 있는 좌측 벽 | 촛대 프랙티컬(전경) | 좁은 창 갓레이 — **화면 좌 상단에서 대각선 하강** |
| **AXIS-E 연기·습격** | C044–C061 (S07·S08) | **지평선**. 위협은 언제나 화면 좌(능선·북쪽 = C028의 리븐 쪽) | 연기 · 적 기병 진입 · 불 | **엘라라** · 도망치는 군중의 도착점 | S07 흐린 하늘 정광 → S08 **ember-red 화염이 카메라 좌측**에서 하드 키 |

> **AXIS-E의 설계 의도:** 군중은 전부 좌→우로 흐른다(위협에서 멀어진다). **엘라라만 왼쪽을 본다.** 흐름에 역행하는 단 하나의 인물 = 그녀의 아크 전체가 프레이밍 하나로 읽힌다.
> 그리고 그 왼쪽에는 C028의 리븐이 있었다. **그녀는 모르는 채로 그를 향해 보고 있다.**

### 1-2. 시선 고정표 (못박음 — 이 표를 벗어난 생성은 폐기)

| 컷 | 인물 | 화면 내 위치 | 시선 방향 | 짝 | 렌즈 | 키 광원 |
|---|---|---|---|---|---|---|
| C006 | 엘라라 | 우 2/3 | **좌·하** (부상자) | C007 | 50mm | 좌후방 |
| C007 | 엘라라의 손 | 프레임 중앙, 숄 자락 **우상단** | — (시선 없음) | C006 | 100mm | 좌후방 |
| C008 | 엘라라의 왼손 | 좌측 진입 | — | C007 | 100mm | 좌측 낮게 |
| **C009** | **노파** | **좌 1/3** | **우** (엘라라) | **C010** | 50mm | 좌후방 역광 림 |
| **C010** | **엘라라** | **우 1/3** | **좌·약간 하** — **렌즈를 보지 않는다** | **C009** | 85mm | 좌측 키 / 우측 네거티브필 |
| C011 | 엘라라 | **우 엣지에서 이탈 → 좌로** | 좌 | C012 | 50mm | 좌후방 역광 |
| C012 | 부상자 열 | 열이 좌→우로 뻗음 | — | C011 | 24mm | 좌후방 |
| C014 | 엘라라 | 우 1/3 | **좌·하** | C015 | 85mm | 좌측 키 |
| C015 | 대야·천 | 중앙 하단, **그녀의 손이 우에서 진입** | — | C014 | 100mm | 좌측 하드 |
| **C016** | **소년** | **좌 1/3** | **우·상** (엘라라) | C017 | 50mm | 좌후방 |
| **C017** | **엘라라(OTS)** | 어깨가 **우 전경** | 좌·하 | C016·C018 | 85mm | 좌측 키 |
| **C018** | **소년** | **좌 1/3** | **우·상** | **C017·C019** | 85mm | 좌후방 림 |
| **C019** | **엘라라** | **우 1/3** | **좌·하 → 정지** | **C018** | 85mm | 좌측 스플릿 |
| C020 | 두 손 | 소년의 손 **좌**, 엘라라의 손 **우** | — | C019 | 100mm | 좌측 |
| C021 | 엘라라 | **우에 서서 좌로 이탈** | 좌 | C022 | 85mm | 좌후방 역광 |
| C023 | 능선 | 마루선 좌→우 | — | C024 | 24mm | 우측 |
| C024 | 기병대 | **좌에서 진입 → 우로** | — | C025 | 24mm | 우측 |
| C025 | 말 다리 | **좌→우 이동** | — | C026 | 35mm | 우측 |
| **C026** | **리븐** | **좌 1/3** | **우·약간 하** | C027 | 85mm | **우측 키 / 좌측 네거티브필** |
| **C027** | 리븐+브리스 | **리븐 좌 / 브리스 우** | 서로 마주봄 | C026·C028 | 50mm | 우측 |
| **C028** | 리븐 / 마을 | **리븐 좌 끝 / 마을 우 끝** | 리븐 → 우 | — (기준 프레임) | 24mm | 우측 |
| C029 | 초소 잔해 | 담장선 좌→우 | — | C030 | 35mm | 우측 |
| C030 | 부상병들 | 좌→우로 누움 | — | C031 | 35mm | 우측 |
| **C031** | **브리스** | **우 1/3** | **좌** (리븐) | **C032** | 50mm | 우후방 림 |
| **C032** | **리븐** | **좌 1/3** | **우** | **C031** | 85mm | 우측 키 |
| **C033** | **요란** | **우 1/3, 땅에 누움** | **좌·상** | C034 | 85mm | 우측 위에서 |
| C034 | 리븐의 엄지·자루 | **좌 1/3**(리븐의 허리 높이) | — | C035 | 100mm | 우측 하드 |
| **C035** | **리븐** | **좌 1/3** | **우·하** | **C036** | 85mm | 우측 스플릿 |
| **C036** | **요란** | **우 1/3, 아래에서 올려다봄** | **좌·상** | **C035** | 85mm | 우측 역광(리븐이 실루엣) |
| C037 | 기병대 | **우→좌로 이탈** ⟵ **방향 반전 = 후퇴의 정의** | — | C038 | 35mm | 우측 |
| C039 | 요란의 손 | 우 1/3, 흙 | — | C040 | 100mm | 우측 하드 |
| C041 | 사제 | 깊이 축 끝 | 정면 아래(회중) | C042 | 50mm | 좌상단 갓레이 |
| C042 | 마을 사람들 | 전경 뒤통수 | 아래 | C043 | 35mm | 좌상단 |
| C043 | 벽화 | **좌측 벽** | — | C044 | 100mm | 좌상단 갓레이 |
| **C044** | **연기** | **화면 좌 1/3 지평선** | — | **C045** | 24mm | 정광 |
| **C045** | **엘라라** | **우 1/3** | **좌·상** (연기) | **C044·C046** | 85mm | 좌측 |
| C046 | 피난민들 | 군중 | **전부 좌·상** | C047 | 35mm | 좌측 |
| C047 | 연기 | **좌 1/3에서 커진다** | — | C048 | 24mm | 정광 |
| C048 | 적 기병 | **좌에서 진입 → 우로** | — | C049 | 24mm | 좌측 화염 |
| C050 | 군중 | **좌→우로 도주** | 우 | C051 | 35mm | 좌측 화염 |
| C051 | 엘라라 | 우 | **좌** (역행) | C052 | 50mm | 좌측 화염 |
| **C054** | **엘라라** | **우 1/3** | **좌** | C055 | 85mm | 좌측 화염 스플릿 |
| C056 | 약초 주머니 | 중앙 하단, 흙 | — | C057 | 100mm | 좌측 화염 |
| C058 | 엘라라 | **우에 정지, 군중이 그녀를 스쳐 우로 빠진다** | 좌 | C059 | 50mm | 좌측 화염 |
| C060 | 엘라라 | 우 1/3 | 좌 | C061 | 85mm | 좌측 화염 |
| C061 | 엘라라 | 중앙 | **좌·상으로 고개를 든다** | → 암전 | 85mm | 좌측 화염 |

---

## 2. 어디서 되돌리는가 — 트레이드오프 판단

이전 지시 **"로우앵글·하이앵글·더치앵글·탑뷰·드론샷을 적절히 섞고 아이레벨이나 정직한 구도는 모두 지양"** 은 화면을 풍부하게 만들었다. 전부 되돌릴 이유는 없다. **인물이 서로를 보는 쌍에서만** 되돌린다.

### 2-1. 되돌리는 것 (3가지, 이것만)

| # | 되돌림 | 대상 | 근거 |
|---|---|---|---|
| **R1** | **쌍 컷에서 탑다운·드론·오브젝트 POV 금지** | C020(현재 macro top-down) | 수직 부감은 **좌우가 존재하지 않는다.** 축을 정의할 수 없으므로 쌍에 쓸 수 없다 |
| **R2** | **쌍 컷에서 더치 각도 통일 또는 해제** | C019(dutch 30°) · C014(dutch) · C054(dutch) | 짝끼리 지평선 기울기가 다르면 **같은 공간으로 읽히지 않는다.** 쌍 안에서는 **같은 방향·같은 각도**의 더치만 허용. C019는 Wound 설치라 **더치 해제**(정지가 더 세다) |
| **R3** | **엘라라의 카메라 높이를 아이레벨로 복귀** | C010 · C014 · C019 · C045 · C054 · C060 | **캐논 07이 명시한다 — "Elara: mostly eye-level."** 화각 맵의 "정면 아이레벨 0컷"은 캐논 07 위반이었다. 단 **정면은 여전히 금지** — 아이레벨 **3/4**로 간다. 높이는 되돌리고 방향은 되돌리지 않는다 |

> **핵심 구분:** 문제는 "아이레벨"이 아니라 **"정면"** 이었다. 두 개가 한 문장에 묶여 함께 금지된 것이 사고였다. **높이는 공간을 만들고, 정면은 공간을 지운다.** 높이만 돌려받는다.

### 2-2. 지키는 것 (그대로 둔다)

- **풍경·군중·액션의 극단 화각 전부 유지** — C012 드론, C023 익스트림 로우, C029·C042 하이, C047·C059 에어리얼, C048 말발굽 높이, C055 버즈아이. 이들은 **짝이 없어 축을 깨지 않는다.**
- **리븐의 로우앵글 유지** — 캐논 07 "Riven early: slightly low-angle". 1부는 초반이므로 맞다.
- **요란의 하이앵글 유지** — C033. 약화 신호이자 리븐과의 **수직 권력차**가 곧 페이오프의 재료다.
- **인서트 매크로 전량 유지** — 단 §5의 소유권 처방을 얹는다.
- **C028 그대로 둔다.** 이 컷은 **문제가 아니라 기준**이다. AXIS-B·C 전체가 여기서 파생된다.

### 2-3. 대사 컷 6개는 클립을 다시 뽑는다

`29_EP01_PART1_SCRIPT`의 대사 컷 **6개(C009 · C017 · C027 · C031 · C035 · C041)** 는 후반 더빙 립싱크가 걸려 있어 **스틸로 대체할 수 없다.** 시선을 고치려면 **클립을 다시 뽑아야 한다.**

전 클립은 **무성**이다(편집 지시서 §6 — 사운드는 전부 후반에서 만든다). 따라서 클립 재생성이 음성을 건드리지 않는다. **6 × 450 = 2,700** — 배정 예산 안이다. **집행한다**(§6 V2 티어).

> 이 결정의 의미: 축을 **기존 자산에서 상속받는 것이 아니라 저작한다.** 여섯 개의 대사 컷이 축의 기준이 되므로, 상속에 기대는 §7 거울 검증은 **재생성하지 않는 컷에만** 적용된다.

### 2-4. 스틸로 남겨도 되는 리액션 컷 (판단 근거)

**C010 · C018 · C019 · C032 · C033 · C036 · C045** 는 **순수 리액션 홀드**이며, 스틸 + 2~3% 푸시인으로도 성립한다.

- 캐논 07이 인간 드라마에 *slow push-in · locked-off*를 명시 → 캐논 정합.
- C019는 편집 지시서가 **앰비언스 −60dB 완전 침묵**으로 설계한 컷이다. 정지 화면이 오히려 맞다.
- C018은 대본 §4가 **"자막 없음 · 들리지 않게 처리"** 로 확정 → 립싱크 불필요.

**다만 예산이 있으므로 선택지를 열어 둔다.** §6 V3 티어에 7클립(720p 기준 2,450)으로 올려두었다. 판단 기준은 하나다 — **"이 컷에서 눈꺼풀이 한 번 내려가는 것이 정보인가?"** C019(굳는다)와 C036(그를 본다)은 그렇다. 나머지 다섯은 아니다.
→ **권고: C019 · C036 두 컷만 클립화(900), 나머지 다섯은 스틸 유지.** 정지 컷 20 → 25 (62컷 중 40%), 연속 정지 없음.

---

## 3. 재생성 대상 목록 (우선순위)

> 이미지는 무료이므로 **장수 제한이 없다.** 그러나 **순서는 있다** — 앞 순위가 뒤 순위의 기준이 되므로 반드시 위에서부터 뽑는다.

### P0 — 축의 기준 프레임 (3장). **이것부터. 나머지가 여기에 맞춰진다**

| 순위 | 컷 | 이유 |
|---|---|---|
| 1 | **C005** | AXIS-A의 마스터. 부상자 열이 좌, 엘라라가 우, 광원이 좌후방임을 **한 프레임에서 확정**해야 S02·S03 13컷이 여기 붙는다 |
| 2 | **C029** | AXIS-C의 마스터. 담장선과 우측 광원을 확정 |
| 3 | **C012** | AXIS-A의 부감 확인용. 드론 탑다운이라 좌우는 없으나 **부상자 열의 방향**이 마스터와 일치해야 한다 |

> C028(AXIS-B 기준)·C040(AXIS-D 기준)은 **재생성하지 않는다.** 이미 축을 정의하고 있다.

### P1 — 쿨레쇼프 쌍 (10장). **여기가 사용자가 느낀 "개연성 없음"의 실체**

| 순위 | 컷 | 이유 |
|---|---|---|
| 4 | **C010** | 현재 렌즈를 정면으로 본다. 노파(C009)가 우를 보는데 엘라라가 좌를 보지 않으면 **두 사람은 다른 방에 있다** |
| 5 | **C018** | 소년이 우·상을 봐야 C017의 엘라라 OTS와 맞물린다. 현재 정면 |
| 6 | **C019** | Wound 설치. 시선이 C018의 소년에게 되돌아가지 않으면 **왜 굳는지 화면이 설명하지 못한다** |
| 7 | **C036** | "요란이 그를 본다" — **그를**이 화면에 정의돼 있지 않다. 좌·상 필수 |
| 8 | **C032** | 브리스(C031)가 좌를 보는데 리븐이 우를 보지 않으면 보고가 성립하지 않는다 |
| 9 | **C033** | 요란 페이오프 설치. C036과 **같은 위치·같은 광원**이어야 같은 사람으로 각인된다 |
| 10 | **C045** | 연기(C044)를 본다. 연기가 좌인데 그녀가 우를 보면 **본 것이 아니다** |
| 11 | **C016** | 소년의 첫 등장. C018과 같은 쪽·같은 광원이어야 같은 소년 |
| 12 | **C014** | C015 인서트의 소유자 지정. 더치를 풀고 좌·하를 본다 |
| 13 | **C046** | 군중 전체가 연기 쪽(좌·상)을 봐야 C045의 시선이 집단으로 확인된다 |

### P2 — 인서트 소유권 (6장). §5 처방 적용

| 순위 | 컷 | 이유 |
|---|---|---|
| 14 | **C007** | 손이 누구 손인지 화면에 없다. 숄 자락이 들어와야 엘라라의 것이 된다 |
| 15 | **C015** | 대야가 누구 대야인지 없다. 그녀의 손이 우에서 들어와야 한다 |
| 16 | **C020** | 탑다운이라 두 손의 좌우가 없다. 45° 사선으로 바꿔 **소년 좌 / 엘라라 우** 확정 |
| 17 | **C034** | 엄지 인서트가 C035와 같은 광원·같은 허리 높이여야 리븐의 것이 된다 |
| 18 | **C039** | 요란의 손. C033·C036과 같은 우측 광원 + 같은 진흙 |
| 19 | **C056** | 약초 주머니. C007·C015와 **같은 주머니·같은 스티치**여야 회수된다 |

### P3 — 흐름·광원 통일 (11장)

| 순위 | 컷 | 이유 |
|---|---|---|
| 20 | **C006** | 부상자를 좌로 옮긴다. AXIS-A의 인물 배치 확정 |
| 21 | **C044** | 연기를 화면 좌 1/3로 고정 |
| 22 | **C047** | 같은 좌측에서 커진다(현재 위치 불명) |
| 23 | **C054** | 좌측 화염 키 + 좌를 본다. 더치는 C019와 같은 방향만 |
| 24 | **C051** | 군중 흐름(좌→우)에 **역행**하는 유일한 인물로 프레이밍 |
| 25 | **C050** | 도주 흐름을 좌→우로 통일 |
| 26 | **C048** | 적 기병 진입을 좌→우로 통일 |
| 27 | **C060** | 좌측 화염 키 유지, 좌를 본다 |
| 28 | **C030** | 부상병들이 좌→우로 누움 (C029 담장선과 평행) |
| 29 | **C042** | 좌상단 갓레이 통일 |
| 30 | **C022** | 천막 틈 새벽빛이 **좌후방**에서 온다 — AXIS-A 광원의 마지막 확인 |

### P4 — 키프레임 자산 (신규 37장 — 전부 영상용 START/END 쌍과 클린 플레이트)

영상을 사는 컷은 **전부 START·END 두 장을 먼저 뽑는다**(§0-1 원리 ③). 이미지가 무료이므로 한 클립에 2장을 쓰는 것이 손해가 아니고, **모션이 통제되어 450짜리 재시도를 막는다.**

| 순위 | 코드 | 용도 |
|---|---|---|
| 31 | **CP-A** | 치료소 **클린 플레이트**(엘라라 없음). C005 직전 0.5초 삽입 → 다음 컷에 그녀가 있으면 **"들어왔다"로 읽힌다.** V1-1 클립의 END 프레임으로도 재사용 |
| 32 | **CP-C** | 초소 클린 플레이트(기병대 없음). C037 클립의 **END 프레임** 겸용 |
| 33 | **CP-E** | 골목 클린 플레이트(군중 없음). C058 클립의 END 참고 프레임 |
| 34 | **C011-S / C011-E** | START: 우 엣지에 반쯤 잘린 이행 자세 / END: 좌측 다음 환자 곁에 무릎 꿇은 자세 |
| 35 | **C021-S / C021-E** | START: 소년 곁에 앉은 자세 / END: 일어서서 좌 엣지로 절반 빠진 자세 |
| 36 | **C037-S / C037-E** | START: 선두가 좌 엣지에 걸린 순간 / END: 대열이 전부 빠진 빈 진흙땅(= CP-C) |
| 37 | **C058-S / C058-E** | START: 군중이 프레임을 채운 상태 / END: 군중이 우로 빠지고 그녀만 남은 프레임 |
| 38~52 | **V1~V3 티어 나머지 클립의 START/END 쌍** | §6의 클립 목록 참조. 각 클립당 2장 |

**합계 — 재생성 30장 + 신규 약 37장 = 약 67장. 전부 무료(0 크레딧).**
> 재생성 스틸(P0~P3)의 상당수가 그대로 클립의 **START 프레임**이 되므로, 실제 추가 작업은 **END 프레임 뽑기**다. 장수가 많아 보여도 설계는 이미 §1 표에 다 있다.

---

## 4. 프롬프트 전문

### 4-0. 공통 접두부 — 모든 프롬프트 맨 앞에 그대로 붙인다

`23_EP01_PART1_ANGLE_MAP` §전 컷 공통 주입 상수의 **VERBATIM 요약본**이 실제 생성에 쓰인 형태다. 그 마지막 줄만 **연속성 조항으로 교체**한다(§2-1 R1~R3의 집행 문구).

```text
PREFIX-CONT (VERBATIM — paste at the head of EVERY prompt below)

MANDATORY DRAMA IMAGE PREFIX:
— IDENTITY LOCK: render EXACTLY the same person(s) as the character-sheet reference — same face, age, hair, signature wardrobe. Never beautify, never average into a generic idol face.
— ARRI Alexa look — filmic latitude, gentle organic softness NOT clinical digital sharpness, fine 35mm grain, Black Pro-Mist halation bloom, anamorphic oval bokeh, crushed blacks, controlled low saturation, true chiaroscuro contrast, never flat video-look.
— Shallow depth of field, razor-thin focus plane, clear FG/MG/BG separation.
— LOW-KEY by default: deep controlled shadows, single motivated key, black negative fill.
— EP1 palette: Burnt Gold / Smoke Grey / Ember Red.
— CONTINUITY OVERRIDE (replaces the old "no eye-level" clause): keep a deliberate off-axis angle, but the 180-DEGREE AXIS OUTRANKS ANGLE VARIETY. The subject must sit on the designated side of frame and look toward the designated screen side. NEVER look into the lens. Camera height may be eye-level when the shot is half of a matched eyeline pair. No top-down and no drone framing on any paired shot. Dutch tilt only if the paired shot carries the same tilt direction and degree.
— NEGATIVE LOCK: no anime, no webtoon, no cartoon, no glossy game render, no MMO armor, no neon magic, no glowing fantasy eyes, no oversized shoulder armor, no spotless costumes, no plastic-looking metal, no modern hairstyles, no superhero poses, no excessive magical particles.
```

**인물 락 블록** (해당 인물이 나오는 프롬프트에 접두부 바로 뒤에 붙인다. `references[type=image]`로 시트도 함께 주입 — 엘라라 `Bh5pGDqoQR` · 리븐 `P3T7rNL42C`):

```text
ELARA-LOCK: ELARA VAREN, exactly 23, 168cm. Soft long-oval face with realistic natural
asymmetry, neutral-fair weathered skin with visible texture, faint freckles across nose and
upper cheeks, straight natural nose, restrained natural lips. Deep grey-green eyes with a
barely visible warm amber outer ring — NO glowing eyes. Dark chestnut-brown waist-length
naturally wavy hair in a practical loose low braid, imperfect strands escaping at temples and
cheeks. Slim practical build. COSTUME ELARA-A: warm ivory linen chemise, weathered
muted-brown wool overdress, faded rust-red wool shawl, dark leather belt with small herb
pouches, worn medical satchel, simple weathered leather boots. Hands: small healed cuts,
herb-stained fingertips, dry working skin, short practical nails. Almost no makeup.
She must never become a glamour fantasy princess.
```

```text
RIVEN-LOCK: RIVEN SKAEL, exactly 27, 188cm. Tall lean sword-trained physique, broad but
realistic shoulders, NOT bodybuilder-large. Angular-oval face, firm refined jaw, high
cheekbones, straight natural nose, cool-neutral fair skin. Deep steel-grey eyes, controlled
and observant — NO glowing eyes. Dark ash-blond shoulder-length hair in loose natural waves
covering the ears and touching the armour collar, 2–3 imperfect strands over the forehead —
no modern fade, no undercut, no gloss styling. Short faded old blade scar above one eyebrow,
always the same side as the master sheet. COSTUME RIVEN-A: functional blackened steel plate,
restrained aged-silver edge details, charcoal chainmail at the joints, dark padded arming
coat, faded midnight-blue wool cloak, worn dark leather gauntlets, practical sword belt,
extremely restrained small silver wolf insignia, high riding boots.
```

```text
SUPPORT-LOCKS (keep identical across every cut they appear in):
OLDWOMAN-A — Aurevian refugee woman about 70, weathered sun-lined face, deep vertical creases,
  thin white-grey hair under a coarse undyed wool kerchief, patched linen and brown wool,
  work-ruined hands with swollen knuckles.
BOY-A — Aurevian refugee boy about 9, dirt-streaked face with clean tear tracks, short matted
  dark-blond hair, patched ochre-brown wool tunic, bare feet wrapped in rags, thin wrists.
BRYS-A — BRYS HALEN, 24, Skeldrian mounted retainer. Plain blackened steel with NO silver
  edging (rank below Riven), mid-brown hair, young open face, mud on the cheekbone.
YORAN-A — YORAN, 19, Skeldrian wounded soldier. Pale, dark hair matted with mud, torn padded
  arming coat over charcoal chainmail, dark blood soaked through the left thigh wrap.
```

---

### P0 — 축 기준 프레임

#### C005 — 길가 임시 치료소 와이드 (AXIS-A 마스터)
```text
[PREFIX-CONT] [ELARA-LOCK]

SHOT C005 — establishing master of the roadside aid station. AURV-B01, dawn.
AXIS-A MASTER FRAME: a single row of wounded refugees lies head-to-foot along a line running
from the LEFT FOREGROUND into the RIGHT MIDGROUND, under a sagging canvas awning. The camera
stands on the near side of that row and NEVER crosses it for the rest of the sequence.
SCREEN POSITION: the wounded occupy the LEFT HALF of the frame. ELARA is in the RIGHT THIRD,
kneeling, small in the frame, her rust-red shawl the only warm accent on the right side.
EYELINE: Elara looks SCREEN-LEFT and DOWN at the nearest wounded man. Nobody looks at camera.
LENS: 35mm, high angle from about 2.5 metres, looking down the length of the row.
KEY LIGHT: low burnt-gold dawn sun entering from CAMERA-LEFT AND SLIGHTLY BEHIND (roughly
7–8 o'clock), through a torn gap in the canvas — visible volumetric god-rays and dust. The
wounded on the left are rim-lit from behind; the right side of the frame falls into smoke-grey
negative fill. This light direction is now locked for every cut from C005 to C022.
FG/MG/BG: FG — a blurred water bucket and rolled linen on a plank table at the bottom-left.
MG — the row of wounded and Elara. BG — the refugee road and grey ash-fall, defocused.
ATMOSPHERE: cold damp pre-sunrise air, woodsmoke, wet wool, the ground churned to mud.
```

#### C029 — 국경 초소 잔해 (AXIS-C 마스터)
```text
[PREFIX-CONT]

SHOT C029 — establishing master of the ruined border outpost, morning after.
AXIS-C MASTER FRAME: the collapsed palisade wall runs across the frame from LEFT to RIGHT and
defines the 180-degree line. The camera stays on the near side of it for C029–C039.
SCREEN POSITION: the standing Skeldrian riders and their horses hold the LEFT of frame; the
wounded and the debris field spread to the RIGHT. No faces readable at this distance.
LENS: 35mm, high angle looking down at the wreckage, bleach-bypass grade.
KEY LIGHT: pale cold morning sun low from CAMERA-RIGHT (roughly 4 o'clock), raking across
the splintered timber; black negative fill on camera-left. This direction is locked for
C029–C039 and is the SAME sun as AXIS-B — it must read as the same morning.
FG/MG/BG: FG — a splintered spear shaft crossing the bottom of frame, heavily defocused.
MG — the wall line and bodies. BG — bare winter hillside dissolving into smoke-grey haze.
ATMOSPHERE: frost still on the shadowed side of the timber, thin smoke lying flat on the ground.
```

#### C012 — 치료소 전경 드론 탑다운
```text
[PREFIX-CONT] [ELARA-LOCK]

SHOT C012 — the aid station seen from directly above. UNPAIRED SHOT — top-down is allowed here.
AXIS-A CONSISTENCY: the row of wounded must run LEFT-to-RIGHT across the frame in the same
orientation as C005, so the overhead view confirms the geography the audience just learned.
SCREEN POSITION: wounded fill the left two-thirds; ELARA is a single small figure at the RIGHT,
moving along the row from right toward left.
LENS: 24mm, true top-down bird's-eye, camera perpendicular to the ground, soft diffused light.
KEY LIGHT: the same burnt-gold dawn from CAMERA-LEFT — read as a long raking shadow cast by
each body toward the RIGHT of frame. Shadow direction is the continuity proof.
FG/MG/BG: awning ropes and canvas edge crossing the top-left corner; mud, blankets, bowls,
bloodied linen laid out in an ordered grid; trampled ground at the bottom.
ATMOSPHERE: order imposed on catastrophe — the rows are neat and that is the horror.
```

---

### P1 — 쿨레쇼프 쌍

#### C010 — 엘라라, 답하지 않는다 ★C009의 짝
```text
[PREFIX-CONT] [ELARA-LOCK]

SHOT C010 — Elara does not answer the old woman's question. REVERSE OF C009.
PAIRED WITH C009: in C009 the old woman sits in the LEFT third and looks SCREEN-RIGHT.
This shot is its exact counterpart and must interlock with it.
SCREEN POSITION: ELARA occupies the RIGHT THIRD of the frame. Empty defocused space on the
left — the space the old woman would be in. Her body is angled three-quarters away from camera.
EYELINE: she looks SCREEN-LEFT and very slightly DOWN, at a point just outside the left frame
edge at roughly chest height. SHE DOES NOT LOOK INTO THE LENS. Her gaze stays down at the
bandage in her hands for the first beat, then lifts only to the left edge, never to camera.
LENS: 85mm telephoto three-quarter close-up, camera at her EYE LEVEL (canon 07: Elara mostly
eye-level), offset about 25 degrees to her right so the framing is never dead-on frontal.
Background melts to creamy anamorphic bokeh.
KEY LIGHT: burnt-gold dawn key from CAMERA-LEFT (7–8 o'clock) landing on the side of her face
she is turned toward; black negative fill on camera-right sculpts the near cheek into shadow.
Split-light discipline: the far cheek lit, the near cheek dark.
EXPRESSION: E1 neutral / observant with a held breath. No defiance, no sadness — refusal by
stillness. The answer she withholds must be readable as a decision, not as distraction.
FG/MG/BG: FG — an out-of-focus grey wool kerchief shoulder entering the extreme LEFT edge
(the old woman's presence, unmistakable but unfocused). MG — Elara. BG — canvas and god-rays.
PROPS: half-wound linen bandage in her hands, herb-stained fingertips visible.
```

#### C016 — 소년 환자, 울고 있다
```text
[PREFIX-CONT] [BOY-A from SUPPORT-LOCKS]

SHOT C016 — the crying boy patient. FIRST APPEARANCE — this frame defines him for C018 and for
the whole season payoff, so his side of frame and his light are locked from here.
SCREEN POSITION: the BOY lies in straw in the LEFT THIRD of frame, body running away from
camera toward the upper-left, head nearest camera.
EYELINE: he looks SCREEN-RIGHT and UP — toward where Elara will be. He is crying without sound,
mouth closed, chest hitching. NEVER at the lens.
LENS: 50mm, high angle looking down at about 40 degrees — he is diminished by the camera
(this angle stays: an unpaired establishing look at him).
KEY LIGHT: burnt-gold dawn from CAMERA-LEFT AND BEHIND — a hard rim along the top of his
shoulder and the edge of his hair; his face is in low-key shadow with only bounce from the
straw. Black negative fill camera-right.
FG/MG/BG: FG — straw stalks crossing the bottom of frame, badly out of focus. MG — the boy.
BG — canvas wall and a defocused row of blanketed bodies receding.
DETAIL: clean tear tracks through the dirt on both cheeks; a rag-wrapped foot at the frame edge.
```

#### C018 — 소년이 답한다 ★C017의 짝 (자막 없음 · 들리지 않는다)
```text
[PREFIX-CONT] [BOY-A from SUPPORT-LOCKS]

SHOT C018 — the boy answers. The audience must NOT hear the name; only see the mouth move.
PAIRED WITH C017: in C017 we are over ELARA's RIGHT-FOREGROUND shoulder looking SCREEN-LEFT
at the boy. This shot is the exact reverse and must interlock with it.
SCREEN POSITION: the BOY sits up slightly in the LEFT THIRD of frame, the right two-thirds
given to the defocused space where Elara is.
EYELINE: he looks SCREEN-RIGHT and UP, at a point just past the right frame edge at standing
head height — Elara is kneeling-tall above him. NEVER into the lens.
LENS: 85mm telephoto demai close-up, camera LOW, at the boy's own chest height looking slightly
up at him so his answer carries weight. Background fully melted.
KEY LIGHT: the same burnt-gold dawn from CAMERA-LEFT AND BEHIND as C016 — identical rim on the
same shoulder, same negative fill on camera-right. He must read as the same boy in the same
five minutes as C016, not as a new setup.
EXPRESSION: mouth opening on a short word, eyes still wet, a child telling an adult something
ordinary. No performance of tragedy.
FG/MG/BG: FG — a sliver of rust-red wool at the extreme RIGHT edge, out of focus (Elara's shawl,
the same fabric as C017's shoulder). MG — the boy. BG — straw and canvas.
```

#### C019 — 엘라라가 잠깐 굳는다 ★Wound 설치 · C018의 짝
```text
[PREFIX-CONT] [ELARA-LOCK]

SHOT C019 — Elara freezes for a beat when she hears the name. THE WOUND IS PLANTED HERE.
PAIRED WITH C018: the boy sits LEFT and looks SCREEN-RIGHT and UP. This is his reverse.
DUTCH RELEASED: the previously assigned 30-degree dutch is REMOVED. A tilted horizon reads as
the camera's opinion; this beat needs the world to stay level while she stops. Level horizon.
SCREEN POSITION: ELARA in the RIGHT THIRD, kneeling, upper body squared, hands still in the
act of tying off a bandage — the hands must be MID-ACTION and then stopped.
EYELINE: she looks SCREEN-LEFT and DOWN toward the boy's face, at a point just outside the left
frame edge at low height. Then her focus goes THROUGH him — the eyes lose their fix while the
head does not move. NEVER at the lens.
LENS: 85mm telephoto close-up, camera at her EYE LEVEL, offset about 20 degrees off-axis to her
right. Razor-thin focus on the near eye only.
KEY LIGHT: split lighting — key from EXACTLY 90 degrees CAMERA-LEFT, the far half of her face
lit, the near half in total darkness. Same burnt-gold dawn source as the whole sequence, just
harder and more lateral. Black negative fill camera-right.
EXPRESSION: E6 grief held under E1 neutrality. Micro-expression only: a single blink that does
not complete, jaw set, breath stopped. NO tears, no trembling lip. The stillness IS the event.
FG/MG/BG: FG — a blurred straw edge at the left. MG — her face. BG — canvas, god-rays, nothing
readable. The frame must be so quiet that the edit's −60dB silence lands on it.
```

#### C032 — 리븐, 계산하는 얼굴 ★C031의 짝
```text
[PREFIX-CONT] [RIVEN-LOCK]

SHOT C032 — Riven receives the count. He is doing arithmetic on people.
PAIRED WITH C031: Brys stands in the RIGHT third and looks SCREEN-LEFT. This is his reverse.
SCREEN POSITION: RIVEN in the LEFT THIRD of frame, mounted or standing tall, the right
two-thirds left to the defocused wreckage where Brys stands.
EYELINE: he looks SCREEN-RIGHT, level, at a point just past the right frame edge. NEVER at lens.
He does not turn his head to look — the eyes move first and the head follows a half beat later.
LENS: 85mm telephoto demai close-up, camera SLIGHTLY LOW (canon 07: Riven early = slightly
low-angle), about 15 degrees below his eye line and 25 degrees off-axis to his left.
KEY LIGHT: pale cold morning sun low from CAMERA-RIGHT (4 o'clock) — the lit side of his face
is the side he is looking toward; black negative fill on camera-left crushes the near cheek.
Identical direction to C026, C028, C035. Smoke-grey bounce from the frost below.
EXPRESSION: R1 neutral command shading into calculation. Absolutely no anger. The eyes flick
once — a count being taken — and settle. Four men is a number, not four men.
FG/MG/BG: FG — a defocused splintered palisade stake crossing the lower LEFT. MG — his face,
midnight-blue cloak edge. BG — flat morning haze, the outpost reduced to shapes.
```

#### C033 — 요란의 얼굴 ★페이오프 설치
```text
[PREFIX-CONT] [YORAN-A from SUPPORT-LOCKS]

SHOT C033 — Yoran's face. THE SEASON PAYOFF IS PLANTED HERE. This frame defines his side of
the axis and his light for C036 and C039, and for his return in S10/S25/S30.
SCREEN POSITION: YORAN lies on his back in the RIGHT THIRD of frame, head nearest camera,
body running away toward the upper-right. The LEFT of frame is the empty space Riven occupies.
EYELINE: he looks SCREEN-LEFT and UP, at a standing man's head height just past the left frame
edge. NEVER at the lens. His focus is fighting to hold.
LENS: 85mm telephoto close-up, HIGH ANGLE looking down at about 35 degrees — he is diminished,
and that vertical power gap is exactly what pays off later. This angle STAYS.
KEY LIGHT: cold morning sun from CAMERA-RIGHT (4 o'clock) falling across his face from the
side he is turned away from; black negative fill on camera-left, so the direction he is looking
is the direction of darkness. Same sun as C029/C032/C035.
EXPRESSION: nineteen years old and not yet certain he is dying. Mud, sweat, and one clear line
where a tear has run sideways into the hair. Mouth slightly open, shallow breathing.
FG/MG/BG: FG — frost-stiff grass blades at the bottom-right, heavily defocused. MG — his face.
BG — churned mud and a fallen shield, unreadable. Do not show the wound here; C039 owns it.
```

#### C036 — 요란이 그를 본다 ★C035의 짝
```text
[PREFIX-CONT] [YORAN-A from SUPPORT-LOCKS] [RIVEN-LOCK for the silhouette only]

SHOT C036 — Yoran watches Riven give the order to withdraw. He is being left.
PAIRED WITH C035: Riven is in the LEFT third in side profile looking SCREEN-RIGHT and DOWN.
This is his exact reverse, from the ground.
SCREEN POSITION: the frame belongs to YORAN in the RIGHT THIRD, but the upper LEFT corner is
occupied by RIVEN'S SILHOUETTE — head, shoulder and cloak edge only, hard-backlit, no facial
detail, no more than a fifth of the frame. Identity ref still applies to that silhouette.
EYELINE: Yoran looks SCREEN-LEFT and UP, directly at that silhouette. The two eyelines meet
across the cut — this is the single most important eyeline match in the sequence.
LENS: 85mm, EXTREME LOW — camera at ground level beside Yoran's head, roughly a Yoran-POV
height, looking up past him. Keep the horizon level; no dutch.
KEY LIGHT: hard rim backlight from CAMERA-RIGHT behind Riven, so Riven reads as a black cutout
against a pale smoke-grey sky and Yoran's face catches only the spill. Same 4 o'clock sun.
EXPRESSION: no accusation. Recognition. He understands the arithmetic and does not argue.
FG/MG/BG: FG — a blade of frost grass and a strand of Yoran's mud-matted hair crossing the lens.
MG — Yoran's face. BG — the silhouette and flat sky. Nothing else may enter the frame.
```

#### C045 — 엘라라가 고개를 든다 ★C044의 짝
```text
[PREFIX-CONT] [ELARA-LOCK]

SHOT C045 — Elara looks up and sees the smoke. FIRST TIME SHE LOOKS AT THE HORIZON.
PAIRED WITH C044 and C047: the black smoke column stands in the LEFT THIRD of the horizon.
Her eyeline must travel to it.
SCREEN POSITION: ELARA in the RIGHT THIRD of frame, standing, three-quarters away from camera.
EYELINE: she looks SCREEN-LEFT and UP, at roughly 20 degrees above the horizon — the exact
height of the smoke column in C044. NEVER at the lens.
LENS: 85mm close-up, camera at her EYE LEVEL or a hair below, offset about 25 degrees off-axis.
KEY LIGHT: flat overcast daylight with a weak burnt-gold break from CAMERA-LEFT; black negative
fill on camera-right. The left side of her face is lit because the fire is on the left. From
here to the end of Part 1, EVERY key light on Elara comes from screen-left.
EXPRESSION: E1 observant turning into E4 fear held back — the transition happens in the eyes,
not the mouth. She does not gasp. Her hands stop first, then her eyes go up.
FG/MG/BG: FG — a defocused bandage roll still in her hand at the bottom-right. MG — her face
and the rust-red shawl. BG — grey ash-fall sky and, far out of focus, a hint of dark column
at the upper-left so the geography is confirmed inside a single frame.
```

#### C046 — 피난민들이 웅성인다
```text
[PREFIX-CONT]

SHOT C046 — the refugee crowd turns toward the smoke. Group confirmation of C045's eyeline.
SCREEN POSITION: a crowd of twenty to thirty Aurevian refugees fills the frame, mostly seen
three-quarters from behind and from the side.
EYELINE: EVERY head in the crowd is turned SCREEN-LEFT and UP, toward the same point outside
the left frame edge. A single child in the midground is the only one facing the other way.
LENS: 35mm, high angle from above the crowd, soft diffused light — an unpaired group shot, so
the high angle stays.
KEY LIGHT: overcast top light with a weak warm break from CAMERA-LEFT; faces catch it on their
left cheeks, confirming the fire's direction without showing the fire.
FG/MG/BG: FG — defocused shoulders and a bundled sack. MG — the turning crowd. BG — carts,
oxen, the road, ash falling.
ATMOSPHERE: the sound of talking stopping, not starting. Blankets, patched wool, mud.
DETAIL: one dropped tin cup rolling in the mud, incidental, never centred.
```

#### C014 — 엘라라 CU, 지친 눈 (C015 인서트의 소유자 지정)
```text
[PREFIX-CONT] [ELARA-LOCK]

SHOT C014 — Elara's exhaustion. This shot must OWN the insert that follows it (C015).
DUTCH RELEASED: the previously assigned dutch tilt is removed; horizon level.
SCREEN POSITION: ELARA in the RIGHT THIRD, three-quarters away from camera.
EYELINE: SCREEN-LEFT and DOWN, into the basin that C015 will cut to. The next cut must feel
like the continuation of this look — so the downward angle of her gaze must be steep.
LENS: 85mm close-up, camera at EYE LEVEL, offset 20 degrees off-axis to her right.
KEY LIGHT: Rembrandt — key from CAMERA-LEFT at 45 degrees side-above, a small triangle of light
on the shadow-side cheek; black negative fill camera-right. Same burnt-gold dawn source.
EXPRESSION: E1 with the fatigue underneath. Reddened lower lids, dry lips, one loose strand
stuck to her cheek. Do not make her cry — she is past that.
FG/MG/BG: FG — the blurred rim of a brass basin entering the BOTTOM-LEFT corner. This basin is
the same basin as C015 and must match in metal, dent and water line. MG — her face.
BG — canvas, god-rays, a defocused row of bodies.
```

---

### P2 — 인서트 (처방은 §5 참조)

#### C007 — 손 인서트 (엘라라의 것)
```text
[PREFIX-CONT] [ELARA-LOCK — hands only, face out of frame]

SHOT C007 — INSERT: Elara's hands winding a bandage. This insert must be unmistakably HERS.
OWNERSHIP RULE: a defocused fringe of FADED RUST-RED WOOL (her shawl) hangs into the frame
from the UPPER-RIGHT corner — she is on the right of the axis, so her body enters from the
right. The patient's forearm enters from the LEFT. The axis survives inside the macro.
SCALE: her hands fill about one third of the frame height — roughly three to four times the
size they read at in C006, so the cut lands as a move closer, not as a different location.
LENS: 100mm macro, camera looking down over her right shoulder at about 45 degrees — NOT
top-down. A top-down insert has no left and no right and cannot belong to anyone.
KEY LIGHT: hard burnt-gold dawn from CAMERA-LEFT (7–8 o'clock), identical to C006 — the
bandage catches a hard edge on its left side and casts a razor shadow to the right. Black
negative fill camera-right.
DETAIL (canon hands): small healed cuts across the knuckles, herb-stained fingertips, dry
working skin, short practical nails, a thin line of dried blood under one nail.
PROPS: coarse undyed linen bandage, a small herb pouch with visible hand-stitching at the
frame edge — THE SAME POUCH that will be recovered in C056.
FG/MG/BG: FG — shawl fringe upper-right, defocused. MG — the hands and the forearm.
BG — straw and mud, melted to nothing.
```

#### C015 — 피 묻은 천이 대야에 (씬 종결 푼크툼)
```text
[PREFIX-CONT] [ELARA-LOCK — hand only]

SHOT C015 — INSERT: a blood-soaked cloth released into a basin of water. Closes S02.
OWNERSHIP RULE: HER HAND enters from the RIGHT of frame holding the cloth and opens — herb
stains, healed knuckle cuts, short nails, the ivory linen cuff of her chemise at the wrist.
The hand must arrive from the right because that is her side of the axis. It withdraws to the
right and leaves the frame, so the shot ends as an empty basin.
SCALE: the basin fills the frame edge to edge; the cloth is roughly a quarter of the frame.
This is the closest the sequence has come — a full step in from C014.
LENS: 100mm macro, camera at a 60-degree oblique above the water — NOT straight down and NOT
from inside the basin. The water surface must still show a horizon line so the space is legible.
KEY LIGHT: one hard burnt-gold source from CAMERA-LEFT, raking the water; the cloth's shadow
falls to the right. Identical source and direction to C014's Rembrandt key, harder.
THE PUNCTUM: the blood does not billow dramatically. It sinks in one slow heavy fold, and the
water goes from clear to unreadable in about a second. Ember-red into smoke-grey — the episode
palette enacted in one object.
CONTINUITY: same dented brass basin, same water line, same plank table as C014's foreground.
FG/MG/BG: FG — the basin rim, defocused. MG — the water surface. BG — nothing; let it go black.
```

#### C020 — 소년의 손을 잡은 그녀의 손
```text
[PREFIX-CONT] [ELARA-LOCK — hand only] [BOY-A — hand only]

SHOT C020 — INSERT: her hand closing over the boy's hand. TOP-DOWN IS REVOKED FOR THIS SHOT.
OWNERSHIP RULE: THE BOY'S HAND comes from the LEFT (his side of the axis) — small, dirty
fingernails, a thin wrist, a patched ochre-brown wool cuff. HER HAND comes from the RIGHT —
larger, herb-stained fingertips, healed cuts, warm ivory linen cuff. Left is the patient, right
is the healer. This is the same left/right that has governed every cut since C005.
SCALE: the two hands fill two thirds of the frame width — a clear step in from C019, where her
hands read at roughly a quarter of that size.
LENS: 100mm macro, camera at a 45-degree LOW OBLIQUE from Elara's side, looking slightly across
and down. Straight-down framing is forbidden here: it erases the axis and makes the gesture
belong to nobody.
KEY LIGHT: soft diffused burnt-gold dawn from CAMERA-LEFT — the boy's hand is rim-lit on its
left edge, hers is keyed on the back of the knuckles, and the seam between them is where the
light dies. Black negative fill camera-right. Same source as C019's split key, diffused.
EXPRESSION IN THE HANDS: she closes over his, does not squeeze. His fingers do not close back
for a beat, then do, weakly. One beat of delay — that delay is the shot.
FG/MG/BG: FG — straw stalks crossing the bottom-left, defocused. MG — the two hands.
BG — blanket wool and darkness.
```

#### C034 — 푼크툼: 엄지가 검 자루를 두 번 누른다
```text
[PREFIX-CONT] [RIVEN-LOCK — gauntlet and sword only]

SHOT C034 — INSERT: Riven's thumb presses the same spot on the sword grip, twice.
This is the character's signature gesture (#punctum-thumb-hilt) and it must be recoverable in
every later episode, so the angle and the light are locked here permanently.
OWNERSHIP RULE: the frame holds his LEFT hip and the sword belt — worn dark leather gauntlet,
charcoal chainmail at the wrist, the faded midnight-blue cloak edge behind. A sliver of the
blackened steel plate on his thigh sits in the UPPER-LEFT corner: he is on the left of the
axis, so his body fills the left of the insert.
SCALE: the grip fills half the frame height. Roughly four times its size in C032.
LENS: 100mm macro, camera at HIS WAIST HEIGHT, from slightly in front and to his right,
looking at the grip across the body — never top-down, never from behind.
KEY LIGHT: hard cold morning sun from CAMERA-RIGHT (4 o'clock) catching the aged-steel
crossguard with a single specular line; the leather grip stays in deep shadow. Identical
direction and hardness to C032 and C035. Black negative fill camera-left.
DETAIL: the leather of the grip is darker and slightly polished at exactly the spot the thumb
touches — the habit has worn a mark into the weapon. Visible battle scratches on the crossguard.
NO glowing runes, no giant blade.
FG/MG/BG: FG — cloak wool, defocused, lower-right. MG — the grip and thumb. BG — frost-white
ground, blown to nothing.
```

#### C039 — 요란의 손이 흙을 쥔다
```text
[PREFIX-CONT] [YORAN-A — hand only]

SHOT C039 — INSERT: Yoran's hand closes on the earth. 18-second hold, closes S05.
OWNERSHIP RULE: the frame holds his hand, his chainmail cuff, and the torn padded arming-coat
sleeve — the SAME mud, the SAME frost grass, the SAME blood tone as C033 and C036. His hand
comes from the RIGHT of frame, his side of the axis. In the far defocused LEFT background, the
last pale shape of a departing horse is barely legible — the thing he is being left by.
SCALE: the hand fills a third of the frame. A step in from C036, not a new place.
LENS: 100mm macro at GROUND LEVEL, camera lying in the mud beside the hand, a shallow oblique
across the ground — the same ground-level eye we took in C036.
KEY LIGHT: hard cold sun from CAMERA-RIGHT (4 o'clock), raking across the churned earth so
every ridge of mud throws a long shadow to the left. Identical to C029/C033/C036.
THE GESTURE: the fingers dig in, close, and hold. They do not release. There is no fist of
rage — it is the grip of somebody holding on to the world.
DETAIL: frost crystals surviving in the shadowed side of a mud ridge; blood on the knuckles
that is not his own; one blade of grass bent under the thumb and not broken.
FG/MG/BG: FG — out-of-focus mud ridge. MG — the hand. BG — the pale departing shape, unreadable.
```

#### C056 — 흙바닥에 떨어진 약초 주머니 ★회수
```text
[PREFIX-CONT]

SHOT C056 — INSERT: Elara's herb pouch lying in the mud of the burning village. Payoff of C007.
OWNERSHIP RULE: it must be THE SAME POUCH seen at the edge of C007 and on her belt in C006,
C014 and C051 — same coarse undyed linen, same hand-stitching, same worn drawstring, same size,
same frayed corner. A recovered prop that is not literally identical does not recover anything.
The torn belt loop is still attached: it did not fall, it was pulled off.
SCALE: the pouch fills a third of the frame. Spilled dried herbs scatter to the LEFT.
LENS: 100mm macro insert, locked-off, low oblique from about 20 degrees above the ground —
the SAME family of angle as C007, so the two read as the same object photographed twice.
KEY LIGHT: hard ember-red firelight from CAMERA-LEFT, flickering, with a cold smoke-grey
ambient from above. This inverts C007's burnt-gold dawn from the same direction — the light
has the same address and a different temperature. That is the whole meaning of the shot.
DETAIL: a bootprint half across the pouch; one dried sprig unburnt and still green, incidental.
FG/MG/BG: FG — defocused embers drifting through the bottom of frame. MG — the pouch.
BG — a blurred wall of ember-red, no readable architecture.
```

---

### P3 — 흐름·광원 통일 (주요분)

#### C006 — 엘라라가 붕대를 감는다
```text
[PREFIX-CONT] [ELARA-LOCK]

SHOT C006 — Elara binding a wounded man's arm. Establishes her body on the RIGHT of AXIS-A.
SCREEN POSITION: the WOUNDED MAN lies in the LEFT HALF of frame, head toward camera-left.
ELARA kneels in the RIGHT THIRD, turned three-quarters away from camera toward him.
EYELINE: SCREEN-LEFT and DOWN, at her own hands and then at his face. NEVER at the lens.
LENS: 50mm two-figure framing (canon 07: 50mm for human relation), camera at a LOW
three-quarter from her right, about 20 degrees below her eye line.
KEY LIGHT: burnt-gold dawn from CAMERA-LEFT AND BEHIND (7–8 o'clock) through the canvas gap;
the wounded man is rim-lit from behind, Elara is keyed on the far side of her face; black
negative fill on camera-right. Motivated practical: a small oil lamp on the plank table,
also camera-left, so the two sources agree.
FG/MG/BG: FG — defocused straw and a water bucket lower-left. MG — the two figures.
BG — god-rays, canvas, the receding row of bodies.
PROPS: her medical satchel open on the ground at her right knee; the herb pouch (C007/C056)
visible on her belt; the dented brass basin (C014/C015) on the plank table behind her.
```

#### C044 — 지평선의 검은 연기
```text
[PREFIX-CONT]

SHOT C044 — a black smoke column on the horizon. The geography of the threat is fixed here.
SCREEN POSITION: the smoke column stands in the LEFT THIRD of frame, rising from behind a low
ridge — THE SAME RIDGE LINE seen in C023 and C028, so the audience places the fire where the
northern cavalry was. The remaining two-thirds of frame is empty grey sky and pale grassland.
LENS: 24mm wide, dutch tilt retained (unpaired landscape — the tilt is allowed), horizon low
in frame at about one third from the bottom.
KEY LIGHT: flat overcast daylight, cold. The smoke is the only black in a smoke-grey frame.
FG/MG/BG: FG — dry winter grass heads crossing the bottom edge, defocused. MG — the fields and
the road. BG — ridge line and the column.
ATMOSPHERE: no wind at ground level; the column goes straight up and then bends. Ash falling.
NOTE: C047 is the same frame from the same position with the column roughly doubled in width
and a second, smaller column appearing beside it, still LEFT of centre. Do not move the camera.
```

#### C054 — 엘라라, 공포를 누른다 (E4)
```text
[PREFIX-CONT] [ELARA-LOCK]

SHOT C054 — Elara holds her fear down while the village burns.
DUTCH: retained, but LOCKED TO THE SAME DIRECTION AND DEGREE as C019 — roughly 15 degrees,
tilting down to the left. A dutch that changes direction between her close-ups makes them read
as different films.
SCREEN POSITION: ELARA in the RIGHT THIRD, body angled three-quarters away from camera.
EYELINE: SCREEN-LEFT, level to slightly up — toward the fire, against the direction everyone
else is running. NEVER at the lens.
LENS: 85mm close-up, camera at EYE LEVEL, offset 25 degrees off-axis to her right.
KEY LIGHT: hard ember-red motivated firelight from CAMERA-LEFT, flickering, split across her
face so the far half is lit ember and the near half is crushed black; cold smoke-grey ambient
from above. Same left-side source as C045, C051, C056, C058, C060.
EXPRESSION: E4 fear held back. The fear is in the breathing and the neck, not the face. Soot on
one cheekbone, hair pulling loose from the braid, jaw locked.
FG/MG/BG: FG — an out-of-focus running figure crossing LEFT TO RIGHT through the near plane,
blurred by motion — the crowd flows past her while she stays. MG — her face.
BG — ember-red bloom, no readable architecture.
```

---

### P4 — 프레임 출입 자산 · 키프레임 (신규)

#### CP-A — 치료소 클린 플레이트 (인물 없음)
```text
[PREFIX-CONT]

SHOT CP-A — CLEAN PLATE of the aid station. EXACTLY the frame of C005 with NO Elara in it.
PURPOSE: cut this for 0.5–0.8 seconds immediately before C005. When she appears in the next
frame, the audience reads it as an ENTRANCE — a still image doing the work of a frame entry.
REQUIREMENT: identical camera position, identical lens (35mm), identical height and angle,
identical light direction and intensity, identical props in identical places to C005.
The ONLY difference is that the right third of frame is empty — her satchel is on the ground
where she will kneel, still open, and the bandage roll lies beside it.
SCREEN POSITION: the row of wounded holds the LEFT HALF exactly as in C005.
KEY LIGHT: burnt-gold dawn from CAMERA-LEFT AND BEHIND, god-rays, identical to C005.
NOTE: generate this in the SAME batch as C005 so the plate and the shot share a seed lineage.
```

#### C011-S — 엘라라가 다음 사람에게 간다 (엣지 프레이밍 · 영상 스타트 프레임)
```text
[PREFIX-CONT] [ELARA-LOCK]

SHOT C011-S — Elara leaves one patient for the next. START FRAME FOR A KLING CLIP.
FRAME EXIT DESIGN: she is CUT BY THE RIGHT FRAME EDGE — roughly one third of her body is
outside the frame. Her weight is already transferred onto her forward foot, her shoulder leads
SCREEN-LEFT, her shawl trails behind her to the right. The pose must be unmistakably mid-transit,
not a person standing still near an edge.
SCREEN POSITION: she occupies the RIGHT edge; the LEFT two-thirds is the row of wounded she is
moving toward, all of it in focus depth so the destination is legible.
EYELINE: SCREEN-LEFT and slightly down, at the next patient. Never at the lens.
LENS: 50mm, camera at a low three-quarter behind her right shoulder, level horizon.
KEY LIGHT: burnt-gold dawn from CAMERA-LEFT AND BEHIND — she is a near-silhouette moving into
the light. Hard rim on her left arm and braid; her face barely readable. Black negative fill
camera-right.
MOTION INTENT (for the clip, and for the Ken Burns if it stays a still): she exits the right
edge completely within the shot; the frame is left holding the wounded man she has gone to.
FG/MG/BG: FG — her blurred shoulder at the right edge. MG — the row. BG — god-rays and canvas.
```

#### C037-S — 기병대가 돌아선다 (방향 반전 · 영상 스타트 프레임)
```text
[PREFIX-CONT]

SHOT C037-S — the Skeldrian column turns and withdraws. START FRAME FOR A KLING CLIP.
DIRECTION REVERSAL — THE POINT OF THE SHOT: in C024 and C025 the cavalry moved SCREEN-LEFT TO
SCREEN-RIGHT. Here they move SCREEN-RIGHT TO SCREEN-LEFT. The reversal of travel direction is
what the audience reads as "withdraw" — it is the visual definition of Riven's one word.
FRAME EXIT DESIGN: the lead rider is already CUT BY THE LEFT FRAME EDGE. The column strings
back across the frame to the right, the last horses still turning. The right third of the frame
is the ground they are giving up — the outpost, out of focus.
LENS: 35mm, long lens compression is NOT wanted here; we need the ground between them and what
they leave. Camera low, at horse-chest height, level horizon.
KEY LIGHT: cold morning sun from CAMERA-RIGHT (4 o'clock) — they ride INTO their own shadows.
The shadows stretch ahead of them to the left. Same sun as C029–C036.
MOTION INTENT: the column clears the left edge and the frame is left with empty churned ground
and the wounded. The emptying of the frame IS the cut.
FG/MG/BG: FG — churned mud and a fallen banner staff. MG — the column. BG — grey ridge, smoke.
```

#### C058-S — 엘라라가 멈춰 선다 (군중 통과 · 영상 스타트 프레임)
```text
[PREFIX-CONT] [ELARA-LOCK]

SHOT C058-S — Elara stops in the street while the village runs past her.
START FRAME FOR A KLING CLIP. The whole shot is built on differential motion.
SCREEN POSITION: ELARA stands in the RIGHT THIRD, dead still, both feet planted, turned
three-quarters toward SCREEN-LEFT. Villagers stream through the frame LEFT TO RIGHT across the
foreground and the midground — one of them is already cut by the right frame edge, another is
entering at the left. She is the only static object in a frame full of transit.
EYELINE: SCREEN-LEFT, into the fire. Never at the lens.
LENS: 50mm, camera at eye level, slightly off-axis to her right, level horizon.
KEY LIGHT: hard ember-red firelight from CAMERA-LEFT, flickering, her lit side facing the fire;
cold smoke-grey ambient above; black negative fill camera-right.
MOTION INTENT: the running figures clear the right edge and leave her alone in frame. Nothing
about her moves except the shawl the passing bodies disturb.
FG/MG/BG: FG — a motion-blurred running shoulder crossing the near plane. MG — Elara.
BG — timber-framed houses, ember bloom, collapsing smoke.
```


#### C021-S — 엘라라가 다시 움직인다 (엣지 프레이밍 · 영상 스타트 프레임)
```text
[PREFIX-CONT] [ELARA-LOCK] [BOY-A from SUPPORT-LOCKS]

SHOT C021-S — Elara leaves the boy and goes back to work. START FRAME FOR A KLING CLIP.
This is the shot that proves the Wound did not stop her. The movement IS the characterisation.
SCREEN POSITION: ELARA is still low beside the boy, in the RIGHT-CENTRE of frame, weight
already shifting onto the forward foot, one hand leaving his. The BOY stays in the LEFT-CENTRE
midground. The LEFT edge of frame is deliberately open — that is where she is going.
EYELINE: SCREEN-LEFT, lifted from the boy to the row beyond him. She does not look back at him.
LENS: 85mm, camera at a low three-quarter from her right, level horizon, no dutch.
KEY LIGHT: burnt-gold dawn from CAMERA-LEFT AND BEHIND — hard rim backlight on her braid and
shoulder, face mostly low-key; black negative fill camera-right. Identical to C011-S so the two
exits read as the same woman doing the same thing twice.
MOTION INTENT (for the clip): she rises and clears the LEFT frame edge; the frame is left with
the boy alone, still looking at the space she has vacated.
FG/MG/BG: FG — straw, defocused, bottom-left. MG — Elara rising, the boy. BG — canvas, god-rays.
```

#### END 프레임 세트 (키프레임 B) — V1 클립용

> **END 프레임의 유일한 규칙: START와 달라지는 것은 인물/대열의 위치 하나뿐이다.** 카메라·렌즈·광원·배경·의상·소품이 함께 움직이면 Kling이 컷 전환으로 해석해 클립이 깨진다(450 손실의 1순위 원인). 아래 프롬프트는 전부 **대응하는 START 프롬프트를 그대로 복사한 뒤 `SCREEN POSITION`과 `MOTION INTENT`만 교체**하는 형태로 썼다.

```text
C011-E — END KEYFRAME for V1-1
[PREFIX-CONT] [ELARA-LOCK]
Identical to C011-S in camera position, 50mm lens, height, angle, light direction (burnt-gold
dawn from CAMERA-LEFT AND BEHIND), canvas, god-rays, props and wardrobe.
THE ONLY CHANGE: ELARA has completed the move. She is now kneeling in the LEFT-CENTRE of frame
beside the NEXT wounded man, her back three-quarters to camera, hands already reaching for his
arm. The RIGHT edge she came from is empty — only the trampled straw where she was.
EYELINE: SCREEN-LEFT and DOWN at the new patient. Never at the lens.
```

```text
C021-E — END KEYFRAME for V1-2
[PREFIX-CONT] [ELARA-LOCK] [BOY-A]
Identical to C021-S in camera position, 85mm lens, height, angle, light direction (burnt-gold
dawn from CAMERA-LEFT AND BEHIND, hard rim backlight), straw, canvas and wardrobe.
THE ONLY CHANGE: ELARA has risen and is CUT BY THE LEFT FRAME EDGE — roughly half her body
outside the frame, shoulder leading screen-left, shawl trailing right. The BOY remains in the
LEFT-CENTRE midground, now alone in the composition, still looking screen-right and up at the
space she has vacated.
EYELINE: hers is already out of frame; HIS is the shot's remaining eyeline.
```

```text
C037-E — END KEYFRAME for V1-3  (= CP-C clean plate, one asset serving two jobs)
[PREFIX-CONT]
Identical to C037-S in camera position, 35mm lens, horse-chest height, level horizon, cold
morning sun from CAMERA-RIGHT (4 o'clock), churned mud, fallen banner staff, grey ridge, smoke.
THE ONLY CHANGE: the cavalry column is GONE. The frame holds empty churned ground, hoofprints
running out of the LEFT edge, the fallen banner staff, and — far in the defocused right
background — the wounded who were left. Not one horse in frame.
This is the emptying of the frame. It is the shot.
```

```text
C058-E — END KEYFRAME for V1-4
[PREFIX-CONT] [ELARA-LOCK]
Identical to C058-S in camera position, 50mm lens, eye level, off-axis 25 degrees, hard
ember-red firelight from CAMERA-LEFT, cold smoke-grey ambient, timber-framed houses, ember bloom.
THE ONLY CHANGE: the running villagers have cleared the RIGHT frame edge. ELARA stands alone in
the RIGHT THIRD, unmoved, still turned three-quarters toward SCREEN-LEFT. The near plane that
was full of motion-blurred bodies is now empty street and drifting embers. Her shawl is still
settling from the last body that brushed past her — the only movement left in frame.
EYELINE: SCREEN-LEFT, into the fire. Never at the lens.
```

```text
C048-S / C048-E — V1-5  (the raid arrives)
[PREFIX-CONT]
START: the village mouth, EMPTY. 24mm, camera at horse-hoof height, hard ember-red key from
CAMERA-LEFT, cold ambient above. Mud lane, a leaning stall, ash falling. Nothing in frame but
the place. (This START doubles as a clean plate.)
END: enemy cavalry has entered from the LEFT and fills two thirds of the frame, driving toward
SCREEN-RIGHT, hooves at lens height, mud thrown toward camera. Identical camera, lens, height
and light. The stall is now half down.
MOTION INTENT: something ENTERS. The entrance is the event.
```

```text
C024-S / C024-E — V1-8  (the threat appears on the ridge)
[PREFIX-CONT]
START: the ridge line against empty smoke-grey sky. 24mm, aerial-adjacent low position looking
up at the crest, cold low-key, pale sun from CAMERA-RIGHT. Nothing on the crest.
END: the northern column has risen over the crest — riders in blackened steel breaking the
skyline from SCREEN-LEFT moving SCREEN-RIGHT, still small, the line unbroken to the left edge.
Identical camera, lens, height and light.
MOTION INTENT: nothing becomes something. Do not move the camera; let the ridge do the work.
```

---

## 5. 인서트 처방 — C007 · C015 · C020

인서트가 자료화면으로 뜨는 이유는 셋이다: **스케일이 튄다 · 광원이 다르다 · 소유자가 화면에 없다.** 세 가지를 전부 고정한다.

### 5-1. 공통 3법칙

| 법칙 | 내용 |
|---|---|
| **① 3~4배 법칙** | 인서트의 대상은 **직전 컷에서 그것이 차지한 화면 크기의 3~4배**로 들어간다. 2배 이하면 같은 컷을 크롭한 것처럼 보이고, 6배 이상이면 어디인지 모른다 |
| **② 신체 잔여물 법칙** | 인서트 프레임 안에 **소유자의 몸 일부가 반드시 초점 밖으로 남는다** — 숄 자락 · 소매 커프 · 건틀릿 · 사슬갑옷 손목. 그리고 그것은 **소유자가 축에서 차지한 쪽**에 있어야 한다 |
| **③ 동일 광원 법칙** | 인서트의 키 광원은 **직전 컷과 같은 시계 방향·같은 경도**여야 한다. 그림자가 같은 쪽으로 떨어지면 관객은 묻지 않는다 |

### 5-2. 컷별 처방

| 컷 | 어느 컷 옆에 | 스케일 | 신체 잔여물 (위치) | 광원 | 각도 판정 |
|---|---|---|---|---|---|
| **C007** | **C006 직후** — C006에서 그녀가 붕대를 감기 시작하는 동작 위에서 컷 | C006 대비 **손 3.5배** | **러스트레드 숄 자락, 우상단** (그녀는 축의 우측) / 환자의 팔은 **좌에서 진입** | 카메라 **좌 7~8시** 하드 버닛골드, 그림자는 우로 | 현재 `macro top-down` → **45° 사선으로 변경.** 탑다운은 좌우가 없어 소유자를 지정할 수 없다 |
| **C015** | **C014 직후** — C014에서 그녀의 시선이 아래로 떨어진 그 끝에 컷 | C014 대비 **대야 4배**(C014 하단 좌측에 대야 테두리를 미리 심는다) | **그녀의 손이 우에서 진입했다가 우로 빠진다**, 아이보리 리넨 커프 | 카메라 **좌 90°** 하드, C014의 렘브란트와 같은 방향의 더 강한 버전 | 현재 `object POV(대야 안)` → **60° 오블리크로 변경.** 대야 안에서 보는 시점은 공간의 주인이 없다 |
| **C020** | **C019 직후** — 그녀가 굳은 직후, 굳음이 풀리는 대신 손이 먼저 움직인다 | C019 대비 **손 4배** | **소년의 손 좌 / 엘라라의 손 우** — 두 사람 각자의 커프(오커 울 / 아이보리 리넨)로 구별 | 카메라 **좌측 소프트 확산**, C019의 스플릿 키를 디퓨즈한 것 | 현재 `macro top-down` → **45° 로우 오블리크로 변경.** 두 손이 위아래로 겹치면 "누가 누구를 잡았는지"가 사라진다 |

> **C020이 특히 중요한 이유:** 이 컷은 "그녀가 그의 손을 잡았다"를 말해야 한다. 탑다운은 두 손을 **위/아래**로만 구분한다. 관객은 위에 있는 손이 누구 것인지 모른다.
> **45° 사선은 좌/우로 구분한다.** 그리고 좌/우는 이미 C016~C019에서 15초 동안 가르쳐 놓았다. **인서트가 배운 것을 쓴다 — 그것이 인서트가 주인을 갖는다는 뜻이다.**

### 5-3. 보너스 — 이미 맞아 있는 인서트

**C034(엄지)·C039(요란의 손)·C056(약초 주머니)** 도 같은 3법칙으로 재생성한다(§4 프롬프트 수록).
특히 **C056은 C007과 같은 주머니여야 한다.** 회수 인서트가 같은 소품이 아니면 회수가 아니라 다른 물건이다 — `06_reference` IMG_INSERT_OBJECT가 명시한 "셋업/페이오프는 동일 앵글·동일 소품 ref".

---

## 6. 이미지로 안 되는 것 — 영상 클립 목록과 크레딧

### 6-0. 확정 조건

| 항목 | 값 |
|---|---|
| 나노 바나나 2 이미지 (Magnific 웹) | **0 크레딧 — 무료 확정** |
| Kling 1080p 5초 | **450 / 클립** |
| Kling 720p 5초 | **350 / 클립** |
| 계정 잔액 | 31,926 |
| **이 문서 몫 배정 가정** | **5,000 ~ 10,000** (정지컷 영상화는 별도 에이전트가 따로 집행) |

> 기존 1부 클립 42개는 **전량 1080p**로 집행됐다(`22_CUT_LIST` 정정 기록). 재생성분도 **기본 1080p**로 맞춘다 — 해상도가 섞이면 편집에서 스케일 불일치가 난다. 720p는 **정지로도 성립하는 리액션 컷(V3)에만** 예외적으로 쓴다.

### 6-1. 이미지로 푸는 것 (0 크레딧) — 먼저 확인

| 문제 | 이미지 해법 | 비용 |
|---|---|---|
| 시선 불일치 | §1 축 설계 + §4 프롬프트 | 0 |
| 화면 내 위치·스케일 | §1 고정표 + §5 3~4배 법칙 | 0 |
| 광원 방향 | 축 그룹별 시계 방향 고정 | 0 |
| 인서트 무소유 | §5 신체 잔여물 법칙 | 0 |
| 프레임 **진입**의 암시 | **클린 플레이트 페어** — 빈 프레임 → 인물 프레임으로 하드 컷 | 0 |
| 프레임 **이탈**의 암시 | **엣지 프레이밍 스틸** — 프레임에 반쯤 잘린 이행 자세 | 0 |
| 카메라가 인물을 **찾는** 느낌 | 켄번스 팬을 빈 공간에서 시작해 인물에 착지 | 0 |

**이 일곱 줄이 전체 문제의 약 8할이다. 여기에 돈은 한 푼도 들지 않는다.**

### 6-2. 이미지로 안 되는 것 — 왜 안 되는가

정지 이미지가 원리적으로 말할 수 없는 문장은 하나다:
> **"A에 있던 것이 B로 갔다."**

암시는 된다(§6-1의 클린 플레이트·엣지 프레이밍). 그러나 **암시는 관객이 완성해야 하고, 완성은 실패할 수 있다.** 이동 자체가 의미인 컷에서는 암시로 부족하다. 1부에서 그런 자리를 전부 골라냈다.

### 6-3. 클립 목록 — 3티어

**모든 클립은 START·END 이미지 2장을 먼저 뽑아 Kling 키프레임으로 물린다.** 이미지 장수는 무료분, 크레딧은 유료분이다.

#### V1 — 프레임 출입 (이미지로 원리적 불가) · **최우선**

| # | 컷 | 이동 A → B | 왜 영상이어야 하는가 | 이미지 | 크레딧 |
|---|---|---|---|---|---|
| V1-1 | **C011** | 그녀가 **우 엣지에 반쯤 걸친 채** → 좌측 다음 환자 곁에 무릎 | S02의 Gap이 **이 이동 자체**다 — "노파는 감사를 기대 / 그녀는 그저 다음 사람에게 간다". 정지 이미지는 이 문장을 말할 수 없다 | 2 (START/END) | 450 |
| V1-2 | **C021** | 소년 곁에 앉은 자세 → **좌 엣지로 절반 이탈** | Wound 설치 직후에도 **그녀가 계속 움직인다**는 것이 인물 정의다. 멈추면 인물이 바뀐다 | 2 | 450 |
| V1-3 | **C037** | 선두가 **좌 엣지에 걸림** → 대열이 전부 빠진 **빈 진흙땅** | 진행 방향의 반전(C024·C025의 좌→우 ↔ 여기 우→좌)이 **"후퇴"의 시각적 정의**다. 방향 반전은 두 프레임 사이에서만 존재한다 | 2 (END = CP-C) | 450 |
| V1-4 | **C058** | 군중이 프레임을 채움 → **전부 우로 빠지고 그녀만 남음** | 차등 운동이 전부인 컷. 한 장에는 담기지 않는다 | 2 | 450 |
| V1-5 | **C048** | 빈 마을 어귀 → **적 기병이 좌에서 프레임을 가득 채우며 진입** | 습격의 도발적 사건. **무언가가 들어온다**가 사건의 내용이다 | 2 (START = CP 변형) | 450 |
| V1-6 | **C050** | 군중이 좌에서 진입 → 우로 프레임 통과 | 도주 흐름의 방향을 관객 몸에 새긴다. 이 흐름이 있어야 C058의 **역행**이 읽힌다 | 2 | 450 |
| V1-7 | **C051** | 그녀가 우에 서 있음 → **부상자를 끌어 우 프레임 밖으로 반쯤 이동** | 실제 A→B 이동. 끌어당김은 정지에서 "잡고 있는 것"과 구별되지 않는다 | 2 | 450 |
| V1-8 | **C024** | 능선 너머 빈 하늘 → **기병대가 마루선 위로 솟아오름** | 위협의 등장. **없던 것이 생긴다**가 컷의 전부 | 2 | 450 |
| V1-9 | **C013** | 아이들이 좌에서 진입 → 우로 통과 | AXIS-A 공간에 **통행**을 심는다. 치료소가 정물이 아니라 장소가 된다 | 2 | 450 |
| | | | **V1 소계** | **18장** | **4,050** |

#### V2 — 대사 컷 축 재생성 (립싱크 필요 → 스틸 불가) · **필수**

축을 상속이 아니라 **저작**하려면 여섯 컷이 새로 나와야 한다(§2-3). 전 클립 무성이므로 음성 영향 없음.

| # | 컷 | 고쳐야 할 것 | 이미지 | 크레딧 |
|---|---|---|---|---|
| V2-1 | **C009** | 노파 좌 1/3 · 시선 우 · 좌후방 역광 림 확정 | 2 | 450 |
| V2-2 | **C017** | 엘라라 숄 어깨 우 전경 OTS · 시선 좌하 | 2 | 450 |
| V2-3 | **C027** | **리븐 좌 / 브리스 우** — AXIS-B·C의 인물 기준 프레임 | 2 | 450 |
| V2-4 | **C031** | 브리스 우 1/3 · 시선 좌 · 우후방 림 | 2 | 450 |
| V2-5 | **C035** | 리븐 좌 1/3 · 시선 우하 · 우측 스플릿 | 2 | 450 |
| V2-6 | **C041** | 사제 깊이 축 · 좌상단 갓레이 (AXIS-D) | 2 | 450 |
| | | **V2 소계** | **12장** | **2,700** |

#### V3 — 리액션 컷 선택 집행 (스틸로도 성립) · **선별**

판단 기준: **"이 컷에서 눈꺼풀이 한 번 내려가는 것이 정보인가?"**

| # | 컷 | 판정 | 해상도 | 이미지 | 크레딧 |
|---|---|---|---|---|---|
| V3-1 | **C019** | **산다.** 굳음은 **움직이다 멈추는 것**이다 — 정지 이미지에는 "멈췄다"가 없고 "정지"만 있다. 손이 붕대를 감다가 서는 반 박자가 컷의 전부 | 1080p | 2 | 450 |
| V3-2 | **C036** | **산다.** "요란이 그를 본다" — 눈이 **따라가는** 것이 동사다. 초점이 리븐을 잡는 순간이 페이오프의 씨앗 | 1080p | 2 | 450 |
| V3-3 | C010 | 안 산다. 답하지 않음 = 정지. 스틸이 더 강하다 | — | 0 | 0 |
| V3-4 | C018 | 안 산다. 입모양만 필요한데 자막도 없다. 스틸 + 미세 켄번스로 충분 | — | 0 | 0 |
| V3-5 | C032 | 안 산다. 계산하는 얼굴 = 정지 | — | 0 | 0 |
| V3-6 | C033 | 안 산다. 설치 컷은 **각인**이 목적이고 정지가 각인에 유리하다 | — | 0 | 0 |
| V3-7 | C045 | 안 산다. 고개를 드는 동작은 C061과 겹친다 — 여기서 쓰면 클리프행어가 싸진다 | — | 0 | 0 |
| | | **V3 소계(권고안)** | | **4장** | **900** |

> V3 전량(7컷)을 사고 싶다면 **720p 7 × 350 = 2,450.** 그러나 기존 42클립이 1080p라 해상도가 섞인다. **권고하지 않는다.**

### 6-4. 집행 합계

| 티어 | 클립 | 이미지(무료) | 크레딧 |
|---|---|---|---|
| **V1 프레임 출입** | 9 | 18 | **4,050** |
| **V2 대사 컷 축** | 6 | 12 | **2,700** |
| **V3 리액션 선별(권고)** | 2 | 4 | **900** |
| **합계** | **17** | **34장 = 0원** | **7,650** |

**배정 가정 5,000~10,000 안에서 성립한다.** 상한까지 여유 2,350 = 재시도 5클립분.

### 6-5. 예산을 줄여야 할 때의 절단 순서

| 잔여 예산 | 집행 | 잘리는 것 |
|---|---|---|
| **7,650 (전량)** | V1 + V2 + V3권고 | — |
| **6,750** | V1 + V2 | C019·C036을 스틸로. 정지 컷 20→22 |
| **5,400** | V1 + V2 중 C027·C035만 | 나머지 대사 4컷은 기존 클립 유지 → **§7 거울 검증으로 축을 상속** |
| **4,050** | V1만 | 대사 컷 전량 상속. 축은 §7로 검증만 |
| **1,800** | V1-1·2·3·4만 | 프레임 출입의 **최소 핵**. 이것 아래로는 이 문서의 3번 문제(프레임 출입)가 미해결로 남는다 |

> **절단은 V3 → V2 → V1 순서로만 한다.** V1을 먼저 자르면 이 문서가 푸는 네 문제 중 하나가 통째로 남는다.

### 6-6. 키프레임 집행 규칙 (재시도 비용 방어)

1. **START·END 두 장은 같은 배치에서 뽑는다.** 같은 시드 계열이어야 두 프레임 사이가 연속으로 보간된다.
2. **두 프레임의 차이는 오직 이동 하나뿐이어야 한다.** 광원·렌즈·배경·의상이 함께 바뀌면 모델이 컷 전환으로 해석해 클립이 깨진다 — 450 손실의 1순위 원인.
3. **END 프레임이 빈 프레임인 경우**(C011·C037·C058) 그 빈 프레임은 **클린 플레이트와 동일 자산**이다. 한 장으로 두 몫을 한다.
4. **프롬프트에 이동 방향을 문장으로 적는다** — `the subject clears the RIGHT frame edge completely`. 키프레임만으로 방향을 추론시키지 않는다.
5. **규칙 0-[B] 영상 프리픽스를 맨 앞에 그대로 붙인다** (`06_reference` §규칙0[B]) — `No background music. NO BGM. NO score. SFX only` + `CHARACTER LOCK`. 1부는 전 클립 무성이 전제다.
6. **첫 집행은 V1-3(C037) 한 클립으로 한다.** 프레임 이탈이 가장 단순하고(인물 표정 없음, 대열만 빠짐) 키프레임 보간이 제대로 도는지를 450원으로 검증할 수 있다. 통과하면 나머지 16클립을 배치로 돌린다.

## 7. 집행 전 거울 검증 (5분, 반드시 먼저)

§6의 V2 티어를 전량 집행하면 대사 컷 6개가 새로 나오므로 축은 **상속이 아니라 저작**된다. 그 경우 이 절은 **C028 한 줄만** 확인하면 끝난다.
**V2를 일부만 사거나(§6-5 절단) 기존 클립을 유지하기로 하면**, 유지하는 컷의 좌/우를 뽑기 전에 실물로 확인해야 한다.

| # | 확인할 클립 | 맞아야 하는 것 | 틀리면 |
|---|---|---|---|
| 1 | C009 | 노파가 **좌**, 시선 **우** | AXIS-A 전체 좌/우 반전 |
| 2 | C017 | 엘라라의 숄 어깨가 **우 전경** | AXIS-A 전체 좌/우 반전 |
| 3 | C027 | 리븐 **좌** / 브리스 **우** | AXIS-B·C 전체 좌/우 반전 |
| 4 | C031 | 브리스가 **우**, 시선 **좌** | AXIS-C 반전 |
| 5 | C035 | 리븐 사이드 프로필이 **우**를 향함 | AXIS-C 반전 |
| 6 | C028 | 리븐 **좌 끝** / 마을 **우 끝** | 이 컷이 최종 기준 — 이것이 다른 넷을 이긴다 |
| 7 | C041 | 사제가 회중을 **내려다봄**(깊이 축) | AXIS-D는 좌우가 없으므로 영향 없음 |

**반전 방법:** 해당 그룹 프롬프트의 `SCREEN-LEFT` ↔ `SCREEN-RIGHT`, `CAMERA-LEFT` ↔ `CAMERA-RIGHT`를 **전부** 치환한다. 시선과 광원은 같은 방향으로 함께 뒤집어야 한다 — 하나만 뒤집으면 더 나빠진다.

## 8. 완료 판정 체크리스트

**무료 단계 (이미지 — 전부 먼저 끝낸다)**
- [ ] §7 거울 검증 — V2 전량 집행이면 C028 1항만, 부분 집행이면 7항 전부
- [ ] P0 3장 생성 → AXIS-A·C 마스터 확정
- [ ] P1 10장 생성 → **쌍끼리 나란히 놓고 본다.** 두 컷을 붙였을 때 두 사람이 서로를 보는가
- [ ] P2 6장 생성 → 인서트를 직전 컷과 붙여 본다. 그림자가 같은 쪽으로 떨어지는가
- [ ] P3 11장 생성 → S08 전체를 연속 재생. 불빛이 항상 왼쪽에서 오는가
- [ ] P4 약 37장 생성 → 클린 플레이트 3장 + V1~V3 클립 17개의 START/END 쌍 34장
- [ ] START/END 쌍 육안 검사: **두 장의 차이가 이동 하나뿐인가.** 광원·렌즈·배경이 함께 움직였으면 다시 뽑는다 (무료)

**유료 단계 (영상 — 위가 끝난 뒤에만)**
- [ ] 파일럿 1클립(V1-3 / C037, 450) 집행 → 키프레임 보간 검증
- [ ] 통과 시 V1 나머지 8클립 (3,600) → 누계 4,050
- [ ] V2 6클립 (2,700) → 누계 6,750
- [ ] V3 권고 2클립 (900) → **누계 7,650**
- [ ] 스틸 유지 5컷(C010·C018·C032·C033·C045)에 켄번스 2~3% 푸시인 적용, 정지 컷 20→25 반영해 `27_EDIT_SHEET` 계층 표 갱신
- [ ] 외형 락 회귀 검사: 엘라라 머리 길이(waist-length) · 눈(grey-green, 발광 없음) · ELARA-A 의상 3점 / 리븐 흉터 위치 동일측 · 머리 길이(어깨) · RIVEN-A 갑옷

---

## 부록 — 이 설계가 만든 것

축을 맞추는 작업은 오류 수정처럼 보이지만, 결과로 **1부에 없던 문장 세 개**가 생긴다.

1. **"엘라라는 왼쪽을 본다."** 모두가 오른쪽으로 도망치는 S08에서 그녀만 왼쪽을 본다. 아크 전체가 프레이밍 하나로 읽힌다.
2. **"리븐은 오른쪽을 본다."** 두 사람은 1부에서 한 번도 만나지 않지만 **62컷 내내 서로를 향해 보고 있다.** 2부 첫 만남에서 축이 그대로 맞물린다.
3. **"위협은 왼쪽에 있다."** C028의 리븐이 있던 자리에 C044의 연기가 선다. 엘라라가 고개를 들어 보는 방향은 **그가 서 있던 방향**이다. 그녀는 모르는 채로 그를 본다.

> 세 문장 모두 **대사가 없다.** 축을 지키면 공짜로 따라온다.
