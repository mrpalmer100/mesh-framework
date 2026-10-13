# v3.34.0 (13 Oct 2026) -- THE LAB ON THE RECORD: THE FIRST BEACON-SEEDED CONFRONTATION FAILS AND IS KEPT; THE MASS-VERSUS-CROSSING LAW MEASURED; THE NUCLEAR ROW'S MISSING TERM NAMED

## The five numbers (NORTH_STAR section 2b)

| Number | v3.33.0 | v3.34.0 | Delta |
|---|---|---|---|
| Fundamental dimensional inputs | 6 (Sigma, a, d_c, the nucleon mass unit, eps, hbar) | 6 | zero |
| Unexplained dimensionless constants | 4 named | 4 named (alpha via rho; m_p/m_e; g = l_q/a; kappa_pack) | zero |
| Imported physical laws | 1 (the quantum layer) | 1 | zero |
| Unique quantitative predictions (census T1) | 1 firm + 1 armed pin | 1 firm (PRED-003) + 1 armed pin (FND-106) | zero |
| Externally adjudicated predictions | 1 (NUC-BLIND-2) | 1 | zero (GRV-BLIND-1 passed on the author's draw; GRV-BLIND-2 failed on a beacon draw; neither adds) |

This release moves none of the five numbers. By section 2b's rule it is infrastructure, and it
says so in those words. What it carries is a kept failed confrontation of the programme's best
D1 content, six locked commissions rendered on the PC and in the sandbox between 8 and 9 October,
and the first promotion from the lab (the autonomous commission pipeline on the Mac mini), whose
files, decisions, digests and the GRV-BLIND-2 lineage reach main with this cut. SM_EMERGENCE rows
moved: none (1 derived, 4 partial, 7 unexplained). Derived-claim grades: unchanged (96 D0, 2 D1,
18 D2, 2 D3, 3 not applicable, of 121); the gravity row's D1 cell now states a pass and a fail.

**780 claims** (779 at v3.33.0). One new claim (GRV-129, Provisional, the lab's verdict-as-rendered
for GRV-BLIND-2, granting the author's act at promotion); no status changes; riders on prior
claims (FND-MATTER-019/021/023/032/066/069, NUC-A, NUC-022, QB-025, FND-185, GRV-030) accepted on
the author's word between 8 and 10 October; one new standing
instrument (tools/holdout_galaxies.py, the rotation-curve hold-out); the lab's own files under
benchmarks/lab/ and analysis/lab/.

## The one-paragraph version

The programme's zero-parameter prediction for the radial-acceleration scale of galaxies,
g_dagger = c H0 / 2 pi (GRV-030), was scored blind twice under the hold-out bar. On thirty SPARC
galaxies drawn by the author it passed (GRV-BLIND-1, rms 0.114 dex against a bar of 0.180); on
thirty drawn from a public randomness beacon, a drand round committed to the record before the
round existed, it failed (GRV-BLIND-2, rms 0.1656 against 0.1582; worst galaxy 0.632 against
0.522). The fail is kept at full weight and is not re-chartered. Two low-acceleration dwarfs carry
it, and the record shows the bars rule itself in the act: the worst held-out galaxy's rms equals,
to six figures, the bar GRV-BLIND-1 had set from the same galaxy when it sat in that draw's
training set; the beacon moved it, and the bars recomputed on the galaxies left behind tightened
as the test got harder. A rule whose bar moves away from the outliers exactly when the outliers
move into the test is measuring the draw as much as the prediction, and calibrating it is the
next charter on the gravity row (GRV-BLIND-OC), not a rescue of this one. The same week on the
PC: the mass-versus-crossing law the proton-topology price assumed was measured on the torus
ladder to n = 21 under a convergence rule (LINEAR, p = 0.96; the price of 1836 moves from ~1029
to ~1500 crossings); the registered certified knot table was re-seated under the same rule in 35
minutes and FND-MATTER-069's stable set survived with its cause relocated to the braid and plat
basins; and the nuclear row learned by name what its one single-particle well lacks: the
registered box closes 2, 8, 20, 34, 58, 92, 138 against nature's 2, 8, 20, 28, 50, 82, 126
(SHELLS-FAIL), the registered machinery has no l . s-class coupling (ORBIT-TWIST,
SO-NO-MECHANISM: the one handedness-times-sense term is flat in the winding number), and no
torsion price closes 28 without destroying 8 and 20 (NUC-SHELL-2, PRICE-NONE), so the row's
"Blocked by" cell is final at this level: the l-scaling of a spin-orbit splitting is the missing
physics, and no registered mechanism supplies it.

## What is new

### The lab (first promotion)
- benchmarks/lab/grv_blind_2/ (driver.py, verdict.py): the lab's commission driver and frozen
  verdict script, hashed with the lock (analysis/lab/locks/GRV-BLIND-2.v1.json, v2.json).
- analysis/lab/beacons/GRV-BLIND-2_round6543429.json: the commitment to drand round 6543429,
  made at 15:41:06Z, ten minutes before the round (15:51:30Z); seed rule recorded in the file
  (int of the first 8 hex digits, 31-bit). analysis/lab/decisions/: the three decision records
  (resolve-block, review-outcome, beacon-draw). analysis/lab/verdicts/GRV-BLIND-2.json.
  analysis/lab/digests/2026-10-10 to 2026-10-13.
- GRV-129 (Provisional): "GRV-BLIND-2: VERDICT AS RENDERED, BLIND-FAILS, DRAW-EXTERNAL,
  OUTLIER-EXCEEDS-BAR". The lab registers the forms verbatim when its reviewers do not pass the
  write-up after two revisions; the write-up (analysis/GRV-BLIND-2_results.md) carries the
  unresolved reviewer concerns at its foot. Granting is the author's act at promotion.
- The lab's own machinery (the runner, the agents, the governance database) lives outside this
  repository (mesh-lab on the Mac mini); its guide is docs/MESH_LAB_GUIDE.md on main since
  PR #1 and #2.

### GRV-BLIND-1 and GRV-BLIND-2 (the gravity row under bar W)
- tools/holdout_galaxies.py: the rotation-curve hold-out (draw splits each held-out galaxy into
  readable inputs and sealed observed velocities; seal; verdict with the two bars; writes LF on
  every platform). benchmarks/gravity/grv_blind_1.py: the predictor and the bars rule (95th
  percentile over 20,000 30-galaxy training subsets).
- GRV-BLIND-1 (author's draw, seed 52525254, PC): BLIND-AGREES, rms 0.1138 dex over 634 points
  (bar 0.1800), worst galaxy 0.380 (bar 0.632); mean residual +0.033. Rider on GRV-030 accepted
  2026-10-09.
- GRV-BLIND-2 (beacon draw, drand round 6543429, seed 1083026663, the lab): BLIND-FAILS, rms
  0.1656 over 647 points (bar 0.1582), worst galaxy PGC51017 0.6321 (bar 0.5224); mean residual
  -0.027; DRAW-EXTERNAL by the mechanical B-6 rule; the seed-rule departure from the amendment's
  wording disclosed at full weight in the write-up's section 7. Five galaxies overlap
  GRV-BLIND-1's hold-out; excluding them the rms is 0.1865, so the overlap does not produce the
  miss.
- Executor's sub-reading, computed after the truth and changing no form (recorded here, not in
  the lab's write-up, which declined to compute it): without PGC51017 the rms is 0.1602 (still
  over); without PGC51017 and UGC04305 it is 0.1438 (under). Both are low-acceleration dwarfs
  (g_bar 2 to 4 x 10^-11 m/s^2, 3 and 12 kept points) where the prediction sits 0.5 to 0.6 dex
  above the observed acceleration. PGC51017's 0.632099 equals GRV-BLIND-1's worst-galaxy bar
  (0.632099): it was in GRV-BLIND-1's training set, where it set that bar, and the beacon moved
  it into the test set.
- NORTH_STAR gravity row: D1 cell now "blind-scored under bar W: GRV-BLIND-1 BLIND-AGREES
  (0.114 dex, the author's draw); GRV-BLIND-2 BLIND-FAILS (0.166 dex, a beacon-seeded draw),
  kept". Section 2b: the fail disclosed beside the count; the count unchanged.

### KNOT-REACH-2 (the PC; 8 Oct)
- LINEAR, p = 0.9605 +/- 0.0378 on the eight rungs n >= 7, reach n = 21, every rung certified at
  both tilts and converged under the 1-percent rule before the cap. The price of 1836 under pure
  length moves from the assumed ~1029 crossings to ~1500 (band 1100 to 2000). Riders on
  FND-MATTER-066 and FND-MATTER-019; NORTH_STAR gap 5 reads "a ~1500-crossing object (measured)".
  The lineage KNOT-REACH to KNOT-REACH-2 is closed.

### SEAT-CONVERGE (the PC; 9 Oct)
- The registered certified knot table (3_1 to 8_1, ten knots from the registered constructors)
  re-seated under the convergence rule, certified at every doubling; all ten converged in 35
  minutes. STABLE-SET-[5, 7]; the 6_1 and 7_2 walls STAND. The stable set rests on the basin-
  limited seats of the braid and plat knots (6_3 +15 percent, 8_1 +11 percent over the
  literature), not on the 4_1 stall the prior assumed; with literature values the spectrum is
  monotone. Riders on FND-MATTER-069/019/021/023/032. The next road is a rearrangement mover.

### The nuclear row's missing term (the PC and the sandbox; 9 Oct)
- NUC-SHELL-1: SHELLS-FAIL. The registered box (r0 = 1.1197 fm) closes 2, 8, 20, 34, 58, 92, 138;
  AME2012's two-nucleon separation drops put nature's at 2, 8, 20, 28, 50, 82, 126; shared at 8
  and 20 only. A Strutinsky step was withdrawn before the lock (no plateau; the harmonic-
  oscillator control failed). Riders on NUC-A, NUC-022.
- ORBIT-TWIST: SO-NO-MECHANISM. Of the four enumerated cells, curvature and the contact law split
  linear polarizations only, the gyroscopic coupling is a Zeeman term blind to the orbital sense,
  and the geometric frame rotation along a path with torsion gives Delta omega = -sigma sign(m) c tau:
  the sign structure of l . s without its l-scaling (WRONG-FORM). Riders on QB-025, FND-185.
- NUC-SHELL-2: PRICE-NONE. No torsion tau R in [0, 2] closes the seven magic numbers or the first
  four together; 28 and 50 appear at tau R 0.8 to 0.9 only after 8 and 20 are destroyed; 82 and
  126 never. Rider on NUC-A; the row's "Blocked by" cell final at this level.

### Infrastructure
- Release 3.33.0's cold verify_corpus was interrupted by a container cycle and resumed from its
  cache; at this cut it stands at 171 claims passed, 0 failed, with the knot benchmarks ahead of
  it. CI (verify_corpus --skip-heavy) is the arbiter for the tag.
- STRATEGIC_TARGETS sections AF to AL. docs/VERIFY_STATUS.md is owed when the cold verify ends.

## Failures kept
GRV-BLIND-2 (BLIND-FAILS on a beacon draw; the first failed blind confrontation); NUC-SHELL-1
(SHELLS-FAIL), ORBIT-TWIST (SO-NO-MECHANISM), NUC-SHELL-2 (PRICE-NONE): the nuclear row's shell
lineage closed at NO MECHANISM with the missing term named; SEAT-CONVERGE's prior (MONOTONE-NULL)
wrong, recorded; NUC-SHELL-2's charter sentence for PRICE-NONE stricter than what happened (28
does appear), recorded; the GRV-BLIND-2 amendment's seed wording not matching the executed rule,
disclosed in the write-up and owed as a charter disclosure before this promotion; the lab's
"interior work" label on a rule-(c) commission, objected to by its reviewers and recorded.

## Scorecard delta (NORTH_STAR section 6)
Rows moved: none from blocked to derived. Gravity row: D1 content blind-scored twice, one pass
(author's draw) and one fail (beacon draw), both kept; grade column unchanged pending the
author's decision. Nuclear row: "Blocked by" final at this level (a spin-orbit-class splitting
with l-scaling; no registered mechanism). Inputs retired: none. Discriminators armed: none new;
the gravity row's bars rule named as the next instrument charter (GRV-BLIND-OC).

## In flight (next release)
COMPOSITE-SELECT Leg B (moved from the laptop to the Mac mini under the lab's runner; cell 13/9
of six at the move; the P32 upper edge and the Leg C price table wait on it). GRV-BLIND-OC (the
lab's backlog, rank 1: the bars rule's operating characteristic, bars fixed from the full eligible
set before any draw). The rearrangement mover for gap 5. The 3.33 and 3.34 tags wait on CI.
