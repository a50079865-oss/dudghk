# S24 — EP01 본 이미지 (캐릭터 락 + ARRI 룩)

> 생성: 사용자 (매그니픽 웹 · **Google Nano Banana 2** · **16:9** · **2K** · QUALITY = **컷당 2안**)
> 조립 (플레이북 24-1): 규칙0[A] + DRAMA_IMG_ENHANCE + ARRI_LOOK + IMG_PERSON_LOCK / IMG_INSERT_OBJECT (전부 **원문 그대로**) + 컷 본문(S21 렌즈) + 조명(S22) + ENV(S23 공간) + STYLE + AVOID
> 참조(ref): 인물 = 시트 **정면 패널 크롭** · 공간 = plate · 구도 = 통과한 S16 프리뷰
> 저장명: `S24_EP01_CUT##_a` / `_b`

## 준비 — 정면 패널 크롭 (참조용)
`S5_FRONT_ELARA` · `S5_FRONT_RIVEN` · `S5_FRONT_YORAN` · `S5_FRONT_LIN` · `S5_FRONT_BRYS` · `S5_FRONT_DORMAN`
(린은 얼굴 = 정면 패널, 체형·의상 = 전신 패널 — `PIPELINE_S5` 예외)

## 배치 1 — 심장 컷 6개 (시트 락 검증)

> 시간대 충돌 수정: 공통 ENV의 "cold diffused daylight"가 밤·저녁 컷을 낮으로 끌어당긴다 (S16 CUT37이 낮으로 나온 원인) → 밤·저녁 컷은 ENV의 시간 구절을 교체.

### CUT13 — 저는 안 세요

**참조 이미지:**
- S5_FRONT_ELARA (얼굴·의상)
- P2_MED_TENT (공간)
- S16_EP01_CUT13 (구도)

```text
MANDATORY DRAMA IMAGE PREFIX (append to EVERY scene-image prompt, no exceptions):
— IDENTITY LOCK: render EXACTLY the same person(s) as the character-sheet reference — same face, age, hair, signature wardrobe. Never beautify, never average into a generic idol face. If two characters share a frame, each must match their own sheet.
— ANGLE BALANCE: pick ONE deliberate angle per shot from {high / low / side / dutch / over-the-shoulder / demai close-up / insert / object POV}, and never repeat the previous shot's angle. ZERO flat front-facing eye-level unless it is a designated peak-emotion reaction.
— DEPTH & TEXTURE: shallow depth of field (telephoto demai bokeh), clear FG/MG/BG separation; ARRI Alexa / ARRI look — filmic latitude, gentle organic softness (NOT clinical digital sharpness), fine 35mm grain, true-to-skin subsurface texture.
— LIGHTING & ART obey the shot's assigned lighting recipe and art-direction (color contrast / color balance) from STORYBOARD_PLAN; LOW-KEY by default, high-key ONLY where the recipe says so.

CINEMATIC PHOTOREAL DRAMA — REQUIRED ENHANCEMENT (append to every scene image):
A real frame from a premium cinema-grade TV drama — never CGI / 3D-render / illustration / video-game render. Heightened photoreal realism with lifelike skin micro-texture (visible pores, subsurface scattering, sharp eye catchlights).
FRAME: obey the project frame (horizontal 16:9 OR vertical 9:16) from STORYBOARD_PLAN. For vertical, keep the lower ~20% as clean defocused negative space for subtitles.
ANGLE BALANCE: use the shot's assigned angle (high / low / side / dutch / OTS / demai CU / insert / object POV); rotate angles between adjacent cuts; reserve dead-on eye-level for peak-emotion reactions only.
DEPTH: telephoto shallow depth of field (demai bokeh) with clear 3-layer FG/MG/BG separation.
LIGHTING: obey the assigned lighting recipe; LOW-KEY luxurious grade by default — deep controlled shadows, restrained highlights, motivated practicals; high-key only where the recipe specifies.
ART: obey the assigned art-direction — deliberate color contrast (subject separated from background by hue) and color balance (one dominant color + one complementary accent); fill FG/MG/BG, no dead space (except the subtitle margin); place the scene's signature/setup props.
Compose so cuts connect via match-cuts; frame as a keyframe primed for the assigned pace's motion.

CAMERA / FILM LOOK (ARRI): shot on ARRI Alexa (Alexa 65 for wides) with vintage anamorphic lenses; filmic latitude and highlight roll-off; gentle organic SOFTNESS — NOT clinical digital sharpness; fine-to-medium 35mm film grain (Vision3 500T feel); Black Pro-Mist halation bloom on highlights; anamorphic oval bokeh + subtle horizontal lens flare; crushed blacks, controlled low saturation, rich but not garish color; true cinematic contrast (chiaroscuro), never flat video-look.

PERSON CUT: exactly the SAME person as the character sheet (face, age, hair, wardrobe) — do not alter identity. Prefer 3/4 or over-the-shoulder framing and reaction close-ups over dead-on lip-sync framing (protects voice-lock dubbing later). Demai shallow DOF on the face; motivated key + negative fill; micro-expression readable.

16:9 frame. Held demai close-up, 135mm telephoto, her face filling most of the frame, framed slightly off-center, low three-quarter side angle, inside the dark canvas medical tent. The young woman EXACTLY as in the character reference: same face, same age, grey cloth tied over her hair, worn undyed linen dress. Faint soot on her cheek, a few loose strands of hair. She is not looking at the old man speaking to her off-screen; her eyes are turned away toward the people lying on the floor beyond frame. Face completely still and closed, jaw set, DRY eyes, lips pressed — no tears. Only a soft blurred sliver of the old man's grey beard at the very edge of frame.
LIGHTING RECIPE: single motivated source — a narrow shaft of grey daylight from the tent entrance on one side; Rembrandt triangle on the shadow cheek; black negative fill on the far side so half the face falls into real darkness.
Late-medieval continent of Kasran, overcast sky, cold diffused daylight, fine GREY ash flakes drifting slowly in the air (dark grey ash, never white snow), wet churned mud underfoot. A refugee camp in open country: only canvas tents, timber frames, ropes, mud and ash — no stone buildings, no walls, no castle, no town houses. Rough wool and linen, blackened steel — nothing new, nothing clean, everything wet, scorched or frayed. Desaturated ash grey and steel slate with mud-brown shadows; the only warm colour in frame is real firelight. Low-key, real darkness allowed. Beautiful but brutal medieval reality, interrupted only rarely by overwhelming ancient myth.
Photoreal live-action cinema. Not illustration, not anime, not 3D render, not concept painting. ARRI Alexa look: fine 35mm grain, black pro-mist, soft halation, crushed blacks, shallow depth of field with clear foreground/midground/background separation. Practical light sources only. Epic scale but cold: thriller-noir tension with the intimacy of melodrama. 11th–13th century European material culture: mail armour, wool, linen, leather, timber, stone. No plate armour.
AVOID: tears, crying, wet eyes, smiling, eye contact with camera, beauty lighting, makeup, outdoors, stone wall, neon aura, glowing eyes, particle effects, magic sparkles, HUD or runes, glossy MMO rendering, plate armour, breastplate, cuirass, pauldrons, spaulders, riveted plates, spikes, superhero poses, idol-perfect faces, modern hairstyles, clean new clothing, centered symmetrical composition, crowds with visible faces, readable in-image text, random letters, labels, logos, watermarks, modern objects, modern shipping pallets, letterbox bars, black bars, white snow, snowflakes, snow on the ground, natural green vegetation.
```

### CUT28 — 이백이다

**참조 이미지:**
- S5_FRONT_YORAN (전경 인물)
- S5_FRONT_RIVEN (선두 기수)
- P3_FIELD (공간)
- S16_EP01_CUT28 (구도)

```text
MANDATORY DRAMA IMAGE PREFIX (append to EVERY scene-image prompt, no exceptions):
— IDENTITY LOCK: render EXACTLY the same person(s) as the character-sheet reference — same face, age, hair, signature wardrobe. Never beautify, never average into a generic idol face. If two characters share a frame, each must match their own sheet.
— ANGLE BALANCE: pick ONE deliberate angle per shot from {high / low / side / dutch / over-the-shoulder / demai close-up / insert / object POV}, and never repeat the previous shot's angle. ZERO flat front-facing eye-level unless it is a designated peak-emotion reaction.
— DEPTH & TEXTURE: shallow depth of field (telephoto demai bokeh), clear FG/MG/BG separation; ARRI Alexa / ARRI look — filmic latitude, gentle organic softness (NOT clinical digital sharpness), fine 35mm grain, true-to-skin subsurface texture.
— LIGHTING & ART obey the shot's assigned lighting recipe and art-direction (color contrast / color balance) from STORYBOARD_PLAN; LOW-KEY by default, high-key ONLY where the recipe says so.

CINEMATIC PHOTOREAL DRAMA — REQUIRED ENHANCEMENT (append to every scene image):
A real frame from a premium cinema-grade TV drama — never CGI / 3D-render / illustration / video-game render. Heightened photoreal realism with lifelike skin micro-texture (visible pores, subsurface scattering, sharp eye catchlights).
FRAME: obey the project frame (horizontal 16:9 OR vertical 9:16) from STORYBOARD_PLAN. For vertical, keep the lower ~20% as clean defocused negative space for subtitles.
ANGLE BALANCE: use the shot's assigned angle (high / low / side / dutch / OTS / demai CU / insert / object POV); rotate angles between adjacent cuts; reserve dead-on eye-level for peak-emotion reactions only.
DEPTH: telephoto shallow depth of field (demai bokeh) with clear 3-layer FG/MG/BG separation.
LIGHTING: obey the assigned lighting recipe; LOW-KEY luxurious grade by default — deep controlled shadows, restrained highlights, motivated practicals; high-key only where the recipe specifies.
ART: obey the assigned art-direction — deliberate color contrast (subject separated from background by hue) and color balance (one dominant color + one complementary accent); fill FG/MG/BG, no dead space (except the subtitle margin); place the scene's signature/setup props.
Compose so cuts connect via match-cuts; frame as a keyframe primed for the assigned pace's motion.

CAMERA / FILM LOOK (ARRI): shot on ARRI Alexa (Alexa 65 for wides) with vintage anamorphic lenses; filmic latitude and highlight roll-off; gentle organic SOFTNESS — NOT clinical digital sharpness; fine-to-medium 35mm film grain (Vision3 500T feel); Black Pro-Mist halation bloom on highlights; anamorphic oval bokeh + subtle horizontal lens flare; crushed blacks, controlled low saturation, rich but not garish color; true cinematic contrast (chiaroscuro), never flat video-look.

PERSON CUT: exactly the SAME person as the character sheet (face, age, hair, wardrobe) — do not alter identity. Prefer 3/4 or over-the-shoulder framing and reaction close-ups over dead-on lip-sync framing (protects voice-lock dubbing later). Demai shallow DOF on the face; motivated key + negative fill; micro-expression readable.

16:9 frame. High wide pull-back, 35mm, deep focus. A column of about two hundred mounted soldiers in dull mail and dark cloaks rides AWAY from camera, receding in depth along a muddy track toward the far bare hills — the column shrinks into the distance, it does not cross the frame; three wooden carts full of wounded in its midst. At the head of the column, far ahead and small, one rider in blackened mail over a dark gambeson, WITHOUT a cloak, short straight black hair, rides forward and does not look back. In the lower foreground, seen from behind, the young soldier EXACTLY as in the character reference sits alone on a slope of dead brown grass, wrapped in an oversized black wool cloak, watching them go.
LIGHTING RECIPE: flat smoke-diffused overcast, pale white disc of sun low behind the hills; cold steel-blue grade; no warm light except one small dying fire.
Late-medieval continent of Kasran, overcast sky, cold diffused daylight, fine GREY ash flakes drifting slowly in the air (dark grey ash, never white snow), wet churned mud underfoot. Open country: no buildings, no walls, no castles, no towers — only mud, smoke, dead brown grass and distant bare hills. Rough wool, leather, blackened steel — nothing new, nothing clean, everything wet, scorched or frayed. Desaturated ash grey and steel slate with mud-brown shadows; the only warm colour in frame is real firelight. Low-key, real darkness allowed. Beautiful but brutal medieval reality, interrupted only rarely by overwhelming ancient myth.
Photoreal live-action cinema. Not illustration, not anime, not 3D render, not concept painting. ARRI Alexa look: fine 35mm grain, black pro-mist, soft halation, crushed blacks, shallow depth of field with clear foreground/midground/background separation. Practical light sources only. Epic scale but cold: thriller-noir tension with the intimacy of melodrama. 11th–13th century European material culture: mail armour, wool, linen, leather, timber, stone. No plate armour.
AVOID: column crossing the frame, rider looking back, cloak on the lead rider, curly hair, beard, fur, green grass, banners with readable symbols, crowds with visible faces, neon aura, glowing eyes, particle effects, magic sparkles, HUD or runes, glossy MMO rendering, plate armour, breastplate, cuirass, pauldrons, spaulders, riveted plates, spikes, superhero poses, idol-perfect faces, modern hairstyles, clean new clothing, centered symmetrical composition, crowds with visible faces, readable in-image text, random letters, labels, logos, watermarks, modern objects, modern shipping pallets, letterbox bars, black bars, white snow, snowflakes, snow on the ground, natural green vegetation.
```

### CUT37 — 멈춘다

**참조 이미지:**
- S5_FRONT_ELARA
- S5_FRONT_LIN
- S6_ASREN_FIRE (불 판정 기준)
- S16_EP01_CUT37 (구도)

```text
MANDATORY DRAMA IMAGE PREFIX (append to EVERY scene-image prompt, no exceptions):
— IDENTITY LOCK: render EXACTLY the same person(s) as the character-sheet reference — same face, age, hair, signature wardrobe. Never beautify, never average into a generic idol face. If two characters share a frame, each must match their own sheet.
— ANGLE BALANCE: pick ONE deliberate angle per shot from {high / low / side / dutch / over-the-shoulder / demai close-up / insert / object POV}, and never repeat the previous shot's angle. ZERO flat front-facing eye-level unless it is a designated peak-emotion reaction.
— DEPTH & TEXTURE: shallow depth of field (telephoto demai bokeh), clear FG/MG/BG separation; ARRI Alexa / ARRI look — filmic latitude, gentle organic softness (NOT clinical digital sharpness), fine 35mm grain, true-to-skin subsurface texture.
— LIGHTING & ART obey the shot's assigned lighting recipe and art-direction (color contrast / color balance) from STORYBOARD_PLAN; LOW-KEY by default, high-key ONLY where the recipe says so.

CINEMATIC PHOTOREAL DRAMA — REQUIRED ENHANCEMENT (append to every scene image):
A real frame from a premium cinema-grade TV drama — never CGI / 3D-render / illustration / video-game render. Heightened photoreal realism with lifelike skin micro-texture (visible pores, subsurface scattering, sharp eye catchlights).
FRAME: obey the project frame (horizontal 16:9 OR vertical 9:16) from STORYBOARD_PLAN. For vertical, keep the lower ~20% as clean defocused negative space for subtitles.
ANGLE BALANCE: use the shot's assigned angle (high / low / side / dutch / OTS / demai CU / insert / object POV); rotate angles between adjacent cuts; reserve dead-on eye-level for peak-emotion reactions only.
DEPTH: telephoto shallow depth of field (demai bokeh) with clear 3-layer FG/MG/BG separation.
LIGHTING: obey the assigned lighting recipe; LOW-KEY luxurious grade by default — deep controlled shadows, restrained highlights, motivated practicals; high-key only where the recipe specifies.
ART: obey the assigned art-direction — deliberate color contrast (subject separated from background by hue) and color balance (one dominant color + one complementary accent); fill FG/MG/BG, no dead space (except the subtitle margin); place the scene's signature/setup props.
Compose so cuts connect via match-cuts; frame as a keyframe primed for the assigned pace's motion.

CAMERA / FILM LOOK (ARRI): shot on ARRI Alexa (Alexa 65 for wides) with vintage anamorphic lenses; filmic latitude and highlight roll-off; gentle organic SOFTNESS — NOT clinical digital sharpness; fine-to-medium 35mm film grain (Vision3 500T feel); Black Pro-Mist halation bloom on highlights; anamorphic oval bokeh + subtle horizontal lens flare; crushed blacks, controlled low saturation, rich but not garish color; true cinematic contrast (chiaroscuro), never flat video-look.

PERSON CUT: exactly the SAME person as the character sheet (face, age, hair, wardrobe) — do not alter identity. Prefer 3/4 or over-the-shoulder framing and reaction close-ups over dead-on lip-sync framing (protects voice-lock dubbing later). Demai shallow DOF on the face; motivated key + negative fill; micro-expression readable.

16:9 frame. Low dutch angle from the floor, 24mm wide, NIGHT, inside a burning canvas refugee tent. A burning timber beam hangs in mid-air above a young woman, frozen dead still in mid-motion, razor-sharp edges with ZERO motion blur, as if caught by an impossibly fast shutter. The flames around her stand still like carved glass, their cores ivory-white; ash hangs motionless; a few flakes drift upward. The young woman EXACTLY as in her character reference, grey cloth over her hair, worn undyed linen dress, soot on her face, kneels clutching a six-year-old girl EXACTLY as in the child's reference (messy dark hair tied with a strip of grey cloth, torn grey tunic) to her chest, looking up at the beam. Foreground: out-of-focus frozen flame tongues. Background: burning tent wall with a torn opening, a blurred frozen silhouette of a man mid-stride.
LIGHTING RECIPE: NIGHT. The only light is the frozen fire itself — ivory-white flame cores fading to orange edges, hard and still; deep black shadows everywhere else.
Late-medieval continent of Kasran, night, a black smoke-filled sky, fine GREY ash flakes drifting slowly in the air (dark grey ash, never white snow), wet churned mud underfoot. A refugee camp in open country: only canvas tents, timber frames, ropes, mud and ash — no stone buildings, no walls, no castle, no town houses. Rough wool and linen, blackened steel — nothing new, nothing clean, everything wet, scorched or frayed. Desaturated ash grey and steel slate with mud-brown shadows; the only warm colour in frame is real firelight. Low-key, real darkness allowed. Beautiful but brutal medieval reality, interrupted only rarely by overwhelming ancient myth. When the firebird Asren is present: fire stops moving, ash rises instead of falling, flame cores turn ivory-white, motion slows by half a beat. Nothing glows, nothing sparkles.
Photoreal live-action cinema. Not illustration, not anime, not 3D render, not concept painting. ARRI Alexa look: fine 35mm grain, black pro-mist, soft halation, crushed blacks, shallow depth of field with clear foreground/midground/background separation. Practical light sources only. Epic scale but cold: thriller-noir tension with the intimacy of melodrama. 11th–13th century European material culture: mail armour, wool, linen, leather, timber, stone. No plate armour.
AVOID: daylight, overcast sky, motion blur, moving fire, glow, magic particles, blonde child, neon aura, glowing eyes, particle effects, magic sparkles, HUD or runes, glossy MMO rendering, plate armour, breastplate, cuirass, pauldrons, spaulders, riveted plates, spikes, superhero poses, idol-perfect faces, modern hairstyles, clean new clothing, centered symmetrical composition, crowds with visible faces, readable in-image text, random letters, labels, logos, watermarks, modern objects, modern shipping pallets, letterbox bars, black bars, white snow, snowflakes, snow on the ground, natural green vegetation.
```

### CUT38 — 날개

**참조 이미지:**
- S5_FRONT_ELARA
- S5_FRONT_LIN
- S6_ASREN_FIRE
- S16_EP01_CUT38 3차 (구도 — 필수)

```text
MANDATORY DRAMA IMAGE PREFIX (append to EVERY scene-image prompt, no exceptions):
— IDENTITY LOCK: render EXACTLY the same person(s) as the character-sheet reference — same face, age, hair, signature wardrobe. Never beautify, never average into a generic idol face. If two characters share a frame, each must match their own sheet.
— ANGLE BALANCE: pick ONE deliberate angle per shot from {high / low / side / dutch / over-the-shoulder / demai close-up / insert / object POV}, and never repeat the previous shot's angle. ZERO flat front-facing eye-level unless it is a designated peak-emotion reaction.
— DEPTH & TEXTURE: shallow depth of field (telephoto demai bokeh), clear FG/MG/BG separation; ARRI Alexa / ARRI look — filmic latitude, gentle organic softness (NOT clinical digital sharpness), fine 35mm grain, true-to-skin subsurface texture.
— LIGHTING & ART obey the shot's assigned lighting recipe and art-direction (color contrast / color balance) from STORYBOARD_PLAN; LOW-KEY by default, high-key ONLY where the recipe says so.

CINEMATIC PHOTOREAL DRAMA — REQUIRED ENHANCEMENT (append to every scene image):
A real frame from a premium cinema-grade TV drama — never CGI / 3D-render / illustration / video-game render. Heightened photoreal realism with lifelike skin micro-texture (visible pores, subsurface scattering, sharp eye catchlights).
FRAME: obey the project frame (horizontal 16:9 OR vertical 9:16) from STORYBOARD_PLAN. For vertical, keep the lower ~20% as clean defocused negative space for subtitles.
ANGLE BALANCE: use the shot's assigned angle (high / low / side / dutch / OTS / demai CU / insert / object POV); rotate angles between adjacent cuts; reserve dead-on eye-level for peak-emotion reactions only.
DEPTH: telephoto shallow depth of field (demai bokeh) with clear 3-layer FG/MG/BG separation.
LIGHTING: obey the assigned lighting recipe; LOW-KEY luxurious grade by default — deep controlled shadows, restrained highlights, motivated practicals; high-key only where the recipe specifies.
ART: obey the assigned art-direction — deliberate color contrast (subject separated from background by hue) and color balance (one dominant color + one complementary accent); fill FG/MG/BG, no dead space (except the subtitle margin); place the scene's signature/setup props.
Compose so cuts connect via match-cuts; frame as a keyframe primed for the assigned pace's motion.

CAMERA / FILM LOOK (ARRI): shot on ARRI Alexa (Alexa 65 for wides) with vintage anamorphic lenses; filmic latitude and highlight roll-off; gentle organic SOFTNESS — NOT clinical digital sharpness; fine-to-medium 35mm film grain (Vision3 500T feel); Black Pro-Mist halation bloom on highlights; anamorphic oval bokeh + subtle horizontal lens flare; crushed blacks, controlled low saturation, rich but not garish color; true cinematic contrast (chiaroscuro), never flat video-look.

PERSON CUT: exactly the SAME person as the character sheet (face, age, hair, wardrobe) — do not alter identity. Prefer 3/4 or over-the-shoulder framing and reaction close-ups over dead-on lip-sync framing (protects voice-lock dubbing later). Demai shallow DOF on the face; motivated key + negative fill; micro-expression readable.

16:9 frame. Low side angle, 24mm, off-center asymmetrical composition, NIGHT, in a burning refugee camp. The young woman EXACTLY as in her character reference walks from left to right across the lower-left third of frame, side profile, stooped, carrying the six-year-old girl EXACTLY as in the child's reference against her chest, looking down at the child, not at the camera. Grey cloth over her hair, worn undyed linen dress. Her sleeve passes straight through a tongue of flame and does not burn. The flames around her are frozen dead still, razor-sharp edges with ZERO motion blur; ivory-white cores; ash drifts upward. Along the very top edge of frame, cropped so the rest is far out of frame, hang the tips of a few gigantic FEATHERED flight feathers, dark against fire-lit smoke, each single feather longer than a whole tent; the enormous shadow of the wing sweeps diagonally across the smoke and the tent roofs behind her. No head, no eyes, no body, no second wing.
LIGHTING RECIPE: NIGHT. Frozen fire with ivory-white cores lights the woman from below; above, the smoke is lit dull orange and the wing's shadow cuts a vast dark diagonal across it.
Late-medieval continent of Kasran, night, a black smoke-filled sky, fine GREY ash flakes drifting slowly in the air (dark grey ash, never white snow), wet churned mud underfoot. A refugee camp in open country: only canvas tents, timber frames, ropes, mud and ash — no stone buildings, no walls, no castle, no town houses. Rough wool and linen, blackened steel — nothing new, nothing clean, everything wet, scorched or frayed. Desaturated ash grey and steel slate with mud-brown shadows; the only warm colour in frame is real firelight. Low-key, real darkness allowed. Beautiful but brutal medieval reality, interrupted only rarely by overwhelming ancient myth. When the firebird Asren is present: fire stops moving, ash rises instead of falling, flame cores turn ivory-white, motion slows by half a beat. Nothing glows, nothing sparkles.
Photoreal live-action cinema. Not illustration, not anime, not 3D render, not concept painting. ARRI Alexa look: fine 35mm grain, black pro-mist, soft halation, crushed blacks, shallow depth of field with clear foreground/midground/background separation. Practical light sources only. Epic scale but cold: thriller-noir tension with the intimacy of melodrama. 11th–13th century European material culture: mail armour, wool, linen, leather, timber, stone. No plate armour.
AVOID: complete bird, bird head, eyes, bat wing, dragon wing, leathery membrane, symmetrical wings, wings like a halo, walking toward camera, heroic pose, woman on fire, golden glow, metal barrels, daylight, neon aura, glowing eyes, particle effects, magic sparkles, HUD or runes, glossy MMO rendering, plate armour, breastplate, cuirass, pauldrons, spaulders, riveted plates, spikes, superhero poses, idol-perfect faces, modern hairstyles, clean new clothing, centered symmetrical composition, crowds with visible faces, readable in-image text, random letters, labels, logos, watermarks, modern objects, modern shipping pallets, letterbox bars, black bars, white snow, snowflakes, snow on the ground, natural green vegetation.
```

### CUT45 — 매듭을 두 번 확인한다

**참조 이미지:**
- S5_FRONT_ELARA
- S5_FRONT_RIVEN
- S5_FRONT_YORAN
- P5_ASH_CAMP (공간)
- S16_EP01_CUT45 (구도)

```text
MANDATORY DRAMA IMAGE PREFIX (append to EVERY scene-image prompt, no exceptions):
— IDENTITY LOCK: render EXACTLY the same person(s) as the character-sheet reference — same face, age, hair, signature wardrobe. Never beautify, never average into a generic idol face. If two characters share a frame, each must match their own sheet.
— ANGLE BALANCE: pick ONE deliberate angle per shot from {high / low / side / dutch / over-the-shoulder / demai close-up / insert / object POV}, and never repeat the previous shot's angle. ZERO flat front-facing eye-level unless it is a designated peak-emotion reaction.
— DEPTH & TEXTURE: shallow depth of field (telephoto demai bokeh), clear FG/MG/BG separation; ARRI Alexa / ARRI look — filmic latitude, gentle organic softness (NOT clinical digital sharpness), fine 35mm grain, true-to-skin subsurface texture.
— LIGHTING & ART obey the shot's assigned lighting recipe and art-direction (color contrast / color balance) from STORYBOARD_PLAN; LOW-KEY by default, high-key ONLY where the recipe says so.

CINEMATIC PHOTOREAL DRAMA — REQUIRED ENHANCEMENT (append to every scene image):
A real frame from a premium cinema-grade TV drama — never CGI / 3D-render / illustration / video-game render. Heightened photoreal realism with lifelike skin micro-texture (visible pores, subsurface scattering, sharp eye catchlights).
FRAME: obey the project frame (horizontal 16:9 OR vertical 9:16) from STORYBOARD_PLAN. For vertical, keep the lower ~20% as clean defocused negative space for subtitles.
ANGLE BALANCE: use the shot's assigned angle (high / low / side / dutch / OTS / demai CU / insert / object POV); rotate angles between adjacent cuts; reserve dead-on eye-level for peak-emotion reactions only.
DEPTH: telephoto shallow depth of field (demai bokeh) with clear 3-layer FG/MG/BG separation.
LIGHTING: obey the assigned lighting recipe; LOW-KEY luxurious grade by default — deep controlled shadows, restrained highlights, motivated practicals; high-key only where the recipe specifies.
ART: obey the assigned art-direction — deliberate color contrast (subject separated from background by hue) and color balance (one dominant color + one complementary accent); fill FG/MG/BG, no dead space (except the subtitle margin); place the scene's signature/setup props.
Compose so cuts connect via match-cuts; frame as a keyframe primed for the assigned pace's motion.

CAMERA / FILM LOOK (ARRI): shot on ARRI Alexa (Alexa 65 for wides) with vintage anamorphic lenses; filmic latitude and highlight roll-off; gentle organic SOFTNESS — NOT clinical digital sharpness; fine-to-medium 35mm film grain (Vision3 500T feel); Black Pro-Mist halation bloom on highlights; anamorphic oval bokeh + subtle horizontal lens flare; crushed blacks, controlled low saturation, rich but not garish color; true cinematic contrast (chiaroscuro), never flat video-look.

PERSON CUT: exactly the SAME person as the character sheet (face, age, hair, wardrobe) — do not alter identity. Prefer 3/4 or over-the-shoulder framing and reaction close-ups over dead-on lip-sync framing (protects voice-lock dubbing later). Demai shallow DOF on the face; motivated key + negative fill; micro-expression readable.

16:9 frame. Low angle, 35mm, DEEP FOCUS — a deliberate exception to the shallow-depth default for this one shot: foreground and background both sharp. In the sharp foreground, the young woman EXACTLY as in her character reference kneels in grey ash, cracked sooty hands pulling a strip of GREY cloth tight around a wooden splint on a young man's shin and holding the finished knot, checking it, looking only at the knot. The young man, EXACTLY as in his reference, lies wrapped in an oversized black wool cloak at the right edge of frame. In the background, also in focus, the man EXACTLY as in his character reference — blackened mail over a dark gambeson, NO cloak, no helmet, his sword SHEATHED at his hip — stands completely still, looking down at her hands, face unreadable. Blackened tent frames behind him.
LIGHTING RECIPE: cold blue-grey evening, soft and directionless; the only warm colour is a few dying embers in the background. Deep focus.
Late-medieval continent of Kasran, cold blue-grey evening dusk, fine GREY ash flakes drifting slowly in the air (dark grey ash, never white snow), wet churned mud underfoot. A refugee camp in open country: only canvas tents, timber frames, ropes, mud and ash — no stone buildings, no walls, no castle, no town houses. Rough wool and linen, blackened steel — nothing new, nothing clean, everything wet, scorched or frayed. Desaturated ash grey and steel slate with mud-brown shadows; the only warm colour in frame is real firelight. Low-key, real darkness allowed. Beautiful but brutal medieval reality, interrupted only rarely by overwhelming ancient myth.
Photoreal live-action cinema. Not illustration, not anime, not 3D render, not concept painting. ARRI Alexa look: fine 35mm grain, black pro-mist, soft halation, crushed blacks, shallow depth of field with clear foreground/midground/background separation. Practical light sources only. Epic scale but cold: thriller-noir tension with the intimacy of melodrama. 11th–13th century European material culture: mail armour, wool, linen, leather, timber, stone. No plate armour.
AVOID: drawn sword, sword in hand, cloak on the standing man, helmet, eye contact between them, eye contact with camera, tears, smiling, shallow focus on only one person, flames, neon aura, glowing eyes, particle effects, magic sparkles, HUD or runes, glossy MMO rendering, plate armour, breastplate, cuirass, pauldrons, spaulders, riveted plates, spikes, superhero poses, idol-perfect faces, modern hairstyles, clean new clothing, centered symmetrical composition, crowds with visible faces, readable in-image text, random letters, labels, logos, watermarks, modern objects, modern shipping pallets, letterbox bars, black bars, white snow, snowflakes, snow on the ground, natural green vegetation.
```

### CUT48 — 묶어라

**참조 이미지:**
- S6_FIREBIRD_MARK (문양 — 필수)
- S16_EP01_CUT48 2차 (구도)

```text
MANDATORY DRAMA IMAGE PREFIX (append to EVERY scene-image prompt, no exceptions):
— IDENTITY LOCK: render EXACTLY the same person(s) as the character-sheet reference — same face, age, hair, signature wardrobe. Never beautify, never average into a generic idol face. If two characters share a frame, each must match their own sheet.
— ANGLE BALANCE: pick ONE deliberate angle per shot from {high / low / side / dutch / over-the-shoulder / demai close-up / insert / object POV}, and never repeat the previous shot's angle. ZERO flat front-facing eye-level unless it is a designated peak-emotion reaction.
— DEPTH & TEXTURE: shallow depth of field (telephoto demai bokeh), clear FG/MG/BG separation; ARRI Alexa / ARRI look — filmic latitude, gentle organic softness (NOT clinical digital sharpness), fine 35mm grain, true-to-skin subsurface texture.
— LIGHTING & ART obey the shot's assigned lighting recipe and art-direction (color contrast / color balance) from STORYBOARD_PLAN; LOW-KEY by default, high-key ONLY where the recipe says so.

CINEMATIC PHOTOREAL DRAMA — REQUIRED ENHANCEMENT (append to every scene image):
A real frame from a premium cinema-grade TV drama — never CGI / 3D-render / illustration / video-game render. Heightened photoreal realism with lifelike skin micro-texture (visible pores, subsurface scattering, sharp eye catchlights).
FRAME: obey the project frame (horizontal 16:9 OR vertical 9:16) from STORYBOARD_PLAN. For vertical, keep the lower ~20% as clean defocused negative space for subtitles.
ANGLE BALANCE: use the shot's assigned angle (high / low / side / dutch / OTS / demai CU / insert / object POV); rotate angles between adjacent cuts; reserve dead-on eye-level for peak-emotion reactions only.
DEPTH: telephoto shallow depth of field (demai bokeh) with clear 3-layer FG/MG/BG separation.
LIGHTING: obey the assigned lighting recipe; LOW-KEY luxurious grade by default — deep controlled shadows, restrained highlights, motivated practicals; high-key only where the recipe specifies.
ART: obey the assigned art-direction — deliberate color contrast (subject separated from background by hue) and color balance (one dominant color + one complementary accent); fill FG/MG/BG, no dead space (except the subtitle margin); place the scene's signature/setup props.
Compose so cuts connect via match-cuts; frame as a keyframe primed for the assigned pace's motion.

CAMERA / FILM LOOK (ARRI): shot on ARRI Alexa (Alexa 65 for wides) with vintage anamorphic lenses; filmic latitude and highlight roll-off; gentle organic SOFTNESS — NOT clinical digital sharpness; fine-to-medium 35mm film grain (Vision3 500T feel); Black Pro-Mist halation bloom on highlights; anamorphic oval bokeh + subtle horizontal lens flare; crushed blacks, controlled low saturation, rich but not garish color; true cinematic contrast (chiaroscuro), never flat video-look.

INSERT / MACRO: no faces (or only hands / silhouette). Extreme shallow DOF, razor-thin focus plane, creamy anamorphic bokeh. The prop/gesture carries story meaning — shoot setup props and payoff props at the SAME angle so they read as the same object across the film. Dramatic hard backlight, halation bloom, strong color contrast; end on a surface/texture filling the frame for a match-cut hand-off.

16:9 frame. Extreme close-up insert, 100mm macro, framed tight on a thin young woman's wrists bound in front of her chest; rough hemp rope being wound around them by a man's gloved hands entering from the edge of frame. Her worn undyed linen dress covers both shoulders; only the collar has been tugged a little open by the movement. Just inside the collar, below the collarbone, the mark EXACTLY as in the mark reference — a thumbprint-sized blistered burn in the silhouette of a single flame, uneven seared edges, not glowing — and the linen is already sliding back over it, HALF HIDING it. Her face is out of frame.
LIGHTING RECIPE: the coldest image of the episode — flat blue-grey evening, no warm light at all.
Late-medieval continent of Kasran, cold blue-grey evening dusk, fine GREY ash flakes drifting slowly in the air (dark grey ash, never white snow), wet churned mud underfoot. A refugee camp in open country: only canvas tents, timber frames, ropes, mud and ash — no stone buildings, no walls, no castle, no town houses. Rough wool and linen, blackened steel — nothing new, nothing clean, everything wet, scorched or frayed. Desaturated ash grey and steel slate with mud-brown shadows; the only warm colour in frame is real firelight. Low-key, real darkness allowed. Beautiful but brutal medieval reality, interrupted only rarely by overwhelming ancient myth.
Photoreal live-action cinema. Not illustration, not anime, not 3D render, not concept painting. ARRI Alexa look: fine 35mm grain, black pro-mist, soft halation, crushed blacks, shallow depth of field with clear foreground/midground/background separation. Practical light sources only. Epic scale but cold: thriller-noir tension with the intimacy of melodrama. 11th–13th century European material culture: mail armour, wool, linen, leather, timber, stone. No plate armour.
AVOID: clean outlined flame, flame icon, emoji, tattoo, ink, large mark, fully visible mark, glowing, bare shoulder, off-shoulder, cleavage, sexualised framing, face, neon aura, glowing eyes, particle effects, magic sparkles, HUD or runes, glossy MMO rendering, plate armour, breastplate, cuirass, pauldrons, spaulders, riveted plates, spikes, superhero poses, idol-perfect faces, modern hairstyles, clean new clothing, centered symmetrical composition, crowds with visible faces, readable in-image text, random letters, labels, logos, watermarks, modern objects, modern shipping pallets, letterbox bars, black bars, white snow, snowflakes, snow on the ground, natural green vegetation.
```
