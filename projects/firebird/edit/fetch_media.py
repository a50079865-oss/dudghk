#!/usr/bin/env python3
"""
매니페스트의 모든 소스를 media/ 로 내려받는다.

  python3 fetch_media.py --urls urls.json --out ./media

urls.json 은 {"C001": "https://...", "dlg/MBuVwMVDCm": "https://..."} 형태다.
Magnific 의 creations_deliver 가 주는 주소를 그대로 넣으면 된다.

⚠️ 현재 이 컨테이너에서는 pikaso.cdnpk.net 이 조직 이그레스 정책에 막혀 있다.
   환경 네트워크 정책에서 그 호스트를 허용하면 이 스크립트가 바로 동작한다.
"""
import argparse, json, os, sys, urllib.request
from pathlib import Path

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--urls", required=True)
    ap.add_argument("--out", default="./media")
    a = ap.parse_args()
    urls = json.loads(Path(a.urls).read_text())
    out = Path(a.out); ok = fail = 0
    for name, url in urls.items():
        dest = out / name
        if dest.suffix == "":
            dest = dest.with_suffix(".mp4" if "mp4" in url else ".png" if "png" in url else ".mp3")
        dest.parent.mkdir(parents=True, exist_ok=True)
        if dest.exists() and dest.stat().st_size > 0:
            print(f"  건너뜀 {dest.name}"); ok += 1; continue
        try:
            urllib.request.urlretrieve(url, dest)
            print(f"  받음  {dest.name}  ({dest.stat().st_size:,} bytes)"); ok += 1
        except Exception as e:
            print(f"  실패  {dest.name}: {e}", file=sys.stderr); fail += 1
    print(f"\n완료 {ok}건 / 실패 {fail}건")
    if fail:
        print("\n실패가 전부 pikaso.cdnpk.net 이면 두 가지 중 하나다:")
        print("  1) 토큰 만료 — 주소를 다시 뽑아야 한다")
        print("  2) 네트워크에서 그 호스트가 막혀 있다")
        # 조용히 성공하면 소스가 빠진 채로 영화가 나온다. 그건 성공이 아니다.
        sys.exit(1)

if __name__ == "__main__":
    main()
