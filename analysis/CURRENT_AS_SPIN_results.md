# COMMISSION CURRENT-AS-SPIN -- RESULTS (executed 2026-09-27, sandbox; charter analysis/CURRENT_AS_SPIN_charter_LOCKED.md)

Verdict computed once from the sealed outputs (analysis/current_as_spin_partA.npz, _partB.npz)
by benchmarks/foundations/current_as_spin_verdict.py; log analysis/CURRENT_AS_SPIN_verdict.log;
instrument benchmarks/foundations/current_as_spin.py.

## Forms rendered (registered as FND-179, granted 2026-09-27)

    (A) TWIST-NOT-SPIN
    (B) ASYMMETRY: transverse O(g^2), azimuthal exactly zero through the registered contact form

## Part A: a steady EMF twists the strand; it does not spin it

The registered screw-stretch sector (EM-RECON-023) with the derived lock (EM-RECON-012),
energy per unit length (lambda/2) Phi'^2 + (k_s/2) u'^2 + c_L u' Phi', c_L = lambda gamma tau_0.
The torque density on the azimuth is, by Euler-Lagrange (sympy, exact),

    torque = lambda Phi'' + c_L u'' = d/ds J,   J = lambda Phi' + c_L u'  (the twist flux),

a TOTAL DERIVATIVE. So the net torque on the azimuth's zero mode (the rotation GRV-020's
SO(2) protects) is J(L) - J(0): a boundary term. A steady EMF, read as the registered bulk
strain gradient (EM-018), exerts NO net torque anywhere in the bulk; it redistributes twist
along the strand (a static profile Phi'' = -(c_L/lambda) u'') and that is all. Under
torsion-free ends the time-averaged rate is zero. This is the conservation law of the
azimuth's angular momentum: d/dt (I Phi_dot) = dJ/ds, with J the angular-momentum current.
"Current is spin" survives only as this conservation law: a steady rotation requires a steady
NET twist flux J(L) - J(0) != 0, i.e. terminals that act as source and sink of angular
momentum. The registry holds no such terminal.

Numeric control (bar B-A1/B-A2): chain of 100 and 200 sites, u pinned at both ends, twist
free, steady body force on u at 1e-4, 1e-3, 1e-2, from rest, 400 time units, velocity Verlet.
Strand-averaged d(Phi)/dt over the last half of every run: 1e-18 to 3e-16, against a twist-rate
scale (c_L/lambda)|u'| of 9e-3 to 1.6: relative 1e-16, six orders inside the 1e-6 bar.
Classification TWIST. Displays (unregistered terminal inputs, run to name the missing input):
a terminal injecting twist flux at s = 0 accelerates the strand without bound (no steady rate
without a sink); a terminal imposing a rotation rate makes the strand follow it. The missing
input is therefore NAMED: the terminal condition on the twist flux J (a battery as a source of
angular momentum, a load as its sink), which no registered claim supplies.

Form TWIST-NOT-SPIN, kept as a failure of the reading "current is spin" at the registered
couplings, with the rescue priced: a strain-gradient-to-rotation coupling in the bulk would be
a NEW coupling (a grant), and a terminal twist-flux condition is a new boundary primitive (a
grant). Neither is adopted here.

## Part B: the reservoir asymmetry

Symbolic: for the registered contact form V(r) with r the centre-line separation, dV/dphi = 0
(EM-RECON-023, reproduced) AND dV/du = 0, because sliding a straight strand along its own
tangent leaves the centre line invariant (u is gauge, EM-RECON-012). So at the registered
contact form neither twist nor stretch reaches a crossing at ANY order: the azimuthal leak
through contacts is exactly zero, not "higher order in g". The finite route GRV-118 named,
twist -> stretch (lock) -> crossing through EM-RECON-026's collective momentum-flux coupling,
is a different coupling whose crossing transfer rate is GRV-118's obligation (3), enumerated
and not owed; it is not computed here and not owed here.

Numeric (transverse): two chains coupled at one site by a contact spring g (the FND-REL-005
pinning class), a wave packet on chain 1, the energy fraction transferred to chain 2:

| g | leak fraction per crossing |
|---|---|
| 0.0032 | 5.7e-5 |
| 0.0100 | 5.7e-4 |
| 0.0316 | 5.6e-3 |
| 0.1000 | 5.1e-2 |

Fit A g^n over the sealed range: n = 1.974 (small-g half 1.998), A = 5.0 (halves 5.6/4.5). By
the letter of bar B-B the form is NOT accepted (the prefactor moves 22 percent across the
halves, the g = 0.1 point already saturating); the raw table is the record, and n = 2 in energy
(O(g) in amplitude) is what it shows at small g.

Asymmetry: transverse O(g^2) per crossing against an azimuthal zero through the contact form.
Unbounded at the contact level; the author's reading that the azimuthal reservoir is the
low-loss channel is CONFIRMED in structure and its finite size is GRV-118 (3).

## What GRV-118's vertex session inherits

Bars B-A and B-B, the total-derivative theorem (the twist flux J is the only carrier of net
torque), and the statement that the contact form is blind to both twist and stretch, so the
vertex's crossing transfer runs through EM-RECON-026 alone.

## NORTH_STAR scorecard (row "Strength of magnets", nearest step)

"Current is spin" at the registered couplings: a conservation law with no bulk source; the
rotation rate is a terminal condition the registry does not hold. Nearest step becomes: the
terminal as a source/sink of twist flux, priced as a grant, or the electron model (unchanged).
Delta: targets moved 0, inputs retired 0, one reading refuted-and-kept at its registered
couplings with the missing primitive named.

## Shakedown notes (instrument, not physics)

1. The first Part A run diverged from a sign error in the chain force assembly (forces
   negated twice); the sealed file was overwritten by the corrected run before the verdict
   script existed. A1's symbolic result was unaffected. Recorded here.
2. The rotation-imposed display shows undamped transients (mean rate 3.4e-3 against the
   imposed 1e-3); it is a display of following, not a rate measurement.
3. B2's g range (3e-3 to 1e-1, 1.5 decades) reaches saturation at its top; a re-run at
   smaller g would be needed to accept the prefactor form under B-B. Not done: the sealed
   range is the record.
