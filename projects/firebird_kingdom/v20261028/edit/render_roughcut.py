"""Render pilot rough cut v0: video concat (clip audio dropped) + dialogue/SFX mix + burned KO subtitles."""
import json, subprocess, sys, os
OUT = 'edit/out'; os.makedirs(OUT, exist_ok=True)
tl = json.load(open('edit/timeline_v0.json'))
cues = json.load(open('edit/sfx_cues_v0.json'))
jobs = json.load(open('edit/sfx_jobs_v0.json'))
TOTAL = tl['total_s']

def run(cmd):
    print(' '.join(cmd[:6]), '...', flush=True)
    subprocess.run(cmd, check=True)

# 1) video: trim + normalize every clip to 1920x1080/24fps, concat, no audio
if 'audio' not in sys.argv:
    inp, fc = [], []
    for k, c in enumerate(tl['clips']):
        inp += ['-i', c['src']]
        fc.append(f"[{k}:v]trim=start={c['in']}:duration={c['dur']},setpts=PTS-STARTPTS,"
                  f"scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,setsar=1,fps=24[v{k}]")
    fc.append(''.join(f'[v{k}]' for k in range(len(tl['clips']))) + f"concat=n={len(tl['clips'])}:v=1:a=0[v]")
    run(['ffmpeg', '-v', 'error', '-y', *inp, '-filter_complex', ';'.join(fc), '-map', '[v]',
         '-c:v', 'libx264', '-crf', '18', '-preset', 'medium', '-pix_fmt', 'yuv420p', f'{OUT}/video_nosub.mp4'])

# 2) audio mix
inp, fc, labels = [], [], []
def add(path, chain, loop=False):
    n = len(inp) // (4 if loop else 2)
    return path, chain
idx = 0
def inp_add(path, loop=False):
    global idx
    inp.extend((['-stream_loop', '-1'] if loop else []) + ['-i', path]); idx += 1
    return idx - 1
# dialogue
for d in tl['dialogue']:
    f = [x for x in os.listdir('edit/dialogue_trim') if x.startswith(f"{d['n']:02d}_")][0]
    i = inp_add(f'edit/dialogue_trim/{f}')
    ms = int(d['start'] * 1000)
    fc.append(f"[{i}:a]aformat=sample_rates=48000:channel_layouts=stereo,adelay={ms}|{ms}[d{d['n']}]"); labels.append(f"[d{d['n']}]")
# beds: loop, trim to scene span, fades, level
bed_gain = {'S03': 'loudnorm=I=-34:TP=-6', 'S08': 'volume=6dB'}
for b in cues['beds']:
    i = inp_add(f"edit/sfx/bed_{b['scene']}.mp3", loop=True)
    span = round(b['end'] - b['start'], 3); ms = int(b['start'] * 1000)
    lvl = bed_gain.get(b['scene'], 'loudnorm=I=-32:TP=-6')
    fc.append(f"[{i}:a]atrim=duration={span},{lvl},aformat=sample_rates=48000:channel_layouts=stereo,"
              f"afade=t=in:d=0.8,afade=t=out:st={max(0, span - 0.8)}:d=0.8,adelay={ms}|{ms}[b{b['scene']}]")
    labels.append(f"[b{b['scene']}]")
# spot effects
clip_start = {c['idx']: c['start'] for c in tl['clips']}
spot_lvl = {'56': 'loudnorm=I=-26:TP=-4', '49': 'loudnorm=I=-22:TP=-2', '53': 'loudnorm=I=-24:TP=-3'}
for key, s in jobs['spots'].items():
    i = inp_add(f'edit/sfx/spot_{key}.mp3')
    t = clip_start[s['idx']] + s['offset_s']; ms = int(t * 1000)
    fc.append(f"[{i}:a]{spot_lvl.get(key, 'loudnorm=I=-24:TP=-3')},aformat=sample_rates=48000:channel_layouts=stereo,adelay={ms}|{ms}[s{key}]")
    labels.append(f"[s{key}]")
fc.append(''.join(labels) + f"amix=inputs={len(labels)}:normalize=0:duration=longest,atrim=duration={TOTAL},alimiter=limit=0.89[mix]")
run(['ffmpeg', '-v', 'error', '-y', *inp, '-filter_complex', ';'.join(fc), '-map', '[mix]',
     '-c:a', 'pcm_s16le', '-ar', '48000', f'{OUT}/mix.wav'])

# 3) mux + burned KO subtitles
style = "Fontname=WenQuanYi Zen Hei,Fontsize=22,PrimaryColour=&H00FFFFFF,OutlineColour=&H80000000,BorderStyle=1,Outline=1.5,Shadow=0,MarginV=36"
run(['ffmpeg', '-v', 'error', '-y', '-i', f'{OUT}/video_nosub.mp4', '-i', f'{OUT}/mix.wav',
     '-vf', f"subtitles=edit/subtitles_ko_v0.srt:force_style='{style}'",
     '-map', '0:v', '-map', '1:a', '-c:v', 'libx264', '-crf', '20', '-preset', 'medium', '-pix_fmt', 'yuv420p',
     '-c:a', 'aac', '-b:a', '192k', '-shortest', f'{OUT}/firebird_pilot_roughcut_v0.mp4'])
print('done')
