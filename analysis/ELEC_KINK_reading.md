# The twist kink as an electron candidate: what the registry already holds, and where it lands (executor reading, 2026-10-27)

Instrument: `benchmarks/foundations/elec_kink_reading.py` (closed forms; log `analysis/elec_kink_reading.log`).
Written before any charter, because the kink turned out to be on the registry already and its numbers follow
from registered identities; a charter that "computed" them would be refused as a preview, rightly.

## 1. The kink is the registered winding
The thought experiment of 2026-10-27 named the sine-Gordon twist kink (Skyrme 1961; Coleman 1975: the classical kink
is the massive Thirring fermion) as the candidate with a theorem behind it. The registry holds it under another
name: a WINDING on a strand is a 2 pi kink of the orientation angle. FND-STRAND-002 transported it (the stadium wave,
winding conserved exactly); FND-181 gave it a force law; FND-182 priced a charge-creation field on its width w; the
on-site orientation potential V_0 that makes it a kink rather than a free rotation is closure gap 2 (FND-186),
sourced by the surface-contact grant (FND-184), and unpriced because STRAND-MASS-SCALE refused for want of A_c in
joules, sigma in metres and the crossing density. The chain identities are on the record (STRAND-MASS-SCALE
results): per node kt = T0 r^2 / 2a (rod route), w^2 = kt / V_0, with the registered COASTING regime w in [0.8, 2.8]
(a winding that carries charge must move freely; FND-STRAND-002 / FND-KIN-002).

## 2. Where it lands (card, M-point; the soliton's closed forms)
A sine-Gordon kink with stiffness kappa and well V has E = 8 sqrt(kappa V) = 8 kt / w per node, gap omega = c / (w a),
and action E / omega = 8 kappa / c with nothing free (the soliton constraint of the thought experiment, met).
    object             coasting w     V_0 per node       kink rest energy            E / omega
    single strand      0.8 to 2.8     0.3 to 0.025 eV    2.0 to 0.56 eV (1e-6 m_e)   hbar / 2.1e9
    two-strand pair    0.8 to 2.8     9.2 to 0.75 keV    59 to 17 keV (0.12 to 0.03 m_e)   hbar / 7.0e4
A kink of electron mass on the pair needs w = 0.09 a and V_0 = 690 keV per node (f = V_0 / (T0 a / 2) = 8.5): pinned
by the lattice, outside the coasting regime by a factor 9 in w. On a bundle of n strands at the pair's packing
(kappa scaling as (n / 2)^2), a coasting kink weighs m_e at n = 6 to 11, and its action is hbar / 8e3 to hbar / 2e3,
inside ACTION-BRIDGE's F-LOR band and short by the same factor as every other twist soliton.

## 3. Reading
The kink meets the structural constraints the ring does not (pointlike core: w a = 1e-17 m; topological charge;
no free amplitude; a gap), and it lands exactly where the ring landed: a rest energy of order T0 a (near m_e by the
M-point calibration, FND-MATTER-044, not by prediction) and an action of order kappa / c, short of hbar by 1e3 to 1e5
depending on the strand count. The candidate's form does not touch the wall; kappa / (hbar c) does. Two things the
kink route DOES change: (i) the mass is a count of strands in a bundle rather than a tension rung, so it is not
excluded by N1's ladder argument; (ii) its one unpriced input, V_0, is the same gap 2 that FND-182's charge-creation
field (a live discriminator against the laser record and Schwinger) waits on. That is the computation with an
unknown outcome: not the kink's mass, which the chain fixes once V_0 is known, but V_0 itself, which decides whether
the registered winding coasts (f small, a keV kink, charge that moves) or is pinned (f of order 1, a sub-lattice
kink, charge that does not). The charter for that is drafted beside this reading (CROSSING-PRICE-1).

## 4. Closed by the record (2026-10-27, after the lab's withdrawal of CROSSING-PRICE-1)
The worker's withdrawal, which I concede in full, settles the kink route on the registry as it stands:
- At the registered level f = 0 identically (JUNCTION-LOCK, verdict JUNCTION-FREE): the registered vacuum has NO
  on-site orientation potential, so the registered winding is a free rotor, not a kink. Section 2's coasting-regime
  rows describe a hypothetical well, not the registered one.
- The only other registered reading is the face-to-face tie at f about 3.5 (the first of the Director's two grants);
  under it every kink is PINNED by three orders (w of order 1e-3 a; CROSSING-PRICE: w = 0.003 at touching), so the
  charge carrier could not move. A coasting kink needs a span of 1e4 to 1e5 spacings that nothing registers.
So the kink candidate is closed: with the registered contact there is no kink; with the tie grant there is a kink
that cannot move; and in either case its action is kappa / c, the same wall. CROSSING-PRICE-1 is parked with the
five reasons (analysis/queue/parked/README.md). What survives of the thought experiment's four candidates on the
registry: the double-cover ring (RING-WAVE-STABILITY-2, FRAMED-EXCHANGE) and the screened vortex (needs a gapped
twist mode, which the registered Goldstone is not). The executor's error, named: I drafted against the state of the
registry as of FND-184 and did not read JUNCTION-LOCK and NODE-STANDOFF, which had already answered the question.
