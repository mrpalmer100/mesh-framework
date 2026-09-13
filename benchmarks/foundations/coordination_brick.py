"""COORDINATION BRICK -- the Topology Commission's second brick.

Charter: analysis/TOPOLOGY_coordination_charter_LOCKED.md (bars
locked 2026-08-24; released by the author 2026-08-26). Shared
parameters throughout: spring stiffness k, pretension via rest
length r0 < a (tension T0 = k*(a - r0) on lattice bonds), node mass
m (mu). NO population- or z-dependent renormalization (no-rescue).

This file implements the network instrument and the tests in charter
order of economy: C3 (static fidelity) first, then C2 (source
fidelity), C4 (impedance), C6 (pendant defect), C1 (percolation),
C5 (isotropy map). Checkpoint: /tmp/coord_ckpt.pkl.

INSTRUMENT NOTES (annotated as lessons accrue):
- Cubic lattice, N = L^3 nodes, z = 6 bulk baseline (the corpus's
  own stencil coordination). Lower z by random bond dilution;
  z = 1 pendant by attaching a single extra node to a bulk node.
- Pretension: isotropic tension field T0 on every bond. For the
  STATIC scalar test the transverse displacement field u on a
  pretensioned network obeys, at harmonic order, the discrete
  Laplace equation sum_j T0/a * (u_j - u_i) = -f_i: the weave's
  psi equation. C3 asks whether the MEASURED response follows the
  3D Green function 1/(4 pi r) (potential) hence 1/r^2 (force),
  and how that degrades with z.
"""
import numpy as np
import pickle
import pathlib
import scipy.sparse as sp
import scipy.sparse.linalg as sla

CKPT = pathlib.Path('/tmp/coord_ckpt.pkl')


def save(st):
    _atomic_write(CKPT, pickle.dumps(st))


def load():
    if CKPT.exists():
        return pickle.loads(CKPT.read_bytes())
    return {}


def cubic_network(L, dilute_to_z=None, seed=0, pendant=False):
    """Cubic lattice, optionally diluted to a target mean z; the
    dilution keeps the graph connected (spanning-tree protected).
    Returns positions (n,3), bonds (m,2), and the pendant index
    (or -1)."""
    rng = np.random.default_rng(seed)
    idx = np.arange(L ** 3).reshape(L, L, L)
    pos = np.stack(np.meshgrid(np.arange(L), np.arange(L),
                               np.arange(L), indexing='ij'),
                   axis=-1).reshape(-1, 3).astype(np.float64)
    bonds = []
    for ax in range(3):
        a = idx
        b = np.roll(idx, -1, axis=ax)
        sl = [slice(None)] * 3
        sl[ax] = slice(0, L - 1)   # open boundaries (no wrap)
        bonds.append(np.stack([a[tuple(sl)].ravel(),
                               b[tuple(sl)].ravel()], axis=1))
    bonds = np.concatenate(bonds, axis=0)
    if dilute_to_z is not None and dilute_to_z < 6:
        # protect a random spanning tree, dilute the rest
        m = len(bonds)
        order = rng.permutation(m)
        parent = np.arange(L ** 3)

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        keep = np.zeros(m, dtype=bool)
        extra = []
        for bi in order:
            i, j = bonds[bi]
            ri, rj = find(i), find(j)
            if ri != rj:
                parent[ri] = rj
                keep[bi] = True
            else:
                extra.append(bi)
        target_m = int(dilute_to_z * L ** 3 / 2)
        need = max(0, target_m - keep.sum())
        for bi in extra[:need]:
            keep[bi] = True
        bonds = bonds[keep]
    pend = -1
    if pendant:
        c = int(idx[L // 2, L // 2, L // 2])
        pos = np.vstack([pos, pos[c] + np.array([0.37, 0.41, 0.53])])
        bonds = np.vstack([bonds, [c, len(pos) - 1]])
        pend = len(pos) - 1
    return pos, bonds, pend


def graph_laplacian(n, bonds, w=1.0):
    i, j = bonds[:, 0], bonds[:, 1]
    data = np.full(len(bonds), w)
    A = sp.coo_matrix((np.concatenate([data, data]),
                       (np.concatenate([i, j]),
                        np.concatenate([j, i]))), shape=(n, n)).tocsr()
    d = np.asarray(A.sum(axis=1)).ravel()
    return sp.diags(d) - A


def c3_static(L=41, z=6, seed=0, source='center', tag=None):
    """C3: unit transverse load at the source, grounded far
    boundary; measure u(r) and fit the potential exponent on
    r in [4, L/3] (a decade-ish for L = 41). BAR (locked): EMBEDDED
    requires force-law 1/r^2, i.e. potential 1/r within 5 percent
    over the fit range."""
    st = load()
    key = tag or f'c3-z{z}-L{L}-s{seed}'
    if key in st:
        return st[key]
    pos, bonds, pend = cubic_network(
        L, None if z >= 6 else z, seed, pendant=(source == 'pendant'))
    n = len(pos)
    Lap = graph_laplacian(n, bonds, w=1.0)   # T0/a = 1 shared unit
    ctr = (np.array([L // 2] * 3, dtype=float) if source != 'pendant'
           else pos[pend])
    src = (pend if source == 'pendant'
           else int(np.argmin(((pos - ctr) ** 2).sum(1))))
    # ground the outer shell (Dirichlet), load the source
    r = np.sqrt(((pos - pos[src]) ** 2).sum(1))
    shell = r >= (L // 2 - 1)
    free = ~shell
    fidx = np.where(free)[0]
    f = np.zeros(n)
    f[src] = 1.0
    Lf = Lap[fidx][:, fidx]
    u = np.zeros(n)
    ui, info = sla.cg(Lf, f[fidx], rtol=1e-10, maxiter=4000)
    u[fidx] = ui
    # fit u ~ C r^-p on the annulus (exclude near field & boundary)
    lo, hi = 4.0, (L // 2) * 0.66
    ann = (r >= lo) & (r <= hi) & free & (np.arange(n) != src)
    # radial bin medians to suppress lattice anisotropy in the fit
    rb = np.round(r[ann]).astype(int)
    med_r, med_u = [], []
    for rv in np.unique(rb):
        med_r.append(rv)
        med_u.append(np.median(u[ann][rb == rv]))
    med_r, med_u = np.array(med_r, float), np.array(med_u)
    ok = med_u > 0
    # INSTRUMENT AMENDMENT (2026-08-26, daylight, measured): with a
    # grounded shell at R the exact solution is C*(1/r - 1/R): an
    # image CONSTANT rides on the 1/r law, and a bare log-log fit
    # of that mixture reported p ~ 1.68 on the PRISTINE z=6 lattice
    # whose Green function is provably ~ 1/(4 pi r). The honest fit
    # is u = C/r + B (B absorbs the image); the exponent is then
    # measured on (u - B). Standard electrostatics, not a rescue:
    # the correction is z-independent and applied identically to
    # every network.
    X = 1.0 / med_r[ok]
    A2 = np.vstack([X, np.ones_like(X)]).T
    (C, B), *_ = np.linalg.lstsq(A2, med_u[ok], rcond=None)
    uc = med_u[ok] - B
    ok2 = uc > 0
    P = np.polyfit(np.log(med_r[ok][ok2]), np.log(uc[ok2]), 1)
    p_exp = -P[0]
    res = dict(z=z, L=L, n=n, cg=info, p=float(p_exp),
               C=float(C), B=float(B),
               bins=[[float(a), float(b)] for a, b in
                     zip(med_r[ok], med_u[ok])],
               u_src=float(u[src]))
    st[key] = res
    save(st)
    return res


def c2_dynamic(L=49, z=6, seed=0, source='center', tag=None,
               omega=0.5236, steps=520, dt=0.18):
    """C2: sinusoidally driven source; measure (a) the steady
    far-field amplitude decay exponent p_dyn on the annulus and
    (b) the wavefront speed from first-arrival times. BAR (locked):
    EMBEDDED requires p_dyn = 1 within 5 percent (3D spreading);
    the medium speed on this lattice/units is c = 1 (dispersion
    omega^2 = 2 sum(1-cos k)).
    Instrument: unit mass, unit bond weight -> u'' = -Lap u + f;
    leapfrog; absorbing sponge (Rayleigh damping ramp) on the outer
    5 layers so reflections do not pollute the envelope; envelope
    from max|u| over the final 1.5 drive periods; arrival = first
    crossing of 1e-3 * drive amplitude."""
    st = load()
    key = tag or f'c2-z{z}-L{L}-s{seed}'
    if key in st:
        return st[key]
    pos, bonds, pend = cubic_network(
        L, None if z >= 6 else z, seed, pendant=(source == 'pendant'))
    n = len(pos)
    Lap = graph_laplacian(n, bonds, w=1.0).tocsr()
    ctr = (np.array([L // 2] * 3, dtype=float) if source != 'pendant'
           else pos[pend])
    src = (pend if source == 'pendant'
           else int(np.argmin(((pos - ctr) ** 2).sum(1))))
    r = np.sqrt(((pos - pos[src]) ** 2).sum(1))
    R = L // 2
    sponge = np.clip((r - (R - 5.0)) / 5.0, 0.0, 1.0) ** 2 * 0.9
    u = np.zeros(n)
    v = np.zeros(n)
    arr = np.full(n, -1.0)
    per = 2 * np.pi / omega
    # INSTRUMENT AMENDMENT (2026-08-26, daylight): Fourier-project
    # u(t) onto sin/cos(omega t) over the final 2 full periods --
    # the steady-state amplitude, immune to transients and
    # dispersion ripple that biased the max-envelope +10 percent on
    # the pristine calibration lattice. z-independent, applied
    # identically everywhere (no rescue).
    t_env0 = steps * dt - 2.0 * per
    cs = np.zeros(n)
    sn = np.zeros(n)
    nsamp = 0
    for k in range(steps):
        t = k * dt
        a = -Lap.dot(u) - sponge * v
        a[src] += np.sin(omega * t)
        v += dt * a
        u += dt * v
        newly = (arr < 0) & (np.abs(u) > 1e-3)
        arr[newly] = t
        if t >= t_env0:
            cs += u * np.cos(omega * t)
            sn += u * np.sin(omega * t)
            nsamp += 1
    env = 2.0 * np.sqrt(cs ** 2 + sn ** 2) / max(nsamp, 1)
    lo, hi = 6.0, R - 7.0
    ann = (r >= lo) & (r <= hi) & (np.arange(n) != src)
    rb = np.round(r[ann]).astype(int)
    med_r, med_e = [], []
    for rv in np.unique(rb):
        med_r.append(rv)
        med_e.append(np.median(env[ann][rb == rv]))
    med_r = np.array(med_r, float)
    med_e = np.array(med_e)
    ok = med_e > 0
    P = np.polyfit(np.log(med_r[ok]), np.log(med_e[ok]), 1)
    p_dyn = -P[0]
    # front speed: robust slope of r vs arrival over the annulus
    fa = ann & (arr > 0)
    S = np.polyfit(arr[fa], r[fa], 1)
    res = dict(z=z, L=L, n=n, p_dyn=float(p_dyn), c=float(S[0]),
               bins=[[float(a_), float(b_)] for a_, b_ in
                     zip(med_r[ok], med_e[ok])])
    st[key] = res
    save(st)
    return res


def c4_impedance(L=41, z=6, seed=0, probe='center', tag=None,
                 omega=0.5236, steps=560, dt=0.18):
    """C4: drive the probe node with force sin(omega t); the
    steady-state complex mobility Y = v_probe / F at the drive
    frequency gives the local impedance Z = 1/|Y|. BAR (locked):
    the EMBEDDED value within 10 percent of the bulk z = 6 medium
    value (measured on the pristine lattice, same instrument); the
    PENDANT pre-registered position: single-bond endpoint impedance,
    far from the bulk value, velocity response dominated by the
    one-rope channel."""
    st = load()
    key = tag or f'c4-z{z}-{probe}-L{L}-s{seed}'
    if key in st:
        return st[key]
    pos, bonds, pend = cubic_network(
        L, None if z >= 6 else z, seed, pendant=(probe == 'pendant'))
    n = len(pos)
    Lap = graph_laplacian(n, bonds, w=1.0).tocsr()
    ctr = np.array([L // 2] * 3, dtype=float)
    src = (pend if probe == 'pendant'
           else int(np.argmin(((pos - ctr) ** 2).sum(1))))
    r = np.sqrt(((pos - pos[src]) ** 2).sum(1))
    R = L // 2
    sponge = np.clip((r - (R - 5.0)) / 5.0, 0.0, 1.0) ** 2 * 0.9
    u = np.zeros(n)
    v = np.zeros(n)
    per = 2 * np.pi / omega
    t0 = steps * dt - 2.0 * per
    vc = vs = 0.0
    nsamp = 0
    for k in range(steps):
        t = k * dt
        a = -Lap.dot(u) - sponge * v
        a[src] += np.sin(omega * t)
        v += dt * a
        u += dt * v
        if t >= t0:
            vc += v[src] * np.cos(omega * t)
            vs += v[src] * np.sin(omega * t)
            nsamp += 1
    Vamp = 2.0 * np.sqrt(vc ** 2 + vs ** 2) / max(nsamp, 1)
    Z = 1.0 / Vamp
    res = dict(z=z, probe=probe, Z=float(Z), Vamp=float(Vamp))
    st[key] = res
    save(st)
    return res


def c1_scan(zs=(3.0, 3.25, 3.5, 3.75, 4.0), L=41, seed=0):
    """C1 (scalar sector): locate the propagation transition in z
    by the C2 classifier (p_dyn near 1 AND finite front speed =
    medium; p_dyn >> 1 = localizing). BAR: the transition z with
    size drift shown on three sizes at the bracketing z.
    HONEST SCOPE NOTE (recorded at charter grade): in the SCALAR
    harmonic model the pretension enters only as the overall bond
    weight (it rescales c), so the pretension AXIS of C1 -- tension
    stabilizing sub-isostatic VECTOR networks -- is not probed
    here; it requires the vector instrument and is recorded as
    deferred, not answered."""
    out = []
    for z in zs:
        r = c2_dynamic(L=L, z=z, source='center',
                       tag=f'c1-z{z}-L{L}-s{seed}', steps=460)
        out.append((z, r['p_dyn'], r['c']))
    return out


def c5_isotropy(z=6, L=41):
    """C5: angular variance of the static response at fixed r
    (octant-averaged direction classes: axis (100), face diagonal
    (110), body diagonal (111)) from the cached C3 solve field.
    Reported as a map (no pass/fail per the charter)."""
    # recompute the static field (cheap) and compare u at matched r
    pos, bonds, _ = cubic_network(L, None if z >= 6 else z, 0)
    n = len(pos)
    Lap = graph_laplacian(n, bonds, w=1.0)
    ctr = np.array([L // 2] * 3, dtype=float)
    src = int(np.argmin(((pos - ctr) ** 2).sum(1)))
    r = np.sqrt(((pos - pos[src]) ** 2).sum(1))
    shell = r >= (L // 2 - 1)
    fidx = np.where(~shell)[0]
    f = np.zeros(n)
    f[src] = 1.0
    u = np.zeros(n)
    ui, _ = sla.cg(Lap[fidx][:, fidx], f[fidx], rtol=1e-10,
                   maxiter=4000)
    u[fidx] = ui
    d = pos - pos[src]
    res = {}
    for name, vec in (('100', (1, 0, 0)), ('110', (1, 1, 0)),
                      ('111', (1, 1, 1))):
        v = np.array(vec, float)
        v /= np.linalg.norm(v)
        for rr in (6, 10, 14):
            q = pos[src] + v * rr
            i = int(np.argmin(((pos - q) ** 2).sum(1)))
            res[f'{name}@{rr}'] = float(u[i] * rr)  # u*r ~ const
    return res


if __name__ == '__main__':
    print('== COORDINATION BRICK: C3 static fidelity ==')
    for z, srcm in [(6, 'center'), (6, 'pendant'), (5, 'center'),
                    (4, 'center'), (3, 'center')]:
        tag = f'c3-z{z}-{srcm}'
        r = c3_static(L=41, z=z, source=srcm, tag=tag)
        bar = 'PASS' if abs(r['p'] - 1.0) <= 0.05 else 'FAIL'
        if srcm == 'pendant':
            note = ('(pendant: p is the exponent AT the anchor '
                    'region; pre-registered position: sourcing is '
                    'from the anchor, not the pendant)')
        else:
            note = ''
        print(f"  z={z} src={srcm}: potential exponent p = "
              f"{r['p']:.4f}  [bar |p-1|<=0.05: {bar}] {note}")

    print('== COORDINATION BRICK: C2 dynamic source fidelity ==')
    for z, srcm in [(6, 'center'), (6, 'pendant'), (4, 'center'),
                    (3, 'center')]:
        tag = f'c2-z{z}-{srcm}'
        r = c2_dynamic(L=49, z=z, source=srcm, tag=tag)
        bar = 'PASS' if abs(r['p_dyn'] - 1.0) <= 0.05 else 'FAIL'
        print(f"  z={z} src={srcm}: p_dyn = {r['p_dyn']:.4f}  "
              f"front speed c = {r['c']:.4f}  "
              f"[bar |p-1|<=0.05: {bar}]")

    print('== COORDINATION BRICK: C4 impedance ==')
    zs = []
    for z, pr in [(6, 'center'), (6, 'pendant'), (4, 'center'),
                  (3, 'center')]:
        tag = f'c4-z{z}-{pr}'
        r = c4_impedance(L=41, z=z, probe=pr, tag=tag)
        zs.append((z, pr, r['Z']))
    Zbulk = [x[2] for x in zs if x[:2] == (6, 'center')][0]
    for z, pr, Z in zs:
        dev = (Z - Zbulk) / Zbulk * 100
        bar = ('PASS' if abs(dev) <= 10 else
               ('EXPECTED-DIVERGENT' if pr == 'pendant' else 'FAIL'))
        print(f"  z={z} probe={pr}: Z = {Z:.4f}  "
              f"({dev:+.1f}% vs bulk)  [{bar}]")

    print('== COORDINATION BRICK: C1 propagation transition ==')
    for z, pd, c in c1_scan():
        cls = 'MEDIUM' if abs(pd - 1) <= 0.15 else 'LOCALIZING'
        print(f"  z={z}: p_dyn = {pd:.3f}  c = {c:.3f}  [{cls}]")
    for L in (33, 49):
        r = c2_dynamic(L=L, z=3.5, source='center',
                       tag=f'c1-z3.5-L{L}', steps=420)
        print(f"  size drift z=3.5 L={L}: p_dyn = "
              f"{r['p_dyn']:.3f}  c = {r['c']:.3f}")
    print('== COORDINATION BRICK: C5 isotropy map (u*r, z=6) ==')
    m = c5_isotropy()
    for k in sorted(m):
        print(f"  {k}: {m[k]:.5f}")

def _atomic_write(path, data):
    """write to a temp file then rename: a full disk can truncate the temp file, never the checkpoint (2026-09-13)."""
    import os
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_bytes(data)
    os.replace(tmp, path)

