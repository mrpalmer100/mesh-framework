"""COMMISSION QP-HULL-1 (draft charter analysis/QP_HULL_1_charter_DRAFT.md) -- the two-frequency state on a
two-phase HULL instrument without a rational cell (2026-10-19/20, the executor's build for Leg 0).

The registered instrument (TRUESTATE stage 2, the tangent-sphere chart of TRAVERSE, the (N1, N2) cells of
Q-SWEEP) discretizes u(s, phi) on a periodic cell of length N1 sqrt 3 holding N1 periods of level 1 and N2 of
level 2, so the modes (m1, m2) and (m1 + k N2, m2 - k N1) are one grid function (the cell aliases). Here the
state is a function of two independent phases, theta1 = K1 s and theta2 = K2 s with K2 = q K1, and of phi:

    u(theta1, theta2, phi), periodic 2 pi in each;   D_s = K1 D_theta1 + K2 D_theta2,

on a grid NT1 x NT2 x NP with the registered stencils (D1O/D1W, D2O/D2W) on each coordinate. The chart is
TRAVERSE's tangent sphere VERBATIM (w_s = sin theta e^{i(theta1 + pt)}, z_s = cos theta; w and zeta by the
FD-consistent inverse of D_s with its null modes projected; gamma = <cos theta>; the transverse-closure rows and
the per-phi gamma rows; the five pins), with D_s^+ taken on the (theta1, theta2) torus instead of the s-line. On
the hull the null set of D_s is {(0, 0)} for irrational q and {k (N2, -N1)} for q = N2 / N1 (the cell's aliases
of the mean, which the cell's single mean-closure row sums over); the closure rows are imposed per null mode.

Rational q and the credential. A cell state lifts to the hull by giving each cell wavenumber n (units 2 pi /
LCELL) the hull mode (m1, m2) of least |m1| + |m2| with m1 N1 + m2 N2 = n (mod ns); the restriction of a hull
function to the line theta2 = q theta1 (trigonometric interpolation in theta2) inverts the lift exactly, and
the hull solution at rational q restricted to the line is the credential's comparison with the retained cell
member (QP-HULL-1 v2). At the registered density per period the hull and the cell apply the SAME stencil
symbol to level-1 content, so the level-1 recovery coincides to roundoff (v1).

Solver: the SPARSE-J machinery (sparsej_instrument.gn_sparse: acceptance ladder, trust cap, basin guard, lam
schedule, stall escalation, all verbatim; BandedTorusSolver as the exact phi-major banded kernel, verbatim, with
the (theta1, theta2) torus in the place of the s-line) with the Jacobian assembled ANALYTICALLY from the recon
matrix (dense per phi-slice, banded across phi), replacing the colored finite differences of the cell instrument:
the hull's slices are too wide to probe column by column.

This file is an instrument. It computes nothing at q = 1.492 (QP-HULL-1 v7); its tests run at small grids.
"""
import pathlib
import sys
from fractions import Fraction

import numpy as np
import scipy.sparse as sp

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from benchmarks.foundations import truestate_stage2 as S2          # noqa: E402

R1, R2, K1, TBAR, OM1_L1 = S2.R1, S2.R2, S2.K1, S2.TBAR, S2.OM1_L1
D1O, D1W, D2O, D2W = S2.D1O, S2.D1W, S2.D2O, S2.D2W
Q_PHYS = 1.492                       # the registered ratio (TRUESTATE stage-1 bars)


def rational(q, max_den=1000, tol=1e-12):
    """(N1, N2) if q is rational to tol with denominator <= max_den, else None."""
    f = Fraction(q).limit_denominator(max_den)
    return (f.denominator, f.numerator) if abs(float(f) - q) < tol else None


def _circulant(n, h, offs, wts):
    M = np.zeros((n, n))
    p = 1 if len(offs) == 4 else 2
    for o, w in zip(offs, wts):
        for i in range(n):
            M[i, (i + o) % n] += w / h ** p
    return M


class HGrid:
    """The hull: grid, operators, chart, residual, analytic Jacobian. State x = [th, pt, T, om1, om2] with the
    fields stored (NS', NP), NS' = NT1 * NT2 ("s" index = theta1-major node on the torus), as TGrid stores them."""

    def __init__(self, nt1, nt2, npn, q):
        self.NT1, self.NT2, self.NP, self.q = nt1, nt2, npn, float(q)
        self.NS = nt1 * nt2
        self.N = self.NS * npn
        self.n = 3 * self.N + 2
        self.K1, self.K2 = K1, self.q * K1
        self.h1, self.h2, self.hp = 2 * np.pi / nt1, 2 * np.pi / nt2, 2 * np.pi / npn
        self.t1 = np.arange(nt1) * self.h1
        self.t2 = np.arange(nt2) * self.h2
        self.pgrid = np.arange(npn) * self.hp
        T1, T2 = np.meshgrid(self.t1, self.t2, indexing='ij')
        self.th1 = T1.ravel(); self.th2 = T2.ravel()                     # per torus node
        self.PSI0 = self.th1[:, None]                                       # the level-1 winding, explicit
        # operators: D_s on the torus is SPECTRAL (symbol i (K1 m1 + K2 m2), exact; Nyquist zeroed): directional
        # fourth-order stencils were tried first (Leg 0, 2026-10-20) and mis-derive the beat modes (m1, -m2),
        # whose small resultant wavenumber is the difference of two large ones with uncancelled truncation errors
        # (3.4 percent on (1, -1) at 12 x 8; om2 off by 4.6 percent against the 13/9 cell). The phi stencils are
        # the registered ones (DP1, DP2), as the cell has them.
        self.DP1 = _circulant(npn, self.hp, D1O, D1W)
        self.DP2 = _circulant(npn, self.hp, D2O, D2W)
        m1 = np.fft.fftfreq(nt1, 1.0 / nt1).astype(int)
        m2 = np.fft.fftfreq(nt2, 1.0 / nt2).astype(int)
        LAM = 1j * (self.K1 * m1[:, None] + self.K2 * m2[None, :])
        LAM[nt1 // 2, :] = 0.0; LAM[:, nt2 // 2] = 0.0                     # the grid's Nyquist lines
        self.LAM = LAM
        self.rat = rational(self.q)
        if self.rat:
            n1, n2 = self.rat
            ks = range(0, 1 + max(nt1, nt2))
            self.null = [(k * n2, -k * n1) for k in ks if k * n2 < nt1 / 2 and k * n1 < nt2 / 2]
        else:
            self.null = [(0, 0)]
        M1, M2 = m1[:, None], m2[None, :]
        nullmask = np.zeros((nt1, nt2), bool)
        for a, b in self.null:
            nullmask |= ((M1 - a) % nt1 == 0) & ((M2 - b) % nt2 == 0)
            nullmask |= ((M1 + a) % nt1 == 0) & ((M2 + b) % nt2 == 0)
        nullmask |= np.abs(self.LAM) < 1e-9 * self.K1                    # the Nyquist lines and exact nulls
        self.nullmask = nullmask
        self.lam_safe = np.where(nullmask, 1.0, self.LAM)
        # the recon matrix R (NS' x NS', complex): w = R ws per phi, the FD-consistent inverse with nulls projected
        self.R = self._recon_matrix()
        self.Ds = self._symbol_matrix(self.LAM)                              # dense NS' x NS' (Jacobian only)
        self.selfconj = [((2 * a) % nt1 == 0 and (2 * b) % nt2 == 0) for a, b in self.null]
        self.nullbasis = [np.exp(1j * (a * self.th1 + b * self.th2)) for a, b in self.null]
        self.e1 = np.exp(-1j * self.th1)                                    # level-1 projector on the torus
        self.e2 = np.exp(-1j * self.th2)                                    # level-2 projector on the torus

    def _symbol_matrix(self, sym):
        """The dense matrix of the Fourier multiplier sym (nt1, nt2) on theta1-major vectors."""
        nt1, nt2 = self.NT1, self.NT2
        I = np.eye(nt1 * nt2).reshape(nt1, nt2, nt1 * nt2)
        Fh = np.fft.fft2(I, axes=(0, 1)) * sym[:, :, None]
        return np.fft.ifft2(Fh, axes=(0, 1)).reshape(nt1 * nt2, nt1 * nt2)

    def _recon_matrix(self):
        return self._symbol_matrix(np.where(self.nullmask, 0.0, 1.0 / self.lam_safe))

    def ds(self, F):
        """D_s F per phi by FFT on the torus (F: (NS', NP))."""
        sh = F.shape
        G = F.reshape(self.NT1, self.NT2, -1)
        return np.fft.ifft2(np.fft.fft2(G, axes=(0, 1)) * self.LAM[:, :, None], axes=(0, 1)).reshape(sh)

    # ----------------------------------------------------------------- chart (TGrid verbatim in form)
    def recon(self, F):
        """D_s^+ F per phi (F: (NS', NP) or (NS',)) by FFT on the torus with the null set projected."""
        sh = F.shape
        G = F.reshape(self.NT1, self.NT2, -1)
        Fh = np.fft.fft2(G, axes=(0, 1))
        Fh = np.where(self.nullmask[:, :, None], 0.0, Fh / self.lam_safe[:, :, None])
        return np.fft.ifft2(Fh, axes=(0, 1)).reshape(sh)

    def unpack(self, x):
        N = self.N
        sh = (self.NS, self.NP)
        return (x[:N].reshape(sh), x[N:2 * N].reshape(sh), x[2 * N:3 * N].reshape(sh), x[3 * N], x[3 * N + 1])

    def pack(self, th, pt, T, om1, om2):
        return np.concatenate([th.ravel(), pt.ravel(), T.ravel(), [om1, om2]])

    def geom(self, x):
        th, pt, T, om1, om2 = self.unpack(x)
        ws = np.sin(th) * np.exp(1j * (self.PSI0 + pt))
        zp = np.cos(th)
        w = self.recon(ws)
        ze = self.recon(zp + 0j).real
        gphi = zp.mean(axis=0)
        gam = gphi.mean()
        return ws, zp, w, ze, gphi, gam, th, pt, T, om1, om2

    def modes(self, w):
        c1 = np.einsum('s,sp->', self.e1, w) / self.N
        c2 = np.einsum('s,sp,p->', self.e2, w, np.exp(1j * self.pgrid)) / self.N     # m2 = -1 sector
        return c1, c2

    def content(self, F, e):
        """Per-phi content of F on the torus mode e: (NP,) complex."""
        return np.einsum('s,sp->p', np.conj(e), F) / self.NS

    def residual(self, x, pin_mode, aux):
        ws, zp, w, ze, gphi, gam, th, pt, T, om1, om2 = self.geom(x)
        wp = w @ self.DP1.T
        wpp = w @ self.DP2.T
        Rw = -om1 ** 2 * w + 2j * om1 * om2 * wp + om2 ** 2 * wpp - self.ds(T * ws)
        Rz = om2 ** 2 * (ze @ self.DP2.T) - self.ds(T * zp).real
        rows = [Rw.real.ravel(), Rw.imag.ravel(), Rz.ravel()]
        for (a, b), e, sc in zip(self.null, self.nullbasis, self.selfconj):
            for ee in ([e] if sc else [e, np.conj(e)]):
                c0 = self.content(ws, ee)
                rows += [c0.real, c0.imag]
            if (a, b) == (0, 0):
                rows += [gphi - gam]
            else:
                cz = self.content(zp, e)
                rows += [cz.real] if sc else [cz.real, cz.imag]
        c1, c2 = self.modes(w)
        if pin_mode == 'a2':
            prow = abs(c2) - aux
        else:
            xprev, tprev, ds = aux
            prow = (x - xprev) @ tprev - ds
        rows.append(np.array([c1.real - R1, c1.imag, prow, c2.imag, T.mean() - TBAR]))
        return np.concatenate(rows)

    def field_rms(self, x, pin_mode='a2', aux=0.0):
        r = self.residual(x, pin_mode, aux)
        return np.sqrt(np.mean(r[:3 * self.N] ** 2))

    def closure_max(self, x):
        r = self.residual(x, 'a2', 0.0)
        return np.abs(r[3 * self.N:-5]).max()

    def wres(self, x, pin_mode, aux, PW):
        r = self.residual(x, pin_mode, aux)
        r[-5:] *= PW
        return r

    # ----------------------------------------------------------------- analytic Jacobian
    def jacobian(self, x, pin_mode, aux, PW):
        """J (csr, m x n) of wres at x, assembled from the recon matrix: dense (NS' x NS') blocks for the
        (theta-torus) coupling of each phi-slice with its phi-stencil neighbours, sparse D_s blocks for the
        local terms, dense closure and pin rows."""
        ws, zp, w, ze, gphi, gam, th, pt, T, om1, om2 = self.geom(x)
        NS, NP, N = self.NS, self.NP, self.N
        R, Ds = self.R, self.Ds
        a = np.cos(th) * np.exp(1j * (self.PSI0 + pt))      # d ws / d th
        b = 1j * ws                                          # d ws / d pt
        dz = -np.sin(th)                                     # d zp / d th
        # phi-stencil coefficients: Lphi(w)[:, k] = sum_o c_o w[:, k + o]
        cw = {}
        for o, w1, w2 in [(-2, D1W[0], D2W[0]), (-1, D1W[1], D2W[1]), (0, 0.0, D2W[2]), (1, D1W[2], D2W[3]), (2, D1W[3], D2W[4])]:
            cw[o] = (-om1 ** 2 if o == 0 else 0.0) + 2j * om1 * om2 * w1 / self.hp + om2 ** 2 * w2 / self.hp ** 2
        cz = {o: om2 ** 2 * w2 / self.hp ** 2 for o, w2 in zip(D2O, D2W)}
        Rr = R.real
        rowsR, colsR, valsR = [], [], []              # Rw real rows (block k) ... assembled as COO pieces

        def put(rblock, cblock, B):
            """dense block B (NS x NS) at row block rblock (slice k, field rows) and column block cblock."""
            B = np.asarray(B)
            nz = np.nonzero(B)
            rowsR.append(rblock[0] + nz[0] * rblock[1]); colsR.append(cblock[0] + nz[1] * cblock[1])
            valsR.append(B[nz])
        # row index of Rw.re at (s, k): s*NP + k ; Rw.im: N + s*NP + k ; Rz: 2N + s*NP + k
        # column index of th at (s, k): s*NP + k ; pt: N + ... ; T: 2N + ...
        for k in range(NP):
            rw_re = (k, NP); rw_im = (N + k, NP); rz = (2 * N + k, NP)
            for o in range(-2, 3):
                kk = (k + o) % NP
                c_th = (kk, NP); c_pt = (N + kk, NP)
                Mth = cw[o] * (R * a[:, kk][None, :])                   # complex NS x NS
                Mpt = cw[o] * (R * b[:, kk][None, :])
                if o == 0:
                    L = Ds * T[:, k][None, :]                            # dense complex: D_s diag(T)
                    Mth = Mth - L * a[:, k][None, :]
                    Mpt = Mpt - L * b[:, k][None, :]
                put(rw_re, c_th, Mth.real); put(rw_im, c_th, Mth.imag)
                put(rw_re, c_pt, Mpt.real); put(rw_im, c_pt, Mpt.imag)
                Mz = cz[o] * (Rr * dz[:, kk][None, :])
                if o == 0:
                    Mz = Mz - (L * dz[:, k][None, :]).real
                put(rz, c_th, Mz)
            # T columns: -D_s diag(ws), -Re D_s diag(zp)
            LT = Ds * ws[:, k][None, :]; put(rw_re, (2 * N + k, NP), -LT.real); put(rw_im, (2 * N + k, NP), -LT.imag)
            put(rz, (2 * N + k, NP), -(Ds * zp[:, k][None, :]).real)
        rows = np.concatenate(rowsR); cols = np.concatenate(colsR); vals = np.concatenate(valsR)
        # global columns
        g1 = -2 * om1 * w + 2j * om2 * (w @ self.DP1.T)
        g2 = 2j * om1 * (w @ self.DP1.T) + 2 * om2 * (w @ self.DP2.T)
        gz = 2 * om2 * (ze @ self.DP2.T)
        rows = np.concatenate([rows, np.arange(2 * N), np.arange(3 * N)])
        cols = np.concatenate([cols, np.full(2 * N, 3 * N), np.full(3 * N, 3 * N + 1)])
        vals = np.concatenate([vals, g1.real.ravel(), g1.imag.ravel(), g2.real.ravel(), g2.imag.ravel(), gz.ravel()])
        Jf = sp.csr_matrix((vals, (rows, cols)), shape=(3 * N, self.n))
        # dense rows: closures and pins
        dense = []
        node = np.arange(NS)[:, None] * NP + np.arange(NP)[None, :]
        for (a_, b_), e, sc in zip(self.null, self.nullbasis, self.selfconj):
            for ee in ([e] if sc else [e, np.conj(e)]):
                cb = np.conj(ee)[:, None] / NS
                Dre = np.zeros((NP, self.n)); Dim = np.zeros((NP, self.n))
                for k in range(NP):
                    Dre[k, node[:, k]] = (cb[:, 0] * a[:, k]).real; Dre[k, N + node[:, k]] = (cb[:, 0] * b[:, k]).real
                    Dim[k, node[:, k]] = (cb[:, 0] * a[:, k]).imag; Dim[k, N + node[:, k]] = (cb[:, 0] * b[:, k]).imag
                dense += [Dre, Dim]
            if (a_, b_) == (0, 0):
                D = np.zeros((NP, self.n))
                for k in range(NP):
                    D[k, node[:, k]] = dz[:, k] / NS
                D[:, :N] -= (dz / (NS * NP)).ravel()[None, :]
                dense.append(D)
            else:
                cb = np.conj(e)[:, None] / NS
                Dre = np.zeros((NP, self.n)); Dim = np.zeros((NP, self.n))
                for k in range(NP):
                    Dre[k, node[:, k]] = (cb[:, 0] * dz[:, k]).real; Dim[k, node[:, k]] = (cb[:, 0] * dz[:, k]).imag
                dense += [Dre] if sc else [Dre, Dim]
        # pins: c1 = mean(e1 . R ws), c2 = mean(e2 e^{i phi} . R ws)
        c1, c2 = self.modes(w)
        u1 = (self.e1 @ R) / N                                       # row vector over torus nodes
        u2 = (self.e2 @ R) / N
        P = np.zeros((5, self.n))
        for k in range(NP):
            P[0, node[:, k]] = (u1 * a[:, k]).real; P[0, N + node[:, k]] = (u1 * b[:, k]).real
            P[1, node[:, k]] = (u1 * a[:, k]).imag; P[1, N + node[:, k]] = (u1 * b[:, k]).imag
            ph = np.exp(1j * self.pgrid[k])
            d2 = u2 * ph
            if pin_mode == 'a2':
                uu = np.conj(c2) / max(abs(c2), 1e-300)
                P[2, node[:, k]] = (uu * d2 * a[:, k]).real; P[2, N + node[:, k]] = (uu * d2 * b[:, k]).real
            P[3, node[:, k]] = (d2 * a[:, k]).imag; P[3, N + node[:, k]] = (d2 * b[:, k]).imag
        if pin_mode != 'a2':
            P[2, :] = aux[1]
        P[4, 2 * N:3 * N] = 1.0 / N
        P *= PW
        J = sp.vstack([Jf, sp.csr_matrix(np.vstack(dense + [P]))], format='csr')
        return J

    # ----------------------------------------------------------------- seeds and the cell maps
    def level1_seed(self, om2=3.20):
        th0 = np.arcsin(K1 * R1)
        return self.pack(np.full((self.NS, self.NP), th0), np.full((self.NS, self.NP), np.pi / 2),
                         np.full((self.NS, self.NP), TBAR), OM1_L1, om2)

    def ramp_seed(self, x, A2, m2=-1):
        """Stage 2's m2 injection on a level-1 chart state: w += A2 e^{i theta2} e^{-i m2 phi}, re-charted."""
        ws, zp, w, ze, gphi, gam, th, pt, T, om1, om2 = self.geom(x)
        w2 = w + A2 * np.exp(1j * self.th2)[:, None] * np.exp(1j * m2 * self.pgrid)[None, :]   # e^{i theta2 - i phi}, as ramp_seed
        ws2 = self.ds(w2)
        th2 = np.arctan2(np.abs(ws2), zp)
        pt2 = np.angle(ws2 * np.exp(-1j * self.PSI0))
        pt2 = np.unwrap(pt2.reshape(self.NT1, self.NT2, self.NP), axis=0).reshape(self.NS, self.NP)
        return self.pack(th2, pt2, T, om1, om2)

    def lift_table(self, cell):
        n1, n2 = cell.G2.N1, cell.G2.N2
        ns = cell.NS
        m1s = np.fft.fftfreq(self.NT1, 1.0 / self.NT1).astype(int)
        m2s = np.fft.fftfreq(self.NT2, 1.0 / self.NT2).astype(int)
        best = {}
        for a in m1s:
            for b in m2s:
                n = (a * n1 + b * n2) % ns
                if n > ns // 2:
                    continue
                cost = (abs(a) + abs(b), abs(b), abs(a), -a, -b)
                if n not in best or cost < best[n][0]:
                    best[n] = (cost, a, b)
        table = {}
        for n, (cost, a, b) in best.items():
            table[n] = (a, b); table[(-n) % ns] = (-a, -b)
        return table

    def lift_field(self, f, cell, table):
        """cell field (ns, NP) -> hull field (NS', NP)."""
        F = np.fft.fft(f, axis=0) / cell.NS
        out = np.zeros((self.NT1, self.NT2, self.NP), dtype=complex)
        for idx, n in enumerate(np.fft.fftfreq(cell.NS, 1.0 / cell.NS).astype(int)):
            key = n % cell.NS
            if key in table:
                a, b = table[key]
                out[a % self.NT1, b % self.NT2, :] += F[idx, :]
        return (np.fft.ifft2(out, axes=(0, 1)) * (self.NT1 * self.NT2)).reshape(self.NS, self.NP)

    def restrict_field(self, F, cell):
        """hull field (NS', NP) -> cell field (ns, NP) on the line theta2 = q theta1, by two-dimensional
        trigonometric interpolation (exact for the band-limited hull function at any density ratio)."""
        ns = cell.NS
        th1 = (self.K1 * cell.sgrid) % (2 * np.pi)
        th2 = (cell.G2.K2 * cell.sgrid) % (2 * np.pi)
        G = F.reshape(self.NT1, self.NT2, self.NP)
        Fh = np.fft.fft2(G, axes=(0, 1)) / (self.NT1 * self.NT2)
        m1 = np.fft.fftfreq(self.NT1, 1.0 / self.NT1); m2 = np.fft.fftfreq(self.NT2, 1.0 / self.NT2)
        E1 = np.exp(1j * np.outer(th1, m1)); E2 = np.exp(1j * np.outer(th2, m2))       # (ns, NT1), (ns, NT2)
        # out[k, p] = sum_{a, b} E1[k, a] E2[k, b] Fh[a, b, p]
        return np.einsum('ka,kb,abp->kp', E1, E2, Fh, optimize=True)

    def lift_state(self, xc, cell):
        table = self.lift_table(cell)
        th, pt, T, om1, om2 = cell.unpack(xc)
        L = lambda f: self.lift_field(f, cell, table).real
        return self.pack(L(th), L(pt), L(T), float(om1), float(om2))

    def prolong_field(self, F, Hs):
        """hull field on a coarser hull grid Hs (same NP) -> this grid, by zero-padded 2D FFT (exact for the
        band-limited coarse function; this grid must hold every coarse mode)."""
        G = np.asarray(F).reshape(Hs.NT1, Hs.NT2, self.NP)
        Fh = np.fft.fft2(G, axes=(0, 1)) / (Hs.NT1 * Hs.NT2)
        out = np.zeros((self.NT1, self.NT2, self.NP), dtype=complex)
        m1 = np.fft.fftfreq(Hs.NT1, 1.0 / Hs.NT1).astype(int)
        m2 = np.fft.fftfreq(Hs.NT2, 1.0 / Hs.NT2).astype(int)
        for i, a in enumerate(m1):
            for j, b in enumerate(m2):
                out[a % self.NT1, b % self.NT2, :] += Fh[i, j, :]
        return (np.fft.ifft2(out, axes=(0, 1)) * (self.NT1 * self.NT2)).reshape(self.NS, self.NP)

    def prolong_state(self, xs, Hs):
        th, pt, T, om1, om2 = Hs.unpack(xs)
        P = lambda f: self.prolong_field(f, Hs).real
        return self.pack(P(th), P(pt), P(T), float(om1), float(om2))

    def restrict_state(self, x, cell):
        th, pt, T, om1, om2 = self.unpack(x)
        Rr = lambda F: self.restrict_field(F, cell).real
        return cell.pack(Rr(th), Rr(pt), Rr(T), om1, om2)


class HullJac:
    """The (J, r0) callable gn_sparse expects, analytic."""

    def __init__(self, H):
        self.H = H

    def __call__(self, x, pin_mode, aux, PW):
        return self.H.jacobian(x, pin_mode, aux, PW), self.H.wres(x, pin_mode, aux, PW)


def metrics(H, x):
    ws, zp, w, ze, gphi, gam, th, pt, T, om1, om2 = H.geom(x)
    _, c2 = H.modes(w)
    return dict(rms=float(H.field_rms(x)), A2=float(abs(c2)), om1=float(om1), om2=float(om2), gam=float(gam),
                minzp=float(zp.min()), minsin=float(np.sin(th).min()), clos=float(H.closure_max(x)))


def pin_residual(H, x, pin_mode, aux):
    """The largest unweighted pin residual (c1 - R1 re/im, the A2 or arc pin, c2.imag, <T> - 3/2)."""
    return float(np.abs(H.residual(x, pin_mode, aux)[-5:]).max())


def solve(H, x, pin_mode, aux, rounds=60, stop_rms=None, st=None, key=None, verbose=True, pin_tol=1e-8, chunk=5):
    """gn_sparse (the SPARSE-J ladder, verbatim) with the analytic hull Jacobian and the banded torus kernel,
    driven in chunks until the field RMS, the closure AND the pins are met. gn_sparse's own stop reads the field
    RMS and the closure only; at level 1 the field equations hold for any theta0 (the pin c1 = R1 is what fixes
    it) and the first small-grid runs stopped with the pin unmet (theta off by 3e-3). The pins are part of the
    acceptance here, as Q-SWEEP's gate() makes them for members."""
    from benchmarks.foundations import sparsej_instrument as SJ
    from benchmarks.foundations import qsweep_stage1 as Q1
    sj = HullJac(H)
    bs = SJ.BandedTorusSolver(H.NS, H.NP, nglob=2)
    if verbose:
        print(f"      [hull {H.NT1}x{H.NT2}x{H.NP} q {H.q:.4f}  n {H.n}  null modes {len(H.null)}]", flush=True)
    st = {} if st is None else st
    key = key or f'hull-solve-{id(x)}'
    bar = stop_rms or Q1.RMS_BAR
    done = 0
    while done < rounds:
        x = SJ.gn_sparse(H, x, pin_mode, aux, sj, bs, rounds=min(chunk, rounds - done), st=st, key=key, stop_rms=1e-300)
        done += chunk
        rms, clos, pr = H.field_rms(x), H.closure_max(x), pin_residual(H, x, pin_mode, aux)
        if verbose:
            print(f"      [hull chunk: rms {rms:.1e} clos {clos:.1e} pins {pr:.1e}]", flush=True)
        if rms < bar and clos < Q1.CLOSURE_BAR and pr < pin_tol:
            break
    return x
