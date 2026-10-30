# 《불새의 왕국》 작업 인계 (새 세션용) — 2026-10-29

## 현재 위치
STAGE 4(영상) 생성 완료 → 검수·오디오 단계 → STAGE 5(편집).
플레이북: `projects/firebird_kingdom/playbook/` (04_video, 05_edit). 모드 QUALITY, 엔진 Higgsfield.

## 확정된 것
- 스토리보드 62컷 = 본 컷 41 + 브릿지 21 → 재생 순서 `v20261028/storyboard/edit_sequence_v1.json`
- 컷별 최종 이미지 `v20261028/images_s24/jobs_s24.json` (picks), 브릿지 `storyboard/bridge_cuts_v1.json`
- 촬영 규칙 `storyboard/SHOT_GRAMMAR.md` (아이레벨 금지, 얕은 심도, ARRI, 로우키/네거티브필, 씬 사이 브릿지 2~3컷)
- 영상 62클립: 클링 3.0 pro 1080p, `v20261028/video/jobs_video_v1.json` (index 1~62 = edit_sequence 순서), 프롬프트 `video/video_prompts.json`
  - Higgsfield 프로젝트 b158e599-5e0b-45ba-a9b1-f9eac413b012, 폴더 「영상 v1」 88424093-1dbd-4d13-8733-1eb70f6a46e7
  - 결과 URL 형식: https://d8j0ntlcm91z4.cloudfront.net/user_33y5OecIsqLwjBCwWgIAggfjfGM/... (jobs_wait로 조회)
- 대사: **영어 음성 + 한글 자막** → `v20261028/voice_sheets/dialogue_en_ko_v1.json` (19줄)
- 목소리 후보(ElevenLabs flow C5b91gJsFTfUVnKwG3qI): `voice_sheets/voice_candidates_v1.json`
  - ELARA Mira 9XELrPIyVsbmAjCB3Bwh · TORVAL Rob N3KdYXuAuQCEeNRC4lXJ · ELDER Jon Peters iB5aLrknrSagc00jivta · OBSERVER Mark GU8Qu28KNb4JbhQV7DX7 (샘플 완료, 사용자 확정 대기)
  - RIVEN Joseph EtGAAwTx6aMveVbqUxuU 샘플 미생성(ElevenLabs 혼잡) · CHILD/SOLDIER 미정(보이스 디자인 필요)

## 검수 결과 (video/qa_video_v1.json)
- 샘플 3클립: 화면 OK, **오디오 FAIL** — 클링 sound=on이 BGM과 대본에 없는 영어 대사를 넣음.
- 결론: 클립 오디오는 전부 버린다. 편집에서 [효과음 레이어 새로 + 락 영어 음성 더빙 + 한글 자막(SRT)]으로 재구성. 영상 재생성 불필요.
- 토르발 가슴 문장이 '사슬 없는 흰 늑대' — 경미, 필요 시 재생성.

## 2026-10-29 세션2 진행
- 네트워크 OK: cloudfront mp4 HTTP 200. 62클립 URL → `video/video_urls_v1.json`
- 62클립 다운로드·프레임 검수 완료 → `video/qa_sheet_00~15.jpg`, 결과 `qa_video_v1.json` full_pass_20261029
  - 재생성 권장(중대): 53(C35 날개그림자→박쥐날개 드래곤 노출), 52(C34 하늘에 CG 소용돌이)
  - 선택: 41(배경 아치 십자가), 48(엘라라 눈 회녹색), 51(깃털 전에 손바닥 불씨), 33(늑대 깃발 형태 변형), 38(칼이 중간에 생김), 40(토르발 문장)
  - 클립 로컬 경로 video/clips/ 는 .gitignore (용량 542MB, URL로 재다운로드)
- 다음: 사용자에게 재생성 범위 확정 → 리븐/아이/부상병 목소리

## 2026-10-29 세션2 후반 진행
- 재생성: 52(C34)·53(C35) 통과, S04 원테이크 16s(앞 8s + 이어붙인 8s) → 22~24 대체 (video/regen_v2.json)
- 목소리 7명 락 (voice_candidates_v1.json locked), 부상병 대사 EN "...Just finish it." (ToS 필터)
- TTS 19/19 (voice_sheets/tts_v1, ElevenLabs 유료 플랜) → 무음 트림 edit/dialogue_trim
- SFX: Magnific 베드 9 + 스폿 20 (edit/sfx, 1,225크레딧), 큐 시트 edit/sfx_cues_v0.json
- 러프컷 v0: python3 edit/build_timeline.py && python3 edit/render_roughcut.py → edit/out/ (gitignore, 재렌더 가능)
  - 294.4s, 1920x1080, 믹스 -22.4 LUFS, 한글 자막 번인(WenQuanYi Zen Hei)
- 다음: 사용자 러프컷 피드백 → 컷 트림/타이밍, 나머지 SFX 스폿 47개(선택), 최종 라우드니스 -14~-16 LUFS 마스터

## 새 세션에서 할 일
1. 네트워크 확인: `curl -sI https://d8j0ntlcm91z4.cloudfront.net/...mp4` 가 200인지 (허용 주소: d8j0ntlcm91z4.cloudfront.net, d2ol7oe51mr4n9.cloudfront.net, upload.higgsfield.ai)
2. 62클립 다운로드 → ffmpeg 프레임 추출로 직접 화면 검수(얼굴·의상 드리프트, 십자가, 모션 깨짐) → 문제 컷만 재생성
3. 리븐·아이·부상병 목소리 후보 생성 → 사용자 확정 → 19줄 TTS(락 voice_id)
4. 효과음(SFX) 레이어 생성(BGM 금지), 한글 자막 SRT
5. STAGE 5: ffmpeg로 62클립 이어붙이기(클립 오디오 제거) + 대사/효과음 믹스 + 자막 → 파일럿 마스터
