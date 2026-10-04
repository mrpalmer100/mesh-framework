# COMMISSION GAUGE-INVENTORY -- RESULTS (sandbox, 2026-10-04, night; verdict computed once)

Charter: analysis/GAUGE_INVENTORY_charter_LOCKED.md (locked before any machine step; reads at lock
recorded there). Instrument: benchmarks/foundations/gauge_inventory.py (sympy; the control runs first);
log analysis/GAUGE_INVENTORY_run.log; sealed analysis/gauge_inventory.npz.

## VERDICT: DISCRETE-ONLY, with the count (NEW-INTERNAL-SPACE-NEEDED); P-EVEN

The registered weave's continuous internal symmetry, at every level, is the SO(2) that GRV-020
derived for the strand's azimuth (times the slide along the strand), and it is already spent:
winding = charge, torsion = light. Everything else is finite. The registered continuous internal
space is one circle, real dimension 1; SU(2) needs 3 or 4 and SU(3) needs 6 or 8. The vacuum is
P-even with a two-fold handedness degeneracy, and spatial inversion acts on the winding label as
charge reversal. No registered variable carries a second continuous internal direction.

## G1, the inventory (every variable with its id; nothing unregistered admitted, B-1)

| level | variable | range | registered energy depending on it | source |
|---|---|---|---|---|
| strand | frame azimuth phi(s) | circle | torsion stiffness (C/2)(phi' - tau0)^2; no on-site term (Goldstone, kappa = 0) | GRV-020, GRV-067 |
| strand | handedness sign of the winding (tau0's sign) | {+, -} | the energy is symmetric under the flip; the winding derivation fixes angles, not signs | FND-088, GRV-045 |
| strand | two-strand exchange | Z2 | none registered (A2 names the count, no energy distinguishes the strands) | ontology A2 |
| strand | the face (section orientation) | circle mod pi | none registered in the vacuum (crossings do not press, junctions are points) | FND-184, NODE-STANDOFF, JUNCTION-LOCK |
| node | director angles of the z ropes | (S^2)^z, spatial | J sum (1 - cos dtheta) | FND-001, FND-148 (z = 6 at embedding) |
| node | rope labels (which rope is which) | S_z | the pair sum is label-blind | FND-001 |
| node | each rope's own-axis azimuth at the node | circle | none (the point bond; f = 0) | JUNCTION-LOCK |
| weave | family label at a site | {x, y, z} | the order-4 cubic harmonic sum n_i^4 - 3/5 in the direction set | ELEC-096, EM-RECON-018 |
| weave | relative level-2 handedness | {aligned, anti} | the two are different registered objects (different om2) | FND-140, FND-173, FND-174 |

Refused by name (B-1): an isospin-like doublet label on a strand, a colour-like label beyond the
three spatial families, any internal phase other than phi. None has a claim id.

## G2, the groups by machine (control first, B-2)

CONTROL. From the registered torsion energy alone, the instrument finds: rotation phi -> phi + alpha
invariant, slide s -> s - a invariant, reflection of phi alone not, inversion of s alone not,
scaling and shear not; the joint P (s -> -s, phi -> -phi) invariant; the helical ground state's
stabiliser is the one-dimensional screw; G/H has dimension 1. GRV-020 reproduced exactly.

STRAND. Continuous: R x SO(2), ground-state manifold S^1 (the control). Discrete: the joint parity;
the handedness flip tau0 -> -tau0 with phi -> -phi (the energy is symmetric between the two signs).
The exchange Z2 and the face carry no registered energy: UNCONSTRAINED, recorded as such and not as
a symmetry (B-4).

NODE (z = 6). Internal: the rope-label permutations S_6 leave FND-001's pair sum invariant
(enumerated by transpositions). The common rotation of all directors is invariant and the rotation
of one director alone is not: that is the spatial SO(3) acting on the directors, not an internal
group. The own-axis azimuth of each rope is absent from the energy: UNCONSTRAINED.

WEAVE. The cubic harmonic sum n_i^4 - 3/5 is invariant under all 48 elements of O_h (enumerated as
signed permutation matrices) and not under a generic SO(3) rotation (ELEC-096 reproduced). The
family label set has symmetry S_3 (6 elements, inside O_h); the identity component of any group
acting on a 3-element set is trivial, so the continuous internal part is dimension 0. The relative
handedness is a Z2 label that the registered energy distinguishes: a label, not a symmetry.

So the continuous internal group at every level is SO(2) (strand) or trivial (node, weave), and the
discrete internal groups are Z2 (handedness flip; exchange, unconstrained), S_6 (node labels), S_3
(families). The only continuous non-abelian group that acts anywhere is the spatial SO(3) on the
node's directors, and the registered three-family weave breaks it to O_h (ELEC-096). A spatial
symmetry is not an internal one, and this one is broken.

## G3, parity (a read, applied variable by variable)

Every registered energy is P-even: the torsion energy under the joint flip, cos dtheta, the cubic
harmonic (O_h contains inversion), the aligned/anti-aligned energy difference (P flips both levels,
so the relative label is P-invariant). The vacuum's absolute handedness is fixed by no registered
claim: FND-088 derives |psi_1|, |psi_2| and not their signs; FND-173 registers both relative signs
as objects. Spatial inversion reverses a winding's sign, so on the charge label P acts as charge
reversal (GRV-045, FND-008). READING: the registered vacuum is P-EVEN with a two-fold handedness
degeneracy. There is a registered handedness LABEL; there is no registered seed of parity VIOLATION.
SM_EMERGENCE row 7's "including parity violation" has nothing registered to build on.

## G4, the label table (groups and labels only, B-3)

A registered excitation carries at most: one integer (the winding, Z), one sign (handedness, or the
relative aligned/anti label for the two-frequency objects), one of three family labels, and one knot
type with its determinant (ring 1; 3_1 3; 5_1 5; 7_1 7; 4_1 5 achiral; square 9 achiral composite;
granny 9 chiral composite; FND-MATTER-019/020). No continuous internal label beyond the U(1) phase.

## G5, the count (the way ACTION-BRIDGE counted)

| level | continuous internal dimension (have) | finite internal groups |
|---|---|---|
| strand | 1 (S^1, GRV-020) | Z2 handedness flip; Z2 exchange (unconstrained) |
| node | 0 | S_6 rope labels |
| weave | 0 | S_3 families; Z2 relative handedness (a label) |

| need | real dimension | shortfall beyond the registered circle |
|---|---|---|
| SU(2) doublet | 4 | 3 |
| SU(2)/SO(3) adjoint on S^2 | 3 | 2 |
| SU(3) triplet | 6 | 5 |
| SU(3) adjoint | 8 | 7 |

Discrete shadows, named as shadows: Z2 (exchange) is the centre of SU(2); S_3 (families) is the Weyl
group of SU(3). A finite subgroup of a group is not the group.

## What this means for the goal, stated plainly

The question "why SU(3) x SU(2) x U(1)" has, for this registry, a registered answer to its third
factor and a registered reason for the absence of the first two. The U(1) is GRV-020's circle and it
is already allocated to electromagnetism. SU(2) and SU(3) are not absent because nobody has looked;
they are absent because the registered internal space has one real dimension and they need three to
eight. Adding them is not a derivation waiting to be done; it is a grant that would have to add two
to seven internal variables per strand, each with a registered energy, and the first question such a
grant faces is why the registry's one circle is not also enlarged. The discrete structure the weave
does have (three families, two strands, a handedness) sits inside those groups as their finite
shadows, which is exactly the pattern a reader hoping for emergence would be tempted to read as the
groups themselves; B-3 was written for that temptation and the commission declines it.

Parity gives the same shape of answer: the registry holds a handedness label and a P-even vacuum,
so the Standard Model's chirality has a label to attach to and no registered mechanism that prefers
one sign. Row 7's parity violation is not merely unexplained; its seed is absent.

## Consequences (adopted on the author's word, 2026-10-04: FND-185 registered; riders on GRV-020, ELEC-096, FND-088; SM_EMERGENCE rows 2, 5, 7, 8)

SM_EMERGENCE: rows 7 and 8 keep "Unexplained" and gain the registered reason (one circle; shortfall
2 to 7 real dimensions; discrete shadows only); row 2 gains the parity read (P-even, handedness
degenerate, P = charge reversal on windings); row 5 gains that the node's S_6 and the weave's S_3 are
the only non-abelian structures and both are finite. The tally 1/4/7 does not change.
GRV-020: rider recording that its SO(2) is, by this commission, the WHOLE continuous internal
symmetry of the registered weave at strand, node and weave level (not only the strand's).
ELEC-096: rider recording that its O_h result is reproduced and that the family label's symmetry is
S_3 inside O_h, with trivial identity component.
FND-088: rider recording that the derived winding fixes angles and not signs, so the vacuum's
absolute handedness is degenerate at the registered level (read, not computed).
Registration: FND-185 (the gauge inventory) if the author wants the count on its own id; the
commission recommends it, as ACTION-BRIDGE's rank-3 matrix was registered, because the count is what
a future grant would be priced against.

## Named next-order (not chartered)

None in the registry. The next step is a grant class, not a computation: "the strand carries an
internal space of dimension d" with d >= 3 and a registered energy on it. The commission does not
propose it. What it does recommend is that any future claim reading SU(2) or SU(3) into the three
families or the two strands be required to cite this commission and say which continuous directions
it has added, so the shadows are not mistaken for the groups.
