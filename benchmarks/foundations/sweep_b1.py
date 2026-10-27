"""GRANT-CANDIDATE-SWEEP, B1 made concrete (sandbox, 2026-10-27): the beat, on the locked azimuth of a rope held by its
nodes (shape frozen). With the shape frozen the dynamics instrument's twist sector reduces exactly to the sine-Gordon
equation (kappa / c^2) Phi-dotdot = kappa Phi'' - V'' sin Phi on the ring, integrated here by Stoermer-Verlet (the
full instrument's Jacobian is needless for a frozen shape). Units kappa = c = 1, R = 1, V'' = 100 so Omega = 10,
l = c / Omega = 0.1, M = 1600 (a = 0.0039 << l << L). Known answers: (1) gapped dispersion omega(n)^2 = Omega^2 +
omega_d(n)^2; (2) the static 2 pi kink, E = 8 sqrt(kappa V''), width c / Omega, stationary under the dynamics;
(3) the kink boosted to v: width l / gamma, E = gamma E_0, and it travels at v (Lorentz covariance of the twist)."""
import math
import numpy as np
from scipy.optimize import minimize

M, R, kappa, Vpp = 1600, 1.0, 1.0, 100.0
Omega = math.sqrt(Vpp / kappa); ell = math.sqrt(kappa / Vpp)
a = 2 * math.pi * R / M; s = a * np.arange(M)
print(f"lock V'' = {Vpp}: Omega = {Omega}, l = c/Omega = {ell}; M {M}, a = {a:.4f}, L = {2 * math.pi * R:.3f}")

def accel(P):                      # periodic with winding handled by unwrapped P and a 2 pi offset at the seam
    Pp = np.roll(P, -1); Pm = np.roll(P, 1); Pp[-1] += 2 * math.pi * W; Pm[0] -= 2 * math.pi * W
    return kappa * (Pp - 2 * P + Pm) / a ** 2 - Vpp * np.sin(P)

def energy(P, Pd):
    Pp = np.roll(P, -1); Pp[-1] += 2 * math.pi * W
    return float(np.sum(0.5 * Pd ** 2 + 0.5 * kappa * ((Pp - P) / a) ** 2 + Vpp * (1 - np.cos(P))) * a)

def run(P, Pd, T, h):
    n = int(round(T / h)); A = accel(P)
    for _ in range(n):
        Pd = Pd + 0.5 * h * A; P = P + h * Pd; A = accel(P); Pd = Pd + 0.5 * h * A
    return P, Pd

h = 2e-4
print('(1) gapped dispersion of the azimuth (standing wave of mode n on winding 0):')
W = 0
for n in (0, 5, 20, 80):
    om_d = (2.0 / a) * math.sin(math.pi * n / M); om_th = math.sqrt(Omega ** 2 + om_d ** 2)
    P = 1e-3 * np.cos(n * s / R); Pd = np.zeros(M); amps = []; ts = []; t = 0.0
    steps = int(0.3 * (2 * math.pi / om_th) / h) + 2
    for k in range(steps):
        P, Pd = run(P, Pd, h, h); t += h; amps.append(float(np.dot(P, np.cos(n * s / R)) * (2 if n else 1) / M)); ts.append(t)
    amps = np.array(amps); ts = np.array(ts); k = int(np.argmax(amps < 0)); tq = ts[k - 1] + (ts[k] - ts[k - 1]) * amps[k - 1] / (amps[k - 1] - amps[k])
    om = 2 * math.pi / (4 * tq)
    print(f'   n {n:3d}: omega measured {om:.5f}  theory sqrt(Omega^2 + omega_d^2) {om_th:.5f}  rel {om / om_th - 1:+.1e}   (gap alone {Omega:.1f}, free wave {om_d:.3f})')

print('(2) the static 2 pi kink:')
W = 1
P0 = np.unwrap(4 * np.arctan(np.exp((s - math.pi * R) / ell)))
res = minimize(lambda P: energy(P, np.zeros(M)), P0, method='L-BFGS-B', options=dict(maxiter=20000, ftol=1e-16, gtol=1e-12))
P = res.x; E0 = energy(P, np.zeros(M)); slope = np.max(np.abs(np.diff(P))) / a
print(f'   E_kink {E0:.6f}  closed form 8 sqrt(kappa V\'\') {8 * math.sqrt(kappa * Vpp):.6f}  rel {E0 / (8 * math.sqrt(kappa * Vpp)) - 1:+.1e};  width from max slope 2/l: {2 / slope:.5f} (c/Omega {ell:.5f})')
P1, Pd1 = run(P.copy(), np.zeros(M), 5.0, h)
c0 = s[np.argmin(np.abs(P - math.pi))]; c1 = s[np.argmin(np.abs(P1 - math.pi))]
print(f'   integrated 5 time units (50 beats): E drift {abs(energy(P1, Pd1) - E0) / E0:.1e}, centre moved {c1 - c0:+.2e}; the kink stays put')

print('(3) the moving kink:')
for v in (0.3, 0.6, 0.9):
    g = 1 / math.sqrt(1 - v * v); s0 = math.pi * R
    Pv = np.unwrap(4 * np.arctan(np.exp(g * (s - s0) / ell))); Wd = -v * g * (2 / ell) / np.cosh(g * (s - s0) / ell)
    Ev = energy(Pv, Wd); Pe, Pde = run(Pv.copy(), Wd.copy(), 2.0, h)
    ce = s[np.argmin(np.abs(Pe - math.pi))]; slope_v = np.max(np.abs(np.diff(Pe))) / a
    print(f'   v {v}: E {Ev:.5f} vs gamma E_0 {g * E0:.5f} (rel {Ev / (g * E0) - 1:+.1e});  width after 2.0: {2 / slope_v:.5f} vs l/gamma {ell / g:.5f};  '
          f'speed {((ce - s0) % (2 * math.pi * R)) / 2.0:.4f} (set {v});  E drift {abs(energy(Pe, Pde) - Ev) / Ev:.1e}')
