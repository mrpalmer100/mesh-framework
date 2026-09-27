"""COMMISSION KIN-BREAKDOWN (charter analysis/KIN_BREAKDOWN_charter_LOCKED.md, locked 2026-09-27).
S1 symbolic derivation with machine dimensional check; S2 E_c(w) at the three registered scale sets;
S3 the w that E_crit and the Schwinger field require; S4 the confrontation. Sealed to analysis/kin_breakdown.npz."""
import pathlib, numpy as np, sympy as sp
from sympy.physics.units import meter, second, kilogram, coulomb, volt, joule, convert_to
ROOT = pathlib.Path(__file__).resolve().parents[2]; OUT = ROOT / 'analysis' / 'kin_breakdown.npz'
# ---- S1: symbolic ----------------------------------------------------------------------------
T0, r, a, w, e, c = sp.symbols('T0 r a w e c', positive=True)
mu = T0 / c**2; I_T = mu * r**2; v_t = c / sp.sqrt(5)
V0_per_len = I_T * v_t**2 / (w**2 * a**2)          # orientation-potential amplitude per unit length
E_c = 2 * sp.pi * V0_per_len / e                    # breakdown field = 2 pi V0 / e
E_c_simplified = sp.simplify(E_c)
dim = convert_to(E_c.subs({T0: joule/meter, r: meter, a: meter, w: 1, e: coulomb, c: meter/second}), volt/meter)
print("[kb S1] E_c =", E_c_simplified, "  dimensional check ->", dim)
assert sp.simplify(E_c_simplified - 2*sp.pi*T0*r**2/(5*e*w**2*a**2)) == 0
# ---- S2/S3: numbers --------------------------------------------------------------------------
E_S = 1.32e18; E_crit = 2.0e23; E_laser = 9.1e14; ee = 1.602176634e-19; rr = 1.87e-19 / 2
sets = {'kappa_pack 1 (M-point)': (434.0, 6.00e-17), 'kappa_pack 50': (1599.0, 1.63e-17), 'kappa_pack 250': (2734.0, 9.53e-18)}
ws = np.array([0.8, 1.0, 1.25, 1.5, 2.0, 2.8]); rows = {}
for name, (t0, aa) in sets.items():
    pref = 2*np.pi*t0*rr**2/(5*ee*aa**2)            # E_c = pref / w^2
    Ec = pref / ws**2; w_S = np.sqrt(pref / E_S); w_crit = np.sqrt(pref / E_crit); w_laser = np.sqrt(pref / E_laser)
    rows[name] = (pref, Ec, w_S, w_crit, w_laser)
    print(f"[kb S2] {name:24s} T0 {t0:6.0f} a {aa:.2e}: E_c = {pref:.2e}/w^2 V/m ->", " ".join(f"w{wv}:{ev:.1e}" for wv, ev in zip(ws, Ec)))
    print(f"[kb S3] {name:24s} E_c = Schwinger at w = {w_S:.2f}; = E_crit at w = {w_crit:.3f}; = laser record at w = {w_laser:.2f}")
np.savez(OUT, ws=ws, names=list(rows), pref=[v[0] for v in rows.values()], Ec=[v[1] for v in rows.values()],
         w_S=[v[2] for v in rows.values()], w_crit=[v[3] for v in rows.values()], w_laser=[v[4] for v in rows.values()],
         E_S=E_S, E_crit=E_crit, E_laser=E_laser, formula=str(E_c_simplified))
print(f"[kb] sealed -> {OUT.name}")
