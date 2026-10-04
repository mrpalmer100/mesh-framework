# COMMISSION GAUGE-INVENTORY -- WHAT INTERNAL SYMMETRY DOES THE REGISTERED WEAVE HAVE, BY MACHINE?
# (CHARTER, LOCKED 2026-10-04 on the author's word, before any machine step)

North Star line (docs/NORTH_STAR.md section 5): names no scorecard target, input or discriminator.
It is interior work under section 5 and spends the one permitted interior session, UNLESS the
author amends section 5 to count an SM_EMERGENCE row moving as progress; the charter asks for
that ruling at lock and proceeds either way. What it moves: SM_EMERGENCE rows 7 (SU(2)_L and
parity) and 8 (SU(3)_C) from "unexplained" to "unexplained, with the registered reason named and
the missing structure counted", and row 2's chirality content read from the registry. It is to
the gauge question what ACTION-BRIDGE was to hbar: the dimension count before any mechanism.

## The question, stated so it cannot be answered by wishing

A gauge group acts on an INTERNAL space: a set of variables attached to a point of the medium
that are not positions. SU(2) needs a complex doublet (real dimension 4, or 3 after the overall
phase) with a continuous unitary action under which the registered energy is invariant; SU(3)
needs a complex triplet (real dimension 6 or 5). The registered weave has internal variables
already, each with a claim id, and GRV-020 (Derived) has computed the symmetry of one of them:
G = R x SO(2) acting on the strand's internal azimuth, helical ground state, stabiliser the screw
subgroup, ground-state manifold G/H = S^1, exactly one Goldstone, pi_1(S^1) = Z, winding = charge.
That is U(1), and it is the one Derived row of SM_EMERGENCE. This commission does for every other
registered internal variable what GRV-020 did for the azimuth, and then counts.

## Steps (reads first, then the machine)

  G1  THE INVENTORY. Every registered internal degree of freedom, at three levels, each with its
      claim id and the registered energy that depends on it; anything without an id is REFUSED:
        strand:   the frame azimuth phi (GRV-020; torsion = light); the two-strand structure of
                  a rope (ontology A2) and its exchange; the section's face orientation (FND-184,
                  the fourth grant, period pi); handedness of the level-2 winding (FND-173: both
                  handedness signs are registered as distinct objects; GRV-045: one 2 pi quantum
                  of frame winding exchanged at reconnection).
        node:     the director angles of the ropes meeting there and the director-locking energy
                  J (1 - cos dtheta) (FND-001); the coordination z (FND-148); the three strand
                  families and their registered angles (EM-RECON-018 counting; FND-091 angles).
        weave:    the family labels as a field over the lattice (which family a strand belongs to
                  at a site), the aligned/anti-aligned relative handedness (FND-173/174).
      The inventory records, for each variable: its range (circle, discrete set, interval), the
      registered energy's dependence on it (exact form or "appears in no registered energy"), and
      whether it is local (attached to a point) or global.
  G2  THE GROUP, BY MACHINE. For each level, the configuration space is the product of the G1
      variables at that level; the group is the set of transformations of that space leaving every
      registered energy of G1 invariant. Computed with sympy: for continuous variables, the Lie
      algebra of invariance (solve for the generators that annihilate the energy); for discrete
      variables, the permutation group preserving the energy, enumerated. Output per level: the
      identity component (a connected Lie group, named by dimension and type), the discrete part,
      and the dimension of the internal space it acts on.
      CONTROL: at the strand level, G2 must return GRV-020's G = R x SO(2) with G/H = S^1 from the
      registered azimuth energy (torsion stiffness) alone. If it does not, REFUSED (instrument fault).
  G3  PARITY. Apply the spatial inversion P and the handedness flip to every G1 variable and ask
      which registered energies change. The registered vacuum is P-EVEN if every registered energy
      is invariant and the ground state is mapped to a degenerate ground state; P-ODD if a
      registered energy or the registered ground state (FND-091's pitch sign; the aligned family's
      handedness, FND-173/174) distinguishes the two. Read, not computed: whether the registry
      fixes ONE handedness for the vacuum or registers both as degenerate.
  G4  THE REPRESENTATION TABLE. Every registered excitation labelled by the G2 quantum numbers:
      winding number (FND-008), handedness (FND-173, GRV-045), family (EM-RECON-018), knot type
      and determinant (FND-MATTER-019's six certified knots), the two-frequency members' (q,
      handedness) labels (FND-173/174). A table of labels, not a match to particles. B-3 forbids
      naming a Standard Model particle in it.
  G5  THE COUNT. For SU(2): does any level's internal space contain a real 3- or 4-dimensional
      subspace on which the G2 group acts as SU(2) or SO(3)? For SU(3): a real 5- or 6-dimensional
      one with SU(3)? If not, state the dimension the registered internal space HAS at each level
      and the dimension it would NEED, as a count, the way ACTION-BRIDGE stated its rank-3 matrix.
      Discrete shadows are named as such: Z2 (strand exchange) sits inside SU(2) and S3 (family
      permutation) inside SU(3), and sitting inside is not being.

## Bars (LOCKED before any step)
B-1  Only registered variables enter G1. A variable the author or the executor "would expect" the
     weave to have is REFUSED by name; the refusal is part of the result.
B-2  The control (G2 reproducing GRV-020 at the strand level) runs before any other group is
     computed and before any parity read.
B-3  No Standard Model particle, multiplet or coupling is named in G4 or G5. The output is groups,
     dimensions and labels. Any sentence of the form "X could be the electron" is struck.
B-4  No new energy term is introduced to make a symmetry appear or disappear; G2 uses the
     registered energies as written, including their registered absences ("appears in no
     registered energy" is a result, and a variable with no energy has the full group of its range,
     which is recorded as UNCONSTRAINED, not as a gauge symmetry).
B-5  The honest prior is stated here and not leaned on: DISCRETE-ONLY, with the continuous part
     exactly GRV-020's SO(2).

## Verdict forms (LOCKED)
CONTINUOUS-STRUCTURE-FOUND  some level's registered internal space carries a continuous invariance
                            group larger than SO(2) acting on a subspace of the right dimension for
                            SU(2) or SU(3). The commission names the level, the variables, the
                            group and the energy that is invariant, and STOPS: whether it is a gauge
                            symmetry (local, with a connection) is a second commission.
DISCRETE-ONLY               the continuous part at every level is GRV-020's SO(2) (possibly times
                            translations) and the rest is finite (Z2, S3, the node's point group).
                            Rows 7 and 8 of SM_EMERGENCE take the registered reason: the weave's
                            internal space is one circle; SU(2) and SU(3) have no registered room.
NEW-INTERNAL-SPACE-NEEDED   DISCRETE-ONLY plus the count: the internal dimension at each level and
                            the dimension SU(2) and SU(3) would need, as the price of a grant that
                            would have to add internal variables with registered energies. The
                            count is registered; no grant is proposed.
P-ODD / P-EVEN              recorded alongside whichever form above, from G3; P-ODD with one
                            registered vacuum handedness is the registered seed of row 7's parity
                            content and is stated as a seed, not as parity violation.
REFUSED                     B-2 fails.

## Rules
No rescue; reads before the machine; the control before any group; registrations and riders the
author's; failure kept; no particle names (B-3); the prior stated and not leaned on (B-5).

## Reads owed at lock
GRV-020 and benchmarks/gravity/internal_symmetry_theorem.py (the registered theorem and its
energy); GRV-067 (the Goldstone identification, phi as the coordinate); FND-001 (J in dtheta);
FND-148 (z); EM-RECON-018 and FND-091 (families, angles, pitch sign); FND-173/174 (both
handedness signs registered); GRV-045 (frame winding at reconnection); FND-184's grant record
(the face variable and its period); FND-MATTER-019 (the certified knots and determinants);
ontology.md A1/A2; the North Star section 5 ruling on whether an SM_EMERGENCE row counts.

## Cost
Sandbox; one session; sympy only.

## Author's lock
Locked on the author's word on 2026-10-04 ("lock GAUGE-INVENTORY"). No machine step had run. No
ruling was given on North Star section 5, so the commission is booked as the one permitted interior
session; the author may re-book it if an SM_EMERGENCE row moving is later ruled progress.

## READS AT LOCK
GRV-020 (Derived) and benchmarks/gravity/internal_symmetry_theorem.py: G = R_slide x SO(2)_rot acts on
  the internal azimuth phi(s) by phi(s) -> phi(s - a) + alpha; helical ground state phi_0 = tau_0 s;
  stabiliser the screw {alpha = tau_0 a}; G/H = S^1; one Goldstone; pi_1 = Z, winding = charge,
  torsion = light. The registered energy is the torsion stiffness in (phi' - tau_0). This is the
  control the instrument must reproduce.
GRV-067: the Goldstone coordinate is the frame orientation phi; the locking mass term is forbidden
  (kappa = 0 exactly by Goldstone's theorem). So phi has no on-site energy at the registered level.
FND-001: node energy E* = (T^2/kappa)(1 - cos dtheta) in the DIRECTOR angle only; a point bond
  (JUNCTION-LOCK: the ropes' azimuths do not appear, f = 0). FND-148: coordination z, cubic
  networks, wave medium above z_c = 3.75, embedding near z = 6.
ELEC-096: the registered direction set {x, y, z} (three families) is invariant under O_h and not
  under SO(3); lowest non-trivial cubic harmonic sum n_i^4 (order 4); odd orders killed by pole
  equivalence (ELEC-091). The three-family weave breaks rotational symmetry to O_h.
EM-RECON-018: three families by coverage counting; in-family and cross-family standoff readings.
FND-088/089 (and FND-091): the two-level winding's angles psi_1 = 35.2644 deg, psi_2 = 59.4444 deg
  are derived with no free angle and NO SIGN: the derivation fixes |pitch angle|, not handedness.
FND-173/174/140: the true state is a two-frequency object; BOTH level-2 handedness signs
  (aligned and anti-aligned relative to level 1) are registered as real, structurally different
  objects with different om2. Relative handedness is a registered Z2 label that the energy
  distinguishes; absolute handedness is not fixed by any registered claim.
GRV-045: material handedness (charge) is the sign of an extensive winding; reconnection exchanges
  one 2 pi quantum and cannot flip the sign. Under spatial inversion a winding's sign flips, so P
  acts on the charge label as charge reversal.
FND-184: the face variable is the two-strand section's orientation, period pi; it is the azimuth
  phi of the rope read modulo pi, not an independent circle.
FND-008: topological charge = integer winding, quantised and conserved.
FND-MATTER-019/020: certified knots ring, 3_1, 5_1, 7_1, square, granny (determinants 1/3/5/7/9/9)
  and 4_1 (det 5); FND-MATTER-021/022: the braid family seated by certified word search.
ontology.md: A1 (d = 3), A2 (the rope has two strands, N = 2).
