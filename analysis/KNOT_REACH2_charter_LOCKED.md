# COMMISSION KNOT-REACH-2 -- THE TORUS LADDER UNDER A CONVERGENCE RULE
# (CHARTER, LOCKED 2026-10-07 by the author before any rung; the PC's next job)

Lineage: KNOT-REACH (analysis/KNOT_REACH_charter_LOCKED.md, results analysis/KNOT_REACH_results.md) returned
REACH-SHORT at reach n = 5: the seventh rung stayed certified but was unconverged at 7 percent under the
locked linear iteration rule 25000 n/3. The failure was the instrument's budget, not the law. NORTH_STAR
section 5 permits one repair to the point where the pending verdict can be read, after which the lineage
stops. This is that repair. ONE thing changes: the iteration rule. Everything else is carried over from the
locked KNOT-REACH charter by reference: the ladder (K1: T(2,n), n = 3 to 21, the FND-MATTER-019
parametrisation at scale 1.8, 40 n points), the certificates (B-1: det == n at both tilts, before and after),
the ledger (K2), the law and its fixed window (K3: n >= 7), the price (K4), the forms and the band (LINEAR
[0.9, 1.1], SUPERLINEAR, SUBLINEAR, REACH-SHORT), the prior (B-4) and the no-particle rule (B-3).

## The one change (C-1, to be LOCKED)
C-1  THE CONVERGENCE RULE. Each rung is tightened to cumulative budgets 25000 x 2^k, k = 0, 1, 2, ... (the
     trefoil's registered budget, doubled), the tightener resumed from the previous doubling's coordinates
     (its state is the curve alone; resumption is exact up to the pair-mask refresh). The rung is CONVERGED
     at the first k >= 1 at which the tightened length differs from the previous doubling's by under 1
     percent; its recorded length, ledger and grade are that doubling's. The 1-percent bar is stricter than
     the registered 3-percent grade (FND-MATTER-021/023), so the grade test (K5) is passed with margin by
     construction and the verdict script's grade filter is unchanged. The cap is 1,600,000 iterations
     (k = 6). A rung still moving by 1 percent or more at the cap is the reach-failure: the ladder stops
     there and the reach is the rung below. Certificates are checked after EVERY doubling, not only at the
     end; a loss at any doubling is REFUSED by name and the ladder stops.
     The rule is fixed here before any rung and is not tuned after one (B-2 carried over: the point-count
     rule, the fit window and this rule are the fixed things). The cap is not raised inside this commission
     (B-5 carried over).

## Bars (carried over, with C-1 in place of the linear rule)
B-1  certificates at both ends at both tilts, now at every doubling; B-2 fixed rules; B-3 no knot named a
     particle; B-4 the prior stated, not leaned on; B-5 one march, a rung at the cap is the reach.

## Verdict forms (unchanged, LOCKED by reference)
LINEAR, SUPERLINEAR, SUBLINEAR as KNOT-REACH locked them; REACH-SHORT if fewer than three rungs are certified
at n >= 7. In every form the reach under the convergence rule is recorded on FND-MATTER-019 by rider, next to
the reach under the linear rule. If REACH-SHORT returns a second time the lineage stops with the two reaches
registered and no further repair; the thousand-crossing demand of FND-MATTER-066 stays an assumption.

## Instrument
benchmarks/foundations/knot_reach2.py (one doubling per invocation; checkpoint analysis/knot_reach2_ckpt.pkl,
atomic; KNOT-REACH's sealed checkpoint is never opened); verdict benchmarks/foundations/knot_reach_verdict.py
on that checkpoint (the same script, the same forms). Launched through go.py:
    python go.py benchmarks\foundations\knot_reach2.py COMPLETE
    python benchmarks\foundations\knot_reach_verdict.py analysis\knot_reach2_ckpt.pkl

## Cost
Rung 7 at perhaps 200,000 iterations (about 20 minutes); the cost per iteration grows as n^2 and the budget
to convergence is unknown above 7, so rung 21 at the cap is about a day; the ladder a day or two on the PC.
Rungs 3 and 5 are re-run fresh under the new rule (they are cheap and the rule must apply to every rung).

## Pre-lock instrument check (sandbox, 2026-10-07; discarded, not a result)
The driver in smoke mode (budgets divided by 20) on rungs 3 and 5: both converged at k = 3 with changes
0.0006 and 0.0011, certified at every doubling, seats 16.900 and 25.208 against the registered 16.844 and
25.09; one doubling per invocation resumed correctly across eight invocations; the verdict script read the
smoke checkpoint and returned REACH-SHORT (0 rungs at n >= 7), as it must with two rungs. The smoke
checkpoint was deleted; the PC runs every rung fresh.

## Author's lock
LOCKED 2026-10-07 ("let's lock knot reach 2"). C-1 (the convergence rule: doublings of 25000, the 1-percent
bar, the 1,600,000 cap, certificates at every doubling), the carried-over bars, the fixed window and the forms
are fixed from this line; nothing in this file or in benchmarks/foundations/knot_reach2.py is edited after a rung
has run. One repair; the lineage stops at the verdict.
