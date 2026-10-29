"""Rough-cut timeline v0 + KO subtitle SRT draft + SFX cue sheet."""
import json, subprocess, re, os
V = 'video'
def dur(p):
    return float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',p]).decode())
prompts = {it['index']: it for it in json.load(open(f'{V}/video_prompts.json'))['items']}

# --- timeline ---
tl, t = [], 0.0
for i in range(1, 63):
    if i in (23, 24):
        continue
    if i == 22:
        src, d, slot, note = f'{V}/clips_v2/S04_onetake_final.mp4', dur(f'{V}/clips_v2/S04_onetake_final.mp4'), 'C14-C16', 'S04 one-take (replaces 22-24)'
    elif i == 52:
        src, d, slot, note = f'{V}/clips_v2/52.mp4', 3.0, 'C34', 'regen v2, trimmed to first 3s'
    elif i == 53:
        src, d, slot, note = f'{V}/clips_v2/53.mp4', dur(f'{V}/clips_v2/53.mp4'), 'C35', 'regen v2'
    else:
        src = f'{V}/clips/{i:02d}.mp4'; d = dur(src); slot = prompts[i]['slot']; note = ''
    p = prompts[i]
    action = p['prompt'].split('ACTION:')[-1].strip()
    tl.append({'idx': i, 'slot': slot, 'scene': p['scene'], 'src': src, 'in': 0.0, 'dur': round(d, 3),
               'start': round(t, 3), 'end': round(t + d, 3), 'action': action, 'note': note})
    t += d
by_idx = {c['idx']: c for c in tl}

# --- dialogue placement (estimated until TTS durations are known) ---
dlg = json.load(open('voice_sheets/dialogue_en_ko_v1.json'))['lines']
tts_dir = 'edit/dialogue_trim' if os.path.isdir('edit/dialogue_trim') else 'voice_sheets/tts_v1'
def line_len(n, en):
    f = [x for x in os.listdir(tts_dir) if x.startswith(f'{n:02d}_')] if os.path.isdir(tts_dir) else []
    if f:
        return dur(os.path.join(tts_dir, f[0])), 'tts'
    words = len(re.findall(r"[A-Za-z']+", en))
    return round(0.6 + words / 2.6, 2), 'est'
# offsets inside clips for slots whose action timing is known
offset = {22: 1.0}          # soldier speaks while knife is at throat (one-take 0-3s)
cursor, subs = 0.0, []
for n, l in enumerate(dlg, 1):
    clip = by_idx[l['video_slot']]
    st = max(clip['start'] + offset.get(l['video_slot'], 0.4), cursor + 0.25)
    d, kind = line_len(n, l['en'])
    subs.append({'n': n, 'speaker': l['speaker'], 'slot': l['video_slot'], 'start': round(st, 2),
                 'end': round(st + d, 2), 'len_src': kind, 'en': l['en'], 'ko': l['ko']})
    cursor = st + d

def ts(x):
    h, r = divmod(x, 3600); m, s = divmod(r, 60)
    return f'{int(h):02d}:{int(m):02d}:{int(s):02d},{int(round((s - int(s)) * 1000)):03d}'
with open('edit/subtitles_ko_v0.srt', 'w') as f:
    for k, s in enumerate(subs):
        end = s['end'] + 0.3
        if k + 1 < len(subs):
            end = min(end, subs[k + 1]['start'] - 0.05)
        f.write(f"{s['n']}\n{ts(s['start'])} --> {ts(end)}\n{s['ko']}\n\n")

json.dump({'version': 'rough_v0', 'fps': 24, 'resolution': '1928x1076', 'total_s': round(t, 2),
           'rules': 'clip audio muted; A1 dialogue (EN), A2 SFX, no BGM; KO subtitles',
           'clips': tl, 'dialogue': subs}, open('edit/timeline_v0.json', 'w'), ensure_ascii=False, indent=1)
print('total', round(t, 2), 'clips', len(tl), 'lines', len(subs))
for s in subs: print(s['n'], s['speaker'], s['start'], s['end'], s['len_src'])
