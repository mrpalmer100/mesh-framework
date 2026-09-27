# COMMISSION KERNEL-MARCH-2 -- RESULTS (2026-09-18; rebuilt 2026-09-27 from the sealed record)
Charter analysis/KERNEL_MARCH2_charter_LOCKED.md (locked 2026-09-17 before any point
beyond p29). Executed on the author's Windows box; sealed checkpoint analysis/
kernel_march_ckpt.pkl (90 points); verdict once (analysis/KERNEL_MARCH2_verdict.log).

## VERDICT BY THE LETTER: ** KM2-NOT-REGULAR ** -- and the letter mis-measured
sigma at p89 = 8.1e-3 < the 1e-2 the form named. But the charter's OPERATIONAL
test of regularization -- a plain Gauss-Newton solve every 10th point -- GATED
at every control from p39 on (rms 5.6e-10 at p39, 6.9e-10, 4.0e-10, 2.2e-10,
1.3e-10, 2.9e-11 at p89), where the same solver floored at 1.3e-7 at A2 0.0021.
The branch IS regular from A2 ~ 0.0065 (sigma ~ 3e-3). The 1e-2 threshold was a
guess written into the form; the sealed data locates the real threshold three
times lower. Rendered as the letter requires; recorded as a mis-set threshold,
not a failed prediction. (House rule kept: the form is not rewritten after the
data.)

## THE UNCHARTERED FINDING: ** KM2-TURN ** at A2 ~ 0.0073
Over two arc steps, p46 -> p48 (A2 0.00723 -> 0.00740):
   rate    1.32e-3 -> 8.15e-4   (-40 pct; settles at 8.7e-4 thereafter)
   f_dir   0.592 -> 0.427       (a DROP of 0.17; recovers slowly to 0.50 by p89)
   V_pt    7.60e-3 -> 7.96e-3 -> 6.43e-3   (a spike, then a 16 pct fall)
   om2     the family LEAVES the resonance: detuning -2.6e-5 (p30) -> -5.6e-4
           (p89), doubling per step through the turn, then growing linearly
   RMS     gated throughout (p47 at 9.2e-9, the closest call); 1-2 rounds/point
   b_step  ~2e-6 with a sign flip at the turn; sigma smooth through it (3.4e-3
           -> 3.5e-3)
This is NOT the aligned collapse signature (rate down 30x, f_dir UP, tangent
object grid-bound). It is a sharp change of character in which the resonant,
phase-dominated branch becomes a non-resonant, displacement-heavier branch
with a smaller amplitude rate, and continues. C1 as chartered (last 10 vs
first 10 of the extension) reads -0.11: no collapse form triggers; no form
names this.

## Reading (hypotheses, not findings)
(a) A FOLD or branch point of the resonant family near A2 0.0073, with the
    march continuing onto the non-resonant continuation. Test: a BACKWARD
    march from p50 -- hysteresis (a different path back) means a fold.
(b) A BRANCH SWITCH induced by the bordering constraint: with the degeneracy
    nearly lifted (GN gates from p39), holding the kernel coordinate fixed
    can pull the corrector onto a neighbouring branch. Test: a plain-GN march
    from p39 through the turn -- if GN sees the same event at the same A2,
    the turn is the family's; if GN continues the resonant branch past
    0.0073, the bordered march switched.
(c) The anti-aligned family's own collapse mode with the opposite f_dir sign.

## What stands regardless (subject to the NYQUIST-CAUTION rider of 2026-09-23)
1. The anti-aligned family is flat and resonant from A2 0.0022 to 0.0072 and
   is GN-gateable from 0.0065.
2. The "degeneracy protected it" reading (KM2-REGULAR-COLLAPSE) is NOT what
   happened: the branch regularized and stayed flat for 7 points, then
   turned in a way that is not a collapse.
3. Beyond 0.0073 the anti-aligned object is a different branch: off
   resonance, rate 0.87e-3, f_dir ~0.5, still flat in the C1 sense to
   A2 0.0102.

## Named next-order: KM-TURN (executed)
The backward march from p50, the plain-GN march from p39, and state-
continuity across p45-p49.

## Process
Forms before data; verdict once; the mis-set threshold and the unchartered
event both reported under the letter rather than by amending the charter
after the fact. Run on the PC while the author travelled; 90/90 points in
two days.
