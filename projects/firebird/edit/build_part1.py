#!/usr/bin/env python3
"""
EP1 1부 빌드 — 편집 지시서(27_EP01_PART1_EDIT_SHEET.md)를 그대로 실행한다.

  python3 build_part1.py --media ./media --out part1.mp4 [--burn-subs] [--draft]

미디어 배치 (컷 번호로 이름을 맞춘다):
  media/C001.png ... media/C061.png      C 계층 스틸
  media/C002.mp4 ... media/C061.mp4      A·B 계층 영상 (C027·C031·C035·C041은 립싱크 판)
  media/dlg/<id>.mp3                     오프스크린 대사 3줄
  media/beds/<name>.wav                  앰비언스 베드
  media/sfx/<cut>.wav                    SFX 타점 (선택 — 없어도 통과한다)

컷·대사·베드·스코어가 하나라도 없으면 끝에서 종료 코드 1로 멈춘다.
빠진 그림은 검은 화면, 빠진 소리는 무음으로 나가는데 둘 다 조용해서
성공과 구별되지 않기 때문이다. 확인이 끝날 때까지 건너뛰려면 소스를 채워라.
"""
import argparse, json, os, re, subprocess, sys, shutil
from pathlib import Path

try:
    import imageio_ffmpeg
    FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()
except Exception:
    FFMPEG = shutil.which("ffmpeg") or "ffmpeg"
FFPROBE = shutil.which("ffprobe")   # 없으면 ffmpeg 자체로 탐지한다

W = int(os.environ.get("FIREBIRD_W", 1920))   # 테스트용 축소 오버라이드
H = int(os.environ.get("FIREBIRD_H", 1080))
FPS = 24          # --draft 가 아니면 소스에서 감지해 덮어쓴다
SAMPLE = 48000

def run(args, quiet=True):
    r = subprocess.run(args, capture_output=True, text=True)
    if r.returncode != 0:
        sys.stderr.write("\n[ffmpeg 실패] " + " ".join(args[:12]) + " ...\n")
        sys.stderr.write(r.stderr[-1500:] + "\n")
        raise SystemExit(1)
    return r

def _ff_info(path):
    """ffprobe 가 없는 환경이 많다. ffmpeg 의 stderr 를 읽어 대체한다."""
    r = subprocess.run([FFMPEG, "-hide_banner", "-i", str(path)], capture_output=True, text=True)
    return r.stderr

def probe_fps(path):
    if FFPROBE:
        r = subprocess.run([FFPROBE, "-v", "0", "-of", "csv=p=0", "-select_streams", "v:0",
                            "-show_entries", "stream=r_frame_rate", str(path)],
                           capture_output=True, text=True)
        try:
            n, d = r.stdout.strip().split("/"); return round(int(n) / int(d), 3)
        except Exception:
            pass
    m = re.search(r"(\d+(?:\.\d+)?)\s+fps", _ff_info(path))
    return float(m.group(1)) if m else None

def probe_duration(path):
    if FFPROBE:
        r = subprocess.run([FFPROBE, "-v", "0", "-show_entries", "format=duration",
                            "-of", "csv=p=0", str(path)], capture_output=True, text=True)
        try:
            return float(r.stdout.strip())
        except Exception:
            pass
    m = re.search(r"Duration:\s*(\d+):(\d+):(\d+(?:\.\d+)?)", _ff_info(path))
    if not m:
        return 0.0
    h, mi, se = m.groups(); return int(h) * 3600 + int(mi) * 60 + float(se)

def has_audio(path):
    if FFPROBE:
        r = subprocess.run([FFPROBE, "-v", "0", "-select_streams", "a", "-show_entries",
                            "stream=index", "-of", "csv=p=0", str(path)], capture_output=True, text=True)
        return bool(r.stdout.strip())
    return "Audio:" in _ff_info(path)

# ── 켄번스 ────────────────────────────────────────────────────────────────
# 지시서 §4: 8초 컷의 총 이동량이 4~6%. 눈에 보이는 줌은 실패다.
# 지터를 줄이려고 4K로 올린 뒤 zoompan 을 걸고 1920x1080 으로 내린다.
def ken_burns(mode, z0, z1, dur, fps):
    n = max(1, int(round(dur * fps)))
    if mode == "hold":
        return f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H}"
    z = f"{z0}+({z1}-{z0})*on/{n}"          # 선형
    if mode in ("in", "out"):
        z = f"{z0}+({z1}-{z0})*(1-pow(1-on/{n},2))"   # ease-out
    x, y = "iw/2-(iw/zoom/2)", "ih/2-(ih/zoom/2)"
    if mode == "tilt_down":   y = f"(ih-ih/zoom)*(on/{n})"
    elif mode == "tilt_up":   y = f"(ih-ih/zoom)*(1-on/{n})"
    elif mode == "pan_right": x = f"(iw-iw/zoom)*(on/{n})"
    return (f"scale=3840:-2:flags=lanczos,"
            f"zoompan=z='{z}':x='{x}':y='{y}':d={n}:s={W}x{H}:fps={fps},"
            f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H}")

def find_media(media, cut, exts, entry=None):
    # 저장소가 직접 들고 있는 소스(엔드 타이틀 카드 등)가 우선한다.
    if entry and entry.get("source"):
        p = Path(__file__).resolve().parent / entry["source"]
        if p.exists():
            return p
    for e in exts:
        p = media / f"{cut}{e}"
        if p.exists():
            return p
    return None

def build_segment(entry, media, work, fps, crf):
    cut, dur = entry["cut"], entry["dur"]
    # 디졸브는 두 컷을 겹치므로 그만큼 총 길이가 줄어든다.
    # 나가는 컷에 전환 길이만큼 핸들을 붙여 420초를 유지한다.
    t = entry.get("transition_after")
    if t and t["type"] == "dissolve":
        dur = round(dur + t["seconds"], 3)
    out = work / f"seg_{cut}.mp4"
    venc = ["-c:v", "libx264", "-preset", "veryfast", "-crf", str(crf),
            "-pix_fmt", "yuv420p", "-r", str(fps), "-video_track_timescale", "90000"]
    aenc = ["-c:a", "aac", "-b:a", "192k", "-ar", str(SAMPLE), "-ac", "2"]

    if entry["kind"] == "still":
        src = find_media(media, cut, [".png", ".jpg", ".jpeg", ".webp"], entry)
        kbs = entry.get("ken_burns", {"mode": "in", "from": 1.0, "to": 1.04})
        if src is None:                       # 없으면 검은 화면으로 자리를 지킨다
            vf = f"color=c=black:s={W}x{H}:r={fps}:d={dur}"
            run([FFMPEG, "-y", "-f", "lavfi", "-i", vf,
                 "-f", "lavfi", "-i", f"anullsrc=r={SAMPLE}:cl=stereo",
                 "-t", str(dur), *venc, *aenc, "-shortest", str(out)])
            return out, False
        vf = ken_burns(kbs["mode"], kbs["from"], kbs["to"], dur, fps)
        run([FFMPEG, "-y", "-loop", "1", "-i", str(src),
             "-f", "lavfi", "-i", f"anullsrc=r={SAMPLE}:cl=stereo",
             "-t", str(dur), "-vf", vf, *venc, *aenc, "-shortest", str(out)])
        return out, True

    src = find_media(media, cut, [".mp4", ".mov", ".mkv", ".webm"], entry)
    if src is None:
        run([FFMPEG, "-y", "-f", "lavfi", "-i", f"color=c=black:s={W}x{H}:r={fps}:d={dur}",
             "-f", "lavfi", "-i", f"anullsrc=r={SAMPLE}:cl=stereo",
             "-t", str(dur), *venc, *aenc, "-shortest", str(out)])
        return out, False
    # 클립이 지시서의 길이보다 짧으면 마지막 프레임을 물리고, 길면 자른다.
    pre = ""
    cr = entry.get("crop")
    if cr:
        # 픽셀이 아니라 비율로 자른다 — 소스 해상도가 달라도 같은 그림이 나온다.
        keep = 1.0 - cr["drop_top"]
        pre = (f"crop=w='min(iw\\,ih*{keep}*16/9)':h='ih*{keep}'"
               f":x='(iw-ow)/2':y='ih*{cr['drop_top']}',")
    vf = (f"{pre}scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},"
          f"tpad=stop_mode=clone:stop_duration=6,fps={fps}")
    run([FFMPEG, "-y", "-i", str(src),
         "-f", "lavfi", "-i", f"anullsrc=r={SAMPLE}:cl=stereo",
         "-t", str(dur), "-vf", vf,
         "-filter_complex", "[0:a]apad[a0];[1:a]anull[a1];[a0][a1]amix=inputs=2:duration=first:normalize=0[aout]",
         "-map", "0:v", "-map", "[aout]", *venc, *aenc, str(out)]) if has_audio(src) else \
    run([FFMPEG, "-y", "-i", str(src),
         "-f", "lavfi", "-i", f"anullsrc=r={SAMPLE}:cl=stereo",
         "-t", str(dur), "-vf", vf, "-map", "0:v", "-map", "1:a", *venc, *aenc, str(out)])
    return out, True

def crossfade(a, b, seconds, out, fps, crf):
    """두 세그먼트 사이 디졸브. 지시서 §5 — 예외 2곳에만 쓴다."""
    da = probe_duration(a)
    off = max(0.0, da - seconds)
    run([FFMPEG, "-y", "-i", str(a), "-i", str(b),
         "-filter_complex",
         f"[0:v][1:v]xfade=transition=fade:duration={seconds}:offset={off}[v];"
         f"[0:a][1:a]acrossfade=d={seconds}[a]",
         "-map", "[v]", "-map", "[a]",
         "-c:v", "libx264", "-preset", "veryfast", "-crf", str(crf), "-pix_fmt", "yuv420p",
         "-r", str(fps), "-c:a", "aac", "-b:a", "192k", "-ar", str(SAMPLE), "-ac", "2", str(out)])

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--media", default="./media")
    ap.add_argument("--out", default="part1.mp4")
    ap.add_argument("--manifest", default=str(Path(__file__).with_name("manifest.json")))
    ap.add_argument("--subs", default=None, help="한국어 SRT 경로")
    ap.add_argument("--burn-subs", action="store_true", help="자막을 화면에 굽는다 (기본은 소프트 트랙)")
    ap.add_argument("--draft", action="store_true", help="빠른 확인용 저화질")
    ap.add_argument("--keep-work", action="store_true")
    a = ap.parse_args()

    man = json.loads(Path(a.manifest).read_text())
    media = Path(a.media)
    work = Path(a.out).resolve().parent / ".build_part1"
    work.mkdir(parents=True, exist_ok=True)
    crf = 30 if a.draft else 17

    # fps 는 소스에서 감지한다 — 지시서 §9: 변환하면 모션이 끊긴다.
    fps = FPS
    for e in man["timeline"]:
        if e["kind"] == "video":
            p = find_media(media, e["cut"], [".mp4", ".mov", ".mkv", ".webm"])
            if p:
                f = probe_fps(p)
                if f:
                    fps = int(round(f)); break
    print(f"[fps] {fps}")

    segs, missing = [], []
    for e in man["timeline"]:
        p, found = build_segment(e, media, work, fps, crf)
        segs.append((e, p))
        if not found:
            missing.append(e["cut"])
        print(f"  {e['cut']}  {e['dur']:>2}s  {e['kind']:<5} "
              f"{'' if found else '(미디어 없음 → 검은 화면)'}")

    # 디졸브가 지정된 자리만 두 세그먼트를 하나로 합친다.
    merged, i = [], 0
    while i < len(segs):
        e, p = segs[i]
        t = e.get("transition_after")
        if t and t["type"] == "dissolve" and i + 1 < len(segs):
            out = work / f"xf_{e['cut']}.mp4"
            crossfade(p, segs[i + 1][1], t["seconds"], out, fps, crf)
            merged.append(out); i += 2
        else:
            merged.append(p); i += 1

    lst = work / "concat.txt"
    lst.write_text("".join(f"file '{Path(m).resolve()}'\n" for m in merged))
    body = work / "body.mp4"
    run([FFMPEG, "-y", "-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy", str(body)])

    # ── 오디오 레이어 ────────────────────────────────────────────────
    starts = {e["cut"]: e["start"] for e in man["timeline"]}
    durs = {e["cut"]: e["dur"] for e in man["timeline"]}
    inputs, filters, labels = ["-i", str(body)], [], ["[0:a]"]
    idx = 1

    def add(path, at, gain_db=0.0):
        nonlocal idx
        inputs.extend(["-i", str(path)])
        lab = f"[l{idx}]"
        filters.append(f"[{idx}:a]adelay={int(at*1000)}|{int(at*1000)},volume={gain_db}dB{lab}")
        labels.append(lab); idx += 1

    for d in man["dialogue"]:
        if d.get("baked_in_clip"):
            continue                      # 립싱크 클립에 이미 들어 있다
        f = media / "dlg" / f"{d['audio']}.mp3"
        if f.exists():
            add(f, starts[d["cut"]] + d["offset"])
        else:
            missing.append(f"dlg/{d['audio']}")

    def pick(d, stem):
        for ext in (".wav", ".mp3", ".m4a", ".ogg"):
            q = media / d / f"{stem}{ext}"
            if q.exists():
                return q
        return None

    for b in man["ambience_beds"]:
        # 다른 구간의 베드를 빌려 쓸 수 있다 — 캐논이 "같은 베드"를 지시하는 자리가 있다.
        stem = b.get("file", b["name"])
        f = pick("beds", stem)
        if f is None:
            f = media / "beds" / f"{stem}.wav"
        if not f.exists():
            missing.append(f"beds/{stem}")
            continue
        # 베드는 30초 한도로 생성되므로 구간 길이만큼 이어 붙인다.
        seg_start = starts[b["from"]]
        seg_end = starts[b["to"]] + durs[b["to"]]
        need = seg_end - seg_start
        src_len = probe_duration(f) or 1.0
        # 같은 파일을 두 구간에 쓰면 루프가 겹쳐 들린다. 시작점을 어긋내 준다.
        off = float(b.get("offset", 0.0)) % src_len
        loops = max(0, int((need + off) // src_len) + 1)
        inputs.extend(["-stream_loop", str(loops), "-i", str(f)])
        lab = f"[l{idx}]"
        filters.append(f"[{idx}:a]atrim={off:.3f}:{off + need:.3f},asetpts=PTS-STARTPTS,"
                       f"afade=t=in:st=0:d=0.75,afade=t=out:st={max(0,need-0.75):.3f}:d=0.75,"
                       f"adelay={int(seg_start*1000)}|{int(seg_start*1000)},volume={b['db']}dB{lab}")
        labels.append(lab); idx += 1

    for sx in man["sfx"]:
        f = pick("sfx", sx["cut"])
        if f:
            add(f, starts[sx["cut"]] + sx["at"])

    # ── 스코어 ──────────────────────────────────────────────
    # 전편에 깔지 않는다. 세 번만, 자리값을 하는 곳에.
    for cue in man.get("score", []):
        f = pick("score", cue["name"])
        if f is None:
            missing.append(f"score/{cue['name']}")
            continue
        use = float(cue["use"])
        inputs.extend(["-i", str(f)])
        lab = f"[l{idx}]"
        filters.append(
            f"[{idx}:a]atrim=0:{use:.3f},asetpts=PTS-STARTPTS,"
            f"afade=t=in:st=0:d=1.5,afade=t=out:st={max(0.0, use-2.5):.3f}:d=2.5,"
            f"adelay={int(cue['start']*1000)}|{int(cue['start']*1000)},"
            f"volume={cue['db']}dB{lab}")
        labels.append(lab); idx += 1

    if len(labels) > 1:
        filters.append("".join(labels) + f"amix=inputs={len(labels)}:duration=first:normalize=0[mixed]")
        amap = "[mixed]"
    else:
        amap = "[0:a]"

    # 의도적 침묵 — 지시서 §6. 해당 구간만 게이트로 눌러 둔다.
    for sil in man["silences"]:
        c = sil["cut"]; st = starts[c] + sil.get("from_offset", 0.0)
        en = starts[c] + durs[c] if sil.get("whole") else st + 14.0
        nxt = f"[s{c}]"
        filters.append(f"{amap}volume=enable='between(t,{st},{en})':volume=0{nxt}")
        amap = nxt

    filters.append(f"{amap}loudnorm=I=-14:TP=-1:LRA=11[aout]")

    vf = []
    if a.burn_subs and a.subs and Path(a.subs).exists():
        vf = ["-vf", f"subtitles={a.subs}:force_style='FontSize=22,Outline=1,Shadow=0,MarginV=60'"]

    cmd = [FFMPEG, "-y", *inputs, "-filter_complex", ";".join(filters),
           "-map", "0:v", "-map", "[aout]", *vf,
           "-c:v", ("libx264" if (vf or a.draft) else "copy")]
    if vf or a.draft:
        cmd += ["-preset", "medium", "-crf", str(crf), "-pix_fmt", "yuv420p"]
    cmd += ["-c:a", "aac", "-b:a", "384k", "-ar", str(SAMPLE), "-ac", "2",
            "-colorspace", "bt709", "-color_primaries", "bt709", "-color_trc", "bt709",
            "-movflags", "+faststart", str(a.out)]
    run(cmd)

    # 자막 소프트 트랙 (기본)
    if a.subs and Path(a.subs).exists() and not a.burn_subs:
        tmp = str(a.out) + ".subbed.mp4"
        run([FFMPEG, "-y", "-i", str(a.out), "-i", a.subs,
             "-c", "copy", "-c:s", "mov_text", "-metadata:s:s:0", "language=kor", tmp])
        os.replace(tmp, a.out)

    dur = probe_duration(a.out)
    print(f"\n완성: {a.out}  ({dur:.2f}초 / 목표 420초)")
    if not a.keep_work:
        shutil.rmtree(work, ignore_errors=True)
    if missing:
        # 빠진 컷은 검은 화면으로, 빠진 스코어·앰비언스는 무음으로 나간다.
        # 둘 다 조용해서 성공과 구별되지 않으므로, 여기서 멈춘다.
        print(f"빠진 소스 {len(missing)}건: {', '.join(missing[:12])}"
              f"{' …' if len(missing) > 12 else ''}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
