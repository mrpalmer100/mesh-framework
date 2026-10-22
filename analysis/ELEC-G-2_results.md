# ELEC-G-2 results: a conditional second-moment diagnostic of the committed terminus (revision round 2)

Verdict form rendered (once, from sealed data): **G-OTHER**. Headline numbers: second-moment ratio g_A = 1.820941
(reading A) and g_B = 1.114923 (reading B); neither is within 5e-4 (absolute) of any of 2, 2.0023193, 1 or 2 pi.
Charter: analysis/ELEC-G-2_charter_LOCKED.md. Verdict log: analysis/ELEC-G-2_verdict.log.
Driver and verdict script: benchmarks/lab/elec_g_2/driver.py, benchmarks/lab/elec_g_2/verdict.py.
Status: provisional until promoted; nothing here is registered.

## 1. What was asked

Target row: "Strength of magnets" in docs/NORTH_STAR.md section 2, whose "Blocked by" cell names the unbuilt electron model.
The charter (sections 0, 1, 1a) asks for one dimensionless number of the committed rotating terminus
(EL-BVP solution of explorations/w_dressing_phase1c.py at k/T0 = 2, Omega = pi/x*, x* = e^(pi^2) = 19333.7, the
solution of ALPHA-DE-CHAIN): the ratio of two second moments in the solver's 2D measure dA = 2 pi r dr,

    g_mech = <r^2>_q / <r^2>_epsilon   (written g_mech in the code as notation),

with epsilon = elastic + rotational energy density, under two charge readings: A (charge at the edge R* = x*, so
<r^2>_q = x*^2, unit winding, GRV-020 corollary 1) and B (rho_q proportional to f^2). The ratio equals a gyromagnetic
ratio only under two assumptions that the charter names as NOT registered: CL1 (momentum density = energy density
carried round at the phase rate, no stress or field angular-momentum term) and CL2 (charge current = rho_q Omega r).
FND-006 (mu = T/c^2) and EM-019 (the inertial term as the rate of change of a gauge label; its locked bars rule out the
material-velocity shortcut) register neither flux, and Omega x* = pi means a literal rigid rotation would exceed c beyond
r = x*/pi. The result below is therefore a second-moment ratio; it is a gyromagnetic ratio only conditionally on CL1 and
CL2, which were not tested.

The question scored (Q1) was whether the ratio lands within 5e-4 (absolute) of any of the four locked values 2,
2.0023193, 1, 2 pi under each reading. Q2 (numbers only) asked how far the ratio is from 2 as a factor F = g/2. No
recording factor from the alpha observable was applied. The charter does not score any comparison with the Gate 2b
construction (docs/commissions/SYNC_STATE.md; ALPHA-DE-CHAIN), and none is made here.

## 2. What was computed

Five fresh solves with the chain's own solver, cells (r_min, tol) = (1e-3, 1e-10), (1e-3, 1e-6), (1e-3, 1e-8),
(1e-4, 1e-8), (3e-4, 1e-8); node counts 12824, 5040, 8121, 6654, 6103. Arrays were sealed before moments were taken.
Moments by cubic Hermite spline and composite 5-point Gauss-Legendre per mesh interval (charter D1).

Validation, as printed in the verdict log. The log prints v1 (through the D_E line), v2, v2b, v3 and the D2 line. It
prints no separate v4 line; that v4 (fresh solves, seals before moments, verdict recomputation agreeing with the driver
record) was met is inferred from the form not being NO-CALL, since the charter renders NO-CALL if any of v1 to v4 fails.
- v3, production moment path on three closed forms: worst relative error 2.38e-11 against the bar 1e-8.
- v1, adjudicating run: D_E = 1.1051026 against the chain's 1.1051029 (difference 3e-7, bar 1e-6).
- v2 (J against J_T): 0.0e+00 on all five runs; v2b (production quadrature against the solver's cumulant): 3.1e-15 on the
  adjudicating run (bar 1e-6).
- D2 floor: the absolute range of each scored g across the five runs is 1.42e-10 (g_A) and 8.69e-11 (g_B), against the
  charter's cap of 1e-5 on that range. The verdict line reads "against 1e-05 (band 0.0005, ratio 50)": the 50 is the band
  half-width 5e-4 divided by the cap 1e-5, not a ratio to the observed ranges. The band half-width divided by the observed
  ranges is about 3.52e6 (g_A) and 5.75e6 (g_B). This shows stability across the five tested (r_min, tol) cells of this one
  solver and the credentialed moment path. It is not a mesh-independence test and not a bound on any numerical bias the
  five cells share.

Scored numbers (adjudicating run, run 1; the other four runs agree with it within the D2 ranges above; for example the
log prints g_B = 1.114922898 in run 1 and 1.114922897 in runs 2 and 3):

| quantity | value |
|---|---|
| <r^2>_epsilon (full epsilon) | 2.052737850e+08 |
| <r^2>_q, reading B | 2.288644432e+08 |
| R*^2 = <r^2>_q, reading A | 3.737915332e+08 |
| **g_A** | **1.820941399** |
| **g_B** | **1.114922898** |

Distances from the locked Q1 targets (absolute): g_A is 0.179 below 2, 0.821 above 1 and 4.46 below 2 pi; g_B is 0.885
below 2 and 0.115 above 1. Neither reading is within 5e-4 of any of the four targets.

Q2 (numbers only). F = g/2 is 0.910470699 (A) and 0.557461449 (B). The Q2 match statistic is relative, unlike Q1's
absolute band: a candidate c matches when |F/c - 1| <= 5e-4, with c in {pi, 1/pi, pi/2, 2/pi, 2 pi, pi/4, 4/pi}. Neither
reading matches any candidate under that statistic (verdict log: "Gate-1 candidates matched within 0.0005: none" for A
and for B). Whether F equals any constant outside the list was not computed.

Sensitivities (reported as numbers only; the charter gives them no role in any form, and no target comparison is made):
with the rotational density excluded (elastic only), g_A = 2.736568 and g_B = 1.675541; with the chain's D_E-numerator
energy (elastic + rotational - f^2/(2 r^2)), g_A = 1.736300 and g_B = 1.063099. The ratio therefore moves by tens of
percent with the choice of energy functional; the scored form uses the locked epsilon only.

## 3. Verdict

Printed: `FORM (Q1): G-OTHER -- reading A: g_A = 1.820941 -> no target; reading B: g_B = 1.114923 -> no target; neither
reading within 0.0005 of any of the four targets`.

## 4. What this establishes, and what it does not

Establishes (scope: this one committed solution at k/T0 = 2; the solver's 2D measure; epsilon = elastic + rotational,
the locked definition; the two charge readings A and B; rigid rotation; the four values 2, 2.0023193, 1, 2 pi at band
5e-4). G-OTHER is a kept null only for these two charge readings, this epsilon, these four values and the 2D measure; it
excludes nothing else.
- The second-moment ratio <r^2>_q / <r^2>_epsilon is 1.8209 (A) and 1.1149 (B). Its absolute range across the five tested
  cutoff and tolerance cells is 1.42e-10 (g_A) and 8.69e-11 (g_B).
- Neither value is within 5e-4 of 2, 2.0023193, 1 or 2 pi.
- If CL1 and CL2 held with these densities and this measure, the ratio would be the gyromagnetic ratio and would read
  1.82 (A) or 1.11 (B). That is a conditional statement; CL1 and CL2 are unregistered and were not tested.

Does not establish:
- That CL1 or CL2 hold, or that they fail. No claim is made about the terminus's own mechanical magnetic moment.
- Anything about Gate 2b (docs/commissions/SYNC_STATE.md; ALPHA-DE-CHAIN): the charter rules any statement on its flags
  out of scope beyond naming a number, and no comparison with its construction was scored. This commission discharges
  neither of its flags and refutes neither.
- Anything about other energy functionals, other charge readings, a 3D re-weighting of ELEC-074's profile, the radiative
  sector, spin statistics, or the transport law (all out of scope per charter section 3). The sensitivity lines show the
  ratio depends on the energy functional.
- A derivation of any recording factor. The Q2 factors (0.9105 for A, 0.5575 for B) match no listed candidate under the
  relative 5e-4 statistic; no successor derivation target is named by this result.
- Any ordering between the two charge readings; the registered inputs do not select one.

## 5. North Star scorecard

Targets moved from blocked to derived: 0. Inputs retired: 0. None of the five numbers (docs/NORTH_STAR.md section 2b)
moves. This is interior work on a target-facing row (charter section 0). Under docs/NORTH_STAR.md section 5(c) (the
discriminator a charter arms) it arms a discriminator only in this narrow sense: two provisional diagnostic numbers
(1.8209 A, 1.1149 B) now exist for this epsilon and these readings. (The charter's own phrase "By section 5(c)" refers to
that North Star rule, not to charter section 5, which is Validation.) The numbers are provisional results of this
commission, not registered values. They constrain a later current-law derivation only if that derivation yields CL1 and
CL2 with the same densities and measure; a derivation that gives different current laws owes nothing to them. The
electron-model block on the "Strength of magnets" row stands unchanged.

## 6. Natural next question

A different question from this one, and not a rescue of it: do the registered claims (FND-006, EM-019 and the dictionary
EM-017..022) yield any charge current and momentum density for the rotating terminus at all, and if so what moment-to-
angular-momentum ratio follows from them? That is a current-law derivation commission, which would also have to face the
Omega x* = pi superluminal edge. Not chartered here.

## Review record (written by the lab)

| Stage | Reviewer | Model | Result |
|---|---|---|---|
| lock r1 | skeptical | anthropic/claude-opus-5-5 | pass |
| lock r1 | external | openai/gpt-6-astra | not passed |
| lock r2 | skeptical | anthropic/claude-opus-5-5 | pass |
| lock r2 | external | openai/gpt-6-astra | pass |
| verdict r1 | skeptical | anthropic/claude-opus-5-5 | not passed |
| verdict r1 | external | openai/gpt-6-astra | not passed |
| verdict r1 | external-second | openai/gpt-6-astra | not passed |
| verdict r1 | skeptical | anthropic/claude-opus-5-5 | not passed |
| verdict r1 | external | openai/gpt-6-astra | not passed |
| verdict r1 | external-second | openai/gpt-6-astra | not passed |
| verdict r1 | skeptical | anthropic/claude-opus-5-5 | pass |
| verdict r1 | external | openai/gpt-6-astra | pass |
| verdict r1 | external-second | openai/gpt-6-astra | pass |
