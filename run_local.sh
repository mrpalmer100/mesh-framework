#!/usr/bin/env bash
# Local runner (author's laptop): loops a checkpointing driver until it prints a terminal line.
# Prefer ./go.sh <driver.py>, which is self-contained; this file is kept for reference.
set -u
DRV="$1"; NAME=$(basename "$DRV" .py); mkdir -p logs
PY=${PY:-$HOME/rope-venv/bin/python}; export SJ_MEMO=${SJ_MEMO:-jac}; fails=0
while true; do
  "$PY" -u "$DRV" >> "logs/$NAME.log" 2>&1; rc=$?
  tail -2 "logs/$NAME.log"
  if [ $rc -ne 0 ]; then fails=$((fails+1)); [ $fails -ge 3 ] && { echo "[$NAME] failing -- see logs/$NAME.log"; exit 1; }; sleep 2; continue; fi
  fails=0
  tail -1 "logs/$NAME.log" | grep -qE "COMPLETE|REFUSED|RESOLVED|run the verdict" && { echo "[$NAME] done"; break; }
  ls -td /tmp/sjjac_* 2>/dev/null | tail -n +3 | xargs -r rm -rf; ls -td /tmp/sjfac_* 2>/dev/null | tail -n +3 | xargs -r rm -rf
done
