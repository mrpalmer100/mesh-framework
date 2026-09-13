# COMMISSION ANTI-ARC-54 -- RESULTS (2026-09-11)
Charter analysis/ANTIARC54_charter_LOCKED.md (locked before any 54 point).
Executed on the author's laptop (benchmarks/foundations/antiarc54.py); log
logs/antiarc54.log; checkpoint analysis/antiarc54_ckpt.pkl (author's copy).

## VERDICT: ** ANTI54-REFUSED ** -- seed pair gated at 54, point 0 refused
                                    at a residual FLOOR sitting on the bar

## What happened
s0 (ANTI-ARC's sealed p0, A2 0.0020880) phi-continued to 144x54 and gated
at RMS 9.4e-9 (closure 8e-12) in 19 rounds; s1 (p1, A2 0.0022592) gated at
RMS 1.00e-8 (closure 7e-12) in 22 rounds -- both by a hair against the
q-sweep bar 1e-8. The first arc point then descended to RMS 1.1e-8 in six
rounds and stayed there for the remaining 54: every step returned df 0.00
pct; the gnd-esc and lsmr assists fired on a fixed cadence and moved
nothing; lambda cycled 3e-9 to 1e-7 without effect. A residual FLOOR, not a
slow descent. Budget expired: REFUSED, per the form.

## The diagnostic: the family's structure ALONG s is at the grid scale (corrected 2026-09-11: wsNyq is the s-Nyquist weight, fft axis 0, NS//2)
Every anti-aligned member carries a large weight at the s-grid's Nyquist
harmonic (144 s-points; the gate's wsNyq = |fft(ws, axis=0)[NS//2]|.max()/NS): wsNyq = 2.2e-3 (s0) and 2.3e-3 (s1) at 54; 8.7e-4 to 8.9e-4 for
the same family at 36 (the s1 gate line of ANTI-ARC). The aligned 5/4
members carry ~1e-7 to 3e-7 there. This is the physical content of
"phase-dominated motion" (FND-174: f_dir ~0.77 from the first point): the
pt field of the anti-aligned family varies steeply in phi. The 36 grid
resolves that structure barely, the 54 grid marginally, and the
discretization residual of the marginally-resolved feature sits at
1.1e-8 -- above the bar by 10 pct. The arc march cannot gate a point
because the family's residual floor at this resolution IS the bar.

## What this establishes, and what it does not
1. GRID-ROBUSTNESS OF ANTI-FLAT IS NOT ESTABLISHED. FND-174 is a 144x36
   statement. Its flatness is measured at a resolution that carries the
   family's phi structure near Nyquist, and the refined grid could not
   march it. The GR54 lesson applies in the other direction: state the
   scope, do not assume the coarse grid told the truth.
2. The handedness contrast at 36 stands as measured: same instrument, same
   bars, the aligned family collapsed and the anti-aligned did not. Whether
   the anti-aligned flatness survives a resolution that actually resolves
   its phi content is OPEN.
3. Instrument finding: the Nyquist weight wsNyq is a resolution diagnostic
   the gate reports but does not bar. The three families now span four
   orders of magnitude in it (1e-7 aligned; 9e-4 anti at 36; 2e-3 anti at
   54), and the family with the largest weight is the one that refused.
   A resolution bar on wsNyq, set before the next anti-aligned run, would
   have predicted this refusal.

## Named next-order (its own charter; the 144x72 idea in the first draft of this
## document was withdrawn once wsNyq was read correctly as the s-direction weight)
ANTI-ARC-S288: the anti-aligned family on a 288x36 chart (s refined 2x;
a new 288x36 a2/arc pattern measured at a non-degenerate state; cheaper
per round than 144x54 because the banded cost scales with the phi count),
with the resolution bar stated in advance: wsNyq <= 1e-4 on the gated
seeds (the gate's own 'confirmation owed' threshold) licenses a verdict;
above it the march is display only (S288-UNRESOLVED). If the family gates
and marches, ANTI-FLAT becomes grid-robust or is overturned; if it refuses
at a floor again, the family is not representable at these resolutions
and that is the finding. Cost: a few laptop hours.

## Process
Forms before data; seed pair by the S3R rule; the refusal rendered under
the letter with its diagnostic; no bar relaxed (a 10 pct relaxation of the
RMS bar would have "passed" the floor -- that is exactly the rescue the
house forbids).
