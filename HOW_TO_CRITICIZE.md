# How to Criticize the Mesh Programme

This document exists because a programme that means its commitment to falsifiability
should tell critics exactly where to aim. It is written to make rigorous criticism
*easier*, not to preempt it.

## Where to look first (highest leverage)

1. **The load-bearing derivations.** Two theorems carry disproportionate weight:
   - the Gamma-convergence / homogenization result (FND-003/004), from which EM,
     thermodynamics, and condensed matter descend;
   - the gravity metric-order no-go (GRV-008 through GRV-020), on which the entire
     adverse gravity verdict rests.
   If either is wrong, a whole sector moves. These are the first targets, and they are
   the two slated for Lean formalization precisely so the algebra can be checked, not trusted.

2. **The single calibrated constants.** Several sectors rest on one fitted number:
   the nuclear mass predictor (NUC-005, one constant, C-12..U-238), the field-strain
   calibration SIGMA (EM-RECON-014). Attack the claim that ONE constant does the work --
   look for hidden second parameters.

3. **The adopted-vs-derived seams.** Wherever an equation is adopted (the Schrodinger
   form in chemistry; the electronegativity charge map; hybridization mixing), the
   "derivation" downstream inherits whatever that adoption smuggles in. These seams are
   labeled; test whether the label is honest.

## Results produced by the Mesh Lab

Since October 2026 many commissions are run by an autonomous lab: AI agents propose, draft and
review charters, and the lab locks, runs and scores them on a separate `lab` branch, which the
author promotes to `main` by merge. Its claims enter the registry as Provisional until then. Check
that each charter was locked before its data, that the verdict follows mechanically from the locked
scoring script, which amendments were made after data existed, and whether the second review came
from outside the Claude model family (the promotion pull request lists any that did not). The full
procedure and its safeguards: [`docs/MESH_LAB_GUIDE.md`](docs/MESH_LAB_GUIDE.md).

## Which assumptions are load-bearing

- **Volume-conserving strands** (P-VOL) -- underlies the mechanical core.
- **The mesh scale as an irreducible input** -- the atomic-scale derivation is blocked here.
- **Preferred-frame (Lorentz-Poincare) relativity** -- transverse-only Lorentz invariance
  is emergent, not fundamental; a genuine test of isotropy stresses this.
- **Configuration counting** -- the choice that makes the model classical, and the reason
  entanglement is out of reach. This is THE load-bearing ontological commitment.

## What would falsify each sector

- **EM/optics:** the PVLAS-class birefringence discriminator -- rope predicts a 3:1
  negative-index shift where QED predicts 7:4 positive. A measurement in the window kills one.
- **Gravity:** already falsified classically; the quantum-completion conjecture (GRV-014)
  falls if its induced action does not produce the factor-of-4 correction.
- **Chemistry:** the heavy-hydride angles must approach 90 from ABOVE, never below
  (CHEM-GEO-002); a single sub-90-degree hydride (H2Po predicted 90.0-90.7) falsifies the
  phase-blocking mechanism. The metallic Na-vs-Cl2 discrimination must hold.
- **Nuclear:** the SEMF surface/volume ratio and shell structure must emerge together from
  the mode-capacity rebuild (NUC-006 next-order); if quantized bonds don't fix both, the
  bundle-contact picture is incomplete.

## Which benchmark failures would collapse entire sections

- If `verify_corpus.py` fails on the Gamma-convergence benchmarks -> EM, thermo, condensed
  matter lose their derived status simultaneously.
- If the Yukawa-from-overlap benchmark (NUC-004) fails -> the entire nuclear AND chemical
  bonding account (shared mechanism) is undermined at once.
- If the electrostatic-sign theorem (EM-015) is wrong -> ionic bonding, hydrogen bonding,
  and the Coulomb sign all fall together.

## Which derivations depend on adopted equations (trust-transitively)

- Everything in chemistry that uses absolute energies inherits the adopted Schrodinger
  scale -- these are "consistency-tier," not independent predictions.
- The hydrogen-bond and reaction-dynamics energies inherit the adopted electronegativity
  charge map, which the F/O miss identified as the sector's load-bearing flaw.

## The fastest disproof

If you can show that any ONE claim labeled "Derived" actually requires a hidden fitted
parameter, or that any "parameter-free" prediction was tuned post-hoc, you will have found
the failure mode the entire methodology is built to prevent -- and the registered
correction history (three refused rescues; four disclosed operator errors) is where to
check whether we have caught ourselves before.
