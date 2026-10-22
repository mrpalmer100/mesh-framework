# COMMISSION ELEC-G-2 -- A CONDITIONAL SECOND-MOMENT DIAGNOSTIC OF THE COMMITTED TERMINUS (ITS "g_mech" UNDER TWO NAMED, UNREGISTERED CURRENT LAWS)
# (CHARTER for the lab's lock; drafted 2026-10-21 from the author's draft analysis/ELEC_G_2_charter_DRAFT.md; successor to
# ELEC-G-1, parked at analysis/queue/parked/ELEC_G_1_charter_DRAFT.md, whose physics passed review and which was withdrawn
# on harness defects alone. This charter binds the harness to benchmarks/lab/_kit/labkit.py.)

## 0. What this commission is, in the programme's own terms

North Star target: the "Strength of magnets" row of docs/NORTH_STAR.md section 2, whose "Blocked by" cell names the
electron model ("the ELEC sector contributes nothing at any census tier", ELEC-062/064; the spin-axis identification was
falsified, ELEC-099/100). This commission computes one dimensionless number of the committed electron configuration: the
ratio of two second moments (charge and energy) of the solution's own densities, which equals a gyromagnetic ratio ONLY
under two additional current-law assumptions named in section 1a (and written g_mech in the code, as notation; it is
conditional throughout). It is a **conditional second-moment diagnostic**. It does NOT establish the terminus's own
mechanical magnetic moment, does NOT derive or test a charge current or an energy flux, and does NOT discharge either
flag on the face of Gate 2b (docs/commissions/SYNC_STATE.md; ALPHA-DE-CHAIN): at most a form names a number that a
later, properly derived current-law commission would have to reproduce. It retires no input and moves no row of the five
numbers (docs/NORTH_STAR.md section 2b): **interior work on a target-facing row**. By section 5(c) it arms a
discriminator: what the second-moment ratio of the committed solution is, against the values 2, 2.0023193, 1 and 2 pi,
before any registered current law exists to turn it into a moment.

## 1a. The two current laws are ASSUMPTIONS, not registered (external objection 1)

Registered: FND-006 (mu = T / c^2, the mass density of a pattern in the one-metric medium) and EM-019 (the inertial term
is forced as a rate of change of a gauge label; there are no material points, FND-REL-002, and EM-019's own locked bars
rule out the material-velocity shortcut). Neither registers an energy flux epsilon Omega r or a charge current rho_q
Omega r for this pattern, and neither registers an angular-momentum current or a stress contribution to L or mu. The
ratio of Q1 is the gyromagnetic ratio only if, additionally:
  CL1  the momentum density is the energy density carried round at the solver's phase rate: energy flux = epsilon Omega r
       (azimuthal), so L = (Omega / c^2) Int epsilon r^2 dA, with no stress or field-angular-momentum term;
  CL2  the charge current is rho_q Omega r (azimuthal), so mu = (Omega / 2) Int rho_q r^2 dA.
Both are assumptions of this diagnostic and the verdict is conditional on them. In the solver's units (c = 1) Omega x* = pi,
so a literal material rotation at Omega would exceed c for r > x* / pi (the registered radius R* = x* is 3.14 times
that); and a phase rotation of a pattern does not by itself imply advection of energy or charge. That is a stated reason
CL1 and CL2 may be false for this pattern. The diagnostic does not test them and no form says they hold; Omega and c
cancel in the ratio, so the number is the same whatever the sub- or superluminal reading, which is why it is a
second-moment ratio first and a gyromagnetic ratio only conditionally.

## 1. The question

Q1 THE RATIO (conditional on CL1 and CL2 of section 1a). For the committed terminus at its registered Omega, with energy density epsilon(r) from the
solution (elastic plus rotational) and charge density rho_q(r) under each of the two registered readings (A, the
R-geometry: charge concentrated at the edge R*; B, profile-weighted: rho_q proportional to f(r)^2, the first flagged
refinement), what is

    g_mech = (mu / L)(2 m / q),  mu = (Omega / 2) Int rho_q r^2 dA,  L = (Omega / c^2) Int epsilon r^2 dA,
    m = (1 / c^2) Int epsilon dA,  q = Int rho_q dA,

with the momentum density taken as energy flux over c^2 (FND-006 for mu = T / c^2; EM-019 for the inertial term; the
flux itself being CL1, an assumption)? With Omega constant Omega and c cancel and g_mech = <r^2>_q / <r^2>_epsilon, a pure
ratio of two second moments in one measure; it cannot be fitted. What is scored is that ratio.

Q2 THE FACTOR. If g_mech is not 2, by what factor does it miss, and does that factor match one of the Gate-1 recording
candidates? Reported as a number (F = g_mech / 2 per reading, matched against the locked list in section 5); no factor is
applied. Q2 has no form token.

## 2. Parts list (every input cited; no others enter)

| Input | Source | How it enters |
|---|---|---|
| The committed solution: EL-BVP at k/T0 = 2, Omega = pi / x*, x* = e^(pi^2) = 19333.7, J = J_T | explorations/w_dressing_phase1c.py, solve_el(); ALPHA-DE-CHAIN (Commissions T to Z; D_E = 1.1051029) | five solves of the solver's own solve_el, unchanged; arrays sealed |
| R* = pi lambda-bar_C, which is x* in the solver's units; winding q = 1 | ALPHA-DE-CHAIN (U's closure, Z brick 4); GRV-020 corollary 1 (winding = charge) | reading A: <r^2>_q = x*^2 with unit charge |
| Momentum density = energy flux / c^2, with energy flux = epsilon Omega r and charge current = rho_q Omega r | FND-006 (mu = T / c^2) and EM-019 for the inertial term only; the two fluxes are ASSUMPTIONS CL1, CL2 (section 1a), not registered | L = (Omega / c^2) Int epsilon r^2 dA, mu = (Omega / 2) Int rho_q r^2 dA, conditional |
| Energy density epsilon = elastic + rotational | the solver's elastic_density(g2, k) with g2 = f'^2 + (f/r)^2, plus 0.5 Omega^2 f^2 | the reading; the author's locked definition |
| 3D reading of the 2D solution | ELEC-074 (hollow hard-cored profile), ELEC-091 (azimuthal boundary tangent) | only as context: moments are taken in the solver's own 2D measure dA = 2 pi r dr, which is what the chain's J and D_E used; a 3D re-weighting is OUT |
| Harness | benchmarks/lab/_kit/labkit.py | Driver, Verdict, seals, manifest, halts, one-shot rendering |

Forbidden to the driver: the measured electron g and moment, alpha, the Schwinger term, mu_B as a number. The one
comparison value that is not a registered number, 2.00231930, is written in the verdict script's `decide` function only
(the last step, after every number is computed) and in no CONFIG. The values 2, 1 and 2 pi are the locked targets.
No recording factor, rectification factor, equipartition 1/2, or any constant derived for the alpha observable is applied
to mu or L. The charge density is not adjusted; the two readings are those the record names and a third is not invented.
Nothing about the outcome is predicted by the author, the drafting worker or the lab.

## 3. Scope (hard boundary)

One solution, one rotation rate, two charge readings, rigid rotation (the solver's own ansatz), the solver's 2D measure,
the current laws CL1 and CL2 as assumptions. OUT: any derivation or test of CL1, CL2, an angular-momentum current or a
stress contribution; any statement that the result is the terminus's own mechanical moment; any statement on Gate 2b's
flags beyond naming a number; the 3D re-weighting of ELEC-074's profile; the radiative sector; any statement about spin statistics or the
transport law (QB-025, QB-031); a derivation of the recording factor (if Q2 names one, that is a successor derivation
commission). The solution domain is [r_min, x*] with r_min in {1e-3, 3e-4, 1e-4}; moments exclude r < r_min, which D2 tests.

## 4. Design commitments (locked at lock; every number is in CONFIG in benchmarks/lab/elec_g_2/driver.py)

D1. THE MOMENTS. From the solution's sealed arrays (mesh r, f, f'): the dense profile is the cubic Hermite spline through
(r, f, f') (the form of solve_bvp's own interpolant); every integral is composite 5-point Gauss-Legendre per mesh
interval on it in dA = 2 pi r dr. E = Int epsilon dA; <r^2>_epsilon = Int epsilon r^2 dA / E; reading A: <r^2>_q = x*^2
(unit charge; x* is checked equal to the sealed outer mesh point to 1e-12 relative); reading B: <r^2>_q = Int f^2 r^2 dA /
Int f^2 dA. g_mech(A) and g_mech(B) are assembled from mu, L, m, q as in Q1 (so Omega and c are carried and shown to
cancel). The scored g is the adjudicating run's, full epsilon. Reported as sensitivities, with no role in any form:
epsilon with the rotational density excluded (elastic only), and epsilon as in the chain's D_E numerator, elastic +
rotational - f^2/(2 r^2) (the LOG subtraction, ALPHA-DE-CHAIN). These two are disclosed because the energy functional
that defines "the mass" is a registered choice the chain itself discusses; the commission scores the author's
locked definition only.

D2. CONVERGENCE. The chain's five (r_min, tol) cells are run: (1e-3, 1e-10) first (the adjudicating run), then (1e-3, 1e-6),
(1e-3, 1e-8), (1e-4, 1e-8), (3e-4, 1e-8). The order differs from the chain's printed order only so that the validation run
is first. FLOOR RULE (objection 3): for each scored g (g_A and g_B, full epsilon), the ABSOLUTE range max - min across
the five runs must be at most 1e-5 (CONFIG d2_tol_abs; the same number in the driver CONFIG, which the verdict imports,
and in this text), else NO-CALL. The earlier relative 1e-5 rule is removed: it did not give a uniform absolute floor.

D3. THRESHOLDS, fixed from the structure of the question and not from any computed number: a form fires when
|g_mech - value| <= 5e-4 (absolute). The radiative term is 2.3e-3 in absolute g, so the band separates "exactly 2" from the
measured value, and both from 1 and 2 pi; the verdict halts if any two target bands overlap.

## 5. Validation (halt-grade; a failure is NO-CALL)

v1. The solver reproduces the chain's D_E = 1.1051029 to 1e-6 absolute on the adjudicating run (D_E recomputed with the
solver's own formulas from the sealed arrays; the chain's printed value for this cell is 1.1051026, 3e-7 from the
1.1051029 target, inside the bar, so the bar is met by the record's own number and a failure would mean the committed solution has drifted).
v2. J = Omega * (the solver's own cumulant of Int f^2 dA) reproduces J_T to 1e-8 relative on all five runs; and the
production quadrature of Int f^2 dA on the adjudicating run agrees with that cumulant to 1e-6 relative (v2b: the moment
path integrates at the solver's own accuracy; the other four cells are not held to v2b because their BVP tolerance is
looser, D2 is their test).
v3. THE PRODUCTION MOMENT PATH on closed forms, run first (unit `credential`) and re-run in the verdict: three
synthetic (r, f, f') arrays on a geometric grid of 2001 points on [1e-3, R], passed through THE SAME functions that
score g (dense profile, spline, quadrature, g assembly): (i) f = r on [1e-3, 7] with the physical epsilon (then
g2 = 2, epsilon = e0 + 0.5 Omega^2 r^2 exactly, <r^2>_f2 = 2 R^2 / 3 in the continuum limit; here on [1e-3, 7]);
(ii) f = r + 0.1 r^3 with the test density f^2 + 0.5 f'^2 (a two-term profile; exercises the derivative path);
(iii) f = exp(-r^2 / 2) on [1e-3, 8] with the same test density (closed form by incomplete-gamma antiderivatives; the
f^2-weighted <r^2> is 1 on [0, infinity)). Returned <r^2>_epsilon, <r^2>_q(B), g_A, g_B and the mu/L/m/q assembly must
agree with the closed forms to 1e-8 relative. The bar is derived in the driver docstring from the grid spacing and the
Hermite and Gauss-Legendre error orders (cases (i) and (ii) are exact in exact arithmetic; (iii) is below 3e-9
by the interpolation bound), not tuned. A uniform-density control that cannot fail is not used.
v4. FRESH PATTERN: every number comes from a fresh solve in this commission; the arrays are sealed before any moment is
taken (the `moments` unit reads only seals; the verdict recomputes from the seals and checks the driver's record to 1e-12).

Floor test. Before any outcome is scored, D2 shows the number is above the numerical floor: each scored g has an absolute
range across five different mesh cutoffs and tolerances of at most 1e-5, which is exactly 50 times below the 5e-4 band
half-width at every value of g (the verdict prints the ratio band / range as a check). If it does not, the answer is
NO-CALL and nothing is scored. The smoke fixture (tolerances up to 1e-4) is not held to this floor; smoke reports D2 and
does not enforce it, and no fixture number is quoted.

## 6. Forms (exhaustive and exclusive; the verdict script prints `FORM (Q1): <TOKEN> -- <reason>`)

ALL FOUR targets (2, 2.00231930, 1, 2 pi) are tested for BOTH readings (A and B); the bands (half-width 5e-4) cannot
overlap, so each reading has at most one outcome o_A, o_B in {2, 2.0023193, 1, 2 pi, none}. Every printed reason states
both outcomes. The form is a function of the pair (o_A, o_B) only:
  both readings hit the same target -> that target's form; neither hits any target -> G-OTHER; any other pair (two
  different targets, or one hit against one miss) -> UNDERSPECIFIED; D2 or a validation bar fails -> NO-CALL.

  G-DIRAC        o_A = o_B = 2 (both |g - 2| <= 5e-4). The second-moment ratio is 2 under both charge readings. Under CL1
                 and CL2 it would be Dirac's value with no imported factor. Establishes: a number that a later commission
                 deriving the current laws from registered claims would have to reproduce, and that the 1/pi transfer of
                 Gate 2b is not needed for THIS ratio. Does NOT establish: that CL1 or CL2 hold, that the 1/pi is derived,
                 that either Gate 2b flag is discharged, that the electron is built, spin statistics, the radiative term,
                 or robustness to the other energy functional (sensitivity lines are printed).
  G-MEASURED     o_A = o_B = 2.00231930. The ratio lands on the measured value under both readings: a numerical coincidence at
                 band 5e-4, with the comparison line the only place the number entered. Establishes nothing about the
                 radiative term until a mechanism is named; by itself it is not evidence for the rope model.
  G-CLASSICAL    o_A = o_B = 1. Charge and energy second moments coincide in this solution under both readings (ratio 1). Says
                 nothing about the spin's moment (no identification of the terminus's circulation with the spin is made or
                 tested); under CL1 and CL2 it would be the classical orbital ratio.
  G-PI-DIRAC     o_A = o_B = 2 pi. The second-moment ratio is 2 pi under both readings; under CL1 and CL2 the record's
                 "pi mu_B" would be reproduced and the Dirac value would need a factor of pi, the successor derivation's
                 target and not a result.
  G-OTHER        o_A = o_B = none: neither reading is within 5e-4 of ANY of the four targets (all four were tested for both
                 readings). g_A and g_B are registered as numbers and Q2 is reported. A kept null only for: these two charge
                 readings, this epsilon, these four values, the 2D measure; it excludes nothing else.
  UNDERSPECIFIED (o_A, o_B) differ, including one reading hitting a target while the other misses all four, or the two
                 readings hitting two different targets. The registered inputs do not select a charge reading, and NO
                 reading's hit is promoted to a result on its own: an A-only hit of 2 does not discharge anything, and a
                 B-only hit does not either. Both outcomes and both numbers are printed and kept.
  NO-CALL        D2 fails, or v1 to v4 not all met, or any harness fault (a failed solve, a changed locked file, a
                 broken seal): the kit renders this form and the reason.

Q2 (numbers only): for each reading F = g_mech / 2 is printed and compared with the locked candidates
{pi, 1/pi, pi/2, 2/pi, 2 pi, pi/4, 4/pi}; a candidate "matches" when |F / c - 1| <= 5e-4. A match names a factor to
derive; it is not a derivation, and a non-match says the miss is something other than the listed Gate-1 factors.

## 7. Instruments and disclosures

- explorations/w_dressing_phase1c.py is the chain's own credentialed solver (D_E = 1.1051029, five configurations
  agreeing to 7 digits, ALPHA-DE-CHAIN). It ends with an unconditional main() call, so importing it would run five
  solves. The driver executes the file's source with that final call removed, in a private namespace, and wraps the
  name solve_bvp in a pass-through so the solver's own solution arrays can be sealed. No solver function is altered. The
  file's hash is in the manifest. v1 is the check that this path reproduces the chain's number.
- The moment path (dense_profile, quad_area, moments, g_assembly in the driver) is new and is credentialed by v3 before
  use.
- SMOKE (not evidence). The smoke run exercises every unit on a synthetic fixture that is not a charter cell: the same
  solver at k/T0 = 3 and x* = e^2 (the registered values are 2 and e^(pi^2)), with r_min and tol pairs not among the five
  evidence cells and a coarser L-BFGS guess grid. It writes analysis/elec_g_2_smoke.pkl only, reads nothing under data/,
  and the evidence checkpoint analysis/elec_g_2_ckpt.pkl does not exist before the run. It confirmed that the units run, that
  the verdict recomputes from the seals and agrees with the driver record to 1e-12, that v3 passes (worst relative error
  2.4e-11 against 1e-8) and that the smoke verdict prints no form token. No fixture number is quoted as a result and
  none enters any bar. No g_mech has been computed on the registered solution before this lock. A scratch probe of the
  fixture's convergence is in analysis/lab/drafts/ELEC-G-2/scratch_fixture_probe.py (fixture only).
- Disclosed: the record already contains a g = 2 reading with a transferred factor. This commission's value is that it
  computes the second-moment ratio without that factor and, conditionally on CL1 and CL2, names what a factor would have
  to be. The answer can be negative or null on any form; a clean G-OTHER or G-CLASSICAL is full credit.
- Objections of the previous review, one line each:
  objection (external, physical currents; north_star): the commission is now chartered as a conditional second-moment
  diagnostic; CL1 and CL2 are named as unregistered assumptions (section 1a), the superluminal edge (Omega x* = pi) and
  the phase-versus-advection point are stated, EM-019's rejection of the material-velocity shortcut is cited, and every
  claim that it establishes the terminus's own mechanical moment or discharges Gate 2b is removed (title, section 0, Q1,
  scope, parts list, forms).
  objection (external, forms match predicates; exhaustive_forms): all four targets are now tested for both readings; a form
  fires only when BOTH readings agree on a target; an A-only or B-only hit is UNDERSPECIFIED with both outcomes printed;
  G-OTHER fires only when neither reading hits any of the four; G-CLASSICAL no longer infers anything about the spin's
  moment; no form claims a Gate 2b flag is discharged. Implemented in verdict.py decide() and exercised on synthetic
  (g_A, g_B) pairs by analysis/lab/drafts/ELEC-G-2/scratch_decide_probe.py (8 pairs, all as locked; fixture only).
  objection (external, floor): the relative 1e-5 rule is replaced by an absolute range cap of 1e-5 per scored g (D2),
  identical in the charter, CONFIG (d2_tol_abs) and the verdict, and the verdict prints band / range as a check.
- Other pre-lock drafting changes from the author's draft: the adjudicating run first; Q2 given a locked candidate list and match band; v2b added (the
  production quadrature against the solver's cumulant) because the production path is not the solver's own; the
  elastic-only and chain-energy sensitivities named, with no role in the forms.
- One honest limit: the scored epsilon is the author's elastic plus rotational density. The rotational part carries
  most of the energy in the chain's accounting, and the chain's own D_E subtracts a LOG self-energy term, so a hit or a
  miss is a statement about this epsilon in the solver's 2D measure, not about every registered energy functional.

## 8. Budgets

Five BVP solves of the chain's size (up to ~1.1e4 mesh nodes each) plus the L-BFGS initial guess on 6400 grid points per
solve; the moment path is seconds. cpu_hours 1, mem_gb 2, usd 0 beyond drafting and review. Results to
analysis/ELEC_G_2_results.md; verdict log analysis/ELEC-G-2_verdict.log.

```lab
commission: ELEC-G-2
target: "Strength of magnets row (the electron model): a conditional second-moment diagnostic of the committed rotating terminus (its charge-to-energy second-moment ratio, a gyromagnetic ratio only under two named unregistered current laws), computed with no factor imported from the alpha observable; names a number for a later current-law derivation, discharges nothing in Gate 2b; interior work on a target-facing row, moves none of the five numbers"
driver: benchmarks/lab/elec_g_2/driver.py
verdict_script: benchmarks/lab/elec_g_2/verdict.py
instrument: [explorations/w_dressing_phase1c.py, benchmarks/lab/_kit/labkit.py]
forms: [G-DIRAC, G-MEASURED, G-CLASSICAL, G-PI-DIRAC, G-OTHER, UNDERSPECIFIED, NO-CALL]
state: [analysis/elec_g_2_ckpt.pkl]
budget: {cpu_hours: 1, usd: 0}
mem_gb: 2
```
