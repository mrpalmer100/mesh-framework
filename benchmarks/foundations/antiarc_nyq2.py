"""COMMISSION ANTI-ARC-NYQ-2 -- the one repair NORTH_STAR section 5 permits: ANTI-ARC-NYQ's aligned control c2
re-run with its per-point round budget raised from 60 to CTRL_BUDGET, NOTHING ELSE CHANGED, so that the pending
verdict can be read from the sealed arms. Charter analysis/ANTIARC_NYQ2_charter_LOCKED.md.

Starts from a COPY of the sealed ANTI-ARC-NYQ checkpoint (analysis/antiarc_nyq_ckpt.pkl is never written):
analysis/antiarc_nyq2_ckpt.pkl. In the copy, c2A1 and c2A2 are reopened (done=False) with their gated s1 seeds and
the sparse instrument's persisted per-key state, so the corrector RESUMES from round 60, it does not restart. The
arms (A1: 20 sealed points; A2: halted at p0) and c1 and the seeds are carried over untouched. One unit per
invocation; the same loop as ANTI-ARC-NYQ. Terminal line: 'ANTI-ARC-NYQ-2 COMPLETE -- run the verdict'. Verdict:
    python benchmarks\\foundations\\antiarc_nyq_verdict.py analysis\\antiarc_nyq2_ckpt.pkl
(the SAME locked forms; the verdict script takes the checkpoint path).
"""
import pathlib, pickle, shutil, sys
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from benchmarks.foundations import antiarc_nyq as AN                   # noqa: E402
from benchmarks.foundations import qsweep_stage1 as q1                 # noqa: E402

SRC = ROOT / 'analysis' / 'antiarc_nyq_ckpt.pkl'
CKPT = ROOT / 'analysis' / 'antiarc_nyq2_ckpt.pkl'
CTRL_BUDGET = 200
AN.CKPT = CKPT          # PersistDict and _atomic_write write through the module global: redirect to the copy


def main():
    free_gb = shutil.disk_usage(ROOT).free / 1e9
    if free_gb < 20.0:
        print(f"[aan2] REFUSING TO START: {free_gb:.2f} GB free; free at least 20 GB and rerun", flush=True); raise SystemExit(2)
    if not CKPT.exists():
        st0 = pickle.loads(SRC.read_bytes())
        for key in ('c2A1', 'c2A2'):
            R = st0[key]
            if R.get('done') and not R['m']['gated_clean']:
                R['done'] = False; R['nyq1_m'] = R['m']; R['halt'] = None     # reopen; keep the 60-round reading on record
        st0['nyq2'] = dict(budget=CTRL_BUDGET, reopened=['c2A1', 'c2A2'], source=str(SRC.name))
        AN._atomic_write(CKPT, pickle.dumps(st0))
        print(f"[aan2] copied the sealed checkpoint; reopened c2A1, c2A2 with budget {CTRL_BUDGET} (resume from their saved rounds); arms untouched", flush=True)
    st = AN.PersistDict(pickle.loads(CKPT.read_bytes()))
    Tl = q1.QTGrid(144, 36, *AN.CELLS['aligned'])
    for arm in ('A1', 'A2'):
        key = f'c2{arm}'; R = st[key]
        if R.get('done'): continue
        a0 = np.asarray(pickle.loads(AN.SRC_ALIGNED.read_bytes())['q4/3']['members'][0]['x'], float)
        xn, m, cum = AN.arc_point(Tl, st, f'sj|{key}|p0', a0, np.asarray(R['s1'], float), arm, budget=CTRL_BUDGET)
        if xn is not None or cum >= CTRL_BUDGET:
            R.update(done=True, m=m, x=xn, halt=None if xn is not None else 'p0 refused', rounds=cum); st[key] = R
            print(f"[aan2 {key}] aligned arc point: RMS {m['rms']:.1e} clos {m['clos']:.1e} wsNyq {m['nyq']:.1e} gated_clean {m['gated_clean']} rounds {cum}", flush=True)
        else:
            print(f"[aan2 {key}] in progress: RMS {m['rms']:.1e} clos {m['clos']:.1e} rounds {cum}", flush=True)
        return
    print("[aan2] ANTI-ARC-NYQ-2 COMPLETE -- run the verdict", flush=True)


if __name__ == '__main__':
    main()
