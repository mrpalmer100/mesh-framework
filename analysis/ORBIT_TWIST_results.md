# COMMISSION ORBIT-TWIST -- RESULTS (sandbox, 2026-10-09; every cell computed once; verdict by the locked types)

Charter: analysis/ORBIT_TWIST_charter_LOCKED.md (locked 2026-10-09 before any step). Instrument
benchmarks/quantum/orbit_twist.py: QB-025's two-polarization chain closed into a ring of N = 96 sites, the
quadratic eigenproblem (omega^2 - i omega G - K) solved by linearization, omega(m, sigma) read by projection on the
circular winding modes; cells analysis/orbit_twist_cells.json; log analysis/ORBIT_TWIST_verdict.log.

## VERDICT: SO-NO-MECHANISM

| cell | what was added to the ring | omega(m,+) - omega(m,-) | type |
|---|---|---|---|
| O1 control | nothing | 0 to 1e-12; omega = 2 sin(pi m/N) to five digits | degenerate (the control passes) |
| M0 curvature | in-plane stiffness from the bend law at the ring's curvature (k_u = 1.0022) | 0: the split is between the LINEAR polarizations, 7e-5 to 4e-4, growing with m, and does not resolve sigma | NONE |
| M1 gyroscopic | QB-025 device B's velocity coupling g = 0.05 on the whole ring | -g = -0.05 at every m and both senses (analytic: omega = -sigma g/2 + sqrt(K + g^2/4)) | WRONG-FORM: sigma alone, even in m (Zeeman-like) |
| M2 Rytov | the transverse frame rotated by tau per site, Psi = N tau per circuit | +0.00654 x sigma sign(m) at Psi = 0.05 turns, flat in |m| (0.00654 to 0.00642 over m = 1..6), linear in Psi (0.0026, 0.0065, 0.0131, 0.0262 at 0.02, 0.05, 0.1, 0.2 turns); analytic omega = 2 sin((pi m - sigma Psi/2)/N) | WRONG-FORM: sigma sign(m), flat in |m| |
| M3 boundary | an open chain whose end segment has the contact law's 2:1 stiffness between the transverse directions (FND-184's support function) | the standing modes split by linear polarization (u 0.0345 vs v 0.0331 at the lowest) and not by the sense of propagation | NONE |

No cell is IDENTITY or SHAPE; by the locked forms the verdict is SO-NO-MECHANISM.

## What the result is

The registered machinery has exactly one way to make a mode's energy depend on its polarization handedness AND
its orbital sense together, and it is M2: the geometric rotation of the transverse frame along a path with torsion.
It has the sign structure of the nuclear term (sigma times the sense of circulation, odd in each and even in the
pair, P-even, T-even as the pre-check required) and the wrong scaling: a constant shift per unit torsion,
Delta omega = -sigma sign(m) c_T tau, the same for every |m|, where nature's V_ls = -lambda (l . s) grows with l.
The gyroscopic coupling (M1) is a Zeeman term, blind to the orbital sense; curvature (M0) and the surface contact
law (M3) split linear polarizations and are blind to handedness.

The charter's prior (SHAPE-ONLY) assumed M2 would carry the l . s form with the torsion as its one unregistered
input. The computation separates two things the prior ran together: the sign structure (M2 has it) and the
l-scaling (M2 lacks it). Under the locked cell types that is WRONG-FORM, and the verdict is read as locked. The
distinction is recorded because it matters for what comes next: a term flat in l is not the textbook spin-orbit
force, but it is not nothing for the magic numbers, which need only that the j = l + 1/2 member of each l drop
below the next gap (1f7/2 to close 28, 1g9/2 for 50, 1h11/2 for 82, 1i13/2 for 126), a question of size against
the box's gaps, not of l-scaling. Whether a flat splitting of the size M2 could supply (hbar v tau, about
50 MeV fm times tau, so 4 MeV at tau = 1/(12 fm)) closes the right shells is a cheap, separate question, and it
would price the one input (the mode path's torsion) rather than derive it.

## Consequences (riders on the author's word)

QB-025: rider: its engine closed into a ring (ORBIT-TWIST): the bend law's curvature and the surface contact law
  split linear polarizations only; the gyroscopic device gives a handedness shift blind to the orbital sense; the
  geometric rotation of the transverse frame along a path with torsion gives the one handedness-times-sense term,
  flat in the winding number. No l . s. On the record with the cell table.
FND-185: rider: the symmetry pre-check for l . s passes (P-even, T-even; nothing registered forbids it) and the
  registered dynamics does not produce it: the inventory's "no new internal space" stands and the spin-orbit-class
  term is not among the discrete structures either.
docs/NORTH_STAR.md, "Weights of atoms", "Blocked by": the named missing term stays, sharpened: "a spin-orbit-class
  splitting; the registered machinery supplies no l . s (ORBIT-TWIST, SO-NO-MECHANISM); its only
  handedness-times-sense term is the geometric frame rotation along a path with torsion, flat in l, with the mode
  path's torsion unregistered".
No status change; the five numbers unchanged.

## Named next-order (not chartered)

NUC-SHELL-2, a price: the registered box ladder with M2's flat splitting Delta = hbar v tau applied to each
(l, sigma) pair, tau scanned over 0 to 2/R and the closures read by NUC-SHELL-1's locked rank rule at every tau;
the verdict is whether any tau in the physical range gives 2, 8, 20, 28, 50, 82, 126, and at what tau, stated as
a price on the mode path's torsion (no fit: the whole scan is the result). Minutes. If no tau does, the flat form
is excluded and the l-scaling itself is the missing physics; if one does, the row's missing term becomes one
geometric number that FND-091's helix angles or the certified knots' torsion could be asked to supply.
