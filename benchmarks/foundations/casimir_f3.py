"""COMMISSION CASIMIR-F3 (charter analysis/CASIMIR_F3_charter_LOCKED.md, locked 2026-09-27).

PART 1b -- the ledger's Casimir energy, known-answer instrument.
  The zero-point ledger (FND-109 convention: the half-sum of carried-mode frequencies,
  lattice-regulated, no imported cutoff) evaluated for a slab of the scalar nearest-
  neighbour cubic lattice with Dirichlet planes at z = 0 and z = d (sites 1..d-1 free),
  units a = 1, c = 1, hbar = 1 [hbar imported per GRV-014 at the conversion to joules,
  which this instrument never makes]. Per transverse wavevector k the slab's half-sum
  is compared with the exact bulk (elliptic-integral) and surface terms:

      E_cas(K, d) = 1/2 sum_{n=1}^{d-1} sqrt(K^2 + 4 sin^2(n pi / 2d))
                    - d * sqrt(K^2 + 4) E(4/(K^2 + 4)) / pi  +  (K + sqrt(K^2 + 4)) / 4,
      K^2 = 4 sin^2(kx/2) + 4 sin^2(ky/2),

  which is exponentially small in d K (the periodic-trapezoid identity), and the
  transverse integral over the Brillouin zone gives the plate energy per area. The
  continuum limit of this construction is -pi^2/(1440 d^3) per pinned polarization
  (two polarizations: -pi^2/(720 d^3)); the run measures how the lattice ledger
  approaches it. Bar B0: the extrapolated coefficient within 1 percent, the quadrature
  converged to 0.1 percent under doubling.

PART 1b display -- the wound slab's mode count: the SHIN6 engine (FND-089, derived
  angles, g = 2 shell calibration untouched) built as a slab with pinned planes, the
  lowest Dirichlet modes at k_perp = 0 listed against the straight slab's.

PART 2b -- the winding rotation under plates, one-dimensional control: a chain carrying
  a fixed-frequency travelling helical wave (the level-1 state's one-dimensional
  analogue: constant modulus, fixed frequency) has pins inserted at 0 and d; the
  energy of the pinned segment is computed exactly for d over three decades and two
  pitches, the extensive and boundary terms removed, the residual period-averaged and
  fitted for a power law (bar B2). A linearly polarized wave is displayed for contrast
  (it has the commensurability term a helix lacks). The SHIN6 wound slab's local bond
  sum versus d is displayed as the three-dimensional locality check.

Outputs are SEALED to analysis/casimir_f3_part1.npz and analysis/casimir_f3_part2.npz;
the verdict is read once by casimir_f3_verdict.py. No number in this file is a bar.
"""
import sys, pathlib, time
import numpy as np
from scipy.special import ellipe

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from benchmarks.foundations import shin6_3d_bloch as S6   # noqa: E402  (FND-089's engine, as registered)

OUT1 = ROOT / 'analysis' / 'casimir_f3_part1.npz'
OUT2 = ROOT / 'analysis' / 'casimir_f3_part2.npz'
CONT_SCALAR = np.pi ** 2 / 1440.0          # continuum, one Dirichlet polarization, hbar = c = 1


# ----------------------------------------------------------------------------------------------
# PART 1b: the lattice ledger's plate energy
# ----------------------------------------------------------------------------------------------
def ecas_per_k(K, d):
    """exponentially small plate energy per transverse mode: half-sum minus exact bulk and surface."""
    K = np.asarray(K, float)
    n = np.arange(1, d)
    half_sum = 0.5 * np.sqrt(K[..., None] ** 2 + 4.0 * np.sin(n * np.pi / (2.0 * d)) ** 2).sum(-1)
    bulk = d * np.sqrt(K ** 2 + 4.0) * ellipe(4.0 / (K ** 2 + 4.0)) / np.pi
    surf = 0.25 * (K + np.sqrt(K ** 2 + 4.0))
    return half_sum - bulk + surf


def plate_energy(d, n_r=400, n_phi=32):
    """E_cas(d) per unit area: polar quadrature over the inscribed disc |k| <= pi of the zone
    (the excluded corners carry exp(-2 d pi)-class weight), Gauss-Legendre in r, uniform in
    phi on the 8-fold wedge."""
    x, w = np.polynomial.legendre.leggauss(n_r)
    r = 0.5 * np.pi * (x + 1.0); wr = 0.5 * np.pi * w
    phi = (np.arange(n_phi) + 0.5) * (np.pi / 4.0) / n_phi           # wedge [0, pi/4]
    R, PHI = np.meshgrid(r, phi, indexing='ij')
    kx, ky = R * np.cos(PHI), R * np.sin(PHI)
    K = np.sqrt(4.0 * np.sin(kx / 2) ** 2 + 4.0 * np.sin(ky / 2) ** 2)
    E = ecas_per_k(K, d)
    inner = (E * R).sum(1) * (np.pi / 4.0) / n_phi                     # phi integral on the wedge
    return 8.0 * (inner * wr).sum() / (2.0 * np.pi) ** 2               # 8 wedges, (2 pi)^-2 measure


def fit_coefficient(ds, E):
    """E d^3 = C (1 + c2 / d^2): linear least squares in (1, 1/d^2)."""
    y = E * ds ** 3
    A = np.vstack([np.ones_like(ds), 1.0 / ds ** 2]).T
    (C, Cc2), *_ = np.linalg.lstsq(A, y, rcond=None)
    return C, Cc2 / C


def wound_slab_modes(d, f=1.0 / 5.0, n_low=6):
    """SHIN6 engine as a slab: sites (x, y, z), x, y periodic with the cell period P, z = 1..d-1
    free, planes z = 0 and z = d pinned (all components, the display's simplest pinning).
    Returns the lowest n_low frequencies at k_perp = 0 for the wound member and the straight
    control, both normalized by the straight medium's z-axis speed as SHIN6 does."""
    def build(wound):
        P = 1
        if wound:
            while P < 13 and abs(f * P - round(f * P)) > 1e-9:
                P += 1
        sites = [(x, y, z) for x in range(P) for y in range(P) for z in range(1, d)]
        idx = {s: i for i, s in enumerate(sites)}
        T = {}
        for x in range(P):
            for y in range(P):
                for z in range(0, d + 1):
                    T[(x, y, z)] = S6.tangent(x, y, z, f, wound)
        n = len(sites); D = np.zeros((3 * n, 3 * n))
        for s in sites:
            i = idx[s]
            for b in S6.NBRS:
                bh = np.array(b, float); r2 = bh @ bh; bh = bh / np.sqrt(r2)
                sj = ((s[0] + b[0]) % P, (s[1] + b[1]) % P, s[2] + b[2])
                shell = 1.0 if r2 == 1 else 2.0
                w = shell * (S6.KX + 0.5 * ((bh @ T[s]) ** 2 + (bh @ T[sj]) ** 2)) / r2
                blk = w * np.outer(bh, bh)
                D[3 * i:3 * i + 3, 3 * i:3 * i + 3] += blk
                if 1 <= sj[2] <= d - 1:                                # a pinned neighbour keeps the diagonal only
                    j = idx[sj]; D[3 * i:3 * i + 3, 3 * j:3 * j + 3] -= blk
        w2 = np.linalg.eigvalsh((D + D.T) / 2)
        return P, np.sqrt(np.clip(w2, 0, None))
    Ps, oms = build(False); Pw, omw = build(True)
    scale = S6.norm_scale(*S6.build_cell(f, False))
    return Ps, oms[:n_low] / scale, Pw, omw[:n_low * Pw * Pw] / scale


def part1():
    t0 = time.time()
    ds = np.array([8, 10, 12, 16, 20, 24, 32, 40, 48])
    E = np.array([plate_energy(int(d)) for d in ds])
    E2 = np.array([plate_energy(int(d), n_r=800, n_phi=64) for d in ds])   # quadrature doubled
    conv = np.abs(E2 / E - 1.0).max()
    C, c2 = fit_coefficient(ds.astype(float), E2)
    print("[f3 part1] lattice ledger, scalar Dirichlet slab, one polarization (hbar = c = a = 1)")
    for d, e, e2 in zip(ds, E, E2):
        print(f"   d {d:3d}  E_cas/A {e2:+.6e}   x d^3 {e2 * d ** 3:+.7f}   continuum {-CONT_SCALAR:+.7f}"
              f"   ratio {e2 * d ** 3 / -CONT_SCALAR:.5f}   quad-doubling {abs(e2 / e - 1):.1e}")
    print(f"   fit E d^3 = C (1 + c2/d^2): C = {C:+.7f}  (continuum {-CONT_SCALAR:+.7f}, "
          f"ratio {C / -CONT_SCALAR:.5f}, deviation {100 * (C / -CONT_SCALAR - 1):+.3f} pct), c2 = {c2:+.3f}")
    print(f"   max quadrature change under doubling: {100 * conv:.4f} pct")
    Ps, oms, Pw, omw = wound_slab_modes(12)
    print("[f3 part1] wound-slab display (SHIN6 engine, k_perp = 0, planes pinned, d = 12):")
    print(f"   straight P={Ps}: lowest modes / v_z  {np.array2string(oms, precision=4)}")
    print(f"   wound    P={Pw}: lowest modes / v_z  {np.array2string(omw[:12], precision=4)}  (cell has {Pw * Pw} sites per layer)")
    np.savez(OUT1, ds=ds, E=E, E2=E2, C=C, c2=c2, conv=conv, cont=CONT_SCALAR,
             straight_modes=oms, wound_modes=omw, Ps=Ps, Pw=Pw, elapsed=time.time() - t0)
    print(f"[f3 part1] sealed -> {OUT1.name}  ({time.time() - t0:.0f} s)")


# ----------------------------------------------------------------------------------------------
# PART 2b: the rotation under plates, one dimension, exact
# ----------------------------------------------------------------------------------------------
def pinned_segment_energy(d, k, R=1.0, circular=True, phase=0.0):
    """chain (unit mass, unit springs, transverse displacement in the plane) carrying the
    travelling wave u_j = R (cos(k j + phase - w t), sin(...)) [circular] or
    u_j = R (cos(k j + phase - w t), 0) [linear], w = 2 sin(k/2), the exact lattice
    dispersion. Pins inserted at 0 and d at t = 0: u_0 = u_d = 0, interior kept.
    Returns the exact energy of the pinned segment (conserved thereafter)."""
    w = 2.0 * np.sin(k / 2.0)
    j = np.arange(0, d + 1)
    th = k * j + phase
    if circular:
        u = R * np.stack([np.cos(th), np.sin(th)], 1); v = R * w * np.stack([np.sin(th), -np.cos(th)], 1)
    else:
        u = R * np.stack([np.cos(th), 0 * th], 1);      v = R * w * np.stack([np.sin(th), 0 * th], 1)
    u[0] = 0; u[d] = 0; v[0] = 0; v[d] = 0
    ke = 0.5 * (v[1:d] ** 2).sum()
    pe = 0.5 * ((u[1:] - u[:-1]) ** 2).sum()
    return ke + pe


def residual_series(k, circular, ds, R=1.0):
    """E(d) minus the extensive term (energy per site of the infinite wave, exact) minus the
    boundary constant (the residual's mean over one pitch at the largest d)."""
    w = 2.0 * np.sin(k / 2.0)
    e_site = 0.5 * R ** 2 * w ** 2 * (2.0 if circular else 1.0)            # KE + PE per site of the wave
    E = np.array([pinned_segment_energy(int(d), k, R, circular) for d in ds])
    r = E - e_site * ds
    period = 2.0 * np.pi / k
    n = max(int(round(period)), 2)
    win = np.arange(int(ds.max()) - n + 1, int(ds.max()) + 1)                     # exactly one period at the top
    r0 = np.mean([pinned_segment_energy(int(x), k, R, circular) - e_site * x for x in win])
    return E, r - r0, e_site, r0


def period_average(ds, k, circular, e_site, r0, period, R=1.0):
    """mean of the residual over one pitch period centred on each sampled d, computed on a
    DENSE integer window (shakedown 2026-09-27: on the log-spaced d grid a window held one
    point at large d and averaged nothing). The commensurability oscillation, if any,
    averages out; a secular term survives."""
    out = np.empty(len(ds))
    n = max(int(round(period)), 2)                      # one period of consecutive integer d
    for i, d in enumerate(ds):
        win = np.arange(int(d) - n // 2, int(d) - n // 2 + n)
        win = win[win >= 3]
        Ew = np.array([pinned_segment_energy(int(x), k, R, circular) for x in win])
        out[i] = (Ew - e_site * win - r0).mean()
    return out


def powerlaw_fit(ds, y):
    """|y| = A d^-p over the given range; returns (p, A) or (nan, nan) if y is at noise."""
    m = np.abs(y) > 1e-12
    if m.sum() < 4:
        return np.nan, np.nan
    (slope, icpt), *_ = np.linalg.lstsq(np.vstack([np.log(ds[m]), np.ones(m.sum())]).T, np.log(np.abs(y[m])), rcond=None)
    return -slope, np.exp(icpt)


def wound_slab_bond_sum(d, f=1.0 / 5.0):
    """the SHIN6 slab's local bond sum (the engine's pairwise weights over all bonds touching a
    free site, pinned planes included once): a local functional of the winding geometry, so
    extensive plus boundary by construction; displayed against d."""
    P = 5
    tot = 0.0
    for x in range(P):
        for y in range(P):
            for z in range(1, d):
                Ts = S6.tangent(x, y, z, f, True)
                for b in S6.NBRS:
                    bh = np.array(b, float); r2 = bh @ bh; bh = bh / np.sqrt(r2)
                    Tj = S6.tangent((x + b[0]) % P, (y + b[1]) % P, z + b[2], f, True)
                    shell = 1.0 if r2 == 1 else 2.0
                    tot += 0.5 * shell * (S6.KX + 0.5 * ((bh @ Ts) ** 2 + (bh @ Tj) ** 2)) / r2
    return tot


def part2():
    t0 = time.time()
    ds = np.unique(np.round(np.logspace(1, 3, 160)).astype(int))          # 10 .. 1000 sites
    out = {}
    print("[f3 part2] one-dimensional control: pinned segment of a fixed-frequency travelling wave")
    for label, k, circ in (('helix|pitch5', 2 * np.pi / 5, True), ('helix|pitch7', 2 * np.pi / 7, True),
                           ('helix|pitch_sqrt3x2', 2 * np.pi / (2 * np.sqrt(3)), True),
                           ('linear|pitch5', 2 * np.pi / 5, False)):
        E, r, e_site, r0 = residual_series(k, circ, ds)
        period = 2 * np.pi / k
        rbar = period_average(ds, k, circ, e_site, r0, period)
        top = ds >= 100
        p_raw, A_raw = powerlaw_fit(ds[top].astype(float), r[top])
        p_avg, A_avg = powerlaw_fit(ds[top].astype(float), rbar[top])
        print(f"   {label:22s} e/site {e_site:.6f}  boundary {r0:+.6f}  |residual| max {np.abs(r).max():.2e}  "
              f"period-avg |res| max {np.abs(rbar[top]).max():.2e}  fit raw p {p_raw:6.3f}  fit avg p {p_avg:6.3f}")
        out[label] = dict(k=k, circular=circ, E=E, r=r, rbar=rbar, e_site=e_site, r0=r0,
                          p_raw=p_raw, A_raw=A_raw, p_avg=p_avg, A_avg=A_avg)
    dd = np.array([6, 8, 10, 12, 16, 20, 24, 30, 40])
    bs = np.array([wound_slab_bond_sum(int(d)) for d in dd])
    (slope, icpt), *_ = np.linalg.lstsq(np.vstack([dd, np.ones_like(dd)]).T, bs, rcond=None)
    lin_res = bs - (slope * dd + icpt)
    print(f"[f3 part2] SHIN6 wound slab local bond sum vs d: slope {slope:.6f}/layer, intercept {icpt:+.6f}, "
          f"max |residual from linear| {np.abs(lin_res).max():.1e} (relative {np.abs(lin_res).max() / bs.max():.1e})")
    np.savez(OUT2, ds=ds, labels=np.array(list(out.keys())),
             **{f"{lab}|{key}": np.asarray(val) for lab, rec in out.items() for key, val in rec.items()},
             slab_d=dd, slab_bond_sum=bs, slab_slope=slope, slab_icpt=icpt, slab_lin_res=lin_res,
             elapsed=time.time() - t0)
    print(f"[f3 part2] sealed -> {OUT2.name}  ({time.time() - t0:.0f} s)")


if __name__ == '__main__':
    which = sys.argv[1] if len(sys.argv) > 1 else 'all'
    if which in ('part1', 'all'):
        part1()
    if which in ('part2', 'all'):
        part2()
