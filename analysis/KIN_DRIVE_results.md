# COMMISSION KIN-DRIVE -- RESULTS (executed 2026-09-27, sandbox; charter analysis/KIN_DRIVE_charter_LOCKED.md)

Verdict once from analysis/kin_drive.npz by benchmarks/foundations/kin_drive_verdict.py; log
analysis/KIN_DRIVE_verdict.log; instrument benchmarks/foundations/kin_drive.py (FND-STRAND-002's
chain as registered, with the lock's uniform torque added and swept).

## Forms rendered (registered as FND-181, granted 2026-09-27)

    KIN-FORCE-DERIVED
    KIN-DRIFTS (loss identified: phonon radiation into the discrete strand)

## D1: the force law, derived

On the chain the cross term c_L sum_j eps_j (phi_{j+1} - phi_j) puts a force c_L (eps_j -
eps_{j-1}) = c_L eps' on every site: a uniform torque F where the strain gradient is uniform.
Integrated over a 2 pi kink, the force on the winding is F_kink = 2 pi F = 2 pi c_L eps'. The
same torque tilts the on-site potential; sin(phi) = F has no solution above F = 1, so the
chain's vacuum ceases to exist above the strain gradient eps'_c = 1/c_L: a breakdown field of
the Schwinger class, recorded as a consequence, not a bar.

## K1: the chain obeys it (bar B-K1, PASS)

Kink relaxed to the chain's own profile at F = 0, then driven from rest; the acceleration from
a parabolic fit on t in [20, 380] on a 2400-node chain with the kink centred (no boundary
arrival inside the window); two trackers (winding-weighted centre; the phi = pi crossing)
agree to 0.1 percent:

| w | F | M = 2 pi F / |a| | 8/w | deviation |
|---|---|---|---|---|
| 2.0 | 1e-4 | 4.043 | 4.000 | +1.1 pct |
| 2.0 | 3e-4 | 4.057 | 4.000 | +1.4 pct |
| 2.8 | 1e-4 | 2.873 | 2.857 | +0.6 pct |
| 2.8 | 3e-4 | 2.883 | 2.857 | +0.9 pct |

The larger-F rows (1e-3, 3e-3) deviate by 5 and 39 percent because the kink is already
relativistic inside the window, as K3 confirms. A positive torque drives the +2 pi kink toward
-s (the sign is the record). Total winding conserved at 0.0 in every run.

## K2: pinning (bar B-K2 not met; reported as a bound)

The bracket failed at its floor: the kink moves at F = 1e-8 at both widths, fifty times below
the static estimate E_PN/2 = 5e-7 at w = 2 (relaxed PN 1e-6). F_th < 1e-8 is an UPPER BOUND;
the instrument's residual velocity after relaxation (about 1e-3 node per time unit, enough to
hop a well of 1e-6) hides any shallower well. Finding: on this chain the static Peierls-Nabarro
barrier overstates dynamic pinning, consistent with FND-KIN-004's kink PN "at or below the
measurement floor". A winding on a coasting-regime strand is effectively free.

## K3: the speed (bar B-K3 fails above 0.5 c_t; outcome (c), then (a))

Under |F| = 1e-3 the kink accelerates relativistically, v(t) within 1.5 percent of the form
(2 pi F t/M)/sqrt(1 + (2 pi F t/(M c_t))^2) up to 0.5 c_t, then falls below it and reaches a
terminal velocity: 0.68 c_t at w = 2 (energy saturating at 22.2 = 1.39 x rest energy 16), still
rising slowly at 0.78 c_t at w = 2.8 when the 6000-node chain ended. The loss is identified by
the energy budget: from t ~ 1500 the kink's energy is constant while the energy left behind it
grows at exactly the rate of the work done, 2 pi |F| dx (4.2 per 500 time units, both), half
of it kinetic: phonon radiation from the moving kink into the discrete chain. A steady drift
therefore EXISTS at the registered couplings, with a loss the chain does contain: its own
discreteness. It is a drift at the torsion-speed scale (0.7 c_t, of order 1e8 m/s with
v_t/c = 1/sqrt5), not the millimetres per second of a copper wire; ordinary resistance is not
this loss, and remains the collective route (GRV-118 obligation 3).

## What this means for the standing items

- FND-KIN-001 narrows: the FORCE on a charge along a strand is derived (the lock supplies q E);
  what remains open is the choreography of loss at ordinary drift speeds, not the drive.
- The terminal price sheet's P4/F4 (no route from the EMF to motion) is DISCHARGED at the bulk
  level: the strain gradient does move a winding along its strand. The terminal itself (the
  boundary handover) is still unpriced; the sheet's T-C verdict is amended to "route exists in
  the bulk, boundary open".
- FND-179 stands untouched: a moving kink advances Phi locally; the bulk still cannot rotate
  the strand as a whole.
- The breakdown field eps'_c = 1/c_L is a new consequence to compare with the registered
  Schwinger-class threshold (EM-021) in a later session, not here.

## NORTH_STAR scorecard

Row "Strength of magnets" nearest step: the terminal handover (boundary) with the bulk drive
now derived; row "Weights of atoms" (the 1836 road) gains a registered transport force.
Targets moved 0; inputs retired 0; one derived force law; one derived terminal velocity with
its loss identified; one static estimate (PN pinning) shown to overstate.

## Shakedown notes

1. First draft: 1200-node chain, kink 300 nodes from an end, 12-unit fit window; the end-held
   boundary layers arrived inside the window at F >= 1e-3 and flipped the fitted sign. Fixed
   before sealing by centring the kink on a 2400-node chain and fitting t in [20, 380]. The
   K1 values at 1e-4 and 3e-4 were unchanged by the fix.
2. The relaxed site-centred kink drifts one node in 20000 time units at F = 0: the residual
   velocity floor named in K2.
3. The energy-budget run for the loss identification used the K3 protocol at w = 2 and is
   reported from its printout; the last two rows of that run are boundary-contaminated and
   excluded.
