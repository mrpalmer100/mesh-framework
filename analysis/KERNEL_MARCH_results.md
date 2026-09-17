# COMMISSION KERNEL-MARCH / KERNEL-MARCH-X -- RESULTS (2026-09-17)
Charter analysis/KERNEL_MARCH_charter_LOCKED.md (locked 2026-09-16 before any
arc point; the KERNEL-MARCH-X amendment locked after the 20-point verdict and
before any extension point). Executed on the author's Windows box with the
bordered solver (kernel_continuation.py, credentialed by KERNEL-CONT / FND-175);
sealed checkpoint analysis/kernel_march_ckpt.pkl; verdicts once per stage
(analysis/KERNEL_MARCH_verdict.log: KM-SCOPE at 20; analysis/KERNEL_MARCH_X_
verdict.log: the 30-point verdict).

## VERDICT: ** KM-FLAT, LICENSED ** -- the handedness-selective collapse is a
## continuum statement at two s-resolutions

30/30 gated (RMS 5.9e-10 to 2.4e-9, an order of magnitude inside the bar;
closure passing; the bordered solver converging in a few rounds per point).
C1 f_dir rise = +0.0004 vs +0.15; A2_max = 0.00537 >= 0.0053; five points
(24-28) sit inside the aligned collapse window 0.0048-0.0053 with f_dir
0.6048-0.6050 and rate 1.372e-3 to 1.373e-3, indistinguishable from the rest
of the family.

## The profile (288x36, ds 0.08, from FND-175's b = -0.10 member)
   A2      0.00219 -> 0.00537   (spacing 1.10e-4 per step; the aligned
                                  families' 3.5e-5; the coarse-grid anti-
                                  aligned family's 1.7e-4)
   rate    1.3860e-3 -> 1.3716e-3  (-1.0 pct over 30 points; the aligned 5/4
                                  family's rate fell 30x at its collapse)
   V_pt    7.695e-3 -> 7.639e-3   (-0.7 pct)
   f_dir   0.6037 -> 0.6050       (the coarse chart had it at 0.76-0.78:
                                  exaggerated by the grid detuning, still
                                  phase-dominated)
   om2     exact resonance throughout: detuning -7e-6 -> -2.5e-5 from -Om1/4
   sigma   2.7e-4 -> 2.4e-3        (x8.7, smooth, monotone; 1e-2 not reached)
   b_step  ~1e-8 per point         (the family marches at fixed kernel coordinate)
No turn marker of any kind. The flattest profile the campaign has produced,
across the amplitude range where the same-handed family collapses on this
same chart family (FND-163 at 36; FND-164 displaced and sharpened at 54).

## What this establishes
1. THE COLLAPSE MECHANISM IS HANDEDNESS-SELECTIVE IN THE CONTINUUM. FND-174's
   finding was measured on a grid-detuned family; this one is measured on the
   s-resolved chart with the solver that reaches the true (resonant) object.
   Same cell, same amplitude range, same bars: the aligned family collapses,
   the anti-aligned family does not. FND-174 is upgraded; its continuum-
   status rider is discharged.
2. THE ANTI-ALIGNED BRANCH IS A RESONANCE THAT SLOWLY REGULARIZES. sigma, the
   near-null direction's residual norm, grows smoothly by a factor 8.7 over
   A2 0.0022 -> 0.0054, with no sign of saturation; extrapolated (roughly
   linear in A2 above 0.003, ~0.6e-3 per 0.001 of A2) it reaches the 1e-2
   "regular branch" level near A2 ~ 0.012. The degeneracy is exact only at
   small amplitude; at larger amplitude the branch would become GN-gateable
   without bordering. A prediction the instrument can test when the family
   is marched further.
3. THE KERNEL COORDINATE IS CONSERVED ALONG THE FAMILY: b_step ~ 1e-8 per
   point over 30 points. The family selected by b = -0.10 at A2 0.0021 is
   still the b = -0.10 family at A2 0.0054; the one-parameter freedom of
   FND-175 is a label the march carries, not a direction it wanders in.
4. The resonance's detuning grows slowly with amplitude (-7e-6 -> -2.5e-5):
   the difference-frequency law of FND-172 acquires a small second-order
   amplitude shift on the resolved chart, of the sign Q2's reduction gave
   (negative pencil root) -- recorded as a number, not identified.
5. Instrument: the bordered solver on the arc constraint delivers RMS ~6e-10
   routinely; the credentialed GN solver's floor at this resonance was
   1.3e-7. Its class is credentialed; its roughness in b (KERNEL-CONT) did
   not show in the march because the march holds b fixed.

## Named next-order
- KERNEL-MARCH-2: continue the same family to A2 ~ 0.012 (the sigma ~ 1e-2
  extrapolation) to see the branch regularize -- and whether it collapses
  after all once the degeneracy is gone (the aligned collapse happens on a
  regular branch).
- The mechanism question, now sharp: what couples the aligned sector to the
  collapse and not the anti-aligned one? The discriminating variable is
  f_dir (0.11 rising to 0.30 at collapse vs 0.60 flat), i.e. whether the
  family's motion is displacement- or phase-dominated. A charter for the
  second-order coupling.

## Process
Forms before data at both stages; the X amendment with the licence stated
before extension; seal held; verdict once per stage; the launcher's stale-
terminal-line stall (instrument, not physics) fixed in both launchers.
