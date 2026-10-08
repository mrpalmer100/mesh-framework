# COMMISSION KNOT-REACH -- THE MASS-VERSUS-CROSSING LAW ON THE TORUS LADDER, TO THE SOLVER'S REACH
# (CHARTER, LOCKED 2026-10-07 on the author's word, before any rung; the PC's job)

North Star line (section 5): prices gap 5 of section 4 (the proton's topology; FND-186). FND-MATTER-066
(Failed, kept) recorded that m_p/m_e = 1836 is spectrum-gated: "1836 demands >= ~343 trefoil-equivalents
(>= ~1029 crossings) UNDER PURE LENGTH", on a solver certified to 3 percent at 5 crossings. The words
"under pure length" are an assumption: that the tightened length of a knot grows linearly with its
crossing number. This commission measures that law on the one family the registry certifies by
determinant alone (the torus knots T(2,n), det = n, FND-MATTER-019 seats 3_1, 5_1, 7_1), marched to
the solver's reach. It does not build the proton (NUC-003) and does not change gap 5's status; it
replaces "about a thousand crossings" with a measured exponent and coefficient, which is the price a
future proton topology is checked against. Expected by the mathematics of ropelength: LINEAR. The
honest product is the coefficient and the solver's certified reach, both of which the registry lacks.

## Steps
  K1  THE LADDER. T(2,n) for n = 3, 5, 7, 9, 11, 13, 15, 17, 19, 21 from the registered parametrisation
      ((2 + cos n t) cos 2t, (2 + cos n t) sin 2t, sin n t) scaled as FND-MATTER-019 scales the trefoil,
      with the point count scaled with n (N = 40 n, the trefoil's 120 at n = 3), tightened with the
      registered instrument (two_term_mass_model.tighten_coords; iterations scaled as 25000 n/3,
      checkpointed per knot so the march resumes). Each knot CERTIFIED at both ends (topology_certifier
      .knot_det == n before and after tightening, at both registered tilts); a knot whose certificate
      fails after tightening is REFUSED at that n and the ladder stops there: that n - 2 is the reach.
  K2  THE LEDGER per knot, as FND-MATTER-019 reads it: tightened length L (in units of D), the
      zero-point second term S by the registered profile, contact count and contact length.
  K3  THE LAW. On the certified rungs with n >= 7 (below that the small-n offset dominates), fit
      log L = p log n + c by least squares; report p with its standard error and the same for the
      two-term mass at the registered coupling window lam in {0, 0.3} (FND-MATTER-019's window).
      Also the per-crossing cost dL/dn on the top three rungs.
  K4  THE PRICE. Under the measured law, the crossing number at which the pure-length mass ratio to the
      trefoil reaches 343 (FND-MATTER-066's demand) and the mass ratio to the ring reaches 1836; stated
      as a number with the fit's error band. Not a prediction: a price.
  K5  THE REACH, registered: the largest n certified at 3-percent grade (the registered grade test:
      the tightened length changes by < 3 percent between the two iteration budgets 0.5x and 1x).

## Bars (LOCKED)
B-1  Certificates at both ends at both tilts, or the rung is REFUSED by name. No rung is kept without
     its determinant.
B-2  The fit window (n >= 7), the point-count rule (40 n) and the iteration rule (25000 n/3) are fixed
     here and not tuned after a rung disappoints.
B-3  No knot is named a particle (FND-MATTER-019's own rule). The price (K4) is reported as a crossing
     number, not as a candidate.
B-4  The prior is stated and not leaned on: LINEAR (p in [0.9, 1.1]).
B-5  One march; a rung that fails its grade test (K5) is the reach, not a reason to raise the budget.

## Verdict forms (LOCKED)
LINEAR        p in [0.9, 1.1]: FND-MATTER-066's thousand-crossing demand is confirmed with a measured
              coefficient; FND-MATTER-066 takes a rider carrying the number; gap 5's price is "a
              ~<K4> crossing object plus NUC-003's layer".
SUPERLINEAR   p > 1.1: fewer crossings than FND-MATTER-066 assumed reach 1836; the price falls to the K4
              number; FND-MATTER-066's "spectrum-gated" stands with a smaller gate; rider.
SUBLINEAR     p < 0.9: more crossings than assumed; the hierarchy is harder than stated; rider.
REACH-SHORT   fewer than three certified rungs at n >= 7: no law is read; the reach is registered
              (K5) and nothing else.
In every form the registered solver reach (K5) is recorded on FND-MATTER-019 by rider.

## Rules
No rescue; certificates before ledgers; the fit window fixed; registrations and riders the author's;
failure kept.

## Reads owed at lock
FND-MATTER-019's benchmark (the trefoil parametrisation, scale, point count, iteration budget, the
ledger and the lam window); topology_certifier.knot_det (the two tilts); FND-MATTER-066 (the 343 and
1029 arithmetic, reproduced before K4 is read); FND-MATTER-021/023 (the 3-percent grade definition).

## Cost
The PC: ten rungs, the top rung at 840 points and 175,000 iterations of the pure-numpy tightener. Measured
in the sandbox at the registered rule: rung 3 in 13 s, rung 5 in 56 s; the pair count grows as n^2 and the
iterations as n, so rung 21 is about an hour and the ladder about three hours. One rung per invocation,
checkpointed (analysis/knot_reach_ckpt.pkl), launched through go.py with the terminal pattern COMPLETE.

## Pre-lock instrument check (sandbox, 2026-10-07; discarded, not a result)
benchmarks/foundations/knot_reach.py run in smoke mode at the registered rule on rungs 3 and 5 reproduced
the registered seats (L/D 16.894 against 16.844; 25.046 against 25.09), both certified at both tilts, grade
1e-4 and 6e-3. knot_reach_verdict.py on a synthetic linear ladder returned p = 1.00 and priced 1836 at about
1000 crossings, matching FND-MATTER-066's arithmetic, so the price formula agrees with the registry before any
real rung is read. The smoke checkpoint was deleted; the PC runs every rung, including 3 and 5, fresh.

## Author's lock
Locked on the author's word on 2026-10-07 ("lock knot-reach"). No rung had run on the PC; the sandbox's
smoke rungs were deleted. Driver benchmarks/foundations/knot_reach.py; verdict benchmarks/foundations/knot_reach_verdict.py
(both delivered before the lock and unchanged after it).

## READS AT LOCK
FND-MATTER-019's benchmark (certified_spectrum.py): trefoil parametrisation ((2 + cos 3t) cos 2t, (2 + cos 3t) sin 2t,
  sin 3t) x 1.8 at 120 points, tightened 25000 iterations; the ledger (profile -> local-loop zero-point term with
  A_C = -0.509658, B_C = 2 pi (5/2 - 7 sqrt 2/4), DIR = -0.502506; contact_phys); lam window {0, 0.3}. The ring
  closes at L = pi (the third anchor): m(ring) = pi D with S = 0 by the registered anchor.
topology_certifier.knot_det: determinant by Goeritz-class colouring at tilt 0.013 (default) and 0.11 (the second
  registered tilt used by FND-MATTER-019's certificates). T(2,n) has determinant n.
FND-MATTER-066 (Failed, kept), verbatim: "1836 demands >= ~343 trefoil-equivalents (>= ~1029 crossings) under pure length -- the fully dimensionless restatement of FND-MATTER-007's ~5,767 / ~30,921 arithmetic, reproduced exactly, with the granny sub-additivity check (31.59 < 2 x 16.84) making the factor a LOWER bound -- and that thousand-crossing region is uncertified (solver grade is 3-percent on 5-crossing knots). PRIMARY POSITIVE FINDING (the session's registrable advance): the registered zero-point second term is measured ANTI-HIERARCHICAL -- against the ring floor it caps ratios at 9.04 and among knots it COMPRESSES toward 1 (the registered 1.491 -> 1.156 lever, cited not recomputed here) -- so within the registered two-term energetics the second term CANNOT be the source of a three-order hierarchy".
  The 343 and 1029 are the targets K4 prices under the measured law; the synthetic check reproduced ~1000.
FND-MATTER-021/023: the 3-percent solver grade (seats stable to 3 percent between budgets), applied here as K5.
FND-MATTER-007: trefoil 16.844 and 5_1 25.09 are the registered seats the pre-lock check reproduced to 0.3 and
  0.2 percent.
