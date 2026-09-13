"""COMMISSION TRAVERSE (2026-08-18) -- the steepened-regime traversal:
the aligned two-frequency branch in a general-position representation.

Executed under analysis/TRAVERSE_bars_LOCKED.md. Same equations, same
pins as stage 2 (benchmarks/foundations/truestate_stage2.py); the ONE
instrument change is the chart -- tangent on the sphere,

    w_s = sin(theta) e^{i(K1 s + psit)},   z_s = cos(theta),

so pointwise inextensibility holds IDENTICALLY (the algebraic
constraint row and its 2 z' degeneracy are gone; theta = pi/2, i.e.
z' = 0, is an ordinary point and z' < 0 is representable) -- plus
pseudo-arclength continuation, so folds in A2 AND gamma are both
traversable. w and zeta are recovered by FD-CONSISTENT s-integration
(the circulant D_s inverted on its non-null modes; mean and s-Nyquist
projected, transverse closure imposed as equations). gamma is an
OUTPUT: gamma = <cos theta>.

Checkpointed pipeline: --pipeline runs seed -> c0 -> trav -> report,
saving to /tmp/trav_ckpt.pkl after every unit; rerunning resumes.
"""
import sys
import time
import pickle
import pathlib
import numpy as np
from scipy.optimize import least_squares

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from benchmarks.foundations import truestate_stage2 as S2

R1, R2, K1, K2, TBAR = S2.R1, S2.R2, S2.K1, S2.K2, S2.TBAR
OM1_L1, LCELL, N1, N2 = S2.OM1_L1, S2.LCELL, S2.N1, S2.N2
CKPT = pathlib.Path('/tmp/trav_ckpt.pkl')
SINTH_FLOOR = 0.05          # control (iii) chart-validity bar
DS_FLOOR = 1e-4             # declared step floor (bars)
RMS_BAR = 1e-8              # control (ii)


def w0_margin(om1, om2):
    """Control (vi): min over integer m != 0 of |Om1 - m Om2|."""
    return min(abs(om1 - m * om2) for m in range(1, 9))


class TGrid:
    """Tangent-sphere chart on the stage-2 grid and operators."""

    def __init__(self, ns, npn):
        self.G2 = S2.Grid(ns, npn)
        self.NS, self.NP, self.N = ns, npn, ns * npn
        self.DS1, self.DP1, self.DP2 = self.G2.DS1, self.G2.DP1, self.G2.DP2
        self.sgrid, self.pgrid = self.G2.sgrid, self.G2.pgrid
        self.E1, self.E2s = self.G2.E1, self.G2.E2s
        # circulant symbol of DS1: (DS1 v) = ifft(lam * fft(v))
        lam = np.conj(np.fft.fft(self.DS1[0, :]))
        v = np.random.default_rng(0).standard_normal(ns)
        assert np.allclose(self.DS1 @ v,
                           np.fft.ifft(lam * np.fft.fft(v)).real, atol=1e-10)
        self.null = np.abs(lam) < 1e-9          # mean + s-Nyquist
        self.lam_safe = np.where(self.null, 1.0, lam)
        self.PSI0 = (K1 * self.sgrid)[:, None]  # winding carried explicitly
        self.n = 3 * self.N + 2

    # ---------------------------------------------------------- recon
    def recon(self, F):
        """FD-consistent s-integration, batched over leading dims:
        returns D_s^+ F with mean and s-Nyquist modes projected out."""
        Fh = np.fft.fft(F, axis=-2)
        Fh = np.where(self.null[:, None], 0.0, Fh / self.lam_safe[:, None])
        return np.fft.ifft(Fh, axis=-2)

    def unpack(self, x):
        N = self.N
        sh = x.shape[:-1] + (self.NS, self.NP)
        th = x[..., :N].reshape(sh)
        pt = x[..., N:2 * N].reshape(sh)
        T = x[..., 2 * N:3 * N].reshape(sh)
        return th, pt, T, x[..., 3 * N], x[..., 3 * N + 1]

    def pack(self, th, pt, T, om1, om2):
        return np.concatenate([th.ravel(), pt.ravel(), T.ravel(),
                               [om1, om2]])

    # ----------------------------------------------------- geometry
    def geom(self, x):
        th, pt, T, om1, om2 = self.unpack(x)
        ws = np.sin(th) * np.exp(1j * (self.PSI0 + pt))
        zp = np.cos(th)
        w = self.recon(ws)
        ze = self.recon(zp + 0j).real
        gphi = zp.mean(axis=-2)                      # per-phi <cos th>_s
        gam = gphi.mean(axis=-1)
        return ws, zp, w, ze, gphi, gam, th, pt, T, om1, om2

    def modes(self, w):
        c1 = np.einsum('s,...sp->...', self.E1, w) / self.N
        e2p = np.exp(1j * self.pgrid)                # m2 = -1 sector
        c2 = np.einsum('s,...sp,p->...', self.E2s, w, e2p) / self.N
        return c1, c2

    # ---------------------------------------------------- residuals
    def residual(self, x, pin_mode, aux):
        """pin_mode 'a2': aux = A2 pin.  pin_mode 'arc': aux =
        (xprev, tprev, ds).  Returns UNWEIGHTED residual."""
        ws, zp, w, ze, gphi, gam, th, pt, T, om1, om2 = self.geom(x)
        o1 = om1[..., None, None] if np.ndim(om1) else om1
        o2 = om2[..., None, None] if np.ndim(om2) else om2
        wp = w @ self.DP1.T
        wpp = w @ self.DP2.T
        Rw = (-o1 ** 2 * w + 2j * o1 * o2 * wp + o2 ** 2 * wpp
              - self.DS1 @ (T * ws))
        Rz = o2 ** 2 * (ze @ self.DP2.T) - self.DS1 @ (T * zp)
        c0 = ws.mean(axis=-2)                        # transverse closure
        ca = gphi - gam[..., None] if np.ndim(gam) else gphi - gam
        c1, c2 = self.modes(w)
        if pin_mode == 'a2':
            prow = np.abs(c2) - aux
        else:
            xprev, tprev, ds = aux
            prow = (x - xprev) @ tprev - ds
        lead = x.shape[:-1]
        f = lambda a: a.reshape(lead + (-1,))
        pins = np.stack([c1.real - R1, c1.imag, prow, c2.imag,
                         T.mean(axis=(-2, -1)) - TBAR], axis=-1)
        return np.concatenate([f(Rw.real), f(Rw.imag), f(Rz),
                               f(c0.real), f(c0.imag), f(ca), pins],
                              axis=-1)

    def field_rms(self, x, pin_mode='a2', aux=0.0):
        r = self.residual(x, pin_mode, aux)
        return np.sqrt(np.mean(r[:3 * self.N] ** 2))

    def closure_max(self, x):
        r = self.residual(x, 'a2', 0.0)
        return np.abs(r[3 * self.N:3 * self.N + 3 * self.NP]).max()

    # ------------------------------------------------------- solver
    def wres(self, x, pin_mode, aux, PW):
        r = self.residual(x, pin_mode, aux)
        r[-5:] *= PW
        return r

    def jac(self, x, pin_mode, aux, PW, chunk=384):
        h = 1e-8 * (1.0 + np.abs(x))
        r0 = self.wres(x, pin_mode, aux, PW)
        J = np.empty((r0.size, x.size))
        for a in range(0, x.size, chunk):
            b = min(a + chunk, x.size)
            X = np.repeat(x[None, :], b - a, axis=0)
            X[np.arange(b - a), np.arange(a, b)] += h[a:b]
            R = self.wres_batch(X, pin_mode, aux, PW)
            J[:, a:b] = ((R - r0[None, :]) / h[a:b, None]).T
        return J

    def wres_batch(self, X, pin_mode, aux, PW):
        R = self.residual(X, pin_mode, aux)
        R[..., -5:] *= PW
        return R

    def solve(self, x0, pin_mode, aux, max_nfev=40):
        # path-only pin weight: N (stage-2's choice) conditions the
        # Krylov inner solver badly in the arc chart; 50 ~ sqrt(N)
        # restores fast lsmr convergence. Reported RMS stays unweighted.
        PW = 50.0
        return least_squares(
            self.wres, x0, jac=self.jac, args=(pin_mode, aux, PW),
            method='trf', tr_solver='lsmr', x_scale='jac',
            xtol=1e-14, ftol=1e-14, gtol=1e-14, max_nfev=max_nfev)

    # ---------------------------------------------- chart conversion
    def from_stage2(self, x2):
        W, Z, T, gam, om1, om2 = self.G2.unpack(x2)
        ws = self.DS1 @ W
        zpr = gam + self.DS1 @ Z
        th = np.arctan2(np.abs(ws), zpr)
        pt = np.angle(ws * np.exp(-1j * self.PSI0))
        pt = np.unwrap(np.unwrap(pt, axis=0), axis=1)
        pt -= 2 * np.pi * np.round(pt.mean() / (2 * np.pi))
        return self.pack(th, pt, T, om1, om2)

    def to_stage2(self, x):
        ws, zp, w, ze, gphi, gam, th, pt, T, om1, om2 = self.geom(x)
        return self.G2.pack(w, ze, T, gam, om1, om2)

    def report(self, x, label):
        ws, zp, w, ze, gphi, gam, th, pt, T, om1, om2 = self.geom(x)
        _, c2 = self.modes(w)
        rms = self.field_rms(x)
        nyq = np.abs(np.fft.fft(ws, axis=0)[self.NS // 2]).max() / self.NS
        print(f"    {label}: RMS {rms:.2e}  A2 = {np.abs(c2):.7f}  "
              f"Om2 = {om2:.5f}  gamma = {gam:.5f}  min z' = {zp.min():+.4f}"
              f"  min sin th = {np.sin(th).min():.4f}  "
              f"W0-margin = {w0_margin(om1, om2):.3f}  clos "
              f"{self.closure_max(x):.1e}  wsNyq {nyq:.1e}", flush=True)
        return dict(rms=rms, A2=float(np.abs(c2)), om1=float(om1),
                    om2=float(om2), gam=float(gam),
                    minzp=float(zp.min()), minsin=float(np.sin(th).min()))


# ==================================================================
def load():
    return pickle.loads(CKPT.read_bytes()) if CKPT.exists() else {}


def save(st):
    _atomic_write(CKPT, pickle.dumps(st))


def task_seed(st):
    """Regenerate the stage-2 aligned branch (LEG 1 ramp + gamma
    traversal converged points) as the seed and control-(0) targets."""
    print("TASK seed -- regenerating the FND-142 aligned branch "
          "(stage-2 instrument, its own code)", flush=True)
    G = S2.Grid(64, 24)
    W, Z, T, gam, om1 = G.level1()
    ph = (np.exp(1j * K2 * G.sgrid)[:, None]
          * np.exp(-1j * G.pgrid)[None, :])
    x = G.pack(W + S2.RAMP_CONV[0] * ph, Z, T, gam, om1, 3.20)
    members = []
    for A2 in list(S2.RAMP_CONV) + S2.FINE:
        x = S2.converge(G, x, A2, -1, tol=1e-9, chunks=3)
        r = G.rms(x, A2, -1)
        _, c2 = G.modes(G.unpack(x)[0], -1)
        print(f"    A2 pin {A2:.4f}: RMS {r:.2e}", flush=True)
        if r < RMS_BAR:
            members.append((float(np.abs(c2)), x.copy()))
        else:
            break
    xg = members[-1][1]
    for gp in S2.GCONT:
        xg = S2.gamma_solve(G, xg, gp, -1)
        r = G.rms(xg, 0.0, -1)
        rr = np.sqrt(np.mean(G.residual(xg, 0.0, -1)[:-6] ** 2))
        _, c2 = G.modes(G.unpack(xg)[0], -1)
        print(f"    gamma pin {gp:.3f}: field RMS {rr:.2e}  "
              f"A2 = {np.abs(c2):.5f}", flush=True)
        if rr < RMS_BAR:
            members.append((float(np.abs(c2)), xg.copy()))
    st['members'] = members
    st['stage'] = 'c0'
    save(st)
    print(f"  seed done: {len(members)} converged members, endpoint "
          f"A2 = {members[-1][0]:.5f}\n", flush=True)


def task_c0(st, deadline=None):
    """Controls (0), (i), (vii) -- nothing else reportable without."""
    T = TGrid(64, 24)
    members = st['members']
    print("CONTROL (0) -- representation equivalence on two registered "
          "members", flush=True)
    ok = True
    st.setdefault('c0_done', {})
    for idx in (len(members) // 2, len(members) - 1):
        if deadline and time.time() > deadline - 30:
            save(st)
            print("  [c0 chunk end -- rerun to resume]", flush=True)
            return
        if str(idx) in st['c0_done']:
            print(f"    member idx {idx}: done in a prior chunk "
                  f"[{st['c0_done'][str(idx)]}]", flush=True)
            ok &= st['c0_done'][str(idx)] == 'PASS'
            continue
        A2m, x2 = members[idx]
        G = S2.Grid(64, 24)
        _, _, _, gam2, _, om22 = G.unpack(x2)
        xt = T.from_stage2(x2)
        r_conv = st.get(f'c0_rconv{idx}', T.field_rms(xt))
        st[f'c0_rconv{idx}'] = float(r_conv)
        xcur = st.get(f'c0_x{idx}', xt)
        for _ in range(4):
            if deadline and time.time() > deadline - 60:
                st[f'c0_x{idx}'] = xcur
                save(st)
                print(f"    member A2 = {A2m:.5f}: mid-solve checkpoint "
                      f"(RMS {T.field_rms(xcur):.1e}); rerun to resume.",
                      flush=True)
                return
            sol = T.solve(xcur, 'a2', A2m, max_nfev=10)
            xcur = sol.x
            if T.field_rms(xcur) < RMS_BAR:
                break
        m = T.report(xcur, f"member A2 = {A2m:.5f} re-solved")
        sol_x = xcur
        d = max(abs(m['om2'] - om22) / om22, abs(m['gam'] - gam2) / gam2,
                abs(m['A2'] - A2m) / A2m)
        # LOCKED bar: reproduce Om2/gamma/A2 to 1e-6 rel at RMS < 1e-8.
        # The converted residual is a DIAGNOSTIC (it inherits the seed's
        # own stage-2 convergence level amplified by the chart map, and
        # is not a bar): an earlier implementation-added 1e-7 sub-bar
        # here HALTED on the endpoint member (converted 4.3e-7 from a
        # seed at stage-2 RMS 6.1e-9) while the locked bar passed by
        # three orders -- the catch is recorded, the code now conforms.
        p = d < 1e-6 and m['rms'] < RMS_BAR
        print(f"      converted-residual {r_conv:.1e} (diagnostic)  "
              f"max rel dev {d:.1e}  [{'PASS' if p else 'HALT'}]",
              flush=True)
        ok &= p
        st['c0_done'][str(idx)] = 'PASS' if p else 'HALT'
        if idx == len(members) - 1:
            st['x_seed'] = sol_x.copy()
        save(st)
    if not ok:
        raise SystemExit("HALT: control (0) failed -- instrument wrong; "
                         "nothing else from this run is reportable.")

    if deadline and time.time() > deadline - 30:
        save(st)
        print("  [c0 chunk end -- rerun to resume]", flush=True)
        return
    print("CONTROL (i) -- level-1 recovery (A2 pin 1e-6)", flush=True)
    th0 = np.arcsin(K1 * R1)
    th = np.full((64, 24), th0)
    pt = np.full((64, 24), np.pi / 2)
    Tf = np.full((64, 24), TBAR)
    sol = T.solve(T.pack(th, pt, Tf, OM1_L1, 3.20), 'a2', 1e-6,
                  max_nfev=25)
    tht, _, Tt, o1t, _ = T.unpack(sol.x)
    dev = np.ptp(tht)
    dval = abs(tht.mean() - 0.955317)
    e_om = abs(o1t - OM1_L1) / OM1_L1
    e_T = np.abs(Tt - TBAR).max()
    p1 = dev < 1e-6 and dval < 1e-3 and e_om < 1e-3 and e_T < 1e-3
    print(f"    theta const dev {dev:.1e}  |theta-0.955317| = {dval:.1e}"
          f"  Om1 rel {e_om:.1e}  max|T-3/2| = {e_T:.1e}  "
          f"[{'PASS' if p1 else 'HALT'}]", flush=True)
    if not p1:
        raise SystemExit("HALT: control (i) failed.")

    print("CONTROL (vii) -- declared dense-band influence pattern",
          flush=True)
    x = st['x_seed']
    N, NP = T.N, T.NP
    r0 = T.residual(x, 'a2', 0.0)
    rng = np.random.default_rng(3)
    bad = 0
    for c in rng.choice(T.n, 25, replace=False):
        xp = x.copy()
        xp[c] += 1e-6
        col = np.abs(T.residual(xp, 'a2', 0.0) - r0) > 1e-9
        mask = np.zeros(r0.size, bool)
        mask[3 * N:] = True                     # closures + pins: allowed
        if c >= 3 * N:                          # scalars: dense
            mask[:] = True
        elif c < 2 * N:
            # theta/psi column: dense in s within phi +-2 (reconstruction),
            # all three field blocks (theta drives Rz via cos theta)
            j0 = (c % N) % NP
            for jj in range(NP):
                if min((j0 - jj) % NP, (jj - j0) % NP) <= 2:
                    rows = np.arange(64) * NP + jj
                    mask[rows] = True
                    mask[N + rows] = True
                    mask[2 * N + rows] = True
        else:
            # T column: s +-2 in its own phi column (DS1 stencil)
            i = (c - 2 * N) // NP
            j0 = (c - 2 * N) % NP
            for di in range(-2, 3):
                g = ((i + di) % 64) * NP + j0
                mask[g] = True
                mask[N + g] = True
                mask[2 * N + g] = True
        col[mask] = False
        bad += int(col.any())
    print(f"    {bad} of 25 probed columns escape  "
          f"[{'PASS' if bad == 0 else 'HALT'}]", flush=True)
    if bad:
        raise SystemExit("HALT: control (vii) failed.")

    st['stage'] = 'trav'
    st['path'] = []
    save(st)
    print("", flush=True)


def task_trav(st, deadline=None):
    """Pseudo-arclength traversal of the aligned branch."""
    T = TGrid(64, 24)
    members = st['members']
    # tangent base: the converted penultimate member, UNSOLVED -- the
    # tangent is a predictor direction only; the corrector owns the
    # equations (a full re-solve here once ate an entire chunk budget).
    x1 = T.from_stage2(members[-2][1])
    x2 = st['x_seed']
    tprev = x2 - x1
    ds0 = np.linalg.norm(tprev)
    tprev /= ds0
    ds = st.get('ds', ds0)
    if st.get('path'):
        if len(st['path']) > 1:
            x1 = st['path'][-2]['x']
        x2 = st['path'][-1]['x']
        tprev = x2 - x1
        tprev /= np.linalg.norm(tprev)
    print(f"TASK trav -- pseudo-arclength from A2 = "
          f"{members[-1][0]:.5f}, ds0 = {ds0:.4f}, resuming at step "
          f"{len(st['path'])}", flush=True)
    A2max = max([members[-1][0]] + [q['A2'] for q in st['path']])
    step = len(st['path'])
    while step < 400:
        pend = st.get('pend')
        if pend is not None and pend.get('step') == step:
            xp, ds, rounds = pend['x'], pend['ds'], pend['rounds']
        else:
            xp = x2 + ds * tprev
            rounds = 0
        rms = np.inf
        while rounds < 3:
            if deadline and time.time() > deadline - 60:
                st['pend'] = dict(x=xp, ds=ds, rounds=rounds, step=step)
                save(st)
                print(f"    step {step:3d}: mid-solve checkpoint "
                      f"(round {rounds}); rerun to resume.", flush=True)
                return
            tsv = time.time()
            sol = T.solve(xp, 'arc', (x2, tprev, ds), max_nfev=14)
            xp = sol.x
            rounds += 1
            print(f"      [round {rounds}: {time.time()-tsv:.0f}s, "
                  f"RMS {T.field_rms(xp):.1e}]", flush=True)
            rms = T.field_rms(xp)
            if rms < RMS_BAR:
                break
        st.pop('pend', None)
        sol_x = xp
        if rms < RMS_BAR:
            m = T.report(sol_x, f"step {step:3d} ds {ds:.4f}")
            m['x'] = sol_x.copy()
            m['ds'] = ds
            st['path'].append(m)
            st['ds'] = ds
            save(st)
            A2max = max(A2max, m['A2'])
            if m['minsin'] <= SINTH_FLOOR:
                st['halt'] = 'chart'; save(st)
                print("  HALT: control (iii) chart-validity floor.",
                      flush=True); return
            if m['A2'] >= R2:
                st['stage'] = 'pin'; save(st)
                print("  REACHED: A2 >= R2 -- switching to the R2 pin.",
                      flush=True); return
            if A2max > 1.5 * members[-1][0] and m['A2'] < 0.6 * A2max \
                    and len(st['path']) > 10:
                st['halt'] = 'fold'; save(st)
                print(f"  FOLD REGISTERED: max A2 = {A2max:.5f}, "
                      "branch returning.", flush=True); return
            tnew = sol_x - x2
            tprev = tnew / np.linalg.norm(tnew)
            x2 = sol_x
            # measured: the ds=0.22 hyperplane misses the branch through
            # this high-curvature stretch (arc solve terminates at a
            # nonzero local minimum); 0.05 converges. Growth capped hard.
            ds = min(ds * 1.2, 0.08)
            step += 1
        else:
            ds *= 0.5
            print(f"    step {step:3d}: unconverged (RMS {rms:.1e}); "
                  f"ds -> {ds:.5f}", flush=True)
            if ds < DS_FLOOR:
                st['halt'] = 'floor'; save(st)
                print("  HALT: declared step floor 1e-4 reached.",
                      flush=True); return
    st['halt'] = 'budget'; save(st)
    print("  budget/step cap reached; path saved.", flush=True)


def task_pin(st):
    """Branch reached R2: pin exactly, tail control (iv), price."""
    T = TGrid(64, 24)
    x = st['path'][-1]['x']
    sol = T.solve(x, 'a2', R2, max_nfev=40)
    m = T.report(sol.x, "AT THE REGISTERED R2")
    st['x_R2'] = sol.x.copy()
    save(st)
    if m['rms'] >= RMS_BAR:
        print("  R2 pin did not converge from the reached point; "
              "registered as the last accepted state.", flush=True)
        return
    # control (iv): 96 x 36 re-solve from FFT-interpolated fields
    Tb = TGrid(96, 36)
    th, pt, Tf, o1, o2 = T.unpack(sol.x)
    xb = Tb.pack(S2.fft_interp(th, 96, 36).real,
                 S2.fft_interp(pt, 96, 36).real,
                 S2.fft_interp(Tf, 96, 36).real, o1, o2)
    solb = Tb.solve(xb, 'a2', R2, max_nfev=40)
    mb = Tb.report(solb.x, "tail control 96 x 36")
    Sg, _ = T.G2.price(T.to_stage2(sol.x))
    Sgb, _ = Tb.G2.price(Tb.to_stage2(solb.x))
    drift = abs(Sgb - Sg) / Sg
    print(f"    Sigma(kb=0) coarse {Sg:.5f}  fine {Sgb:.5f}  drift "
          f"{drift:.2%}  [{'PASS' if drift < 0.005 else 'DISPLAY ONLY'}]",
          flush=True)
    st['price'] = (float(Sg), float(Sgb), float(drift))
    save(st)


def task_report(st):
    """Final comparison leg -- clean room opens here."""
    print("\nFINAL LEG -- comparison targets enter (clean room)",
          flush=True)
    print("  registered box [3.222, 4.313]; level-1-exact 2.598; "
          "FND-142 price display 2.62.", flush=True)
    if 'price' in st:
        Sg, Sgb, drift = st['price']
        print(f"  Sigma_wave kb = 0 corner from THE SOLUTION: "
              f"{Sg:.4f} T0 (drift {drift:.2%}).", flush=True)
    else:
        p = st.get('path', [])
        if p:
            A2s = [q['A2'] for q in p]
            print(f"  no R2 solution: halt = {st.get('halt')}; "
                  f"max A2 on path = {max(A2s):.5f} of R2 = {R2:.5f}; "
                  f"last member A2 = {A2s[-1]:.5f}, min z' = "
                  f"{p[-1]['minzp']:+.4f}.", flush=True)


def main(argv):
    st = load()
    st.setdefault('stage', 'seed')
    if '--reset' in argv:
        st = {'stage': 'seed'}
    deadline = None
    if '--budget' in argv:
        deadline = time.time() + float(argv[argv.index('--budget') + 1])
    while True:
        if deadline and time.time() > deadline:
            save(st)
            print("[chunk end -- rerun to resume]", flush=True)
            return 0
        s = st['stage']
        if s == 'seed':
            task_seed(st)
        elif s == 'c0':
            task_c0(st, deadline)
            if st['stage'] == 'c0' and deadline and time.time() > deadline - 30:
                return 0
        elif s == 'trav':
            task_trav(st, deadline)
            if st.get('stage') == 'trav' and deadline and \
                    time.time() > deadline - 61:
                return 0
            if st.get('stage') != 'pin' and st.get('halt'):
                st['stage'] = 'done'
                save(st)
        elif s == 'pin':
            task_pin(st)
            st['stage'] = 'done'
            save(st)
        else:
            task_report(st)
            return 0


if __name__ == '__main__':
    raise SystemExit(main(sys.argv[1:]))

def _atomic_write(path, data):
    """write to a temp file then rename: a full disk can truncate the temp file, never the checkpoint (2026-09-13)."""
    import os
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_bytes(data)
    os.replace(tmp, path)

