# JOIN-SYMMETRY: the gauge group a join of registered strands can carry (a reading, 2026-10-29)

Executor's reading on the author's word; no commission, no number compared with measurement, no registration
(the rider at the end is proposed for the author's decision). Instrument: benchmarks/foundations/
join_symmetry_reading.py; log analysis/JOIN_SYMMETRY_reading.log.

## 1. The question, and why it is new

FND-185 (GAUGE-INVENTORY) counted the registered weave's internal symmetry at the strand, the node and the weave:
one continuous group, the azimuth SO(2) (GRV-020), already spent on electromagnetism (winding = charge, torsion =
light); everything else finite (Z_2 handedness, S_6 rope labels at a z = 6 node, S_3 families). Its verdict for rows 7
and 8 of docs/SM_EMERGENCE.md: an SU(2) doublet needs 3 to 4 real internal dimensions per strand and an SU(3)
triplet 6 to 8, against the registered 1.

Chain Theory (A. Wissner-Gross, October 2026) obtains the Standard Model gauge group another way: not from the
internal space of one constituent but from the JOIN of two, as what survives of the local basis freedom at the two
ends of a maximally entangled qutrit-qubit pair once the pair is joined. In group terms: the gauge group at a join is
the stabilizer of the joined state under the product of the ends' local groups (there U(3) x U(2); the surviving
factors assemble into SU(3) x SU(2) x U(1) / Z_6 across the link types). FND-185 did not ask that question of the
mesh's join, the registered two-strand contact of FND-184. This reading asks it.

## 2. The computation

The ends: two identical strands, each with local group SO(2) (its azimuth phi), so the product is the torus
SO(2) x SO(2), extended by the strand swap Z_2. The joined state: the registered contact, whose energy is a function
of the two azimuths with period pi in each and flat lying preferred (FND-184, the two-disc section): in the
lowest harmonic, V_R = -A [cos 2 phi_1 + cos 2 phi_2]. For contrast, the one contact form that WOULD carry a
continuous phase at the join, not registered: V_H = -A cos 2 (phi_1 - phi_2), a relative-azimuth (Josephson-like)
contact. The group at the join is the subgroup of the torus (and swap) leaving V invariant; found by brute force on
a 96 x 96 grid of the torus.

Result (log):
- (R) the registered join: four invariant shifts, (0, 0), (pi, 0), (0, pi), (pi, pi), each also with the swap; no
  continuous family. The group is (Z_2 x Z_2) x| Z_2, order 8, finite, non-abelian only through the swap. Both
  azimuth circles are broken by the contact; no continuous phase survives the join.
- (H) the relative-azimuth contact: a continuous family (the common azimuth, phi_1 and phi_2 shifted together) times
  Z_2 (the relative shift by pi): U(1) x Z_2. That U(1) is the pair's common azimuth, the Goldstone of GRV-020 that
  electromagnetism already owns; it is nothing new, and the contact form that keeps it is not the registered one.

## 3. The general statement, which is a theorem and not a grid

The stabilizer of any state under an action of a group G is a subgroup of G. With the registered ends, G is a torus
(times a finite swap), and every subgroup of a torus is abelian. So no join of registered strands, of any number of
strands and with any contact energy whatever, carries a continuous non-abelian group: at most a sub-torus of the
ends' azimuths, extended by finite relabelings (the S_k of k identical strands, FND-185's S_6 at a node). Chain
Theory's non-abelian factors come from its ENDS (U(3) and U(2)), and the join only selects among them. The join
cannot manufacture what the ends lack. FND-185's shortfall of 2 to 7 real internal dimensions per strand stands at
the join exactly as at the strand: rows 7 and 8 of SM_EMERGENCE do not move, and the reason is now stated for the
join as well as for the constituent.

What the join CAN do, stated so it is not lost: it selects. Of the ends' torus, the registered contact keeps a
finite group and the relative-azimuth contact keeps a circle. If a later registered contact form depended on the
relative azimuth (a two-strand engine of Phase 2b would say), the join would carry U(1) x Z_2, with the U(1) the
one already spent. The Z_2 x Z_2 of the registered join is the period-pi lock seen as a symmetry: the two half-turn
shifts that the SWEEP sheet (T-2) found split a unit kink into two half-kinks. Same object, group-theoretic face.

## 4. What transfers from Chain Theory, and what does not

Transfers: the question's form (the gauge group as the stabilizer of a joined state under the ends' local groups), a
one-line computation here with a definite negative. Does not transfer: the non-abelian content, which in Chain Theory
is carried by ends of dimension 3 and 2, and the mesh's registered end has dimension 1. The honest reading of row 7
and row 8 is unchanged: a weak or strong gauge group needs a strand with more internal room than the registered
one, and that room needs a registered energy; neither a node nor a join supplies it.

## 5. Proposed rider (for the author's decision; not registered by this reading)

On FND-185 and on SM_EMERGENCE rows 7 and 8, "What is missing" column: "[JOIN RIDER 2026-10-29, analysis/
JOIN_SYMMETRY_reading.md: the shortfall holds at the join as at the strand. The symmetry of a join is the stabilizer
of the contact state in the product of the ends' groups, a torus for registered strands, so it is abelian up to
finite relabelings whatever the contact; the registered contact (FND-184) keeps (Z_2 x Z_2) x| Z_2, and a relative-
azimuth contact would keep only the U(1) already spent on electromagnetism. A non-abelian gauge factor requires
non-abelian ends, i.e. the internal dimensions FND-185 counts as missing.]"
