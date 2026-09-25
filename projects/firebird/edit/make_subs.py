#!/usr/bin/env python3
"""
자막 타임코드를 매니페스트에서 다시 만든다.

컷 순서나 길이를 바꾸면 SRT 의 절대 시각이 전부 낡는다. 대사 텍스트와
표시 길이는 기존 SRT 에서 그대로 가져오고, 시작 시각만 다시 계산한다.

  python3 make_subs.py --manifest manifest.json --subs ../v2026-09-19/subtitles
"""
import argparse, json, re
from pathlib import Path


def parse_srt(p):
    blocks, cur = [], []
    for line in Path(p).read_text(encoding="utf-8").splitlines():
        if line.strip() == "":
            if cur:
                blocks.append(cur); cur = []
        else:
            cur.append(line)
    if cur:
        blocks.append(cur)
    out = []
    for b in blocks:
        m = re.match(r"(\d+):(\d+):(\d+),(\d+)\s*-->\s*(\d+):(\d+):(\d+),(\d+)", b[1])
        g = [int(x) for x in m.groups()]
        st = g[0]*3600 + g[1]*60 + g[2] + g[3]/1000
        en = g[4]*3600 + g[5]*60 + g[6] + g[7]/1000
        out.append({"dur": en - st, "text": b[2:]})
    return out


def ts(t):
    h, rem = divmod(t, 3600); mi, s = divmod(rem, 60)
    return f"{int(h):02d}:{int(mi):02d}:{int(s):02d},{int(round((s%1)*1000)):03d}"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", default="manifest.json")
    ap.add_argument("--subs", default="../v2026-09-19/subtitles")
    a = ap.parse_args()

    man = json.loads(Path(a.manifest).read_text())
    starts, t = {}, 0.0
    for e in man["timeline"]:
        starts[e["cut"]] = t; t += e["dur"]

    # 화면에 자막이 붙는 대사만. C018 은 설계상 자막을 넣지 않는다.
    lines = [d for d in man["dialogue"] if d.get("subtitle", True)]

    for lang in ("ko", "en"):
        src = Path(a.subs) / f"EP01_part1.{lang}.srt"
        if not src.exists():
            print(f"  {src.name} 없음 — 건너뜀"); continue
        old = parse_srt(src)
        if len(old) != len(lines):
            raise SystemExit(f"{src.name}: 자막 {len(old)}개 vs 대사 {len(lines)}개 — "
                             "수가 맞지 않아 안전하게 멈춘다")
        out = []
        for i, (d, o) in enumerate(zip(lines, old), 1):
            st = starts[d["cut"]] + d["offset"]
            out.append(f"{i}\n{ts(st)} --> {ts(st + o['dur'])}\n" + "\n".join(o["text"]) + "\n")
        src.write_text("\n".join(out), encoding="utf-8")
        print(f"  {src.name} — {len(out)}줄 재계산")


if __name__ == "__main__":
    main()
