# COMMISSION CURRENT-AS-SPIN -- WHAT MAKES A CONDUCTION ROPE SPIN RATHER THAN VIBRATE?
# (CHARTER, LOCKED 2026-09-27 on the author's word ("lock CURRENT-AS-SPIN"), before any number was computed)

North Star line (docs/NORTH_STAR.md section 5): this charter serves the target row
"Strength of magnets" at its mechanism step. It computes no magnet and no number against
a measurement; the electron model still blocks that. What it can move is the row's
"nearest registered step": whether conduction current IS azimuthal rotation of the wound
strand at a rate derivable from registered constants, and why that rotation does not
leak away as vibration does. Outcome class: structural (DERIVED-RATE or a named missing
input), entered on the scorecard as such.

## The question (the author's, 2026-08-16, STRATEGIC_TARGETS section E item 4)

Two halves, both answered from registered structure with bars locked before computing:

  (a) TORQUE INJECTION. Does an EMF-class longitudinal strain gradient on a WOUND strand
      force azimuthal rotation through the registered twist-stretch lock (EM-RECON-012,
      Derived) at a derivable rate? The torque-balance allocation steady EMF -> steady
      rotation rate is currently UNREGISTERED as a quantitative statement.
  (b) SPIN PERSISTENCE. Quantify the asymmetry already exact in structure: transverse
      vibration leaks at every crossing through the O(g) machinery, while azimuth escapes
      only via the lock chain (dV/dphi = 0 identically, EM-RECON-023), so the azimuthal
      reservoir is the low-loss channel and current survives as spin.

## Registered parts list (complete per the 2026-08-16 entry; reads owed at lock marked [R])

  The winding-is-charge identification (GG-006 lineage, Derived: handedness is the linking
    number; EM-RECON-026: circulation count = winding number, the q-linear force).
  The lock, Derived (EM-RECON-012): strand-length conservation under rope strain gives
    delta_tau = -gamma tau_0 eps with gamma = 1/sin^2(theta) exactly; gradient-order, no
    gap. [R] which angle theta is the registered one on the level-1 wound carrier (the
    FND-088 magic angle, sin^2 psi_1 = 1/3, would give gamma = 3).
  The exact azimuth-blindness (EM-RECON-023): the contact form depends on centre-line
    separation only, dV/dphi = 0 identically; twist reaches crossings only through the
    lock's higher-order-in-g chain; stiffness matrix [[lambda, c_L], [c_L, k_s]] entrywise
    q-independent (both branches omega = c_i q exactly). [R] the order in g of the chain.
  The O(g) crossing coupling of the transverse displacement (FND-REL-005; EM-RECON-022
    item 1: the displacement mode acquires an O(g) mass from crossing stiffness). [R] the
    registered value or bracket of g.
  Torsional stiffness and the priced torsion speed (FND-MATTER-047: v_t/c = 1/sqrt5 from
    the registered C; FND-131: C = kb/(1 + nu) = 0.8 kb at the fine level). [R] which C
    applies to the coarse conduction strand.
  The EMF-strain reading: the scalar potential's mechanical channel is the longitudinal
    tension channel (EM-018, Derived by elimination); an EMF is a longitudinal strain
    gradient along the strand. [R] the claim that fixes the normalization strain <-> volt.
  Adjacency disclosed in advance (as the 2026-08-16 entry requires): this parts list is
    the twist-to-carrier vertex session's (GRV-118, three enumerated obligations). The two
    compute a lock-mediated conversion rate from the same three objects; this commission
    runs FIRST and GRV-118's session inherits its bars.

## Pre-commitments (from the 2026-08-16 entry, verbatim in substance)

  No new coupling registered. The drive is the registered EMF-strain reading only. Every
  constant that enters is a registered constant or is NAMED as the missing input. The
  three admissible outcomes are fixed below; "the mechanism is interesting" is not one.

## Protocol (sandbox; derivation plus small exact computations)

PART A (torque injection). On the coupled screw-stretch sector of EM-RECON-023, with the
  lock as the only twist-stretch coupling, impose a steady longitudinal strain gradient
  (the EMF reading) along a wound strand of length L and solve the torque balance:
  A1. the steady state of the azimuth phi(s, t) under the drive; whether it is a steady
      ROTATION (phi = Omega t + ...) or a static TWIST (phi = f(s), Omega = 0);
  A2. if rotation: Omega as a closed form in the registered constants (lambda, k_s, c_L,
      gamma, the drive strain), with every constant cited; if the closed form needs an
      unregistered quantity (a crossing friction, a boundary condition at the strand's
      ends, a material rate), that quantity is NAMED and the outcome is
      RATE-UNDERDETERMINED, not a fitted number;
  A3. a numeric control: a chain of N sites with the registered stiffness matrix, driven
      at the ends, integrated to steady state; the closed form must reproduce it to 1e-6
      relative, or the closed form is wrong.
PART B (spin persistence). On the same chain with crossings:
  B1. the leak rate of transverse displacement energy through the O(g) crossing coupling,
      as a function of g (expected O(g^1) in the rate at leading order);
  B2. the leak rate of azimuthal (twist) energy, reachable only through the lock chain
      (expected O(g^n), n >= 2, per EM-RECON-023's "higher-order-in-g chain"); the
      commission COMPUTES n and the prefactor;
  B3. the asymmetry stated as an order and a prefactor, not adjectives: leak_transverse /
      leak_azimuth = A g^-(n-1), with A and n from the computation.
PART C (accounting). The tier verdict by the census rule (a structural result shared with
  no standard alternative is not a discriminator until it produces an observable); the
  scorecard row updated; GRV-118's session told what it inherits.

## Bars (LOCKED before any computation)

B-A1  The steady state is classified by the computation, not read into it: ROTATION iff
      d phi/dt averaged over the strand is nonzero and constant to 1e-6 relative over the
      last half of the integration at the registered drive; otherwise TWIST.
B-A2  DERIVED-RATE requires a closed form with zero unregistered inputs that reproduces
      the numeric control to 1e-6 relative at three drive strengths spanning a decade and
      at two strand lengths. One unregistered input, named, is RATE-UNDERDETERMINED.
B-B   The orders in g are read from a fit over at least a decade in g at small g; the
      asymmetry form is accepted only if n is an integer to 0.05 and the prefactor is
      stable to 10 percent across the decade. Otherwise the asymmetry is reported as the
      raw ratio table with no form.
B-C   No constant is tuned; the drive strain is swept, never chosen to make a rate land.

## Verdict forms (LOCKED)

DERIVED-RATE:         steady rotation at Omega = closed form in registered constants,
                      numeric control met. The mechanism half of "current is spin" is
                      registered; the scorecard row's nearest step advances to the
                      electron model.
RATE-UNDERDETERMINED: rotation exists but Omega needs one named unregistered input. The
                      input is the finding; the row's nearest step becomes that input.
TWIST-NOT-SPIN:       the registered lock produces a static twist under steady EMF, no
                      rotation. The author's reading "current is spin" is NOT supported
                      at the registered couplings; kept as a failure; the row's nearest
                      step becomes "a coupling that converts strain gradient to rotation,
                      priced as a grant".
ASYMMETRY (always):   the (n, A) of Part B, registered whichever form above fires; an n
                      of 1 (no asymmetry) is a second kept failure.
REFUSED:              the numeric control does not converge or the closed form cannot be
                      checked; stop.

## Rules

No rescue; the bars are the bars; one verdict computed once from sealed outputs
(analysis/current_as_spin_*.npz); failures kept; no new coupling; no tuned constant;
adjacency with GRV-118 disclosed and honoured (this runs first); riders and grants are
the author's act.

## Reads owed at lock (a title is not a verdict)

EM-RECON-012 (the lock's form and its theta); EM-RECON-023 (the stiffness matrix entries
and the order in g of the twist-to-crossing chain); FND-REL-005 and EM-RECON-022 (the O(g)
crossing mass); FND-MATTER-047 and FND-131 (which torsional C applies); EM-018 and the
claim that normalizes strain to volts; GRV-118 (its three obligations, so the inheritance
is stated correctly); FND-088 (the angle).

## Cost and machines

Sandbox only: derivations one session; the chain controls minutes. Neither compute
machine is touched.

## Author's lock

Locked on the author's word on 2026-09-27. No computation ran before this line was written.

## READS AT LOCK (executed 2026-09-27 before any computation)

1. EM-RECON-012: SAYS WHAT IS ATTRIBUTED. delta_tau = -gamma tau_0 eps, gamma =
   1 + 1/(r tau_0)^2 = 1/sin^2(theta) exactly, theta the TWO-STRAND twining angle
   ("~2-4 for moderate twining"); gradient-order; u is gauge (no material points), so
   no mass term. Note: theta is the rope's twining angle, not FND-088's level-1 fibre
   angle; the commission carries gamma symbolically and its result below does not
   depend on its value.
2. EM-RECON-023: SAYS WHAT IS ATTRIBUTED. Stiffness matrix [[lambda, c_L], [c_L, k_s]]
   entrywise q-independent; dV/dphi = 0 identically for the registered contact form
   (centre-line separation only). "Higher-order-in-g chain" is the claim's PHRASE; GRV-118
   records at full volume that NO ORDER WAS COMPUTED. Part B must compute or say why not.
3. FND-REL-005 and EM-RECON-022: SAY WHAT IS ATTRIBUTED. The transverse displacement mode
   acquires an O(g) mass from crossing stiffness; the exact transfer relation
   cos(qa) = cos(ka) + (g/2ka) sin(ka) for point pinnings of contrast g is the registered
   crossing model for displacement. Correction to the 2026-08-16 parts list: the O(g)
   crossing coupling of DISPLACEMENT is FND-REL-005; EM-RECON-026 is the q-linear
   collective (momentum-flux) coupling of a winding to the moving medium. Both stand;
   they are different objects and Part B keeps them apart.
4. FND-MATTER-047 and FND-131: v_t/c = 1/sqrt5 from the registered torsional C at the
   coarse level (047); C = 0.8 kb at the fine level (131). Part A's result is independent
   of the numerical value; the chain control uses 047's ratio.
5. EM-018: SAYS WHAT IS ATTRIBUTED. phi's channel is the longitudinal tension channel by
   elimination; an EMF is a longitudinal strain gradient. The strain-to-volt normalization
   is EM-RECON-027 (kappa_0 = c/sqrt(eps0 Sigma)); Part A's result does not need it.
6. GRV-118: SAYS WHAT IS ATTRIBUTED. Obligations (1) emission from time-varying tau,
   (2) lock conversion efficiency, (3) crossing transfer rate at the registered coupling,
   enumerated and not owed; "no order computed". Inheritance stated in Part C.
7. FND-088: the angles psi_1 = 35.2644 deg, psi_2 = 59.4444 deg; not consumed by Part A.

Outcome: one parts-list correction (item 3), no bar moved, no form changed. Computation
may begin.
