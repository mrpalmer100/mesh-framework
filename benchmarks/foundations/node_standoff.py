"""COMMISSION NODE-STANDOFF (charter analysis/NODE_STANDOFF_charter_LOCKED.md, locked 2026-10-04).
G1-G3 are reads (recorded in the results file). This script does G5's arithmetic in the only form the reads allow:
the registered weave is a NETWORK of ropes joined at nodes (FND-148: coordination z, cubic networks; FND-001: the
endpoint locking energy J = T^2/kappa = T0 a/Pi = T0 a/2 with Pi = 2, exact XY form in the DIRECTOR angle), and
strands that cross away from nodes pass through each other without interaction (rope_weave_universe; FND-KIN-005;
FND-070: the vacuum is sub-threshold). So there is no pressing crossing with a standoff to read; the only candidate
on-site orientation potential sits at the JUNCTIONS, and whether the tie locks the two-strand rope's material azimuth
(as distinct from its director) is unregistered. Display: if a junction locks the azimuth with a fraction f of its
director locking J, then V_0 = f J per node and E_c = (4 pi/5) f J/(e a) = (2 pi/5) f T0/e, independent of a.
The f that would put E_c at the laser record, at Schwinger, and in the registered coasting regime, at each scale set.
"""
import numpy as np, pathlib
OUT = pathlib.Path(__file__).resolve().parents[2] / 'analysis' / 'node_standoff.npz'
E, C, DC = 1.602e-19, 2.998e8, 1.87e-19; R = DC / 2
SETS = [('kappa_pack 1', 434.0, 6.0e-17), ('kappa_pack 50', 1599.0, 1.63e-17), ('kappa_pack 250', 2734.0, 9.53e-18)]
E_LASER, E_SCHW, PI_COUPLING = 9.1e14, 1.32e18, 2.0


def main():
    print("[ns G4] the registered weave has no pressing crossings (strands pass through each other away from nodes; the vacuum is sub-threshold); ropes are JOINED at nodes with director locking J = T0 a/Pi, Pi = 2 (FND-001, PRED-003-LOCK). 'Crossing standoff' is not a registered object; the candidate V_0 source is the junction's azimuthal locking, UNREGISTERED.")
    rows = []
    for lab, T0, a in SETS:
        J = T0 * a / PI_COUPLING
        Ec_per_f = (2 * np.pi / 5) * T0 / E                       # E_c = (2 pi/5) f T0 / e, a-independent
        f_laser, f_schw = E_LASER / Ec_per_f, E_SCHW / Ec_per_f
        kt = T0 * R ** 2 / (2 * a)
        f_w = [kt / (w * w) / J for w in (2.8, 0.8)]              # V_0 = kt/w^2 = f J
        rows.append((lab, J, Ec_per_f, f_laser, f_schw, f_w[0], f_w[1]))
        print(f"[ns G5] {lab:14s}: J = T0 a/2 = {J:.2e} J ({J / E:.2e} eV);  E_c = {Ec_per_f:.2e} x f V/m;  f at laser record {f_laser:.1e}, at Schwinger {f_schw:.1e};  coasting regime w in [0.8, 2.8] <-> f in [{f_w[0]:.1e}, {f_w[1]:.1e}];  f = 1 (full lock): E_c {Ec_per_f:.2e} V/m, w {np.sqrt(kt / J):.1e}")
    print("[ns G5] reading: a junction that locks the azimuth at O(0.1 to 1) of its director locking gives E_c of order 1e21 V/m (ABOVE QED) and a self-trapped kink (w ~ 0.003); the discriminator window and the registered coasting regime both need f of order 1e-7 to 1e-4, a locking a thousand to a million times weaker than the director's. No registered geometry supplies a fraction of that size.")
    print("[ns VERDICT] STANDOFF-UNREGISTERED: the question as chartered is ill-posed for the registered weave (no pressing crossings); restated, the on-site potential's source is the junction's azimuthal locking fraction f, unregistered; its required size for the FND-182 reading is f ~ 1e-7 to 1e-4.")
    np.savez(OUT, rows=np.array(rows, dtype=object), verdict='STANDOFF-UNREGISTERED'); print(f"[ns] sealed -> {OUT.name}")


if __name__ == '__main__':
    main()
