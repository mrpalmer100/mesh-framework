# COMMISSION QP-HULL-1 -- THE QUASI-PERIODIC STATE ON AN INSTRUMENT WITHOUT A CELL
# (CHARTER, the author's DRAFT for the lab's lock, 2026-10-19; the successor COMPOSITE-SELECT's QB named;
# gated on an instrument credential, section GATING; nothing here has been run at q = 1.492)

## WHERE THE ARC STANDS (the honest sentence, before the question)
COMPOSITE-SELECT's Leg B rendered RAT-RESONANT at both grid densities (rho(D, N1) -0.983 and -0.956 against
rho(D, q) -0.167 and -0.257, 2026-10-19): the amplitude-growth collapse of the aligned two-frequency family
tracks the commensurability order of the rational cell the instrument imposes, not the ratio value. Cells of
order 2 and 3 collapse inside the A2 window 0.0048 to 0.0051 (9.56x, 5.31x); cells of order 5, 7 and 9 march
through the same window flat (D 1.03 to 1.06x) and stop at the protocol's budget, not at a fold. The charter's
locked consequence is that the physical branch at q = 1.492 is read from the high-order cells and that "the
anti-aliased continuum of the state becomes the next instrument question". This is that question. What is not
known: whether the quasi-periodic state at the registered ratio, on an instrument that imposes no cell, grows
without bound, saturates, folds, or collapses as a function of its level-2 amplitude alone; and whether the
collapse at 3/2 that TRUESTATE, Q-SWEEP and Q54 built on is in the quasi-periodic state at all or only in the
cell. Leg A's QA stands (COMP-PIN-UNREACHABLE, FND-169) and is not reopened: a selection principle is not what
this charter tests.

## THE MECHANISM NAMED (why a cell aliases, stated before the build so the credential can test it)
The registered instrument discretizes the state u(s, phi) on a periodic cell of length LCELL = N1 sqrt 3 in s,
holding N1 periods of level 1 (K1 = 2 pi / sqrt 3) and N2 periods of level 2 (K2 = N2 2 pi / LCELL = q K1). On
that cell a Fourier mode (m1, m2) of the two-frequency content has s-wavenumber (2 pi / LCELL)(m1 N1 + m2 N2),
so every pair of modes with equal m1 N1 + m2 N2 is the SAME grid function: (m1, m2) and (m1 + k N2, m2 - k N1)
alias. The lowest alias of the mean field (0, 0) is (N2, -N1): for 3/2 it is the (3, -2) mode, for 4/3 the
(4, -3), for 13/9 the (13, -9). A nonlinear response that feeds (N2, -N1) back onto the mean field is strong when
N1 is small and vanishes as N1 grows; that is the dependence on order and not on q which RAT-RESONANT measured.
On a two-phase (hull) representation u(theta1, theta2, phi), with theta1 = K1 s and theta2 = K2 s independent
angles, no two modes coincide for any q, rational or not, and the s-derivative is K1 d/dtheta1 + K2 d/dtheta2.
The rational cell is the restriction of the hull function to the line theta2 = q theta1 (mod 2 pi); the hull
instrument contains every registered cell as a special case and adds no operator the cell does not have.

## GATING (binding)
This charter LOCKS only after Leg 0 (the instrument credential, section VALIDATION BARS v1 to v4) is on the
record with every bar met, and after the instrument's memory footprint at the credential grid has been measured
under the lab's cap. The lock records the credential's numbers. No number at q = 1.492 is produced before the
lock. If the instrument cannot meet v1 at any grid under the cap, the commission renders INSTRUMENT-OPEN at Leg 0
and stops; that is a result about the instrument, kept.

## THE QUESTION
  Q1  THE QUASI-PERIODIC BRANCH. On the hull instrument at the registered ratio q = 1.492, marched by the
      registered protocol (level-1 recovery, ramp to the waypoints, the rate march at ds = 0.08, full-bar
      members only), what does the aligned family do as a function of A2: flat through the window and past the
      0.0063 target, collapse in rate, or fold (the march ends by the protocol's own rule before the target)?
  Q2  THE 3/2 ALIAS. On the same instrument at q = 3/2 exactly, does the collapse the cell shows (D 9.56x,
      registered) appear? If the hull at 3/2 is flat, the collapse at 3/2 was the cell's aliasing; if it
      collapses, RAT-RESONANT's reading ("an artifact of the rationalized instrument") is wrong about 3/2 and is
      corrected by name, a failure kept.
  Q3  THE PRICE (a table, not a verdict). Sigma_wave by FND-135's closed form, with the torus average in place
      of the time average, at the deepest full-bar member of Q1's march; beside the retreat 2.598 and Leg B's
      2.6069 at 13/9.

## WHAT IS GIVEN (registered inputs; no others enter a build leg)
- The stage-2 operators, stencils, pins and weights (TRUESTATE stage 2; the sparse f32-J solver, SJ-CREDENTIALED;
  the rung budgets, basin guard and acceptance ladder of the Q-SWEEP protocol), reused unchanged.
- The level-1 sector (K1, R1, <T> = 3/2, gauge), q-independent, shared.
- The registered ratio 1.492 (TRUESTATE stage-1 bars) and the registered rational cells 3/2, 4/3, 5/3, 5/4, 7/5,
  8/5, 10/7, 11/7, 13/9, 14/9 with their retained members and per-point measurements (read-only).
- D(q) as Q-SWEEP stage 1 defined it (rate at the full-bar point nearest A2 = 0.0048 over rate at the point
  nearest 0.0063; nearest-point pairing; RMS < 1e-8, closure < 1e-6); A2_max; om2 at matched A2.
- FND-135's closed-form two-level kinetic energy; Leg A's identity torus average = time average on the gated
  states (v6 there); FND-132's level-1-at-c identity.
- COMPOSITE-SELECT's Leg B record (analysis/COMPOSITE_SELECT_legB_results.md) as data, not as a bar.

## WHAT IS NOT ASSUMED
No new pin, no new weight, no new solver: the hull instrument is the registered operators acting on two phases
instead of one periodic coordinate. Nothing about the outcome at 1.492 is predicted by the author, the executor
or the lab before it is measured (the FLAT/COLLAPSE prediction game stays over). R2 = 0.09396 is not a target and
appears in no file of this commission except Q3's comparison line. The order-N1 aliasing mechanism above is a
reason to build the instrument, not a result; Q2 tests it.

## SCOPE (hard boundary)
One ratio (1.492) and one control ratio (3/2) on the hull instrument; no ladder, no sweep in q. The anti-aligned
branch is OUT. No selection principle is evaluated (QA is closed). No re-adjudication of FND-147/163/164's cell
results: Q2 reads the hull at 3/2, which is a different instrument, and the CELL-SCOPE riders of Leg B's QB
consequence (a) are the author's to grant or not, independently of this commission.

## DESIGN COMMITMENTS (locked at lock)
D1. THE INSTRUMENT: benchmarks/foundations/qp_hull.py, built BEFORE the lock and credentialed by Leg 0. State
    u(theta1, theta2, phi) with the three registered fields, periodic 2 pi in each coordinate, on a grid
    NT1 x NT2 x NP; the s-derivative operator D_s = K1 D_theta1 + q K1 D_theta2 with the registered one-sided
    stencils (D1O/D1W) on each phase; the phi operators (DP1, DP2) unchanged; the level-1 carrier
    exp(-i theta1) and the level-2 carrier exp(-i theta2) replacing E1 and E2s. The residual, the Jacobian
    pattern, the pins (R1, <T>, gauge) and the acceptance ladder are the stage-2 ones evaluated on the hull grid.
    The density per phase is the registered 48 points per level-1 period (NT1 = 48) and NT2 = 48; NP = 36 at
    the working grid and 54 at the refinement (the GR54 lesson), so the credential grid is 48 x 48 x 36 and
    the refinement 48 x 48 x 54.
D2. THE RESTRICTION MAP (the credential's instrument): from a hull state at rational q = N2/N1, the cell state on
    the registered (N1, N2) grid is u(K1 s, K2 s, phi) sampled at the cell's s-points; from a cell state, the
    hull state is defined on the line only. The credential compares in the cell's own metrics.
D3. THE PROTOCOL at each ratio: P1 level-1 recovery (the hull state independent of theta2), P2 the ramp to the
    registered waypoints (0.02 R2, 0.05 R2 in the registered sense of A2 as the level-2 amplitude), P3 the rate
    march at ds = 0.08 with full-state retention and sealed per-point measurements, 20 full-bar points per
    profile at NP 36 and again at NP 54, the march continued until the 0.0063 target is reached or the
    protocol's fold rule ends it (the registered near-singularity class), within the budget of section
    SCHEDULING. Per-point measurements: A2, rate, om2, RMS, closure, the tangent moments (v6).
D4. THE STATISTIC: D exactly as registered, per ratio and per NP; A2_max per ratio and per NP; the convergence
    bar D within 20 percent between NP 36 and 54 (else NO CALL at that ratio).
D5. THE PRICE: FND-135's closed form on the deepest full-bar member at 1.492 (NP 36 and 54), the torus average
    taken over (theta1, theta2) directly (exact for the hull; Leg A's identity is what makes it the time
    average); the share 1 - T0 / Sigma_wave; the retreat and Leg B's 13/9 number beside it.
D6. THRESHOLDS for the forms, fixed here from Leg B's record and not from any hull number: COLLAPSE is D >= 2.0
    (the registered collapses are 5.3x and 9.6x; the flat cells 1.03 to 1.06x; 2.0 is the geometric middle of
    the gap, rounded); FLAT is D <= 1.25 with the 0.0063 target REACHED (a full-bar point within 0.0003 of
    0.0063); FOLD is the march ending by the protocol's rule with A2_max < 0.0060 and D < 2.0; anything else is
    MIXED.

## VALIDATION BARS (halt-grade; Leg 0, before the lock)
v1. LEVEL-1 IDENTITY: the hull instrument's level-1 recovery (theta2-independent state) reproduces the
    registered level-1 member in the cell metrics to RMS <= 1e-9 and <T> = 3/2 to 1e-10, at 48 x 48 x 36.
v2. CELL REPRODUCTION at rational q: the hull state at q = 13/9 restricted to the line (D2) reproduces one
    retained 13/9 member from Leg B (432 x 36, the deepest full-bar member) at the C2 credential (RMS <= 1e-9,
    |dA2| / A2 <= 1e-6) when the hull is solved from the restricted-and-lifted cell state as its seed; the same
    at q = 7/5 against a retained 7/5 member. (At a rational q the hull problem is the cell problem plus a
    free phase; the credential pins the phase by the seed.)
v3. ENERGY CONTROL: FND-135's closed form with the torus average reproduces, on the lifted 13/9 member, Leg B's
    QC price 2.6069 T0 to 1e-4 relative.
v4. MOMENT CONTROL: the torus-averaged second moment of the level-1 sector on the hull is 1/3 to 1e-9 (FND-088).
v5. CLOSURE halt-grade (< 1e-6) on every accepted member; FRESH PATTERN keyed grid + pin_mode + q (faults
    9/10/11 binding); per-point measurements sealed by the runner.
v6. MEMORY: the measured peak at 48 x 48 x 54 recorded at Leg 0; the commission's booking is that peak plus 20
    percent, under the lab's cap of 48 GB; above the cap the refinement is HELD and Q1/Q2 are read at NP 36 only,
    with the 20 percent convergence bar unmet and said so (MIXED cannot be excluded; the forms then carry
    "NP 36 only" on their face).
v7. CLEAN ROOM: R2 appears only in Q3's comparison line; no hull number at 1.492 is computed before the lock.

## THE LEGS
Leg 0  Build and credential (v1 to v7); the lock follows on the record.
Leg 1  Q2 first: q = 3/2 on the hull, both NP (the control runs before the question, so the question's reading
       cannot shape the control's).
Leg 2  Q1: q = 1.492 on the hull, both NP.
Leg 3  Q3 price table; results doc; the author reads before any claim is drafted.

## PRE-REGISTERED INTERPRETATION RULES (locked before results; anything else is NO CALL)
Q1 (exactly one, per the thresholds of D6, with the NP 36/54 convergence bar):
  QP-FLAT: the quasi-periodic branch marches through the window and past the target without collapse; A2_max
      is the budget's. The level-2 amplitude is unbounded by the registered dynamics on the reachable range;
      the fold and the collapse were both the cell's.
  QP-COLLAPSE: the quasi-periodic branch collapses in rate inside the window. The collapse is physical at the
      registered ratio; RAT-RESONANT's "artifact" reading is narrowed to "artifact in its ORDER dependence,
      physical at 1.492", by name, and the low-order cells were right for a reason the ladder could not see.
  QP-FOLD: the march ends before the target without a rate collapse. The family has a reachable maximum that
      is a property of the state (not of a cell), to be priced by Q3 and named as A2_max of record.
  QP-MIXED: between the thresholds, or the convergence bar unmet. Reported with both NP numbers.
Q2 (exactly one):
  HULL-ALIAS-CONFIRMED: D(3/2 on the hull) <= 1.25 at both NP. The registered 3/2 collapse was the cell's
      aliasing; FND-147/151/152/153's 3/2 statements take the CELL-SCOPE rider as Leg B proposed, now with the
      mechanism shown.
  HULL-COLLAPSE-PHYSICAL: D(3/2 on the hull) >= 2.0 at both NP. The 3/2 collapse is in the quasi-periodic
      state; RAT-RESONANT is corrected by name (the order dependence was real, the artifact reading was not),
      and Q1's result is read beside it.
  HULL-32-MIXED: anything else; reported with both numbers.
Joint readings written on the results file's face, not formed: QP-FLAT with HULL-ALIAS-CONFIRMED is the clean
case (the collapse phenomenology was the instrument's); QP-COLLAPSE with HULL-COLLAPSE-PHYSICAL is the other
clean case (the collapse is the state's and the ladder's order dependence was a resolution effect, not an
alias); the mixed quadrants are reported as such and a longer charter is their next order.
Q3: a TABLE: deepest full-bar member at 1.492 (NP 36, NP 54), Leg B's 13/9 member, the retreat 2.598; Sigma_wave,
the share, the grid scope. No grant.
INSTRUMENT-OPEN (Leg 0 only): v1 or v2 unmet at every grid under the cap; the commission stops before the lock
and the record says what the instrument could not do.

## NO-RESCUE RULE
No change to the thresholds of D6, the D definition, the targets 0.0048/0.0063, the density 48 per period or the
NP pair after the lock. No third ratio. No deep march past the budget to reach a target the protocol did not
reach on its own. If the hull solver fails to converge at 1.492 where it converged at 3/2, that is reported as
NO CALL at 1.492 with the failure's numbers, not retried with a changed ladder. Failures kept.

## SCHEDULING (budgets, not bars)
Leg 0 is the executor's build in the sandbox on small grids plus one credential run on the mini (the only
machine for this job): expect two to four sessions. Leg 1 and Leg 2 are stage-1-class native runs, each two
profiles of 20 points: by Leg B's rate (six cells, two profiles each, 136 invocations over six days on the mini
at 42.7 GB) expect two to four days per ratio. Memory booking per v6. cpu_hours 400; mem_gb 48; usd 0 (compute
only). Results to analysis/QP_HULL_1_results.md; the price table inside it.

## STANDING
Registered claims untouched until the author grants. The lock is the lab's, after Leg 0; the draft, the
instrument and Leg 0 are the executor's, delivered on the queue branch; the runs are the lab's runner's. Adjacent:
COMPOSITE-SELECT (closed by its Leg D on the author's reading); the degenerate-perturbation session on the Om1/2
root and the second-order coupling commission (both OUT, separately charterable); the om2(q) observation of Leg
B's section 7 (a derivation question, not this charter's).

```lab
commission: QP-HULL-1
target: "Vacuum / foundations: the two-frequency state on a two-phase (hull) instrument without a rational cell: at q = 1.492 does the aligned family go flat, fold or collapse as a function of A2 alone (Q1), and does the registered 3/2 collapse appear on the hull at 3/2 (Q2); Sigma_wave priced at the deepest member (Q3); the successor COMPOSITE-SELECT's RAT-RESONANT named; moves no number in section 2b"
driver: benchmarks/lab/qp_hull_1/driver.py
verdict_script: benchmarks/lab/qp_hull_1/verdict.py
instrument:
  - benchmarks/foundations/qsweep_stage1.py
  - benchmarks/foundations/truestate_stage2.py
forms: [QP-FLAT, QP-COLLAPSE, QP-FOLD, QP-MIXED, HULL-ALIAS-CONFIRMED, HULL-COLLAPSE-PHYSICAL, HULL-32-MIXED, INSTRUMENT-OPEN, NO-CALL]
state: [analysis/qp_hull_1_ckpt.pkl]
budget: {cpu_hours: 400, usd: 0}
mem_gb: 48
```
