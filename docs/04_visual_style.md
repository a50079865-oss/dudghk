# 4단계 결과물: 비주얼 스타일 방향 설정 (비주얼 바이블)

> **한 줄 정의**
> 반지의 제왕의 세계관 규모, The Green Knight의 몽환적 중세미, Kingdom of Heaven의 현실적 기사 미술,
> Macbeth의 감정적 색감, The Northman의 거친 질감을 결합한 **실사 중세 하이판타지**.

## 요약 기준 표

| 항목 | 내용 |
|---|---|
| 아트 스타일 | 실사 라이브액션 중세 하이판타지. 판타지가 고증된 중세 사극 위에 얹힌다. 35mm 아나모픽 필름룩 |
| 영상 톤 | 서사적 숭고 → 신화적 몽환 → 육체적 잔혹. 기본값은 영웅적 고양이 아니라 경외와 불안 |
| 색감 방향 | 저채도 회청 그레이 기본 / 이끼 초록·젖은 황토 / 핏빛 앰버·심홍은 감정 임계점에만 개방 |
| 조명 방향 | 100% 실광원 논리. 오버캐스트 확산광, 저각도 역광, 횃불·촛불·달빛. 필 라이트 금지 |
| 렌더링 / 질감 | 아날로그 그레인, 블랙 프로미스트 디퓨전, 표면에 항상 이력(녹·진흙·마른 피·젖은 양모) |
| 문화·장르 시각 요소 | 12~14세기 서북유럽(켈트·앵글로색슨·노르드). 초자연은 발광이 아니라 자연의 이상 현상 |
| 피해야 할 방향 | §12 참조 |

---

## 1. 레퍼런스 배합

각 레퍼런스는 제목이 아니라 **가져올 요소**로 분해해 사용한다.

| 레퍼런스 | 가져오는 것 | 가져오지 않는 것 |
|---|---|---|
| **The Lord of the Rings** | 지형 앞에서 인간이 축소되는 스케일감, 실재하는 로케이션의 무게, 극단적 와이드 | 영웅적 고양감, 밝고 따뜻한 샤이어톤, 크레인 슛 남용 |
| **The Green Knight** | 안개 속에서 현실감이 녹는 신화적 정적, 저채도 이끼 초록, 대칭·상징 프레이밍 | 노골적 초현실 연출, 채도 높은 색면 |
| **Kingdom of Heaven** | 고증된 갑옷·무구·직물의 물성, 먼지와 땀, 실제 무게가 느껴지는 액션 | 대규모 CG 공성전의 매끈함 |
| **Macbeth (2015)** | 감정 상태를 색으로 전환하는 규칙, 하이 콘트라스트 실루엣 | 무대적 과장, 슬로모션 남용 |
| **The Northman** | 진흙·피·젖은 모피의 촉각, 자연광과 횃불만 쓰는 원칙, 롱테이크 | 의식적 광기의 톤 전체를 그대로 가져오지는 않음 |

## 2. 아트 스타일

실사 시네마틱 라이브액션. 판타지 요소는 존재하되 **흙·쇠·가죽의 물성**을 반드시 갖는다. 게임 시네마틱이나 CG 판타지가 아니라, 실제 로케이션에서 촬영된 35mm 필름 영화의 질감을 기준으로 한다.

## 3. 영상 톤

장엄함과 불길함의 동거. 광활한 지형 앞의 서사적 숭고 → 안개 속 신화적 몽환 → 피와 진흙의 육체적 잔혹으로 층이 이동한다. 조용한 롱테이크 뒤에 짧고 폭발적인 파열을 두는 리듬. 감정은 **억제되어 있으나 깊게** 흐른다 — 배우가 감정을 연기해 보이는 것이 아니라 관객이 침묵에서 읽어내게 한다.

## 4. 색감 방향 — 3막 팔레트

색은 장식이 아니라 **감정 상태의 지표**로 쓴다.

| 단계 | HEX | 적용 |
|---|---|---|
| ① 회청빛 안개 그레이 | `#8C9296` `#6E7A80` | 평시·이동·의식. 프로젝트의 기본 저채도 톤 |
| ② 이끼 초록 + 젖은 황토 | `#4A5540` `#7A6640` | 숲·습지·야영. 몽환 구간 |
| ③ 핏빛 앰버·심홍 | `#C24A1E` `#7B1F16` | 감정이 임계에 닿는 순간에만 개방 |

파랑↔주황 보색 대비는 **하늘과 실제 불꽃**(횃불·화톳불·화재)에서만 자연 발생시킨다. 후반 자동 그레이딩으로 만들지 않는다.

## 5. 조명 방향

100% 자연광·실광원 논리.

- **낮** — 오버캐스트 확산광, 저각도 골든아워 역광
- **밤** — 횃불·모닥불·촛불·달빛만. 밤은 어둡게 유지한다
- **실내** — 좁은 창의 단일 방향광 + 깊은 낙차의 로우키 그림자
- 안개·연기·먼지에 빛을 통과시켜 볼류메트릭 광선을 만든다
- **인물을 예쁘게 하는 필 라이트 금지.** 얼굴 절반이 어둠에 잠기는 것을 허용한다

## 6. 렌더링 / 질감

거칠고 촉각적인 물성이 최우선. 표면에는 항상 이력이 남는다 — 갑옷의 긁힘과 녹, 젖은 양모와 모피의 무게, 손톱 밑 때, 진흙, 마른 피, 입김, 땀 젖은 피부.

- 아날로그 필름 그레인, 살짝 소프트한 안티크 렌즈 해상감
- **블랙 프로미스트 디퓨전** — 하이라이트가 부드럽게 번지되 암부는 탁해지지 않는 정도
- 실제 안개·불·비 등 프랙티컬 이펙트 우선, 디지털 합성은 보이지 않게
- 배경은 얕은 심도로 부드럽게 무너뜨리되 인물 텍스처는 선명하게

## 7. 문화·장르 시각 요소

12~14세기 서북유럽 기반 — 켈트·앵글로색슨·노르드 혼합.

- **의상 / 무구** — 리벳 체인메일, 서코트, 무두질한 가죽, 거친 리넨과 두꺼운 양모 망토, 브로치와 벨트 버클, 손으로 두들긴 철제 헬름. 고증 우선, 게임식 과장 실루엣 금지
- **건축** — 로마네스크 석조, 목조 홀, 흙벽·초가, 봉수대, 무덤 봉분, 선돌과 룬석
- **자연** — 이끼 낀 고목림, 안개 습지, 검은 화산 해안, 이탄 늪, 안개 낮게 깔린 협곡
- **반복 상징** — 까마귀, 사슴뿔, 매듭 문양, 불타는 나무, 안개 속 단독 기수

## 8. 판타지 레이어 규칙

초자연은 **빛나는 마법 이펙트가 아니라 자연의 이상 현상**으로 표현한다. 이 규칙이 게임 시네마틱룩으로 미끄러지는 것을 막는 가장 중요한 방어선이다.

- 방향이 틀린 그림자
- 갑자기 멈춘 새떼, 사라진 소리
- 인광을 띤 이끼와 물
- 뿔과 뼈로 이루어진 형상
- 크기가 잘못된 실루엣
- 안개가 바람과 반대로 흐르는 순간

## 9. 카메라 / 렌즈 / 화면비

| 항목 | 기준 |
|---|---|
| 화면비 | 2.39:1 아나모픽 기본 / 인물 단독 시퀀스는 1.66:1까지 좁혀 압박감 부여 |
| 렌즈 | 안티크 아나모픽 계열. 미세한 렌즈 브리딩과 가장자리 왜곡을 남긴다 |
| 필터 | 블랙 프로미스트 (전 시퀀스 공통) |
| 심도 | 얕은 자연광 심도. 인물 텍스처는 선명, 배경은 부드럽게 |
| 무빙 | 정적 롱테이크가 기본. 핸드헬드는 미세한 호흡 수준으로, 전투에서만 밀착 |

## 10. 장면별 룩 프리셋

> **C·D는 확정 프리셋이다.** A·B·E·F는 같은 형식으로 채운 제안이므로, 이미 정해둔 안이 있으면 교체하면 된다.

| 프리셋 | 적용 장면 | 광원 | 색 | 카메라 |
|---|---|---|---|---|
| **A. 광활한 여정** | 대지 이동, 행군, 성·유적 첫 등장 | 오버캐스트 확산광, 저각도 역광 | ① 회청 그레이 + 옅은 황토 | 극단적 와이드, 인물은 프레임의 1/20, 느린 트래킹 |
| **B. 안개의 문턱** | 숲·습지 진입, 초자연 조우 | 안개 통과광, 방향 불명확 | ② 이끼 초록, 최저 채도 | 고정 또는 초저속 180° 회전, 대칭 프레이밍 |
| **C. 로맨스 장면** | 밀실·정원·회랑에서의 정서적 밀착 | 촛불(온) + 달빛(냉) 혼합 | ①의 냉기 위에 ③의 앰버를 최소량 | 미들·클로즈업, 얕은 심도, 소프트 할레이션 |
| **D. 전장 장면** | 전투, 패주, 시신 수습 | 흐린 회색 하늘, 연기·재의 확산 | 절제된 저채도, 진흙과 강철 | 다이내믹하되 통제된 무빙, 밀착 핸드헬드 |
| **E. 횃불의 홀** | 실내 모의, 연회, 의식 | 단일 화톳불·촛대, 로우키 | ③ 앰버 하이라이트 + 잉크빛 암부 | 미들샷, 미세한 핸드헬드 호흡 |
| **F. 창백한 새벽** | 여파, 상실, 결말 | 저각도 차가운 여명 | 탈색된 청회 단색조 | 정적 롱테이크 |

### 프롬프트 블록

**A. 광활한 여정**
```
A cinematic live-action medieval fantasy landscape journey, vast weathered terrain
dwarfing the lone figures, overcast diffused daylight with low-angle backlight,
slate-grey and pale ochre palette, low saturation, volumetric mist in the valleys,
real location weight and scale, slow deliberate tracking movement, extreme wide shot,
35mm anamorphic film texture, black pro-mist diffusion, no stylized game-like effects.
```

**B. 안개의 문턱**
```
A cinematic live-action medieval fantasy encounter at the edge of a fog-bound wood,
directionless light filtered through heavy mist, moss-green and wet-ochre palette at
lowest saturation, mythic stillness, symmetrical framing, a silhouette of wrong scale
half-visible in the haze, natural uncanny phenomena instead of glowing magic,
static or extremely slow rotating camera, 35mm film grain, black pro-mist diffusion,
poetic and unsettling, no neon magic, no fantasy VFX.
```

**C. 로맨스 장면** — *확정*
```
A cinematic live-action medieval fantasy romantic scene, quiet emotional intimacy,
soft backlight, flowing hair and fabric, subtle wind, warm candlelight mixed with cool
moonlight, poetic atmosphere, elegant costume textures, shallow depth of field,
soft halation, 35mm film look, emotionally restrained but deeply felt.
```
> 운용 주석 — "elegant costume textures"는 **새 옷이 아니라 잘 관리된 옷**을 뜻한다. 실크·벨벳의 광택은 허용하되 착용 이력(구김, 닳은 소맷단, 수선 자국)을 남긴다. 촛불과 달빛의 밝기 차는 1스톱 이내로 유지해 §12의 "너무 밝은 밤 장면"으로 넘어가지 않게 한다.

**D. 전장 장면** — *확정*
```
A cinematic live-action medieval fantasy battlefield, muddy ground, torn banners,
smoke and ash in the air, weathered armor, cold grey sky, restrained color palette,
dramatic realism, brutal and tragic atmosphere, dynamic but controlled camera feeling,
35mm film texture, black pro-mist diffusion, no stylized game-like effects.
```

**E. 횃불의 홀**
```
A cinematic live-action medieval great hall interior at night, single hearth and candle
sources, deep low-key shadows with amber highlights and ink-black falloff, smoke haze
catching the firelight, coarse wool and worn leather, hand-forged metal, faces half lost
to darkness, no fill light, subtle handheld breathing, 35mm film grain,
black pro-mist diffusion.
```

**F. 창백한 새벽**
```
A cinematic live-action medieval fantasy aftermath at first light, cold low-angle dawn,
bleached blue-grey monochrome palette, breath visible in the air, exhaustion and loss,
static long take, shallow natural depth of field, 35mm film texture,
black pro-mist diffusion, emotionally restrained, no dramatic score-driven staging.
```

## 11. 공통 프롬프트 블록

모든 컷 프롬프트에 기본으로 얹는 고정 블록.

```
photoreal live-action medieval high fantasy, shot on 35mm anamorphic film,
naturalistic practical lighting only (overcast diffusion, low golden-hour backlight,
torchlight, firelight, moonlight), volumetric fog and god rays,
desaturated slate-grey and moss-green palette with restrained blood-amber accents,
historically accurate 12th-14th century Northwestern European armour and garb —
riveted mail, surcoat, worn leather, coarse linen and heavy wool,
tactile weathered surfaces: rust, scratches, mud, dried blood, sweat, visible breath,
epic landscape scale with the human figure dwarfed by terrain,
dreamlike mythic stillness, organic film grain, black pro-mist diffusion,
subtle handheld breathing, shallow natural depth of field,
low-key deep shadows, no fill light
```

## 12. 이 프로젝트의 금지 요소

아래 요소는 이 비주얼 바이블 기준에서 최대한 피한다.

| # | 금지 요소 | 대신 |
|---|---|---|
| 1 | 현대적인 헤어/메이크업 느낌 | 기름지고 헝클어진 머리, 맨얼굴, 실제 피부 결과 잡티 |
| 2 | 너무 깨끗한 갑옷과 새 옷 | 착용 이력이 남은 표면 — 긁힘, 수선 자국, 닳은 가장자리 |
| 3 | 플라스틱처럼 보이는 금속 질감 | 손으로 두들긴 철의 불균일한 반사, 녹과 기름때 |
| 4 | 네온빛 마법 | §8의 자연 이상 현상 |
| 5 | 게임 UI 같은 이펙트 | 화면 위 정보 표기 일절 없음 |
| 6 | 과포화 색감 | §4의 저채도 3막 팔레트 |
| 7 | 애니메이션풍 과장 표정 | 억제된 미세 표정, 시선과 침묵 |
| 8 | 현대 드레스 같은 실루엣 | 12~14세기 재단, 자연 낙차의 두꺼운 직물 |
| 9 | 지나친 CGI 광택 | 프랙티컬 이펙트, 필름 그레인 |
| 10 | 너무 밝은 밤 장면 | 실광원 밝기 그대로, 암부는 암부로 |
| 11 | 무게감 없는 판타지 장식 남발 | 기능이 있는 물건만. 장식은 문화적 근거가 있을 때만 |

**추가 회피 항목**

- MMO/게임 시네마틱룩 — 과장된 어깨 장식, 비현실적 대검, 발광 룬 각인
- 디즈니·영웅서사식 밝고 따뜻한 룩, 웅장한 크레인 슛 남용
- 동아시아·중동·스팀펑크·바이킹 판타지 코스프레 혼입
- 오버샤프닝, HDR 톤매핑, 과한 렌즈 플레어, 후반 블루-오렌지 자동 그레이딩
- 판독 불가능한 무작위 룬·의미 없는 문자열
- 시대착오 소품 — 안경, 지퍼, 티나는 재봉선, 현대식 직조 원단
- 애니풍·카툰풍·3D 렌더룩, 유아틱한 비율

### Negative 프롬프트 블록

```
negative: modern hair and makeup, glamour styling, clean shiny new armour,
plastic-looking metal, neon magic VFX, glowing runes, game UI overlay, HUD,
oversaturated colors, exaggerated cartoon expressions, anime, 3D render look,
modern dress silhouette, excessive CGI gloss, overlit night scene,
weightless decorative fantasy ornaments, MMO fantasy armour, oversized pauldrons,
oversharpened, HDR tonemapping, heavy lens flare, teal-and-orange auto grade,
cosplay, steampunk, random illegible runes, anachronistic props,
modern fabrics and visible machine stitching
```

---

## 다음 단계 제안

- **4.5단계 캐릭터 컨셉 프리뷰** — 다섯 레퍼런스의 배합비를 이미지로 확인하고 넘어가면 5·6단계 재작업이 줄어든다. 4안 비교 제안: **A안** 고증 최대(Kingdom of Heaven) / **B안** 몽환 최대(Green Knight) / **C안** 거친 질감 최대(Northman) / **D안** 색감 최대(Macbeth)
- 캐릭터 설정(1~3단계)이 아직 없다면 4.5단계를 건너뛰고 **6단계 세계관 시트**부터 만들어 룩을 먼저 고정하는 순서도 가능하다
- §10의 A·B·E·F를 확정하거나 교체하면 컷별 이미지·영상 프롬프트 확장으로 바로 넘어갈 수 있다
