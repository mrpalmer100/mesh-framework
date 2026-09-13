#!/usr/bin/env bash
# self-contained launcher: loops the driver with the venv python until its LAST log line is a terminal line.
# SJ_MEMO defaults to jac (Jacobian memos only; full memos wrote 2.6 GB factor files and filled the disk).
# Memo pruning uses ls -td: the memos are DIRECTORIES (/tmp/sjjac_*.pkl.d), and without -d nothing was pruned.
DRV="$1"; NAME=$(basename "$DRV" .py); mkdir -p logs
PY=$HOME/rope-venv/bin/python; export SJ_MEMO=${SJ_MEMO:-jac}
pkill -f "$NAME" 2>/dev/null; sleep 1
nohup bash -c '
  fails=0
  while true; do
    "'"$PY"'" -u "'"$DRV"'" >> "logs/'"$NAME"'.log" 2>&1; rc=$?
    if [ $rc -ne 0 ]; then fails=$((fails+1)); [ $fails -ge 3 ] && { echo "['"$NAME"'] failing -- see logs/'"$NAME"'.log" >> "logs/'"$NAME"'.log"; exit 1; }; sleep 2; continue; fi
    fails=0
    tail -1 "logs/'"$NAME"'.log" | grep -qE "COMPLETE|REFUSED|RESOLVED|run the verdict" && exit 0
    ls -td /tmp/sjjac_* 2>/dev/null | tail -n +3 | xargs rm -rf; ls -td /tmp/sjfac_* 2>/dev/null | tail -n +3 | xargs rm -rf
  done' > /dev/null 2>&1 &
echo "launched $DRV -> logs/$NAME.log"
