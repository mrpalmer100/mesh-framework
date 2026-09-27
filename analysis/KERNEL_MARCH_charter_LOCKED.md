# COMMISSION KERNEL-MARCH -- THE ANTI-ALIGNED FAMILY MARCHED IN THE CONTINUUM
# (CHARTER, LOCKED 2026-09-16 on the author's word; before any arc point)

## Question
FND-174's handedness-selective flatness was measured on a grid-detuned
family (144x36). FND-175 shows the continuum anti-aligned object is a
resonance carrying a family of full-bar members along its kernel, reachable
by the bordered solver. Marched on the s-resolved chart with that solver:
does the anti-aligned 5/4 family stay flat through the aligned collapse
region, or collapse?

## Protocol
Chart 288x36, cell 5/4. s0 = FND-175's b = -0.10 member (RMS 6.6e-9, A2
0.0020880, om2 -1.110728). s1 = a bordered a2-pinned member at 1.02 A2
(kernel coordinate held at s0's: c^T(x - s0) = 0 with c recomputed at s0),
gated. Then the stage-2c arc march at ds 0.08, 20 points, each arc solve
BORDERED: the near-null direction c_n recomputed at each predictor state in
the (1,1) subspace (injection direction and phase partner excluded), the
constraint c_n^T (x - x_pred) = 0 (the kernel coordinate carried along the
tangent), 60 rounds. Measurements SEALED per point: A2, rate, V_pt, f_dir,
om2, RMS, closure, and the kernel coordinate step b_n = c_n^T(x_n - x_{n-1})
and sigma_n = |J c_n| / row norm (does the kernel persist along the family?).
Verdict once under C1 (the DISC corrected rule) on the 20-point profile.

## Verdict forms (LOCKED)
KM-FLAT:     20/20 gated, C1 f_dir rise < +0.15, A2_max >= 0.0053: the
             handedness-selective collapse is a CONTINUUM statement at
             two s-resolutions (FND-174 upgraded).
KM-COLLAPSE: C1 rise >= +0.15: the 144x36 flatness was a grid-detuning
             artifact; the anti-aligned family collapses too on the resolved
             chart (handedness selectivity withdrawn).
KM-SCOPE:    rise < +0.15 but A2_max < 0.0053: flat over the span reached.
KM-REFUSED:  s1 or fewer than 12 arc points gated.
Display (unsealed): b_n and sigma_n along the family; om2 vs -Om1/4;
Sigma_wave; max|v|.

## Rules
No rescue; q-sweep bars (RMS 1e-8, closure 1e-6); the bordered solver as
credentialed by KERNEL-CONT (one machine, the PC); verdict in the session;
FND-173/174/175 riders inherited.

## AMENDMENT KERNEL-MARCH-X (2026-09-17, after the 20-point verdict KM-SCOPE,
## before any extension point): the 20-point march (20/20 gated, C1 rise
## +0.0001, A2 0.0022 -> 0.0043) gains A2 at 1.10e-4 per step on 288x36 (vs
## 1.71e-4 at 144x36) and stopped short of the 0.0053 licence. Budget extended
## to 30 points (10 more at ds 0.08; ~0.0054 at this spacing), same protocol,
## same seal, same forms; the verdict re-rendered ONCE on the 30-point profile:
##   KM-FLAT (licensed): rise < +0.15, 30/30 gated, A2_max >= 0.0053
##   KM-COLLAPSE:        rise >= +0.15
##   KM-SCOPE (again):   rise < +0.15, A2_max < 0.0053
##   KM-REFUSED:         fewer than 12 gated (moot: 20 already)
## Display added: sigma along the family (the degeneracy weakened 2.7e-4 ->
## 1.6e-3 over the first 20 points; does it continue to lift?) and the amplitude
## at which sigma reaches 1e-2 (the branch becoming regular), if reached.
