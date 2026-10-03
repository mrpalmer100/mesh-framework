# COMMISSION NYQ-CONTROL -- RESULTS (v3 run; verdict computed once, 2026-10-03)

Charter: analysis/NYQ_CONTROL_charter_LOCKED.md (locked 2026-09-23; v2/v3 shakedown notes
recorded there before any result was read). Driver: benchmarks/foundations/nyq_control.py (v3).
Sealed checkpoint: analysis/nyq_control_v3_ckpt.pkl (the PC, 288x36 cell 5/4; interrupted
during travel and resumed from the atomic checkpoint; terminal line printed 2026-10-02).
Verdict: benchmarks/foundations/nyq_control_verdict.py on the sealed checkpoint, once;
log analysis/NYQ_CONTROL_verdict.log. The verdict reads only the per-cell summary fields
written at each cell's stop; no state vector is opened.

## VERDICT: NYQ-CONTROL-FAIL (control c3 did not reproduce the fault)

## The nine cells

| cell | state | RMS | closure | wsNyq | om2 | rounds |
|---|---|---|---|---|---|---|
| c1 b = 0 (de-aliased, bar) | floor | 1.3e-7 | 8.2e-11 | 2.6e-7 | -1.110727 | 7 |
| B b = -0.100 | floor | 5.8e-6 | 4.5e-8 | 2.6e-7 | -1.110732 | 14 |
| B b = -0.200 | floor | 1.3e-5 | 8.7e-8 | 2.6e-7 | -1.110741 | 14 |
| B b = -0.050 | floor | 1.7e-6 | 1.6e-8 | 2.6e-7 | -1.110728 | 24 |
| B b = +0.050 | floor | 1.1e-6 | 7.0e-9 | 2.6e-7 | -1.110728 | 34 |
| B b = +0.100 | floor | 3.8e-6 | 3.1e-8 | 2.6e-7 | -1.110731 | 24 |
| B b = +0.200 | floor | 1.2e-5 | 8.8e-8 | 2.6e-7 | -1.110738 | 14 |
| c3 b = -0.100, dealias off, no bar | floor | 9.1e-7 | 3.7e-8 | 2.1e-3 | -1.110728 | 60 |
| c2 aligned 4/3, b = 0 (de-aliased, bar) | GATED (clean) | 4.3e-9 | 1.6e-10 | 1.9e-9 | +2.148419 | 1 |

Bars: gate = RMS < 1e-8 and closure < 1e-6; Nyquist bar wsNyq <= 1e-4.

## Controls

c1 PASS. The de-aliased bordered solve at b = 0 reproduces the GN floor to the digit (RMS
1.3e-7, wsNyq 2.6e-7, om2 -1.110727: the source state's own numbers). The instrument adds
nothing without a degeneracy, as FND-175's c1 found.

c2 PASS. The aligned 4/3 member stays gated clean in one round under the de-aliased solve
(RMS 4.3e-9, wsNyq 1.9e-9). De-aliasing does not disturb a smooth solution.

c3 FAIL. The fault reproduction (b = -0.10, dealias off, same source state as FND-175's
stage B) grew its Nyquist weight from 2.6e-7 to 2.1e-3, four decades, exactly the class
FND-175's members carry; but it never gated. It floored at RMS 9.1e-7 after its full
60-round budget, where FND-175 gated this same b at RMS 6.63e-9 within 40 rounds. The locked
form requires both halves (gates AND wsNyq > 1e-3). Half a reproduction is a failure of the
control, and the commission stops without a physics verdict.

## Why c3 missed (instrument, read from the shakedown notes, not from physics)

The v3 driver changed the solver, not only its logging. The v2 shakedown (2026-09-24) added
lam escalation on a rejected step; v3 (2026-09-27) bounded the ladder at 1e-5, made lam
persist across rounds, and added the six-round stall rule. FND-175's stage-B members were
gated on the solver as it stood at the 2026-09-16 grant (commit a626c99): fixed lam = 1e-9,
the fraction ladder (1, .5, .25, .1, .03), a single rejected step terminal, no stall rule,
40 rounds. c3 was therefore run on a different instrument from the one that produced the
fault it was meant to reproduce. The v3 changes were made so that v2 would not sit silent for
a day on c1; they also changed what the corrector can reach. The v2 note already recorded the
other side of the same fact: under the 09-16 solver the DE-ALIASED corrector could not take
one accepted step at any b.

## The sweep observation (recorded; no verdict attaches)

All six de-aliased cells floored under the bar at RMS 1.1e-6 to 1.3e-5 (one to two decades
above the b = 0 floor), with wsNyq held at the source's 2.6e-7 throughout and om2 within
2e-5 of the resonance value. Not one gated. Read at face value this is the NYQ-FLOOR
signature; it is NOT read, because the control that would license the reading failed.
Under the locked form the sweep cells are carried as sealed data for a follow-on that
re-credentials the control (NYQ-CONTROL-2, chartered 2026-10-03).

## Consequences for the registry (nothing moves)

FND-175 keeps its NYQUIST-CAUTION rider of 2026-09-23: its members, marches and statistics
read as instrument-conditioned until a credentialed NYQ commission renders. FND-176, FND-177,
the KM-TURN results and FND-174 stay where they are under the same caution. Neither NYQ-MEMBER
nor NYQ-FLOOR is registered.

Proposed rider on FND-175 (applied only on the author's word):
  [NYQ-CONTROL 2026-10-03: CONTROL-FAIL. The de-aliased sweep (v3 driver) floored at every b
  (RMS 1.1e-6 to 1.3e-5, wsNyq 2.6e-7) and controls c1, c2 passed, but the fault-reproduction
  control c3 (dealias off) floored at 9.1e-7 with wsNyq 2.1e-3 instead of gating: the v3 solver
  (bounded lam ladder, stall rule) is not the 09-16 solver that gated this claim's members. No
  verdict attaches to the sweep. NYQ-CONTROL-2 re-runs the control and the sweep on the 09-16
  solver with de-aliasing as its only amendment (analysis/NYQ_CONTROL_2_charter).]

## Named next-order

NYQ-CONTROL-2 (charter drafted 2026-10-03): the control c3 and the sweep on the 2026-09-16
solver verbatim, de-aliasing the only amendment; the v3 sweep carried as a second, sealed arm.
