"""Conform LatentSync outputs (25fps, ~4% shorter) back into 24fps clips of the original length.
LatentSync re-times frames to 25fps while lip motion follows the audio clock, so we keep its real
time (fps=24 drop/dup) and fill the missing tail: freeze for end-of-clip shots, or continue the
source from the next unused frame for the one-take."""
import subprocess, json
def dur(p): return float(subprocess.check_output(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',p]))
def frames(p): return int(subprocess.check_output(['ffprobe','-v','error','-count_frames','-select_streams','v','-show_entries','stream=nb_read_frames','-of','csv=p=0',p]))
L = 'edit/lipsync'
for c in (12, 26, 38, 40, 41, 47):
    src = f'video/clips/{c:02d}.mp4'; pad = dur(src) - dur(f'{L}/{c}_ls.mp4')
    subprocess.run(['ffmpeg','-v','error','-y','-i',f'{L}/{c}_ls.mp4','-vf',f'fps=24,tpad=stop_mode=clone:stop_duration={pad:.3f}',
                    '-t',f'{dur(src):.3f}','-an','-c:v','libx264','-crf','14','-preset','fast','-pix_fmt','yuv420p',f'{L}/final/{c:02d}.mp4'],check=True)
# one-take: lip-synced head (src frames 0..n-1) + one-take from frame n
n = frames(f'{L}/22_ls.mp4'); ot = 'video/clips_v2/S04_onetake_final.mp4'
subprocess.run(['ffmpeg','-v','error','-y','-i',f'{L}/22_ls.mp4','-i',ot,'-filter_complex',
    f'[0:v]fps=24,setpts=PTS-STARTPTS[a];[1:v]trim=start_frame={n},setpts=PTS-STARTPTS[b];[a][b]concat=n=2:v=1:a=0,format=yuv420p[v]',
    '-map','[v]','-c:v','libx264','-crf','14','-preset','fast',f'{L}/final/22.mp4'],check=True)
for c in (12,22,26,38,40,41,47): print(c, round(dur(f'{L}/final/{c:02d}.mp4'),3))
