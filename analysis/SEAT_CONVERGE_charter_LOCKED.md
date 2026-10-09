# COMMISSION SEAT-CONVERGE -- THE CERTIFIED KNOT TABLE UNDER THE CONVERGENCE RULE
# (CHARTER, LOCKED 2026-10-09 by the author before any knot at full budget; the PC's night job)

North Star line (section 5): (a) the scorecard row "Why the observed particle spectrum" (SM_EMERGENCE row 10) and
gap 5 of section 4 (the proton's topology, now priced at ~1500 crossings by KNOT-REACH-2). The registry's certified
knot table (FND-MATTER-019/020/021/022/023: ten knots to eight crossings, every row with a topological certificate)
was seated under per-knot iteration budgets at the 3-percent grade, and two of its rows are known stalls: the 6_1
"wall" at 32.3 (FND-MATTER-032 gave the mover designs a terminal grade against it) and 7_2 at 38.6 (provisional).
The spectrum law read on that table (FND-MATTER-069, sigma = L/n, strict local minima) found a stable set {5, 7}
that traced to the 4_1 stall anomaly and the composite penalty, with a pre-registered sensitivity: resolve 4_1
downward and the set collapses to the monotone null, no proton pointer. KNOT-REACH-2 then converged every torus
rung to 1 percent with a budget rule that doubles until the length stops moving. This commission applies that rule
to the whole registered table, from the registered constructors, certified at every doubling, and reads
FND-MATTER-069's rule once on the converged seats. Either the walls dissolve under a converged budget (an instrument
finding that reopens 6_1 and 7_2) or they stand (confirming FND-MATTER-032's basin reading under the strongest
budget the registry has used); and the stability rule either selects a crossing number or returns the null, on seats
that are converged rather than budgeted.

## The ten knots (fixed; registered constructors, registered point counts)
3_1, 5_1, 7_1 by the torus parametrisation (40 n points, KNOT-REACH); 4_1 by FND-MATTER-020's trace-closure braid
(N = 130); 5_2, 6_2, 6_3 by FND-MATTER-021's certified 3-strand words (N = 130); 6_1, 7_2, 8_1 by FND-MATTER-023's
plat words (N = 140), identified by determinant AND the Alexander odd part (FND-MATTER-022) as those claims identify
them. No new geometry, no new word, no rounding preprocessor, no mover.

## Steps
  C1  Each knot from its constructor, certified at construction (det at tilts 0.013 and 0.11; Alexander odd part
      where registered) or REFUSED by name. Then KNOT-REACH-2's rule C-1 unchanged: doublings of 25000, resumed
      from the previous coordinates, CONVERGED at the first k >= 1 with under 1 percent change, cap 1,600,000;
      certified after every doubling. A knot at the cap unconverged is WALLED: its last length is kept and
      flagged, and the table goes on (the knots are independent; one wall does not stop the others).
  C2  The ledger per knot as FND-MATTER-019 reads it (L/D, S, contacts). Checkpointed per doubling;
      analysis/seat_converge_ckpt.pkl sealed at the end.
  C3  The verdict once (seat_converge_verdict.py): V1 the table against the registered seats; V2 FND-MATTER-069's
      rule, sigma(n) = min L/n over the knots of each crossing number, strict local minima over n = 3..8, read WITH
      the walled knots (as the registry's own table was) and also without them (printed); V3 the walls (6_1, 7_2:
      DISSOLVED if the seat falls more than 5 percent below the registered one, STANDS otherwise); V4 the solver
      systematic over the literature ideals the registry carries (3_1, 4_1, 5_1, 7_1).

## Bars (to be LOCKED)
B-1  The constructors, point counts and words are the registered ones; the rule is KNOT-REACH-2's; nothing is
     tuned after a knot disappoints (a walled knot is walled).
B-2  Certificates at every doubling; a loss is REFUSED and kept.
B-3  No knot is named a particle (FND-MATTER-019's rule); the stability rule's output is a crossing number or null.
B-4  The prior, stated and not leaned on: 4_1 converges near 21.5 (the smoke run: 21.547 against the registered
     21.64 and the literature 21.04); 5_2, 6_2, 6_3 converge within the solver systematic; 6_1 and 7_2 STAND
     (FND-MATTER-032: basin, not budget); 8_1 takes its first seat; the stability rule reads MONOTONE-NULL on the
     converged seats (FND-MATTER-069's own sensitivity, now that 4_1 is at 21.5).
B-5  One pass; the verdict is the script's line; failures kept.

## Verdict forms (to be LOCKED)
MONOTONE-NULL     no strict local minimum in sigma(n): the registered rule selects nothing on converged seats;
                  FND-MATTER-069's pre-registered sensitivity is discharged and its stable set {5, 7} is recorded as
                  an artifact of the 4_1 stall; rider on FND-MATTER-069.
STABLE-SET-{...}  a strict minimum at some n: recorded, with the knots that make it; no particle named; rider.
Per wall: WALL-DISSOLVED (rider on FND-MATTER-032 and FND-MATTER-022/023: the wall was budget, not basin; the
          seat moves) or WALL-STANDS (rider: the wall survives a converged budget; the basin reading stands).
In every form: riders on FND-MATTER-019 (the converged table beside the budgeted one) and, for 8_1, on
FND-MATTER-023 (its first seat); the solver systematic re-read (V4). No status change; the five numbers unchanged.

## Instrument
benchmarks/foundations/seat_converge.py (one doubling per invocation; go.py terminal pattern COMPLETE) and
benchmarks/foundations/seat_converge_verdict.py. Smoke run 2026-10-09 (budgets divided by 20) on 4_1 and 5_2:
4_1 converged at k = 5 to 21.547, certified at every doubling; 5_2 running correctly across invocations; the smoke
checkpoint deleted.
    python go.py benchmarks\foundations\seat_converge.py COMPLETE
    python benchmarks\foundations\seat_converge_verdict.py

## Cost
Point counts 120 to 280; doublings cost as N^2 x iterations: the torus rungs took 0.4 to 11 minutes to converge on
the PC; the braid and plat knots are 130 to 140 points. A converged knot is minutes; a walled knot runs to the cap,
about 40 minutes at these point counts. The night: ten knots in two to six hours, resumable if it runs long.

## Rules
No rescue; certificates before ledgers; the rule fixed; registrations and riders the author's; failure kept.

## Author's lock
LOCKED 2026-10-09 ("lock seat-converge"). The ten knots and their constructors, the rule, the certificates, the forms,
the wall test and the prior are fixed from this line; nothing in this file or in the two scripts is edited after a knot
has run at full budget.
