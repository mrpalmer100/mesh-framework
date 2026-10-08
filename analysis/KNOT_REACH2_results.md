# COMMISSION KNOT-REACH-2 -- RESULTS (the PC, 2026-10-08; verdict computed once)

Charter: analysis/KNOT_REACH2_charter_LOCKED.md (locked 2026-10-07 before any rung; the one repair of KNOT-REACH's
REACH-SHORT: the linear iteration rule replaced by a convergence rule, C-1). Driver benchmarks/foundations/knot_reach2.py
(one doubling per invocation, launched through go.py); verdict benchmarks/foundations/knot_reach_verdict.py on the
sealed checkpoint analysis/knot_reach2_ckpt.pkl (the same locked forms as KNOT-REACH); log analysis/KNOT_REACH2.log;
verdict log analysis/KNOT_REACH2_verdict.log. The sandbox verdict on the sealed checkpoint is the verdict of record.

## VERDICT: LINEAR (p = 0.9605 +/- 0.0378; band [0.9, 1.1]); reach n = 21 (the full ladder)

| n | N | iterations to converge | L/D | change at last doubling | S | contacts (len) | certified |
|---|---|---|---|---|---|---|---|
| 3 | 120 | 50000 | 16.908 | 0.0008 | -13.429 | 3 (26.49) | yes |
| 5 | 200 | 50000 | 25.048 | 0.0055 | -19.776 | 3 (39.01) | yes |
| 7 | 280 | 200000 | 31.452 | 0.0014 | -29.289 | 8 (57.85) | yes |
| 9 | 360 | 400000 | 44.370 | 0.0076 | -42.105 | 14 (83.19) | yes |
| 11 | 440 | 400000 | 53.541 | 0.0052 | -56.094 | 17 (110.92) | yes |
| 13 | 520 | 200000 | 59.230 | 0.0053 | -63.890 | 13 (126.32) | yes |
| 15 | 600 | 100000 | 68.021 | 0.0023 | -67.257 | 25 (132.81) | yes |
| 17 | 680 | 100000 | 76.900 | 0.0012 | -81.251 | 34 (160.59) | yes |
| 19 | 760 | 50000 | 88.319 | 0.0079 | -96.143 | 39 (190.06) | yes |
| 21 | 840 | 200000 | 93.334 | 0.0070 | -103.410 | 36 (204.39) | yes |

Every rung certified (det == n at tilts 0.013 and 0.11, before and after every doubling); every rung converged
under the 1-percent bar before the 1.6-million cap (the deepest was 400,000 iterations, rungs 9 and 11). Total PC
time about five hours. Rungs 3 and 5 reproduce FND-MATTER-019's registered seats (16.84, 25.09) to 0.4 and 0.2
percent; rung 7 (31.45) is the ladder's first seat beyond the registered table and sits within a few percent of the
literature ideal for 7_1, as the solver's registered grade allows.

## K3 the law
Pure length on n >= 7 (fixed window): log L = 0.9605 log n + 1.6328, p = 0.9605 +/- 0.0378 (8 rungs). The two-term
mass at the registered coupling window: p = 0.9605 at lam = 0 (the same fit) and p = 0.897 +/- 0.039 at lam = 0.3,
the zero-point term pulling the exponent to the band's lower edge within one standard error (reported, not read into
the form: the locked form reads the pure-length exponent). Per-crossing cost on the top three rungs: 5.71 D
(17 to 19) and 2.51 D (19 to 21); the mean over the ladder is 4.2 D per crossing at the top against 5.6 D per
crossing at the trefoil, which is the sublinear tilt the exponent records.

## K4 the price (a price, not a prediction; B-3: no knot is named a particle)
Under the fitted pure-length law, with m(3_1) = 16.908 D and m(ring) = pi D (the registered anchor):
  m/m(3_1) = 343 at about 1514 crossings (band 1147 to 2043 over p +/- one standard error);
  m/m(ring) = 1836 at about 1505 crossings (band 1141 to 2031).
FND-MATTER-066 assumed about 1029 crossings "under pure length" with the trefoil's per-crossing cost held fixed; the
measured law, with its slightly sublinear exponent, raises the price by about half: the thousand-crossing-class gate
is a fifteen-hundred-crossing-class gate, with a band from eleven hundred to two thousand.

## What the result is
The mass-versus-crossing law on the one family the registry certifies by determinant alone is LINEAR to within the
locked band, measured rather than assumed, with its coefficient and the solver's certified reach (n = 21 at 840
points under the convergence rule) now on the record. It confirms the structure of FND-MATTER-066's argument (1836
demands a thousand-crossing-class object under pure length) and corrects its number upward. It does not build the
proton, does not change gap 5's status (NORTH_STAR section 4: the proton topology is still unregistered), and does
not touch the registered second term's anti-hierarchical finding. The lineage KNOT-REACH to KNOT-REACH-2 is closed
by its charter: one repair, then it stops.

Recorded, not read: the contact count is not monotone in n (17 at n = 11, 13 at n = 13, 39 at n = 19, 36 at
n = 21), and rung 13 converged at half the budget of rungs 9 and 11, which says the tightener settles into different
local contact arrangements on neighbouring rungs; the 1-percent rule and the 3-percent grade both admit this, and
the fit's standard error carries it. A future commission that wants the coefficient to better than a few percent
needs a solver with a convergence certificate, not a budget rule.

## Consequences (riders on the author's word)
FND-MATTER-066: rider: KNOT-REACH-2 measured the law this claim assumed: LINEAR, p = 0.96 +/- 0.04 on T(2,n) for
  n = 7 to 21; the price of 1836 under pure length is about 1500 crossings (band 1100 to 2000), up from the
  assumed ~1029; "spectrum-gated" stands with the gate measured.
FND-MATTER-019: rider: the solver's certified reach under the convergence rule is n = 21 (840 points, 200,000
  iterations); next to the linear-rule reach n = 5 (KNOT-REACH); the torus seats 7 through 21 are on the record
  in analysis/knot_reach2_ckpt.pkl, certified at both tilts, converged to 1 percent.
docs/NORTH_STAR.md section 4, gap 5: the price line becomes "a ~1500-crossing object (measured, KNOT-REACH-2;
  band 1100 to 2000) plus NUC-003's layer".
No status change; scorecard rows unchanged; the five numbers unchanged (a price is not a prediction).

## Named next-order (not chartered)
None in this lineage. The honest next question for gap 5 is not the law but the object: a registered proton
topology (NUC-003's unbuilt layer) that a ~1500-crossing price can be checked against.
