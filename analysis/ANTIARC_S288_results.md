# COMMISSION ANTI-ARC-S288 -- RESULTS (2026-09-12)
Charter analysis/ANTIARC_S288_charter_LOCKED.md (locked before any 288 solve;
the DISPLACED form and the pre-run finding added before the first solve).
Executed on the author's laptop; sealed record analysis/antiarc_s288_ckpt.pkl;
verdict analysis/ANTIARC_S288_verdict.log.

## VERDICT: ** S288-REFUSED ** -- at a residual floor, RESOLVED, at EXACT resonance

## What the resolved grid showed (s0 = ANTI-ARC's sealed p0, s-refined 144 -> 288)
   start (spectral pad)   RMS 8.5e-2   A2 0.0020879   om2 -1.110632   wsNyq 2.4e-8
   after 8 rounds         RMS 1.3e-7   A2 0.0020880   om2 -1.110727   wsNyq 2.6e-7
   after 60 rounds        RMS 1.29e-7  (floor: 0.06 pct per round, gnd-esc every 7)
   closure 1.9e-10; |x - x0|/|x0| = 9.5e-4; om2 shift from the 144 value 9.5e-5.
Resolution bar wsNyq <= 1e-4: MET by three orders. DISPLACED thresholds
(om2 shift 1e-3, state shift 0.1): not reached. So: the family IS a
continuum object (the pre-run 8.5e-2 was the pad's aliasing, not a grid-
locked solution -- it fell nine orders in eight rounds), it is resolved
at 288, it keeps its amplitude -- and it sits at RMS 1.3e-7, 13x the bar,
with om2 = -1.110727 against the difference frequency -Om1/4 = -1.110721:
detuning -6e-6, i.e. ZERO to the precision of the solve.

## The reading
1. THE 8.7e-5 DETUNING WAS AN s-DISCRETIZATION EFFECT. On the 144 grid the
   5/4 anti-aligned member sat 8.7e-5 off the difference frequency and
   gated (FND-173). On the resolved grid it returns to EXACT resonance,
   where the pinned linearization carries the 2D kernel Q2 exhibited --
   and there the solve floors: the FND-142 plateau class (converged om2,
   residual crawl) that 3/2, 4/3 and 5/3 showed at 144x36. 5/4 was the
   one cell whose coarse-grid detuning happened to lift the degeneracy
   enough to gate. That is why it gated and the others did not.
2. FND-172 IS STRENGTHENED: the anti-aligned linear root is EXACTLY
   -sqrt(T)(K2 - K1) once the strand direction is resolved.
3. FND-173 IS GRID-CONDITIONED: "an anti-aligned member exists at full
   bars" was true of the 144x36 chart because the chart detuned it. The
   continuum object is the resonance itself -- a degenerate direction at
   which no member gates at these bars. The D3 letter was met on the
   coarse chart; it is not met on the resolved one.
4. FND-174 MARCHED A GRID-DETUNED FAMILY. The handedness contrast at 144x36
   stands as an instrument fact (same bars: the aligned family collapsed,
   the anti-aligned did not), and its continuum status is now OPEN for a
   specific reason: the family that marched flat exists as a gateable
   family only on the coarse chart.
5. Q2's Lyapunov-Schmidt pencil (linear roots at -7.2e-5 and +4.0e-4
   detuning, computed on the 144 chart) was itself grid-affected; on the
   resolved chart the root is at 0. The reduction's structural content
   (the 2D kernel, the other-polarization partner) stands; its numbers do
   not.

## What is named
- The anti-aligned sector's continuum object is a RESONANCE, not a
  branch: to march it one needs a solver that handles the degenerate
  direction (a bordered/Lyapunov-Schmidt continuation along the kernel,
  or a deflated solve), not more resolution. That is a new instrument,
  its own charter, and the honest prerequisite for any continuum
  statement about anti-aligned flatness.
- The wsNyq resolution bar earned its place: a resolved refusal reads
  differently from an under-resolved one, and this one is resolved.

## Process
Forms before data; the DISPLACED form and the pre-run finding recorded
before the first solve; no bar relaxed (a 13x relaxation of RMS would
have "gated" the floor). One session plus a laptop hour. Instrument
incident on the way: the laptop disk filled with SJ_MEMO=1 factor memos
and the pattern cache was truncated mid-write; recovered by re-measuring
the patterns (launchers now default to Jacobian memos and prune both memo
kinds).
