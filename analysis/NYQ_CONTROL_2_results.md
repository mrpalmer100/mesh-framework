# COMMISSION NYQ-CONTROL-2 -- RESULTS (verdict computed once, 2026-10-03)

Charter: analysis/NYQ_CONTROL_2_charter_LOCKED.md (locked 2026-10-03 before any solve). Solver:
benchmarks/foundations/kernel_continuation_0916.py, the 2026-09-16 corrector frozen, de-aliasing
the only amendment; sha256 bfe24d2d2b1b3250c8b4f0ec22ae2bc78032f62c11f840eb16b6af82c5e92009,
recorded in the checkpoint by the driver and printed by the verdict (match). Driver:
benchmarks/foundations/nyq_control_2.py (the PC, 288x36 cell 5/4). Sealed checkpoint:
analysis/nyq_control_2_ckpt.pkl. Verdict: benchmarks/foundations/nyq_control_2_verdict.py, once;
log analysis/NYQ_CONTROL_2_verdict.log.

## VERDICT: NYQ2-IRREPRODUCIBLE

The fault-reproduction control c3 (b = -0.10, de-aliasing OFF, 40 rounds, from the registered
source state antiarc_s288 s0) did not gate on the registered instrument:

| cell | state | RMS | closure | wsNyq | om2 | rounds | ended by |
|---|---|---|---|---|---|---|---|
| c3 b = -0.100, dealias off | floor | 1.3e-6 | 6.3e-8 | 1.8e-3 | -1.110728 | 40 | budget |

FND-175 stage B gated this b from this source at RMS 6.63e-9 within the same 40-round budget.
Per the locked form the sweep was not run; c1 and c2 were not run.

## What the run showed

Source state read as registered: RMS 1.3e-7, wsNyq 2.6e-7, pin 0.0020880, near-null direction
|Jc|/row 3.9e-5 (FND-175: 4e-5). Predictor to b = -0.10 landed at RMS 2.26e-6. The first
corrector step was accepted at fraction 0.1 (11 percent decrease); every one of the following 38
rounds was accepted only at the ladder's smallest rung, 0.03, for 0.1 to 1.7 percent per round,
RMS 2.0e-6 to 1.28e-6 over the budget. The Nyquist weight rose from 2.6e-7 to 1.8e-3: the half of
the fault that concerns grid-scale content reproduced; the half that concerns reaching the gate
did not. om2 held at -1.110728 (the resonance value) throughout.

## What was checked for the cause (instrument; recorded, not speculated past)

Same code: bordered_gn did not change between the 2026-09-13 sync (when stage B executed) and
the 2026-09-16 grant commit the frozen file is taken from (the only diff is the pin_mode/aux
plumbing for KERNEL-MARCH, inactive at the default 'a2'); sparsej_instrument.py,
qsweep_stage1.py, kernel_cont.py and truestate_stage2.py are unchanged since 09-16; near_null and
harmonic_basis are unchanged. Same invocation: stage B's driver (kernel_cont.py) also ran one
bordered round per invocation with ROUNDS = 40 and the same stop rule. Same source key
('s288|s0' of analysis/antiarc_s288_ckpt.pkl). Same budget. Three decades apart in outcome.

Checked on the PC by tools/nyq2_forensics.py (read-only; the registered run's history is
FND-175's own published result):

  source state: stage B's sealed x_floor, c3's x0 and the s0 array on disk today are the SAME
    array (sha256 prefix f585e824ef92bf58 for all three; max difference 0.0); pin 0.0020880
    and floor RMS 1.287e-7 identical.
  near-null direction: stage B's c and c3's c have cosine +1.000000; sigma 3.89e-5 both.
  So the inputs were identical to the bit. The outputs were not:
  stage B, b = -0.10 (registered, gated in 23 rounds):
    predictor 3.2e-6; rounds 1-15 at 1 to 5 percent (3.0e-6 ... 1.2e-6); rounds 16-22
    accelerating (9.5e-7, 8.2e-7, 6.0e-7, 4.6e-7, 3.3e-7, 1.9e-7); round 23 a single step from
    1.9e-7 to 6.6e-9 (a factor 29 in one round); |mu| decaying steadily 3.7e-8 -> 3e-13.
  NYQ-CONTROL-2 c3 (this run, same inputs, budget 40):
    predictor 2.26e-6; rounds 1-39 at 0.1 to 1.7 percent, 2.0e-6 ... 1.28e-6; ended by budget
    at a value stage B passed at its round 15.

What this means, read at the instrument level. The PREDICTOR step is a single deterministic
linear solve from identical inputs (identical J, r0, c, lam = 1e-9), and it produced a 40
percent different residual (3.2e-6 vs 2.26e-6). That is only possible if the solve is
conditioning-limited: the bordered system inverts (J^T J + lam D) against a direction with
|Jc|/row = 3.9e-5, i.e. sigma^2 ~ 1.5e-9, the same size as lam. At that ratio the step along the
near-null direction is set by rounding and library internals (scipy/BLAS version, the sparse
factorization's pivot order), not by the equations. The 09-13 run and today's run are two
samples of a solver operating at the edge of its conditioning; they diverge from the first step.
The late acceleration and the factor-29 final step in the registered run are the signature the
Fault-13 rider already named (the gate reached by admitting grid-scale structure); this run shows
the same slow phase but did not reach that event inside the registered budget. Whether it would
have at round 60 or 70 is not asked here and would not change the reading: a gate reached by a
conditioning-set path is not a reproducible gate.

Also recorded: stage B's own c1 (b = 0) improved the GN floor 1.2e-7 -> 7.2e-8 in 13 rounds,
where NYQ-CONTROL v3's c1 could not improve it (1.3e-7, floor in 7 rounds): the same
sensitivity, seen at b = 0.

## Consequences (the locked form; applied only on the author's word)

NYQ2-IRREPRODUCIBLE: FND-175's stage-B gating is not reproducible on its own instrument from the
registered source state. FND-175 is REFUTED on reproducibility and KEPT as a failure. FND-176
(KERNEL-MARCH, KM-FLAT) and FND-177 (KERNEL-MARCH-2, KM-TURN) are artifact records of a solver
whose gating cannot be re-obtained. FND-174 inherits the caution (its states carried wsNyq
8.7e-4; its instrument was the stage-2c arc march, not the bordered solver, so it is caution, not
refutation). The anti-aligned resonance itself (FND-172) and the 5/4 member (FND-173, RMS
8.35e-10 by plain Gauss-Newton) are measured on clean states and are not touched.

Proposed riders (verbatim, for the author's word):

FND-175 -> status: refuted (kept). Rider:
  [REFUTED ON REPRODUCIBILITY 2026-10-03, NYQ-CONTROL-2: the stage-B gating at b = -0.10 could
  not be re-obtained on the 09-16 corrector (frozen, sha256 bfe24d2d...) from the registered source
  state within the registered 40-round budget: RMS floored at 1.3e-6 (claim: 6.63e-9) with wsNyq
  rising to 1.8e-3. Inputs identical to the bit (same source array, same near-null direction,
  forensics in the results file); the predictor step itself differed by 40 percent, which places
  the bordered solve at lam 1e-9 against sigma^2 ~1.5e-9 at the edge of its conditioning: the
  gating path is set by library internals, not by the equations. The de-aliased sweep of
  NYQ-CONTROL (v3 driver) had already floored at every b with wsNyq clean, and its own
  fault-reproduction control also failed to gate (9.1e-7). Kept as a failure. The kernel
  question (does the anti-aligned resonance carry a continuum of full-bar members) is OPEN, not
  answered either way; the bordered corrector is not credentialed to answer it.
  analysis/NYQ_CONTROL_2_results.md.]

FND-176, FND-177 -> rider:
  [ARTIFACT RECORD 2026-10-03: rests on FND-175's bordered members, which NYQ-CONTROL-2 could not
  reproduce (NYQ2-IRREPRODUCIBLE). Read as a record of the instrument's behaviour, not of the
  family. The plain Gauss-Newton control points of FND-177 (gated from A2 0.0065) are measured
  states and stand on their own.]

FND-174 -> rider:
  [CAUTION 2026-10-03: the anti-aligned sector's continuum claim (FND-175) is refuted on
  reproducibility; this claim's states carried wsNyq 8.7e-4 against the 1e-4 bar now in force.
  Its instrument (stage-2c arc march) is distinct from the bordered solver, so this is caution,
  not refutation; a re-march under the Nyquist bar would settle it.]

Scorecard delta (docs/NORTH_STAR.md section 6): no row moves; one input retired from the
"Also carried" column (the anti-aligned continuum family is no longer carried as established).

## Named next-order (not chartered)

The kernel question itself stays open. Two honest routes: (1) a corrector that is credentialed
on a known member first (gate FND-173's 5/4 member under the bordered solve at b != 0 small,
where the answer is known), then applied at the resonance; (2) retire the bordered solver and
ask the continuum question with the plain Gauss-Newton march under the Nyquist bar, accepting
that at exact resonance it floors. Neither is cheap; neither is this commission's to decide.
