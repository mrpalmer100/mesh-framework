# THICK-ROPE-SYMMETRY: what a rope's thickness adds to its internal space, and what it cannot add (a reading, 2026-10-29)

Executor's reading on the author's word, after his question on the JOIN-SYMMETRY reading: the registered strand's
internal space has real dimension 1 (FND-185), but a rope is three-dimensional, thin and not a line; does its thickness
supply the internal dimensions the weak and strong groups need? No commission, no number compared with measurement, no
registration (the rider at the end is proposed). Instrument: benchmarks/foundations/thick_rope_symmetry_reading.py;
log analysis/THICK_ROPE_SYMMETRY_reading.log.

## 1. Two different dimensions

The mesh has three spatial dimensions (axiom A1), and its ropes have thickness: the two-disc section of FND-184 is that
thickness taken seriously, and the rope level of FND-188 (n_rs strands, R = 113 a) more so. The "dimension 1" of
FND-185 is not the rope's size. It is the real dimension of the strand's INTERNAL STATE SPACE: the set of ways the
strand can differ from itself at a point along its length, with a registered energy. For the registered strand that
space is the azimuth, one angle, and its symmetry is the rotation of that angle, SO(2), spent on electromagnetism.

A gauge group is a symmetry of the internal state space that leaves the energy unchanged. SU(2) acts on a space of
at least three real dimensions and needs the energy invariant under all of SU(2); SU(3) on at least six (eight for
the adjoint). FND-185's shortfall is a count of such dimensions. The author's point is that a thick rope has more
internal freedoms than an angle, and none of them was counted because none has a registered energy. That is correct,
and it makes the question precise: for each freedom thickness supplies, what is the symmetry of its energy?

## 2. The freedoms, and the symmetry of each

The rope's local frame is its tangent t and the section plane perpendicular to it. Every geometric freedom of the
section is DEFINED relative to the axis, so the only rotations that act on it are the rotations about t (a rotation
tilting the plane does not map the state space to itself). The instrument samples random states of each freedom and
tests the energy's invariance under the generators of the rotations that act; the stabilizer's Lie algebra is a
subalgebra of so(3), so its dimension is 0, 1 or 3. The energies are the generic ones elasticity gives: functions of
the mode's own rotation invariants.

| freedom | state space | what acts | symmetry of the energy |
|---|---|---|---|
| azimuth phi (registered) | 1 | rotations about t | SO(2): the Goldstone, spent (GRV-020) |
| elliptical section (eps, psi) | 2 | rotations about t | SO(2) (the energy is f(eps^2)) |
| core offset u in the sheath | 2 | rotations about t | SO(2) (f(abs(u))) |
| twist rate tau | 1 | nothing continuous | finite |
| positions of n strands in a bundle section | 2n | rotations about t, relabelings S_n | SO(2) x| S_n |
| two section amplitudes of unequal stiffness | 2 | rotations about t | finite only |
| a 3D director d with energy f(d . t) (a tilted core) | 2 | all rotations | SO(2) about t |
| a 3D director d with energy BLIND to the axis (hypothetical) | 2 | all rotations | SO(3) = SU(2)/Z_2 |

Thickness raises the dimension count freely: two real dimensions per section mode, 2n for a bundle, as many as one
likes. It never raises the symmetry. Every section freedom's energy is invariant only under rotation about the
tangent, the same circle the azimuth already provides, and rotations about one axis commute. Two section modes of
unequal stiffness (the generic case) have no continuous symmetry at all. The one entry with a non-abelian group is
the director whose energy does not know which way the rope runs, and that is not a geometric mode of the section,
because the section is defined by the axis.

## 3. The statement

A rope's thickness supplies internal DIMENSIONS; the weak and strong groups need internal SYMMETRY, a freedom whose
energy is blind to the rope's own axis. Nothing built from the section can be blind to the axis that defines the
section. So a non-abelian internal group requires a new internal field carried along the strand (a free
three-dimensional director, or a two-component amplitude whose energy depends only on its magnitude) with a
registered energy that has the invariance: FND-185's "a registered energy per missing dimension," restated as a
physical condition rather than a count. The join (JOIN-SYMMETRY, same day) cannot supply it either: a stabilizer in
the product of abelian end groups is abelian.

What this does NOT say: that the mesh cannot have such a field. It says the registered rope does not, that thickness
alone does not create one, and that whoever proposes one must register its energy and show the invariance, which is
the same bar every other primitive meets.

## 4. Proposed rider (for the author's decision)

On SM_EMERGENCE rows 7 and 8, "What is missing": "[THICKNESS RIDER 2026-10-29, analysis/THICK_ROPE_SYMMETRY_reading.md:
the missing internal dimensions cannot come from the rope's thickness. Every freedom of the section (ellipticity,
core offset, twist, bundle positions, section amplitudes) has an energy symmetric only under rotation about the
tangent, SO(2), the azimuth's own circle; a non-abelian factor needs an internal freedom whose energy is blind to the
axis, a new field with a registered energy.]"
