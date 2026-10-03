# COMMISSION NYQ-CONTROL-2 -- THE NYQUIST QUESTION ON THE INSTRUMENT THAT RAISED IT
# (CHARTER, DRAFT 2026-10-03; becomes LOCKED on the author's word, before any solve)

North Star line (docs/NORTH_STAR.md section 5): retires an input. The kernel-branch family
(FND-175/176/177, the KM-TURN results) and FND-174's coarse-grid flatness are the anti-aligned
sector's claim to a continuum; all of it is under the NYQUIST-CAUTION rider since 2026-09-23.
NYQ-CONTROL (v3) could not settle it because its fault-reproduction control ran on a solver
that is not the one that gated the members (NYQ_CONTROL_results.md). This commission asks the
same question with the control pinned to the registered instrument, so that whichever way it
goes the rider is retired: the sector either has clean members or it does not.

## Question (unchanged from NYQ-CONTROL)

Do bordered kernel-branch members exist WITHOUT s-Nyquist content? Every member FND-175 rests
on carries wsNyq 1e-3 to 1.4e-2 against 2.6e-7 for the GN-floored resonant state it was
continued from and 1e-4 for the credentialed gate's own threshold.

## What changed, and only this

The solver is benchmarks/foundations/kernel_continuation.py at commit a626c99 (2026-09-16, the
grant of FND-175), copied verbatim to benchmarks/foundations/kernel_continuation_0916.py:
fixed lam = 1e-9, acceptance fractions (1, .5, .25, .1, .03), a single rejected step terminal,
no stall rule, stop at the RMS bar. ONE amendment is added behind a switch that is off by
default: dealias=True projects each corrector step onto s-harmonics |k| <= NS/3 before the
acceptance ladder (the same dealias_s as v3; the predictor along c is smooth by construction).
With the switch off the function is byte-for-byte the 09-16 corrector. Nothing from v2/v3
(lam escalation, persistent lam, stall rule) is carried. The gate's Nyquist flag remains a BAR
for reporting (wsNyq <= 1e-4), as the 09-23 rule requires.

## Protocol (the PC; 288x36, cell 5/4; source analysis/antiarc_s288_ckpt.pkl s0)

Arm S1, the 09-16 solver with the de-aliasing switch:
  c3  b = -0.10, dealias OFF, 40 rounds, no Nyquist bar on the gate (the fault reproduction,
      on the instrument that found it). Must GATE (RMS < 1e-8, closure < 1e-6) with
      wsNyq > 1e-3. RUN FIRST; if it fails the commission stops before the sweep.
  c1  b = 0, dealias ON, 10 rounds: reproduces the GN floor (RMS ~1e-7, wsNyq < 1e-4).
  c2  the aligned 4/3 member (144x36) at b = 0, dealias ON, 10 rounds: stays gated clean.
  B   b in {-0.20, -0.10, -0.05, +0.05, +0.10, +0.20}, dealias ON, 60 rounds each; record
      RMS, closure, wsNyq, om2, rounds, and the manner of stopping (gated / rejected step /
      budget).
Arm S2, sealed already: the six v3 sweep cells in analysis/nyq_control_v3_ckpt.pkl (de-aliased,
lam ladder, stall rule), carried as a second corrector flavor. They are not re-run.

Order on the PC: c3, c1, c2, then B in the order -0.10, -0.20, -0.05, +0.05, +0.10, +0.20.
Checkpoint analysis/nyq_control_2_ckpt.pkl (atomic, one round per invocation as v3, the
solver's round messages in the log). Terminal line: 'NYQ-CONTROL-2 COMPLETE -- run the
verdict'. One machine per job.

## Bars (LOCKED before any solve)

gate: RMS < 1e-8 and closure < 1e-6 (qsweep_stage1 bars). Nyquist bar: wsNyq <= 1e-4.
"floor class": RMS <= 1.3e-6 (ten times the b = 0 GN floor). "stall": the corrector ends on a
rejected step with RMS above the floor class.

## Verdict forms (LOCKED)

NYQ2-CONTROL-FAIL   c1 or c2 fails: the de-aliasing amendment is not credentialed; stop.
NYQ2-IRREPRODUCIBLE c3 does not gate with wsNyq > 1e-3 on the 09-16 solver from the registered
                    source state: FND-175's stage-B gating is not reproducible on its own
                    instrument. FND-175 is REFUTED on reproducibility (kept, as a failure);
                    FND-176/177 and KM-TURN are artifact records; FND-174 inherits the caution.
                    The sweep is not run.
NYQ2-MEMBER         c3 passes and some B cell in S1 or S2 is GATED under the Nyquist bar: a
                    clean kernel-branch member exists. FND-175 stands (members re-measured
                    clean); the Nyquist content was a corrector artifact riding on a real
                    branch; the marches are re-run under the bar (a follow-on).
NYQ2-FLOOR          c3 passes and no B cell in S1 or S2 gates under the bar. The kernel branch
                    was WHOLLY Nyquist-supported: the only corrector that reaches the gate is
                    the one allowed to add grid-scale structure. FND-175 is REFUTED (kept, as a
                    failure); FND-176/177 and the KM-TURN results are artifact records; the
                    anti-aligned resonance has no full-bar member at these bars (ANTI-ARC-S288's
                    reading stands); FND-174 inherits the same caution. The sub-reading is
                    recorded with the verdict and changes nothing in it: FLOOR-LEVEL (S1 cells
                    reach the floor class) or FLOOR-STALL (S1 cells end on a rejected step
                    above it, i.e. with the Nyquist modes projected out the corrector cannot
                    descend from the predictor state at all).
NYQ2-REFUSED        the near-null direction is not found.

## Rules

No rescue; the bars are the bars; the solver file is frozen at lock and its hash recorded in
the verdict log; verdict once from the sealed checkpoint by nyq_control_2_verdict.py; the
failure is kept whichever way it goes; registrations and riders on the author's word.

## Reads owed at lock

FND-175 (stage-B protocol: 40 rounds, b values, the source state, c1/c2 as run), FND-172/173
(the resonance and its grid-condition rider), FND-174 (what inherits), the 09-23 Nyquist-bar
rule as registered, commit a626c99's bordered_gn (confirm fixed lam and ladder as stated here).

## Cost

The PC. c3 is 40 rounds at most on 288x36 (v3's c3 took 60); c1, c2 are minutes; the six S1
cells are 60 rounds each at most, and the v2 note predicts that most end on a rejected step
within a few rounds. Expect hours, not days. Sandbox: the frozen solver file, the driver, the
verdict script, all delivered as a zip before lock.

## Author's lock

Locked on the author's word on: ______ . Until then no solve runs.
