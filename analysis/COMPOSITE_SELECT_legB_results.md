# COMPOSITE-SELECT -- LEG B RESULTS (QB, the cell question) AND LEG C (QC, the price table), 2026-10-19

Charter analysis/COMPOSITE_SELECT_charter_LOCKED.md (gating amendment of 2026-09-05: two refinements per cell,
36 and 54 densities, the 20 percent D convergence bar, a 20-point profile budget per cell at 54). Driver
benchmarks/foundations/composite_legB.py; verdict benchmarks/foundations/composite_legB_verdict.py, written
2026-10-04 and dry-run before any Leg B number existed (analysis/COMPOSITE_SELECT_legB_verdict_readiness.md).
Run as lab job legB on the Mac mini (the one machine for this job; moved there from the laptop on 2026-10-13 at
42.7 GB booked), 136 invocations, every invocation sealed, LADDER COMPLETE on 2026-10-19. The verdict was computed
once from the sealed checkpoint on the mini: analysis/COMPOSITE_SELECT_legB_verdict.log (sha256
85c263ed452ed9d23f04bc62c998be2346f95531ce02e0741dbc7ebf38f51015).

The sealed checkpoint composite_legB_ckpt.pkl is 122 MB (sha256
557d071b57e897d1bd6490b39616084f384689a5c933ab01f3efb43e823169f0) and stays on the machine of record (the mini's
job tree ~/mesh-compute/jobs/legB/tree/analysis/) and in the author's keeping. The repository carries
analysis/composite_legB_ckpt_verdict_extract.pkl (4.4 MB, sha256
3d4a5a06a9a9eefa2c5fefcfe1e322598a27973665001ee19824520df9a6040d): the six cell records with every per-point
measurement, member scalars and phase, and of the solver states only the one the price step reads per profile (the
deepest full-bar member), the rest replaced by None with a note; built by tools/legb_ckpt_extract.py. The verdict
script run on the extract reproduces the mini's log byte for byte (checked 2026-10-19 in the sandbox, which is not
a machine of record; the log of record is the mini's).

## 1. What was run

Six new rational cells at the registered density (48 s-points per sqrt 3), approaching q = 1.492 from both sides:
7/5, 10/7, 13/9 below and 8/5, 11/7, 14/9 above (N1 = 5, 7, 9). Per cell: level-1 recovery, the ramp to the gate,
then the rate profile marched at NP = 36 (prof36), continued to 54 (cont54) and marched again at 54 (prof54), 20
full-bar points per profile. The N1 = 9 cells (432 x 36, 432 x 54) cleared the memory clause: the job booked
42.7 GB on the mini and no cell was closed by the spike rule. No cell halted; every cell reached phase done.

D(q) exactly as Q-SWEEP stage 1 defined it: the rate at the full-bar point nearest A2 = 0.0048 over the rate at
the full-bar point nearest 0.0063, nearest-point pairing, full-bar states only (RMS < 1e-8, closure < 1e-6). The
existing cells enter as data by the same rule: 3/2 from the registered stage-1 constants, 4/3 and 5/3 from
analysis/qsweep_stage1_ckpt.pkl (FND-147). 5/4 has no D at the matched definition on the record (FND-163/164
report f_dir rises and rate changes over 0.0048 to 0.0052 and a collapse before 0.0063 is reached), nothing was
entered, and the script reports it NOT LOADABLE; it stays out of the ladder, as the readiness note said it would.

## 2. The ladder (sealed; from the verdict log)

| cell | q | N1 | D at 36 | D at 54 | A2 window paired (36) | A2_max 36 / 54 | om2 at the low point |
|---|---|---|---|---|---|---|---|
| 7/5 | 1.4000 | 5 | 1.06x | 1.05x | 0.00479 to 0.00537 | 0.00537 / 0.00532 | +2.64485 |
| 8/5 | 1.6000 | 5 | 1.05x | 1.04x | 0.00479 to 0.00537 | 0.00537 / 0.00532 | +3.90115 |
| 10/7 | 1.4286 | 7 | 1.04x | 1.04x | 0.00480 to 0.00527 | 0.00527 / 0.00522 | +2.82672 |
| 11/7 | 1.5714 | 7 | 1.04x | 1.04x | 0.00480 to 0.00527 | 0.00527 / 0.00522 | +3.72415 |
| 13/9 | 1.4444 | 9 | 1.04x | 1.03x | 0.00479 to 0.00520 | 0.00520 / 0.00516 | +2.92671 |
| 14/9 | 1.5556 | 9 | 1.04x | 1.03x | 0.00479 to 0.00520 | 0.00520 / 0.00516 | +3.62469 |
| 3/2 (existing) | 1.5000 | 2 | 9.56x | | registered constants | | |
| 4/3 (existing) | 1.3333 | 3 | 5.31x | | 0.0063 unreached; best 0.005042 | | |
| 5/3 (existing) | 1.6667 | 3 | 1.11x | | target reached | | |

Every new cell has 20 full-bar points at each density. The 20 percent convergence bar of the gating amendment is
met with room: D differs between 36 and 54 by at most 1 percent at every cell. The 0.0063 target was not reached by
any new cell (A2_max 0.0052 to 0.0054), so the nearest-point rule paired the low point against the cell's deepest
full-bar member, as it did for 4/3 in stage 1 under the unreached-target clause; the rates in the log are the
rates at the points named.

## 3. QB, the order test (D4, rank-based, computed once)

| grid | cells with a D | rho(D, q) | rho(D, N1) | form |
|---|---|---|---|---|
| NP 36 | 9 | -0.167 | -0.983 | RAT-RESONANT |
| NP 54 | 6 (the new cells) | -0.257 | -0.956 | RAT-RESONANT |

Against the locked thresholds (RAT-RESONANT: |rho(D, N1)| >= 0.8 and |rho(D, q)| < 0.5) the form fires at both
densities, and not at the margin. The readiness note's pre-data finding was that RAT-SMOOTH could not fire on this
ladder (the registered cells cap |rho(D, q)| at 0.767) and that RAT-RESONANT could fire "only barely"; the data
exceeded that: with the existing cells in, |rho(D, N1)| is 0.983, and on the six new cells alone 0.956.

What the ladder shows in words: the low-order cells collapse inside the window (3/2 at N1 = 2 by 9.56x, 4/3 at
N1 = 3 by 5.31x, both within 0.0048 to 0.0051), and every cell of order 5, 7 and 9 marches through the same window
and past it with a decline of 3 to 6 percent, at both densities. The cells bracketing the physical ratio most
closely (13/9 at 1.4444 and 14/9 at 1.5556, which sit 3.2 and 4.3 percent from 1.492) are the flattest. Cells at
nearly the same q behave differently when their order differs (7/5 at 1.400 and 4/3 at 1.333 are 5 percent apart
in q; one is flat, the other collapses), and cells far apart in q behave alike when their order matches (7/5 and
8/5). A smooth function of the ratio value cannot produce that pattern; a function of the commensurability order
does.

## 4. QB consequences, as the charter pre-registered them (executed only on the author's word)

RAT-RESONANT's locked reading: the collapse tracks the cell's commensurability order, not the physics; it is an
artifact of the rationalized instrument. The charter's consequences:
(a) FND-147, FND-151, FND-152, FND-153 and FND-163 gain a CELL-SCOPE rider: their collapse statements describe
    rational cells of low order, not the quasi-periodic state. The claims stand as rendered (every one was computed
    under its own locked rules); the rider says what they are about.
(b) The physical branch at q = 1.492 is read from the highest-denominator cells: at N1 = 9 the aligned family does
    not collapse through 0.0048 to 0.0052 (D 1.03 to 1.04 at both densities); its A2_max under the registered
    protocol and budget is 0.0052 (36) and 0.0052 (54).
(c) The anti-aliased continuum of the state becomes the next instrument question (a charter of its own; nothing
    here designs it).
What is NOT a consequence: the phenomenology at 5/4 (FND-163/164, physical and grid-displaced) is not re-read; it
is a low-order cell and (a) applies to it as to the others. The author's FLAT prediction of record for 5/4 stays
falsified as rendered; what this leg adds is that FLAT is what the high-order cells do.

## 5. QC, the price table (D5; a table, not a verdict)

Sigma_wave by FND-135's closed form (truestate_stage2.Grid.price on the state exported by QTGrid.to_stage2), per
strand per axial length, in units of T0; the Prediction 32 share as 1 - T0 / Sigma_wave (FND-132); the kb ceiling
consequence left to the desk (FND-141's 0.09332 chain).

| row | member | Sigma_wave | P32 upper edge | grid scope |
|---|---|---|---|---|
| (i) A2* selected by QA | none (Leg A: COMP-PIN-UNREACHABLE, FND-169) | | | |
| (ii) deepest gated member at the cell nearest 1.492 | 13/9, A2 0.00520, 432 x 36 (ke 0.5007) | 2.6069 | 0.6164 | NP 36 |
| (ii) the same at 54 | 13/9, A2 0.00516, 432 x 54 (ke 0.5007) | 2.6067 | 0.6164 | NP 54 |
| (iii) level-1-exact retreat | | 2.598 | 0.6151 (the exact lower edge) | |

The hold and the retreat differ by 0.34 percent in Sigma_wave and by 0.0013 in the share. Leg A's S-b finding
(the price is level-1-dominated, level 2 adding +0.3 percent at reachable amplitudes) holds on the new cells: the
reachable-family price across all nine cells is 2.598 to 2.609 T0.

## 6. The decision on the desk

The author granted the retreat on 2026-09-05 (FND-169's consequences): Sigma_wave at the level-1-exact 2.598 T0
with a rider giving the reachable-family price, and Prediction 32's upper edge re-priced to the level-1 value. The
desk memo analysis/SIGMA_WAVE_decision_memo.md prices hold and retreat side by side with Leg B's numbers and
states what each would commit the registry to. Nothing in Leg B moves the retreat; what Leg B supplies is the
rider's number from a nine-cell ladder instead of a three-cell one, and the knowledge that the deepest member the
family reaches is at a cell whose behaviour is the quasi-periodic state's, not a low-order resonance's.

## 7. Recorded, not formed

- om2 at the low point tracks q linearly across the six new cells: om2 = 6.282 (q - 1) + 0.134, maximum residual
  0.002 (fit by least squares on the six logged values; display only; the slope sits 0.02 percent from 2 pi, with a
  slope uncertainty of order 0.01 from six points over a span of 0.2 in q, so the coincidence is noted, not claimed). FND-147 recorded om2 as strongly
  q-dependent; this is the shape of that dependence on the new cells. Not adjudicated; a candidate for a charter
  that asks what the level-2 frequency is a function of.
- The rates themselves fall with N1 at matched A2 (4.38e-4 at N1 = 5, 3.70e-4 at 7, 3.27e-4 at 9, all at NP 36 and
  A2 0.0048), roughly as 1/sqrt(N1). Not part of any locked statistic.
- 5/4's D at the matched definition does not exist on the record; a stage-1-class march of 5/4 to 0.0063 under
  the registered protocol would supply it and is the only way to put 5/4 on this ladder.

## 8. Faults and departures from the plan

None of the charter's NO CALL triggers fired: no control failed after a cell opened, no member gated above
closure 1e-6, no D was formed from a non-full-bar state. The job ran on the mini rather than the laptop (the
laptop could not give 42.7 GB), under the lab's runner with sealing per invocation; the move changed the machine,
not the protocol. The CI-red hold of 2026-10-19 (the lab refuses invocations while the lab branch's verify fails;
the failure was GRV-130's benchmark rewriting its own record, fixed in PR #5) paused the job between invocations
129 and 130 and touched no state.

## 9. Proposed registration (drafted after the author read the verdict; registered only on his word)

FND-NNN, Modeled: COMMISSION COMPOSITE-SELECT, LEG B -- RAT-RESONANT: the amplitude-growth collapse of the
aligned two-frequency family tracks the cell's commensurability order, not the ratio value (Spearman rho(D, N1)
-0.983 and rho(D, q) -0.167 over nine cells at NP 36; -0.956 and -0.257 over the six new cells at NP 54; locked
thresholds 0.8 and 0.5); cells of order 5, 7 and 9 march flat (D 1.03 to 1.06x) through the window in which the
order-2 and order-3 cells collapse (9.56x, 5.31x); the physical branch near 1.492 is read from the N1 = 9 cells and
does not collapse under the registered protocol; FND-147/151/152/153/163 take a CELL-SCOPE rider; QC prices the
deepest gated member at 2.6069 T0 against the retreat 2.598 (P32 upper edge 0.6164 vs 0.6151); the retreat
granted at FND-169 stands with its rider's range now 2.598 to 2.609 over nine cells.
