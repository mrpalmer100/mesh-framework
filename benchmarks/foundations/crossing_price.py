"""COMMISSION CROSSING-PRICE (charter analysis/CROSSING_PRICE_charter_LOCKED.md, locked 2026-10-04).
D1 A_c: EM-RECON-017 names A_c/(T0 a) as 'one unregistered material ratio' with a registered LOWER BOUND from core
   survival, A_c/(T0 a) > [0.40, 0.46] (EM-RECON-018; the sqrt3 re-solve FND-068 owes moves it; carried as a bound).
   The nuclear-sector import that would fix it is a calibration 'waiting for a go' (EM-RECON-017): B-1 forbids it here.
   D1 returns a BOUND, not a number.
D2 sigma: EM-RECON-018 registers sigma_0 = w, the strand width ('surfaces interact at centre distance ~ one width').
   The STANDOFF of two crossing strands in the VACUUM weave, d/sigma, is not registered: the threshold readings
   (d0/sigma0 = 1.00 and 1.38) are for MATTER at the coverage onset (FND-070: the vacuum is NOT at threshold;
   FND-129: the fine weave is sub-threshold). D2 returns sigma = w and an unregistered d/sigma.
D3 crossings per node: three strand families (EM-RECON-018's coverage counting, FND-091's angles); a strand of one
   family crosses the two others once per spacing: n_x = 2 per node. Derived from the registered family count.
D4 the chain as a function of the two unregistered quantities, alpha_c = A_c/(T0 a) (bounded below) and d/sigma
   (unbounded), with the two-strand section's rho/sigma = rho/w in [1/4, 1/2] (two discs side by side: width 4 rho
   along the pair axis, 2 rho across; w is 'one width'). V_sec/V_line from the T-1 geometry at (d/sigma, rho/sigma).
   Then V_0 = n_x V_sec, w^2 = T0 r^2/(2 a V_0), E_c = (4 pi/5) V_0/(e a) at the three scale sets.
"""
import numpy as np, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[2]; sys.path.insert(0, str(ROOT))
from benchmarks.foundations.contact_section_t1 import V as Vsurf   # noqa: E402
OUT = ROOT / 'analysis' / 'crossing_price.npz'
E, HBAR, C, DC = 1.602e-19, 1.0546e-34, 2.998e8, 1.87e-19; R = DC / 2
SETS = [('kappa_pack 1', 434.0, 6.0e-17), ('kappa_pack 50', 1599.0, 1.63e-17), ('kappa_pack 250', 2734.0, 9.53e-18)]
E_LASER, E_SCHW = 9.1e14, 1.32e18
ALPHA_LO = 0.40          # registered lower bound on A_c/(T0 a) (EM-RECON-018, pre-sqrt3 re-solve)
NX = 2                   # crossings per node, three families


def vsec(d_over_s, rho_over_s):
    phis = np.linspace(0, 2 * np.pi, 720, endpoint=False)
    v = Vsurf(d_over_s, phis, 0.0, rho_over_s, 1.0)          # sigma = 1; A_c = 1
    return (v.max() - v.min()) / 2, v.mean()                   # V_sec, V_line in units of A_c


def main():
    print("[cp D1] A_c/(T0 a) is unregistered; registered lower bound 0.40 (core survival, EM-RECON-017/018; FND-068's sqrt3 re-solve owed). The nuclear import that would fix it is the one calibration; not spent here (B-1).")
    print("[cp D2] sigma_0 = w (EM-RECON-018); the vacuum crossing's standoff d/sigma is NOT registered (threshold readings 1.00/1.38 are for matter at the coverage onset, FND-070; the vacuum is sub-threshold, FND-129).")
    print("[cp D3] n_x = 2 crossings per node (three families, EM-RECON-018 counting; a strand crosses the two other families once per spacing).")
    print("[cp D4] chain at alpha_c = 0.40 (the bound), rho/sigma in [0.25, 0.5], as a function of the standoff d/sigma:")
    rows = []
    hdr = f"{'d/sigma':>8s} {'rho/sig':>7s} {'V_sec/A_c':>9s} | " + ' | '.join(f"{lab}: V_0(eV) w E_c(V/m)" for lab, _, _ in SETS)
    print("[cp D4] " + hdr)
    for d in (1.0, 1.38, 2.0, 3.0, 5.0, 10.0, 20.0, 50.0, 320.0):
        for rs in (0.25, 0.5):
            vs, vl = vsec(d, rs)
            cells = []
            for lab, T0, a in SETS:
                Ac = ALPHA_LO * T0 * a; V0 = NX * vs * Ac; w = np.sqrt(T0 * R ** 2 / (2 * a * V0)); Ec = 4 * np.pi * V0 / (5 * E * a)
                rows.append((d, rs, lab, vs, V0, w, Ec)); cells.append(f"{V0 / E:9.2e} {w:7.2e} {Ec:9.2e}")
            print(f"[cp D4] {d:8.2f} {rs:7.2f} {vs:9.2e} | " + ' | '.join(cells))
    # the standoff window where E_c would sit between the laser record and Schwinger, per scale set (alpha_c = 0.40, rho/sigma = 0.25)
    print("[cp D4] standoff window for a discriminator (E_c between the laser record and Schwinger), alpha_c = 0.40, rho/sigma = 0.25:")
    ds = np.linspace(1.0, 400.0, 4000)
    for lab, T0, a in SETS:
        Ec = np.array([4 * np.pi * NX * vsec(d, 0.25)[0] * ALPHA_LO * T0 * a / (5 * E * a) for d in ds])
        inwin = ds[(Ec > E_LASER) & (Ec < E_SCHW)]
        print(f"[cp D4]   {lab:14s}: d/sigma in [{inwin.min():.1f}, {inwin.max():.1f}]" if len(inwin) else f"[cp D4]   {lab}: no window")
        print(f"[cp D4]   {lab:14s}: at touching (d/sigma 1) E_c {Ec[0]:.2e} V/m, w {np.sqrt(T0 * R ** 2 / (2 * a * NX * vsec(1.0, 0.25)[0] * ALPHA_LO * T0 * a)):.2e}; at d/sigma = a/d_c = {a / DC:.0f}: E_c {4 * np.pi * NX * vsec(a / DC, 0.25)[0] * ALPHA_LO * T0 * a / (5 * E * a):.2e} V/m")
    print("[cp VERDICT] CROSSING-UNDETERMINED: D1 is a bound and D2's vacuum standoff is unregistered; E_c spans from below the laser record (crossings at the lattice spacing) to far above Schwinger (touching crossings); the discriminator reading needs the standoff in a narrow registered window that does not exist today.")
    np.savez(OUT, rows=np.array(rows, dtype=object), verdict='CROSSING-UNDETERMINED'); print(f"[cp] sealed -> {OUT.name}")


if __name__ == '__main__':
    main()
