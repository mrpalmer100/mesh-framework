# COMMISSION KNOT-REACH -- RESULTS (the PC, 2026-10-07; verdict computed once)

Charter: analysis/KNOT_REACH_charter_LOCKED.md (locked 2026-10-07 before any rung). Driver
benchmarks/foundations/knot_reach.py (one rung per invocation; launched through go.py); verdict
benchmarks/foundations/knot_reach_verdict.py; log analysis/KNOT_REACH.log (the PC's logs/knot_reach.log);
verdict log analysis/KNOT_REACH_verdict.log; sealed analysis/knot_reach_ckpt.pkl.

## VERDICT: REACH-SHORT, reach n = 5

The locked form: "fewer than three certified rungs at n >= 7: no law is read; the reach is registered
(K5) and nothing else." Rungs 3 and 5 certified at both ends and within the 3-percent grade; rung 7
certified at both ends (determinant 7 before and after tightening, at both tilts) but failed the grade:
the tightened length moved from 33.74 at half the budget to 31.54 at the full budget, 7.0 percent, still
shrinking. By B-5 the rung is the reach and the budget is not raised inside this commission. The ladder
stopped at 7; rungs 9 to 21 were not run.

| n | N | iterations | L/D (full) | L/D (half) | grade | S | contacts | certified |
|---|---|---|---|---|---|---|---|---|
| 3 | 120 | 25000 | 16.894 | 16.896 | 0.0001 | -13.418 | 3 (len 26.47) | yes |
| 5 | 200 | 41666 | 25.049 | 25.196 | 0.0059 | -19.779 | 3 (len 39.01) | yes |
| 7 | 280 | 58333 | 31.535 | 33.740 | 0.0699 | -29.536 | 7 (len 58.34) | certificate yes, grade no |

Rungs 3 and 5 reproduce the registered seats (FND-MATTER-007: 16.844 and 25.09) to 0.3 and 0.2 percent,
as the pre-lock check did in the sandbox. Times: 0.3, 1.5 and 5.3 minutes.

## What the result is

An instrument-budget result, not a result about the law. The iteration rule fixed at lock (25000 n/3,
the trefoil's registered budget scaled linearly in n) under-budgets the tightener as the point count
grows: the tightener relaxes a closed curve by local moves, and its relaxation time grows faster than
the point count, so a budget linear in n leaves the 280-point rung unconverged by 7 percent. FND-MATTER-019
did not use a rule; it chose budgets per knot (22000 for the trefoil at 110 to 150 points, 45000 for the
composites at 180 points), which is why its seats are converged and this ladder's seventh rung is not.
The registry's own statement of the solver grade, "3 percent on 5-crossing knots" (FND-MATTER-066), is
reproduced exactly as the reach under this rule. Nothing about the mass-versus-crossing law is learned;
FND-MATTER-066's "about a thousand crossings under pure length" keeps its status as an assumption.

The partial rung is still informative as a record (not read into any form): at n = 7 the certified knot
has 7 contact clusters (the torus rungs at 3 and 5 have 3), and its length at the budget's end was
still falling, so 31.5 is an upper bound on the seat, not the seat.

## Consequences (riders on the author's word)

FND-MATTER-019: rider recording the reach under a linear budget rule (n = 5 at 3-percent grade; the
seventh rung unconverged at 7 percent after 58333 iterations on 280 points) and that its own seats used
per-knot budgets, not a rule.
FND-MATTER-066: rider recording that KNOT-REACH did not reach the law; the thousand-crossing demand
remains the pure-length assumption it was.
No status change; no scorecard movement; the five numbers unchanged.

## Named next-order: the one repair (section 5), for the author's word

KNOT-REACH-2: the same ladder, the same certificates, the same grade test and the same fit window, with
ONE change: the budget rule replaced by a convergence rule. Each rung is tightened in doublings of the
registered trefoil budget (25000, 50000, 100000, ...) until the length changes by under 1 percent between
successive doublings (a stricter bar than the 3-percent grade, so the grade test is passed with margin),
capped at 1.6 million iterations; a rung that hits the cap unconverged is the reach. The rule is fixed in
the charter before any rung and is not tuned after one. Cost: rung 7 at perhaps 200,000 iterations
(about 20 minutes), rung 21 at the cap about a day; the ladder a day or two on the PC. The lineage then
stops whatever it returns.
