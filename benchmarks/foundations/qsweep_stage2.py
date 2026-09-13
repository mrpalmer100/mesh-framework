"""Q-SWEEP STAGE 2 -- the frozen-direction transplant instrument.

Charter: analysis/QSWEEP_stage2_charter_LOCKED.md (+amendments 1-2,
both pre-execution). The direction field is the phase/winding field
pt (amendment 2); the free sector is (th, T, om1, om2), 2N+2 =
10370 dof on the 144x36 chart. Gates are stage-1 gates on the
composed full state. Transplant map: identity on node coordinates
(shared chart; amendment 1's strongest-form no-rescue map).

Reduced solver: finite-difference Jacobian over the FREE columns
only (the stage-1 chunked FD jac restricted to free indices),
f64 normal matrix via dsyrk from the f32 reduced J, lm damping,
monotone acceptance, closure-aware stop, per-round checkpoint --
the stage-1 lessons carried over. Checkpoint: /tmp/s2_ckpt.pkl.

RUN ORDER (charter): X3a (4/3 self), X3b (5/3 self) -- both must
reproduce native anchor rates within 20 percent -- then X1 (5/3 pt
on 4/3 cell), X2 (4/3 pt on 5/3 cell).
"""
import numpy as np
import pickle
import pathlib
import sys
import scipy.linalg as sla

sys.path.insert(0, str(pathlib.Path(__file__).parent))
import qsweep_stage1 as q1  # noqa: E402

CKPT = pathlib.Path('/tmp/s2_ckpt.pkl')
S1CKPT = pathlib.Path('/tmp/qsweep_ckpt.pkl')
N = 144 * 36
RMS_BAR, CLOSURE_BAR = q1.RMS_BAR, q1.CLOSURE_BAR
NATIVE_RATE = {'4/3': 5.5e-4, '5/3': 5.6e-4}   # anchor-region native
FREE = np.concatenate([np.arange(N),                 # th
                       np.arange(2 * N, 3 * N),      # T
                       [3 * N, 3 * N + 1]])          # om1, om2


def save(st):
    _atomic_write(CKPT, pickle.dumps(st))


def load():
    if CKPT.exists():
        return pickle.loads(CKPT.read_bytes())
    return {}


def grids():
    return {'4/3': q1.QTGrid(144, 36, 3, 4),
            '5/3': q1.QTGrid(144, 36, 3, 5)}


def members():
    s1 = pickle.loads(S1CKPT.read_bytes())
    out = {}
    for tag, key in (('4/3', 'q4/3'), ('5/3', 'q5/3')):
        ms = s1[key]['members']
        out[tag] = (np.asarray(ms[0]['x'], float),
                    np.asarray(ms[1]['x'], float))
    return out


def compose(x_template, pt_frozen, free_vals):
    x = x_template.copy()
    x[N:2 * N] = pt_frozen
    x[:N] = free_vals[:N]
    x[2 * N:3 * N] = free_vals[N:2 * N]
    x[3 * N] = free_vals[2 * N]
    x[3 * N + 1] = free_vals[2 * N + 1]
    return x


def free_of(x):
    return np.concatenate([x[:N], x[2 * N:3 * N],
                           [x[3 * N], x[3 * N + 1]]])


def gn_frozen(T, st, key, x0, pt_frozen, pin_mode, aux, PW,
              max_rounds=1):
    """One (or few) reduced GN rounds per call, checkpointed.
    Stage-1 discipline: lm damping on diag, f64 monotone accept,
    closure-aware stop, lam persisted."""
    rec = st.get(key, {})
    free = rec.get('free')
    lam = rec.get('lam', 3e-5)
    if free is None:
        free = free_of(x0)
    x = compose(x0, pt_frozen, free)
    fx = float(np.linalg.norm(T.wres(x, pin_mode, aux, PW)))
    for _ in range(max_rounds):
        J = T.jac(x, pin_mode, aux, PW)          # f32, full cols
        Jr = np.ascontiguousarray(J[:, FREE])
        del J
        r0 = T.wres(x, pin_mode, aux, PW)
        # MEMORY (2026-08-26, measured OOM): no f64 copy of Jr
        # (1.3 GB), no A.T symmetrization transient; cho_factor
        # reads the lower triangle only.
        A = sla.blas.ssyrk(1.0, Jr, trans=1, lower=1).astype(
            np.float64)
        g = (Jr.T @ r0.astype(np.float32)).astype(np.float64)
        d = np.diag(A).copy()
        acc = False
        for _t in range(8):
            M = A + lam * np.diag(d)
            try:
                c = sla.cho_factor(M, lower=True, check_finite=False)
            except np.linalg.LinAlgError:
                lam *= 10
                continue
            dx = sla.cho_solve(c, -g, check_finite=False)
            nd = float(np.linalg.norm(dx))
            if nd > 0.05:                        # stage-1 trust cap
                dx *= 0.05 / nd
            for frac in (1.0, 0.5, 0.25, 0.1):
                ft = free + frac * dx
                xt = compose(x0, pt_frozen, ft)
                f2 = float(np.linalg.norm(
                    T.wres(xt, pin_mode, aux, PW)))
                if f2 < fx:
                    free, x, fx, acc = ft, xt, f2, True
                    lam = max(lam / 3.0, 1e-9)
                    break
            if acc:
                # CHORD STEPS (2026-08-26, annotated): the FD
                # Jacobian dominates the round cost; under the 0.05
                # trust cap the reduced J stays valid over several
                # short steps, so take up to 6 more damped steps
                # reusing A (refreshing only the gradient) before
                # the next full jac. Monotone acceptance unchanged.
                # chord steps REUSE the accepted factor c (a
                # triangular solve per step, not a fresh 10370^3/3
                # Cholesky -- measured to blow the reap window)
                for _c in range(6):
                    r0 = T.wres(x, pin_mode, aux, PW)
                    g = (Jr.T @ r0.astype(np.float32)).astype(
                        np.float64)
                    dx = sla.cho_solve(c, -g, check_finite=False)
                    nd = float(np.linalg.norm(dx))
                    if nd > 0.05:
                        dx *= 0.05 / nd
                    ft = free + dx
                    xt = compose(x0, pt_frozen, ft)
                    f2 = float(np.linalg.norm(
                        T.wres(xt, pin_mode, aux, PW)))
                    if f2 < fx:
                        free, x, fx = ft, xt, f2
                    else:
                        break
                break
            lam *= 10
        r = T.field_rms(x)
        print(f"      [s2 gn: RMS {r:.1e}  wres {fx:.3e}  "
              f"lam {lam:.0e}  acc {acc}]")
        st[key] = dict(free=free, lam=lam)
        save(st)
        if r < RMS_BAR and T.closure_max(x) < CLOSURE_BAR:
            st[key]['done'] = True
            save(st)
            break
        if not acc and lam > 1e6:
            break
    return x


def arc_rate_frozen(tag_cell, tag_field, nsteps=4, ds=0.02):
    """The X-run: on cell tag_cell with pt frozen from tag_field's
    member-2, march the arc from the (m1, m2) free-sector pair and
    measure dA2/ds per gated step. Returns list of (A2, rate)."""
    st = load()
    G = grids()[tag_cell]
    mem = members()
    x_m1_cell, x_m2_cell = mem[tag_cell]
    pt_frozen = mem[tag_field][1][N:2 * N].copy()
    key0 = f'X-{tag_cell}-pt{tag_field}'
    # anchor solve: member-2 free sector under the frozen pt
    A2_anchor = 0.0046979
    if not st.get(key0 + '-anchor', {}).get('done'):
        gn_frozen(G, st, key0 + '-anchor', x_m2_cell, pt_frozen,
                  'a2', A2_anchor, 50.0)
    if not st.get(key0 + '-anchor', {}).get('done'):
        return st.get(key0, {}).get('rates', [])
    # arc march in the free sector
    rec = st.setdefault(key0, {'rates': [], 'pair': None})
    if rec['pair'] is None:
        f1 = free_of(x_m1_cell)
        f2 = st[key0 + '-anchor']['free']
        rec['pair'] = [f1, f2]
        save(st)
    while len(rec['rates']) < nsteps:
        f1, f2 = rec['pair']
        t = f2 - f1
        t /= np.linalg.norm(t)
        fs = f2 + ds * t
        kk = key0 + f'-step{len(rec["rates"])}'
        st[kk] = st.get(kk, {'free': fs, 'lam': 3e-5})
        save(st)
        x_prev = compose(x_m2_cell, pt_frozen, f2)
        t_full = compose(np.zeros_like(x_m2_cell), np.zeros(N),
                         t) - compose(np.zeros_like(x_m2_cell),
                                      np.zeros(N),
                                      np.zeros_like(t))
        t_full /= np.linalg.norm(t_full)
        xs = gn_frozen(G, st, kk, compose(x_m2_cell, pt_frozen, fs),
                       pt_frozen, 'arc', (x_prev, t_full, ds), 1.0)
        if not st.get(kk, {}).get('done'):
            return rec['rates']
        fN = st[kk]['free']
        xN = compose(x_m2_cell, pt_frozen, fN)
        _, c2n = G.modes(G.geom(xN)[2])
        _, c2p = G.modes(G.geom(compose(x_m2_cell, pt_frozen,
                                        f2))[2])
        A2n, A2p = abs(c2n), abs(c2p)
        rate = (A2n - A2p) / ds
        rec['rates'].append([float((A2n + A2p) / 2), float(rate)])
        rec['pair'] = [f2, fN]
        save(st)
        print(f"    [{key0}] dA2/ds = {rate:.3e} at A2 ~ "
              f"{(A2n + A2p) / 2:.6f}")
    return rec['rates']


if __name__ == '__main__':
    tag_cell, tag_field = sys.argv[1], sys.argv[2]
    rates = arc_rate_frozen(tag_cell, tag_field)
    if rates:
        nat = NATIVE_RATE[tag_cell]
        for A2, rr in rates:
            print(f"  R = {rr / nat:.3f} at A2 {A2:.5f} "
                  f"(rate {rr:.3e} vs native {nat:.1e})")

def _atomic_write(path, data):
    """write to a temp file then rename: a full disk can truncate the temp file, never the checkpoint (2026-09-13)."""
    import os
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_bytes(data)
    os.replace(tmp, path)

