# COMMISSION NUC-SHELL-2 -- RESULTS (the PC, 2026-10-09; the scan run once; the sandbox reproduces it exactly, no data involved)

Charter: analysis/NUC_SHELL_2_charter_LOCKED.md (locked 2026-10-09 after the tau R = 0 control and before the scan).
Driver benchmarks/nuclear/nuc_shell_2.py; log analysis/NUC_SHELL_2_verdict.log; the full scan analysis/nuc_shell_2_scan.json
(both signs, tau R = 0 to 2 by 0.02, closures by NUC-SHELL-1's locked rank rule).

## VERDICT: PRICE-NONE

No tau R gives all seven magic numbers; no tau R gives the first four (2, 8, 20, 28) together. The driver's locked
verdict line is PRICE-NONE. One thing the charter's prose did not foresee and the scan shows: 28 does appear, at
tau R from 0.64 to 1.14, and at tau R 0.80 to 0.92 the well closes at 2, 14, 28, 50, 76, 136, 164. So the flat-in-l
term CAN bring 1f7/2 down to close 28 and 1g9/2 to close 50, but only at a torsion that has already destroyed 8 and
20 (the light shells split too far: the term grows with k and the light gaps are small) and never reaches 82 or
126 (76 and 136 instead). There is no torsion at which the light and the heavy closures coexist. The charter's
PRICE-NONE sentence ("no tau R gives 28 at all") is therefore stricter than what happened, and the driver's form
(neither all seven nor the first four: NONE) is what was locked and what is read; the discrepancy is recorded here
and the verdict stands as the driver printed it.

The closures along the scan, j = l + 1/2 lower (the sign that closes 28):
| tau R | closures | hits |
|---|---|---|
| 0.00 | 2, 8, 20, 34, 58, 92, 138 | 2, 8, 20 |
| 0.20 | 2, 8, 58, 80, 92, 138, 164 | 2, 8 |
| 0.40 | 2, 8, 38, 92, 114, 136, 164 | 2, 8 |
| 0.60 | 2, 38, 76, 92, 114, 136, 164 | 2 |
| 0.80 | 2, 14, 28, 50, 76, 136, 164 | 2, 28, 50 |
| 1.00 | 2, 6, 14, 28, 76, 82, 118 | 2, 28, 82 |
| 1.20 to 2.00 | 2, 6, 14, ... | 2 |
The opposite sign never closes 28 (as the sign structure requires).

## What the result is

The price does not exist. The one handedness-times-sense term the registered machinery has (ORBIT-TWIST M2),
carried by NUC-A's dispersion as a splitting proportional to the level's wavenumber and flat in l, cannot close
nature's shells at any torsion: what it needs to do at the heavy end (drop 1g9/2, 1h11/2, 1i13/2 by a full shell
spacing) it can only do at a strength that wrecks the light end, because nature's splitting grows with l and this
one does not. The l-scaling of the spin-orbit term is the missing physics, not its sign and not its scale. That
is the sharpest statement the row has had: the mesh nucleus lacks a term proportional to l . s, the registered
machinery has no mechanism with that scaling, and the mode path's torsion, even if a geometry were found to pin it,
would not supply it.

The scan is also a small positive fact about the term itself: at tau R about 0.8 (tau = 1/(5 fm) at A = 56) it
produces 28 and 50 from the registered box with no constant, which is what a flat chiral splitting does to the
f and g intruders. It is recorded, not read into any form.

## Consequences (riders on the author's word)
NUC-A: rider: the scan on the record; the flat-in-l chiral splitting of ORBIT-TWIST's M2 applied to this claim's
  well closes 28 and 50 only at a torsion that destroys 8 and 20 and never reaches 82 or 126; PRICE-NONE. The
  l-scaling of the spin-orbit term is named as the missing physics.
docs/NORTH_STAR.md, "Weights of atoms", "Blocked by": final at this level: "the shell closures above 20 need a
  splitting that grows with l (l . s); the registered machinery supplies no such term (ORBIT-TWIST), and its one
  chiral term, flat in l, closes no consistent set of shells at any torsion (NUC-SHELL-2, PRICE-NONE)".
No new claim unless the author wants the three-commission chain (NUC-SHELL-1, ORBIT-TWIST, NUC-SHELL-2) on one id
as a kept negative result; no status change; the five numbers unchanged.

## Named next-order (not chartered)
None in this lineage; it stops here by its own charters. The row's remaining roads are the ones the scorecard
already names (He-4's zero-point, pairing), and a spin-orbit term would need a new primitive, which is a decision
for the author, not a computation for the sandbox.
