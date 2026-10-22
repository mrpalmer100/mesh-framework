# FINE-DISP-1 PREVIEW (the executor, 2026-10-21, on the author's instruction; NOT the commission's verdict)

Sequence, for the record: the charter's forms and thresholds were committed at queue 5201dc8; this preview was run
afterwards; the charter was then amended in D1/D3 (expansion variable k p rather than k a_f) and v2 (tolerance),
both instrument facts this run exposed, and the preview is disclosed in the charter's PREVIEW section. The lab's
sealed run on the locked harness is the record.

Script: benchmarks/foundations/fine_disp_preview.py (SHIN6 inherited verbatim plus the D2 bending channel along
the three axes, kappa normalized to the engine's along-fibre stiffness). Logs: analysis/fine_disp_preview.json
(the k a_f window, superseded for the wound member) and analysis/fine_disp_preview_smallk.log (the k p window).

## The credential (straight medium, P = 1)
| kb / T0 a^2 | beta along the fibre | closed form 1/12 - kb/(T0 a^2) | difference |
|---|---|---|---|
| 0 | +0.0833333 | +0.0833333 | -4.4e-8 |
| 0.02 | +0.0633377 | +0.0633333 | +4.3e-6 |
| 0.04 | +0.0433421 | +0.0433333 | +8.7e-6 |
| 0.06 | +0.0233464 | +0.0233333 | +1.3e-5 |
| 0.07909 | +0.0042606 | +0.0042433 | +1.7e-5 |

Fit residuals 1e-10 to 1e-9. Across the fibre the straight lattice's beta is 1/12 on the axes and 1/24 on the
face diagonals (the cubic lattice's own anisotropy), with the 45 percent speed obstruction SHIN6 recorded.

## The wound adjudicating member (f = 1/5, P = 5), window k p in [0.02, 0.20]
beta_p is the coefficient per (k p)^2, p = 5 a_f the winding period; beta_f = 25 beta_p per (k a_f)^2.

| kb / T0 a_f^2 | beta_p isotropic mean | per-direction range | band split (mean) | crossings in window |
|---|---|---|---|---|
| 0 | +0.0073 (excluding the crossing) | +0.0013 to +0.0134 | about 2x to 3x between bands | one: direction (1, 0, 1), both bands, residual 5e-3 |
| 0.07909 | +0.0052 | +0.0010 to +0.0121 | about 2x to 3x between bands | none |

Every direction and band is positive (subluminal at the correction order). The bending sweep from 0 to the
FND-131 ceiling moves the mean by a third and does not approach zero. The phase speeds c_d spread 0.609 to 0.640
(the SHIN6 phase-spread bar 0.05, met as before). In the k a_f window of the first run the fit form fails on the
wound member (residual 1e-2, beta of either sign and order 5 per (k a_f)^2), which is the supercell's band
structure at k p of order one and is why the charter's D1/D3 were corrected to the k p variable.

## What it says, read against the forms as they stood
Not DISP-CANCELS and not DISP-NUMERIC-ZERO: no admissible kb takes |beta_iso| anywhere near the 1e-6 floor.
A / |beta_iso| is of order one and the two bands differ by a factor two to three, so the form is
DISP-ANISOTROPIC (with the DISP-FLOOR price attached), on this engine. The price at beta = 5e-3 per (k p)^2:
p sqrt(beta_p) <= 2.70e-28 m gives p <= 3.8e-27 m against the grant's minimal p <= lambda / 4 = 2.2e-22 m at
1.4 PeV, a factor 6e4 in the pitch; with a_f = p / 5 that is a_f near 8e-28 m and n_sub = (a / a_f)^2 of order
6e21 against the grant's priced 1e10. The two bands dispersing differently is dispersion birefringence at order
(k p)^2, which gamma-ray-burst polarimetry bounds more tightly than time of flight does; the charter's form names
it and the lab's run should put the number against that bound.

## Caveats the preview carries
The engine is the SHIN spring lattice, not the registered fibre operator (the charter discloses this); the
winding is the f = 1/5 member on a cubic supercell, so the anisotropy pattern includes the supercell's; the
bending channel is the executor's implementation of D2 (three axes, each triple once), credentialed on the
straight medium only. None of these would plausibly move beta_p by the eight orders the minimal pitch needs.

## Caveat added 2026-10-21 (from the lab's round-3 skeptical review of the vetoed charter)
The SHIN engine's straight cubic lattice is itself anisotropic at order (k a)^2: beta = 1/12 on the axes and 1/24
on the face diagonals (the credential table above shows it). Part of the direction dependence reported for the
wound member is therefore the engine's lattice, not the winding's; the statistic that would attribute anisotropy
to the winding is the difference against a folded straight cell of the same supercell, per direction and band,
which this preview did not compute. The wound spread in a_f units (25 beta_p: 0.025 to 0.30, twelve-fold) exceeds
the straight lattice's (0.042 to 0.106), so the conclusions that the dispersion does not cancel across the bending
box and that the pitch is priced by the bound stand; the attribution of the anisotropy and the band split to the
winding does not, and a successor on the registered fibre operator should score the difference.
