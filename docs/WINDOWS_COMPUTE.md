# Running drivers on a Windows compute box (no admin required)

The drivers are pure Python; only the launcher was bash. Since 2026-09-13
the solver's memo files go to the platform temp directory (tempfile.
gettempdir(): /tmp on Unix, %TEMP% on Windows) and go.py replaces go.sh.

DISK (2026-10-04, after the box filled twice in one day). The sparse-Jacobian
instrument writes a factor memo of ~0.6 GB per factorisation into %TEMP% when
SJ_MEMO is unset; go.py sets SJ_MEMO=jac (no factor memos) and prunes between
invocations, but a hand-rolled PowerShell loop does neither. Since 2026-10-04 the
instrument prunes its own memos (sparsej_instrument._prune_memos, newest two of
each kind kept), so no launcher can refill the disk; the ANTI-ARC-NYQ driver also
refuses to start under 20 GB free. House rule for any PC run: launch through
go.py (which since 2026-10-07 takes an optional terminal pattern, e.g. COMPLETE for the ANTI-ARC drivers
that print REFUSED per point, and refuses to launch under 20 GB free), never a hand-rolled loop; check free space and the memo count once
on the first day:
    Get-PSDrive C | Select-Object @{N='FreeGB';E={[math]::Round($_.Free/1GB,1)}}
    (Get-ChildItem $env:TEMP -Force | Where-Object Name -like 'sjfac_*').Count

## One-time setup (PowerShell, no elevation)
    py -3.12 -m venv %USERPROFILE%\rope-venv
    %USERPROFILE%\rope-venv\Scripts\pip install numpy==2.4.4 scipy==1.17.1 sympy pyyaml
Download the repository as a zip from GitHub (Code -> Download ZIP), unzip
to %USERPROFILE%\rope. Git is not required.

## Running a job
Copy the job's checkpoint(s) into %USERPROFILE%\rope\analysis\ (the job's
inputs are named in its driver docstring), then in PowerShell:
    cd %USERPROFILE%\rope
    %USERPROFILE%\rope-venv\Scripts\python go.py benchmarks/foundations/<driver>.py
Leave the window open; the log is logs\<driver>.log. Ctrl-C stops the
job; relaunching the same line resumes from the checkpoint. The pattern
cache (analysis/sparsej_pattern_144x36.pkl) is gitignored and large: do
not copy it; the driver measures the patterns it needs on first run.

## Rules
- ONE machine per job. Two machines writing the same checkpoint corrupt it.
- Keep the box awake (Settings -> Power: never sleep on AC) and out of
  scheduled reboots for the duration.
- Bring analysis\<job>_ckpt.pkl back for the verdict.

## Memory
16 GB is enough for 144x36 through 288x36 jobs (3-7 GB). The 240x54 and
336x54 Leg B cells (7-11 GB) are better on a machine doing nothing else.
