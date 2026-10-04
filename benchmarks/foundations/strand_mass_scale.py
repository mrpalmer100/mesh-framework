"""COMMISSION STRAND-MASS-SCALE (charter analysis/STRAND_MASS_SCALE_charter_LOCKED.md, locked 2026-10-04).
The chain from the fourth grant's V_0 source to the twist gap in eV and FND-182's number, under B-1 (every
input registered with its claim id or REFUSE at that step) and B-2 (dimensional check by machine).
C1 V_sec per crossing needs A_c and sigma of the registered contact law (EM-RECON-023) in joules and metres and
   the crossing density per node: READ AT LOCK: A_c and sigma are SYMBOLIC in EM-RECON-023; FND-KIN-005's 13.8 eV
   plateau is a hydrogen-calibrated (13.6 eV) vortex-mode overlap in an atomic toy, not the vacuum crossing; no
   registered crossing density per strand length exists at the coarse level. C1 is therefore REFUSED under B-1 and
   V_0 is carried as a symbol through C2..C5, which is what this script computes exactly:
   the chain's identities, its dimensional check, and the displays that follow from the registered w bracket.
Inputs (registered): T0 434/1599/2734 J/m at a 6.0e-17/1.63e-17/9.53e-18 m (ROPE_PARAMETERS); r = d_c/2 with d_c = 1.87e-19 m
(HBAR-005); mu = T0/c^2; I_T = mu r^2 per unit length (GRV-073 rod class); twist stiffness per node by two registered routes,
C_rod = T0 r^2/2 (GRV-073: C = G pi r^4/2, G ~ E/2, E = k/(pi r^2), k = 2 T0) and C_band = I_T v_t^2 = T0 r^2/5 (FND-MATTER-047,
the route FND-182 used); w bracket [0.8, 2.8] (FND-STRAND-002, FND-KIN-002); e = 1.602e-19 C; hbar 1.0546e-34 J s (imported, GRV-014,
display only); the laser record ~9.1e14 V/m (Yoon et al. 2021, to be confirmed at registration); Schwinger 1.32e18 V/m.
"""
import numpy as np, sympy as sp, pathlib
OUT = pathlib.Path(__file__).resolve().parents[2] / 'analysis' / 'strand_mass_scale.npz'
E_LASER, E_SCHW, HBAR, E = 9.1e14, 1.32e18, 1.0546e-34, 1.602e-19
C = 2.998e8; DC = 1.87e-19; R = DC / 2
SETS = [('kappa_pack 1', 434.0, 6.0e-17), ('kappa_pack 50', 1599.0, 1.63e-17), ('kappa_pack 250', 2734.0, 9.53e-18)]


def chain():
    T0, a, r, c, e, V0, w = sp.symbols('T0 a r c e V_0 w', positive=True)
    mu = T0 / c ** 2; I_T = mu * r ** 2                          # per unit length
    C_rod = T0 * r ** 2 / 2; C_band = T0 * r ** 2 / 5             # torsional rigidity, two registered routes (energy x length)
    kt_node = C_rod / a                                            # twist stiffness per node (energy)
    w2 = kt_node / V0                                              # FND-STRAND-002: kt in units of V_0 is w^2
    om2 = V0 / (I_T * a)                                           # FND-STRAND-008: omega_min^2 = V_0 / I_T per node
    E_c182 = 2 * sp.pi * T0 * r ** 2 / (5 * e * w ** 2 * a ** 2)  # FND-182 as registered (band route)
    E_c_V0 = sp.simplify(E_c182.subs(w ** 2, w2))                  # with w^2 from the rod route
    ident = sp.simplify(E_c_V0 / (4 * sp.pi * V0 / (5 * e * a)))
    print(f"[sms C2-C5] w^2 = kt_node/V_0 = {sp.simplify(w2)};  omega_min^2 = {sp.simplify(om2)};  E_c(V_0) = {E_c_V0}")
    print(f"[sms identity] E_c = (4 pi / 5) V_0 / (e a) exactly (ratio {ident}): the breakdown field is the well depth per node over the charge times the spacing, times 4 pi/5. FND-182's unpinned w is the same unknown as V_0.")
    # dimensional check (B-2) with SI unit symbols
    J, m, Cc, s = sp.symbols('J m C s', positive=True)
    dims = {T0: J / m, a: m, r: m, c: m / s, e: Cc, V0: J}
    E_dim = sp.simplify(E_c_V0.subs(dims)); om_dim = sp.simplify(sp.sqrt(om2.subs(dims)))
    ok = sp.simplify(E_dim / (J / (Cc * m))).is_number and sp.simplify(om_dim * s) == 1
    print(f"[sms B-2] E_c dimensions {E_dim} (J/(C m) = V/m up to the numeric factor: {sp.simplify(E_dim/(J/(Cc*m))).is_number}); omega_min dimensions {om_dim} (1/s: {sp.simplify(om_dim*s) == 1}); w^2 dimensionless: {sp.simplify(w2.subs(dims)).is_number}")
    print(f"[sms note] two registered twist stiffnesses per node: rod route T0 r^2/(2a) (GRV-073) and band route T0 r^2/(5a) (FND-MATTER-047, used by FND-182); ratio 2.5, both registered, both carried.")
    return ok


def displays():
    rows = []
    print(f"[sms display] the registered w bracket [0.8, 2.8] mapped to V_0 per node, the twist gap and E_c (hbar imported for the eV line):")
    for lab, T0, a in SETS:
        for route, kfac in (('rod', 0.5), ('band', 0.2)):
            kt = kfac * T0 * R ** 2 / a
            for w in (0.8, 2.8):
                V0 = kt / w ** 2; I_T_node = (T0 / C ** 2) * R ** 2 * a
                om = np.sqrt(V0 / I_T_node); Ec = 4 * np.pi * V0 / (5 * E * a)
                rows.append((lab, route, w, V0, om, HBAR * om / E, Ec))
                print(f"[sms display]   {lab:14s} {route:4s} w {w:3.1f}: V_0 {V0:.2e} J ({V0 / E:.3f} eV/node)  omega_min {om:.2e} rad/s  hbar omega {HBAR * om / E / 1e9:.2f} GeV  E_c {Ec:.2e} V/m")
    print(f"[sms display] V_0 per node that would put E_c at the laser record / at Schwinger (kappa_pack 1): {5 * E * 6.0e-17 * E_LASER / (4 * np.pi):.2e} J ({5 * 6.0e-17 * E_LASER / (4 * np.pi):.3f} eV) / {5 * E * 6.0e-17 * E_SCHW / (4 * np.pi):.2e} J ({5 * 6.0e-17 * E_SCHW / (4 * np.pi):.1f} eV); against T0 a = {434.0 * 6.0e-17 / E:.1e} eV per node of tension energy")
    return rows


def main():
    ok = chain(); rows = displays()
    print("[sms C1] REFUSED under B-1: A_c and sigma of the contact law are symbolic in EM-RECON-023 (no registered joules or metres); FND-KIN-005's plateau is a 13.6 eV-calibrated atomic mode overlap, not the vacuum crossing; no registered coarse crossing density per node. V_0 stays a symbol.")
    print("[sms VERDICT] MASS-SCALE-UNDETERMINED: the chain is exact and dimensionally checked; the missing registered inputs are A_c (J), sigma (m) and the crossings per node of the coarse weave.")
    np.savez(OUT, b2_ok=ok, rows=np.array(rows, dtype=object), verdict='MASS-SCALE-UNDETERMINED'); print(f"[sms] sealed -> {OUT.name}")


if __name__ == '__main__':
    main()
