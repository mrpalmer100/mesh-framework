# COMMISSION KM-TURN -- RESULTS (2026-09-22; rebuilt 2026-09-27 from the sealed record)
Charter analysis/KM_TURN_charter_LOCKED.md (locked 2026-09-18 before any new
solve; Test C recorded as a pre-run finding). Executed on the author's Windows
box; sealed checkpoint analysis/km_turn_ckpt.pkl; verdict once (analysis/
KM_TURN_verdict.log).

## VERDICT BY THE LETTER: ** TURN-UNRESOLVED **
Test A's hysteresis threshold (state distance > 1e-2) was not reached (max
1.7e-3, growing steadily); Test B refused AT the turn rather than seeing the
event or the no-event. Neither named combination fired.

## What the sealed record shows
TEST A (backward bordered march, 12/12 gated, from p51 -> p50): the march
does NOT retrace the resonant branch. It runs back down in A2 from 0.00753
to 0.00675 on a branch with rate -0.93e-3 (magnitude), f_dir 0.42 -> 0.45,
om2 detuned, while the forward resonant branch at the same A2 has rate
+1.37e-3, f_dir 0.60, om2 on the difference frequency. The state distance
between the paths grows monotonically 1e-6 -> 1.7e-3 over 12 points. A
different branch, coexisting with the resonant one over 0.0067-0.0073.
TEST B (plain credentialed solver, forward from p38 -> p39): p0-p6 gate and
track the bordered resonant path to four digits; p7 at A2 0.00733 -- the
turn -- FLOORS: 60 rounds at 5 pct per round to RMS 1.3e-8, never gating.
TEST C (pre-run): the turn is continuous in state space.

## The reading: a BRANCH CROSSING at A2 ~ 0.00733
Two branches exist over the interval: R, the resonant branch (f_dir 0.60,
om2 = -Om1/4), and N, a non-resonant branch (f_dir 0.45, rate 0.93e-3, om2
detuned). They meet at A2 ~ 0.00733, a genuine singular point of the family
(Gauss-Newton floors there). The bordered forward march turned from R onto N
at the crossing; the backward march from N continued N downward through it.
FND-177's "turn" is a crossing, not the end of R; R's continuation beyond
0.00733 was UNMEASURED at this point (KM-TURN-2 measured it). The charter
thresholds were set as round numbers rather than from the data's own scale;
the next charter sets its thresholds from the sealed forward profile.

## Named next-order: KM-TURN-2 (executed) -- continue R across the crossing.
NYQUIST-CAUTION (added 2026-09-23): all bordered states in this commission
carry an s-Nyquist weight of ~1e-2 (instrument fault 13); the reading above
is instrument-conditioned until NYQ-CONTROL renders.
