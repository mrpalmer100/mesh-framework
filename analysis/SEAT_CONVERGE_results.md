# COMMISSION SEAT-CONVERGE -- RESULTS (the PC, 2026-10-09 night; verdict computed once; the sandbox reproduces it)

Charter: analysis/SEAT_CONVERGE_charter_LOCKED.md (locked 2026-10-09 before any knot at full budget). Driver
benchmarks/foundations/seat_converge.py; verdict seat_converge_verdict.py on the sealed analysis/seat_converge_ckpt.pkl;
log analysis/SEAT_CONVERGE.log; verdict log analysis/SEAT_CONVERGE_verdict.log. Ten knots, every one certified at
construction and after every doubling (determinant at both tilts; the Alexander odd part for 6_1, 7_2, 8_1), every
one CONVERGED under the 1-percent rule (none walled, none refused); 35 minutes in all.

## VERDICT: STABLE-SET-[5, 7]; walls 6_1 WALL-STANDS, 7_2 WALL-STANDS

| knot | n | constructor | converged L/D | iterations | S | contacts | registered seat | literature ideal (the values the registry carries) | over literature |
|---|---|---|---|---|---|---|---|---|---|
| 3_1 | 3 | torus | 16.908 | 50000 | -13.43 | 3 | 16.84 | 16.37 | +3.3% |
| 4_1 | 4 | trace-closure braid (FND-MATTER-020) | 21.576 | 50000 | -18.16 | 5 | 21.64 | 21.04 | +2.5% |
| 5_1 | 5 | torus | 25.048 | 50000 | -19.78 | 3 | 25.09 | 23.55 | +6.4% |
| 5_2 | 5 | 3-strand word (FND-MATTER-021) | 26.660 | 200000 | -22.80 | 8 | 27.5 | (24.7) | (+8%) |
| 6_1 | 6 | plat word (FND-MATTER-023) | 34.456 | 100000 | -34.66 | 10 | 32.3 (wall) | 26.5 | +30% |
| 6_2 | 6 | 3-strand word | 32.582 | 200000 | -31.63 | 8 | first seat | 26.5 | +23% |
| 6_3 | 6 | 3-strand word | 30.451 | 50000 | -28.45 | 10 | first seat | 26.5 | +15% |
| 7_1 | 7 | torus | 31.452 | 200000 | -29.29 | 8 | 31.45 (KNOT-REACH-2) | 30.7 | +2.4% |
| 7_2 | 7 | plat word | 38.610 | 50000 | -39.66 | 12 | 38.6 (provisional) | (30.7) | (+26%) |
| 8_1 | 8 | plat word | 36.223 | 50000 | -35.27 | 11 | first seat | 32.7 | +11% |

(Literature values in parentheses are FND-MATTER-069's per-crossing-number entries applied to a knot the registry
did not cite individually; the comparison is indicative there, exact for 3_1, 4_1, 5_1, 7_1 and for the n = 6, 8
entries 069 carries.)

sigma(n) = min L/n over the converged table: n = 3: 5.636, 4: 5.394, 5: 5.010, 6: 5.075, 7: 4.493, 8: 4.528.
Strict local minima: n = 5 (5_1) and n = 7 (7_1). The same with or without walled knots (none were walled).

## What the result is, and what the prior got wrong

The prior said MONOTONE-NULL: FND-MATTER-069 had traced its stable set {5, 7} to the 4_1 stall anomaly (31.93) and
stated as a pre-registered sensitivity that resolving 4_1 toward the literature would collapse the set. 4_1 is now
converged at 21.58, within 2.5 percent of the literature, and the set {5, 7} SURVIVES. It survives for a different
reason than the one 069 named: the n = 6 and n = 8 entries are now the converged seats of the braid and plat knots
(6_3 at 30.45 and 8_1 at 36.22), which sit 15 and 11 percent above the literature ideals (26.5 and 32.7), while
the torus knots and 4_1 sit 2 to 6 percent above. With the registry's own literature values substituted at n = 6
and n = 8 and everything else converged, the minima move to n = 6 alone (sigma 5.636, 5.394, 5.010, 4.417, 4.493,
4.088), and with literature throughout the spectrum is monotone, as 069 recorded. So the stable set is real on the
converged table and is a property of the CONSTRUCTOR BASINS of the non-torus knots, not of the rope energetics: the
3-strand and plat closures descend into basins 11 to 30 percent above the ideal and the convergence rule, which
only adds iterations, does not leave them. That is FND-MATTER-023's basin lesson restated with converged numbers:
nativeness is not compactness; what the solver rewards is the start.

The walls. 6_1 converged at 34.46 from the plat word without the rounding preprocessor (the registered 32.3 came
through that preprocessor from a second start, FND-MATTER-023); it stands, and stands higher: the plat basin is the
shallower one and a converged budget does not cross between basins. 7_2 converged at 38.61, the provisional seat
to three digits: it was converged all along. Both WALL-STANDS; FND-MATTER-032's terminal grade (basin, not budget)
is confirmed under the strongest budget the registry has used, and the deep-basin search it named stays the open
item for these knots.

Solver systematic on the knots with exact literature values: +3.3, +2.5, +6.4, +2.4 percent, mean +3.7 (registered
+2.3). 5_1's +6.4 is the torus ladder's known local-contact arrangement (KNOT-REACH-2's record).

What this does for the target. SM_EMERGENCE row 10 and gap 5 gain nothing positive: the stability rule's output on
the registry's best table is a basin artifact, which is the same conclusion FND-MATTER-069 reached by a different
route ("absence of selection, not wrong scale"), now with the 4_1 route closed and the 6_x/8_1 route opened and
named. The rule cannot select a proton candidate on a table whose non-torus rows are basin-limited; the next real
step is the rearrangement mover FND-MATTER-024/032 specified and did not build, not more iterations.

## Consequences (riders on the author's word)
FND-MATTER-069: rider: the sensitivity statement corrected: 4_1 converged at 21.58 (2.5 percent over the literature)
  and the stable set {5, 7} survives; it now traces to the basin-limited seats of 6_3 (30.45, +15 percent) and 8_1
  (36.22, +11 percent); with the literature at n = 6 and 8 the minimum moves to n = 6 alone, with literature
  throughout the spectrum is monotone. The verdict (absence of selection) stands; its cause is relocated.
FND-MATTER-019: rider: the certified table under the convergence rule (all ten converged, the numbers above), beside
  the budgeted seats; solver systematic +3.7 percent on the knots with literature values.
FND-MATTER-021: rider: 5_2 converged at 26.66 (registered 27.5); 6_2 and 6_3 take their first converged seats
  (32.58, 30.45), both basin-limited against the literature 26.5.
FND-MATTER-023: rider: 8_1's first seat 36.22 (named next-order discharged); 7_2 confirmed at 38.61; the plat 6_1
  without the rounding preprocessor converges at 34.46, above the registered 32.3: the basin lesson confirmed.
FND-MATTER-032: rider: the 6_1 wall stands under a converged budget (WALL-STANDS); the terminal grade is confirmed
  as basin, not budget.
No status change; the five numbers unchanged; SM_EMERGENCE row 10 unchanged.

## Named next-order (not chartered)
The rearrangement mover (FND-MATTER-024/032's specification), run under the convergence rule on 6_1, 6_2, 6_3, 8_1
with the literature ideals as the pre-registered targets: the only road to a table on which the stability rule can
be read for energetics rather than for basins. A PC campaign, days, with its own charter; the author decides whether
gap 5's price (a ~1500-crossing object) makes a ten-crossing table worth it.
