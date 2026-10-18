# COMMISSION SEAT-FLOW-1 -- THE BANKED REPTATION MOVERS RUN ON THE CONVERGED NON-TORUS SEATS, AGAINST THE SOURCED ANCHORS
# (CHARTER, the author's DRAFT for the lab's lock, 2026-10-18; nothing has run; no number here was read from a run of this commission)

## 1. The question, and the North Star line

Question key: seat-table-basins-vs-energetics.

SEAT-CONVERGE (analysis/SEAT_CONVERGE_results.md, 2026-10-09) converged the registered certified knot table under
KNOT-REACH-2's convergence rule and found FND-MATTER-069's stable set {5, 7} surviving, now resting on the seats of
the braid and plat knots rather than on the 4_1 stall. It named one road: the rearrangement mover the registry
already built (FND-MATTER-024, 025, 032) run on those knots with the literature ideals as pre-registered targets.
This commission walks that road with the equipment the registry banked and nothing new: the uniform reptation
conveyor (benchmarks/foundations/reptation_conveyor.py, tighten_conveyor, FND-MATTER-025) and the oscillatory
conveyor (benchmarks/foundations/adaptive_flow_campaign.py, tighten_oscillatory, FND-MATTER-032), each followed by
the convergence-rule descent, certified at every stage, the best certified state banked (FND-MATTER-024's lesson a).

Q1 (per knot). From its SEAT-CONVERGE converged seat, does a banked reptation mover plus convergence descent carry
each non-torus knot (5_2, 6_1, 6_2, 6_3, 7_2, 8_1) to within the solver's systematic band of its literature
anchor, improve it without reaching, or leave it where it is?
Q2 (the table). With the moved seats in place of the SEAT-CONVERGE seats (the torus knots and 4_1 carried over
unchanged, since they sit within 2 to 6 percent of their anchors and are not moved here), what does FND-MATTER-069's
stability rule read: a stable set, or none?

North Star line (section 5, rule (c)): a discriminator. SEAT-CONVERGE concluded the stability rule "reads
constructor basins, not energetics, on the registry's table"; this commission decides whether the registry's
movers can take the table off those basins, which is the precondition for reading the rule for energetics at all
(SM_EMERGENCE row 10; NORTH_STAR gap 5, the proton topology). It moves no number in section 2b; a MONOTONE-NULL
or a STABLE-SET here is a property of the solver's table either way, and the write-up says so.

What this commission does NOT do: it builds no new mover (FND-MATTER-032 graded the attack space exhausted at
prototype grade and named the next step as a production constrained-gradient solver, which this is not); it does
not touch the torus seats or 4_1; it does not re-read SEAT-CONVERGE's forms (kept); it does not claim a knot's
"true" ropelength, only the best certified seat the registered equipment reaches from the registered start.

## 2. The parts list (every input cited; nothing is chosen in this commission)

| part | what | source |
|---|---|---|
| the starting seats | the SEAT-CONVERGE converged seats of 5_2, 6_1, 6_2, 6_3, 7_2, 8_1, reconstructed deterministically: the registered constructor (3-strand words of FND-MATTER-021 for 5_2, 6_2, 6_3 at N = 130; the plat words of FND-MATTER-023 for 6_1, 7_2, 8_1 at N = 140) tightened by tighten_coords under the doubling schedule to the iteration count the sealed record carries (5_2 200000, 6_1 100000, 6_2 200000, 6_3 50000, 7_2 50000, 8_1 50000) | benchmarks/foundations/seat_converge.py (KNOTS, the schedule); analysis/seat_converge_ckpt.pkl (the recorded L/D and iteration counts; coordinates are not in the record, hence the reconstruction and credential C-1) |
| the movers | tighten_conveyor(P, iters=26000, shrink=0.9997, v0) with v0 = +0.05, -0.05, +0.08; tighten_oscillatory(P, iters=24000, shrink=0.9997, v0=0.08, period=3000) | FND-MATTER-025 (v0 = 0.05 the registered stable amplitude; 0.12 tolerated by 4_1, detonates 6_1), FND-MATTER-032 (oscillatory v0 = 0.08 banked; 6_1 tears at 0.15) |
| the descent | tighten_coords from the mover's output under the convergence rule: cumulative 25000 x 2^k, CONVERGED at the first k >= 1 with under 1 percent length change, cap 400000 (SEAT-CONVERGE's deepest converged at 200000) | KNOT-REACH-2 C-1; seat_converge.py |
| the certificates | knot_det at tilts 0.013 and 0.11 equal to the knot's determinant (7, 9, 11, 13, 11, 13); for 6_1, 7_2, 8_1 the Alexander odd part (0, 5, 1) at both tilts | topology_certifier.knot_det; alexander_certifier_61 (alexander_at, odd_part); seat_converge.certified |
| the ledger | L/D, S, contacts as FND-MATTER-019 reads them | knot_reach.ledger with mapping_calibrated.build_table |
| the anchors | solid, sourced (FND-MATTER-028, literature_anchors.LIT): 6_1 28.353, 6_3 28.920. Approximate, the registry's per-crossing entries (FND-MATTER-069): 5_2 24.7, 6_2 26.5, 7_2 30.7, 8_1 32.7. The grade is carried with every comparison | benchmarks/foundations/literature_anchors.py; FND-MATTER-069 |
| the systematic band | +5.0 percent above the anchor: SEAT-CONVERGE's solver systematic on the knots with exact anchors was +2.4 to +6.4 percent, mean +3.7; the registered figure is +2.3 | analysis/SEAT_CONVERGE_results.md; FND-MATTER-069 |
| the carried seats | 3_1 16.908, 4_1 21.576, 5_1 25.048, 7_1 31.452 | analysis/seat_converge_ckpt.pkl (read for these four numbers only) |

Disclosure on the anchors, made here because it changes a prior: SEAT-CONVERGE's results compared 6_3 (30.451) with
the generic n = 6 entry 26.5 (+15 percent); against its sourced anchor 28.920 the same seat is +5.3 percent, at the
edge of the systematic band. The kept results and the FND-MATTER-069 rider stand as written; this charter reads
every knot against the best-grade anchor the registry holds and says which grade it is.

## 3. Steps (one unit per invocation; checkpoint analysis/seat_flow_1_ckpt.pkl, atomic; resumable)

S0 setup: file hashes (driver, verdict, the two mover files, seat_converge.py, this charter); the anchors, the carried
seats and the recorded iteration counts copied into the checkpoint from their files.
S1 credentials C-1 to C-3 (below), one unit each; a failure writes CREDENTIAL-FAIL and stops.
S2 the runs: for each evidence knot, for each of the four mover settings, one unit: the mover from the reconstructed
seat; certificate and ledger after the mover; then the convergence descent, certificate and ledger after every
doubling; the best CERTIFIED state's ledger banked (the start counts as a certified state, so the bank never rises
above the start); the run's flags (TORN if any stage's L/D exceeds 1.5 x the start; CERT-LOST if any certificate
fails, the stage discarded and the run continued from the last certified state; neither flag changes the bank's
rule). 24 units.
S3 terminal seal: status COMPLETE, the plan (knots, settings, caps), per-unit digests, written last; the driver
prints "SEAT-FLOW-1 COMPLETE -- run the verdict".

## 4. Credentials (pass bars locked here; every one must pass before S2)

C-1 reconstruction: each evidence knot's reconstructed seat has L/D within 1e-3 of the sealed SEAT-CONVERGE record
and passes its certificates; the four carried seats are read from the record, not recomputed.
C-2 the answer key (FND-MATTER-025): the plat 4_1 (plat_closure(LADDER['4_1'][0]), N = 140) from its greedy seat
under tighten_conveyor at v0 = 0.05 then the descent reaches L/D <= 22.0 (the boundary 22.5 fallen; the registered
figure 21.54; the trace-closure floor 21.53), with its certificate held. The plat 4_1 is not an evidence knot.
C-3 the oscillatory mover on the same plat 4_1 at v0 = 0.08, period 3000, reaches L/D <= 22.5 (FND-MATTER-032
recorded 21.96).
C-2 and C-3 are the controls FND-MATTER-024's lesson demands: a mover that cannot reproduce its own registered
crossing has no standing to report on a wall.

## 5. The floor test

The floor is the start itself: a run whose bank equals its start (within 0.2 percent) has done nothing, and the
verdict reads it as HOLDS, never as evidence that the basin is a wall. A knot is read from the best bank over its
four runs; the per-run flags are recorded. There is no noise floor to estimate: the movers are deterministic for a
given setting, and the four settings are the sample.

## 6. The bars (locked here; no pilot; from the registry's numbers alone)

Per knot, with A its anchor (grade carried), S its SEAT-CONVERGE seat, B the best bank over the four runs:
- ANCHOR-REACHED: B <= 1.05 A.
- IMPROVED: B <= 0.99 S and B > 1.05 A.
- HOLDS: B > 0.99 S.
For the table (Q2): sigma(n) = min over knots of crossing number n of B/n (the carried seats for 3_1, 4_1, 5_1, 7_1),
strict local minima over n = 3..8 exactly as seat_converge_verdict.rule reads them; STABLE-SET-{...} or MONOTONE-NULL.
Prior, stated and not leaned on: ANCHOR-REACHED for 6_3 (5.3 percent to close, the conveyor closed 7 percent on
5_2 in FND-MATTER-025), IMPROVED for 5_2 and 6_2, HOLDS for 6_1 and 7_2 (the standing walls, eleven attacks), IMPROVED
for 8_1; on that prior sigma(6) falls to about 4.82 and n = 5 leaves the set while n = 7 stays, so the prior table
form is STABLE-SET-[7]. If 8_1 reaches 1.05 x 32.7 the set is empty: MONOTONE-NULL.
Sub-readings, recorded, not read: which setting produced each knot's bank; the stage at which it was banked (after
the mover or at which doubling); the count of TORN and CERT-LOST stages per setting (the congestion gauge of
FND-MATTER-025 read on four new knots).

## 7. Verdict forms (exhaustive; reached in this order)

FORM (instrument): CREDENTIAL-FAIL, CHECKPOINT-INVALID, INCOMPLETE-OPEN (status not COMPLETE or any of the 24 units
missing).
FORM (Q1, one line per knot, six lines): K52-ANCHOR-REACHED / K52-IMPROVED / K52-HOLDS and likewise K61, K62, K63,
K72, K81, with the anchor's grade printed after the token (solid or approximate).
FORM (Q2): STABLE-SET / MONOTONE-NULL; the token is followed on the same line by the list of minima and the
sigma values, as seat_converge_verdict prints them.
A HOLDS on a knot with an approximate anchor says nothing about the anchor; an ANCHOR-REACHED on an approximate
anchor is reported as reached-to-the-registry's-entry, not to the literature. The Q2 form is read from the bank
table alone and does not depend on the anchors.

## 8. The verdict script (benchmarks/lab/seat_flow_1/verdict.py; frozen at lock)

Reads the checkpoint only. Order fixed: (1) validate in full (status COMPLETE; all 24 units present, each with its
stage ledgers, certificates and flags; every numeric finite; the manifest of file hashes equal to the lock record in
analysis/lab/locks/; the carried seats and anchors equal to the charter's); (2) only then create
analysis/SEAT-FLOW-1_verdict.log with O_EXCL (an existing log refuses the run); (3) CREDENTIAL-FAIL returns at once
if any credential failed; (4) the Q1 lines, then Q2. Every bank is printed with the start, the anchor, the grade and
the setting that produced it.

## 8a. Development and smoke discipline (binding on the worker; a lock-review item)

Before the lock nothing runs on the six evidence knots. LAB_SMOKE=1 runs the whole pipeline on the torus trefoil
(knot_reach.torus(3), not an evidence knot, whose anchor 16.372 is on the record) with iteration counts divided by
50, writes analysis/seat_flow_1_smoke.pkl and never the evidence checkpoint; the smoke verdict prints the plumbing
it checked and "smoke: forms withheld" and no FORM token. The credentials C-2 and C-3 run on the plat 4_1 only in
the evidence run, after the lock.

## 9. Budgets

Per run: the mover (26000 iterations at N = 130 to 140, pair distances each iteration, about two minutes) plus the
descent (SEAT-CONVERGE converged ten knots in 35 minutes under the same rule). Estimate 5 to 12 minutes per run, 24
runs, 2 to 5 hours; the controls add two runs. Declared cpu_hours 8; mem_gb 2; usd 0. Single-threaded; runs in the
lab's ordinary job slots beside Leg B.

## 10. Disclosures (instrument and process)

The movers, the certifiers, the constructors and the descent are the registry's, unchanged; the only new code is
the driver that sequences them and the verdict that reads the checkpoint. FND-MATTER-032's terminal grade on the
6_1 wall is not contested: 6_1 is in the evidence set so that the table is complete, and its prior is HOLDS. The
anchor disclosure in section 2 is a reading of kept files, not a run. The author wrote this charter without
executing anything; the iteration counts in section 2 are copied from the sealed SEAT-CONVERGE record as printed in
its results file.

```lab
commission: SEAT-FLOW-1
target: "SM_EMERGENCE row 10 and NORTH_STAR gap 5: a discriminator (rule c) deciding whether the registry's banked reptation movers take the certified knot table off its constructor basins, the precondition for reading FND-MATTER-069's stability rule for energetics; moves no number"
driver: benchmarks/lab/seat_flow_1/driver.py
verdict_script: benchmarks/lab/seat_flow_1/verdict.py
instrument:
  - benchmarks/foundations/reptation_conveyor.py
  - benchmarks/foundations/adaptive_flow_campaign.py
  - benchmarks/foundations/seat_converge.py
  - benchmarks/foundations/two_term_mass_model.py
  - benchmarks/foundations/topology_certifier.py
  - benchmarks/foundations/alexander_certifier_61.py
forms: [CREDENTIAL-FAIL, CHECKPOINT-INVALID, INCOMPLETE-OPEN, K52-ANCHOR-REACHED, K52-IMPROVED, K52-HOLDS, K61-ANCHOR-REACHED, K61-IMPROVED, K61-HOLDS, K62-ANCHOR-REACHED, K62-IMPROVED, K62-HOLDS, K63-ANCHOR-REACHED, K63-IMPROVED, K63-HOLDS, K72-ANCHOR-REACHED, K72-IMPROVED, K72-HOLDS, K81-ANCHOR-REACHED, K81-IMPROVED, K81-HOLDS, STABLE-SET, MONOTONE-NULL]
state: [analysis/seat_flow_1_ckpt.pkl]
budget: {cpu_hours: 8, usd: 0}
mem_gb: 2
```
