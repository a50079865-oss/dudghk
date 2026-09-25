#!/usr/bin/env python3
"""
엔드 타이틀 카드 — 지시서 107행 "암전 + 엔드 타이틀 카드".

CI 러너에는 한글 글꼴이 없을 수 있으므로 여기서 렌더해 PNG 로 저장소에 넣는다.
빌드는 이 파일을 C062 의 소스로 쓴다.

  python3 make_endcard.py --out assets/C062_endcard.png
"""
import argparse
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

W, H = 1920, 1080
BG    = (6, 7, 9)          # 완전한 검정보다 한 단계 위 — 압축 밴딩을 피한다
BONE  = (216, 210, 200)    # 한국어 제목
DIM   = (122, 117, 108)    # 영문·부제
RULE  = (58, 56, 52)

FONTS = ["/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc",
         "/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc"]
LATIN = ["/usr/share/fonts/truetype/liberation/LiberationSerif-Regular.ttf",
         "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"]

def font(paths, size):
    for p in paths:
        if Path(p).exists():
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                pass
    return ImageFont.load_default()

def centered(d, y, text, f, fill, track=0):
    if track:
        widths = [d.textlength(ch, font=f) for ch in text]
        total = sum(widths) + track * (len(text) - 1)
        x = (W - total) / 2
        for ch, w in zip(text, widths):
            d.text((x, y), ch, font=f, fill=fill)
            x += w + track
        return
    w = d.textlength(text, font=f)
    d.text(((W - w) / 2, y), text, font=f, fill=fill)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="assets/C062_endcard.png")
    a = ap.parse_args()

    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)

    centered(d, 392, "불새의 왕국", font(FONTS, 104), BONE)
    centered(d, 536, "1화 — 재가 내리는 길", font(FONTS, 46), DIM)
    d.line([(W/2 - 150, 626), (W/2 + 150, 626)], fill=RULE, width=2)
    centered(d, 664, "THE KINGDOM OF THE FIREBIRD",
             font(LATIN, 27), DIM, track=7)

    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    im.save(a.out)
    print(f"{a.out}  {W}x{H}")

if __name__ == "__main__":
    main()
