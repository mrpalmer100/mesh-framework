# COMMISSION ACTION-BRIDGE -- RESULTS (sandbox, 2026-10-04; verdict computed once)

Charter: analysis/ACTION_BRIDGE_charter_LOCKED.md (locked 2026-10-04 on the author's word before any
derivation step). Instrument: benchmarks/foundations/action_bridge.py (sympy; the derivation trail is
its stdout, analysis/ACTION_BRIDGE_run.log); sealed numbers analysis/action_bridge.npz; verdict
benchmarks/foundations/action_bridge_verdict.py, once; log analysis/ACTION_BRIDGE_verdict.log.

## VERDICT: BRIDGE-NO-MECHANISM

No registered mechanism bridges the medium's derived snap action to hbar. Every candidate in the
pre-committed enumeration was refused, blocked or excluded, and the bounded theorem (S4) says why
the enumeration had to come out that way. Grant 3 ("the quantum arrives whole", FND-STRAND-025)
stays a grant. The primitive a bridge would need is named below.

## S1. The one-power theorem reproduced; the count the bridge must produce

Symbolically (sympy), with the invariants (T0, h, l_q, alpha, c) held fixed: hbar (R1) carries
a^0, the snap action A* = (3 beta/(0.23 chi)) T0 a h / c carries a^1, and the count
N = hbar/A* = (0.23 chi/(3 beta)) l_q^2/(4 pi alpha a h) carries a^-1. GRV-094's theorem holds
on these three. The number a bridge must produce:

| evaluation point | chi | A* (J s) | n_q = A*/hbar | N = 1/n_q |
|---|---|---|---|---|
| F-LOR, GRV-092's point (Sigma 3.7e35 to 5.1e35 J/m^3 registered, a = 1e-16 m) | 1 to 3 | 1.2e-38 to 4.9e-38 | 1.1e-4 to 4.6e-4 | 2.2e3 to 9.0e3 |
| F-LOR, the three scale sets (Sigma = 3 T0/a^2; T0 a fixed on the degeneracy line) | 1 to 3 | 2.5e-39 to 7.5e-39 | 2.4e-5 to 7.1e-5 | 1.4e4 to 4.2e4 |
| F-SAK, a = 8 l_P = 1.293e-34 m (GRV-095), T0 434 to 2734 J/m | 1 to 3 | 5.4e-57 to 1.0e-55 | 5.1e-23 to 9.7e-22 | 1.0e21 to 2.0e22 |

Two F-LOR rows because the registry carries two conventions for Sigma a^3: GRV-092 evaluated at the
Lorentz-bound spacing with the measured Sigma (FND-030), the scale sets evaluate at their own
spacing with Sigma = 3 T0/a^2 (FND-017); they differ by a factor of about five and both are
registered. Neither convention changes anything below. At the adopted fork the bridge must
produce a pure number of order 1e21 to 1e22; at the Lorentz fork, of order 1e3 to 1e4.

## S2. The enumeration

| candidate | result | why |
|---|---|---|
| M0 the bending area kappa/T0 | REFUSED (dimensions) | FND-005's coupling is Pi = kappa a/T, so kappa = Pi T0/a has dimensions M/T^2 and kappa/c is M/(L T), not an action; kappa/T0 = Pi/a is an inverse length, not an area. The candidate dies before the clean-room test is reached. |
| M1 the snap-overlap count | REFUSED (no universal count) | the number of snaps coherent within one emitted period scales with the snap rate, which the accretion rate sets (GRV-040: luminosity gated by feeding); it is not a medium constant. The one universal number in the chain, beta = 35.4 barriers per bit, is already a factor of A* (e_bit = beta N h) and cannot also be the bridge. |
| M2 the twist-band count c_t/(omega_min a) | BLOCKED (unregistered input) | omega_min in physical units needs the on-site potential V_0; the registered contact form has dV/dphi = 0 exactly (FND-179 result B) and GRV-072 records that FND-STRAND-002 fixes only the ratio kt/V_0. No registered object sources V_0 (the V_0 note, below). Not evaluated with an assumed potential (B-4). |
| M3 the winding's own action 2 pi I_T omega_min | BLOCKED (unregistered input) | the same V_0. |
| M4 the registered pure counts | NO COINCIDENCE | kappa_pack 1/50/250, the fine-over-coarse spacing ratios 3.7 and 6.3, beta 35.4, 1/0.23 = 4.35, chi 1 to 3: none within half a decade of N at either fork. |
| M5 the quantum area in cells l_q^2/a^2 | EXCLUDED | this is the target (GRV-093's geometry question), not a mechanism. |

## S4. The bounded theorem (machine-checked at the dimensional level; enumeration grade beyond it)

The postulate set is {T0, a, c} with the one dimensionless coupling Pi (FND-005). Its dimension
matrix over (M, L, T) has rank 3: there is no dimensionless combination of the three, so every
dimensioned quantity built from the postulates is unique up to a function of Pi. The only length
is a g(Pi); the only action is T0 a^2 g(Pi)/c, which carries TWO powers of a. The snap action
carries one power only because the strand thickness h entered the horizon chain, and h is
anchored to the electron (GRV-094: d_c through ELEC-021, i.e. through m_e). hbar carries zero
powers, as a measured constant must.

Therefore no action built from the postulates alone is fork-invariant, and a bridge from the snap
action to hbar must supply one of two things from outside the postulates: a fork-invariant
length (the registry holds exactly two, d_c anchored to m_e and l_q anchored to alpha, both
forbidden to a clean bridge because they are what the bridge is supposed to explain), or a pure
number g(Pi) equal to N(a), which would pin a and then face R2 (test d). The dimensional part of
this is a theorem by rank. The second part, that the registry holds no pure number of the
required size and no mechanism producing one, is the enumeration above and is enumeration grade:
a future registered mechanism that produces a pure number of order 1e21 (F-SAK) or 1e3 to 1e4
(F-LOR) from Pi alone would reopen it, and that is the shape of the primitive a bridge needs.

## What this means, read at scorecard level

The fence is where it was, and it is now known to be a fence of a specific shape. The mesh's own
quantum of action, if it has one, is T0 a^2/c times a pure number, and that quantity depends on
the lattice spacing while hbar does not. So "derive hbar" in this framework is not a calculation
waiting to be done; it is a demand for a mechanism that manufactures a dimensionless number of
order 1e21 from a single coupling, with the lattice spacing then fixed by the result. Nothing
registered does that. Grant 3 keeps hbar as an imported primitive, honestly labelled. Every
scorecard row blocked at hbar stays blocked, and the input ledger does not shorten.

What the commission bought: the fence's shape, stated once and machine-checked where it can be;
the two fork conventions for Sigma a^3 recorded side by side; the M2/M3 block traced to the same
registered gap (V_0) that blocks the strand-mass-scale route to FND-182's window. Three roads,
one missing object.

## The V_0 note (the registered gap behind M2, M3 and the strand mass scale)

FND-STRAND-002's chain gives every mode a mass through an on-site orientation potential of unit
amplitude in chain units, and FND-STRAND-008 reads the twist band's gap as "exactly the strand
mass scale". GRV-072 recorded that the chain fixes only the RATIO of twist stiffness to that
potential. The physical amplitude V_0 would have to come from what resists a strand's azimuth at a
contact. FND-179 result B shows the registered contact form V(r_line) has dV/dphi = 0 exactly:
as registered, the contacts do not resist the azimuth at all. The rope's two-strand cross-section
is the natural source (a non-circular section has a physical orientation at a crossing), but the
registered contact form is a function of the centre line only and cannot see it. So V_0 has no
registered source; FND-182's window, the strand mass scale in eV, M2 and M3 here all wait on the
same grant: a cross-section-aware contact form, priced as a primitive. Until it is granted, the
honest statement is that the sine-Gordon potential the kink lives in is a model input.

Proposed registration (on the author's word): one claim, status Modeled (registry consistency, no
new physics), in the class of FND-123's "no registered handle": ACTION-BRIDGE renders
BRIDGE-NO-MECHANISM with the dimensional theorem and the enumeration; a rider on FND-STRAND-025
(Grant 3 cannot retire into a theorem from the postulate set as registered; the primitive it
would need is named); a rider on FND-182 and FND-STRAND-008 (V_0 has no registered source).

## Named next-order (not chartered)

Not another attempt at the bridge from inside. The two honest moves are both grants, priced and
left to the author: (1) a cross-section-aware contact form (unblocks V_0, M2, M3, the strand mass
scale, FND-182's window); (2) a candidate mechanism for a large pure number from Pi (a coherence
count, an exponential of 1/Pi, a percolation threshold's inverse), stated with its falsifier
before any evaluation, because the number it must hit is already on this page.
