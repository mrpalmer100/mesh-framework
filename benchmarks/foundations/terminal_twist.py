"""COMMISSION TERMINAL-TWIST (charter analysis/TERMINAL_TWIST_charter_LOCKED.md, locked 2026-09-27).

T1 -- which variable carries GRV-045's quantum, read BEFORE and AFTER the event. The registered
  engine (benchmarks/gravity/handedness_reconnection.py, used as registered: same seed, same
  relaxation, same Frenet bookkeeping) is run with its initial seeded 'over' state kept, and
  three quantities are read on the initial and the final ('through') curve: the Frenet frame
  rotation phi/2pi (GRV-045's F2 observable), the writhe Wr (Gauss double integral), and, for the
  symmetric-seed control GRV-045 itself logged, the same two. Under strand conservation (no cut,
  FND-010; Lk of the material framing conserved) the material twist changes by -dWr (Calugareanu,
  the ledger FND-131 uses), so dWr is the quantity that would reach the screw azimuth.
T2 -- display only if T1 fails: FND-179's chain with 2 pi steps of Phi applied at s = 0 at rate R
  (the candidate's quantum, IF it existed), strand-averaged rate over the last half vs 2 pi R.
Outputs SEALED to analysis/terminal_twist.npz; verdict by terminal_twist_verdict.py.
"""
import sys, pathlib, time
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[2]; sys.path.insert(0, str(ROOT))
from benchmarks.gravity import handedness_reconnection as HR   # noqa: E402  (GRV-045's engine, as registered)
from benchmarks.foundations import current_as_spin as CAS       # noqa: E402  (FND-179's chain)
OUT = ROOT / 'analysis' / 'terminal_twist.npz'


def run_engine(L, N, lateral=True, iters=10000):
    x = np.linspace(-L, L, N); dx = x[1] - x[0]; sig, H, T = HR.sig, HR.H, HR.T
    u = -H + (H + 2 * sig) * np.exp(-(x / (4 * sig)) ** 2)
    v = (0.3 * sig * np.exp(-((x - 0.15) / (2.5 * sig)) ** 2) - 0.12 * sig * np.exp(-((x + 0.35) / (4 * sig)) ** 2)) if lateral else np.zeros_like(x)
    u[0] = u[-1] = -H; v[0] = v[-1] = 0.0
    init = np.stack([x, v, u], 1).copy(); dt = min(0.4 * dx ** 2 / T, 0.02)
    for _ in range(iters):
        r = np.sqrt(x ** 2 + u ** 2) + 1e-12
        gu = T * (np.roll(u, -1) - 2 * u + np.roll(u, 1)) / dx ** 2 - HR.dU(r) * u / r
        gv = T * (np.roll(v, -1) - 2 * v + np.roll(v, 1)) / dx ** 2
        gu[0] = gu[-1] = 0; gv[0] = gv[-1] = 0
        u = u + dt * gu; v = v + dt * gv; u[0] = u[-1] = -H; v[0] = v[-1] = 0.0
    return init, np.stack([x, v, u], 1), float(u[N // 2])


def frenet_phi(rr):
    t = np.diff(rr, axis=0); t /= np.linalg.norm(t, axis=1, keepdims=True)
    b = np.cross(t[:-1], t[1:]); nb = np.linalg.norm(b, axis=1); ok = nb > 1e-12
    bb = b[ok] / nb[ok, None]; tt = t[1:][ok]; phi = 0.0
    for i in range(len(bb) - 1):
        c = np.clip(np.dot(bb[i], bb[i + 1]), -1, 1); s = np.dot(np.cross(bb[i], bb[i + 1]), tt[i]); phi += np.arctan2(s, c)
    return float(phi)


def writhe(P, stride=2):
    P = P[::stride]; t = np.diff(P, axis=0); m = (P[1:] + P[:-1]) / 2; W = 0.0
    for i in range(len(t)):
        d = m[i] - m; r3 = np.linalg.norm(d, axis=1) ** 3; r3[i] = np.inf
        W += ((np.cross(t[i], t) * d).sum(1) / r3).sum()
    return float(W / (4 * np.pi))


def T1():
    rows = []
    for L, N, lat in ((4.0, 601, True), (6.0, 901, True), (4.0, 601, False)):
        init, fin, umid = run_engine(L, N, lat)
        p0, p1 = frenet_phi(init) / (2 * np.pi), frenet_phi(fin) / (2 * np.pi); w0, w1 = writhe(init), writhe(fin)
        rows.append((L, lat, p0, p1, w0, w1, umid))
        print(f"[tt T1] L {L} {'asymmetric seed' if lat else 'symmetric seed (control)'}: through {umid < -0.15};  Frenet phi/2pi initial {p0:+.4f} final {p1:+.4f} "
              f"(change {p1 - p0:+.4f});  writhe initial {w0:+.4f} final {w1:+.4f} (change {w1 - w0:+.4f}); material twist change by Lk conservation {-(w1 - w0):+.4f} x 2pi")
    return rows


def T2_display(R, N=200, T_end=400.0, dt=0.02):
    """FND-179's chain; a 2 pi step of Phi at site 0 every 1/R time units (the candidate's quantum, if it existed)."""
    LAM, CL, KS, I_T, MU = CAS.LAM, CAS.CL, CAS.KS, CAS.I_T, CAS.MU
    Phi = np.zeros(N + 1); u = np.zeros(N + 1); vP = np.zeros(N + 1); vu = np.zeros(N + 1)
    def forces(Phi, u):
        dP = np.diff(Phi); du = np.diff(u); JP = LAM * dP + CL * du; Ju = KS * du + CL * dP
        tP = np.zeros(N + 1); tu = np.zeros(N + 1); tP[:-1] += JP; tP[1:] -= JP; tu[:-1] += Ju; tu[1:] -= Ju; return tP, tu
    steps = int(T_end / dt); rates = []; next_ev = 0.0; n_ev = 0
    for n in range(steps):
        t = n * dt
        if t >= next_ev: Phi[0] += 2 * np.pi; n_ev += 1; next_ev += 1.0 / R
        tP, tu = forces(Phi, u); vP += 0.5 * dt * tP / I_T; vu += 0.5 * dt * tu / MU; vu[0] = vu[N] = 0; vP[0] = 0
        Phi += dt * vP; u += dt * vu
        tP, tu = forces(Phi, u); vP += 0.5 * dt * tP / I_T; vu += 0.5 * dt * tu / MU; vu[0] = vu[N] = 0; vP[0] = 0
        if n >= steps // 2: rates.append(vP[1:].mean())
    return float(np.mean(rates)), 2 * np.pi * R


def main():
    t0 = time.time(); rows = T1()
    disp = [(R,) + T2_display(R) for R in (0.005, 0.02, 0.05)]
    for R, m, ex in disp: print(f"[tt T2 display] R {R}: strand mean rate {m:+.4f} vs 2 pi R {ex:.4f} (ratio {m / ex:.3f})")
    np.savez(OUT, rows=np.array(rows, dtype=object), disp=np.array(disp), elapsed=time.time() - t0)
    print(f"[tt] sealed -> {OUT.name} ({time.time() - t0:.0f} s)")


if __name__ == '__main__':
    main()
