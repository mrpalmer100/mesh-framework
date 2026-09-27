# COMMISSION KM-TURN-2 -- RESULTS (2026-09-23; rebuilt 2026-09-27 from the sealed record)
Charter analysis/KM_TURN2_charter_LOCKED.md (locked 2026-09-22 before any solve;
the 3 ds first-step amendment before any solve). Executed on the author's
Windows box; sealed checkpoint analysis/km_turn2_ckpt.pkl; verdict once
(analysis/KM_TURN2_verdict.log).

## VERDICT: ** R-CONTINUES-FLAT **
The resonant branch R passes the crossing at A2 ~0.00733 and continues, flat,
to A2 0.0086: 12/12 points on R by the pre-set thresholds (rate 1.371e-3 ->
1.329e-3, f_dir 0.5985 -> 0.6107, om2 on the difference frequency to 8e-5);
C1 f_dir rise +0.0086 vs +0.15; RMS 2e-10 to 6e-9; the plain-solver control
GATES at p3, p7 and p11 (2.2e-10, 4.6e-11, 1.3e-10) -- R is regular on the
far side; the singularity is confined to the crossing point itself.

## What this would settle (subject to the NYQUIST-CAUTION rider below)
1. FND-177's "turn" was a BRANCH CROSSING, not a turn of the resonant family.
2. The anti-aligned flatness would extend from A2 0.0022 (FND-176) through
   0.0086.
3. R stays on resonance (detuning -5e-5 -> -8e-5); sigma keeps rising slowly
   (3.6e-3 -> 4.4e-3).
4. Two anti-aligned branches coexist above ~0.0067: R and N, both flat.

## NYQUIST-CAUTION (2026-09-23, instrument fault 13)
Every bordered state in this commission carries an s-Nyquist weight (the
credentialed gate's wsNyq) of 1.2e-2 to 1.4e-2, against 2.6e-7 for the GN-
floored resonant state the family descends from and ~1e-9 for aligned
members. The R -> N difference at matched A2 has 70 pct of its theta-field
power at s = 144, the 288 grid's Nyquist. The findings above are instrument-
conditioned until COMMISSION NYQ-CONTROL renders. No form here is withdrawn
by the author's word; the record is kept with this rider on its face.

## Process
Forms before data; the first-step amendment and the threshold rule before any
solve; no rescue; verdict once.
