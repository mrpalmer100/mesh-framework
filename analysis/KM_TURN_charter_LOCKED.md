# COMMISSION KM-TURN -- WHAT HAPPENS AT A2 ~ 0.0073 ON THE ANTI-ALIGNED FAMILY
# (CHARTER, LOCKED 2026-09-18 on the author's word; before any new solve)

## Question
KERNEL-MARCH-2 (FND-177) found a sharp turn at A2 ~0.0073: rate -40 pct in two
steps, f_dir 0.59 -> 0.43, the family leaving the resonance. Three hypotheses:
(a) a fold of the resonant family, the march continuing onto its non-resonant
continuation; (b) a branch switch induced by the bordering constraint once the
degeneracy was nearly lifted; (c) a continuous bend of a single branch.

## PRE-RUN FINDING (Test C, from the sealed states, no new solve; recorded
## before the forms were fixed): the turn is CONTINUOUS in state space. Arc
## step lengths p38..p56 stay at ds = 0.08 (p46 -> p47: 0.097, a 21 pct
## overshoot at the bend); the tangent turns 13.6 deg (p45 -> p46) then 34.3
## deg (p46 -> p47), then relaxes to ~1 deg per step. A discontinuous switch
## (step >> ds, angle ~90 deg or more) is excluded. What remains: fold vs
## bordered-induced bend vs intrinsic bend.

## Protocol (two tests, the PC)
TEST A -- BACKWARD MARCH. From the sealed p50 and p51 states, the bordered arc
  march with the tangent reversed (from p51 toward p50 and on), ds 0.08, 12
  points, measurements sealed. Compare, point by point, to the forward
  states p49, p48, ... p38: the relative state distance d_k = |x_back_k -
  x_fwd_(50-k)| / |x|. RETRACE means d_k < 1e-3 at every k. HYSTERESIS means
  d_k > 1e-2 at some k with the backward march still gated.
TEST B -- PLAIN-GN MARCH THROUGH THE TURN. From the sealed p38 and p39 states
  (regular branch, GN gates there), the stage-2c arc march with the PLAIN
  credentialed solver (gn_sparse, 60 rounds, no bordering), ds 0.08, 15
  points (to A2 ~0.0081), measurements sealed. SAME EVENT means: rate falls
  below 1.0e-3 within 2 points of A2 0.0073 and f_dir falls below 0.50. NO
  EVENT means: rate > 1.3e-3 and om2 within 5e-5 of -Om1/4 at A2 >= 0.0076.
  REFUSED means fewer than 6 points gated.

## Verdict forms (LOCKED)
TURN-INTRINSIC-BEND: A retraces AND B sees the same event.
TURN-FOLD:           A shows hysteresis AND B sees the same event (or B
                     refuses at the turn).
TURN-SWITCH:         B sees NO event (the resonant branch continues past
                     0.0076 under the plain solver): an instrument artifact.
TURN-UNRESOLVED:     any other combination.

## Rules
No rescue; q-sweep bars; bordered solver for A, the plain credentialed solver
for B; one machine; verdict once from the sealed checkpoint; FND-177 riders
inherited.
