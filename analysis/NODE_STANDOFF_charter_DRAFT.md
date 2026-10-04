# COMMISSION NODE-STANDOFF -- HOW FAR APART ARE CROSSING STRANDS AT A NODE OF THE VACUUM WEAVE?
# (CHARTER, DRAFT 2026-10-04; becomes LOCKED on the author's word, before any number)

North Star line (docs/NORTH_STAR.md section 5): arms a discriminator. CROSSING-PRICE reduced the
chain from the fourth grant to FND-182's number to one unregistered quantity: the standoff d/sigma
of two crossing strands at a node of the vacuum weave, in units of the strand width. Touching
crossings self-trap the charge-kink and put the breakdown field 500 times above Schwinger;
crossings at the lattice spacing put it at 1e9 V/m and kill the reading; the window in which
FND-182 is a discriminator is d/sigma of about 5 to 20, and the registered coasting regime of the
kink sits inside it. This commission reads the standoff from the registered geometry of the weave,
or finds that the weave's node geometry is not a registered object and says so.

## The question, stated exactly

At a node of the coarse vacuum weave, where a strand of one family crosses a strand of another,
what is the centre-line separation d of the two strands at closest approach, in units of the
strand width w (= sigma_0, EM-RECON-018)? Three readings are possible and the registry must
pick one or none:
  (i)   touching: d ~ w (the strands press at the node; a woven over-under lattice);
  (ii)  spaced: d ~ a (the strands pass through the node region without pressing; a lattice of
        lines at the spacing, thickness d_c = 0.003 a at kappa_pack 1);
  (iii) intermediate: d set by a registered helical or two-level geometry (FND-091's angles and
        pitch; the fine fibres' winding bringing crossing partners to within a few widths).

## Protocol (sandbox; reads and geometry, one session)

  G1  The coarse weave as registered: how many families cross at a node, at what angles
      (EM-RECON-018's three-family counting; the director-field lattice of FND-001/002; the
      triaxial geometry the Casimir and winding instruments assume), and whether the registered
      node is a point where three strands meet or three pairwise crossings.
  G2  The strand width at the coarse level: d_c = 1.87e-19 m (HBAR-005; the two-strand rope's
      section 4 rho x 2 rho) against the spacing a at each scale set; and whether any registered
      claim places coarse strands in contact at nodes (the lock of EM-RECON-012 is a within-strand
      screw-stretch coupling and does not; FND-KIN-005's interpenetration is a primitive).
  G3  The two-level geometry: FND-091's derived angles and pitch regime; whether the fine fibres'
      winding gives a crossing partner's closest approach as a derived multiple of the width.
  G4  The reading: d/sigma from G1 to G3 as a number or a bracket, with every input cited, or the
      statement that the node geometry is unregistered and what would register it.
  G5  If G4 returns a number or bracket: CROSSING-PRICE's chain evaluated at it (the chain is
      sealed; this step is arithmetic on registered inputs plus the bound on A_c), giving FND-182's
      E_c as a lower bound with scale-set spread, read against the laser record and Schwinger.

## Bars (LOCKED before any number)
B-1  No standoff is chosen; a reading that rests on an unregistered packing or weave assumption
     is REFUSED and the assumption named.
B-2  Every input in G1 to G3 carries its claim id.
B-3  G5 runs only on a G4 number or bracket; the coincidence of CROSSING-PRICE (the coasting
     regime inside the window) is not an input and is not used to choose.
B-4  The sqrt3 re-solve FND-068 owes on the standoff readings is NOT performed here; if the
     reading depends on it, that dependence is stated and the result bracketed over it.

## Verdict forms (LOCKED)
STANDOFF-DERIVED      G4 returns d/sigma as a registered-input number or bracket. Then G5 gives
                      FND-182's field (lower bound in A_c) and exactly one of: IN-WINDOW (a firm
                      discriminator candidate; ELEC-101 re-read; FND-182's T2 revisited with the
                      number on its face), ABOVE-QED (no discriminator; registered as a number),
                      BELOW-DATA (FND-184's F1 fires: the reading dies, Failed and kept; the
                      commission says whether touching, spacing or the convention is the cause).
STANDOFF-TOUCHING     G4 finds the registered weave has pressing crossings at nodes (reading i):
                      a special case of DERIVED with ABOVE-QED and the self-trapped kink; FND-181's
                      coasting regime takes a rider.
STANDOFF-SPACING      G4 finds the registered weave has crossings at the spacing (reading ii):
                      a special case of DERIVED with BELOW-DATA.
STANDOFF-UNREGISTERED G4 finds the node geometry is not a registered object (the registry has a
                      lattice of lines and a coverage, but no statement of what two strands do
                      where they cross): named; no number; the registration that would fix it
                      stated as the next-order (a grant-class statement about the weave's nodes,
                      or a derivation from the two-level winding if G3 can supply it).
REFUSED               B-2 fails on every route.

## Rules
No rescue; no standoff chosen to land in the window; reads at lock; every number from a cited
input; riders and registrations the author's; failure kept.

## Reads owed at lock
FND-001/002 (the director lattice), EM-RECON-018 (three families; the counting), FND-091 (the
angles, the pitch regime), FND-087 (n_sub; the fine fibres' arrangement inside a coarse strand),
HBAR-005 (d_c), ROPE_PARAMETERS (the scale sets; section 6), EM-RECON-012 (the lock: within-strand),
FND-KIN-005 (interpenetration primitive), GRV-036 (the comb), the Casimir instrument's lattice
assumptions (casimir_f3.py, casimir_plate.py: what geometry they assume at a node).

## Cost
Sandbox; one session.

## Author's lock
Locked on the author's word on: ______ . Until then no number is computed.
