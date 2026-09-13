"""CASIMIR-PLATE Legs 2-3 -- the wound piston ladder on the FND-089 instrument.
Charter analysis/CASIMIR_PLATE_charter_LOCKED.md (+A1 piston calibration, +A2 plate
condition from E-RECON, +A3 below). Plate normal along z (weave axis). Plate condition:
tangential (in-plane x,y) collective displacement PINNED at the plate sites (Dirichlet,
both transverse bands); normal (z) displacement free; d_eff = d + 1.
Per k_par point: dense eigenvalues of the slab dynamical matrix (3 P^2 n dof) for every
slab height the piston needs; three readings from the same spectrum:
  (ii)  standing-wave action:  E = (1/2) S sum omega          (CAS-FORM reads this)
  (i)   coherent winding:      the k_par = 0 slice, one mode family per band (A3)
  (iii) warm-weave:            F = k_B T_w sum ln(omega/omega_0)  (classical)
Checkpoint per k-point to analysis/casimir_plate_ckpt.pkl. Resumable. One process; run
with run_local.sh (it loops until 'COMPLETE'). SJ memos not used (no torus solves).
"""
import numpy as np, pickle, pathlib, sys, time, itertools
from scipy.linalg import eigvalsh


def _atomic_write(path, data):
    """write to a temp file then rename: a full disk can truncate the temp file, never the checkpoint (2026-09-13)."""
    import os
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_bytes(data)
    os.replace(tmp, path)

ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'benchmarks' / 'foundations'))
import shin6_3d_bloch as S6                     # noqa  (instrument, byte-identical)

CKPT = ROOT / 'analysis' / 'casimir_plate_ckpt.pkl'
F = 1 / 5                                        # adjudicating member (FND-089/100)
RUNGS = [10, 20, 30, 40]                         # commensurate with P = 5 (recorded)
LPIST = 120                                      # 3 x d_max
NR, NT, KC, POW = 12, 8, np.pi / 5, 3           # polar stretched quadrature (Leg 0)
NR_CHK, NT_CHK = 24, 32                          # v4 check grid (top rung only)


def polar_nodes(kc, Nr, Nt, power):
    t, wt = np.polynomial.legendre.leggauss(Nr); t = (t + 1) / 2; wt = wt / 2
    k = kc * t ** power; dk = kc * power * t ** (power - 1) * wt
    th = np.pi * (np.arange(Nt // 2) + 0.5) / (Nt // 2); dth = 2 * np.pi / (Nt // 2)   # k <-> -k symmetry
    K, TH = np.meshgrid(k, th, indexing='ij'); W = np.outer(k * dk, np.full(Nt, dth))
    return list(zip((K * np.cos(TH)).ravel(), (K * np.sin(TH)).ravel(), W.ravel()))


def slab_matrix(kx, ky, n, P, T, PR):
    """Slab of n layers z = 0..n-1, periodic in-plane with Bloch phase (kx, ky);
    plate sites at z = -1 and z = n: in-plane displacement pinned (u_x = u_y = 0),
    z-displacement free (treated as an extra free layer? no: the plate site is a
    fixed site for the pinned components and absent for the free one -- a free
    z-component at the plate has no restoring partner, so it is simply not a dof:
    bonds to plate sites contribute their on-site stiffness for x,y only)."""
    sites = [(x, y, z) for z in range(n) for x in range(P) for y in range(P)]
    idx = {s: i for i, s in enumerate(sites)}
    N = len(sites); D = np.zeros((3 * N, 3 * N), dtype=complex)
    for s in sites:
        i = idx[s]
        for b in S6.NBRS:
            bh = np.array(b, float); r2 = bh @ bh; bh = bh / np.sqrt(r2)
            xj, yj, zj = s[0] + b[0], s[1] + b[1], s[2] + b[2]
            shell = 1.0 if r2 == 1 else 2.0
            tj = T[(xj % P, yj % P, zj % P)]          # tangent field continues through the plate
            ts = T[(s[0], s[1], s[2] % P)]
            w = shell * (S6.KX + 0.5 * ((bh @ ts) ** 2 + (bh @ tj) ** 2)) / r2
            blk = w * np.outer(bh, bh)
            if 0 <= zj < n:
                j = idx[(xj % P, yj % P, zj)]
                ph = np.exp(1j * (kx * b[0] + ky * b[1]))
                D[3 * i:3 * i + 3, 3 * j:3 * j + 3] -= blk * ph
                D[3 * i:3 * i + 3, 3 * i:3 * i + 3] += blk
            else:                                     # plate site: pinned x,y; z free (no partner)
                pin = np.diag([1.0, 1.0, 0.0])
                D[3 * i:3 * i + 3, 3 * i:3 * i + 3] += pin @ blk @ pin
    return (D + D.conj().T) / 2


def slab_omegas(kx, ky, n, P, T, PR, scale):
    w2 = eigvalsh(slab_matrix(kx, ky, n, P, T, PR), driver="evd")
    return np.sqrt(np.clip(w2, 0, None)) / scale


def g(d, L): return 1 + (d / (L - d)) ** 3 - 2 * (2 * d / L) ** 3


def main():
    st = pickle.loads(CKPT.read_bytes()) if CKPT.exists() else {}
    P, sites, T, PR = S6.build_cell(F, True)
    scale = st.get('scale') or S6.norm_scale(P, sites, T, PR)
    st['scale'] = scale
    nodes = polar_nodes(KC, NR, NT, POW) + [(0.0, 0.0, 0.0)]   # last node: k_par = 0 slice for reading (i), weight 0
    heights = sorted(set([d for d in RUNGS] + [LPIST - d for d in RUNGS] + [LPIST // 2]))
    st.setdefault('meta', dict(P=P, rungs=RUNGS, L=LPIST, heights=heights, quad=(NR, NT, KC, POW)))
    done = st.setdefault('k', {})
    todo = [(i, nd) for i, nd in enumerate(nodes) if i not in done]
    if not todo:
        print("[casimir] LADDER COMPLETE -- run the verdict step", flush=True); return
    i, (kx, ky, W) = todo[0]
    t0 = time.time(); rec = dict(kx=kx, ky=ky, W=W, om={})
    for n in heights:
        rec['om'][n] = slab_omegas(kx, ky, n, P, T, PR, scale).astype(np.float64)
    done[i] = rec; _atomic_write(CKPT, pickle.dumps(st))
    print(f"[casimir] k-point {i+1}/{len(nodes)} done in {time.time()-t0:.0f}s "
          f"(|k|={np.hypot(kx,ky):.4f}); {len(nodes)-len(done)} remain", flush=True)


if __name__ == '__main__':
    main()
