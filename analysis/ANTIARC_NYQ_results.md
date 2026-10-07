# COMMISSION ANTI-ARC-NYQ -- RESULTS (the PC, 2026-10-04 to 2026-10-05; verdict computed once)

Charter: analysis/ANTIARC_NYQ_charter_LOCKED.md (locked 2026-10-04 before any arc point; shakedown
notes recorded there). Driver: benchmarks/foundations/antiarc_nyq.py (one unit per invocation, atomic
checkpoint analysis/antiarc_nyq_ckpt.pkl); verdict benchmarks/foundations/antiarc_nyq_verdict.py; logs
analysis/ANTIARC_NYQ.log (the run) and analysis/ANTIARC_NYQ_verdict.log (the verdict, four lines).

## VERDICT: ANTI-NYQ-CONTROL-FAIL

The locked form: "c2 fails under either arm, or c1 fails the RMS/closure gate: stop." c2 failed under
both arms. Nothing downstream is read.

## What the controls returned

  c1  FND-173's registered member, re-gated by the registered corrector: RMS 8.3e-10, closure 5.0e-12,
      gated. Its Nyquist weight is 8.7e-4, 8.7 times the bar; this was known at lock (charter, "the
      member itself carries Nyquist content above the bar") and is a sub-reading, not a failure of c1,
      whose gate is RMS and closure only.
  c2  the aligned 4/3 waypoint-1 arc point, which the charter required to gate CLEAN under both arms
      (aligned members carry wsNyq ~1e-7 to 1e-9). Bars: RMS < 1e-8, closure < 1e-6, wsNyq <= 1e-4.
        under A1: RMS 1.6e-9 (passes), closure 1.0e-6 (fails, at the bar), wsNyq 4.0e-9 (passes);
        under A2: RMS 1.0e-8 (fails, at the bar), closure 4.2e-7 (passes), wsNyq 1.9e-9 (passes);
      both after the full 60-round budget per point (the driver's cap). Each arm missed exactly one
      of the two convergence bars by the last digit, with the Nyquist bar met by five orders.

## The honest reading of the control failure

The control did not find that the aligned arc point does not exist or is not clean; it found that the
instrument's per-point round budget (60) is not enough for the aligned arc point to reach the q-sweep
bars on this chart under either arm, and it stopped a hair outside them. That is an instrument-budget
fault, of the kind NORTH_STAR section 5 allows to be repaired "to the point where the pending verdict
can be read, then the lineage stops". It is not a physics finding about FND-174, and the no-rescue rule
forbids re-reading c2 with a larger budget inside this commission: the verdict was computed once and
is CONTROL-FAIL.

## What the driver printed about the arms, recorded and NOT read into any form

The driver prints, by design, each point's gating status, wsNyq and A2 and seals the rest. For the
record only:
  A1 (the registered march): 20 of 20 points gated at RMS/closure; wsNyq rose monotonically from
      9.0e-4 to 1.3e-3, every point over the 1e-4 bar; A2 from 0.0020 to 0.0053 (the licence span
      covered). Zero points gated clean.
  A2 (the de-aliasing projection on): the first arc point REFUSED (RMS 5.6e-7 after 60 rounds); the
      arm halted at p0 by the charter's rule.
  seeds: s1 gated at A2 0.0019167 with wsNyq 8.8e-4, the same 8.7e-4 class as c1.
Under CONTROL-FAIL these lines are not evidence for any form. If they were read (they are not), they
would say that the registered corrector's anti-aligned states carry Nyquist content near 1e-3 at every
point and that the projection which removes it does not converge in 60 rounds on this family, while
on the aligned control it converges to within the last digit of the bars. The commission does not
read them. A future commission may, from the sealed checkpoint, if its charter says how.

## What the run log shows about the control's stall (analysis/ANTIARC_NYQ.log)

On the aligned arc point under both arms the corrector's normal factor step was rejected and the
corrector spent its budget in the LSMR fallback ("alt: lsmr step accepted" at nearly every round),
creeping at wres 2.5e-4 to 2.9e-4: RMS 1.9e-9 to 1.6e-9 over 60 rounds under A1, 1.9e-8 to 1.0e-8
under A2. Under A2 the creep was on course to cross the RMS bar within a few more rounds; under A1
the failing bar is closure, which the log does not print per round, so a larger budget is a guess
there and not a forecast. The de-aliased arm's refusal at the anti-aligned p0 is of a different kind:
no step at any damping from 1e-8 to 4 for 60 rounds at RMS 5.6e-7 (recorded, not read).

The disk incident's footprint is in the log: one invocation died with EOFError reading a memo
truncated by the full disk; the next invocation resumed from the saved round with no state loss
(atomic checkpoint; the instrument's own resume). The sealed checkpoint analysis/antiarc_nyq_ckpt.pkl
holds c1, c2 under both arms, the seeds, A1's 20 points and A2's halted p0 (phase and counts only
readable here; measurements sealed).

## Consequences (on the author's word)

FND-174: rider recording that ANTI-ARC-NYQ was run under a Nyquist bar and returned CONTROL-FAIL
(instrument budget on the aligned control); the licence stands as it was, the caution reopened on
2026-10-04 (NYQ-CONTROL-2 consequences) stands as it was; nothing read.
FND-173: rider recording c1's sub-reading (the registered member re-gates at RMS 8.3e-10 and carries
wsNyq 8.7e-4, known at lock, now sealed on the PC).
No status changes. No new claim unless the author wants the control failure on an id.

## Named next-order (not chartered)

ANTI-ARC-NYQ-2: the same charter with c2's round budget raised (120 or 200) and nothing else changed,
so that the pending verdict can be read. One repair, then the lineage stops (NORTH_STAR section 5).
Cost: the aligned control is two arc points; the arms would then be resumed from the sealed
checkpoint, not recomputed. The author decides whether the question (does the anti-aligned family
survive a Nyquist bar) is worth the PC's week; the matrix (FND-186) puts it inside gap 1's
housekeeping, not on any closure target.

## Incident record (instrument hygiene, 2026-10-04)

The PC's disk filled twice during this run. Cause: the sparse-Jacobian instrument writes a ~0.6 GB
factor memo per factorisation into %TEMP% when SJ_MEMO is unset; go.py sets SJ_MEMO=jac and prunes,
but the hand-rolled PowerShell loop did neither. Fixed in this package: the instrument prunes its own
memos (sparsej_instrument._prune_memos, newest two kept), the driver refuses to start under 20 GB
free, and docs/WINDOWS_COMPUTE.md carries the rule. The run's physics was unaffected (atomic
checkpoint; the guard refused rather than died).
