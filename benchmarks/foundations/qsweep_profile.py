"""Q-SWEEP STAGE 2c -- the profile experiment (retention re-march).

CHARTER (LOCKED HERE, 2026-08-26, before this driver first runs;
this docstring IS the charter, granted its slot by the author with
FND-151):

QUESTION: does the winding velocity's rise quantitatively account
for the amplitude rate's fall along the collapsing branch?

DESIGN: re-march the q = 4/3 branch from its gated member pair
with the stage-1 arc instrument UNCHANGED (ds = 0.08, all gates,
all solver lessons) but with PER-STEP FULL-STATE RETENTION, from
A2 ~ 0.0047 into the collapse (budget 12 steps). The q = 5/3
profile is the optional control, chartered but second.

PER-STEP MEASUREMENTS (from retained gated states only):
  dA2/ds  (the stage-1 rate, recomputed identically)
  V_pt    = RMS_nodes(delta pt mod 2pi) / ds
  f_dir   = |delta pt|^2 / |delta x|^2   (direction share of the
            step's full-state arclength)

PRE-REGISTERED STATISTIC AND LINES (fixed before any number):
  Over the profile, r = Pearson corr( log V_pt, -log dA2/ds ).
  E-LEDGER   : r >= 0.8 AND V_pt monotone nondecreasing through
               the collapse (ties within 2 percent allowed) AND
               f_dir rises by >= 0.15 absolute start-to-end.
  E-PARTIAL  : 0.5 <= r < 0.8, or the f_dir rise in [0.05, 0.15).
  E-NULL     : otherwise.
  E-DATA     : fewer than 6 gated steps achieved.
E-LEDGER lifts nothing by itself but completes, with FND-150/151,
the evidence set the author may weigh against the FND-147 freeze.

NO-RESCUE: statistic, lines, ds, and node treatment fixed above;
retained states are the sole inputs; any exploratory analysis of
the retained states is labeled exploratory and cannot fire forms.

Checkpoint: /tmp/s2c_ckpt.pkl (fresh key space; the stage-1
record is NOT touched). Log: /tmp/s2c.log.
"""
import numpy as np
import pickle
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import qsweep_stage1 as q1  # noqa: E402

# CHECKPOINT UNIFICATION (2026-08-27, measured): gn_lean persists
# rounds through q1.CKPT, so a separate driver store split the
# state across two files and the first launch clobbered the
# stage-1 /tmp record (durable analysis/ export intact, by
# design). One store: q1's. Members come from the durable export.
CKPT = q1.CKPT
S1_EXPORT = pathlib.Path(__file__).resolve().parents[2] / \
    'analysis' / 'qsweep_stage1_ckpt.pkl'
N = 144 * 36
DS = 0.08
BUDGET = 12


def _atomic_write(path, data):
    """write to a temp file then rename: a full disk can truncate the temp file, never the checkpoint (2026-09-13)."""
    import os
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_bytes(data)
    os.replace(tmp, path)

def load():
    if CKPT.exists():
        return pickle.loads(CKPT.read_bytes())
    return {}


def save(st):
    _atomic_write(CKPT, pickle.dumps(st))


def run(tag='4/3'):
    n2 = {'4/3': 4, '5/3': 5}[tag]
    T = q1.QTGrid(144, 36, 3, n2)
    s1 = pickle.loads(S1_EXPORT.read_bytes())
    ms = s1[f'q{tag}']['members']
    st = load()
    rec = st.setdefault(f'prof-{tag}', dict(states=[], meas=[]))
    if not rec['states']:
        rec['states'] = [np.asarray(ms[0]['x'], float),
                         np.asarray(ms[1]['x'], float)]
        save(st)
    while len(rec['meas']) < BUDGET:
        x0, x1 = rec['states'][-2], rec['states'][-1]
        t = x1 - x0
        t /= np.linalg.norm(t)
        kk = f'prof-{tag}-s{len(rec["meas"])}'
        xn, r = q1.gn_lean(T, x1 + DS * t, 'arc', (x1, t, DS),
                           rounds=60, st=st, key=kk)
        clos = T.closure_max(xn)
        if not (r < q1.RMS_BAR and clos < q1.CLOSURE_BAR):
            print(f"    [prof-{tag} s{len(rec['meas'])}] not gated "
                  f"yet (RMS {r:.1e} clos {clos:.1e})")
            return
        _, c2p = T.modes(T.geom(x1)[2])
        _, c2n = T.modes(T.geom(xn)[2])
        rate = (abs(c2n) - abs(c2p)) / DS
        dpt = (xn[N:2 * N] - x1[N:2 * N] + np.pi) % (2 * np.pi) \
            - np.pi
        dx = xn - x1
        vpt = float(np.sqrt(np.mean(dpt ** 2)) / DS)
        fdir = float(np.dot(dpt, dpt) / np.dot(dx, dx))
        rec['meas'].append(dict(A2=float((abs(c2n) + abs(c2p)) / 2),
                                rate=float(rate), vpt=vpt,
                                fdir=fdir))
        rec['states'].append(xn)
        save(st)
        m = rec['meas'][-1]
        print(f"    [prof-{tag}] A2 {m['A2']:.6f}  dA2/ds "
              f"{m['rate']:.3e}  V_pt {m['vpt']:.5f}  f_dir "
              f"{m['fdir']:.4f}  [{len(rec['meas'])}/{BUDGET}]")
    ms_ = rec['meas']
    lv = np.log([m['vpt'] for m in ms_])
    lr = -np.log([max(m['rate'], 1e-9) for m in ms_])
    r_p = float(np.corrcoef(lv, lr)[0, 1])
    print(f"  [prof-{tag}] COMPLETE. r = {r_p:.3f}  f_dir "
          f"{ms_[0]['fdir']:.3f} -> {ms_[-1]['fdir']:.3f}")


if __name__ == '__main__':
    run(sys.argv[1] if len(sys.argv) > 1 else '4/3')
