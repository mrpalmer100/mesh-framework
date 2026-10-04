"""SPARSE-J instrument (commission: analysis/SPARSEJ_charter_LOCKED.md,
locked 2026-08-29; spike: analysis/SPARSEJ_spike_results.md).

Replaces the dense-J / dense-normal-matrix kernel of the registered
gn_lean solver (qsweep_stage1.py) with an exact sparse-f64 route so
144x54+ full-bar gating fits the ~4 GB container class. Design
commitments D1-D5 of the charter:
  D1  the registered wres is called BYTE-IDENTICALLY (no physics here);
  D2  the Jacobian is assembled sparse by finite-difference graph
      coloring over the EMPIRICALLY MEASURED dependency pattern of
      wres on the marching chart (same h = 1e-8*(1+|x|) probes as
      TGrid96.jac);
  D3  full f64 end-to-end (the f32-J memory workaround is retired);
  D4  the linear solve is exact: METIS-ND-ordered no-pivot symmetric
      SuperLU on the SPARSE CORE of the damped normal matrix, with
      the dense rows (pins) and dense columns (globals) handled as a
      low-rank border by block elimination + Woodbury -- spike ledger
      faults 1-3 are the reason for every one of these choices;
  D5  acceptance ladder, trust cap, basin guard, lam persistence,
      stall escalation: carried over from gn_lean VERBATIM (diffs
      against gn_lean are annotated [SJ] at their sites).
"""
import sys, time, pathlib, pickle
import numpy as np
import tempfile as _tempfile


def _memo_dir():
    """platform memo directory: /tmp on Unix, %TEMP% on Windows (2026-09-13, for the Windows compute box)."""
    return pathlib.Path(_tempfile.gettempdir())

import scipy.sparse as sp
import scipy.sparse.linalg as spl

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
from benchmarks.foundations import qsweep_stage1 as Q          # noqa: E402

DENSE_COL = 200      # a column touching > this many rows is border
DENSE_ROW = 200      # a row touching > this many columns is border (pins)


def build_pattern(T, x, pin_mode, aux, PW, h_rel=1e-8, thresh=0.0):
    """EMPIRICAL dependency pattern of wres on the marching chart:
    one probe per column (a one-time, cached, per-grid cost -- ~16 s
    at 144x36). thresh=0: any bit-level residual change marks a
    dependency; no assumed stencil (spike fault 2 is why we measure
    the pattern rather than assume it)."""
    r0 = T.wres(x, pin_mode, aux, PW)
    m, n = r0.size, x.size
    rows, cols = [], []
    for jcol in range(n):
        h = h_rel * (1.0 + abs(x[jcol]))
        xp = x.copy(); xp[jcol] += h
        d = T.wres(xp, pin_mode, aux, PW) - r0
        nz = np.nonzero(np.abs(d) > thresh)[0]
        rows.append(nz); cols.append(np.full(nz.size, jcol))
    rows = np.concatenate(rows); cols = np.concatenate(cols)
    S = sp.csr_matrix((np.ones(rows.size, np.int8), (rows, cols)),
                      shape=(m, n))
    return S


def color_columns(S):
    """Greedy distance-2 coloring restricted to CORE columns (border
    columns are probed individually -- they are few and dense)."""
    Sc = S.tocsc()
    colnnz = np.diff(Sc.indptr)
    border = np.nonzero(colnnz > DENSE_COL)[0]
    core = np.setdiff1d(np.arange(S.shape[1]), border)
    # column conflict graph via row buckets
    ST = S.tocsr()
    color = -np.ones(S.shape[1], dtype=np.int64)
    row_colors = [set() for _ in range(S.shape[0])]
    for j in core:
        used = set()
        for r in Sc.indices[Sc.indptr[j]:Sc.indptr[j + 1]]:
            used |= row_colors[r]
        c = 0
        while c in used:
            c += 1
        color[j] = c
        for r in Sc.indices[Sc.indptr[j]:Sc.indptr[j + 1]]:
            row_colors[r].add(c)
    ncolors = int(color.max()) + 1
    return color, ncolors, core, border


class SparseJac:
    """Colored-FD sparse f64 Jacobian on the measured pattern."""

    def __init__(self, T, pattern, color, ncolors, core, border):
        self.T, self.S = T, pattern.tocsc()
        self.color, self.nc = color, ncolors
        self.core, self.border = core, border

    def __call__(self, x, pin_mode, aux, PW):
        # [SJ-OPT 2026-08-29] cross-process memo (C3 session): resumed
        # chunks replay identical (x -> J) evaluations; the memo returns
        # the stored bytes of the SAME deterministic computation. No
        # numerical path change.
        import hashlib
        # [SJ FAULT-11 corollary] memo key includes the pattern
        # identity: a J memoized under a superseded pattern must
        # not survive a pattern rebuild.
        hk = hashlib.sha1(x.tobytes() +
                          np.int64(self.S.nnz).tobytes()
                          ).hexdigest()[:16]
        mp = _memo_dir() / f'sjjac_{hk}.pkl'
        if mp.exists():
            J, r0 = pickle.loads(mp.read_bytes())
            return J, r0
        T, S = self.T, self.S
        r0 = T.wres(x, pin_mode, aux, PW)
        m, n = r0.size, x.size
        data = np.zeros(S.nnz)
        h = 1e-8 * (1.0 + np.abs(x))          # TGrid96.jac's probe, D2
        for c in range(self.nc):
            cols = np.nonzero(self.color == c)[0]
            xp = x.copy(); xp[cols] += h[cols]
            d = (T.wres(xp, pin_mode, aux, PW) - r0)
            for j in cols:
                sl = slice(S.indptr[j], S.indptr[j + 1])
                data[sl] = d[S.indices[sl]] / h[j]
        for j in self.border:                  # individual probes
            xp = x.copy(); xp[j] += h[j]
            d = (T.wres(xp, pin_mode, aux, PW) - r0)
            sl = slice(S.indptr[j], S.indptr[j + 1])
            data[sl] = d[S.indices[sl]] / h[j]
        J = sp.csc_matrix((data, S.indices.copy(), S.indptr.copy()),
                          shape=(m, n))
        J = J.tocsr()
        import os
        if os.environ.get('SJ_MEMO', '1') in ('1', 'jac'):
            try:
                mp.write_bytes(pickle.dumps((J, r0)))
            except Exception:
                pass
        return J, r0


class BorderedSolver:
    """Exact damped-normal-equation solve (charter D4).
    J is split by measured density: A (sparse field rows x core cols),
    dense rows P (pins) and dense cols B (globals). The damped normal
    matrix on the core is S0 + P_cT P_c (S0 sparse-factored once per
    (x, lam); P via Woodbury; border columns by Schur complement)."""

    def __init__(self, n, core, border, perm):
        self.core, self.border, self.perm = core, border, perm
        self.iperm = np.argsort(perm)

    def solve(self, J, r0, lam, d2):
        core, border = self.core, self.border
        rownnz = np.diff(J.indptr)
        drows = np.nonzero(rownnz > DENSE_ROW)[0]
        srows = np.setdiff1d(np.arange(J.shape[0]), drows)
        A = J[srows][:, core]
        P = np.asarray(J[drows][:, core].todense())        # k x nc
        Bfull = np.asarray(J[:, border].todense())          # m x nb
        g = J.T @ r0                                        # f64 exact
        gc, gb = g[core], g[border]
        S0 = (A.T @ A).tocsc()
        S0 = S0 + sp.diags(lam * d2[core], format='csc')
        Sp = S0[self.perm][:, self.perm].tocsc()
        lu = spl.splu(Sp, permc_spec='NATURAL', diag_pivot_thresh=0.0,
                      options=dict(SymmetricMode=True))

        def s0_solve(v):
            if v.ndim == 1:
                return lu.solve(v[self.perm])[self.iperm]
            return np.stack([lu.solve(v[self.perm, i])[self.iperm]
                             for i in range(v.shape[1])], axis=1)

        # Woodbury: (S0 + P^T P)^{-1} = S0inv - S0inv P^T (I + P S0inv P^T)^-1 P S0inv
        k = P.shape[0]
        if k:
            Y = s0_solve(P.T)                               # nc x k
            Kmat = np.eye(k) + P @ Y

            def n_solve(v):
                u = s0_solve(v)
                return u - Y @ np.linalg.solve(Kmat, P @ u)
        else:
            n_solve = s0_solve
        # Schur on the border columns
        Bc = (A.T @ Bfull[srows]) + P.T @ Bfull[drows]      # nc x nb
        Dbb = Bfull.T @ Bfull + np.diag(lam * d2[border])
        Z = n_solve(Bc)                                     # nc x nb
        Schur = Dbb - Bc.T @ Z
        u = n_solve(-gc)
        dxb = np.linalg.solve(Schur, -gb - Bc.T @ u)
        dxc = u - Z @ dxb
        dx = np.empty(J.shape[1])
        dx[core], dx[border] = dxc, dxb
        return dx


def make_instrument(T, x0, pin_mode, aux, PW, cache=None):
    """Build (or load) pattern+coloring+ordering for T's grid.
    [SJ FAULT-9 2026-08-29, C3 session] the cache key now includes
    pin_mode: the C1/C2 pattern was reused for the arc chart, whose
    arc row (dense in ALL columns) it did not contain -- measured as
    O(1) missing entries in row m-3 at the C3 stall point. Fault 4's
    lesson applies to the pin mode too: measure the pattern of the
    residual you will actually solve.
    [SJ FAULT-10 2026-08-29, S3R session -- LATENT, caught before
    firing] the key also lacked the CELL (n2): the S3R 4/3 members
    would have silently reused the 144x54:a2 pattern measured on the
    5/3 operator. Same lesson, third axis: grid AND pin mode AND
    cell. Old-format keys remain readable for their original
    (grid, pin_mode, cell) combinations only.
    [SJ FAULT-11 2026-08-30, Q54 session] the pattern must be
    measured at a NON-DEGENERATE state of the chart: the Q54
    pattern was built at the level-1 state (A2 ~ 0), where every
    dependency proportional to the level-2 amplitude is genuinely
    zero -- and therefore MISSING for any injected state (O(1e-2)
    entries, 80 field rows in the probe; hard no-step stall at
    rung 1). Corollary: a C1a column check at a degenerate state
    passes bit-exact and certifies NOTHING beyond that point.
    Callers must pass an x0 generic for the chart (A2 != 0 for
    a2 ramps); the Q54 pattern was re-measured at the injected
    rung state."""
    n2 = getattr(getattr(T, 'G2', None), 'N2', None)
    key = f'{T.NS}x{T.NP}:{pin_mode}' + \
          (f':n2={n2}' if n2 is not None else '')
    if cache and pathlib.Path(cache).exists():
        d = pickle.load(open(cache, 'rb'))
        if key in d:
            e = d[key]
            return (SparseJac(T, e['S'], e['color'], e['nc'],
                              e['core'], e['border']),
                    BorderedSolver(x0.size, e['core'], e['border'],
                                   e['perm']))
    S = build_pattern(T, x0, pin_mode, aux, PW)
    color, nc, core, border = color_columns(S)
    # [SJ-OPT 2026-08-29] the METIS ND ordering served only the
    # SUPERSEDED BorderedSolver (fault 6); the BandedTorusSolver
    # carries its own phi-major permutation. Identity kept for the
    # cache-format contract.
    perm = np.arange(len(core))
    if cache:
        d = pickle.load(open(cache, 'rb')) if pathlib.Path(cache).exists() else {}
        d[key] = dict(S=S, color=color, nc=nc, core=core, border=border,
                      perm=perm)
        pickle.dump(d, open(cache, 'wb'))
    return (SparseJac(T, S, color, nc, core, border),
            BorderedSolver(x0.size, core, border, perm))


def gn_sparse(T, x, pin_mode, aux, sj, bs, rounds=60, PW=50.0,
              st=None, key=None, stop_rms=None, project=None):
    """gn_lean VERBATIM (qsweep_stage1.gn_lean) with the linear
    kernel swapped per the charter. [SJ]-annotated diffs ONLY:
      [SJ-1] J via colored sparse FD (f64) instead of dense f32.
      [SJ-2] the normal step via BorderedSolver instead of dense
             dsyrk + cho_factor; ALWAYS the f64 exact single-attempt
             branch (the f32 multi-retry band existed only as the
             memory diet this instrument retires, per its own
             docstring; the n > 12000 route of the registered solver
             is the branch carried).
      [SJ-3] the lsmr escalation/fallback uses the SAME sparse f64 J
             (a precision upgrade on an identical operator).
    Acceptance ladder, fractions, trust cap 0.05, basin guard, lam
    schedule, stall trigger, persistence: unchanged.
    [SJ AMENDMENT 2026-10-04, ANTI-ARC-NYQ] project: optional callable
    applied to every candidate step (the normal step AND the lsmr
    fallback) before the acceptance ladder; None (the default) is the
    credentialed solver byte-for-byte in behaviour. Used only by arm A2
    of ANTI-ARC-NYQ with kernel_continuation.dealias_s."""

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
        lam = st[key].get('lam', 1e-4)
        print(f"      [sj resume from saved round {st[key]['it']}  "
              f"lam {lam:.0e}]", flush=True)
    hist = (st[key].get('hist', []) if st is not None and key is not None
            and key in st else [])
    esc = (st[key].get('esc', 0) if st is not None and key is not None
           and key in st else 0)
    fx = wn(x)
    for it in range(rounds):
        rms_now = T.field_rms(x)
        stalled = len(hist) >= 3 and fx > 0.75 * hist[-3]
        if stalled and esc % 2 == 1:
            esc += 1
            J2, r2 = sj(x, pin_mode, aux, PW)               # [SJ-3]
            dxl = spl.lsmr(J2, -r2, atol=1e-11, btol=1e-11,
                           maxiter=1500)[0]
            if project is not None:
                dxl = project(dxl)                          # [SJ 2026-10-04] ANTI-ARC-NYQ A2 only
            acc = False
            for a_ in (1.0, 0.5, 0.25, 0.1):
                xt = x + a_ * dxl
                f2 = wn(xt)
                if f2 < fx and guard_ok(xt):
                    x, fx, acc = xt, f2, True
                    break
            hist = []
            r = T.field_rms(x)
            print(f"      [sj {it} (gnd-esc): RMS {r:.1e}  wres "
                  f"{fx:.2e}{'' if acc else '  no step'}]", flush=True)
            if st is not None and key is not None:
                st[key] = dict(x=x, it=it, lam=lam, hist=hist, esc=esc)
            if r < (stop_rms or Q.RMS_BAR):
                # [SJ FAULT-8 2026-08-29, C3 session] the stop broke
                # on RMS alone; gn_lean's stop (2026-08-23 annotation)
                # is CLOSURE-AWARE for gate-facing solves. Restored.
                if stop_rms is None:
                    if T.closure_max(x) < Q.CLOSURE_BAR:
                        break
                elif pin_mode != 'a2' or aux <= 1e-5:
                    break
                else:
                    _, c2n = T.modes(T.geom(x)[2])
                    if abs(abs(c2n) - aux) / aux < 0.05:
                        break
            continue
        if stalled:
            esc += 1
            hist = []
            lam = 1e-9
        J, r0 = sj(x, pin_mode, aux, PW)                    # [SJ-1]
        d2 = np.maximum(np.asarray(J.power(2).sum(axis=0)).ravel(),
                        1e-12)
        acc = False
        fx0 = fx
        try:                                                # [SJ-2]
            bs.factor(J, lam, d2)
            dx = bs.solve(J.T @ r0)
            _nd = float(np.linalg.norm(dx))
            # [SJ AMENDMENT 2026-09-07, COMPOSITE-SELECT Leg B] the trust
            # cap 0.05 was credentialed on the 144 x 36 chart as a bound on
            # the WHOLE step vector; on larger charts the same bound means
            # proportionally smaller moves per point (7/5 at 240 x 36: 5-8
            # pct per round vs 50-90). The cap is made scale-invariant by
            # keeping the per-point step identical to the credentialed one:
            # cap = 0.05 * sqrt(n / n_144x36). Unchanged on 144 x 36.
            _cap = 0.05 * np.sqrt(len(dx) / (2 * 144 * 36 + 2))
            if _nd > _cap:
                dx = dx * (_cap / _nd)
            if project is not None:
                dx = project(dx)                            # [SJ 2026-10-04] ANTI-ARC-NYQ A2 only
            for a_ in (1.0, 0.5, 0.25, 0.1, 0.03):
                xt = x + a_ * dx
                f2 = wn(xt)
                if f2 < fx and guard_ok(xt):
                    x, fx, acc = xt, f2, True
                    print(f"        [step: frac {a_}  |dx| "
                          f"{np.linalg.norm(dx):.2e}  df "
                          f"{1 - f2 / fx0:.2%}]", flush=True)
                    break
        except Exception as e:
            print(f"        [sj solve fault: {e}]", flush=True)
        lam = max(lam / 3.0, 1e-9) if acc else lam * 10.0
        if not acc:
            dxl = spl.lsmr(J, -r0, atol=1e-11, btol=1e-11,
                           maxiter=1500)[0]                 # [SJ-3]
            if project is not None:
                dxl = project(dxl)                          # [SJ 2026-10-04] ANTI-ARC-NYQ A2 only
            for a_ in (1.0, 0.5, 0.25, 0.1):
                xt = x + a_ * dxl
                f2 = wn(xt)
                if f2 < fx and guard_ok(xt):
                    x, fx, acc = xt, f2, True
                    break
            if acc:
                print("      [alt: lsmr step accepted]", flush=True)
        # [SJ FAULT-7 2026-08-29, C3 session] hist was appended
        # unconditionally and uncapped -- gn_lean appends ONLY on
        # accepted rounds, capped at 4. The defect made the stall
        # trigger fire on every no-step and the gnx branch re-floor
        # lam perpetually. Restored to gn_lean-verbatim.
        if acc:
            hist = (hist + [fx])[-4:]
        r = T.field_rms(x)
        print(f"      [sj {it}: RMS {r:.1e}  wres {fx:.2e}  lam "
              f"{lam:.0e}{'' if acc else '  no step'}]", flush=True)
        if st is not None and key is not None:
            st[key] = dict(x=x, it=it, lam=lam, hist=hist, esc=esc)
        if r < (stop_rms or Q.RMS_BAR):
            # [SJ FAULT-8] closure-aware stop, as above.
            if stop_rms is None:
                if T.closure_max(x) < Q.CLOSURE_BAR:
                    break
            elif pin_mode != 'a2' or aux <= 1e-5:
                break
            else:
                _, c2n = T.modes(T.geom(x)[2])
                if abs(abs(c2n) - aux) / aux < 0.05:
                    break
    return x


# ---------------------------------------------------------------------------
# BANDED TORUS SOLVER (checkpoint 2026-08-29, ledger faults 4-6; the
# corrected exact-solve of charter D4). The generic-sparse route is
# SUPERSEDED: on the marching chart the s-direction is spectral, so
# N = J^T J has ~150M nnz and must never be formed globally (fault 6,
# measured OOM at 3.79 GB). Here N is assembled slice-pair by
# slice-pair into phi-major banded storage; the phi wrap and the two
# global columns form a dense BORDER (last BSL slices + globals); the
# truly dense rows (pins/closure/norm) enter by WOODBURY. Exact f64
# throughout; Marquardt damping lam*d2 on the diagonal at assembly.
# ---------------------------------------------------------------------------
import scipy.linalg as _sla


class BandedTorusSolver:
    BSL = 4          # border slices (>= N-graph phi halfwidth)
    PHW = 4          # N-graph phi halfwidth (J phi +-2, doubled)

    def __init__(self, NS, NP, nglob=2):
        self.NS, self.NP, self.nglob = NS, NP, nglob
        S = 3 * NS
        self.S = S
        n = 3 * NS * NP + nglob
        # phi-major permutation: slice p holds (f, s); globals last
        perm = np.empty(n, dtype=np.int64)
        k = 0
        for p in range(NP):
            for f in range(3):
                base = f * NS * NP
                for s in range(NS):
                    perm[k] = base + s * NP + p
                    k += 1
        perm[k:] = np.arange(3 * NS * NP, n)
        self.perm = perm
        self.iperm = np.argsort(perm)
        self.ncore = S * (NP - self.BSL)
        self.nbord = S * self.BSL + nglob

    def _classify_rows(self, J):
        NP, S = self.NP, self.S
        m = J.shape[0]
        banded_rows, dense_rows = [], []
        for r in range(m):
            cols = J.indices[J.indptr[r]:J.indptr[r + 1]]
            fld = cols[cols < 3 * self.NS * NP]
            if fld.size == 0:
                dense_rows.append(r)
                continue
            ps = np.unique(fld % NP)
            # contiguous mod NP within J's phi halfwidth (2)?
            if ps.size <= 5:
                span = (ps.max() - ps.min())
                wrap = (NP - ps.max() + ps.min())
                if min(span, wrap) <= 4:
                    banded_rows.append(r)
                    continue
            dense_rows.append(r)
        return np.array(banded_rows), np.array(dense_rows)

    def factor(self, J, lam, d2):
        # [SJ-OPT 2026-08-29] cross-process memo, same rationale as the
        # SparseJac memo: resumed chunks replay identical (J, lam)
        # factors; stored arrays are the bytes of the same computation.
        import hashlib
        hk = hashlib.sha1(J.data.tobytes() + np.float64(lam).tobytes()
                          ).hexdigest()[:16]
        self._mp = _memo_dir() / f'sjfac_{hk}.pkl'
        d = pathlib.Path(str(self._mp) + '.d')
        if (d / 'ok').exists():
            self.cb = np.load(d / 'cb.npy')
            self.Y = np.load(d / 'Y.npy')
            self.Ncb = np.load(d / 'Ncb.npy')
            self.P = np.load(d / 'P.npy')
            if (d / 'Zw.npy').exists():
                self.Zw = np.load(d / 'Zw.npy')
                self.Kw = np.load(d / 'Kw.npy')
            else:
                self.Zw = None
                self.Kw = None
            self.Slu = pickle.loads((d / 'slu.pkl').read_bytes())
            return
        if self._mp.exists():
            (self.cb, self.Y, self.Ncb, self.Slu, self.P,
             self.Zw, self.Kw) = pickle.loads(self._mp.read_bytes())
            return
        NS, NP, S = self.NS, self.NP, self.S
        perm, ncore, nbord = self.perm, self.ncore, self.nbord
        brows, drows = self._classify_rows(J)
        Jb = J[brows].tocsc()[:, perm].tocsc()
        self.P = np.asarray(J[drows].tocsc()[:, perm].todense())  # k x n
        d2p = d2[perm]
        # slice column blocks
        cols = [Jb[:, i * S:(i + 1) * S] for i in range(NP)]
        gcols = Jb[:, S * NP:]
        bw = self.PHW * S + (S - 1)
        ab = np.zeros((bw + 1, ncore))                 # lower banded
        Ncb = np.zeros((ncore, nbord))
        Nbb = np.zeros((nbord, nbord))
        ncs = NP - self.BSL                            # core slices

        def blk(i, j):
            return np.asarray((cols[i].T @ cols[j]).todense())

        # [SJ-OPT 2026-08-29] band-scatter vectorized (C3 session).
        # The per-element Python triple loop here was the annotated
        # optimization candidate from the C2 run (61-93 s/factor,
        # machine-dependent); it is replaced by precomputed fancy-index
        # scatter per slice-offset. Identical assignments (each (ii,jj)
        # written once); verified bit-identical against the loop on a
        # 48x12 factor before first credential use. No logic change.
        aa, bb = np.meshgrid(np.arange(S), np.arange(S), indexing='ij')
        self._sc = {}
        for di in range(self.PHW + 1):
            ii = aa + di * S
            jj = bb
            msk = (ii >= jj) & (ii - jj <= bw)
            self._sc[di] = (msk, (ii - jj)[msk])

        def scatter(i, j, B):
            msk, doff = self._sc[i - j]
            ab[doff, j * S + bb[msk]] = B[msk]

        for i in range(ncs):
            for j in range(max(0, i - self.PHW), i + 1):
                B = blk(i, j)
                if i == j:
                    B = B + np.diag(lam * d2p[i * S:(i + 1) * S])
                scatter(i, j, B)
        # core-border and border-border
        bslices = list(range(ncs, NP))
        for i in range(ncs):
            for bj, j in enumerate(bslices):
                dp = min(abs(i - j), NP - abs(i - j))
                if dp <= self.PHW:
                    Ncb[i * S:(i + 1) * S, bj * S:(bj + 1) * S] = blk(i, j)
            Ncb[i * S:(i + 1) * S, S * self.BSL:] = np.asarray(
                (cols[i].T @ gcols).todense())
        for bi, i in enumerate(bslices):
            for bj, j in enumerate(bslices):
                dp = min(abs(i - j), NP - abs(i - j))
                if dp <= self.PHW:
                    B = blk(i, j)
                    if i == j:
                        B = B + np.diag(lam * d2p[i * S:(i + 1) * S])
                    Nbb[bi * S:(bi + 1) * S, bj * S:(bj + 1) * S] = B
            Nbb[bi * S:(bi + 1) * S, S * self.BSL:] = np.asarray(
                (cols[i].T @ gcols).todense())
            Nbb[S * self.BSL:, bi * S:(bi + 1) * S] = \
                Nbb[bi * S:(bi + 1) * S, S * self.BSL:].T
        Nbb[S * self.BSL:, S * self.BSL:] = np.asarray(
            (gcols.T @ gcols).todense()) + np.diag(lam * d2p[S * NP:])
        # factor core; Schur on border
        self.cb = _sla.cholesky_banded(ab, lower=True, check_finite=False)
        Y = _sla.cho_solve_banded((self.cb, True), Ncb,
                                  check_finite=False)   # ncore x nbord
        self.Y = Y
        self.Ncb = Ncb
        Schur = Nbb - Ncb.T @ Y
        self.Slu = _sla.lu_factor(Schur, check_finite=False)
        # Woodbury for dense rows: A = B + P^T P
        k = self.P.shape[0]
        if k:
            Z = self._bsolve(self.P.T)                  # n x k
            self.Zw = Z
            self.Kw = np.eye(k) + self.P @ Z
        else:
            self.Zw = None
            self.Kw = None
        import os
        if os.environ.get('SJ_MEMO', '1') == '1':
            # [SJ-OPT 2026-08-29b] streamed memo: pickle.dumps of the
            # whole factor doubled ~1 GB transiently at 144x54 and was
            # OOM-reaped. np.save writes each array from its own
            # buffer (no aggregate copy); small members stay pickled.
            try:
                d = pathlib.Path(str(self._mp) + '.d')
                d.mkdir(exist_ok=True)
                np.save(d / 'cb.npy', self.cb)
                np.save(d / 'Y.npy', self.Y)
                np.save(d / 'Ncb.npy', self.Ncb)
                np.save(d / 'P.npy', self.P)
                if self.Zw is not None:
                    np.save(d / 'Zw.npy', self.Zw)
                    np.save(d / 'Kw.npy', self.Kw)
                (d / 'slu.pkl').write_bytes(pickle.dumps(self.Slu))
                (d / 'ok').touch()
            except Exception:
                pass

    def _bsolve(self, b):
        one = (b.ndim == 1)
        if one:
            b = b[:, None]
        bc, bb = b[:self.ncore], b[self.ncore:]
        u = _sla.cho_solve_banded((self.cb, True), bc, check_finite=False)
        xb = _sla.lu_solve(self.Slu, bb - self.Ncb.T @ u,
                           check_finite=False)
        xc = u - self.Y @ xb
        out = np.vstack([xc, xb])
        return out[:, 0] if one else out

    def solve(self, g):
        """Solve (J^T J + lam diag(d2)) dx = -g   (g = J^T r0)."""
        b = -g[self.perm]
        z = self._bsolve(b)
        if self.Zw is not None:
            z = z - self.Zw @ np.linalg.solve(self.Kw, self.P @ z)
        return z[self.iperm]
