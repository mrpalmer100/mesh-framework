# COMMISSION ANTI-ARC-NYQ-2 -- THE ONE REPAIR: THE ALIGNED CONTROL WITH ITS BUDGET RAISED
# (CHARTER, LOCKED 2026-10-05 on the author's word, before any step)

North Star line (section 5): "An instrument fault is repaired to the point where the pending verdict
can be read, then the lineage stops." ANTI-ARC-NYQ returned ANTI-NYQ-CONTROL-FAIL because the aligned
control c2 stopped at its 60-round budget a hair outside one bar in each arm. This commission raises
that budget and changes nothing else, so that the locked forms of ANTI-ARC-NYQ can be applied to the
arms it already sealed. It is the last commission in this lineage whatever it returns.

## What changes and what does not

CHANGES: c2's per-point round budget, 60 -> 200, in both arms, resuming from the saved round 60 (the
sparse instrument's persisted state in the sealed checkpoint; the corrector does not restart).
DOES NOT CHANGE: the bars (RMS < 1e-8, closure < 1e-6, wsNyq <= 1e-4); the forms; c1; the seeds; the
arms (A1's 20 sealed points and A2's halted p0 are carried over byte for byte and are not re-run; the
A2 refusal was no step at any damping, which a budget does not repair, and the charter does not
pretend otherwise); the verdict script (the same file, pointed at the new checkpoint).
The sealed ANTI-ARC-NYQ checkpoint is never written; the repair runs on a copy
(analysis/antiarc_nyq2_ckpt.pkl) that records the 60-round readings it reopened.

## What the pending verdict is, stated before the repair runs (B-4)

If c2 gates clean under both arms, ANTI-ARC-NYQ's forms applied to the sealed arms read:
A1 has 20 points gated on RMS and closure, none clean (wsNyq 9.0e-4 to 1.3e-3); A2 has none; so
the form is ANTI-FLAT-NYQ (or its collapse variant if the sealed C1 rise is >= +0.15, which reads the
same for FND-174): FND-174 REFUTED as a continuum statement (Failed, kept), the 2026-09-07 flatness
standing as a record of this grid; FND-173's rider for c1 already adopted. That is the prior and it is
not leaned on: the controls decide.
If c2 fails under either arm at 200 rounds, the verdict is ANTI-NYQ-CONTROL-FAIL again and the lineage
stops there: FND-174 keeps its licence and its caution, and the record says the aligned control could
not be certified under a Nyquist bar by this corrector within 200 rounds, which is a fact about the
instrument the next instrument must answer.

## Steps
  N1  Copy the sealed checkpoint; reopen c2A1 and c2A2 with budget 200; arms untouched.
  N2  One unit per invocation until both controls are done (gated, or 200 rounds).
  N3  The verdict, once, by the ANTI-ARC-NYQ script on the new checkpoint.

## Bars (LOCKED)
B-1  Only the budget changes. Any other edit to the driver, the bars, the forms or the seeds voids the
     commission.
B-2  The arms are not re-run. The verdict reads the sealed A1 and A2 as ANTI-ARC-NYQ left them.
B-3  The verdict is computed once, by the unchanged script.
B-4  The prior (ANTI-FLAT-NYQ, FND-174 refuted) is stated above and not leaned on.
B-5  This is the last commission in the lineage (section 5). No ANTI-ARC-NYQ-3.

## Verdict forms (LOCKED)
Those of ANTI-ARC-NYQ, unchanged: ANTI-NYQ-CONTROL-FAIL / ANTI-FLAT-CLEAN / ANTI-COLLAPSE-CLEAN /
ANTI-FLAT-NYQ / ANTI-NYQ-REFUSED, with their consequences as written there.

## Rules
No rescue beyond the one named repair; failure kept; riders, status changes and registrations the
author's; the lineage stops here.

## Cost
The PC: two control points at up to 140 further rounds each (hours, not days), then the verdict in
seconds. Launch through go.py or the pruning loop (WINDOWS_COMPUTE); the instrument now prunes its own
memos and the driver refuses to start under 20 GB free.

## Author's lock
Locked on the author's word on 2026-10-05 ("lock ANTI-ARC-NYQ-2"). No step had run. The driver
(benchmarks/foundations/antiarc_nyq2.py) was built and its reopen logic smoke-tested against the sealed
checkpoint in the sandbox before the lock (both controls resume at round 60 with 140 rounds remaining;
arms untouched; the sealed checkpoint not written); no corrector round ran anywhere.

## READS AT LOCK
analysis/ANTIARC_NYQ_results.md and the run log: c2 under A1 stopped at RMS 1.6e-9, closure 1.0e-6,
  wsNyq 4.0e-9 after 60 rounds in the LSMR fallback (wres creeping 2.9e-4 to 2.5e-4); under A2 at RMS
  1.0e-8, closure 4.2e-7, wsNyq 1.9e-9, RMS creeping 1.9e-8 to 1.0e-8 over 45 rounds. The sealed arms:
  A1 20 points gated on RMS/closure, wsNyq 9.0e-4 to 1.3e-3, zero clean; A2 halted at p0 (no step at
  any damping, RMS 5.6e-7). The ANTI-ARC-NYQ verdict script applies the forms to whatever checkpoint
  path it is given (unchanged).
