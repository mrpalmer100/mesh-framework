# COMMISSION KIN-BREAKDOWN -- RESULTS (executed 2026-09-27, sandbox; charter analysis/KIN_BREAKDOWN_charter_LOCKED.md)

Verdict once from analysis/kin_breakdown.npz by benchmarks/foundations/kin_breakdown_verdict.py;
log analysis/KIN_BREAKDOWN_verdict.log; instrument benchmarks/foundations/kin_breakdown.py.

## Form rendered (registered as FND-182, granted 2026-09-27)

    BREAKDOWN-DISAGREES with E_crit (different objects, per the lock note), and, like with like,
    a DISCRIMINATOR CANDIDATE against the Schwinger field.

## S1: the formula

Breakdown is where the lock's torque tilts the orientation potential past its maximum,
c_L eps'_c = V_0/a (V_0 the potential's amplitude per site, a the node spacing); the force on
a winding is 2 pi c_L eps' (FND-181) and a winding carries e, so E = 2 pi c_L eps'/e and

    E_c = 2 pi V_0 / (e a) = 2 pi I_T v_t^2 / (e w^2 a^2) = 2 pi T0 r^2 / (5 e w^2 a^2),

using the registered twist band (gap = strand mass scale, FND-STRAND-008), the rod's polar
inertia I_T = (T0/c^2) r^2 (FND-MATTER-047, GRV-073), the torsion speed c/sqrt5 and the unit
map kt = C/(V_0 a), v_t = w sqrt(V_0 a/I_T). Dimensional check by machine: volt per metre.
The single unpinned input is w, the kink width in nodes (registered regime 0.8 to 2.8; the
free-transport regime is w >= 2).

## S2/S3: the numbers

| scale set | E_c (V/m) | w in [0.8, 2.8] gives | w for Schwinger | w for E_crit |
|---|---|---|---|---|
| kappa_pack 1 (M-point, T0 434, a 6.0e-17) | 8.3e15 / w^2 | 1.1e15 to 1.3e16 | 0.08 | none |
| kappa_pack 50 (T0 1599, a 1.63e-17) | 4.1e17 / w^2 | 5.3e16 to 6.4e17 | 0.56 | none |
| kappa_pack 250 (T0 2734, a 9.53e-18) | 2.1e18 / w^2 | 2.6e17 to 3.2e18 | 1.25 | none |

Reference fields: Schwinger 1.32e18 V/m; the registered linearity limit E_crit 2.0e23 V/m;
the highest field applied to vacuum without breakdown 9.1e14 V/m (1.1e23 W/cm^2, Yoon et
al. 2021, entered at lock, to be verified at paper sync).

## S4: the confrontation

- Against E_crit: E_c is five to eight orders below it at every w and scale set (B-2 fails).
  The lock note governs the reading: E_crit is where the mesh's LINEAR response fails, a
  Kerr-class onset; E_c is where the vacuum CREATES WINDINGS, the mesh analogue of pair
  creation. Two different limits; no contradiction; the corpus should stop calling E_crit
  "the vacuum breakdown field" without the qualifier.
- Against the laser record: E_c exceeds it at every registered w and scale set, the closest
  call being the M-point at w = 2.8 (1.1e15 V/m, 1.2x above the record). B-3 does not hold;
  the reading survives the data by a small margin at its weakest corner.
- Against the Schwinger field: over most of the registered range E_c is BELOW 1.3e18; at
  the continuum floor with w = 1.25 it equals it. QED predicts no charge creation below the
  Schwinger field; the mesh predicts it in a window [1.1e15, 3.2e18] V/m whose position is
  set by w and the scale set.

The mesh therefore makes a prediction here that standard physics does not share: vacuum
breakdown (charge creation) below the Schwinger field, reachable by the next generation of
lasers (1e24 to 1e25 W/cm^2 corresponds to 3e15 to 1e16 V/m). By the census criteria it is
distinctive in outcome, checkable near-term and live; it is quantitative only as a window
three orders wide until w and the scale set are pinned. That width is its weakness and is
stated on its face. A null result at 1e16 V/m would kill the M-point row outright (every w)
and push the surviving rows toward the continuum floor and small w.

## What it means

- First mesh number of the day put against an external scale where the mesh and QED
  differ in outcome. It goes to the census pass (predictions 20 to 34) as a candidate, not
  to the paper yet: the house rule is that a prediction paper carries computed numbers, and
  this one is a computed window with one unpinned input.
- The unpinned input is the same absolute-scale class the fence already owns (kappa_pack
  and the kink width w, i.e. the orientation potential's amplitude in physical units); any
  future determination of either narrows the window to a number.
- Consequence for the corpus's language: E_crit (FND-031) is a linearity limit, not a
  breakdown of the vacuum; the qualifier is owed in ROPE_PARAMETERS and wherever E_crit is
  quoted as "breakdown".

## NORTH_STAR scorecard

"Also carried" row gains: vacuum charge-creation field, window [1.1e15, 3.2e18] V/m, one
unpinned input (w), distinctive from QED, near-term checkable. Discriminator count: candidate
pending the census pass. Targets moved 0; inputs retired 0.

## Shakedown notes

1. No instrument beyond sympy and arithmetic; no shakedown runs. The external values are
   from memory with sources named and are to be verified at the paper sync before any
   registration quotes them.
