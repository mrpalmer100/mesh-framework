"""COMMISSION KNOT-REACH-2 -- the one repair NORTH_STAR section 5 permits after KNOT-REACH's REACH-SHORT: the same
torus ladder T(2,n), the same certificates, the same ledger, the same fit window and forms, with ONE change: the
linear iteration rule (25000 n/3) is replaced by a CONVERGENCE RULE fixed here before any rung. Charter
analysis/KNOT_REACH2_charter_LOCKED.md. Checkpoint analysis/knot_reach2_ckpt.pkl (KNOT-REACH's sealed checkpoint is
never read or written). One doubling per invocation (resumable, atomic); the PC runs it through go.py:
    python go.py benchmarks\\foundations\\knot_reach2.py COMPLETE
The convergence rule (C-1): each rung is tightened to cumulative budgets 25000 x 2^k (k = 0, 1, 2, ...; the trefoil's
registered budget doubled), the tightener resumed from the previous doubling's coordinates (its state is the curve
alone). The rung is CONVERGED at the first k >= 1 whose length differs from the previous doubling's by under 1 percent
(stricter than the registered 3-percent grade, which is then passed with margin); its recorded L is that doubling's.
The cap is 1,600,000 iterations (k = 6); a rung still moving by 1 percent or more at the cap is the reach-failure and
the ladder stops: the reach is the rung below (B-5 unchanged: no budget is raised beyond the rule). Certificates
(knot_det == n at tilts 0.013 and 0.11) are checked at construction and after EVERY doubling; a loss is REFUSED by name.
The verdict is knot_reach_verdict.py on this checkpoint (the SAME locked forms, NMIN 7, band [0.9, 1.1]):
    python benchmarks\\foundations\\knot_reach_verdict.py analysis\\knot_reach2_ckpt.pkl
"""
import os, pathlib, pickle, shutil, sys, time
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'benchmarks' / 'foundations')); sys.path.insert(0, str(ROOT))
from two_term_mass_model import tighten_coords                      # noqa: E402
from topology_certifier import knot_det                             # noqa: E402
from mapping_calibrated import build_table                          # noqa: E402
from knot_reach import torus, certified, ledger, RUNGS, _atomic     # noqa: E402  (the locked ladder, unchanged)

CKPT = ROOT / 'analysis' / 'knot_reach2_ckpt.pkl'
BASE, CAP, CONV = 25000, 1_600_000, 0.01            # C-1: doublings of the trefoil's budget; cap; the 1-percent bar
SMOKE = '--smoke' in sys.argv                        # sandbox only: rungs 3 and 5 on a separate checkpoint, BASE / KR_SMOKE_DIV
SMOKE_DIV = float(os.environ.get('KR_SMOKE_DIV', '20'))


def main():
    global CKPT, BASE, CAP
    rungs = RUNGS
    if SMOKE:
        rungs = (3, 5); CKPT = ROOT / 'analysis' / 'knot_reach2_SMOKE_ckpt.pkl'; BASE = int(BASE / SMOKE_DIV); CAP = int(CAP / SMOKE_DIV)
    free_gb = shutil.disk_usage(ROOT).free / 1e9
    if free_gb < 20.0 and not SMOKE:
        print(f"[kr2] REFUSING TO START: {free_gb:.2f} GB free; free at least 20 GB", flush=True); raise SystemExit(2)
    st = pickle.loads(CKPT.read_bytes()) if CKPT.exists() else dict(rungs={}, reach=None, halt=None, rule=dict(base=BASE, cap=CAP, conv=CONV), live=None)
    if st['halt']:
        print(f"[kr2] KNOT-REACH-2 COMPLETE -- run the verdict ({st['halt']})", flush=True); return
    Ns, dEs = build_table()
    for n in rungs:
        if n in st['rungs']:
            continue
        live = st.get('live')
        if live is None or live['n'] != n:
            P0 = torus(n)
            if not certified(P0, n):
                st['rungs'][n] = dict(refused='construction certificate', det=(knot_det(P0), knot_det(P0, 0.11)))
                st['halt'] = f'rung {n} refused at construction'; st['live'] = None; _atomic(CKPT, pickle.dumps(st))
                print(f"[kr2 n={n}] REFUSED: construction certificate det {st['rungs'][n]['det']} != {n}", flush=True); return
            live = dict(n=n, N=len(P0), P=P0, cum=0, k=-1, Ls=[], seconds=0.0); st['live'] = live
        # one doubling: tighten from the live coordinates to the next cumulative budget
        k = live['k'] + 1; target = BASE * 2 ** k; step = target - live['cum']
        t0 = time.time()
        P = tighten_coords(np.array(live['P'], float), iters=step)
        ok = certified(P, n)
        led = ledger(P, Ns, dEs)
        live.update(P=P, cum=target, k=k, seconds=live['seconds'] + time.time() - t0); live['Ls'].append(led['L'])
        change = abs(live['Ls'][-1] - live['Ls'][-2]) / live['Ls'][-1] if k >= 1 else float('nan')
        print(f"[kr2 n={n} k={k}] cum {target}; L/D {led['L']:.3f}; change {change:.4f}; det {'ok' if ok else 'LOST'}; contacts {led['nc']}; {(time.time()-t0)/60:.1f} min", flush=True)
        done = None
        if not ok:
            done = 'certificate lost'
        elif k >= 1 and change < CONV:
            done = 'converged'
        elif target >= CAP:
            done = 'cap'
        if done:
            rec = dict(n=n, N=live['N'], iters=target, L_half=live['Ls'][-2] if k >= 1 else float('nan'), grade=change, det_ok=ok,
                       seconds=live['seconds'], doublings=list(live['Ls']), rule=done, **led)
            st['rungs'][n] = rec; st['live'] = None
            if done == 'certificate lost':
                st['halt'] = f'rung {n} refused: certificate lost after tightening (k={k})'
            elif done == 'cap':
                st['reach'] = max([m for m in st['rungs'] if m < n], default=None)
                st['halt'] = f'rung {n} unconverged at the cap ({change:.3f} at {target}); reach {st["reach"]}'
            print(f"[kr2 n={n}] {done}: iters {target}; L/D {led['L']:.3f} (previous doubling {rec['L_half']:.3f}, grade {change:.4f}); S {led['S']:.3f}; contacts {led['nc']} len {led['lc']:.2f}; {live['seconds']/60:.1f} min", flush=True)
        _atomic(CKPT, pickle.dumps(st))
        if st['halt']:
            print(f"[kr2] KNOT-REACH-2 COMPLETE -- run the verdict ({st['halt']})", flush=True)
        return
    st['reach'] = max(st['rungs']); st['halt'] = f'ladder complete; reach {st["reach"]}'; _atomic(CKPT, pickle.dumps(st))
    print(f"[kr2] KNOT-REACH-2 COMPLETE -- run the verdict (ladder complete; reach {st['reach']})", flush=True)


if __name__ == '__main__':
    main()
