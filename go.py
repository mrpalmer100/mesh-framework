"""go.py -- the launcher for Windows (no bash, no admin): loops a checkpointing driver with this
Python until the LAST log line is a terminal line. Same semantics as go.sh.
    py -3.12 go.py benchmarks/foundations/kernel_cont.py
Run it in a PowerShell window you leave open (or: start /min py -3.12 go.py ...). Ctrl-C stops it;
relaunching resumes from the checkpoint. Memo pruning keeps the two newest sjjac_/sjfac_ memos in
the temp directory, as go.sh does. SJ_MEMO defaults to jac."""
import os, sys, subprocess, pathlib, re, shutil, tempfile, time

drv = sys.argv[1]; name = pathlib.Path(drv).stem
root = pathlib.Path(__file__).resolve().parent; os.chdir(root)
pathlib.Path('logs').mkdir(exist_ok=True); log = pathlib.Path('logs') / f'{name}.log'
# a previous run's terminal line must not stop this one: rotate the old log if its last line is terminal
if log.exists():
    _last = log.read_text(errors='replace').rstrip('\n').split('\n')[-1]
    if re.search(r'COMPLETE|REFUSED|RESOLVED|run the verdict', _last):
        n = 1
        while (pathlib.Path('logs') / f'{name}_run{n}.log').exists(): n += 1
        log.rename(pathlib.Path('logs') / f'{name}_run{n}.log')
env = dict(os.environ); env.setdefault('SJ_MEMO', 'jac'); env['PYTHONUNBUFFERED'] = '1'
TERMINAL = re.compile(r'COMPLETE|REFUSED|RESOLVED|run the verdict')
fails = 0
print(f'launched {drv} -> {log}  (Ctrl-C to stop; relaunch to resume)', flush=True)
while True:
    with open(log, 'a') as lf:
        rc = subprocess.call([sys.executable, '-u', drv], stdout=lf, stderr=subprocess.STDOUT, env=env)
    if rc != 0:
        fails += 1
        if fails >= 3:
            print(f'[{name}] failing -- see {log}', flush=True); sys.exit(1)
        time.sleep(2); continue
    fails = 0
    lines = log.read_text(errors='replace').rstrip('\n').split('\n')
    if lines and TERMINAL.search(lines[-1]):
        print(f'[{name}] done: {lines[-1]}', flush=True); sys.exit(0)
    tmp = pathlib.Path(tempfile.gettempdir())
    for pat in ('sjjac_*', 'sjfac_*'):
        memos = sorted(tmp.glob(pat), key=lambda p: p.stat().st_mtime, reverse=True)
        for m in memos[2:]:
            shutil.rmtree(m, ignore_errors=True) if m.is_dir() else m.unlink(missing_ok=True)
