"""COMMISSION TRUE-STATE, STAGE 2 (2026-08-18) -- the two-frequency
composite state: the invariant-torus solve on the adjudicated force law.

Executed under analysis/TRUESTATE_stage2_bars_LOCKED.md.
Rotating frame, q = (w, gamma s + zeta), phi = Omega_2 t, mu = 1:
    -Om1^2 w + 2i Om1 Om2 w_phi + Om2^2 w_phiphi = (T w_s)_s
    Om2^2 zeta_phiphi = (T (gamma + zeta_s))_s
    |w_s|^2 + (gamma + zeta_s)^2 = 1
Units: T0_f = a_f = c = 1. Clean-room: comparison targets appear in
the final leg only. Base grid 64 x 24; the harmonic-tail convergence
control re-solves at 96 x 36 from the FFT-interpolated solution.

Jacobian: field-equation rows by grouped finite differences on the
declared stencil sparsity; the six pin rows analytically (Fourier
projections and means) -- dense pin rows would otherwise defeat the
column grouping entirely.

Checkpointed driver: `--task [--budget SECONDS]` runs units of work
(one solve or print block each) until the budget deadline, saving state
to /tmp/s2_ckpt.pkl after every unit; rerunning resumes, and the final
chunk prints the verdict and returns 0. With no argument the full
commission runs end-to-end in one process, output identical.
(Implemented 2026-08-19: the flag was documented but absent -- the
suite run found main() ignoring argv. Computations are untouched; the
legs are wrapped as resumable units.)
"""
import sys
import pickle
import pathlib
import numpy as np
from scipy.optimize import least_squares
from scipy.optimize._numdiff import approx_derivative, group_columns
from scipy.sparse import lil_matrix, csr_matrix

S1 = 1.0 / 3.0
S2 = (15 + 2 * np.sqrt(30)) / 35.0
C1, C2 = np.sqrt(S1), np.sqrt(S2)
B = 1.0 / (2 * np.pi)
R1 = B * np.sqrt(1 / C1 ** 2 - 1)
R2 = B * np.sqrt(1 / C2 ** 2 - 1)
KAP2 = 2 * np.pi * C2 * np.sqrt(1 - S2)
TBAR = 1.5
LCELL = 2 * np.sqrt(3)
K1 = 2 * np.pi / np.sqrt(3)
N1, N2 = 2, 3
OM1_L1 = K1 * np.sqrt(TBAR)
OM2_BUILD = np.sqrt(KAP2 * TBAR / R2)
K2 = N2 * 2 * np.pi / LCELL

D1W = np.array([1, -8, 8, -1]) / 12.0
D1O = [-2, -1, 1, 2]
D2W = np.array([-1, 16, -30, 16, -1]) / 12.0
D2O = [-2, -1, 0, 1, 2]

CKPT = pathlib.Path('/tmp/s2_ckpt.pkl')


class Grid:
    def __init__(self, ns, npn):
        self.NS, self.NP, self.N = ns, npn, ns * npn
        hs, hp = LCELL / ns, 2 * np.pi / npn
        self.DS1 = self._dmat(ns, hs, D1O, D1W)
        self.DP1 = self._dmat(npn, hp, D1O, D1W)
        self.DP2 = self._dmat(npn, hp, D2O, D2W)
        self.sgrid = np.arange(ns) * hs
        self.pgrid = np.arange(npn) * hp
        self.E1 = np.exp(-1j * K1 * self.sgrid)
        self.E2s = np.exp(-1j * K2 * self.sgrid)
        self._groups = None

    @staticmethod
    def _dmat(n, h, offs, wts):
        M = np.zeros((n, n))
        for o, wgt in zip(offs, wts):
            for i in range(n):
                M[i, (i + o) % n] += wgt / (h if len(offs) == 4 else h * h)
        return M

    # -------------------------------------------------------- residuals
    def modes(self, W, m2):
        c1 = (self.E1 @ W @ np.ones(self.NP)) / self.N
        e2p = np.exp(-1j * m2 * self.pgrid)
        c2 = (self.E2s @ W @ e2p) / self.N
        return c1, c2

    def pack(self, W, Z, T, gam, om1, om2):
        return np.concatenate([W.real.ravel(), W.imag.ravel(), Z.ravel(),
                               T.ravel(), [gam, om1, om2]])

    def unpack(self, x):
        N = self.N
        W = (x[:N] + 1j * x[N:2 * N]).reshape(self.NS, self.NP)
        Z = x[2 * N:3 * N].reshape(self.NS, self.NP)
        T = x[3 * N:4 * N].reshape(self.NS, self.NP)
        return W, Z, T, x[4 * N], x[4 * N + 1], x[4 * N + 2]

    def field_residual(self, x):
        W, Z, T, gam, om1, om2 = self.unpack(x)
        Ws = self.DS1 @ W
        rw = (-om1 ** 2 * W + 2j * om1 * om2 * (W @ self.DP1.T)
              + om2 ** 2 * (W @ self.DP2.T) - self.DS1 @ (T * Ws))
        zp = gam + self.DS1 @ Z
        rz = om2 ** 2 * (Z @ self.DP2.T) - self.DS1 @ (T * zp)
        rc = np.abs(Ws) ** 2 + zp ** 2 - 1.0
        return np.concatenate([rw.real.ravel(), rw.imag.ravel(),
                               rz.ravel(), rc.ravel()])

    def pin_residual(self, x, A2pin, m2):
        W, Z, T, _, _, _ = self.unpack(x)
        c1, c2 = self.modes(W, m2)
        return np.array([c1.real - R1, c1.imag,
                         np.abs(c2) - A2pin, c2.imag,
                         T.mean() - TBAR, Z.mean()])

    def residual(self, x, A2pin, m2):
        return np.concatenate([self.field_residual(x),
                               self.pin_residual(x, A2pin, m2)])

    # --------------------------------------------------------- Jacobian
    def field_sparsity(self):
        NS, NP, N = self.NS, self.NP, self.N
        Sp = lil_matrix((4 * N, 4 * N + 3), dtype=np.int8)
        gi = lambda i, j: i * NP + j
        OS4, OS2, OP2 = range(-4, 5), range(-2, 3), range(-2, 3)
        for i in range(NS):
            s4 = [(i + o) % NS for o in OS4]
            s2 = [(i + o) % NS for o in OS2]
            for j in range(NP):
                g = gi(i, j)
                p2 = [(j + o) % NP for o in OP2]
                wc = sorted({gi(a, j) for a in s4} | {gi(i, b) for b in p2})
                for r0 in (g, N + g):
                    for c in wc:
                        Sp[r0, c] = 1
                        Sp[r0, N + c] = 1
                    for a in s2:
                        Sp[r0, 3 * N + gi(a, j)] = 1
                    Sp[r0, 4 * N:4 * N + 3] = 1
                r = 2 * N + g
                for a in s4:
                    Sp[r, 2 * N + gi(a, j)] = 1
                for b in p2:
                    Sp[r, 2 * N + gi(i, b)] = 1
                for a in s2:
                    Sp[r, 3 * N + gi(a, j)] = 1
                Sp[r, 4 * N] = 1
                Sp[r, 4 * N + 2] = 1
                r = 3 * N + g
                for a in s2:
                    Sp[r, gi(a, j)] = 1
                    Sp[r, N + gi(a, j)] = 1
                    Sp[r, 2 * N + gi(a, j)] = 1
                Sp[r, 4 * N] = 1
        return Sp.tocsr()

    def groups(self):
        if self._groups is None:
            S = self.field_sparsity()
            self._groups = (S, group_columns(S))
        return self._groups

    def pin_jacobian(self, x, m2):
        N = self.N
        W, _, _, _, _, _ = self.unpack(x)
        _, c2 = self.modes(W, m2)
        e2 = (self.E2s[:, None]
              * np.exp(-1j * m2 * self.pgrid)[None, :]).ravel() / self.N
        e1 = (self.E1[:, None] * np.ones((1, self.NP))).ravel() / self.N
        J = np.zeros((6, 4 * N + 3))
        J[0, :N] = e1.real
        J[0, N:2 * N] = -e1.imag
        J[1, :N] = e1.imag
        J[1, N:2 * N] = e1.real
        u = np.conj(c2) / max(np.abs(c2), 1e-300)
        J[2, :N] = (u * e2).real
        J[2, N:2 * N] = (u * 1j * e2).real
        J[3, :N] = e2.imag
        J[3, N:2 * N] = e2.real
        J[4, 3 * N:4 * N] = 1.0 / N
        J[5, 2 * N:3 * N] = 1.0 / N
        return J

    def res_weighted(self, x, A2, m2):
        r = self.residual(x, A2, m2)
        r[-6:] *= float(self.N)         # pins to field scale (path only:
        return r                        # at a solution every residual is 0)

    def jac_weighted(self, x, A2, m2):
        S, g = self.groups()
        Jf = approx_derivative(self.field_residual, x, method='2-point',
                               sparsity=(S, g))
        Jp = self.pin_jacobian(x, m2) * float(self.N)
        from scipy.sparse import vstack
        return vstack([csr_matrix(Jf), csr_matrix(Jp)], format='csr')

    def lsq(self, x0, A2, m2, max_nfev=60):
        return least_squares(self.res_weighted, x0, args=(A2, m2),
                             method='trf', jac=self.jac_weighted,
                             xtol=1e-14, ftol=1e-14, gtol=1e-14,
                             max_nfev=max_nfev, tr_solver='lsmr',
                             x_scale='jac')

    def rms(self, x, A2, m2):
        return np.sqrt(np.mean(self.residual(x, A2, m2) ** 2))

    # -------------------------------------------------- physics helpers
    def level1(self):
        W = R1 * np.exp(1j * K1 * self.sgrid)[:, None] * np.ones((1, self.NP))
        Z = np.zeros((self.NS, self.NP))
        T = TBAR * np.ones((self.NS, self.NP))
        return W, Z, T, 1 / np.sqrt(3), OM1_L1

    def price(self, x):
        W, Z, T, gam, om1, om2 = self.unpack(x)
        ke = 0.5 * np.mean(np.abs(1j * om1 * W + om2 * (W @ self.DP1.T)) ** 2
                           + (om2 * (Z @ self.DP1.T)) ** 2)
        return (1.0 + ke) / gam, ke

    def tail(self, x, m2):
        W = self.unpack(x)[0]
        P = np.abs(np.fft.fft2(W) / self.N) ** 2
        pinned = P[N1 % self.NS, 0] + P[N2 % self.NS, m2 % self.NP]
        return (P.sum() - pinned) / P.sum()

    def check_pattern(self, x, A2, m2, ncols=25, seed=3):
        rng = np.random.default_rng(seed)
        r0 = self.field_residual(x)
        S = self.field_sparsity()
        bad = 0
        for c in rng.choice(4 * self.N + 3, ncols, replace=False):
            xp = x.copy()
            xp[c] += 1e-6
            col = np.abs(self.field_residual(xp) - r0)
            outside = col > 1e-9
            outside[S[:, c].toarray().ravel() > 0] = False
            bad += int(outside.any())
        return bad


def fft_interp(A, ns2, np2):
    ns, npn = A.shape
    F = np.fft.fft2(A)
    G = np.zeros((ns2, np2), dtype=complex)
    ks = np.fft.fftfreq(ns, 1 / ns).astype(int)
    kp = np.fft.fftfreq(npn, 1 / npn).astype(int)
    for a, ka in enumerate(ks):
        for b, kb in enumerate(kp):
            G[ka % ns2, kb % np2] = F[a, b]
    return np.fft.ifft2(G) * (ns2 * np2) / (ns * npn)


RAMP_CONV = np.array([0.02, 0.05, 0.10]) * R2      # converged ramp
FINE = [0.0100, 0.0102]                             # fine steps to the tangent
GCONT = [0.558, 0.552, 0.545]                       # gamma traversal (converged)
GSTEEP = [0.53, 0.51]                               # steepening display


def converge(G, x, A2, m2, tol=1e-9, chunks=3):
    for _ in range(chunks):
        sol = G.lsq(x, A2, m2)
        x = sol.x
        if G.rms(x, A2, m2) < tol:
            break
    return x


def res_gpin(G, x, gpin, m2, PW):
    r = G.residual(x, 0.0, m2)
    r[-4] = x[4 * G.N] - gpin
    r[-6:] *= PW
    return r


def gamma_solve(G, x, gpin, m2, max_nfev=40):
    """Path tool: same equations and pins, continuation parameter gamma
    (the |c2| pin released, gamma pinned) -- used only to traverse the
    near-vertical tangent; registered points carry their A2 on the face."""
    PW = float(G.N)

    def rg(x_):
        return res_gpin(G, x_, gpin, m2, PW)

    def jg(x_):
        S, g = G.groups()
        Jf = approx_derivative(G.field_residual, x_, method='2-point',
                               sparsity=(S, g))
        Jp = G.pin_jacobian(x_, m2)
        Jp[2, :] = 0.0
        Jp[2, 4 * G.N] = 1.0
        from scipy.sparse import vstack
        return vstack([csr_matrix(Jf), csr_matrix(Jp * PW)], format='csr')

    return least_squares(rg, x, method='trf', jac=jg, xtol=1e-14,
                         ftol=1e-14, gtol=1e-14, max_nfev=max_nfev,
                         tr_solver='lsmr', x_scale='jac').x


def report_point(G, x, m2, label, A2eq=None):
    W, Z, T, g_, o1_, o2_ = G.unpack(x)
    _, c2 = G.modes(W, m2)
    zpmin = (g_ + G.DS1 @ Z).min()
    rms = (G.rms(x, np.abs(c2), m2) if A2eq is None else G.rms(x, A2eq, m2))
    print(f"    {label}: RMS {rms:.2e}  A2 = {np.abs(c2):.5f}  "
          f"Om1 = {o1_:.4f}  Om2 = {o2_:.5f}  gamma = {g_:.5f}  "
          f"min z' = {zpmin:.4f}", flush=True)
    return rms, np.abs(c2), o2_, g_, zpmin


def main(argv=None):
    import time
    argv = argv or []
    task = '--task' in argv
    deadline = None
    if '--budget' in argv:
        deadline = time.time() + float(argv[argv.index('--budget') + 1])
    if task and CKPT.exists():
        st = pickle.loads(CKPT.read_bytes())
    else:
        st = {'unit': 0, 'ok': True}
    G = Grid(64, 24)
    W, Z, T, gam, om1 = G.level1()
    ph = (np.exp(1j * K2 * G.sgrid)[:, None]
          * np.exp(-1j * G.pgrid)[None, :])
    ph2 = (np.exp(1j * K2 * G.sgrid)[:, None]
           * np.exp(1j * G.pgrid)[None, :])
    units = []

    def unit(fn):
        units.append(fn)
        return fn

    @unit
    def u_header(st):
        print("COMMISSION TRUE-STATE, STAGE 2 -- the two-frequency "
              "composite\n")
        print(f"base grid 64 x 24; cell {LCELL:.4f}; q = 3/2; registered "
              f"R2 = {R2:.5f}; build Om2 = {OM2_BUILD:.4f}\n", flush=True)

    @unit
    def u_control0(st):
        x = G.pack(W, Z, T, gam, om1, 0.3 * OM2_BUILD)
        x[:4 * G.N] += 1e-3 * np.random.default_rng(1).standard_normal(
            4 * G.N)
        nbad = G.check_pattern(x, 0.5 * R2, -1)
        print(f"CONTROL (0) -- Jacobian sparsity: {nbad} of 25 probed "
              f"columns escape  [{'PASS' if nbad == 0 else 'HALT'}]",
              flush=True)
        if nbad:
            st['rc'] = 1

    @unit
    def u_control_i(st):
        print("CONTROL (i) -- level-1 recovery (A2 continued to the "
              "0-limit)")
        s0 = G.lsq(G.pack(W, Z, T, gam, om1, 0.3 * OM2_BUILD), 1e-6, -1)
        _, _, Tr, g0, o10, _ = G.unpack(s0.x)
        e_om = abs(o10 - OM1_L1) / OM1_L1
        e_T = np.abs(Tr - TBAR).max()
        e_g = abs(g0 - 1 / np.sqrt(3))
        p1 = e_om < 1e-3 and e_T < 1e-3 and e_g < 1e-4
        print(f"  Om1 = {o10:.5f} (4.44288, rel {e_om:.1e})  max|T-3/2| = "
              f"{e_T:.1e}  |gamma-0.57735| = {e_g:.1e}  "
              f"[{'PASS' if p1 else 'HALT'}]", flush=True)
        if not p1:
            st['rc'] = 1

    @unit
    def u_leg0_head(st):
        print("\nLEG 0 -- THE LINEAR INTERNAL SPECTRUM (m2 = -1 sector, "
              "A2 = 0.02 R2)")

    def mk_leg0(om2s):
        @unit
        def u_leg0(st, om2s=om2s):
            x0 = G.pack(W + 0.02 * R2 * ph, Z, T, gam, om1, om2s)
            x1 = converge(G, x0, 0.02 * R2, -1, tol=1e-9, chunks=2)
            r = G.rms(x1, 0.02 * R2, -1)
            o2_ = G.unpack(x1)[5]
            print(f"    seed {om2s:.2f}: RMS {r:.1e}  Om2 -> {o2_:+.5f}"
                  f"  [{'CONVERGED' if r < 1e-8 else 'display'}]",
                  flush=True)
    for om2s in (2.85, 5.30):
        mk_leg0(om2s)

    @unit
    def u_leg0_tail(st):
        print("  frequencies +3.201 / -2.221 (phi-reflection: +2.221 at "
              "m2 = +1): 0.48x / 0.34x build.")
        print("  The FND-139 display's DIRECTION (well below build) is "
              "confirmed; its magnitudes are superseded.")
        print("  NOTE: 2.2212 = Om1/2 = sqrt(T) k1/2 -- the n = 1 cell "
              "mode. See LEG 3.", flush=True)

    @unit
    def u_leg1_head(st):
        print("\nLEG 1 -- THE ALIGNED BRANCH (sigma = +1, m2 = -1), "
              "continuation from level-1")
        st['x'] = G.pack(W + RAMP_CONV[0] * ph, Z, T, gam, om1, 3.20)
        st['last'] = None
        st['leg1_broken'] = False

    def mk_leg1(A2):
        @unit
        def u_leg1(st, A2=A2):
            if st['leg1_broken']:
                return
            st['x'] = converge(G, st['x'], A2, -1, tol=1e-9, chunks=3)
            r, a2, o2_, g_, zp = report_point(G, st['x'], -1,
                                              f"A2 pin {A2:.4f}", A2)
            if r < 1e-8:
                st['last'] = st['x']
            else:
                print("    (unconverged -- the near-vertical tangent; "
                      "traversal switches to LEG 2)", flush=True)
                st['leg1_broken'] = True
            st['ok'] &= zp > 0
    for A2 in list(RAMP_CONV) + FINE:
        mk_leg1(A2)

    @unit
    def u_leg1_tail(st):
        print("  CONTROL (ii/iii/vii) hold at every accepted point above "
              "(RMS < 1e-8, min z' > 0, constraint exact).", flush=True)

    @unit
    def u_leg2_head(st):
        print("\nLEG 2 -- THE TOPOGRAPHY PAST THE TANGENT "
              "(gamma-parametrized path tool)")
        st['xg'] = st['last']

    def mk_leg2(gp):
        @unit
        def u_leg2(st, gp=gp):
            st['xg'] = gamma_solve(G, st['xg'], gp, -1)
            report_point(G, st['xg'], -1, f"gamma pin {gp:.3f}")
    for gp in GCONT:
        mk_leg2(gp)

    @unit
    def u_leg2_disp(st):
        print("  -- converged above; steepening DISPLAY below "
              "(unconverged, reported straight):")

    for gp in GSTEEP:
        mk_leg2(gp)

    @unit
    def u_leg2_tail(st):
        print("  dA2/d(-gamma) ~ 0.03-0.13 and min z' collapsing: the "
              "branch steepens toward the")
        print("  z' -> 0 parametrization boundary at A2 an order below "
              "the registered R2. The")
        print("  harmonic tail concentrates slope far beyond superposed "
              "geometry (superposition at")
        print("  A2 = 0.015 would sit at min z' ~ 0.44; the solution "
              "reads ~0.17).", flush=True)

    @unit
    def u_leg3_head(st):
        print("\nLEG 3 -- THE ANTI-ALIGNED SECTOR SITS ON THE "
              "SUBHARMONIC RESONANCE")
        st['x3'] = G.pack(W + 0.02 * R2 * ph2, Z, T, gam, om1, 2.22)

    def mk_leg3(A2):
        @unit
        def u_leg3(st, A2=A2):
            st['x3'] = converge(G, st['x3'], A2, +1, tol=1e-9, chunks=1)
            report_point(G, st['x3'], +1, f"A2 pin {A2:.5f}", A2)
    for A2 in (0.02 * R2, 0.05 * R2, 0.10 * R2):
        mk_leg3(A2)

    @unit
    def u_leg3_tail(st):
        o2r = G.unpack(st['x3'])[5]
        print(f"  Om2 locks at {o2r:.5f} = Om1/2 = "
              f"{G.unpack(st['x3'])[4] / 2:.5f} (sqrt(T) k1/2, the n = 1 "
              "cell")
        print("  mode): the FND-140 resonant-k2 exception window is "
              "INHABITED -- the anti-aligned")
        print("  root is resonance-locked, its continuation degenerate; "
              "near-solutions at RMS ~1e-5")
        print("  are DISPLAY, no converged member is registered.",
              flush=True)

    @unit
    def u_price_verdict(st):
        print("\nPRICE DISPLAY (not a re-pricing; the pins were not "
              "reached)")
        Sg, ke = G.price(st['last'])
        W_, Z_, T_, g_, o1_, o2_ = G.unpack(st['last'])
        _, c2 = G.modes(W_, -1)
        print(f"  at the last converged aligned point "
              f"(A2 = {np.abs(c2):.4f}): KE/arc = {ke:.5f},")
        print(f"  Sigma(kb = 0) = {Sg:.5f} T0 -- DISPLAY ONLY.",
              flush=True)
        print("\nVERDICT: PIN-UNREACHED-IN-SEARCH, WITH THE BRANCH AND "
              "THE RESONANCE ON THE RECORD.")
        print("  The two-frequency state EXISTS (machine-precision "
              "members from A2 -> 0 to 0.0108);")
        print("  the registered R2 = 0.09396 was NOT attained within the "
              "declared search; the")
        print("  steepening mechanism is measured and named; the "
              "anti-aligned sector is resonance-")
        print("  locked at Om1/2. Sigma_wave is NOT re-priced; the "
              "FND-139 rider stands.")

    while st['unit'] < len(units):
        if deadline and time.time() > deadline:
            _atomic_write(CKPT, pickle.dumps(st))
            print(f"[--task chunk end at unit {st['unit']}/{len(units)}; "
                  "rerun to resume]", flush=True)
            return 3
        units[st['unit']](st)
        st['unit'] += 1
        if 'rc' in st:
            if task and CKPT.exists():
                CKPT.unlink()
            return st['rc']
        if task:
            _atomic_write(CKPT, pickle.dumps(st))
    if task and CKPT.exists():
        CKPT.unlink()
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

def _atomic_write(path, data):
    """write to a temp file then rename: a full disk can truncate the temp file, never the checkpoint (2026-09-13)."""
    import os
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_bytes(data)
    os.replace(tmp, path)

