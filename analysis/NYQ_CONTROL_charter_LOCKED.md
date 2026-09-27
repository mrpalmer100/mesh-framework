# COMMISSION NYQ-CONTROL -- DO KERNEL-BRANCH MEMBERS EXIST WITHOUT NYQUIST CONTENT?
# (CHARTER, LOCKED 2026-09-23 on the author's word; before any de-aliased solve)

## Question (Instrument Fault 13)
Every bordered kernel-branch member (KERNEL-CONT stage A and B, the KERNEL-
MARCH family, KM-TURN, KM-TURN-2) carries an s-Nyquist weight (the
credentialed gate's wsNyq) of 1e-3 to 1.4e-2, against 2.6e-7 for the GN-
floored resonant state they were continued from, 1.5e-5 for the b = 0
control, ~1e-9 for aligned members, and 1e-4 for the gate's own confirmation
threshold. The bordered corrector gates by adding grid-scale structure along
the strand. Do kernel-branch members exist WITHOUT it?

## Instrument amendment (the remedy, credentialed by this commission)
kernel_continuation.bordered_gn(dealias=True): every corrector step is
projected onto s-harmonics |k| <= NS/3 before acceptance (the predictor
along c is smooth by construction). nyq_bar: a solve is not reported gated
unless wsNyq <= 1e-4. Rule for every driver from today: the credentialed
gate's Nyquist flag is a BAR (wsNyq <= 1e-4), not a note.

## Protocol (the PC; 288x36, cell 5/4)
The KERNEL-CONT stage-B sweep repeated with the de-aliased corrector and the
Nyquist bar: from the GN-floored resonant state (analysis/antiarc_s288_
ckpt.pkl s0, RMS 1.29e-7, wsNyq 2.6e-7), b in {-0.20, -0.10, -0.05, +0.05,
+0.10, +0.20}, 60 rounds each; record RMS, closure, wsNyq, om2 per b.
CONTROLS: c1 -- b = 0 reproduces the GN floor (RMS ~1e-7, wsNyq stays
< 1e-4). c2 -- the aligned 4/3 member under the de-aliased bordered solve at
b = 0 stays gated (the de-aliasing does not disturb a smooth solution).
c3 (the fault reproduced) -- b = -0.10 with dealias=False from the same
state gates with wsNyq > 1e-3, as FND-175 found.

## Verdict forms (LOCKED)
NYQ-MEMBER:   at some b, RMS < 1e-8, closure < 1e-6, AND wsNyq <= 1e-4:
              a clean kernel-branch member exists; FND-175 stands (the
              members re-measured clean), and the marches are re-run under
              the bar (a follow-on). The Nyquist content was a corrector
              artifact riding on a real branch.
NYQ-FLOOR:    no b gates under the bar (the de-aliased solves floor at
              ~1e-7 like GN): the kernel branch was WHOLLY Nyquist-supported.
              FND-175 is REFUTED (kept, as a failure); FND-176/177 and the
              KM-TURN results are artifact records; the anti-aligned
              resonance has no full-bar member at these bars (ANTI-ARC-
              S288's reading stands); FND-174's coarse-grid flatness
              inherits the same caution (its states carried wsNyq 8.7e-4).
NYQ-CONTROL-FAIL: c1, c2 or c3 fails: the amended instrument is not
              credentialed; stop.
NYQ-REFUSED:  the near-null direction is not found.

## Rules
No rescue; the bar is the bar; one machine; verdict once from the sealed
checkpoint; the failure is kept whichever way it goes.

## SHAKEDOWN NOTES (instrument, not physics; recorded before any result is read)
2026-09-24 (v2): the first de-aliased sweep stalled at round 1 on every b
  because bordered_gn treated a single rejected step as terminal (the
  credentialed solver escalates lam and retries). Those runs are shakedown,
  not results. c1's floor at round 0 stands as its control.
2026-09-27 (v3): the v2 run sat 24 hours on c1 with no visible output: the
  driver silenced the solver's log, gave the b = 0 control the full 60-round
  budget, and let the lam ladder climb to 1e-2 (seven factorizations per
  rejected round). v3: the solver's round messages go to the log; the ladder
  is bounded at 1e-5; lam persists across rounds; a FLOOR is declared after
  six consecutive accepted rounds below 1e-3 relative decrease (the
  credentialed solver's own stall rule); the controls c1 and c2 get a
  10-round budget; the sweep keeps 60. The forms are unchanged. Sealed
  checkpoint: analysis/nyq_control_v3_ckpt.pkl.
