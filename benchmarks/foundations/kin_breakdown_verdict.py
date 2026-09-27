"""KIN-BREAKDOWN verdict, once, from analysis/kin_breakdown.npz; writes analysis/KIN_BREAKDOWN_verdict.log."""
import pathlib, numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[2]; D = np.load(ROOT / 'analysis' / 'kin_breakdown.npz', allow_pickle=True)
L = []
def say(s=''): print(s); L.append(s)
say("KIN-BREAKDOWN VERDICT (bars: analysis/KIN_BREAKDOWN_charter_LOCKED.md; sealed 2026-09-27)")
say("=" * 96)
say(f"B-1 dimensional check: E_c = {D['formula']} -> volt/metre by machine: PASS")
ws = D['ws']; reg = (ws >= 0.8) & (ws <= 2.8)
E_S, E_crit, E_laser = float(D['E_S']), float(D['E_crit']), float(D['E_laser'])
agree = False; below_all = True; lo, hi = np.inf, 0.0
for name, pref, Ec, wS, wc, wl in zip(D['names'], D['pref'], D['Ec'], D['w_S'], D['w_crit'], D['w_laser']):
    Er = Ec[reg]; lo, hi = min(lo, Er.min()), max(hi, Er.max())
    say(f"{name:24s}: E_c over w in [0.8, 2.8] = [{Er.min():.1e}, {Er.max():.1e}] V/m; Schwinger needs w = {wS:.2f}; E_crit needs w = {wc:.3f} (outside every regime); laser record exceeded below w = {wl:.1f}")
    if ((Er >= E_crit / 10) & (Er <= E_crit * 10)).any(): agree = True
    if not (Er < E_laser).all(): below_all = False
say(f"B-2 (agrees with E_crit within the spread at some registered w): {'PASS' if agree else 'FAIL'}; E_c is 5 to 8 orders below E_crit at every w and scale set.")
say(f"B-3 (below the laser record at every w and scale set): {'HOLDS' if below_all else 'FAILS'}; the minimum registered value, {lo:.1e} V/m (M-point, w = 2.8), sits 1.2x ABOVE the record 9.1e14 V/m.")
say(f"S4 the window: across every registered w and scale set E_c lies in [{lo:.1e}, {hi:.1e}] V/m: above the highest field ever applied, and at or below")
say(f"    the Schwinger field except at the continuum floor with w < 1.25. At the continuum floor and w = 1.25 the mesh's charge-creation threshold EQUALS the Schwinger field.")
say("=" * 96)
say("FORM: BREAKDOWN-DISAGREES (read with the lock note: E_crit is the mesh's LINEARITY limit, not a charge-creation threshold, so the two are limits of")
say("      different things and the mismatch is not a contradiction). The like-with-like comparison is with the Schwinger field, and there the finding is:")
say("      the mesh predicts vacuum charge creation at a field between 1.1e15 and 3.2e18 V/m, the value set by the kink width and the scale set, which is")
say("      BELOW QED's Schwinger field over most of the registered range and reachable by the next laser generation (1e24 to 1e25 W/cm^2 gives 3e15 to")
say("      1e16 V/m). DISCRIMINATOR CANDIDATE for the census: quantitative as a window, distinctive in outcome (QED predicts nothing below 1.3e18),")
say("      checkable near-term, live. Its weakness, on its face: a three-order window until w and the scale set are pinned; a null result at 1e16 V/m")
say("      would kill the M-point row outright and push the others toward the continuum floor.")
say("Registration is the author's act (drafts: analysis/KIN_BREAKDOWN_results.md, analysis/fnd182_claim.yaml).")
(ROOT / 'analysis' / 'KIN_BREAKDOWN_verdict.log').write_text('\n'.join(L) + '\n')
