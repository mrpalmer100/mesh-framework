"""benchmarks/foundations/qsweep_stage1.py

Q-SWEEP STAGE 1 -- the q-sensitivity probe. Charter and bars locked
BEFORE computing: analysis/QSWEEP_stage1_bars_LOCKED.md. Authorized
by the author 2026-08-22 on FND-146's Rule C promotion.

The instrument: QGrid / QTGrid parameterize the registered stage-2
grid and tangent-sphere chart by the rationalization (N1, N2) --
identical operators, stencils, pins, and weights; only LCELL, K2,
and the grid size change, exactly as the registered constants
prescribe (LCELL = N1 sqrt(3), K2 = N2 2pi / LCELL). K1, R1, R2,
TBAR, and the level-1 sector are q-independent and shared.

SCHEDULING ANNOTATIONS (locked-charter conformance):
- Cross-resolution confirmations are OWED TO STAGE 3 (the author's
  resolution-replication stage), not discharged here; wsNyq is
  recorded at every member and the debt is registered in the state.
- The 0.0063 rate point is reached by an ADDED a2 pin between the
  registered waypoints; rates are always measured from arc pairs at
  full-bar members (the standing rule), so the added pin is
  measurement scheduling, not an instrument change. If the a2 pin
  stalls (the registered near-singularity class), the arc march is
  the fallback, per the FND-143 registered-deviation precedent.

Run detached, MEMORY-EXCLUSIVE:
    setsid nohup python3 benchmarks/foundations/qsweep_stage1.py \
        > /tmp/qsweep.log 2>&1 < /dev/null &
Per-milestone checkpoint /tmp/qsweep_ckpt.pkl; rerun to resume.
"""
import pathlib
import pickle
import sys
import time

import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from benchmarks.foundations import truestate_stage2 as S2      # noqa: E402
from benchmarks.foundations.traverse_steepened import (        # noqa: E402
    TGrid, RMS_BAR, SINTH_FLOOR, DS_FLOOR)
from benchmarks.foundations.traverse96_scout import TGrid96    # noqa: E402

CKPT = pathlib.Path('/tmp/qsweep_ckpt.pkl')
CLOSURE_BAR = 1e-6          # halt-grade, FND-143 promotion (bar v3)
PIN_TOL = 1e-8
WAYPOINTS = [0.02 * S2.R2, 0.05 * S2.R2]        # 0.0018792, 0.0046979
FINE_PIN = 0.0063277                            # matched to the march head
DS = 0.08                                        # the registered arc step


class QGrid(S2.Grid):
    """The stage-2 grid on the (N1, N2) rationalized cell."""

    def __init__(self, ns, npn, n1, n2):
        self.N1, self.N2 = n1, n2
        self.LCELL = n1 * np.sqrt(3.0)
        self.K2 = n2 * 2 * np.pi / self.LCELL
        self.NS, self.NP, self.N = ns, npn, ns * npn
        hs, hp = self.LCELL / ns, 2 * np.pi / npn
        self.DS1 = self._dmat(ns, hs, S2.D1O, S2.D1W)
        self.DP1 = self._dmat(npn, hp, S2.D1O, S2.D1W)
        self.DP2 = self._dmat(npn, hp, S2.D2O, S2.D2W)
        self.sgrid = np.arange(ns) * hs
        self.pgrid = np.arange(npn) * hp
        self.E1 = np.exp(-1j * S2.K1 * self.sgrid)
        self.E2s = np.exp(-1j * self.K2 * self.sgrid)
        self._groups = None


class QTGrid(TGrid96):
    """The tangent-sphere chart with the f32-J solver, on a QGrid.
    Body verbatim from TGrid.__init__ except the grid construction;
    every operator, pin, and weight is inherited unchanged."""

    def __init__(self, ns, npn, n1, n2):
        self.G2 = QGrid(ns, npn, n1, n2)
        self.NS, self.NP, self.N = ns, npn, ns * npn
        self.DS1, self.DP1, self.DP2 = self.G2.DS1, self.G2.DP1, self.G2.DP2
        self.sgrid, self.pgrid = self.G2.sgrid, self.G2.pgrid
        self.E1, self.E2s = self.G2.E1, self.G2.E2s
        lam = np.conj(np.fft.fft(self.DS1[0, :]))
        v = np.random.default_rng(0).standard_normal(ns)
        assert np.allclose(self.DS1 @ v,
                           np.fft.ifft(lam * np.fft.fft(v)).real,
                           atol=1e-10)
        self.null = np.abs(lam) < 1e-9
        self.lam_safe = np.where(self.null, 1.0, lam)
        self.PSI0 = (S2.K1 * self.sgrid)[:, None]
        self.n = 3 * self.N + 2


def load():
    return pickle.loads(CKPT.read_bytes()) if CKPT.exists() else {}


def save(st):
    _atomic_write(CKPT, pickle.dumps(st))


def metrics(T, x):
    ws, zp, w, ze, gphi, gam, th, pt, Tf, om1, om2 = T.geom(x)
    _, c2 = T.modes(w)
    nyq = np.abs(np.fft.fft(ws, axis=0)[T.NS // 2]).max() / T.NS
    return dict(rms=float(T.field_rms(x)), A2=float(np.abs(c2)),
                om1=float(om1), om2=float(om2), gam=float(gam),
                minzp=float(zp.min()), minsin=float(np.sin(th).min()),
                clos=float(T.closure_max(x)), nyq=float(nyq))


def gate(T, x, label, pin=None):
    """The full acceptance gates of the native protocol (RMS, halt-
    grade closure, pin, geometry floors). Confirmation debt recorded,
    owed to stage 3."""
    m = metrics(T, x)
    ok = (m['rms'] < RMS_BAR and m['clos'] < CLOSURE_BAR
          and m['minsin'] > SINTH_FLOOR and m['minzp'] > DS_FLOOR)
    if pin is not None:
        ok = ok and abs(m['A2'] - pin) < PIN_TOL
    m['conf_owed_stage3'] = bool(m['nyq'] > 1e-4)
    print(f"    [{label}] RMS {m['rms']:.2e}  A2 {m['A2']:.7f}  "
          f"Om2 {m['om2']:.5f}  gam {m['gam']:.5f}  clos "
          f"{m['clos']:.1e}  wsNyq {m['nyq']:.1e}  "
          f"[{'MEMBER' if ok else 'FAILS GATES'}]"
          f"{'  (conf owed to stage 3)' if m['conf_owed_stage3'] else ''}",
          flush=True)
    return m, ok


def level1_seed(T):
    th0 = np.arcsin(S2.K1 * S2.R1)
    return T.pack(np.full((T.NS, T.NP), th0),
                  np.full((T.NS, T.NP), np.pi / 2),
                  np.full((T.NS, T.NP), S2.TBAR), S2.OM1_L1, 3.20)


def solve(T, x0, pin_mode, aux, nfev=60, tight=False):
    t0 = time.time()
    res = T.solve(x0, pin_mode, aux, max_nfev=nfev, tight=tight)
    r = T.field_rms(res.x)
    print(f"      [solve {time.time()-t0:.0f}s  nfev {res.nfev}  "
          f"RMS {r:.1e}]", flush=True)
    return res.x, r


def gn_lean(T, x, pin_mode, aux, rounds=60, PW=50.0, st=None, key=None,
            stop_rms=None):
    """THE LADDER, THIRD FORM (charter amendment 1 continued,
    2026-08-22, annotated): bar (v5) FAILED the first two forms and
    the autopsy against the registered lm_round found two structural
    defects, both mine: (1) isotropic lsmr damping crushes
    weak-curvature directions -- exactly the m2 mode -- where the
    registered solver uses MARQUARDT SCALING (lam * diag(JtJ)),
    curvature-proportional per column; (2) truncated lsmr resolves
    only the dominant singular subspace, so loose rounds structurally
    cannot move the weak mode at all. This form is lm_round's math
    verbatim -- Marquardt-scaled damping, exact Cholesky normal
    steps, multi-retry against one Jacobian -- with the S4 memory
    diet for n = 15554: f64 dsyrk accumulation FROM the f32 J, the
    normal matrix held f32 for the retry band (step precision ~1e-3
    rel, ample for damped GN), and an f64 in-place single-attempt
    endgame below 3e-5 (the native diet, substeps disabled).
    Acceptance is the f64 monotone residual plus the basin guard,
    both unchanged."""
    import scipy.linalg as sla
    from scipy.linalg import blas as _blas

    def wn(z):
        return float(np.linalg.norm(T.wres(z, pin_mode, aux, PW)))

    def guard_ok(xt):
        if pin_mode == 'a2' and aux > 1e-5:
            _, c2t = T.modes(T.geom(xt)[2])
            return abs(c2t) >= 0.3 * aux
        return True

    lam = 1e-4
    if st is not None and key is not None and key in st:
        x = st[key]['x']
        # LAM PERSISTENCE (2026-08-22, annotated, measured): the
        # container reaps at every tool boundary and each restart was
        # resetting the damping to 1e-4, so the escalation a stalled
        # transition needs could never accrue -- the rung retried the
        # same failing lam values forever. lam rides in the solve key.
        lam = st[key].get('lam', 1e-4)
        print(f"      [gn resume from saved round {st[key]['it']}  "
              f"lam {lam:.0e}]", flush=True)
    hist = (st[key].get('hist', []) if st is not None and key is not None
            and key in st else [])
    esc = (st[key].get('esc', 0) if st is not None and key is not None
           and key in st else 0)
    n = x.size
    fx = wn(x)
    for it in range(rounds):
        rms_now = T.field_rms(x)
        # BAND BY BOTH SCALES (2026-08-22, annotated, measured): a
        # fresh pin move leaves field RMS tiny (inherited polish) but
        # wres large (the pin row); the single-attempt f64 endgame
        # then stalls at 'no step' while lam escalates. Endgame only
        # when BOTH the field and the weighted residual are small;
        # transitions take the multi-retry band.
        endgame = (rms_now < 3e-5 and fx < 1e-3) or n > 12000
        # (n > 12000: the f32 multi-retry band is noise-limited at
        # heavy damping -- steps below f32 solve precision cannot
        # improve an f64-measured residual -- and f64 multi-retry
        # cannot fit; the single-attempt f64 branch with persisted
        # lam is the memory-safe route at this size.)
        # REGISTERED ESCALATION (2026-08-22, ported verbatim from
        # the native96 FORCING INCIDENT rule): if the last 3 accepted
        # rounds improved < 25% cumulative, ALTERNATE the exact step
        # and the capped min-norm lsmr descent on a persistent
        # counter -- both objective-monotone, so the alternation is a
        # schedule, not a new solver. My earlier fallback fired only
        # on no-steps and slept through the 0.2%/round crawl; the
        # registered trigger catches the crawl.
        stalled = len(hist) >= 3 and fx > 0.75 * hist[-3]
        if stalled and esc % 2 == 1:
            esc += 1
            from scipy.sparse.linalg import lsmr, LinearOperator
            J2 = T.jac(x, pin_mode, aux, PW, dtype=np.float32)
            r2 = T.wres(x, pin_mode, aux, PW)
            op = LinearOperator(
                J2.shape,
                matvec=lambda v: (J2 @ v.astype(np.float32)
                                  ).astype(np.float64),
                rmatvec=lambda u: (J2.T @ u.astype(np.float32)
                                   ).astype(np.float64))
            dxl = lsmr(op, -r2, atol=1e-11, btol=1e-11,
                       maxiter=1500)[0]
            del J2
            acc = False
            for a_ in (1.0, 0.5, 0.25, 0.1):
                xt = x + a_ * dxl
                f2 = wn(xt)
                if f2 < fx and guard_ok(xt):
                    x, fx, acc = xt, f2, True
                    break
            hist = []
            r = T.field_rms(x)
            print(f"      [gn {it} (gnd-esc): RMS {r:.1e}  wres "
                  f"{fx:.2e}{'' if acc else '  no step'}]", flush=True)
            if st is not None and key is not None:
                st[key] = dict(x=x, it=it, lam=lam, hist=hist, esc=esc)
                save(st)
            if r < (stop_rms or RMS_BAR):
                if stop_rms is None or pin_mode != 'a2' or aux <= 1e-5:
                    break
                _, c2n = T.modes(T.geom(x)[2])
                if abs(abs(c2n) - aux) / aux < 0.05:
                    break
            continue
        if stalled:
            esc += 1
            hist = []
            lam = 1e-9        # gnx-esc: the exact step at the floor
        r0 = T.wres(x, pin_mode, aux, PW)
        J = T.jac(x, pin_mode, aux, PW, dtype=np.float32)
        Jtr = np.zeros(n)
        JtJ = np.zeros((n, n), order='F')
        for a in range(0, J.shape[0], 1024):
            B = np.asfortranarray(J[a:a + 1024].astype(np.float64))
            JtJ = _blas.dsyrk(1.0, B, beta=1.0, c=JtJ, trans=1,
                              lower=1, overwrite_c=1)
            Jtr += B.T @ r0[a:a + 1024]
        del J
        d2 = np.maximum(np.diag(JtJ).copy(), 1e-12)
        acc = False
        fx0 = fx
        if endgame:
            # f64 in-place, one damping attempt per Jacobian
            JtJ[np.arange(n), np.arange(n)] += lam * d2
            try:
                c, low = sla.cho_factor(JtJ, lower=True,
                                        overwrite_a=True,
                                        check_finite=False)
                dx = sla.cho_solve((c, low), -Jtr,
                                   check_finite=False)
                # TRUST CAP (2026-08-24, measured q5/3
                # cycle): huge floor steps exit the
                # basin; cap step length before the
                # fraction ladder. Monotone acceptance
                # and the guard are unchanged.
                _nd = float(np.linalg.norm(dx))
                if _nd > 0.05:
                    dx = dx * (0.05 / _nd)
                for a_ in (1.0, 0.5, 0.25, 0.1, 0.03):
                    xt = x + a_ * dx
                    f2 = wn(xt)
                    if f2 < fx and guard_ok(xt):
                        x, fx, acc = xt, f2, True
                        print(f"        [step: frac {a_}  |dx| "
                              f"{np.linalg.norm(dx):.2e}  df "
                              f"{1 - f2 / fx0:.2%}]", flush=True)
                        break
            except np.linalg.LinAlgError:
                pass
            lam = max(lam / 3.0, 1e-9) if acc else lam * 10.0
            del JtJ
            if not acc:
                # ALTERNATION FALLBACK (2026-08-22, annotated; the
                # registered escalation, lineage: the gnd-capped /
                # gnx alternation that broke every closure-subspace
                # circulation in the 96 and 112 fights): the
                # Marquardt-Cholesky step and the truncated-lsmr
                # step regularize DIFFERENTLY (diagonal damping vs
                # spectral cutoff); when the Cholesky operator
                # stalls, one deep undamped lsmr step is offered
                # under the same monotone acceptance and basin
                # guard. Measured trigger: waypoint-2 wres frozen at
                # 7.34e-3 across three floor-lam rounds then
                # no-step.
                from scipy.sparse.linalg import lsmr, LinearOperator
                J2 = T.jac(x, pin_mode, aux, PW, dtype=np.float32)
                r2 = T.wres(x, pin_mode, aux, PW)
                op = LinearOperator(
                    J2.shape,
                    matvec=lambda v: (J2 @ v.astype(np.float32)
                                      ).astype(np.float64),
                    rmatvec=lambda u: (J2.T @ u.astype(np.float32)
                                       ).astype(np.float64))
                dxl = lsmr(op, -r2, atol=1e-11, btol=1e-11,
                           maxiter=1500)[0]
                del J2
                for a_ in (1.0, 0.5, 0.25, 0.1):
                    xt = x + a_ * dxl
                    f2 = wn(xt)
                    if f2 < fx and guard_ok(xt):
                        x, fx, acc = xt, f2, True
                        break
                if acc:
                    print("      [alt: lsmr step accepted]",
                          flush=True)
        else:
            JtJ32 = np.asfortranarray(JtJ, dtype=np.float32)
            del JtJ
            for _ in range(6):
                A = JtJ32.copy()
                A[np.arange(n), np.arange(n)] += (lam * d2).astype(
                    np.float32)
                try:
                    c, low = sla.cho_factor(A, lower=True,
                                            overwrite_a=True,
                                            check_finite=False)
                    dx = sla.cho_solve((c, low),
                                       (-Jtr).astype(np.float32),
                                       check_finite=False
                                       ).astype(np.float64)
                except np.linalg.LinAlgError:
                    lam *= 10.0
                    continue
                del A
                _nd = float(np.linalg.norm(dx))
                if _nd > 0.05:   # TRUST CAP (2026-08-24)
                    dx = dx * (0.05 / _nd)
                xt = x + dx
                f2 = wn(xt)
                if f2 < fx and guard_ok(xt):
                    x, fx, acc = xt, f2, True
                    lam = max(lam / 3.0, 1e-8)
                    break
                lam *= 10.0
            del JtJ32
        r = T.field_rms(x)
        print(f"      [gn {it}{' (f64)' if endgame else ''}: RMS "
              f"{r:.1e}  wres {fx:.2e}  lam {lam:.0e}"
              f"{'' if acc else '  no step'}]", flush=True)
        if acc:
            hist = (hist + [fx])[-4:]
        if st is not None and key is not None:
            st[key] = dict(x=x, it=it, lam=lam, hist=hist, esc=esc)
            save(st)                  # persist even on no-step
        # RUNG EARLY-EXIT (2026-08-22, annotated, pacing; AMENDED
        # same day, measured defect): gating on field RMS alone let
        # rungs 2-4 'complete' in one round WITHOUT MOVING -- after a
        # pin move the field RMS stays tiny while the pin is
        # unsatisfied, so all four rungs stored the same iterate at
        # A2 = 1.79e-4 and the final solve was asked to grow the
        # mode 10x in one jump, exactly what the ladder exists to
        # avoid. A rung is done only when the field is quiet AND the
        # iterate has actually reached its sub-pin (5% relative).
        if r < (stop_rms or RMS_BAR):
            if stop_rms is None:
                # CLOSURE-AWARE STOP (2026-08-23, annotated,
                # measured): the first q4/3 arc member converged to
                # RMS 8.8e-9 but FAILED its gate at closure 4.7e-6
                # against the 1e-6 halt bar -- the RMS-only break
                # raced the closure polish while wres was still
                # descending 24%/round. A gate-facing solve runs
                # until BOTH bars it must face are satisfied (or
                # progress stops); this is the solve meeting its
                # own gates, not a bar change.
                if T.closure_max(x) < CLOSURE_BAR:
                    break
            else:
                pass
        if stop_rms is not None and r < stop_rms:
            if pin_mode == 'a2' and aux > 1e-5:
                _, c2n = T.modes(T.geom(x)[2])
                if abs(abs(c2n) - aux) / aux < 0.05:
                    break
            else:
                break
        if not acc and lam > 1e6:
            # REJECTION-ABORT PERSISTENCE (2026-08-24): keep the
            # solve key so the rung retry RESUMES this descent
            # instead of replaying from seed (the measured q5/3
            # cycle). Normal completions still clean their key.
            if st is not None and key is not None:
                st[key] = dict(x=x, it=it, lam=1e-7, hist=[],
                               esc=esc)
                save(st)
            return x, T.field_rms(x)
    if st is not None and key is not None and key in st:
        del st[key]
        save(st)
    return x, T.field_rms(x)


_ST = {}


def set_solve_key(st, key):
    _ST['st'], _ST['key'] = st, key


def solve_to_bar(T, x0, pin_mode, aux, rounds=6):
    """Loose-then-tight trf phases until the RMS bar or no progress.
    At n > 12000 the trf path OOMs this container (measured); the
    gn_lean ladder is used instead -- see its annotation."""
    if T.n > 12000:
        return gn_lean(T, x0, pin_mode, aux, st=_ST.get('st'),
                       key=_ST.get('key'))
    x, r = solve(T, x0, pin_mode, aux, nfev=60, tight=False)
    for _ in range(rounds):
        if r < RMS_BAR:
            break
        x2, r2 = solve(T, x, pin_mode, aux, nfev=40, tight=True)
        if r2 > 0.7 * r:
            x, r = (x2, r2) if r2 < r else (x, r)
            break
        x, r = x2, r2
    return x, r


def level1_check(T, x, tag):
    th, pt, Tf, o1, o2 = T.unpack(x)
    dev = float(np.ptp(th))
    dval = abs(float(th.mean()) - 0.955317)
    e_om = abs(float(o1) - S2.OM1_L1) / S2.OM1_L1
    e_T = float(np.abs(Tf - S2.TBAR).max())
    p = dev < 1e-6 and dval < 1e-3 and e_om < 1e-3 and e_T < 1e-3
    print(f"    [{tag}] theta dev {dev:.1e}  |theta-0.955317| "
          f"{dval:.1e}  Om1 rel {e_om:.1e}  max|T-3/2| {e_T:.1e}  "
          f"[{'PASS' if p else 'HALT'}]", flush=True)
    return p


def ramp_seed(T, A2first):
    """Stage-2's own m2-injection at the first pin amplitude, on this
    cell (the degenerate-|c2|-pin seeding lesson, replicated)."""
    G = T.G2
    W, Z, Tf, gam, om1 = G.level1()
    ph = (np.exp(1j * G.K2 * G.sgrid)[:, None]
          * np.exp(-1j * G.pgrid)[None, :])
    return T.from_stage2(G.pack(W + A2first * ph, Z, Tf, gam, om1, 3.20))


def arc_rate(T, st, key, x0, x1, targets, budget_steps=40):
    """Arc pairs from (x0, x1); returns measured (A2_mid, dA2/ds)
    list, marching until past max(targets) or the step budget."""
    cur = st.get(key, {})
    rates = cur.get('rates', [])
    x0, x1 = cur.get('pair', [x0, x1])
    while len(rates) < budget_steps:
        a_prev = metrics(T, x1)['A2']
        if rates and a_prev > max(targets) + 5e-4:
            break
        t = x1 - x0
        t /= np.linalg.norm(t)
        set_solve_key(st, f'{key}-solve')
        x2, r = solve_to_bar(T, x1 + DS * t, 'arc', (x1, t, DS))
        m, ok = gate(T, x2, f'{key} arc step {len(rates)}')
        if not ok:
            print(f"    [{key}] arc member FAILS GATES; rate march "
                  f"stops (full-bar rule)", flush=True)
            break
        rate = (m['A2'] - a_prev) / DS
        rates.append((0.5 * (m['A2'] + a_prev), float(rate)))
        print(f"    [{key}] dA2/ds = {rate:.3e} at A2 ~ "
              f"{rates[-1][0]:.6f}", flush=True)
        x0, x1 = x1, x2
        st[key] = dict(rates=rates, pair=[x0, x1])
        save(st)
    return rates


def run_q(st, n1, n2, ns, npn, qtag):
    T = QTGrid(ns, npn, n1, n2)
    q = st.setdefault(qtag, {})
    if q.get('halt'):
        print(f"== {qtag} previously halted: {q['halt']} ==", flush=True)
        return
    print(f"== Q-SWEEP {qtag}: cell {T.G2.LCELL:.4f}  K2/K1 = "
          f"{T.G2.K2 / S2.K1:.4f}  grid {ns} x {npn}  n = {T.n} ==",
          flush=True)

    if 'l1' not in q:                                   # P1 / bar (v2)
        set_solve_key(st, f'{qtag}-l1-solve')
        x, r = solve_to_bar(T, level1_seed(T), 'a2', 1e-6)
        if not level1_check(T, x, f'{qtag} level-1'):
            q['halt'] = 'bar (v2) level-1'
            save(st)
            return
        q['l1'] = x
        save(st)

    q.setdefault('members', [])
    x = q['members'][-1]['x'] if q['members'] else None
    while len(q['members']) < len(WAYPOINTS):           # P2
        A2 = WAYPOINTS[len(q['members'])]
        print(f"  [{qtag}] ramp pin A2 = {A2:.7f}", flush=True)
        # SUB-PIN LADDER (2026-08-22, annotated, same incident):
        # from the injection seed the pin is approached through
        # sub-waypoints (a ramp within the ramp -- measurement
        # scheduling), each held by the basin guard above; only the
        # final pin is solved to the full bar and gated.
        if x is None:
            xw = None
            for frac in (0.15, 0.3, 0.55, 0.8):
                rk = f'{qtag}-rung{frac}-done'
                if rk in st:               # completed rungs persist
                    xw = st[rk]
                    continue
                sub = frac * A2
                seed = ramp_seed(T, sub) if xw is None else xw
                key = (f'{qtag}-ramp{len(q["members"])}'
                       f'-sub{frac}-solve')
                print(f"    [sub-pin {sub:.7f}]", flush=True)
                xw, _ = gn_lean(T, seed, 'a2', sub, rounds=10,
                                st=st, key=key, stop_rms=1e-5)
                st[rk] = xw
                save(st)
            seed = xw
        else:
            # WAYPOINT RUNGS (2026-08-23, annotated, measured need):
            # the rungless member-1 -> waypoint-2 jump built
            # clos = 1.2e-3 of closure debt by corner-cutting,
            # leaving wres 5-10x the bottom sigma band where exact
            # GN steps inflate O(1); the a2, secant-arc, and
            # measured-singlet arc pins each failed with |dx|
            # tracking r/sigma of whichever soft mode remained
            # (0.89, 2.59, 2.22). The FND-146 states carry the same
            # band; the registered fights converged by never letting
            # the residual get that large. Rungs keep the debt
            # shallow -- that is their entire job. 40/70% of the
            # gap from the previous member, then the full pin.
            base = metrics(T, x)['A2']
            xw = x
            for frac in (0.4, 0.7):
                sub = base + frac * (A2 - base)
                rk = f'{qtag}-w{len(q["members"])}rung{frac}-done'
                if rk in st:
                    xw = st[rk]
                    continue
                key = (f'{qtag}-w{len(q["members"])}'
                       f'-sub{frac}-solve')
                print(f"    [sub-pin {sub:.7f}]", flush=True)
                xw, _ = gn_lean(T, xw, 'a2', sub, rounds=12,
                                st=st, key=key, stop_rms=1e-5)
                st[rk] = xw
                save(st)
            seed = xw
        set_solve_key(st, f'{qtag}-ramp{len(q["members"])}-solve')
        xn, r = solve_to_bar(T, seed, 'a2', A2)
        m, ok = gate(T, xn, f'{qtag} A2 = {A2:.7f}', pin=A2)
        m['x'] = xn
        q['members'].append(m)
        save(st)
        if not ok:
            q['halt'] = f'gates at waypoint {A2:.7f}'
            save(st)
            return
        x = xn

    if 'fine' not in q:                                 # the 0.0063 pin
        print(f"  [{qtag}] fine pin A2 = {FINE_PIN:.7f}", flush=True)
        # RUNGED (2026-08-23, annotated): this block predated the
        # waypoint-rung generalization and jumped direct; the audit
        # caught closure debt at 3.3e-4 half way up -- the rungless
        # syndrome, milder but the same mechanism. Same treatment.
        base = metrics(T, q['members'][-1]['x'])['A2']
        xw = q['members'][-1]['x']
        for frac in (0.4, 0.7):
            sub = base + frac * (FINE_PIN - base)
            rk = f'{qtag}-finerung{frac}-done'
            if rk in st:
                xw = st[rk]
                continue
            print(f"    [sub-pin {sub:.7f}]", flush=True)
            xw, _ = gn_lean(T, xw, 'a2', sub, rounds=12, st=st,
                            key=f'{qtag}-fine-sub{frac}-solve',
                            stop_rms=1e-5)
            st[rk] = xw
            save(st)
        set_solve_key(st, f'{qtag}-fine-solve')
        xn, r = solve_to_bar(T, xw, 'a2', FINE_PIN)
        m, ok = gate(T, xn, f'{qtag} A2 = {FINE_PIN:.7f}', pin=FINE_PIN)
        if ok:
            m['x'] = xn
            q['fine'] = m
        else:
            print(f"  [{qtag}] fine pin did not land at member grade "
                  f"(registered near-singularity class); the arc "
                  f"march from the waypoints is the fallback",
                  flush=True)
            q['fine'] = None
        save(st)

    # P3 -- rates at the matched targets, from arc pairs
    if 'hi_unreached' in q or 'hi_closed' in q:
        # the hi march was closed under the charter's
        # unreached-target clause (author-authorized); rates stand
        # as recorded and the D lower bound rides in q['hi_unreached']
        return
    lo = arc_rate(T, st, f'{qtag}-rate-lo',
                  q['members'][0]['x'], q['members'][1]['x'],
                  targets=[0.0048], budget_steps=6)
    if q.get('fine'):
        hi = arc_rate(T, st, f'{qtag}-rate-hi',
                      q['members'][1]['x'], q['fine']['x'],
                      targets=[0.0063], budget_steps=6)
    else:
        # (2026-08-23, annotated): the hi march continues FROM the lo
        # march's final pair rather than re-treading its six steps
        # from the member pair -- same instrument, same ds, the march
        # simply keeps walking. The lo rates already cover the ground
        # behind it.
        lo_pair = st.get(f'{qtag}-rate-lo', {}).get('pair')
        hx0, hx1 = (lo_pair if lo_pair is not None else
                    (q['members'][0]['x'], q['members'][1]['x']))
        hi = arc_rate(T, st, f'{qtag}-rate-hi', hx0, hx1,
                      targets=[0.0063], budget_steps=40)
    q['rates_lo'], q['rates_hi'] = lo, hi
    save(st)


def capture_singlet(st):
    """THE CHEAP SINGLET (2026-08-23, annotated): the heavyweight
    eigh probe kept being reaped mid-computation, but the inflated
    exact-GN step IS the measurement -- at the lam floor the step
    direction J^-1 r weights components by 1/sigma^2 and is
    overwhelmingly along the soft singlet. One Cholesky round on the
    a2-pinned system, normalize dx, validate by ||J t|| / ||t||
    (should sit near the probed sigma_eff = 8.24e-4, three orders
    under smax ~ 570)."""
    import scipy.linalg as sla
    from scipy.linalg import blas as _blas
    T = QTGrid(144, 36, 3, 4)
    key = 'q4/3-ramp1-solve'
    x = st[key]['x'] if key in st else st['q4/3']['members'][-1]['x']
    aux = WAYPOINTS[1]
    r0 = T.wres(x, 'a2', aux, 50.0)
    J = T.jac(x, 'a2', aux, 50.0, dtype=np.float32)
    n = x.size
    Jtr = np.zeros(n)
    JtJ = np.zeros((n, n), order='F')
    for a_ in range(0, J.shape[0], 1024):
        B = np.asfortranarray(J[a_:a_ + 1024].astype(np.float64))
        JtJ = _blas.dsyrk(1.0, B, beta=1.0, c=JtJ, trans=1,
                          lower=1, overwrite_c=1)
        Jtr += B.T @ r0[a_:a_ + 1024]
    d2 = np.maximum(np.diag(JtJ).copy(), 1e-12)
    JtJ[np.arange(n), np.arange(n)] += 1e-9 * d2
    c, low = sla.cho_factor(JtJ, lower=True, overwrite_a=True,
                            check_finite=False)
    dx = sla.cho_solve((c, low), -Jtr, check_finite=False)
    del JtJ
    t = dx / np.linalg.norm(dx)
    Jt = (J @ t.astype(np.float32)).astype(np.float64)
    del J
    sig_est = float(np.linalg.norm(Jt))
    print(f"singlet captured: |dx| {np.linalg.norm(dx):.2e}  "
          f"||J t|| {sig_est:.3e}  (probe sigma_eff 8.24e-4)",
          flush=True)
    N = T.N
    fr = {b_: float(t[sl] @ t[sl]) for b_, sl in
          (('th', slice(0, N)), ('pt', slice(N, 2 * N)),
           ('T', slice(2 * N, 3 * N)), ('om', slice(3 * N, None)))}
    print(f"singlet anatomy: "
          f"{ {k: round(v_, 4) for k, v_ in fr.items()} }", flush=True)
    st['q4/3-singlet'] = t
    st['q4/3-singlet-sig'] = sig_est
    save(st)
    print("singlet stored", flush=True)


def arc_land(st):
    """REGISTERED-DEVIATION-CLASS MOVE (2026-08-23, annotated;
    precedent: native96 pin 3, the FND-142 near-vertical-tangent
    class). The waypoint-2 a2-pinned solve crawled at <1%/round with
    exact-GN steps inflating to |dx| ~ 0.9 accepted only at the 3%
    fraction, and the sigma probe found the cause: an ISOLATED soft
    singlet at 8.24e-4 under an otherwise healthy doublet band
    (eff-ratio 1.445e-6, no FND-146-style collapse) -- the branch
    tangent leaking through an a2 pin gone nearly blind because
    dA2/ds is small here. The iterate was measurably SLIDING along
    the branch (om2 drifting) while fighting closure. The registered
    cure is the ARC pin, which constrains exactly the direction the
    a2 pin cannot: land the state at its current arc position
    (ds = 0) with the tangent from the member-1 pair, gate WITHOUT
    the pin requirement, and record the member at its MEASURED A2.
    Waypoints are scaffolding; rates cite full-bar members at
    measured amplitudes (the standing rule)."""
    T = QTGrid(144, 36, 3, 4)
    q = st['q4/3']
    key = 'q4/3-ramp1-solve'
    x_cur = st[key]['x'] if key in st else q['members'][-1]['x']
    x_m1 = q['members'][0]['x']
    # SINGULAR-COORDINATE PIN (2026-08-23, annotated; external
    # review step 4, adopted): the secant tangent failed -- at the
    # lam floor the exact step re-inflated (|dx| = 2.59 at the 3%
    # crumb), because near a dA2/ds collapse the TRUE local tangent
    # points mostly through om2, nearly orthogonal to the huge
    # member1 -> current secant. The pin direction is the MEASURED
    # soft singlet (capture_singlet), stored in the checkpoint.
    if 'q4/3-singlet' in st:
        t = np.asarray(st['q4/3-singlet'], float)
    else:
        t = x_cur - x_m1
    t /= np.linalg.norm(t)
    set_solve_key(st, 'q4/3-arcland-solve')
    xn, r = gn_lean(T, x_cur, 'arc', (x_cur, t, 0.0), rounds=60,
                    st=st, key='q4/3-arcland-solve')
    m, ok = gate(T, xn, 'q4/3 arc-landed waypoint 2', pin=None)
    if ok:
        m['x'] = xn
        m['arc_landed'] = True
        q['members'].append(m)
        st.pop(key, None)
        save(st)
        print("  [q4/3] waypoint-2 member LANDED by the arc pin at "
              f"measured A2 = {m['A2']:.7f}", flush=True)
    else:
        save(st)


def nearest(rates, a2):
    if not rates:
        return None
    return min(rates, key=lambda p: abs(p[0] - a2))


def main():
    st = load()

    # ---- bar (v1): QGrid reproduces the registered instrument ----
    if not st.get('v1'):
        print("== bar (v1): QTGrid(2,3) at 96 x 36 reproduces the "
              "registered instrument ==", flush=True)
        T = QTGrid(96, 36, 2, 3)
        n96 = pickle.loads(pathlib.Path('/tmp/n96_ckpt.pkl').read_bytes())
        m1 = n96['members'][1]
        m = metrics(T, np.asarray(m1['x'], float))
        rel = max(abs(m['A2'] - m1['A2']) / m1['A2'],
                  abs(m['om2'] - m1['om2']) / m1['om2'],
                  abs(m['gam'] - m1['gam']) / m1['gam'])
        okA = rel < 1e-6 and m['rms'] < RMS_BAR and m['clos'] < CLOSURE_BAR
        print(f"    S1 member re-verified: RMS {m['rms']:.2e}  max "
              f"metric rel {rel:.1e}  [{'PASS' if okA else 'HALT'}]",
              flush=True)
        x, r = solve_to_bar(T, level1_seed(T), 'a2', 1e-6)
        okB = level1_check(T, x, 'q=3/2 level-1')
        if not (okA and okB):
            st['halt'] = 'bar (v1)'
            save(st)
            return
        st['v1'] = True
        save(st)

    # ---- bar (v5), charter amendment 1: the ramp-solver control.
    # The identical ladder + guard + sub-pin protocol must reproduce
    # the registered q = 3/2 first-waypoint member from the injection
    # seed at 96 x 36 before any neighbor ramp outcome is
    # interpreted. Forced through gn_lean regardless of n.
    if not st.get('v5'):
        print("== bar (v5): lean-ladder ramp control at q = 3/2, "
              "96 x 36 ==", flush=True)
        T = QTGrid(96, 36, 2, 3)
        A2 = WAYPOINTS[0]
        xw = None
        for frac in (0.15, 0.3, 0.55, 0.8):
            sub = frac * A2
            seed = ramp_seed(T, sub) if xw is None else xw
            print(f"    [v5 sub-pin {sub:.7f}]", flush=True)
            xw, _ = gn_lean(T, seed, 'a2', sub, rounds=10,
                            st=st, key=f'v5-sub{frac}')
        xn, r = gn_lean(T, xw, 'a2', A2, rounds=40, st=st, key='v5-final')
        m, ok = gate(T, xn, f'v5 control A2 = {A2:.7f}', pin=A2)
        st['v5'] = dict(passed=bool(ok), metrics={k: v for k, v in
                                                  m.items() if k != 'x'})
        save(st)
        if not ok:
            print("bar (v5) FAILED -- the ladder cannot ramp where "
                  "the branch provably exists; neighbor outcomes are "
                  "INSTRUMENT statements only. HALT.", flush=True)
            return
        print("bar (v5) PASS -- the ladder is validated for ramping.",
              flush=True)

    run_q(st, 3, 4, 144, 36, 'q4/3')                    # neighbors
    run_q(st, 3, 5, 144, 36, 'q5/3')

    # ---- verdict: the registered rules on D(q) ----
    print("\n== Q-SWEEP STAGE 1 RULES (locked) ==", flush=True)
    D_REG = 6.5e-4 / 6.8e-5
    print(f"registered q = 3/2 collapse factor D = {D_REG:.1f}x",
          flush=True)
    Ds = {}
    for qtag in ('q4/3', 'q5/3'):
        q = st.get(qtag, {})
        lo = nearest(q.get('rates_lo', []), 0.0048)
        hi = nearest(q.get('rates_hi', []), 0.0063)
        if q.get('halt') or lo is None or hi is None or hi[1] <= 0:
            print(f"  {qtag}: NO CALL "
                  f"({q.get('halt', 'rates incomplete')})", flush=True)
            Ds[qtag] = None
            continue
        Ds[qtag] = lo[1] / hi[1]
        print(f"  {qtag}: dA2/ds {lo[1]:.3e} @ {lo[0]:.5f} -> "
              f"{hi[1]:.3e} @ {hi[0]:.5f}   D = {Ds[qtag]:.2f}x",
              flush=True)
    if all(d is not None for d in Ds.values()):
        a, b = Ds['q4/3'], Ds['q5/3']
        if a < 3 and b < 3:
            print("RULE S1-CELL: the collapse is a property of the "
                  "q = 3/2 rationalized cell; the split experiment "
                  "(stage 2) is chartered to confirm mechanism.",
                  flush=True)
        elif a > 5 and b > 5:
            print("RULE S1-BRANCH: the collapse reproduces across "
                  "rationalizations; direction-field mechanism "
                  "leads; the cell is acquitted at stage-1 grade.",
                  flush=True)
        elif (a < 3 and b > 5) or (a > 5 and b < 3):
            print("RULE S1-SPLIT: the neighbors disagree; stage 2 "
                  "REQUIRED before any interpretive grant.",
                  flush=True)
        else:
            print("NO CALL: outside the registered rules; report "
                  "and stop.", flush=True)


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'arcland':
        arc_land(load())
    elif len(sys.argv) > 1 and sys.argv[1] == 'singlet':
        capture_singlet(load())
    else:
        main()

def _atomic_write(path, data):
    """write to a temp file then rename: a full disk can truncate the temp file, never the checkpoint (2026-09-13)."""
    import os
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_bytes(data)
    os.replace(tmp, path)

