# The self-field anomaly of the travelling-twist ring: g - 2 = 4 alpha / pi (the executor's reading, 2026-10-25)

Status: a reading, not a verdict. Instrument `benchmarks/foundations/ring_selffield.py` (source-form field
energies by pair sums over a uniform tube of sub-rings with exact elliptic-integral potentials and mutual
inductances; credential in the file and in `analysis/ring_selffield_reading.log`). Asked by the Director's advice
memo of 2026-10-25 (RING-WAVE-ANOMALY): does the one mechanism class that reaches g = 2 by mechanics
(ELEC_MECH_1_reading.md, M7b) also get the measured O(alpha) excess from its own registered self-field, and is the
answer cutoff-free or ln(R / b)-enhanced?

## 1. The computation
The ring: charge q uniformly distributed (the time average of the travelling winding), circulating at beta = 1,
radius R, core radius b, in Gaussian-type units (1 / 4 pi eps0 = 1, c = 1). Its own fields add to the class's
energetics: the moment is the current's, mu = q c R / 2, exact; the mass is m c^2 = 2 (E_wave + U_E + U_M) by the
scale virial (every 1 / R energy balances the tension, section 1 of ELEC_MECH_1_legC_instrument.md); the angular
momentum is J = E_wave R / c + L_field. Hence
    g - 2 = 2 (U_E + U_M - c L_field / R) / (E_wave + c L_field / R).
Field energies from the thin-tube closed forms, which the instrument reproduces (credential):
    U_E = (q^2 / 2 pi R)(ln(8R/b) + c_E), c_E = 0.2495 (1/4 for a uniform tube; slope d U_E / d ln b exact to 1e-4)
    U_M = (beta^2 q^2 / 2 pi R)(ln(8R/b) + c_M), c_M = -1.7505 (-7/4 for a uniform tube; the slope exact to 1e-4)
    L_field = q <Phi_self> / 2 pi c (the quasistatic field-momentum theorem Int E x B / 4 pi c = Int rho A / c,
    checked on a 3D grid to 0.996 to 0.998 before the grid was dropped for its near-field errors), which for
    beta = 1 gives c L_field / R = 2 U_M exactly.
So U_E + U_M - c L_field / R = U_E - U_M = (q^2 / 2 pi R)(c_E - c_M) = (q^2 / 2 pi R) x 2.000: the logarithms
cancel, the cross-section constants cancel (+1/4 each), and the inductance's curvature constant -2 is all that
survives. With e^2 = alpha hbar c and E_wave = hbar c / 2R at the Compton radius (m c^2 = 2 E_wave at leading order),
    g - 2 = 4 alpha / pi = 9.29e-3,  independent of b (b / R from 1e-3 to 1e-1 give 4.0000, 4.0001, 3.9988) and of nc.
Next order: the O(alpha) shift of E_wave and of the denominator, of relative size alpha, is not included.

## 2. Reading
The class's self-field gives the Schwinger FORM, cutoff-free, with coefficient 4 instead of 1: (g - 2) / 2 =
2 alpha / pi against the measured alpha / 2 pi = 1.16e-3. Nothing was tuned and no cutoff enters, so the factor is
a property of the mechanics as modelled, not of a parameter. Honest possibilities, none adopted here:
  (a) the field energies are additional to the twist energy, as assumed: then the class predicts 4 alpha / pi and
      is wrong by 4 at O(alpha), a precise kill of the class as the free electron;
  (b) the registered dictionary (EM-017 to EM-022) already counts the magnetic self-energy inside the twist energy
      (the twist IS the magnetic field's mechanical form in this ontology): then U_M must not be added to m, the
      bracket becomes U_E - 2 U_M and is ln-enhanced, and the class fails at O(alpha) in a different way;
  (c) the charge of the travelling winding is not uniform on the time average, or rides a different radius from
      the energy, which the time-average argument (ELEC_MECH_1_legC_instrument.md) says it cannot;
  (d) a factor 4 from the quantum layer the programme does not have (the registered spin machinery, ELEC-100).
Which of (a) and (b) holds is a registry question, not a computation, and it is the first thing the lab should
settle; (c) and (d) are named as directions of escape.

## 3. What this is worth
It is the first O(alpha) number the electron sector has produced from mechanics with no fitted parameter, and it
has the right form. It is not evidence for the framework: the coefficient is wrong by 4, and the ring-wave is
still 9 percent above the co-moving fold in energy and nine orders off in scale (Leg C record sections 3c and 6).
It is evidence that the class is a sharp object: it predicts a specific wrong number rather than a vague one.
