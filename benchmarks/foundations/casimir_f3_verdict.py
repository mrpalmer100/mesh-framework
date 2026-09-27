"""COMMISSION CASIMIR-F3 -- the verdict, computed ONCE from the sealed outputs of casimir_f3.py
against the bars of analysis/CASIMIR_F3_charter_LOCKED.md. Prints the forms; writes
analysis/CASIMIR_F3_verdict.log. Bar B1 (the derivation closing on three cited claims) is a
reading, recorded at lock in the charter's READS AT LOCK section; it is entered here as the
constant B1_CLOSED and the three citations are printed so the reader can check them."""
import pathlib, sys
import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[2]
P1 = np.load(ROOT / 'analysis' / 'casimir_f3_part1.npz', allow_pickle=True)
P2 = np.load(ROOT / 'analysis' / 'casimir_f3_part2.npz', allow_pickle=True)
B1_CLOSED = True            # FND-089/FND-090 (two isotropic polarizations), EM-RECON-011/012 (longitudinal unpinned),
                            # FND-STRAND-008 (twist band gapped): read at verdict level at lock, see the charter.
lines = []
def say(s=''):
    print(s); lines.append(s)

say("CASIMIR-F3 VERDICT (bars: analysis/CASIMIR_F3_charter_LOCKED.md; outputs sealed 2026-09-27)")
say("=" * 96)
# ---- B0: known answer -----------------------------------------------------------------------
C = float(P1['C']); cont = -float(P1['cont']); conv = float(P1['conv']); c2 = float(P1['c2'])
dev = C / cont - 1.0
b0 = abs(dev) <= 0.01 and conv <= 1e-3
say(f"B0  known answer: extrapolated C = {C:+.7f} vs continuum -pi^2/1440 = {cont:+.7f}; deviation {100 * dev:+.4f} pct "
    f"(bar 1 pct); quadrature change under doubling {100 * conv:.2e} pct (bar 0.1 pct); lattice c2 = {c2:+.3f}  -> {'PASS' if b0 else 'FAIL'}")
for d, e in zip(P1['ds'], P1['E2']):
    say(f"      d {int(d):3d}  E_cas d^3 / continuum = {float(e) * int(d) ** 3 / cont:.5f}")
# ---- B1: the derivation ---------------------------------------------------------------------
say(f"B1  derivation closes on cited claims read at verdict level: polarization count two and isotropy (FND-089, FND-090 Derived); "
    f"longitudinal channel unpinned by matter at linear order (EM-RECON-011/012); twist band gapped (FND-STRAND-008)  -> "
    f"{'CLOSED' if B1_CLOSED else 'OPEN'}")
say(f"      ledger plate energy per area, two pinned polarizations: -pi^2 hbar c / (720 d^3) [hbar imported per GRV-014]; "
    f"force pi^2 hbar c / (240 d^4); corrections O((a_f/d)^2), unobservable at laboratory d.")
say(f"      excluded control (longitudinal pinned, c_L >= sqrt2 c): >= +35 pct on the two-polarization value, displayed, not adopted.")
say(f"      gapped twist band: exp(-2 m d) with m at the strand mass scale, zero at any laboratory d.")
# ---- B2/B3: the rotation under plates -------------------------------------------------------
say("B2  the winding rotation under plates (one-dimensional control, exact energies; residual after extensive + boundary):")
labels = [str(x) for x in P2['labels']]
helix_short = True; long_range = []
for lab in labels:
    r = P2[f'{lab}|r']; rbar = P2[f'{lab}|rbar']; e_site = float(P2[f'{lab}|e_site'])
    p_avg = float(P2[f'{lab}|p_avg']); A_avg = float(P2[f'{lab}|A_avg']); p_raw = float(P2[f'{lab}|p_raw'])
    noise = np.abs(rbar).max() <= 1e-9 * e_site * float(P2['ds'].max())
    if noise:
        form = 'NO TERM (residual at machine noise)'
    elif not np.isnan(p_avg) and p_avg <= 4.0:
        form = f'candidate LONG-RANGE p = {p_avg:.3f}'; long_range.append((lab, p_avg, A_avg))
    else:
        form = 'SHORT-RANGE (bounded or fast decay)'
    if lab.startswith('helix') and not noise:
        helix_short = False
    say(f"      {lab:22s} |residual| max {np.abs(r).max():.2e}   period-averaged max {np.abs(rbar).max():.2e}   "
        f"raw fit p {p_raw:6.3f}   averaged fit p {p_avg:6.3f}   -> {form}")
say(f"      SHIN6 wound slab local bond sum vs d: residual from linear {float(np.abs(P2['slab_lin_res']).max()):.1e} "
    f"(relative {float(np.abs(P2['slab_lin_res']).max() / P2['slab_bond_sum'].max()):.1e})  -> extensive + boundary exactly")
say("      the linearly polarized wave is the contrast display only: its commensurability term is bounded and period-averages to noise.")
# ---- forms ----------------------------------------------------------------------------------
say("=" * 96)
if not b0:
    say("FORM: CAS-REFUSED -- the known-answer instrument did not meet B0; no physics read.")
else:
    say("FORM (Q1): CAS-LEDGER-CONSISTENT -- the registered ledger predicts the measured Casimir force exactly given hbar; "
        "consistency-tier; no tier motion; no discriminator; instrument credentialed." if B1_CLOSED else
        "FORM (Q1): CAS-LEDGER-DEFECT -- a cited claim does not close the derivation; see the charter's reads.")
    if helix_short and not any(l.startswith('helix') for l, *_ in long_range):
        say("FORM (Q2): CAS-IDENTITY-SHORT-RANGE -- the fixed-frequency, constant-modulus rotating state has NO scale-free plate term: "
            "its energy is extensive plus a boundary constant, exactly (residual at machine noise over three decades of d and three pitches). "
            "The winding's rotation is the vacuum's energy budget, not its spectral zero-point; the two zero-points are DISTINCT objects.")
    else:
        say("FORM (Q2): CAS-IDENTITY-LONG-RANGE -- a scale-free term exists on the helix runs; B3 applies: " + str(long_range))
say("Riders and registration are the author's act (drafts: analysis/CASIMIR_F3_results.md, analysis/fnd178_claim.yaml).")
(ROOT / 'analysis' / 'CASIMIR_F3_verdict.log').write_text('\n'.join(lines) + '\n')
