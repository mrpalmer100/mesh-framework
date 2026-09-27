"""COMMISSION KIN-DRIVE (charter analysis/KIN_DRIVE_charter_LOCKED.md, locked 2026-09-27).
FND-STRAND-002's chain (phi_ddot = kt Lap(phi) - sin(phi), kink 4 arctan exp(x/w), ends held,
winding-weighted centre; the kink relaxed to the chain's own site-centred profile at F = 0 by the
pn_barrier protocol before the drive is switched on) with the registered lock's uniform torque
F = c_L eps' added and swept. Two trackers (winding-weighted centre; the phi = pi crossing) are
read; both are recorded. K1 force law (mass 2 pi |F| / |a| vs 8/w), K2 depinning threshold vs the
relaxed PN barrier, K3 velocity history vs the relativistic form. Outputs SEALED to
analysis/kin_drive.npz. Shakedown (recorded): a first draft used a 1200-node chain with the kink
300 nodes from an end and a 12-unit fit window; end-held boundary layers reached the kink inside
the window and flipped the fitted sign at F >= 1e-3. The sealed protocol centres the kink on a
2400-node chain (ends 1200 away, c_t <= 2.8, no arrival inside t <= 380) and fits t in [20, 380]."""
import sys, pathlib, time
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[2]; sys.path.insert(0, str(ROOT))
from benchmarks.foundations import strand_twist_transport as ST   # noqa: E402 (FND-STRAND-002's engine)
OUT = ROOT / 'analysis' / 'kin_drive.npz'


def run(w, F, N=2400, x0=1200, T=400.0, dt=0.02, every=50, stop=None):
    kt = w * w; xs = np.arange(N) - x0; phi = 4 * np.arctan(np.exp(xs / w)); dtr = 0.25 / max(kt, 1.0)
    for _ in range(20000):
        lap = np.zeros_like(phi); lap[1:-1] = phi[2:] - 2 * phi[1:-1] + phi[:-2]; g = kt * lap - np.sin(phi); g[0] = g[-1] = 0; phi += dtr * g
    phidot = np.zeros(N); wind0 = (phi[-1] - phi[0]) / (2 * np.pi)
    def com(p): dp = np.diff(p); return float(np.sum(0.5 * (np.arange(N - 1) + np.arange(1, N)) * dp / dp.sum()))
    def cross(p): i = int(np.argmax(p > np.pi)); return float(i - 1 + (np.pi - p[i - 1]) / (p[i] - p[i - 1]))
    ts, xc, xp = [], [], []; t = 0.0; k = 0; we = 0.0
    while t < T:
        lap = np.zeros_like(phi); lap[1:-1] = phi[2:] - 2 * phi[1:-1] + phi[:-2]
        phidot += dt * (kt * lap - np.sin(phi) + F); phidot[0] = phidot[-1] = 0.0; phi += dt * phidot; t += dt; k += 1
        if k % every == 0:
            ts.append(t); xc.append(com(phi)); xp.append(cross(phi)); we = max(we, abs((phi[-1] - phi[0]) / (2 * np.pi) - wind0))
            if stop is not None and (xp[-1] > stop[1] or xp[-1] < stop[0]): break
    return np.array(ts), np.array(xc), np.array(xp), we


def K1(w, Fs):
    rows = []
    for F in Fs:
        ts, xc, xp, we = run(w, F); m = (ts > 20) & (ts < 380)
        a_c = 2 * np.polyfit(ts[m], xc[m], 2)[0]; a_p = 2 * np.polyfit(ts[m], xp[m], 2)[0]
        Mc, Mp = 2 * np.pi * F / abs(a_c), 2 * np.pi * F / abs(a_p); rows.append((F, a_c, a_p, Mc, Mp, we))
        print(f"[kd K1] w {w}: F {F:.0e}  a(com) {a_c:+.3e} a(cross) {a_p:+.3e}  M = 2pi F/|a| {Mc:.4f}/{Mp:.4f} vs 8/w {8 / w:.4f} (ratio {Mc * w / 8:.4f})  winding err {we:.1e}")
    return rows


def K2(w, F_lo=1e-8, F_hi=3e-6):
    M = 8 / w
    def moves(F):
        t3 = np.sqrt(6 * M / (2 * np.pi * F)); ts, xc, xp, _ = run(w, F, T=3 * t3, every=200)
        return abs(xp[-1] - xp[0]) > 3.0
    lo_ok, hi_ok = not moves(F_lo), moves(F_hi)
    print(f"[kd K2] w {w}: bracket check: pinned at {F_lo:.0e}: {lo_ok}; moves at {F_hi:.0e}: {hi_ok}")
    if not (lo_ok and hi_ok): return (np.nan, np.nan, ST.pn_barrier(w, iters=150000))
    while F_hi / F_lo > 1.5:
        Fm = np.sqrt(F_lo * F_hi)
        if moves(Fm): F_hi = Fm
        else: F_lo = Fm
    E_pn = ST.pn_barrier(w, iters=150000)
    print(f"[kd K2] w {w}: depinning F_th in [{F_lo:.2e}, {F_hi:.2e}]; relaxed PN {E_pn:.2e}; E_PN/2 = {E_pn / 2:.2e}; F_th/(E_PN/2) in [{F_lo / (E_pn / 2):.2f}, {F_hi / (E_pn / 2):.2f}]")
    return F_lo, F_hi, E_pn


def K3(w, F=-1e-3):
    ts, xc, xp, we = run(w, F, N=6000, x0=300, T=1e6, every=50, stop=(50, 5700))
    v = np.gradient(xp, ts); M = 8 / w; Fa = abs(F)
    vform = (2 * np.pi * Fa * ts / M) / np.sqrt(1 + (2 * np.pi * Fa * ts / (M * w)) ** 2)
    m = (v > 0.05 * w) & (v <= 0.9 * w); dev = float(np.abs(v[m] / vform[m] - 1).max()) if m.any() else np.nan
    late = v[-len(v) // 5:]; steady = bool(np.std(late) / max(np.mean(late), 1e-12) < 0.01 and v.max() < 0.5 * w)
    print(f"[kd K3] w {w} |F| {Fa:.0e}: v reaches {v.max():.3f} (c_t = {w}); max |v/v_rel - 1| over 0.05..0.9 c_t: {dev:.3f}; steady sub-luminal drift? {steady}; winding err {we:.1e}; run length {ts[-1]:.0f}")
    return ts, v, vform, dev, float(v.max()), steady, we


def main():
    t0 = time.time(); out = {}
    for w in (2.0, 2.8):
        out[f'K1_{w}'] = np.array(K1(w, [1e-4, 3e-4, 1e-3, 3e-3]))
    for w in (2.0, 2.8):
        out[f'K2_{w}'] = np.array(K2(w))
    for w in (2.0, 2.8):
        ts, v, vf, dev, vmax, steady, we = K3(w)
        out[f'K3_{w}'] = np.array([dev, vmax, float(steady), we]); out[f'K3_{w}_ts'] = ts; out[f'K3_{w}_v'] = v; out[f'K3_{w}_vform'] = vf
    np.savez(OUT, elapsed=time.time() - t0, **out); print(f"[kd] sealed -> {OUT.name} ({time.time() - t0:.0f} s)")


if __name__ == '__main__':
    main()
