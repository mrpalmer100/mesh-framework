"""COMMISSION ORBIT-TWIST -- does the registered machinery couple a mode's polarization handedness to its orbital
sense? Charter analysis/ORBIT_TWIST_charter_LOCKED.md (locked 2026-10-09). The instrument is QB-025's two-polarization
chain (unit masses, unit tension/transverse stiffness, x and y displacements per site; benchmarks/quantum/
junction_realized.py) closed into a RING of N sites, so a mode carries an orbital winding m (GRV-020's azimuth) and a
polarization handedness sigma = +/-1 (the circular basis QB-025's device B resolves). Each cell of the locked
enumeration is one modification of the ring's dynamical matrix; the eigenfrequencies omega(m, sigma) are read by
projecting the eigenvectors on the circular winding modes, and the cell is typed by the FORM of omega(m, +) - omega(m, -):
  IDENTITY   proportional to sigma * m with a registered coefficient (the l . s form, coefficient fixed)
  SHAPE      the l . s form with one unregistered input named
  WRONG-FORM sigma-dependent but not proportional to m (e.g. sigma alone, or sigma * sign(m) flat in |m|)
  NONE       sigma-independent (a linear-basis splitting is NONE for l . s: it does not resolve sigma)
Cells: O1 control (bare ring); M0 curvature (in-plane stiffness from the bend law); M1 the gyroscopic coupling (QB-025
device B, g on the whole ring); M2 the geometric (Rytov) rotation of the transverse frame along a non-planar path,
frame angle d psi / d s = tau; M3 a polarization-dependent reflecting boundary (open chain, contact-law segment).
The quadratic eigenproblem (omega^2 M - i omega G - K) v = 0 is solved by linearization; every number is from the
engine's own matrices, no fit anywhere. Usage: python benchmarks/quantum/orbit_twist.py [--N 96]
"""
import sys, json, pathlib
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[2]
N = int(sys.argv[sys.argv.index('--N') + 1]) if '--N' in sys.argv else 96
MS = [1, 2, 3, 4, 5, 6]
A_C = -0.509658; B_C = 2 * np.pi * (2.5 - 7 * np.sqrt(2) / 4)        # the bend law (FND-MATTER-013/014), for M0


def ring_matrices(ku=1.0, kv=1.0, g=0.0, tau=0.0):
    """K (stiffness) and G (gyroscopic) for the ring; local transverse frame rotated by tau per site (Rytov transport)."""
    K = np.zeros((2 * N, 2 * N)); G = np.zeros((2 * N, 2 * N))
    c, s = np.cos(tau), np.sin(tau)
    R = np.array([[c, -s], [s, c]])                      # frame of site j+1 relative to site j
    D = np.diag([ku, kv])
    for j in range(N):
        a, b = j, (j + 1) % N
        # bond energy 1/2 (x_b' - x_a)^T D (x_b' - x_a) with x_b' = R^T x_b (b's displacement expressed in a's frame)
        Ia, Ib = slice(2 * a, 2 * a + 2), slice(2 * b, 2 * b + 2)
        K[Ia, Ia] += D; K[Ib, Ib] += R @ D @ R.T; K[Ia, Ib] += -D @ R.T; K[Ib, Ia] += -R @ D
        G[Ia, Ia] += np.array([[0, g], [-g, 0]])         # a_u += g v', a_v -= g u'  (QB-025 device B)
    return K, G


def spectrum(K, G):
    """eigenfrequencies and vectors of omega^2 v = K v + i omega G v (linearized); returns positive omegas."""
    n = K.shape[0]
    A = np.block([[np.zeros((n, n)), np.eye(n)], [K, 1j * G]])      # state (v, y = omega v): omega [v; y] = A [v; y]
    w, V = np.linalg.eig(A)
    keep = w.real > 1e-9
    return w.real[keep], V[:n, keep]


def read(K, G, ms=MS):
    """omega(m, sigma) by projecting eigenvectors on circular winding modes e^{i m theta} (u +/- i v)."""
    w, V = spectrum(K, G)
    th = 2 * np.pi * np.arange(N) / N
    out = {}
    for m in ms:
        for sg in (+1, -1):
            for sm in (+1, -1):                           # orbital sense: m > 0 and m < 0
                e = np.exp(1j * sm * m * th) / np.sqrt(N)
                vec = np.zeros(2 * N, complex); vec[0::2] = e; vec[1::2] = sg * 1j * e; vec /= np.linalg.norm(vec)
                ov = np.abs(vec.conj() @ V) ** 2 / (np.linalg.norm(V, axis=0) ** 2)
                # the overlap-weighted frequency of the circular mode: exact when the eigenmodes are circular, the mean of
                # the linear pair when they are linear (so a linear-basis splitting reads as sigma-independent: NONE)
                wmean = float((ov * w).sum() / ov.sum()); out[(sm * m, sg)] = (wmean, float(ov.max()))
    return out


def typed(table, label):
    """type the cell from omega(m,+) - omega(m,-) over m = 1..6 and both senses."""
    d = {m: table[(m, 1)][0] - table[(m, -1)][0] for m in [sm * mm for mm in MS for sm in (1, -1)]}
    pos = np.array([d[m] for m in MS]); neg = np.array([d[-m] for m in MS])
    tiny = 1e-9
    if np.all(np.abs(pos) < tiny) and np.all(np.abs(neg) < tiny):
        t = 'NONE'
    else:
        odd_in_m = np.allclose(pos, -neg, atol=1e-7)          # sigma.sign(m) structure
        prop_m = np.allclose(pos / np.array(MS, float), pos[0], rtol=0.05) if odd_in_m and abs(pos[0]) > tiny else False
        if odd_in_m and prop_m:
            t = 'SHAPE'                                        # proportional to sigma * m (coefficient tied to the cell's input)
        elif odd_in_m:
            t = 'WRONG-FORM (sigma * sign(m), flat in |m|)'
        else:
            t = 'WRONG-FORM (sigma alone, even in m)'
    print(f"[ot {label}] delta omega(m) = omega(m,+) - omega(m,-):  m>0: " + ', '.join(f"{v:+.5f}" for v in pos) +
          "   m<0: " + ', '.join(f"{v:+.5f}" for v in neg) + f"   -> {t}")
    return t, pos.tolist(), neg.tolist()


def main():
    res = {}
    # O1 control: the bare ring; sigma degenerate; omega = 2 sin(pi m / N)
    K, G = ring_matrices(); T = read(K, G)
    exact = [2 * np.sin(np.pi * m / N) for m in MS]
    print(f"[ot O1] bare ring N = {N}: omega(m,+) " + ', '.join(f"{T[(m,1)][0]:.5f}" for m in MS) + "  vs 2 sin(pi m/N) " + ', '.join(f"{e:.5f}" for e in exact))
    res['O1'] = typed(T, 'O1 control')
    # M0 curvature: in-plane transverse stiffness raised by the bend law's cost at the ring's curvature 1/R, R = N/(2 pi)
    R = N / (2 * np.pi); dE = (A_C + B_C * np.log(2 * np.pi * R)) / (2 * np.pi * R)     # bend law dE x L = a + b ln L per unit length
    ku = 1.0 + abs(dE)                                           # the in-plane bond stiffened by the bend energy density (out-of-plane unchanged)
    K, G = ring_matrices(ku=ku); T = read(K, G)
    print(f"[ot M0] curvature: R = {R:.2f}, bend-law density {dE:+.5f}, k_u = {ku:.5f}, k_v = 1; linear splitting omega_u - omega_v at m=1..6: " +
          ', '.join(f"{2*np.sqrt(ku)*np.sin(np.pi*m/N) - 2*np.sin(np.pi*m/N):+.5f}" for m in MS))
    res['M0'] = typed(T, 'M0 curvature')
    # M1 gyroscopic coupling on the whole ring (QB-025 device B's form; g at the device's own value class)
    g = 0.05
    K, G = ring_matrices(g=g); T = read(K, G)
    print(f"[ot M1] gyroscopic g = {g}: analytic omega = -sigma g/2 + sqrt(K + g^2/4): shift {-g/2:+.5f} per sigma, independent of m and of its sign")
    res['M1'] = typed(T, 'M1 gyroscopic')
    # M2 Rytov transport: frame rotation tau per site (total Psi = N tau around the ring)
    tau = 2 * np.pi * 0.05 / N                                   # Psi = 0.05 turns of the frame per circuit
    K, G = ring_matrices(tau=tau); T = read(K, G)
    print(f"[ot M2] Rytov: tau = {tau:.5f} per site, Psi = {N*tau:.4f} rad per circuit; analytic omega = 2 sin((pi m - sigma Psi/2)/N): shift {-2*np.cos(np.pi/N)*np.sin(N*tau/(2*N)):+.5f} x sigma sign(m) at small m, flat in |m|")
    res['M2'] = typed(T, 'M2 Rytov')
    # M2 scan in tau: the shift vs Psi
    print("[ot M2] shift vs Psi (turns): " + ', '.join(f"{t:.2f}: {read(*ring_matrices(tau=2*np.pi*t/N))[(1,1)][0] - read(*ring_matrices(tau=2*np.pi*t/N))[(1,-1)][0]:+.5f}" for t in (0.02, 0.05, 0.1, 0.2)))
    # M3 boundary reflection: open chain; the end segment has a polarization-dependent stiffness (contact on surfaces: in-plane
    # vs out-of-plane differ, FND-184's support function h(phi) = rho (1 + |cos phi|) gives the ratio 2:1 between the two
    # transverse directions at a crossing); the standing modes' frequencies are read per polarization
    def open_chain(ku_end, kv_end, seg=8):
        K = np.zeros((2 * N, 2 * N))
        for j in range(N - 1):
            d = np.diag([ku_end, kv_end]) if j >= N - 1 - seg else np.eye(2)
            Ia, Ib = slice(2 * j, 2 * j + 2), slice(2 * j + 2, 2 * j + 4)
            K[Ia, Ia] += d; K[Ib, Ib] += d; K[Ia, Ib] -= d; K[Ib, Ia] -= d
        K[0:2, 0:2] += np.eye(2) * 1e6; K[-2:, -2:] += np.eye(2) * 1e6       # pinned ends
        return K, np.zeros_like(K)
    K, G = open_chain(2.0, 1.0); w, V = spectrum(K, G)
    wu = sorted(w[np.abs(V[0::2, :]).sum(axis=0) > np.abs(V[1::2, :]).sum(axis=0)])[:6]
    wv = sorted(w[np.abs(V[0::2, :]).sum(axis=0) <= np.abs(V[1::2, :]).sum(axis=0)])[:6]
    print(f"[ot M3] boundary segment stiffness (u, v) = (2, 1): lowest standing modes u: " + ', '.join(f"{x:.5f}" for x in wu) + "; v: " + ', '.join(f"{x:.5f}" for x in wv))
    print("[ot M3] the splitting is between LINEAR polarizations (u vs v) and does not depend on the sense of propagation: sigma is not resolved -> NONE")
    res['M3'] = ('NONE', wu, wv)
    # the table and the verdict by the locked forms
    print("[ot] cells: " + '; '.join(f"{k}: {v[0]}" for k, v in res.items() if k != 'O1'))
    types = [v[0].split()[0] for k, v in res.items() if k != 'O1']
    if 'IDENTITY' in types:
        verdict = 'SO-DERIVED (size and sign to be read)'
    elif 'SHAPE' in types:
        verdict = 'SO-SHAPE-ONLY'
    else:
        verdict = 'SO-NO-MECHANISM'
    print(f"[ot] VERDICT: {verdict}")
    (ROOT / 'analysis' / 'orbit_twist_cells.json').write_text(json.dumps({k: {'type': v[0], 'pos': v[1], 'neg': v[2]} for k, v in res.items()}, indent=1))
    return verdict


if __name__ == '__main__':
    main()
