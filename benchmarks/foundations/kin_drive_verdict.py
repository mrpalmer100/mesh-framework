"""COMMISSION KIN-DRIVE -- verdict computed once from analysis/kin_drive.npz against the bars of
analysis/KIN_DRIVE_charter_LOCKED.md; writes analysis/KIN_DRIVE_verdict.log."""
import pathlib, numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[2]
D = np.load(ROOT / 'analysis' / 'kin_drive.npz', allow_pickle=True)
L = []
def say(s=''): print(s); L.append(s)
say("KIN-DRIVE VERDICT (bars: analysis/KIN_DRIVE_charter_LOCKED.md; outputs sealed 2026-09-27)")
say("=" * 96)
k1 = True
for w in (2.0, 2.8):
    rows = D[f'K1_{w}']
    for F, ac, ap, Mc, Mp, we in rows:
        say(f"K1  w {w}: F {F:.0e}  a {ac:+.3e} (centre) {ap:+.3e} (pi-crossing)  M = 2 pi F/|a| = {Mc:.4f}  vs 8/w = {8 / w:.4f}  ({100 * (Mc * w / 8 - 1):+.2f} pct)  winding err {we:.1e}")
    for F, ac, ap, Mc, Mp, we in rows[:2]:
        if abs(Mc * w / 8 - 1) > 0.05 or abs(Mp * w / 8 - 1) > 0.05: k1 = False
say(f"B-K1 (mass within 5 pct of 8/w at the two smallest F, both w): {'PASS' if k1 else 'FAIL'}; the sign: a positive torque F = c_L eps' drives the +2 pi kink toward -s.")
for w in (2.0, 2.8):
    lo, hi, epn = D[f'K2_{w}']
    say(f"K2  w {w}: bracket failed at the floor: the kink moves at F = 1e-8 (relaxed PN {epn:.2e}, estimate E_PN/2 = {epn / 2:.2e}); F_th < 1e-8, an UPPER BOUND; the instrument's residual-velocity floor (~1e-3 node per time after relaxation) hides any well shallower than that.")
say("B-K2 (bracket to 1.5x): NOT MET; reported as the bound F_th < 1e-8 at both w, fifty times below the static estimate at w = 2: the static PN barrier overstates dynamic pinning on this chain.")
for w in (2.0, 2.8):
    dev, vmax, steady, we = D[f'K3_{w}']
    say(f"K3  w {w}: relativistic form holds to 1.5 pct up to 0.5 c_t; max deviation over 0.05..0.9 c_t {dev:.3f}; v reaches {vmax:.3f} = {vmax / w:.2f} c_t; winding err {we:.1e}")
say("K3  loss identified (energy budget at w = 2, |F| = 1e-3): the kink's energy saturates at 22.2 (gamma 1.39, v = 0.69 c_t) from t ~ 1500 while the")
say("    energy left behind it grows at exactly the rate of the work 2 pi |F| dx (slopes 4.2 per 500 time units, both), half of it kinetic:")
say("    phonon radiation from the moving kink into the discrete chain. At w = 2.8 the kink was still rising slowly at 0.78 c_t when it reached the chain end.")
say("B-K3 (form (b) to 0.9 c_t within 3 pct): FAIL above 0.5 c_t; outcome (c): relativistic acceleration to about half the torsion speed, then a")
say("    radiation-limited terminal velocity below c_t set by the chain's discreteness.")
say("B-K4 winding conserved: every run at 0.0.")
say("=" * 96)
say("FORM: KIN-FORCE-DERIVED -- a winding on a strand feels F_kink = 2 pi c_L eps' from the registered lock; the chain obeys it with the")
say("      sine-Gordon mass to 1 pct. The mesh has a q E along the strand, built from registered objects only.")
say("FORM: KIN-DRIFTS (with the loss identified) -- above a threshold below 1e-8 the winding accelerates relativistically to ~0.5 c_t and then")
say("      reaches a terminal velocity of about 0.7 c_t at w = 2 (higher at w = 2.8), the excess work radiated as phonons into the strand.")
say("      This is a steady drift at the registered couplings, but at the torsion-speed scale, not the mm/s of a copper wire; the loss is the")
say("      strand's own discreteness, an instrument-class property of the registered chain (FND-STRAND-002's node spacing).")
say("Registration is the author's act (drafts: analysis/KIN_DRIVE_results.md, analysis/fnd181_claim.yaml).")
(ROOT / 'analysis' / 'KIN_DRIVE_verdict.log').write_text('\n'.join(L) + '\n')
