# COMMISSION ANTI-ARC-NYQ-2 -- RESULTS (the PC, 2026-10-07; verdict computed once; the lineage closes)

Charter: analysis/ANTIARC_NYQ2_charter_LOCKED.md (the one repair: c2's budget 60 -> 200, nothing else).
Driver benchmarks/foundations/antiarc_nyq2.py on a copy of the sealed ANTI-ARC-NYQ checkpoint; sealed
analysis/antiarc_nyq2_ckpt.pkl (budget 200, reopened c2A1 and c2A2, source antiarc_nyq_ckpt.pkl; arms
carried over untouched: A1 20 points, A2 halted at p0). Launched through go.py. Log analysis/ANTIARC_NYQ2.log (copied from the PC's
logs/antiarc_nyq2.log); verdict analysis/ANTIARC_NYQ2_verdict.log, by the unchanged ANTI-ARC-NYQ verdict script.

## VERDICT: ANTI-FLAT-NYQ (arm A1)

The locked form (ANTI-ARC-NYQ charter): "no arm reaches 8 points gated clean, but A1 gates >= 8 points
on RMS and closure alone (as FND-174 did) with wsNyq > 1e-4: the family's flatness at 144x36 exists only
with grid-scale content. FND-174 REFUTED as a continuum statement (Failed, kept); the instrument fact of
2026-09-07 stands as a record of this grid."

## The controls, now certified

  c1  FND-173's member: RMS 8.3e-10, closure 5.0e-12, wsNyq 8.7e-4 (the sub-reading; rider already adopted).
  c2  under A1: RMS 1.6e-9, closure 1.0e-6 (under the bar at the last digit), wsNyq 4.0e-9: gated CLEAN at
      round 177, after 117 further rounds of LSMR creep (wres 2.46e-4 -> 1.51e-4).
      under A2: RMS 1.0e-8 (under the bar), closure 4.2e-7, wsNyq 1.9e-9: gated CLEAN at round 64, four
      rounds past where the first run's budget cut it.
  The instrument can certify a known-clean aligned point under both arms; the Nyquist bar is a bar the
  aligned family clears by five orders.
  On the round numbers: the checkpoint's counters read 177 (c2A1) and 64 (c2A2); the log shows 56 and 4
  further printed corrector rounds after the resumes at 60 and 43. The counter is the instrument's
  state-write count, which advances more than once per printed round; both numbers are recorded, the log's
  is the one to read as "rounds of work".

## The sealed arms, read once

  A1 (the registered corrector): 20 of 20 points gated on RMS (4.7e-9 to 9.9e-9) and closure (3e-12 to
      2.6e-9); wsNyq 9.0e-4 at p0 rising monotonically to 1.3e-3 at p19, every point over the 1e-4 bar by
      an order; A2 0.0020 to 0.0053 (the licence span A2_max >= 0.0052 covered); C1 f_dir rise +0.018
      (0.759 -> 0.777, far under the +0.15 collapse rule): FLAT, as FND-174 found; rate +2.14e-3 constant
      to 0.1 percent; om2 pinned at -1.11063. Zero points gated clean.
  A2 (the de-aliasing projection): halted at p0, no step at any damping over 60 rounds (RMS 5.6e-7).
      Zero points.

So the march of 2026-09-07 reproduces exactly, and every one of its states carries Nyquist content near
1e-3. The flatness is real on this grid and is not a continuum statement.

## What it means

FND-174's licence said the anti-aligned two-frequency family marches flat through the aligned family's
collapse region at 144x36. It does, on the registered corrector, with the registered states. What the
Nyquist bar adds is that those states are not continuum objects: their grid-scale weight is ten times the
bar at every point and grows along the march, and the projection that would remove it cannot find a
member at all from the registered seed. The registered result was never wrong as an instrument fact; it
was read as a fact about the continuum, and that reading is refuted. NYQ-CONTROL-2 retired the bordered
corrector that produced FND-175 for irreproducibility; this commission retires the continuum reading of
FND-174 for grid content, on the plain corrector, reproducibly. FND-173's member survives (it gated under
its own bars; the bar that catches it postdates it; its rider says so). FND-172's structural root is
untouched (a closed form, not a march).

## Consequences (adopted on the author's word, 2026-10-07)

FND-174: status registered -> Failed (kept), with the rider: refuted as a continuum statement by
ANTI-ARC-NYQ-2 under the locked Nyquist bar; the 2026-09-07 march stands as a record of the 144x36 grid.
FND-176 and FND-177 (the 288x36 kernel-march lineage, already artifact records after NYQ-CONTROL-2):
rider noting that the family they marched carries, at 144x36, Nyquist content ten times the bar, so
their chart-level statements inherit the same caution.
FND-173: no change (rider adopted 2026-10-05).
Scorecard: no row moves; the input ledger's anti-aligned entry (retired 1 at 3.32.0 for FND-175) gains
"and the continuum reading of FND-174 (2026-10-07)". Five numbers unchanged.
The lineage ANTI-ARC -> ANTI-ARC-X -> ANTI-ARC-NYQ -> ANTI-ARC-NYQ-2 is closed (charter B-5). No
ANTI-ARC-NYQ-3. A future continuum claim for this family needs a different chart or a different
corrector and a fresh charter.

## Instrument record

Two runs, one repair. The first run's control failure was a round budget; the repair raised it and nothing
else; the arms were not re-run. go.py launched the repair with the per-driver terminal pattern (the launcher
fix of 2026-10-07); memos pruned by the instrument; disk guard at 20 GB cleared after the OneDrive cache was
identified as the box's real consumer.
