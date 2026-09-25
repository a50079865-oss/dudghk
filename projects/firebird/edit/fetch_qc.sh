#!/usr/bin/env bash
# 검수 결과를 qc/results 에서 가져온다.
#
# `git checkout qc/results -- <path>` 를 쓰면 안 된다. 그건 파일을 인덱스에
# 스테이징해서 추적을 되살리고, 그러면 CI 체크아웃에 낡은 판이 섞여
# 새 결과로 오인된다(그 버그를 한 번 겪었다). git show 는 인덱스를 건드리지 않는다.
set -euo pipefail

REF="${1:-origin/qc/results}"
DIR="projects/firebird/edit/qc"

git fetch -q origin "${REF#origin/}"
echo "가져오는 판: $(git log --oneline -1 "$REF")"

for f in contact_sheet.jpg waveform.png spectrogram.png report.md; do
    if git cat-file -e "$REF:$DIR/$f" 2>/dev/null; then
        git show "$REF:$DIR/$f" > "$DIR/$f"
        printf '  %-20s %s\n' "$f" "$(md5sum "$DIR/$f" | cut -c1-8)"
    else
        echo "  $f — 없음"
    fi
done
