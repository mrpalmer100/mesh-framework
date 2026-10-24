# COMMISSION QP-HULL-2 -- THE QUASI-PERIODIC STATE ON THE CREDENTIALED HULL
# (CHARTER, the author's DRAFT for the lab's lock, 2026-10-24; the successor to QP-HULL-1, whose charter was parked
# on a compute estimate for its 48 x 48 x 36 instrument and whose Leg 0 is now on the record for the spectral hull
# at 24 x 8 x 36 and 48 x 12 x 36 (analysis/QP_HULL_1_leg0_results.md); this draft charters the same two questions
# on the grids Leg 0 measured, with the credential stated as a convergence rate and the booking measured, not
# estimated; the harness is bound to benchmarks/lab/_kit/labkit.py; nothing here has been run at q = 1.492)

## WHERE IT STANDS (the honest sentence, before the question)
COMPOSITE-SELECT's Leg B rendered RAT-RESONANT (2026-10-19): on the registered cell instrument the collapse of the
aligned two-frequency family tracks the commensurability ORDER of the rational cell, not the ratio. QP-HULL-1 named
the mechanism (a cell aliases the mode (N2, -N1) onto the mean field; a two-phase hull u(theta1, theta2, phi) keeps
every mode distinct and contains each cell as its restriction to the line theta2 = q theta1) and gated itself on
an instrument credential. That credential is now on the record: the spectral hull (benchmarks/foundations/
qp_hull.py, exact s-derivative symbol K1 D_theta1 + K2 D_theta2), marched INDEPENDENTLY at q = 13/9 by the
registered protocol, converges onto COMPOSITE-SELECT's retained 13/9 members as it is refined, with no operator
added: om2 gap 5.0e-4 to 1.7e-5 at the first member and 1.5e-2 to 3.7e-3 at the second between 24 x 8 x 36 and
48 x 12 x 36; om1, gamma and FND-135's price to 1e-5 to 1e-4 on both grids; the level-1 identities (om1 = pi
sqrt 2, gamma = 1 / sqrt 3, cos^2 theta = 1 / 3) to 1e-14. The second member's gap scales as NT2^(-3.4), so the
instrument is theta2-limited at NT2 = 12 and the next refinement is NT2 = 24. One 48 x 12 x 36 rung costs 14 to 17
hours on the mini. What is not known is unchanged from QP-HULL-1: whether the quasi-periodic state at q = 1.492,
on an instrument that imposes no cell, goes flat, folds or collapses as a function of A2 alone; and whether the
cell's collapse at 3/2 is in the state or in the cell. Leg A's QA stands (COMP-PIN-UNREACHABLE, FND-169) and is
not reopened.

## THE QUESTION (unchanged from QP-HULL-1 in substance; restated on the credentialed grids)
  Q1  THE QUASI-PERIODIC BRANCH. On the hull at the registered ratio q = 1.492, marched by the registered protocol
      (level-1 recovery, the sub-pin ladder to the waypoints, the rate march at ds = 0.08, full-bar members only),
      what does the aligned family do as a function of A2: flat through the window and past the 0.0063 target,
      collapse in rate, or fold (the march ends by the protocol's own rule before the target)?
  Q2  THE 3/2 ALIAS. On the same instrument at q = 3/2 exactly, does the cell's collapse (D 9.56x, registered)
      appear? If the hull at 3/2 is flat, the collapse at 3/2 was the cell's aliasing; if it collapses,
      RAT-RESONANT's "artifact" reading is wrong about 3/2 and is corrected by name, a failure kept.
  Q3  THE PRICE (a table, not a verdict). Sigma_wave by FND-135's closed form with the torus average, at the
      deepest full-bar member of Q1's march; beside the retreat 2.598 and Leg B's 2.6069 at 13/9.

## WHAT IS GIVEN (registered inputs; no others enter)
- The stage-2 operators, pins and weights (TRUESTATE stage 2; the sparse f32-J solver, SJ-CREDENTIALED; the rung
  budgets, basin guard and acceptance ladder of the Q-SWEEP protocol), reused unchanged inside qp_hull.py.
- The level-1 sector (K1, R1, <T> = 3/2, gauge), q-independent, shared.
- The registered ratio 1.492 (TRUESTATE stage-1 bars) and the registered rational cells with their retained
  members (read-only); COMPOSITE-SELECT Leg B's retained 13/9 members at A2 = 0.0018792 and 0.0046979 (the
  sealed checkpoint on the mini) as the credential's reference.
- D(q) as Q-SWEEP stage 1 defined it (rate at the full-bar point nearest A2 = 0.0048 over rate at the point
  nearest 0.0063; nearest-point pairing; RMS < 1e-8, closure < 1e-6); A2_max; om2 at matched A2.
- FND-135's closed-form two-level kinetic energy; Leg A's identity torus average = time average on the gated
  states; FND-132's level-1-at-c identity.
- Leg 0's record (analysis/QP_HULL_1_leg0_results.md, analysis/qp_hull_leg0_part2.json) as the credential's
  baseline numbers, read by the driver's credential unit and checked against (D2 below).

## WHAT IS NOT ASSUMED, AND WHAT IS FORBIDDEN
No new pin, weight, stencil or solver: the hull is the registered operators on two phases. Nothing about the
outcome at 1.492 is predicted by the author, the executor or the lab. R2 = 0.09396 appears in no file of this
commission except Q3's comparison line. The order-N1 aliasing mechanism is the reason for the instrument, not a
result; Q2 tests it. No number at 1.492 exists before the lock, and the credential unit (Leg 1) runs to
completion and is sealed before the first 1.492 solve starts (v7).

## SCOPE (hard boundary)
One ratio (1.492) and one control ratio (3/2); no ladder or sweep in q; the anti-aligned branch OUT; no selection
principle evaluated; no re-adjudication of FND-147/163/164's cell results (Q2 reads a different instrument). The
phi resolution is the cell's registered NP = 36 throughout: the convergence axis of this commission is theta2
(NT2), which Leg 0 showed to be the limiting one; an NP refinement is a separate, later commission and its
absence is stated on every form's face as "NP 36 only".

## DESIGN COMMITMENTS (locked at lock)
D1. THE INSTRUMENT: benchmarks/foundations/qp_hull.py as credentialed (spectral D_s; the three registered fields
    on NT1 x NT2 x NP; level-1 carrier exp(-i theta1), level-2 carrier exp(-i theta2); the stage-2 residual,
    Jacobian pattern, pins and acceptance ladder on the hull grid). Working grid W = 48 x 12 x 36 (Leg 0's
    credentialed grid). Convergence grid C = 48 x 24 x 36 (the theta2 refinement Leg 0's rate calls for).
    Finer grids are seeded by exact prolongation of the coarser grid's state (HGrid.prolong_state), member by
    member, with the three-rung ramp from the fine grid's previous member (the Leg 0 part-2 lesson: prolonging an
    under-resolved coarse member seeded a fine solve at RMS 0.5).
D2. THE CREDENTIAL (Leg 1, run first, sealed; binding forms below). At q = 13/9 against the two retained members:
    (a) RATE: the om2 gap at the second member (A2 0.0046979) on grid C is at most 1e-3 relative, and the ratio
        of the gaps W / C is at least 6 (Leg 0's measured order 3.4 in NT2 predicts 2^3.4 = 10.6 and a gap near
        3.5e-4; 6 is the bar, below which the instrument is not converging as the record claims). The first
        member's gap on C must not exceed its W value (1.7e-5) by more than a factor 2 (a refinement that
        worsens the resolved member is a fault).
    (b) BASELINE: the driver's own solve on W reproduces Leg 0's recorded W numbers (om2 2.8519316 and 2.9119786;
        the restricted-state metrics) to 1e-7 relative, from a fresh solve: the instrument is the one on the
        record, not a drift of it.
    (c) SEEDED REPRODUCTION (QP-HULL-1's v2, cheap, run on W): the hull solved from the restricted-and-lifted
        retained cell state as its seed returns to the cell state in the cell metrics with RMS <= 1e-9 and
        |dA2| / A2 <= 1e-6 (at a rational q the hull problem is the cell problem plus a free phase; the seed pins
        the phase). If (c) fails while (a) and (b) pass, the lift map is at fault and the form is INSTRUMENT-OPEN
        with the lift named.
    (d) ENERGY: FND-135's price on the lifted 13/9 members reproduces Leg B's to 1e-4 relative (Leg 0: 2.6e-5
        and 8.4e-5 on W).
    (e) MOMENT: the torus-averaged second moment of the level-1 sector on the hull is 1 / 3 to 1e-9 (FND-088),
        computed as a number, not inferred from theta.
    (f) MEMORY AND TIME: peak RSS and wall time per rung measured on W and on C and written to the record; the
        booking of SCHEDULING is these numbers plus 20 percent; if C exceeds the lab's cap of 48 GB, C is HELD,
        Q1 and Q2 are read on W only and every form carries "W only, convergence bar unmet".
D3. THE PROTOCOL at each ratio: P1 level-1 recovery (theta2-independent); P2 the sub-pin ladder to the registered
    waypoints (fractions 0.15, 0.3, 0.55, 0.8, 1 of the first waypoint pin, then three rungs per further member);
    P3 the rate march at ds = 0.08 with full-state retention and sealed per-point measurements (A2, rate, om2, RMS,
    closure, the tangent moments), continued until the 0.0063 target is reached or the protocol's fold rule ends
    it, within SCHEDULING's budget; all on W. On C: the two D points only (the full-bar point nearest 0.0048 and
    nearest 0.0063, or the fold point if the march folded), reached by prolongation of W's states and the
    three-rung ramp; this is the convergence check of D4, not a second march.
D4. THE STATISTIC: D exactly as registered, per ratio, on W; D on C from the two prolonged points; the
    convergence bar D(W) and D(C) within 20 percent (else MIXED at that ratio); A2_max per ratio on W; om2 at
    matched A2 on both grids.
D5. THE PRICE: FND-135's closed form on the deepest full-bar member at 1.492 on W and at the corresponding point
    on C, torus average over (theta1, theta2) directly; the share 1 - T0 / Sigma_wave; the retreat and Leg B's
    13/9 beside it.
D6. THRESHOLDS (QP-HULL-1's D6, unchanged, fixed from Leg B's record): COLLAPSE is D >= 2.0; FLAT is D <= 1.25
    with the 0.0063 target REACHED (a full-bar point within 0.0003 of 0.0063); FOLD is the march ending by the
    protocol's rule with A2_max < 0.0060 and D < 2.0; anything else MIXED.

## HARNESS (binding)
Driver and verdict on benchmarks/lab/_kit/labkit.py (Driver / Verdict / Halt / Blocked; the README and example
pair). Units in order, one per invocation, each sealed before the next starts: credential (D2 a to f at 13/9),
leg1 (q = 3/2: P1 to P3 on W, then the two C points), leg2 (q = 1.492: the same), price (D5), verdict. The
verdict's form_rule recomputes D, the convergence ratios and every threshold test from the sealed per-point
records, checks the driver's own record to 1e-12, and decides every form before any number is rendered. CONFIG
(one dict in the driver, imported by the verdict) holds every locked number here (grids, pins, fractions, ds,
targets, thresholds, bars). A failed solve is a Halt; a Halt in leg2 is NO-CALL at 1.492 with the failure's
numbers, not a retry with a changed ladder. The per-solve state pickles are the checkpoint's; --resume recomputes
a saved state's rms, closure and pins rather than trusting what was saved (the Leg 0 KeyError lesson).

## VALIDATION BARS (halt-grade; the credential unit)
v1. LEVEL-1 IDENTITY on W and C: om1 = pi sqrt 2, gamma = 1 / sqrt 3, cos^2 theta = 1 / 3, each to 1e-12; RMS
    <= 1e-12.
v2. D2 (a) to (e) as written.
v3. CLOSURE below 1e-6 and all pins met on every accepted member; FRESH PATTERN keyed grid + pin_mode + q (faults
    9/10/11 binding); per-point measurements sealed by the runner.
v4. RESTRICTION on an analytic field: the 2D trigonometric restriction of a known hull field to the 13/9 line
    reproduces the closed form to 1e-12 (the smoke's control, run again in production).
v5. CLEAN ROOM: no hull number at 1.492 before the credential unit is sealed; the leg2 unit refuses to start
    without the credential seal.

## THE LEGS
Leg 1  Credential at 13/9 (D2, v1 to v4) on W and C; memory and time measured; the lock follows on this record
       if the forms CRED-RATE-MET fires; INSTRUMENT-OPEN otherwise and the commission stops.
Leg 2  Q2 first: q = 3/2 on W (the full march), then the two C points.
Leg 3  Q1: q = 1.492 on W, then the two C points. DECISION GATE (the author's, 2026-10-24): Leg 3 starts only on
       the author's word after Leg 2's form is rendered and read. If the hull collapses at 3/2 as the cell did,
       the aliasing reading is dead and the author may close the commission at Leg 2 with Q1 unrun; that is a
       completed commission (Q2 answered, Q1 WITHHELD-BY-AUTHOR on the record), not a withdrawal. The gate does
       not change any form or threshold; it decides whether three further weeks are spent.
Leg 4  Q3 price table; results doc; the author reads before any claim is drafted.

## FORMS (exhaustive; pre-registered; anything else is NO-CALL)
Credential (exactly one; decided before Leg 2 starts):
  CRED-RATE-MET            D2 (a) to (e) met; (f) measured and under the cap. The lock proceeds.
  CRED-HELD                D2 (a) to (e) met; C over the cap: Q1 and Q2 on W only, every later form carrying
                           "W only, convergence bar unmet".
  INSTRUMENT-OPEN          D2 (a) unmet (the hull is not converging onto the cell at the measured rate), or (b)
                           unmet (the instrument drifted from the record), or (c) unmet with the lift named: the
                           commission stops; the record says what the instrument could not do.
Q1 (exactly one, per D6 with the D4 convergence bar):
  QP-FLAT                  D <= 1.25 on W and C, target reached: the level-2 amplitude is unbounded by the
                           registered dynamics on the reachable range; the fold and the collapse were the cell's.
  QP-COLLAPSE              D >= 2.0 on W and C: the collapse is physical at 1.492; RAT-RESONANT narrowed to
                           "artifact in its order dependence, physical at 1.492", by name.
  QP-FOLD                  the march ends by the fold rule with A2_max < 0.0060 and D < 2.0 on W, the fold point
                           reproduced on C within 20 percent in A2: a reachable maximum that is the state's.
  QP-MIXED                 between thresholds, or D(W) and D(C) differ by more than 20 percent, or CRED-HELD.
  WITHHELD-BY-AUTHOR       Leg 3 not started at the author's decision after Leg 2 (the gate); Q1 unanswered by
                           choice, stated as such; no reading of Q1 is implied.
Q2 (exactly one):
  HULL-ALIAS-CONFIRMED     D(3/2 on the hull) <= 1.25 on W and C: the registered 3/2 collapse was the cell's
                           aliasing; FND-147/151/152/153's 3/2 statements take the CELL-SCOPE rider as Leg B
                           proposed, with the mechanism shown.
  HULL-COLLAPSE-PHYSICAL   D(3/2 on the hull) >= 2.0 on W and C: the 3/2 collapse is in the quasi-periodic state;
                           RAT-RESONANT corrected by name.
  HULL-32-MIXED            anything else; both grids' numbers reported.
Q3: a TABLE (no form, no grant).
NO-CALL                    a Halt in leg1 or leg2 with the failure's numbers; v1, v3, v4 or v5 unmet.
Joint readings are written on the results file's face, not formed: QP-FLAT with HULL-ALIAS-CONFIRMED is the clean
case (the collapse phenomenology was the instrument's); QP-COLLAPSE with HULL-COLLAPSE-PHYSICAL is the other clean
case; mixed quadrants are reported as such and a longer charter is their next order.

## NO-RESCUE RULE
No change to D6's thresholds, the D definition, the targets 0.0048 / 0.0063, the grids W and C, the fractions or
ds after the lock. No third ratio. No march past the budget to reach a target the protocol did not reach. A solver
failure at 1.492 where 3/2 converged is NO-CALL at 1.492 with its numbers. If D2 (a)'s ratio lands between 6 and
10.6, that is CRED-RATE-MET with the measured order on the record, not a reason to add a grid. Failures kept.

## SMOKE DISCIPLINE (binding on the drafting worker)
LAB_SMOKE=1 runs on 12 x 4 x 12 at q = 13/9 only: the level-1 recovery identities (v1 at the smoke tolerance the
driver derives from the grid), the analytic-restriction control (v4), and a synthetic two-member comparison on
fields the smoke constructs itself; it prints the bars and no D, no om2 at any rational other than 13/9, and
nothing at 1.492. One unit per invocation, atomic checkpoint, one FORM per question, a second rendering refused.

## SCHEDULING (budgets, not bars; measured, from Leg 0)
Leg 0 measured 32000 s for the level-1 solve plus the first member on W by prolongation and 52000 to 61000 s per
further rung on W (14 to 17 hours), on the mini. The solver is single-threaded (the lab's Phase-0 benchmark:
threads_per_job 1, extra BLAS threads gave nothing), so the lab runs jobs side by side and the binding constraint
is MEMORY, which D2 (f) measures: a hull job on W is at least Leg B's cell in grid points (20736 against 15552) and
Leg B's cell ran at 42.7 GB under the 48 GB cap. CONCURRENCY RULE, decided by the measurement, not in advance: if a
W job's measured peak is at most one third of the cap, Legs 2 and 3 run concurrently (the control and the question
are both sealed before either is read, so the "control first" ordering is an ordering of reading, which concurrency
does not touch); if more, they run in sequence; C runs alone if its peak exceeds half the cap. A march of 10 to 14
full-bar points per ratio on W is 6 to 10 days per ratio; the two C points per ratio 3 to 4 days; Legs 1 to 3 are
two to four weeks of wall time depending on the concurrency the measurement allows. The author decides whether that
is acceptable before the lock, and the lock records the booking and the concurrency. cpu_hours 700 (single-thread
hours); mem_gb from D2 (f), booked at the measured peak plus 20 percent per job and under 48 in total; usd 0 beyond
drafting and review. Results to analysis/QP_HULL_2_results.md; the price table inside it.

## DISCLOSURES (for the lock checklist's anti-fishing item; the reviewers judge)
Leg 0 part 1 (benchmarks/foundations/qp_hull_leg0.py, runs A and C, 2026-10-20) computed hull numbers at the FIRST
RAMP WAYPOINT ONLY (A2 = 0.0018792, NP 12, grids 12 x 8 and 24 x 8): run A at q = 1.492 (om2, gamma, the level-1
theta, closure, to read the density at which om2 converges), run C at q = 3/2 against the 3/2 cell (the restricted
state in the cell metrics, to show the size of the degenerate-mode effect at that density). Neither computed a rate,
a march, a D, nor any point near 0.0048 or 0.0063; the part-1 JSON was not kept on the record (part 2 superseded
it). These are instrument-convergence quantities at an amplitude 2.5 to 3.4 times below the statistic's window,
and the executor's reading is that they do not preview Q1 or Q2, whose evidence is D at the two statistic points and
the fold rule; but FINE-DISP-1 taught that a preview is the result for a deterministic computation, so the
disclosure is made here in full and the skeptical reviewer decides whether checklist item I is met. Leg 0 part 2
computed nothing at 1.492 or 3/2.

## STANDING
Registered claims untouched until the author grants. The lock is the lab's, after the credential unit; the draft
and the instrument are the executor's, on the queue branch; the runs are the lab's runner's. Adjacent and OUT:
COMPOSITE-SELECT (closed by its Leg D on the author's reading); the degenerate-perturbation session on the Om1/2
root and the second-order coupling commission; the om2(q) observation of Leg B's section 7; an NP refinement
(a later commission, named on every form's face as absent here).

```lab
commission: QP-HULL-2
target: "Vacuum / foundations: the two-frequency state on the credentialed two-phase hull without a rational cell: at q = 1.492 does the aligned family go flat, fold or collapse as a function of A2 alone (Q1), and does the registered 3/2 collapse appear on the hull at 3/2 (Q2); Sigma_wave priced at the deepest member (Q3); the credential stated as the hull's convergence rate onto the 13/9 cell (D2) and measured before the lock; moves no number in section 2b"
driver: benchmarks/lab/qp_hull_2/driver.py
verdict_script: benchmarks/lab/qp_hull_2/verdict.py
instrument:
  - benchmarks/foundations/qp_hull.py
  - benchmarks/foundations/qp_hull_leg0.py
  - benchmarks/foundations/qsweep_stage1.py
  - benchmarks/foundations/sparsej_instrument.py
  - benchmarks/lab/_kit/labkit.py
forms: [CRED-RATE-MET, CRED-HELD, INSTRUMENT-OPEN, QP-FLAT, QP-COLLAPSE, QP-FOLD, QP-MIXED, WITHHELD-BY-AUTHOR, HULL-ALIAS-CONFIRMED, HULL-COLLAPSE-PHYSICAL, HULL-32-MIXED, NO-CALL]
state: [analysis/qp_hull_2_ckpt.pkl]
budget: {cpu_hours: 700, usd: 0}
mem_gb: 48
```
