# COMMISSION ANTI-ARC-S288 -- THE ANTI-ALIGNED FAMILY WITH s REFINED 2x
# (CHARTER, LOCKED 2026-09-11 on the author's word; before any 288 point)

## Question
The anti-aligned 5/4 family is flat at 144x36 (FND-174) and refused at
144x54 at a residual floor (ANTI-ARC-54): its structure lies ALONG THE
STRAND at the 144-point grid scale (wsNyq 8.7e-4 at 36, 2.2e-3 at 54,
against ~1e-7 for aligned members). Does a chart with s refined 2x
(288 x 36) resolve the family -- and if it does, is the family still flat?
PRE-RUN FINDING (recorded before any 288 solve): the s-zero-padded seeds
have residual RMS 8.5e-2 and 8.9e-2 on the 288 grid, against 3e-5 to 8e-5
for the aligned family's phi-continuations -- the 144-grid solution
satisfies the discrete equations at its own points (RMS 9e-9) but its
spectral interpolant misses them by nine orders on the finer grid. This is
the signature of a GRID-SUPPORTED object. The commission therefore also
tests whether the 144x36 anti-aligned family (FND-173's member, FND-174's
flatness) is a continuum object at all. A2 and om2 carry over to five
decimals; the geometry floors hold; wsNyq of the padded state is 2.4e-8
(by construction: the pad puts nothing at the new Nyquist).

## Protocol
Seed pair: ANTI-ARC's sealed p0 and p1 (144x36) s-refined to 288x36 by
spectral zero-padding along s (the phi rule of S3R transposed: unwrap the
phase field along s, remove its integer winding trend, pad, restore the
trend on the new grid), a2-pinned at their own A2, gated at the q-sweep
bars. RESOLUTION BAR, stated now: wsNyq <= 1e-4 on BOTH gated seeds (the
gate's own "confirmation owed" threshold; aligned members sit at ~1e-7).
Then the stage-2c arc march at ds 0.08 on 288x36, credentialed sparse
instrument, fresh 288x36 a2/arc patterns measured at the (non-degenerate)
seed state; 20-point budget; measurements SEALED; verdict once under C1;
continuity at every point.

## Verdict forms (LOCKED)
S288-FLAT:       seeds gated with wsNyq <= 1e-4; 20/20 gated; C1 rise < +0.15;
                 A2_max >= 0.0053. ANTI-FLAT is grid-robust along s; the
                 handedness selectivity of the collapse stands at two
                 s-resolutions.
S288-COLLAPSE:   seeds gated with wsNyq <= 1e-4; C1 rise >= +0.15. The
                 36-grid flatness was an s-resolution artifact; the anti-
                 aligned family collapses too (handedness selectivity
                 withdrawn).
S288-SCOPE:      resolved seeds, rise < +0.15, A2_max < 0.0053.
S288-UNRESOLVED: seeds gate but wsNyq > 1e-4 on either: the family is not
                 resolved at 288 either; the march (if any) is DISPLAY
                 ONLY; no verdict on flatness.
S288-DISPLACED:  a seed gates but far from where it started -- om2 off the
                 difference frequency by more than 1e-3 (the 36/54
                 detuning was 9e-5), or A2 off its pin by more than the
                 pin tolerance, or |x - x0| / |x0| > 0.1: the 144-grid
                 family was an s-grid artifact and the resolved object is
                 something else; FND-173/174 acquire artifact riders; the
                 handedness contrast at 36 is withdrawn as a continuum
                 statement. (Form added 2026-09-11 after the pre-run
                 finding, before any 288 solve.)
S288-REFUSED:    a seed or the first arc point refused (with RMS 8.5e-2 to
                 start, a refusal at a FLOOR far above the bar reads the
                 same way as DISPLACED: not a continuum object at this
                 resolution).
Display: wsNyq per seed and per point; om2 vs -Om1/4; Sigma_wave; max|v|.

## Rules
No rescue (no bar relaxed, no filtered continuation); q-sweep bars; local
execution with the driver shipped, AFTER Leg B releases the machine
(memory); verdict in the session; the grid-scope riders inherited.
