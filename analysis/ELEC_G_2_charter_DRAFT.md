# COMMISSION ELEC-G-2 -- THE GYROMAGNETIC RATIO OF THE COMMITTED TERMINUS FROM ITS OWN MOTION
# (CHARTER, the author's DRAFT for the lab's lock, 2026-10-21; the successor to ELEC-G-1, whose physics passed the
# skeptical review in rounds 2 and 3 and which was withdrawn on harness defects alone; this draft binds the
# harness to benchmarks/lab/_kit/labkit.py and fixes the round-1 control-leg objection; a measurement on the
# registered electron solution; the measured electron moment, alpha and the Schwinger term are out of the room
# until the verdict's last line)

## WHERE IT STANDS (the honest sentence, before the question)
The electron sector has a committed configuration: the rotating winding terminus of the alpha chain (ALPHA-DE-
CHAIN, Commissions T to Z; the EL-BVP solution of explorations/w_dressing_phase1c.py on the registered low
branch k / T0 = 2, rotating at Omega = pi / x* with x* = e^{pi^2}, radius R* = pi lambda-bar_C, winding q = 1),
with ELEC-074's hollow hard-cored radial profile and ELEC-091's azimuthal boundary tangent as its 3D reading.
On 6 August 2026 (Gate 2b, docs/commissions/SYNC_STATE.md) the chain reported a magnetic moment of pi mu_B
"mechanically" from a current-loop formula with the charge concentrated at the edge, converted to exactly 1 mu_B,
the Dirac value g = 2, by the Gate-1 "rectified recording" factor 1 / pi carried over from the alpha observable,
with two flags on its face: the profile-weighted moment integral was not computed, and the 1 / pi (with its
internal equipartition 1 / 2) was transferred, not re-derived on the moment. The record calls g = 2 a byproduct
and quotes it with restraint. ELEC-100's audit says spin in the corpus is carried by the internal azimuth and
the spinor transport law, not by a geometric axis, so the rotational-behaviour half of "spin one-half" has its
own derived machinery (QB-025, QB-031); what has NOT been done is the mechanical half: the ratio of the
configuration's magnetic moment to its angular momentum, both computed from the same motion, with no factor
imported from any other observable. That ratio is dimensionless, cannot be fitted, and both of its classical
values are informative. This commission computes it.

## THE QUESTION
  Q1  THE RATIO. For the committed terminus rotating rigidly at its registered Omega, with its energy density
      epsilon(r) from the solution (elastic plus rotational) and its charge density rho_q(r) under each of the
      two registered readings (R-geometry: edge-concentrated at R*; profile-weighted: proportional to f(r)^2,
      the first flagged refinement), what is
          g_mech = (mu / L) (2 m / q),   mu = (Omega / 2) Int rho_q r^2 dA,   L = (Omega / c^2) Int epsilon r^2 dA,
          m = (1 / c^2) Int epsilon dA,   q = Int rho_q dA,
      the momentum density of a pattern in the one-metric medium being its energy flux over c^2 (FND-006,
      mu = T / c^2; EM-019, the inertial term), so that for rigid rotation g_mech = <r^2>_q / <r^2>_epsilon?
  Q2  THE FACTOR. If g_mech is not 2 under either reading, by what factor does it miss, and is that factor the
      Gate-1 recording factor (pi, or pi with its 1 / 2) or something else? Reported as a number; no factor is
      applied.

## WHAT IS GIVEN (registered inputs; no others enter)
- The committed solution: explorations/w_dressing_phase1c.py solve_el() at k / T0 = 2, r_min = 1e-3, tol
  1e-10 (the chain's adjudicating run), its profile f(r), slope f'(r), elastic density and rotational density
  0.5 Omega^2 f^2, on its own grid; the normalization J = J_T as the solver imposes it (read, not re-derived).
- ALPHA-DE-CHAIN: R* = pi lambda-bar_C; q = 1 (Z brick 4); the R-geometry charge reading (edge at R*).
- FND-006 and EM-019 for the momentum density; GRV-020 corollary 1 (winding = charge) for q.
- ELEC-074 / ELEC-091 only as the 3D reading of the 2D solution: the moments are taken in the solver's own
  2D measure dA = 2 pi r dr, which is what the chain's J and D_E used; a 3D re-weighting is OUT (named below).

## WHAT IS NOT ASSUMED, AND WHAT IS FORBIDDEN
No recording factor, rectification factor, equipartition 1 / 2, or any constant derived for the alpha
observable is applied to mu or to L. The measured electron g, mu_e, alpha, the Schwinger term, mu_B as a
number: forbidden to the driver; the verdict script loads the comparison values in its last unit only. The
charge density is not adjusted; the two readings are the two the record names, and a third is not invented.
Nothing about the outcome is predicted by the author, the executor or the lab.

## SCOPE (hard boundary)
One solution, one rotation rate, two charge readings, rigid rotation (the solver's own ansatz). OUT: the 3D
re-weighting of ELEC-074's profile; the radiative sector; any statement about spin statistics or the transport
law; a derivation of the recording factor (if Q2 names one, that is a successor derivation commission).

## DESIGN COMMITMENTS (locked at lock)
D1. THE MOMENTS. From the solution's arrays: E = Int epsilon dA; <r^2>_epsilon = Int epsilon r^2 dA / E;
    reading A: <r^2>_q = R*^2 with R* the solver's outer radius x* in its units (the R-geometry);
    reading B: <r^2>_q = Int f^2 r^2 dA / Int f^2 dA. g_mech(A), g_mech(B). Also reported: the same with the
    rotational density excluded from epsilon (elastic only), as a sensitivity, not a reading.
D2. CONVERGENCE: the chain's five (r_min, tol) runs repeated; g_mech must agree across them to 1e-5 relative,
    else NO-CALL.
D3. THRESHOLDS, fixed here from the structure of the question and not from any computed number: a form fires
    when |g_mech - value| <= 5e-4 (the radiative term is 2.3e-3 in absolute g, so 5e-4 separates "exactly 2"
    from "the measured value" and both from "pi times 2").

## HARNESS (binding; what ELEC-G-1 lacked)
The driver and the verdict script are built on benchmarks/lab/_kit/labkit.py (Driver / Verdict; README and the
example pair). Units in order: credential (v1 to v4 on the production moment path, sealed), solve (the five
(r_min, tol) runs, each solution's arrays sealed with the solver's success flag and status, a failed solve a HALT),
moments (every moment and every g from the sealed arrays only, all five runs collected before any is published),
with the verdict's form_rule recomputing the moments from the seals, checking the driver's record to 1e-12, and
deciding the form before any number is printed. The kit supplies the fail-closed validation, the halt-to-NO-CALL
path, the one-shot rendering and the smoke separation; the draft does not reimplement them. CONFIG (one dict in
the driver, imported by the verdict) holds every locked number in this charter.

## VALIDATION BARS (halt-grade; run first, sealed before the moments)
v1. The solver reproduces the chain's D_E = 1.1051029 to 1e-6 on the adjudicating run (the solution is the
    committed one, not a drift of it).
v2. J = Omega Int f^2 dA reproduces J_T to 1e-8 (the normalization is the solver's).
v3. THE PRODUCTION MOMENT PATH on closed forms: synthetic (r, f, f') arrays from profiles whose f^2-weighted and
    energy-weighted <r^2> are known in closed form (f = r on [0, R]: <r^2>_f2 = 2 R^2 / 3 under dA = 2 pi r dr;
    f = exp(-r^2 / 2): <r^2>_f2 = 1; and a two-term profile whose two moments differ by a known ratio) are passed
    through THE SAME functions that produce the scored g (the dense profile, the spline, the moment quadrature
    and the g assembly), and the returned g_A, g_B, <r^2>_q and <r^2>_epsilon agree with the closed forms to
    1e-8 (the spline and quadrature truncation on these grids; the bar is derived in the driver docstring from
    the grid spacing, not tuned). A uniform-density control that cannot fail is not a control and is not used.
v4. FRESH PATTERN: every number from a fresh solve; the checkpoint seals the arrays before any moment is taken.

## FORMS (exhaustive)
  G-DIRAC        |g_mech - 2| <= 5e-4 under reading A or B (the reading named): the mechanical ratio is Dirac's
                 with no imported factor; Gate 2b's two flags discharge.
  G-MEASURED     |g_mech - 2.00231930| <= 5e-4 under either reading: the mechanical ratio lands on the measured
                 value, which would mean the radiative term is in the geometry; registered as such with the
                 reading named and the verdict's comparison line disclosed as the only place the number entered.
  G-CLASSICAL    |g_mech - 1| <= 5e-4 under the reading the record uses (A): charge and energy share a radius;
                 the terminus's circulation is not the spin's moment.
  G-PI-DIRAC     |g_mech - 2 pi| <= 5e-4 under reading A: the record's "pi mu_B" is reproduced and the Dirac
                 value needs the Gate-1 factor, which is then the successor derivation's target, not a result.
  G-OTHER        None of the above under either reading: g_mech registered as a number with both readings.
  UNDERSPECIFIED The registered inputs do not fix epsilon or rho_q to the precision D3 needs (the missing item
                 named: for instance the 3D reading changes <r^2>_q by more than 5e-4 relative and no claim
                 selects it).
  NO-CALL        D2 fails, or v1 to v4 not all met.

## SMOKE DISCIPLINE (binding on the drafting worker)
LAB_SMOKE=1 runs v3 and a coarse solve (r_min 1e-3, tol 1e-6) and prints the bars, no g; the full run does the
five solves. One unit per invocation (credential; solves; moments; verdict), atomic checkpoint, one FORM, a
second rendering refused.

## BUDGETS AND DISCLOSURES
Five BVP solves of the chain's size, minutes each; cpu_hours 1; mem_gb 2; usd 0 beyond drafting and review.
Disclosed: the record already contains a g = 2 reading with a transferred factor; this commission's value is
that it computes the ratio without the factor and names what the factor would have to be. Results to
analysis/ELEC_G_2_results.md.

```lab
commission: ELEC-G-2
target: "Electron sector (STATE_OF_THE_PROGRAMME: contributes nothing at any prediction tier): the gyromagnetic ratio of the committed rotating terminus computed from its own energy and charge densities with no factor imported from the alpha observable; discharges or names Gate 2b's two flags; arms the electron row's first dimensionless confrontation; moves no number in section 2b"
driver: benchmarks/lab/elec_g_2/driver.py
verdict_script: benchmarks/lab/elec_g_2/verdict.py
instrument:
  - explorations/w_dressing_phase1c.py
  - benchmarks/lab/_kit/labkit.py
forms: [G-DIRAC, G-MEASURED, G-CLASSICAL, G-PI-DIRAC, G-OTHER, UNDERSPECIFIED, NO-CALL]
state: [analysis/elec_g_2_ckpt.pkl]
budget: {cpu_hours: 1, usd: 0}
mem_gb: 2
```
