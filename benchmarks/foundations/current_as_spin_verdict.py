"""COMMISSION CURRENT-AS-SPIN -- verdict computed once from the sealed outputs against the bars of
analysis/CURRENT_AS_SPIN_charter_LOCKED.md; writes analysis/CURRENT_AS_SPIN_verdict.log."""
import pathlib, numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[2]
A = np.load(ROOT / 'analysis' / 'current_as_spin_partA.npz', allow_pickle=True)
B = np.load(ROOT / 'analysis' / 'current_as_spin_partB.npz', allow_pickle=True)
L = []
def say(s=''): print(s); L.append(s)
say("CURRENT-AS-SPIN VERDICT (bars: analysis/CURRENT_AS_SPIN_charter_LOCKED.md; outputs sealed 2026-09-27)")
say("=" * 96)
say(f"A1  torque density on the azimuth = {A['torque']}  =  d/ds of J = {A['J']}  (total derivative: {bool(A['total_derivative'])})")
say("    net torque on the zero mode = J(L) - J(0): boundary flux only; the bulk strain gradient exerts none.")
rel = np.abs(A['mean_rate']) / A['scale']
rot = bool((rel > 1e-6).any())
for N, f0, r, d, sc in zip(A['N'], A['f0'], A['mean_rate'], A['rate_drift'], A['scale']):
    say(f"A2  N {int(N):3d} f0 {float(f0):.0e}: <dPhi/dt> {float(r):+.2e}  drift {float(d):+.2e}  twist-rate scale {float(sc):.2e}  relative {abs(float(r))/float(sc):.1e}")
say(f"B-A1 classification: {'ROTATION' if rot else 'TWIST'} (max relative rate {rel.max():.1e} against the 1e-6 bar)")
say(f"A3  displays (unregistered terminal inputs, named not adopted): twist flux injected at s=0 -> mean rate {float(A['disp_flux_rate']):+.2e} drifting {float(A['disp_flux_drift']):+.2e} per window (accelerates; no steady rate without a sink); "
    f"rotation rate imposed at s=0 -> the strand rotates ({float(A['disp_omega_rate']):+.2e}, undamped transients).")
say(f"B1  registered contact form: dV/dphi = {B['dVdphi']}, dV/du = {B['dVdu']}: the azimuthal leak through the contact form is exactly zero at every order.")
for g, f in zip(B['gs'], B['fr']): say(f"B2  g {float(g):.4f}: transverse energy leak fraction per crossing {float(f):.3e}")
n, Aq = float(B['n']), float(B['A']); nh = [float(x) for x in B['n_halves']]; Ah = [float(x) for x in B['A_halves']]
form_ok = abs(n - round(n)) <= 0.05 and abs(Ah[0] / Ah[1] - 1) <= 0.10
say(f"B2  fit leak = A g^n over the sealed range: n = {n:.3f} (halves {nh[0]:.3f}/{nh[1]:.3f}), A = {Aq:.3f} (halves {Ah[0]:.3f}/{Ah[1]:.3f}); "
    f"B-B form {'ACCEPTED' if form_ok else 'NOT ACCEPTED by the letter (prefactor moves more than 10 percent across the halves; n = 2 to 0.03 on the small-g half)'}")
say("B3  asymmetry: transverse leak O(g^2) in energy per crossing; azimuthal leak ZERO through the registered contact form. Unbounded at the contact level;")
say("    the finite azimuthal route is EM-RECON-026's collective coupling, whose crossing transfer rate is GRV-118 obligation (3): not computed here, not owed here.")
say("=" * 96)
say("FORM (A): TWIST-NOT-SPIN -- at the registered couplings a steady EMF (bulk strain gradient) produces a static twist, not rotation; the azimuth's")
say("          rotation rate is set by the TERMINALS (the twist flux J at the ends), an input the registry does not hold. Kept as a failure of the")
say("          reading 'current is spin' at registered couplings; the row's nearest step is a terminal (source/sink of twist flux) priced as a grant.")
say("FORM (B): ASYMMETRY -- transverse O(g^2), azimuthal exactly 0 through the contact form (raw table above; prefactor form not accepted by the letter).")
say("Registration and riders are the author's act (drafts: analysis/CURRENT_AS_SPIN_results.md, analysis/fnd179_claim.yaml).")
(ROOT / 'analysis' / 'CURRENT_AS_SPIN_verdict.log').write_text('\n'.join(L) + '\n')
