# COMMISSION KERNEL-CONT -- RESULTS (2026-09-16)
Charter analysis/KERNEL_CONT_charter_LOCKED.md (locked 2026-09-12 before any sweep
point). Instrument benchmarks/foundations/kernel_continuation.py (the bordering
algorithm on the credentialed banded solver). Stage A and B executed on the
author's machines (Mac, then a Windows box; checkpoint analysis/kernel_cont_
ckpt.pkl, sealed); control c2 in the session (analysis/antialigned/kc_c2.pkl);
verdict once from the sealed record (analysis/KERNEL_CONT_verdict.log).

## VERDICT: ** KC-MEMBER **
On the s-resolved chart (288x36, cell 5/4, the S288 state that Gauss-Newton
floored at RMS 1.3e-7), the bordered continuation along the kernel gates
FULL-BAR MEMBERS at b = -0.05, -0.10, -0.20 (RMS 6.9e-9, 6.6e-9, 3.9e-9;
closure < 5e-10; pin held to 1e-7), all at exact resonance (om2 -1.110728
to -1.110730 vs -Om1/4 = -1.110721). A continuum anti-aligned member exists
as a Lyapunov-Schmidt branch of the resonance -- and not one member: a
FAMILY along the kernel coordinate.

## Controls
c1 (b = 0 reproduces the GN floor): stage A 6.15e-7 vs 6.57e-7; stage B
7.2e-8 vs 1.29e-7. The instrument adds nothing where there is no degeneracy
to remove. PASS.
c2 (an aligned member gates unchanged): the gated 4/3 waypoint-1 member
(RMS 1.9e-9) under the bordered solve at b = 0: RMS 6.5e-11, |dx|/|x|
1.7e-6, om2 shift 4e-6, GATED. PASS. Bonus reading: the smallest (1,1)-
subspace direction at the aligned member is 2.3e-2 of the row norm, against
8e-5 and 4e-5 at the two resonant states: the near-null direction is a
property of the resonance, not of the subspace or the instrument.

## The sweep
STAGE A (144x36, cell 4/3, the state GN floored at 6.6e-7): every b != 0
gated, seven of seven, RMS 1e-9 to 9e-9, in 6 to 22 rounds; om2 -1.48099
to -1.48102 (the difference frequency -Om1/3 = -1.48096). The resonance
carries a family in BOTH directions along the kernel at this resolution.
STAGE B (288x36, cell 5/4): b < 0 gates (three of three); b > 0 floors
inside the 40-round budget at 1.4x to 3x the bar (+0.2: 1.39e-8 in 32
rounds, stalled; +0.05 and +0.3: 2.9e-8 and 2.6e-8 at the budget; +0.1
stalled early at 2.7e-6). The bisection points are non-monotone (-0.167 at
1.5e-8, -0.133 at 1.9e-6 between two gated neighbours): the predictor's
jump can land in a rougher basin, and the corrector is not monotone in b.
Whether the positive side is genuinely one-sided or budget-limited is NOT
decided by this run and is recorded as open (a doubled budget or a smaller
predictor step decides it; not a rescue -- a follow-on).

## What this establishes
1. FND-173's continuum object -- the resonance -- is not empty of members:
   it carries a one-parameter family of full-bar solutions parametrized
   by the kernel coordinate. The grid-condition rider on FND-173 becomes a
   scope note (the coarse chart's detuning picked ONE member of this
   family; the family itself is continuum).
2. The anti-aligned sector is MARCHABLE in the continuum: the stage-2c arc
   protocol with the bordered solver in place of GN, b carried as a
   coordinate, can test the handedness-selective flatness (FND-174) on the
   resolved grid. That is the named next-order, KERNEL-MARCH.
3. The instrument is credentialed by this run's two controls for the class
   of problem it was built for (a single near-null direction found in the
   physical harmonic subspace). Its roughness in b (the bisection) is a
   known limitation; predictor step control is the first improvement.

## Named next-order
- KERNEL-MARCH: the anti-aligned 5/4 family marched on 288x36 with the
  bordered solver, from the b = -0.10 member, ds 0.08, 20 points, the
  ANTI-ARC forms, b reported per point. The continuum test of FND-174.
- The positive-b question (budget or one-sidedness), and the predictor
  step control.

## Process
Forms and controls before data; the omitted c2 (a driver omission, not a
charter change) executed in the session before the verdict was rendered;
no bar relaxed; the two machines each ran one job (the PC took the kernel
job after the Mac's memory pressure); verdict once.
