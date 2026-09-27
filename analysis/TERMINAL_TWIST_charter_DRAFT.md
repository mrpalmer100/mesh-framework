# COMMISSION TERMINAL-TWIST -- WHAT KIND OF TERMINAL MAKES CURRENT SPIN?
# (CHARTER, DRAFT 2026-09-27; becomes LOCKED on the author's word, before any number is computed)

North Star line (docs/NORTH_STAR.md section 5): serves the target row "Strength of magnets"
at the step FND-179 named. FND-179 proved that at the registered couplings a steady EMF
cannot spin a strand from the bulk: the torque on the azimuth is the derivative of the twist
flux J, so a steady rotation needs TERMINALS that act as source and sink of twist flux. This
commission asks whether the registry already holds such a terminal, or whether it is a new
primitive to be priced. Outcome class: structural; it either retires a "missing primitive" by
identifying it with a registered object, or prices the grant.

## The question

What registered object can inject a steady twist flux J into a strand's azimuth at one end of
a conductor and remove it at the other, so that the azimuth rotates at a steady rate, and does
the rate it injects equal the current?

## The candidate, stated before computing (so the answer cannot be retro-fitted)

The registry holds three facts that together make one candidate:
  (i)  Charge is winding (GG-006, Derived; EM-RECON-026: circulation count = winding number).
  (ii) A reconnection (punch-through) exchanges EXACTLY ONE 2 pi quantum of frame winding
       between the two strands, length-independent, continuous, no break (GRV-045, Derived,
       measured 1.007 x 2 pi); total topological charge is conserved by it (FND-010, Derived).
  (iii) Twist is exactly conserved and can only be transported, never created or decayed
       locally (GRV-061; FND-STRAND-002 transport at error 0.0), and reconnection is
       ONE-WAY, the through-branch absorbing (GRV-037).
CANDIDATE T-RECON: a terminal is a RECONNECTION SITE with a supply. Each reconnection hands
one 2 pi of frame winding from an arriving strand (the electrode side) to the conductor
strand; a steady rate R of reconnections injects twist flux J = R x (angular momentum per
2 pi quantum) into the conductor's azimuth, and the conductor rotates at d(Phi)/dt = 2 pi R
at the terminal. Since a winding IS a charge, R is the current in winding units: current =
phase advance rate, exactly. The far terminal is the same object run in reverse (the
conductor's windings handed off), which is a SINK; the electrode strands carry the counter-
twist, so a closed circuit through the battery has zero net torque, as FND-179's theorem
requires. Because reconnection is one-way (GRV-037), a steady R needs a steady SUPPLY of
fresh crossings: arriving strands (the electrolyte's ropes, or the other conductor's) rather
than a fixed crossing that flips once. That supply is the battery's chemistry in mesh terms.

The candidate is a reading of registered objects. The commission does not assume it holds;
it tests three things that could break it.

## What is tested

T1 (the quantum). Does a punch-through hand its 2 pi of FRAME winding into the AZIMUTH
   field Phi of EM-RECON-023's screw sector (the field FND-179's J is built from), or into a
   different winding bookkeeping (material winding, GRV-045's "extensive" count)? GRV-045
   distinguishes frame winding (the exchanged quantum) from material winding (the extensive
   charge sign). The screw field Phi is the frame azimuth. The test: on the registered
   crossing engine (GRV-045's instrument, benchmarks named at lock), measure the change of
   the strand's integrated Phi' (its twist, in units of 2 pi) across one punch-through. Bar:
   the change is 1.00 +/- 0.05 of 2 pi in the screw variable, or the candidate FAILS at T1.
T2 (the flux). With one reconnection per time R at s = 0 on FND-179's chain (the registered
   screw-stretch sector, torsion-free far end), does the strand reach a steady rotation
   d(Phi)/dt = 2 pi R after transients, and does the twist flux settle to J = I_T x 2 pi R
   per unit time at the terminal? (Each event is applied as a 2 pi step of Phi at the end
   site, the registered quantum, nothing else.) Bar: the strand-averaged rate over the last
   half of the run equals 2 pi R to 1 percent at three rates spanning a decade; the
   transient decays or rings without secular drift.
T3 (the sink and the circuit). Two chains joined end to end through a "battery" that
   reconnects windings from chain 2's end onto chain 1's start at rate R (source) and from
   chain 1's end onto chain 2's start (sink): does the pair reach a steady circulating
   rotation with zero total angular momentum change? Bar: total I Phi_dot summed over both
   chains constant to 1e-6 relative; each chain at 2 pi R.
T4 (the one-way constraint). Reconnection is absorbing at a fixed crossing (GRV-037). The
   commission states, from GRV-037's measured branch structure, what a steady R requires:
   a supply of arriving crossings at rate R. It does NOT model the chemistry; it names the
   demand (crossings per second per terminal for one ampere, in winding units: I/e = 6.2e18
   per second) and records it as the terminal's price.

## What is NOT assumed

No new coupling; no strain-to-rotation term; no terminal primitive beyond the registered
reconnection event and its registered quantum. The rate R is an INPUT swept over a decade,
never chosen; the chemistry that supplies crossings is named, not modelled.

## Verdict forms (LOCKED)

TERMINAL-IS-RECONNECTION:  T1, T2, T3 pass. The missing primitive FND-179 named is not new:
    it is the registered reconnection event at a supplied site. "Current is spin" is then a
    theorem chain: charge = winding (GG-006), reconnection moves one 2 pi (GRV-045), twist is
    conserved and transported (GRV-061), the bulk cannot source it (FND-179), so a steady
    current is a steady 2 pi R phase advance at the terminal and a steady rotation in the
    conductor. The magnets row's nearest step returns to the electron model. T4's supply
    demand is registered as the terminal's price.
TERMINAL-RECON-WRONG-VARIABLE: T1 fails: the 2 pi lands in a winding bookkeeping other than
    the screw azimuth. The candidate is dead as stated; the terminal remains a new primitive
    to be priced; the finding (which variable carries the quantum) is registered.
TERMINAL-RECON-NO-STEADY-STATE: T1 passes, T2 or T3 fails (the injected quanta do not
    organize into a steady rotation of the registered sector). Kept as a failure with the
    dynamics recorded.
REFUSED: the crossing engine or the chain control cannot be run to its bar.

## Rules

Bars are bars; no rescue; verdict once from sealed outputs (analysis/terminal_twist_*.npz);
failures kept; the reconnection engine used as registered; riders and grants the author's.

## Reads owed at lock

GRV-045 (which winding variable the quantum is measured in; the engine and its seed);
GRV-037 (the branch structure and the one-way measurement); GRV-061 and FND-STRAND-002 (the
transport bookkeeping); GG-006 and EM-RECON-026 (the winding = charge identification's
variable); GRV-104/105 (angular momentum = twist, beta_J = 1, the angular momentum per 2 pi
quantum); FND-179 (inherited: J, the bars).

## Cost and machines

Sandbox: T2 and T3 minutes; T1 depends on the registered crossing engine's cost (read at
lock; GRV-045's run was three-dimensional and may take hours). No Mac or PC time.

## Author's lock

Locked on the author's word on: ______ . Until then no computation runs.
