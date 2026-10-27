# Road 1: is the charge's electromagnetic source the rope's centreline? A dictionary reading (executor, 2026-10-27)

Check: `benchmarks/foundations/road1_check.py`, log `analysis/ROAD1_check.log`. The question left by FND-189 and the
answer the registered dictionary gives, by quotation.

## 1. The quotations
EM-015 (Derived): "winding number is TOPOLOGY, a boundary condition on the braid-phase configuration space, not a
term in the energy; there is nothing to couple. For constraint sources the energy is purely (K / 2)|grad Phi|^2 on
the constrained minimizer ... winding is a CONSTRAINT source (topology imposed as boundary condition), not a
COUPLING source."
GRV-020 as identified by ELEC-089: "this claim's internal azimuth, the angular orientation of the strand pair about
their common centreline, the single circle-valued Goldstone, is the mechanical degree of freedom whose winding is
the charge."
EM-016 / EM-017: charge q = winding (GG-006); E = the gradient of the twist-tension channel plus the orientation-
transport rate; the dictionary is forced pointwise by the force on test windings, unique up to gauge and one scale.

## 2. What they say about size
A constraint source has no density. Outside the rope the braid phase is a harmonic function with winding 1 about
the line where the azimuth is defined, and that line is the pair's COMMON CENTRELINE by GRV-020's definition. A
harmonic function of winding 1 outside any compact core is theta + const + sum_{m >= 1} c_m (rho / r)^m sin(m theta
+ alpha_m): its isotropic part is EXACTLY theta, with no radial correction of any order (a winding has no "monopole
size"); every size-dependent term is anisotropic and carries the core's instantaneous orientation. Along a 2 pi
kink that orientation sweeps the full circle with the charge density dPhi / ds as the weight, so every anisotropic
term averages to zero (int e^{i m Phi} dPhi = 0, m >= 1). The check confirms the arithmetic: even in the worst
reading, half a winding on each strand, the exterior FIELD averaged over the pair's orientation equals the
point-winding field to 2e-15 at every radius outside the strands (the mean-value property of harmonic functions).
The two readings differ only INSIDE the pair, and the registered definition has no split: the singular line is
the centreline, so the field is theta all the way in.

## 3. What T-3 did wrong
T-3 scored the kink's charge as a COUPLING source: point charges at the strands' positions, azimuthally averaged
into a ring of radius rho, with the Born form factor J0(q rho) of that ring. That model contradicts EM-015 on its
face. For the registered constraint source on the centreline the transverse form factor is 1 at every q; the
charge's only structure is along the rope, F_par = sech(pi q l / 2), the Compton-length spread at the Darwin order
that T-3 (a) found and QED already has. The transverse bound FND-189 registered applies to the strands' STRESS
field (the conditioning channel of GRV-005, the mass, gravitational-class), which no e+ e- experiment measures;
it does not apply to the charge.

## 4. Consequences, each a rider on the author's word
- FND-189: a rider narrowing the bound to the stress channel ("a strand-borne charge's EM form factor is F_par
  alone; the transverse bound is on the mass form factor"), with this reading as its source. The claim's
  general sentence ("no object whose charge sits on strands at a is pointlike") is withdrawn for the charge and
  kept for the mass.
- SWEEP (analysis/GRANT_CANDIDATE_SWEEP_price_sheet.md): the T-3 kill of B2 is LIFTED. B2 still owes what T-2
  found (no spin by the belt on the charged state; two unbound half-kinks under a pi-periodic lock), and the
  stiffness identity (section 5 below) still binds. The decision line is re-opened to that extent.
- The ring-wave and the pair: no longer excluded by size on the charge side.

## 5. What this does NOT change
The identity kappa = T0 sum rho^2 with T0 / a^2 the vacuum energy density: an object whose SPIN is the twist of a
bundle has rho about 3e-16 m at any substructure level. Road 1 makes that radius invisible to e+ e- scattering
(it is a mass radius, not a charge radius), so the identity no longer kills on the pointlike bound. It still
says the spinning bundle is a 3e-16 m object by mass, which the registry has no observation against. Road 3
(spin as the belt-trick quantum number, not twist) is no longer forced by Road 1's failure; it is one of two
readings of the spin, and T-2's ledger (SL = 2 on the double-cover state) is the obstacle on the other.

## 6. Status
A reading, not a claim. The author's word is needed for the FND-189 rider and the SWEEP decision line; the
executor recommends both, and records that T-3's error was his: the coupling-source model was the natural
scattering picture and the wrong one for this dictionary, and the dictionary said so in a Derived claim two
months old.
