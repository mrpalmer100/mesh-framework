"""SPARSE-J C3 -- RATE CREDENTIAL (charter: analysis/SPARSEJ_charter_LOCKED.md).

Re-march TWO consecutive arc-rate points of the q = 4/3 profile from
the retained stage-2c states with the SPARSE instrument (SparseJac +
BandedTorusSolver via gn_sparse), the arc-step machinery replicated
VERBATIM from qsweep_profile.run (tangent predictor, ds = 0.08, full
gates, identical rate/V_pt/f_dir formulas). Bar: both re-marched
rates within 1 percent of the registered (FND-147-profile) rates,
point-by-point. Checkpoint: /tmp/sjc3_ckpt.pkl (fresh store; the
stage-2c record is read-only input from analysis/ -- the 2026-08-27
clobber lesson).
"""
import numpy as np, pickle, pathlib, sys, time, resource

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from benchmarks.foundations import qsweep_stage1 as q1           # noqa
from benchmarks.foundations import sparsej_instrument as SJ      # noqa


def _atomic_write(path, data):
    """write to a temp file then rename: a full disk can truncate the temp file, never the checkpoint (2026-09-13)."""
    import os
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_bytes(data)
    os.replace(tmp, path)

ROOT = pathlib.Path(__file__).resolve().parents[2]
CKPT = pathlib.Path('/tmp/sjc3_ckpt.pkl')
PAT = ROOT / 'analysis' / 'sparsej_pattern_144x36.pkl'
S2C = ROOT / 'analysis' / 'qsweep_stage2c_ckpt.pkl'
N = 144 * 36
DS = 0.08
POINTS = 2          # two consecutive arc-rate points, per the charter


def main():
    T = q1.QTGrid(144, 36, 3, 4)                    # q = 4/3
    rec = pickle.loads(S2C.read_bytes())['prof-4/3']
    reg = rec['meas']                               # registered profile
    x0 = np.asarray(rec['states'][0], float)
    x1 = np.asarray(rec['states'][1], float)

    sj, _ = SJ.make_instrument(T, x1, 'arc', (x0, (x1 - x0) /
                               np.linalg.norm(x1 - x0), DS), 50.0,
                               cache=str(PAT))
    bs = SJ.BandedTorusSolver(144, 36, nglob=2)

    class PersistDict(dict):
        # gn_sparse writes st[key] once per accepted round; persisting
        # on every write makes any timed-out chunk resumable mid-point.
        def __setitem__(self, k, v):
            super().__setitem__(k, v)
            _atomic_write(CKPT, pickle.dumps(dict(self)))

    st = PersistDict(pickle.loads(CKPT.read_bytes())
                     if CKPT.exists() else {})
    res = st.setdefault('c3', dict(states=[x0, x1], meas=[]))

    while len(res['meas']) < POINTS:
        i = len(res['meas'])
        xa, xb = res['states'][-2], res['states'][-1]
        t = xb - xa
        t /= np.linalg.norm(t)
        t0 = time.time()
        xn = SJ.gn_sparse(T, xb + DS * t, 'arc', (xb, t, DS), sj, bs,
                          rounds=60, st=st, key=f'c3-s{i}')
        r = T.field_rms(xn)
        clos = T.closure_max(xn)
        if not (r < q1.RMS_BAR and clos < q1.CLOSURE_BAR):
            print(f"[c3 s{i}] NOT GATED (RMS {r:.1e} clos {clos:.1e}) "
                  f"-- resume this driver", flush=True)
            CKPT.write_bytes(pickle.dumps(dict(st)))
            return
        _, c2p = T.modes(T.geom(xb)[2])
        _, c2n = T.modes(T.geom(xn)[2])
        rate = (abs(c2n) - abs(c2p)) / DS
        dpt = (xn[N:2 * N] - xb[N:2 * N] + np.pi) % (2 * np.pi) - np.pi
        dx = xn - xb
        m = dict(A2=float((abs(c2n) + abs(c2p)) / 2), rate=float(rate),
                 vpt=float(np.sqrt(np.mean(dpt ** 2)) / DS),
                 fdir=float(np.dot(dpt, dpt) / np.dot(dx, dx)),
                 rms=float(r), clos=float(clos),
                 mins=float(time.time() - t0) / 60)
        res['meas'].append(m)
        res['states'].append(xn)
        CKPT.write_bytes(pickle.dumps(dict(st)))
        dev = abs(m['rate'] - reg[i]['rate']) / reg[i]['rate']
        print(f"[c3 s{i}] A2 {m['A2']:.7f}  rate {m['rate']:.4e}  "
              f"reg {reg[i]['rate']:.4e}  dev {dev * 100:.3f}%  "
              f"({m['mins']:.1f} min)", flush=True)

    print("\n== C3 VERDICT ==")
    allpass = True
    for i, m in enumerate(res['meas']):
        dev = abs(m['rate'] - reg[i]['rate']) / reg[i]['rate']
        ok = dev <= 0.01
        allpass &= ok
        print(f"  point {i}: rate {m['rate']:.6e} vs registered "
              f"{reg[i]['rate']:.6e}  dev {dev * 100:.4f}%  "
              f"[{'PASS' if ok else 'FAIL'}]")
    print(f"  C3: {'PASS' if allpass else 'FAIL'}")
    print(f"  peak RSS {resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1e6:.2f} GB")


if __name__ == '__main__':
    main()
