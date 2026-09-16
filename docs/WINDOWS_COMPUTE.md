# Running drivers on a Windows compute box (no admin required)

The drivers are pure Python; only the launcher was bash. Since 2026-09-13
the solver's memo files go to the platform temp directory (tempfile.
gettempdir(): /tmp on Unix, %TEMP% on Windows) and go.py replaces go.sh.

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
