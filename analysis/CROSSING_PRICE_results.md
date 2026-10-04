# COMMISSION CROSSING-PRICE -- RESULTS (sandbox, 2026-10-04, night; verdict computed once)

Charter: analysis/CROSSING_PRICE_charter_LOCKED.md (locked before any number). Instrument:
benchmarks/foundations/crossing_price.py (the chain against the two unregistered quantities; T-1's
surface-contact geometry reused); log analysis/CROSSING_PRICE_run.log; sealed analysis/crossing_price.npz.

## VERDICT: CROSSING-UNDETERMINED

The three inputs came back as one bound, one registered form with an unregistered argument, and
one derived count:

  D1  A_c: EM-RECON-017 names A_c/(T0 a) as "one unregistered material ratio" and EM-RECON-018
      gives it a registered LOWER BOUND from core survival, > 0.40 to 0.46 (FND-068's sqrt3
      re-solve is owed and will move it). The number that would fix it is the nuclear sector's
      contact-energy import, which EM-RECON-017 already calls a calibration "waiting for a go".
      B-1 forbids spending it here. D1 is a bound.
  D2  sigma: EM-RECON-018 registers sigma_0 = w, the strand width (surfaces interact at a centre
      distance of about one width). But the standoff of two CROSSING strands in the VACUUM weave,
      d/sigma, is not registered anywhere: the threshold readings (d0/sigma0 = 1.00 in-family,
      1.38 cross-family) describe MATTER at the coverage onset, and FND-070 retracted the vacuum's
      placement at threshold (FND-129: the fine weave is sub-threshold). D2 is a form with an
      unregistered argument.
  D3  n_x = 2 crossings per node: three strand families (EM-RECON-018's coverage counting,
      FND-091's angles), a strand of one family crossing each of the other two once per spacing.
      Derived.

So the chain cannot close on registered inputs, and the form says UNDETERMINED. What it says
beyond the verdict is the commission's real product.

## The chain as a function of the standoff (alpha_c at its registered bound, 0.40)

With V_sec per crossing from the surface-contact geometry at (d/sigma, rho/sigma = 1/4 to 1/2),
V_0 = 2 V_sec, w^2 = T0 r^2/(2 a V_0), E_c = (4 pi/5) V_0/(e a), at kappa_pack 1:

| standoff d/sigma | V_0 per node | kink width w | E_c (V/m) | reading |
|---|---|---|---|---|
| 1.0 (touching) | 1.7e4 eV | 0.003 | 7e20 | self-trapped kink; 500x above Schwinger |
| 3 | 290 eV | 0.03 | 1e19 | self-trapped; above Schwinger |
| 5 | 22 eV | 0.09 | 9e17 | pinned regime; just under Schwinger |
| 10 | 0.67 eV | 0.54 | 3e16 | near the coasting edge; a discriminator |
| 20 | 0.02 eV | 3.1 | 9e14 | coasting; at the laser record |
| 50 | 2e-4 eV | 31 | 9e12 | reached in the laboratory: BELOW DATA |
| 321 (= a/d_c, the lattice spacing) | 2e-8 eV | 3200 | 8e8 | below everyday fields: BELOW DATA |

The other scale sets shift the columns (the table and the full sweep are in the log) but not the
shape: across the registered scale sets the standoff window in which FND-182's field would sit
between the laser record and the Schwinger field is d/sigma in [4.7, 19.8] (kappa_pack 1),
[6.1, 25.6] (50), [6.8, 28.5] (250). Because alpha_c is a lower bound, every E_c in the table is
a lower bound at its standoff and the window moves to larger d/sigma as alpha_c rises.

## The coincidence the chain exposes, recorded and not read

The registered kink-width regime, w in [0.8, 2.8] (FND-STRAND-002, FND-KIN-002: the kink coasts
rather than self-traps), maps through the same chain to d/sigma in [11.7, 19.2] at kappa_pack 1,
[7.0, 11.4] at 50, [5.6, 9.2] at 250, and to E_c in [1.1e15, 1.3e16], [5.3e16, 6.4e17] and
[2.6e17, 3.2e18] V/m. That is INSIDE the discriminator window at every scale set. In words: if the
vacuum's crossing strands sit roughly ten strand-widths apart, the charge-kink coasts as the
registry says it does AND the breakdown field lies between what lasers have reached and what
QED predicts. The registered w bracket and the discriminator window are the same statement about
the standoff. Nothing here derives the standoff; the coincidence is recorded under the ledger's
rule and it names the one number that would make FND-182 a prediction.

## What the two horns mean for FND-182 and the fourth grant

If the vacuum's crossing strands TOUCH (d ~ sigma, as matter does at threshold), the kink is
self-trapped (w ~ 0.003, far below the self-trapping onset 0.8) and E_c is hundreds of times the
Schwinger field: no discriminator, and FND-181's coasting kink is contradicted. If they sit at
the LATTICE SPACING (d ~ a = 321 sigma at kappa_pack 1), the orientation well is 2e-8 eV and the
vacuum would break down in fields of 1e9 V/m, which exist in laboratories without any such
effect: the grant's falsifier F1 fires. The reading survives only in the window. The commission
does not read the window as the answer; it reads it as the question.

## What is missing, named (one number now, not three)

  The standoff d/sigma of crossing strands in the vacuum weave, in units of the strand width.
  Everything else is a bound (alpha_c), a registered form (sigma_0 = w) or derived (n_x). The
  standoff is a statement about the vacuum's own geometry: how the three families are spaced at a
  node relative to the strand width. Candidate registered routes, not evaluated here: the coarse
  weave's coverage from the registered thickness d_c and spacing a (which puts d ~ a and kills
  the reading), against the two-strand helical geometry of FND-091 (whose pitch may bring crossing
  partners to within a few widths at a node). Which geometry the vacuum weave has at a node is the
  registered question, and it is a reading of FND-091 and the coarse-level packing, not a choice.

## Consequences (riders on the author's word)

FND-182: rider carrying the standoff window and the two horns; the reading is conditional on
d/sigma in the window; T2 unchanged. FND-184: rider recording that its first cash-out needs the
vacuum standoff, named. EM-RECON-017: rider noting alpha_c's lower bound now has a second consumer.
No new claim unless the author wants the window on its own id.
