# COMMISSION ANTI-ARC / ANTI-ARC-X -- RESULTS (2026-09-11)
Charter analysis/ANTIARC_charter_LOCKED.md (+ the ANTI-ARC-X amendment of
2026-09-07, made after the 12-point verdict and before any extension point).
Executed on the author's laptop (benchmarks/foundations/antiarc.py, v2
launcher); sealed checkpoint analysis/antiarc_ckpt.pkl; verdict computed once
on the 20-point profile (analysis/ANTIARC_X_verdict.log; the 12-point verdict
analysis/ANTIARC_verdict.log stands as the provisional record).

## VERDICT: ** ANTI-FLAT, LICENSED **
20/20 gated (RMS 4.7e-9 to 9.9e-9, closure passing); C1 f_dir rise = +0.0172
vs +0.15; A2_max = 0.00526 >= 0.0052. The flat march COVERS the aligned
families' 144x36 collapse region (points 17 and 18 sit inside 0.0048-0.0052
with f_dir 0.7772, rate 2.143e-3, identical to the rest of the family).

## The profile (144x36, ds 0.08, from FND-173's polished member)
   rate   2.1410e-3 -> 2.1428e-3    (+0.08 pct over 20 points; the aligned 5/4
                                     family's rate fell ~30x at its collapse)
   V_pt   1.2104e-2 -> 1.2244e-2    (+1.2 pct)
   f_dir  0.7589 -> 0.7771          (rise +0.017; phase-dominated motion
                                     throughout, vs 0.11 -> 0.30 for the
                                     aligned collapse)
   om2    -1.110632 -> -1.110635    (detuning from the difference frequency
                                     -Om1/4 constant at +8.8e-5 -> +8.6e-5)
   A2 spacing 1.714e-4 per arc step (5x the aligned families')
No turn marker of any kind: no rate collapse, no V_pt jump, no f_dir rise, no
om2 drift. The family is a straight line in every sealed statistic across a
span 2.6 times the aligned profiles' length.

## What this establishes
1. THE COLLAPSE MECHANISM IS HANDEDNESS-SELECTIVE. At the same cell (5/4),
   the same grid (144x36), the same amplitude range (through 0.0052) and the
   same protocol, the aligned two-frequency family collapses (FND-163:
   f_dir rise +0.2342, rate 30x down at 54) and the anti-aligned family does
   not. Whatever produces the collapse -- the n = 17 deep tangent object,
   the winding-into-f_dir conversion of FND-152/153 -- acts on one level-2
   handedness only. The discriminator is now two-cell (4/3 collapses at 36
   but not at 54 to 0.0055; 5/4 collapses at both, displaced) AND
   two-handedness.
2. The two handedness sectors are different dynamical objects end to end:
   the anti-aligned branch is born as a linear difference-frequency
   resonance (FND-172), exists as a detuned member (FND-173), and continues
   as a phase-dominated straight family with no collapse; the aligned branch
   is born off the cell ladder and collapses.
3. Sigma_wave along the anti-aligned family: 2.5986 -> 2.6025 T0 over A2
   0.0020 -> 0.0053 (level-1-dominated, +0.15 pct; the aligned families
   ran 2.598 -> 2.609 over a shorter span). FND-139's anti-aligned corner
   is now PRICED on its object: 2.60 T0, not the ansatz bracket.
4. The superluminal excess grows more slowly here (1.007 -> 1.017 vs 1.002
   -> 1.028 on the aligned family over a narrower span): the anti-aligned
   branch adds less material speed per unit A2 -- consistent with the
   phase-dominated (low-displacement) character of its motion.
5. Not an artifact verdict; open beyond A2 0.0053. The extension was
   chartered exactly to avoid the GR54 mistake and the licence was set
   before the extension ran.

## Named next-order
- The same march at 144x54 (the anti-aligned analogue of GR54): does the
  refined grid keep the family flat where it displaced the aligned collapse?
  Cheap (the 54 pattern is cached; ~3 h locally).
- The mechanism question sharpened: what in the aligned sector's dynamics
  couples to the collapse and is absent in the anti-aligned sector? The
  f_dir contrast (0.11 rising to 0.30 vs 0.77 flat) says the aligned family
  converts arclength into phase motion only at collapse while the anti-
  aligned family lives in phase motion from the start -- a candidate
  discriminating variable for the second-order coupling commission.

## Process
Forms locked before data at both stages (12-point charter; 20-point
amendment with the licence condition stated before any extension point);
seal held; verdict computed once per stage; the provisional verdict kept.
The resumed run stalled twice for a launcher defect (the loop read an old
terminal line; fixed in go.sh/run_local.sh) -- no effect on the physics.
