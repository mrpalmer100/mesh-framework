# The Gapped-Phase Medium: a clean-room design study of a mechanical electron
# (the author's request, 2026-10-27; written in its own vocabulary, with no rope or mesh words in Part I,
# then mapped onto the registry in Part II; a design study, not a claim; nothing here is registered)

## Part I. The model, written clean

### 1. Discipline
Part I uses only these words for the physical content: medium, tension, phase, winding, frame, gap, soliton.
It assumes nothing from any existing programme. Every statement is either an axiom (marked A) or a derivation
from the axioms (marked D). The electron's measured properties are the target, listed once in section 4, and the
model is scored against them there. Numbers with units appear only in section 4's scoring, where the target's
mass and spin are used to read the medium's constants off the model, never the other way round.

### 2. The axioms
A1  THE MEDIUM. Space is filled by a continuous elastic medium with a tension T (energy per length along any
    line of it) and inertia T / c^2 per length, so that transverse disturbances travel at c. The medium carries one
    internal angle, the PHASE theta, valued modulo 2 pi, with stiffness K: a gradient of the phase along a line
    costs (K / 2)(d theta / ds)^2 per length and a rate of change costs (K / 2 c^2)(d theta / dt)^2, so phase waves
    also travel at c. sqrt(K / T) is the one length the medium's constants define, and K / c is its one action.
A2  WINDING IS CHARGE. The medium's lines close on themselves, and a closed line carries an integer, the number of
    times its phase winds around the circle. Winding is conserved under every smooth motion and changes only when
    two lines of opposite winding are created or destroyed together. Charge is winding; its sign is the particle
    versus the antiparticle; its exactness and universality are topology.
A3  THE FRAME. A line of the medium is a ribbon, not a curve: it carries a material frame, and the frame is tied to
    the medium far away. Rotating the object once (2 pi) therefore twists the frame against its anchoring and is a
    different configuration from not rotating it; rotating it twice (4 pi) can be undone. Configuration space has
    the belt topology (its fundamental group is Z_2).
A4  THE BEAT. The medium has one intrinsic frequency Omega, a mode that resonates: a disturbance of the phase at
    that frequency is sustained by the medium and a disturbance at other frequencies is not. The medium's screening
    length is lambda = c / Omega: beyond lambda the medium relaxes a winding's far field, so a winding's energy
    and angular momentum are finite and localized.
A5  THE SOLITON. The elementary object is a stationary solution of the medium's equations with no free amplitude:
    its energy E, its size and its internal frequency omega are fixed by (T, K, Omega) and the winding. There is no
    family of such objects at a given winding with continuously varying energy.

### 3. What follows
D1  THE QUANTUM OF ACTION IS A MEDIUM CONSTANT. By A5 the elementary object has a fixed energy E and a fixed
    internal frequency omega. Their ratio is therefore a constant of the medium, and it is of order K / c for any
    object whose motion is a phase wave (the energy is K times a gradient squared times a length, the frequency is
    c over that length). Define hbar := E / omega for the elementary object. Then E = hbar omega for every object
    the medium makes, because every object is built from the same phase waves with the same K. Universality of
    the quantum is the universality of K.
D2  THE RING SOLUTION. A closed line of radius R carrying one unit of winding with its phase travelling along the
    line at c: the phase energy per length is (K / 2)(1 / R)^2 twice (gradient and rate, equal for a wave at c), the
    tension energy is T per length, so E(R) = 2 pi R T + 2 pi K / R, stationary at R* = sqrt(K / T) with E = 4 pi
    sqrt(K T), half in tension and half in the wave. The wave's momentum flux circulates, giving angular momentum
    J = 2 pi K / c, independent of R (the ring-wave of the author's Leg C, in this vocabulary). The internal
    frequency is omega = c / R*, so E / omega = 4 pi K / c: D1's constant for this object, with the number 4 pi.
D3  THE GYROMAGNETIC RATIO. The winding moves with the wave at c; the tension does not move. The magnetic moment is
    the winding's current times the area, mu = q c R / 2; the angular momentum is J = E_wave R / c with E_wave =
    E / 2. So g = (mu / J)(2 m / q) = E / E_wave = 2, exactly, for any closed shape: the shape theorem. The 2 is
    the statement that half the mass is at rest and the charge is not.
D4  THE DOUBLE COVER. By A3 the ring's frame returns to itself only after a 4 pi rotation; quantizing the ring as
    a Z_2-framed object gives spin 1/2 (Finkelstein and Rubinstein). D3's g = 2 and A3's spin 1/2 are two faces of
    one fact only if the winding's current closes after two traversals of the loop, that is, if the phase wave and
    the frame twist are locked so that one circuit of the wave carries half a turn of the frame. This locking is
    the one derivation Part I does not complete; it is stated as the model's internal consistency condition C1.
D5  THE EXTERNAL CHECK. Seen from far away, a charged object with mass m, charge q and angular momentum J in a
    medium whose large-scale response is Einstein's must look like the Kerr-Newman solution with those
    parameters, which has g = 2 and a ring of radius a = J / (m c) (Carter 1968). For D2's ring, J / (E / c^2 . c)
    = (2 pi K / c) / (4 pi sqrt(K T) / c) = R* / 2. So the model's ring and the geometric ring agree on g and
    differ by exactly a factor 2 in radius, the Kerr-Newman ring sitting at half the phase ring. Both facts are
    fixed by the axioms with no number chosen.
D6  QUANTIZATION AS RESONANCE. A4 gives the medium one frequency Omega. An object whose internal clock runs at
    Omega / 2, half the medium's beat, is sustained by its own wave (the period-doubled response of a driven
    medium, the mechanism of the walking-droplet experiments): its orbits are quantized where the clock and the
    wave agree, and the 2 pi versus 4 pi structure of A3 is the period doubling itself. For the elementary object
    omega = Omega / 2 is therefore not an extra assumption; it is A4 and A5 together. Its size is then R* =
    c / omega = 2 lambda, twice the screening length.
D7  PAIR CREATION. A2 forbids creating one winding; two of opposite sign can be created from a phase wave of
    energy at least 2 E. The threshold is 2 E, the pair's rest energy, with nothing else.
D8  THE MASS IS THE MEDIUM'S. Combining D2 and D6: R* = sqrt(K / T) = 2 c / Omega, so T = K Omega^2 / (4 c^2) and
    E = 4 pi sqrt(K T) = 2 pi K Omega / c = 2 pi (K / c) Omega. With D1's hbar = 4 pi K / c this reads E = (hbar / 2)
    Omega = hbar omega. The elementary mass is the medium's beat times the medium's action: m c^2 = hbar omega.
    The object does not own its mass; the medium does.
D9  GENERATIONS. A5 allows other stationary solutions at the same winding (higher radial or azimuthal modes of
    the ring, or objects of different frame structure); their energies are fixed ratios of E set by (T, K, Omega).
    The model predicts a discrete spectrum of charge-one objects. Which ratios is the model's second incomplete
    derivation, C2.

### 4. Scoring against the electron
    property                                   model                                      status
    charge exact, conserved in pairs            A2 winding                                  met
    stable                                      A2 topology                                 met
    spin 1/2, Fermi statistics                  A3 belt topology, D4                        met, conditional on C1
    g = 2 at tree level                         D3 shape theorem                            met
    Compton size of (E, J): R >= J c / E        D2: J c / E = R* / 2                        met (saturated within 2)
    pointlike charge below 1e-19 m              NOT met by D2 as written (the winding sits on the ring); see 5(i)
    J finite and environment-independent        A4 screening, D6                            met
    quantization, E = hbar omega                D1, D6                                      met; hbar = 4 pi K / c
    pair threshold 2 m c^2                      D7                                          met
    Kerr-Newman exterior (g = 2, a = lambda_C/2) D5                                         met, with R* = 2 a
    generations                                 D9                                          open, C2
    chirality, weak doublet                     no axiom                                    not addressed
    the anomaly alpha / 2 pi                    needs the medium's self-field               not addressed here
Reading the medium's constants off the target (the only place the target's numbers enter): from J = hbar / 2 and
D2, K = hbar c / 4 pi = 2.5e-27 J m; from m_e c^2 = 4 pi sqrt(K T), T = m_e^2 c^3 / (4 pi hbar) = 1.7e-2 J/m; from
D6, Omega = 2 c / R* = 2 m_e c^2 / hbar = 1.55e21 rad/s, the zitterbewegung frequency, and lambda = c / Omega =
lambda-bar_C / 2 = 1.9e-13 m. The model's medium is therefore specified by three numbers: a tension of 17 mN, a
phase stiffness of 2.5e-27 J m, and a beat at the zitter frequency. Nothing in Part I says why those three.

### 5. What Part I does not do (the open design items, each named once)
(i)  POINTLIKE CHARGE. D2 puts the winding on a Compton-size ring, which would scatter as a ring. The constraint
     needs the charge seen from outside to be a scalar topological number of the whole object (a linking or Hopf
     number) sourced at a core, with the ring-scale structure carrying J and mu but not the charge's form factor.
     The design that does this is the SCREENED VORTEX: a pointlike winding core whose far field is relaxed beyond
     lambda by A4; its angular momentum is in the screened circulation, its charge at the core. Part I solves the
     ring because the ring is solvable; the vortex is the object the constraints want, and its solution needs the
     mechanical form of A4's relaxation (a second, gapped mode of the medium that compensates the phase gradient
     at distance, as a superconductor's current compensates a vortex's phase). That compensator is design item 1.
(ii) C1, the locking of the phase wave to the frame (one circuit, half a turn), which makes g = 2 and spin 1/2
     one fact. Design item 2.
(iii) C2, the spectrum of charge-one objects. Design item 3; Dirac's membrane electron failed here (53 against
     207) and any version of this model must be scored on it.
(iv) Chirality. A4's beat has no handedness; the weak interaction's does. The medium would need a handed beat or
     a handed frame. Not designed.
(v) Why K, T and Omega. The model converts "why hbar, why m_e" into "why these three medium constants", which is
     progress in form (three constants of one medium instead of properties of many particles) and not in content.

## Part II. The map onto the registry

### 6. Axiom by axiom
A1  REGISTERED. The medium is the weave; T is T0 = 434 J/m (FND-MATTER-044); the phase is the rope's twist angle
    with the Goldstone stiffness kappa (GRV-020); phase waves at c are EM-RECON-012. The registered stiffness
    of the two-strand rope is kappa_pair = 0.035 T0 a^2 = 5.5e-32 J m (consult reading A), against the model's
    K = 2.5e-27: short by 4.6e4. The registered tension is 2.6e4 above the model's T. These are N1's two numbers.
A2  REGISTERED. Charge is the linking of a rope's two strands (GG-006, GRV-020); conserved by identity, pairs
    annihilate free (FND-KIN-005); winding transported exactly (FND-STRAND-002).
A3  REGISTERED IN STRUCTURE, UNTESTED AS SPIN. The rope is framed, the Calugareanu ledger holds live on the strand
    engine (FND-STRAND-003), the one-generator theorem makes the ribbon's fiber the holonomy (GRV-020). Whether
    the exchange of two framed ropes equals a 2 pi frame rotation is the Director's FRAMED-EXCHANGE-FR, never run.
A4  ABSENT, and this is the whole map. The registered twist mode is a Goldstone (GRV-020), massless; JUNCTION-LOCK
    found no on-site potential at the registered level (f = 0); the one registered way to gap it (the face-holding
    tie, f about 3.5) gaps it at a GeV-class frequency with a screening length of a strand spacing, not at the zitter
    frequency with a screening length of a Compton wavelength. The medium has no beat at m_e. Every electron
    candidate the registry has tried failed on the number that A4 supplies.
A5  REGISTERED FOR THE RING. The travelling-twist ring is a stationary solution with no free amplitude (Leg C;
    the shape theorem; the dynamics instrument's K3). RING-WAVE-STABILITY-2 asks whether it persists.
D2 to D5  REGISTERED OR ON RECORD. The ring's closed forms are Leg C's; g = 2 is Leg C section 5's theorem; the
    Kerr-Newman check is new here and costs nothing: the registered ring has R* = lambda-bar_C at the electron
    point and the geometric ring sits at half of it, by the same arithmetic.
D6  ABSENT. No registered resonance; no registered period doubling. The walker mechanism has no mesh analogue yet.
D8  CONTRADICTED BY THE LADDER AS REGISTERED. The model says the elementary mass is the medium's beat times its
    action. The registry's ladder (FND-110) puts no rung at the model's T and no mode at the model's Omega; N1's
    "missing rung" and A4's "missing beat" are the same absence seen from the tension side and the frequency side.
5(i) THE VORTEX. The registered medium has no compensator mode; the twist's far field is not relaxed; a winding's
    far field is the registered 1/r conditioning (GRV-005), unscreened. Design item 1 has no registered object.

### 7. The one question the map leaves
Everything the model needs that the registry lacks is A4: a mode of the medium at the zitter frequency, with
the twist's far field relaxed beyond half a Compton wavelength. Supply it and the ring, the vortex, the
quantum, the mass and the Kerr-Newman exterior follow from registered structure (sections 3 and 6). Nothing
registered produces it, and the two routes the registry has tried to gap the twist (the junction tie; the
substructure count) gap it at the wrong frequency by four to nine orders. The question for the author's desk is
therefore not "which object is the electron" but "what in the medium beats at 1.55e21 radians per second", and
whether that is a grant (a registered resonance with its falsifier stated first) or a derivation from something
already registered that nobody has asked. The executor's reading of the registry's own candidates for a beat,
so that none is proposed by mistake: the junction tie gaps the twist at a strand-spacing length (GeV class); the
fine level's rotating-wave winding (FND-130/131) turns at a frequency of order c / a_f, nine orders above the
zitter frequency at the grant's a_f; the granted rope (FND-188) has a radius of 113 spacings against the 3,200
spacings that c / Omega = lambda-bar_C / 2 would need. Nothing registered beats within three orders of the
electron, in either direction. The beat is a new mechanism or it is nothing; that is the honest end of the map.

### 8. Name
Inside the programme this is the Gapped Twist model: the mesh plus one mechanism. If it were ever its own
programme it should be named for the mechanism and not the material; the author's choice. The executor's
suggestion was Cadence, for a medium with a beat and an object that keeps time at half of it.

## 9. Postscript (2026-10-27, the same day): the beat was pursued and the lesson registered
A4 was supplied as a grant candidate (SWEEP, a weak lock on the azimuth; allowed because light is not on the
azimuth, GRV-102 / EM-RECON-025, which Part II section 6 had missed) and priced with three cheap tests. The beat is
real on the instrument (B1: gapped dispersion, a Compton-width relativistic kink), the chain lands the charge-creation
field at pi / 5 of Schwinger as an identity (T-1), the double cover and the unit charge are different states of the
rope (T-2, C1 fails), and design item (i) is answered in the negative with a number (T-3, registered as FND-189): at
the registered strand spacing, charge carried on strands is one to three orders too wide for e+ e- scattering. The
candidate was declined as the electron on the author's word and kept as a mechanism. The study's open items after
this: (i) is now a registered bound on the medium (charge must be sourced on a line, or carried two orders finer);
C1 is closed in the negative on the ledger; C2 is closed (no lepton spectrum from one lock); chirality untouched.

