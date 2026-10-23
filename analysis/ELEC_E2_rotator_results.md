# ELEC E2: the rotating charge-one pair, instrument and first march (executor, sandbox, 2026-10-23)

Status: exploratory record (no commission, no verdict). Instrument: `benchmarks/foundations/elec_rotator.py`
(queue 1e87ce5 and after). Records: `analysis/elec_rotator_control.log`, `analysis/elec_rotator_march_chain1.{log,json}`,
`analysis/elec_rotator_march_multiseed.{log,json}`. Everything below is in the instrument's dimensionless units
(T0 = 1, c = 1, lengths in units of the Hopf base radius at the first rung); nothing physical is scored here.
This note exists so that E3 is charted on what the instrument actually does, not on what section 6 of the
ledger hoped it would do.

## 1. What the instrument is

Two closed curves (ELEC-020's Hopf base circles plus K = 8 Fourier modes each, 194 shape parameters) in rigid
rotation at angular speed Omega about z. Energy E = T0 int gamma ds with gamma from the transverse velocity
v_perp = v - (v . t) t, the Nambu-Goto string in rigid rotation; angular momentum J = T0 int gamma (p x v_perp)_z ds;
Coulomb energy of the erf-smeared uniform line charge at kappa = alpha pi (the ledger's section 6 strength);
a hard-core penalty keeping strands D_HARD = 0.06 apart (ELEC-020's regulator, carried over). E is minimized over
the shape at FIXED J, with Omega eliminated by a root find on J(z, Omega) = J_target at every evaluation, and the
rest frame enforced (the rotation axis through the centre of energy, P = T0 int gamma v_perp ds = 0).

## 2. The control, and the two loopholes it exposed

A single loop, no Coulomb, no hard core, from a flat-ellipse seed, must reproduce the folded rotating string:
E = 2 pi T0 R, J = pi T0 R^2, 2 J / E = R, <r^2>_charge = R^2 / 3, g = 2/3 for a uniform line charge, and the
closed-string Regge bound 4 pi T0 J / E^2 <= 1.

  R = 1: E +1.2 percent, 2J/E = 0.983, <r^2>/R^2 = 0.403, Regge ratio 0.971, cm speed 1e-5, J 0.5 percent under
         target at the speed wall.
  R = 2: E +0.27 percent, 2J/E = 1.974, <r^2>/R^2 = 0.355, Regge ratio 0.984, cm speed 4e-6, J 1.0 percent under.

Before this passed, the instrument found two states that no rotating string can have, and both are standing
warnings for any rotator number from any instrument:
  (a) Node tangents from central differences are meaningless at a cusp. With them the exact-constraint solver
      found loops 20 percent BELOW the fold's energy at the same J (Regge ratio 1.66). Fixed by segment tangents
      with sub-segment gamma integrals; the Regge ratio is printed on every line and must be <= 1.
  (b) Without the momentum constraint the minimizer finds the lopsided hairpin: one tip lightlike at 1 / Omega,
      the other end on the axis, E = pi T0 R and J = pi T0 R^2 / 2, "half the fold's energy for half its J",
      except that its J is the orbital angular momentum of a centre of energy moving at 0.6 c. Fixed by enforcing
      P = 0; the cm speed is printed on every line.
Also recorded: a near-circle seed finds a second stationary branch (a ring rotating about a diameter) 19 to 34
percent above the fold at the same J; the landscape has several rotating branches, and every rung of the pair
march is therefore solved from four seeds (the previous rung's shape, flat, round, tilted) with the lowest E kept.

## 3. The pair march (Hopf-linked pair, kappa = alpha pi, D_HARD = 0.06, M = 48, best over all seeds and chains)

  J     E        E^2/(4 pi T0 J)  2J/E    R_end   R_end/(2J/E)  R_rms(q)/(2J/E)  edge    E_C/E   g_perp  |Lk|   min_sep
  0.5   2.822    1.268            0.354   0.407   1.15          (chain 1)        0.969   0.0084  0.70    0.97   (chain 1)
  1.0   3.875    1.195            0.515   0.565   1.10          0.58             0.990   0.0057  0.68    0.95   on the core
  2.0   5.522    1.204            0.724   0.740   1.02          0.57             0.999   0.0036  0.64    0.97   0.0615
  4.0   7.430    1.100            1.070   1.074   1.00          0.57             1.000   0.0023  0.64    0.96   0.0576
  8.0   10.338   1.063            1.548   1.566   1.01          0.58             1.000   0.0014  0.66    0.98   0.0573

(J = 1 is chain 1's state, 3.875, which the multi-seed run did not revisit; the multi-seed best at J = 1 from
fresh seeds was 4.024. Seeds at one rung spread by 2 to 7 percent in E; the round seed lands high at every rung.)

## 4. What the march says

F1. The rotating linked pair exists as a stationary state at every J tried, and it is a Regge rotator: E^2
    proportional to J with E^2 / (4 pi T0 J) falling from 1.27 to 1.06 as J grows, i.e. the pair approaches the
    single folded string's trajectory from above. R_end = 2 J / E holds to 1 to 2 percent from J = 2 up (the
    rotator identity of ledger section 6, now shown on the pair rather than assumed). Edge speed reaches c from
    J = 2 up. The two curves do not stay a round clasp: the lowest-energy shapes are fold-like, length
    proportional to sqrt(J), with the second curve riding along the first.

F2. EVERY lowest-energy state sits on the hard core. The closest approach between the two curves is 0.057 to
    0.062 against D_HARD = 0.06 at every J; the Gauss linking number smears to 0.95 to 0.98 because the strands
    touch; seeds that slipped through the core during the optimization ended unlinked (J = 1, E 3.886 against
    3.875 linked) or relinked with the opposite sign (J = 4, J = 8) at the same energy to 1 percent. Tension plus
    rotation drive the clasp toward strand crossing, and the only thing holding it in the instrument is a
    regulator that is not registered mesh physics. Consequence: E(J), R(J) and everything downstream of them
    depend on D_HARD at a level still to be measured (a D_HARD scan at J = 2 is running; its result is appended
    below when it lands). Until the medium's contact rule is registered (what two strands do when they meet:
    repel at a core radius set by the strand thickness, or reconnect), the rotating pair has no size of its own.

F3. The Coulomb fraction is 0.1 to 0.8 percent and falls as 1 / R, as it must for a fixed kappa / T0. In
    physical terms A5 is scored at the physical R (Compton scale under H), where the fraction is alpha times a
    geometry factor; the instrument cannot score it until the scale is fixed by A7, and it has nothing to say
    about A5 beyond "small", which is what H needs.

F4. g for the registered charge is 2/3, not 2. The instrument assigns the charge uniformly along the strand
    length (the winding is transported along the whole strand, EM-008 / EM-014, so this is the registered reading,
    not a choice), and for a uniform line charge on a rotating fold g = (mu / J)(2 E / q) = 2/3 exactly; the pair
    gives 0.64 to 0.70. Ledger section 6 obtained g = 2 by putting the charge AT the lightlike end. That is not
    what the registered winding does. So H as stated has a hole exactly where it claimed its cleanest result:
    g = 2 needs the charge-bearing winding concentrated at the edge, and nothing in the registry puts it there.
    The same uniform charge gives R_rms(charge) / (2 J / E) = 0.58 (the fold's 1 / sqrt 3), so A3 as worded
    (R_rms(charge) within 10 percent of 2 c J / E) fails by construction for a uniform winding even on the
    ideal fold; A3's wording presumed the edge-located charge too. Both A3 and A4 must be re-worded against the
    registered charge locus before E3, or the charge locus must be registered first.

F5. Not tested: A2's linear stability (no Hessian; the solver finds minima at fixed J but the stability of the
    pair against unlinking is exactly F2's regulator question), A7 (the tension, which needs the physical scale),
    A9 (E4). A1 holds by construction (the pair is linked; |Lk| 0.95 to 0.98 is contact smearing, and the
    relinked seeds show the core is crossable in the optimizer).

## 5. The registry check (same day), which supersedes the reading above

Before registering anything for F2 or F4, the registry was read for what it already says about strands meeting
and about where charge sits. It answers F2 and reframes F4:
  - The charge-carrying link is the linking of the two strands OF ONE ROPE (GG-006: charge = the two strands'
    handedness = their linking number; GRV-020: the winding of the rope's internal twist phase Phi(s) around the
    closed loop, pi_1(S^1) = Z). ELEC-001's "unit-linked Hopf configurations" are the two strand curves of one
    rope, linked once; so are this instrument's two curves.
  - Ropes interpenetrate OTHER ropes freely below the coverage threshold (FND-MATTER-004, magnetism paper 2.1;
    load-bearing in the gravity audit, GRV-013). But the two strands of one rope are BOUND: their separation is
    gapped (GRV-020, "Branch-A logic"), with a registered standoff d0 (EM-RECON-017/018, d0 / sigma0 in
    [0.40, 0.46]). Linking conservation and interpenetrability are statements about different pairs of strands,
    and both stand.
  So Q1 needs no registration: the two strands of the rope ride at the registered standoff, held by a restoring
  potential; they neither cross nor collide as tubes. The instrument's free loops with a hard core are the wrong
  object: what it found at the core (two loops hooked at one point, each stretched into an arm of the fold, a
  two-link chain) is a configuration the bound rope cannot take, and the D_HARD dependence is the dependence of
  a non-registered object on its regulator. The scan confirms the point from the other side: at D_HARD = 0.03 the
  chain seed crossed and unlinked (Lk -0.09), leaving no linked state at all; see section 6.
  The rotating electron candidate under H is therefore ONE closed rope with one unit of twist, folded and
  rotating: the control object of section 2 with an internal twist field. E2 is rebuilt on that (E2b), not
  patched.

  For F4 the registry supplies the density to derive from: the local charge density along the rope is the twist
  density dPhi/ds / 2 pi (the registry defines the integral; reading it locally is the one decision here, and it
  is the natural one since the Coulomb source must be local). The twist is the Goldstone with energy
  (kappa / 2)(dPhi/ds)^2 (GRV-020), and on a rotating rope each element's internal energy carries the gamma of
  its motion, so minimizing the twist energy at fixed total winding gives Phi' proportional to 1 / gamma: the
  twist is pushed AWAY from the lightlike folds toward the slow centre. On the fold, with x = r / R weighted by
  the charge density, g = 2 <x^2>:
      density proportional to 1 / gamma (twist minimizing its energy):  <x^2> = 1/4,  g = 1/2
      uniform (this instrument as built):                               <x^2> = 1/3,  g = 2/3
      proportional to gamma (following the energy density):             <x^2> = 1/2,  g = 1
      at the lightlike edge (ledger section 6's assumption):            <x^2> = 1,    g = 2
  The registered reading, carried through, predicts g = 1/2; the only route to 2 is a mechanism that pins the
  winding to the edge, which nothing in the registry supplies. E2b computes this properly (shape and twist
  distribution minimized together at fixed J and fixed winding, g from the twist-density current). If it
  confirms 1/2, H dies at R4 with a number attached: the Dirac g = 2 is not available to a rotating twisted rope
  with the registered twist energy, and the electron sector needs a different carrier of charge or a different
  object. That is a result, not a setback; it is the first electron number the registry's own mechanics would
  have produced.

## 6. D_HARD scan at J = 2 (the free-loop instrument's regulator dependence; a footnote after section 5)

  D_HARD 0.03: the chain seed crossed the core and unlinked (Lk -0.09, E 5.43); no linked state survived.
  D_HARD 0.06: E 5.522 (section 3).
  D_HARD 0.12: (appended when it lands)
