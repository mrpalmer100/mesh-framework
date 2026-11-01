# NUC-MIRROR-COULOMB: SEALED EVIDENCE DESIGN (written before any instrument is touched)

Commission NUC-MIRROR-COULOMB, kind discriminator, question key nuc-coulomb-mirror-displacement. Theorist's design,
2026-11-03. A redraft of NUC-MIRROR-CDE (analysis/lab/drafts/NUC-MIRROR-CDE/design.md, withdrawn before any lock,
not a try; no review record found by the Director or by me). Queue rule: this file is committed before the kit
exists; nothing below changes afterwards; a change is a new name. No mass value of the evidence cell was read while
writing it; every number here is a registered number, stated arithmetic on registered numbers, or a synthetic
fixture. The redraft's cures are listed in the DISCLOSURES section at the end.

## 0. WHY

The Director's proposal, in my words. The weights-of-atoms row carries two frozen mass models (M1, NUC-018's
three-term form; M2, the four-term form with NUC-A plus NUC-B's a_A = 19.85 MeV). Both have been scored only on
absolute masses (NUC-BLIND-1, NUC-BLIND-2, NUC-NEW-5), where the one calibrated constant (the bond depth eps,
equivalently a_V fixed on Ca-40), the surface term and the symmetry term carry most of the number, and the derived
Coulomb term is a correction whose coefficient the registry itself records as 9 percent high (NUC-018:
a_C = 0.7716 MeV against the empirical 0.711). On one channel every other term cancels identically: the mass
difference of a T = 1/2 mirror pair, M(Z+1, N = Z) minus M(Z, N = Z+1). In both M1 and M2 the volume term a_V A,
the surface term (a_S/a_V) a_V A^(2/3) and the symmetry term a_A (N-Z)^2 / A (with (N-Z)^2 = 1 for both members)
are identical for the two members, neither model has a pairing term, and what remains is the Coulomb term alone.
The Ca-40 calibration does not enter. So the mirror channel scores the derived, zero-constant Coulomb term by
itself, and the registry has never formed this difference (the Director's search and mine found no mirror-pair
reading anywhere in the corpus; NUC-MIRROR-CDE was designed for it and withdrawn before a kit existed).

North Star row served: Weights of atoms (docs/NORTH_STAR.md section 2), the cell "Coulomb term derived from
winding charge and spacing (+9%)". Rule of section 5: this charter names (c), a discriminator: it arms and
adjudicates the mirror-channel discriminator between the two registered Coulomb forms (the uniform sphere sealed
in M1 and M2; NUC-C's diffuseness-plus-exchange form). It moves no target from blocked to derived and retires no
input; section 7 says so in those words.

Gear: breadth (the atoms row is the only row with a target-facing question a lab commission can decide this week,
by the Director's notes; it has been visited once since the last promotion, by NUC-NEW-5). Not a dive; no lead is
followed (lead L88294 is a different question, the AME forecast). Nearest write-ups read for this design:
analysis/NUC_NEW_5_results.md and analysis/NUC_BLIND_2_results.md (the frozen models, the house constants, the
harness pattern); claims NUC-005, NUC-018, NUC-C, NUC-D, GG-006; the NUC-C charter
docs/commissions/COMMISSION_NUC_C_coulomb_corrections.md and the NUC-C result record in
docs/commissions/SYNC_STATE.md; the driver benchmarks/lab/nuc_new_5/driver.py; the withdrawn design.

The Director's guess about the withdrawn design (that the NUC-C leg was the weak point) is, on my reading, right
and sharper than stated: NUC-C's diffuseness correction is registered as a profile (Fermi, width a_d = xi/2 =
0.699 fm), a base sphere (r0 = 1.05 fm) and one number (-7.8 percent at Pb-208), but NOT as a rule for how the
profile's radius is tied to the sphere's, and the leading-order Coulomb expansion (section 8, arithmetic shown)
gives different Pb-208 numbers under each natural rule. The withdrawn design fixed one rule and would have
registered a "not reproducible" finding if that rule failed, which is a finding about the theorist's choice as
much as about NUC-C. This redraft pre-states every admissible rule, gates NUC-C's instantiation on the registered
Pb-208 number under a rule chosen by arithmetic on registered numbers only, and credentials the new Poisson
integrator on two closed forms (the uniform sphere and a Gaussian) before any evidence is read. The Director's
other option (keep the NUC-C leg to closed forms) is not available: the only closed-form content of NUC-C's
Coulomb term is the exchange shape Z^(4/3) / A^(1/3) and the Pb-208 effective coefficient 0.704 MeV; the
diffuseness fraction's A-dependence, which dominates NUC-C's form on this channel (A = 13 to about 75, where
(a_d / R)^2 is four to twenty times its Pb-208 value), is numerical in NUC-C and nowhere in closed form. A
constant 0.704 MeV is not NUC-C's form on this channel and is not scored as such.

## 1. THE QUESTION

Q1 (the Coulomb term as sealed). Does the uniform-sphere Coulomb term of M1 and M2 (form F-U, a_C = 0.7716 MeV on
Z^2 / A^(1/3)) reproduce the measured Coulomb displacement energies of the T = 1/2 mirror pairs at its registered
precision (a bias within 8.5 percent, the coefficient's own registered offset; section 4)? U-AGREES upgrades the
Coulomb cell's evidence from "coefficient within 9 percent of the SEMF's" to "confirmed on a calibration-free
channel". U-MISS-HIGH or U-MISS-LOW names the Coulomb term, with its sign, as the registered miss on that channel.
Neither answer changes any claim's status or any grade (section 7).

Q2 (the NUC-C form). Does NUC-C's form (F-C, section 3: the uniform sphere on NUC-C's registered base r0 = 1.05 fm,
the diffuseness correction of a Fermi charge profile at a_d = 0.699 fm by numerical Poisson under the convention
the gate of section 5 selects, and the exchange term of SEMF shape Z^(4/3) / A^(1/3) with its coefficient fixed by
NUC-C's registered Pb-208 fraction) reproduce the same displacement energies at the same precision? C-AGREES and
C-MISS-* are the same answers for NUC-C's claim. Two open answers are kept apart: C-INSTRUMENT-OPEN records that
the design's Poisson integrator failed its own calibration or convergence (a fault of the new instrument, no
finding about NUC-C); C-NOT-REPRODUCED records that the integrator passed and NO admissible convention reproduces
NUC-C's registered Pb-208 number, i.e. that NUC-C's Coulomb construction cannot be instantiated from the registry
(its code is not in the repository). Only the second is a fact about the record.

Q3 (the discriminator). Which of F-U and F-C has the smaller rms fractional residual on the pairs, and is the
difference above the pair-resampling floor? PREFERS-U or PREFERS-C decides between the two registered forms on
this channel; NO-PREFERENCE leaves them tied here. This does not decide which form the absolute-mass models should
carry (NUC-C's S1 regression and NUC-D's recovery are a separate, registered matter).

What no answer changes: the grade of the row (D3), the status of NUC-018 or NUC-C, the five numbers of
NORTH_STAR section 2b, the shell, pairing and light-isotope cells.

Sub-reading S (no form; no claim or rider may quote it): the Spearman rank correlation of each form's fractional
residual with A, beside a permutation null (section 4), printed by the verdict with its rule. It describes whether
a miss is flat in A or grows; it adjudicates nothing.

## 2. THE EVIDENCE SET

The table. data/ame2012/AME2012.txt in the repository, sha256
88c6272c9e4117d68ac1317e2590c9e376d25f77c9bf68fd6062bbb4e238cb13 (the pin in benchmarks/lab/nuc_new_5/driver.py
CONFIG['pins']['ame2012_sha256'], carried by NUC-NEW-5 and NUC-032), 2438 data rows 'Z N M' with M the mass excess
in MeV after a one-line header, the table NUC-BLIND-1, NUC-BLIND-2 and NUC-NEW-5 treat as experimental. No
AME2020 row is used (the AME2020 file is not in the repository; a build that needed it would wait on a person).
The mirror-pair masses of AME2012 are decades-old measurements at the keV to tens-of-keV level; nothing in this
channel waits on a newer table.

The rule (the build script tools/mirror_pairs.py, written by the worker to this rule, no choice left to it): a
pair is every odd A >= 13 (the models' registered domain is A >= 12, CONFIG min_a = 12; 13 is the smallest odd A
in it) with Z_p = (A+1)/2 such that BOTH rows (Z_p, Z_p - 1) and (Z_p - 1, Z_p) are in the table. No upper limit
on A; no exclusion by any other criterion; the rule selects what is there. The build reads the Z and N columns
only to form the label list and never prints or stores a mass. It writes
analysis/holdout/NUC_MIRROR_COULOMB/labels.txt ('A Z_p' rows, ascending A) and MANIFEST.json (the AME2012
sha256, the labels sha256, the count n, the rule, the time) and refuses to overwrite. The driver's manifest unit
requires the manifest's AME2012 hash to equal the pin above and records n and the labels hash. Pinned by this
design: the AME2012 hash and the rule. Recorded by the build: the labels hash and n (the design does not know n).

The quantity scored, read once. For pair i with A_i and Z_p,i, the measured Coulomb displacement energy
    CDE_meas,i = [M(Z_p, Z_p - 1) - M(Z_p - 1, Z_p)] + (d_n - d_h),
with d_n = 8.07131714 MeV and d_h = 7.28897059 MeV the neutron and H-1 mass excesses (CONFIG d_n, d_h of
benchmarks/lab/nuc_new_5/driver.py; rows (0, 1) and (1, 0) of the table), d_n - d_h = 0.78234655 MeV. This is the
binding difference B(Z_p - 1, Z_p) - B(Z_p, Z_p - 1) exactly (B = Z d_h + N d_n - M). The truth unit reads the two
M values of every labelled pair once, seals the array, and nothing else reads the table.

What the programme has and has not inspected, plainly. The AME2012 table is public and the programme has read it
as ABSOLUTE masses many times: NUC-005 and NUC-018 (C-12 to U-238), the 50-row draws NUC-BLIND-1 and -2, the
whole-table regressions of LAMED and NUC-026/027. Most members of these pairs are in those readings. The
programme has never formed a mirror difference, and no registered quantity was fitted to one: the Coulomb term's
only inputs are the winding charge (GG-006) and the spacing d0 = 2.026 fm from the saturation density 0.17 fm^-3
(NUC-017), not a mass; NUC-C's width and depth come from xi and NUC-B's eta, not a mass. This is a
calibration-free channel scored on a public table, NOT a blind hold-out under NORTH_STAR section 5's bar W (bar W
binds models that carry a calibration against the table; the calibration cancels here). No rider will use the
word blind.

Expected size, for the record and not as a pin: odd A from 13 upward with both members measured holds at most
about 32 pairs (A = 13 to about 75). The halt-grade count floor is 15 (section 5, C-5): the fifteen pairs A = 13
to 41 (N-13/C-13 through Sc-41/Ca-41) are textbook nuclides whose masses have been in every evaluation for
decades, so a build that finds fewer than 15 has misparsed the table. The floor is a misparse detector, not a
statistical bar.

## 3. THE MODELS OR PREMISES

Both forms are frozen as registered; nothing is calibrated, re-fit or re-derived here.

F-U, the Coulomb term as sealed in M1 and M2 (NUC-018; NUC-032 carries the frozen constants; code
benchmarks/lab/nuc_new_5/driver.py, functions a_c() and binding(), imported unchanged): E_C = a_C Z^2 / A^(1/3),
a_C = 0.6 x 1.44 MeV fm / r0, r0 = (3 / (4 pi sqrt 2))^(1/3) x d0, d0 = 2.026 fm (NUC-017). Arithmetic:
4 pi sqrt 2 = 17.771532; 3 / 17.771532 = 0.1688097; cube root 0.552687; r0 = 1.119744 fm;
a_C = 0.864 / 1.119744 = 0.771605 MeV (the sealed 0.7716). Mirror prediction, exact for both M1 and M2 and for any
a_V:
    CDE_U(A) = a_C [Z_p^2 - (Z_p - 1)^2] / A^(1/3) = a_C (2 Z_p - 1) / A^(1/3) = a_C A^(2/3).
Credential C-1 proves this cancellation numerically from the sealed binding() with each model's sealed a_V rather
than taking it from this paragraph.

F-C, NUC-C's form as registered (NUC-C, Modeled; depends on NUC-B, NUC-005, GG-006). NUC-C's code is not in the
repository (it ran "in-package", docs/commissions/SYNC_STATE.md; no file under benchmarks/ carries it), so the
form is instantiated from the claim text, by the following reading, with the one thing the text does not fix
(the radius convention) handled by the gate C-4(iii) of section 5 and not by a choice of mine.
  (a) Base: the uniform sphere on NUC-C's own spacing, r0 = 1.05 fm (the NUC-C charter's "spacing r0 = 1.05 fm
      derived"; NUC-005's d0 = 1.9 fm times 0.552687 = 1.0501 fm), a_C0 = 0.864 / 1.05 = 0.822857 MeV (the
      registered 0.823). NUC-C was built on the spacing NUC-017 had already superseded; the design scores NUC-C as
      registered and does not move it to d0 = 2.026 fm (that would be a re-derivation, not a test). R(A) =
      r0 A^(1/3) is the sphere's radius; E_uniform = (3/5) Z^2 e^2 / R with e^2 = 1.44 MeV fm.
  (b) Diffuseness: a Fermi charge profile rho(r) = rho_0 / (1 + exp((r - C) / a_d)), a_d = xi / 2 = 0.699 fm
      (NUC-C: "a_d = xi/2 = 0.699 fm, committed before grading"), rho_0 fixed by the total charge Z. The
      electrostatic energy by numerical Poisson in spherical symmetry, E = (e^2 / 2) int_0^inf [q(r) / r]^2 dr
      with q(r) the charge inside r (the field-energy form; identical to (1/2) int rho phi). The fraction
      f_d(A) = E_Fermi(A) / E_uniform(A) - 1 depends on A only (E scales as Z^2 for a fixed profile). The claim
      text ties the profile to the sphere by the sphere's radius R(A) and nothing else, which admits two rules for
      the half-density radius C:
        convention H: C = R(A) (the profile's half-density radius is the sphere's radius);
        convention V: rho_0 equals the sphere's density Z / (4 pi R^3 / 3), so C solves
                      4 pi rho_0 int_0^inf r^2 / (1 + exp((r - C) / a_d)) dr = Z (the sphere's interior density
                      is kept and the edge is smeared at constant volume; the Myers-Swiatecki reading of a
                      diffuseness correction); C exists and is unique because the integral is monotone in C.
      A third rule, the equal-rms convention S (C chosen so the profile's mean-square radius equals the sphere's
      3 R^2 / 5), is computed at Pb-208 as a diagnostic only and is NOT an instantiating convention, by arithmetic:
      the Fermi profile's mean-square radius is (3/5) C^2 [1 + (7/3) pi^2 (a_d / C)^2] plus exponentially small
      terms, so equal rms needs R^2 >= (7/3) pi^2 a_d^2 = 23.027 x 0.488601 = 11.251 fm^2, i.e.
      A^(2/3) >= 11.251 / 1.1025 = 10.205, A >= 32.6; convention S has no Fermi profile at all for the pairs
      A = 13 to 31, so it cannot be NUC-C's form on this channel whatever NUC-C did at Pb-208.
      The registered value the gate reads: f_d(208) = -0.078 (NUC-C: "-7.8% at Pb-208"), under whichever of H and
      V reproduces it (section 5, C-4(iii)). The reading is fixed here and is not revised in any case.
  (c) Exchange: - c_ex Z^(4/3) / A^(1/3), the registered SEMF shape, with c_ex fixed by NUC-C's registered Pb-208
      fraction of -6.6 percent of the uniform-sphere energy: c_ex = 0.066 x a_C0 x 82^2 / 82^(4/3) =
      0.066 x 0.822857 x 82^(2/3); ln 82 = 4.406719, x 2/3 = 2.937813, exp = 18.874; c_ex = 0.054309 x 18.874 =
      1.0250 MeV. Reading check: a_C0 (1 - 0.078 - 0.066) = 0.822857 x 0.856 = 0.7044, the registered "effective
      a_C = 0.704", so both fractions are read at Pb-208 and add; that is the whole basis of the reading. (NUC-C's
      own construction of the coefficient, the winding-correlation hole at depth 1 - eta = 0.424, is not
      re-derived; the registered fraction pins c_ex.)
  Mirror prediction under the selected convention X in {H, V}:
      CDE_C(A) = a_C0 [1 + f_d,X(A)] A^(2/3) - c_ex [Z_p^(4/3) - (Z_p - 1)^(4/3)] / A^(1/3).
  If C-4(i) or (ii) fails, F-C is not instantiated and every F-C form is C-INSTRUMENT-OPEN (an integrator fault).
  If (i) and (ii) pass and (iii) selects no convention, F-C is not instantiated and every F-C form is
  C-NOT-REPRODUCED (a fact about the registry).

Not a premise here: the bond depth eps, a_V, a_S/a_V, a_A, pairing, shells. They cancel or are absent, which is
the point of the channel. The nucleon mass unit and m_e enter only through d_n - d_h, a measured constant.

## 4. THE STATISTICS AND BARS

Per pair i and form F in {U, C}: the fractional residual e_F,i = (CDE_F(A_i) - CDE_meas,i) / CDE_meas,i
(positive: the form overpredicts the displacement energy).
    b_F = (1/n) sum_i e_F,i                     the bias
    s_F = sqrt((1/n) sum_i e_F,i^2)             the rms fractional residual
    D = s_C - s_U                               the discriminator (positive favours F-U)

Bar B1 (agreement, both forms): |b_F| <= 0.085. Provenance: NUC-018's registered offset of the derived
coefficient against the empirical SEMF value, 0.7716 / 0.711 - 1 = +0.0852, the precision at which the registry
already calls the Coulomb term derived; the mirror channel either holds that precision with no calibration or it
does not. The same bar for F-C, so the two forms are judged at one standard (NUC-C's own window, 0.68 to 0.75 MeV
on 0.711, is -4.4 to +5.5 percent, narrower; the wider registered bar is used for both and is the more lenient of
the two for F-C).

Floor N1 (the bias is above the pair scatter): the centered bootstrap of the mean. Seed 20261103 (the date of this
design), 10000 resamples of n pairs with replacement, statistic |mean(e*) - b_F|, floor phi_F = its 99th
percentile. A MISS form needs |b_F| > 0.085 AND |b_F| > phi_F; |b_F| > 0.085 with |b_F| <= phi_F is NO-CALL (the
miss is not resolved against the scatter). The percentile and the resample count are the house values of
NUC-NEW-5's floor F (CONFIG floor_percentile 99.0, floor_resamples 10000).

Floor N2 (the discriminator is above the scatter): the paired centered bootstrap of D. Same seed, 10000 resamples
of pairs, statistic |D* - D|, floor psi = its 99th percentile. PREFERS needs |D| > psi.

Sub-reading S (no form): Spearman correlation r_F of e_F,i with A_i; permutation null seed 20261103, 1000
permutations of A among the pairs, 99th percentile of |r| printed beside r_F (the house values of NUC-NEW-5's Q3
null: q3_permutations 1000, q3_percentile 99.0). No threshold is applied and no claim or rider quotes it.

Nothing else is computed from the cell. No per-pair exclusion, no reweighting, no second statistic. Every number
above is fixed here; the evidence is read once, after every credential in section 5 has passed.

## 5. THE CREDENTIALS

All run before the truth unit opens the table; each is halt-grade unless marked diagnostic. A halt renders the
open form for every question that depends on it. The order is C-1, C-2, C-3, C-4, C-5; the Poisson integrator is
credentialed (C-4(i), (ii)) before it computes anything that bears on a form.

C-1 Cancellation (halt-grade). The kit imports binding() and a_c() from benchmarks/lab/nuc_new_5/driver.py
    (unchanged, credentialed by NUC-NEW-5's C-1 and run binding). For every label and for both sealed models
    (M1: a_S/a_V 1.34, a_A 0, a_V 17.770286909889982; M2: a_S/a_V 1.108, a_A 19.85, a_V 15.987072226683638; the
    NUC-032 constants) it requires binding(A, Z_p - 1, ...) - binding(A, Z_p, ...) = a_c() A^(2/3) to 1e-9 MeV,
    and a_c() = 0.771605 to 1e-5 MeV. This proves the channel is the Coulomb term alone, for both models. (The
    labels are read from labels.txt; no mass is touched.)
C-2 House constants (halt-grade). d_n - d_h from CONFIG equals the table's rows (0, 1) minus (1, 0) to 1e-8 MeV;
    the table's sha256 equals the pin.
C-3 Build on a synthetic fixture (halt-grade). A planted 'Z N M' table (synthetic numbers only): planted pairs at
    A = 13, 15, 27, 41, 59; a planted A = 11 pair (must be excluded: below the domain); a planted T = 1 sibling at
    A = 27 (rows (14, 13) and (13, 14) plus (15, 12); the T = 1 row must not change the pair); a planted odd A = 31
    with one member missing (must be excluded); a planted even A = 28 with rows (15, 13) and (13, 15) (must be
    excluded: even A is not a T = 1/2 pair); the fixture's (0, 1) and (1, 0) rows. The build must return exactly
    the five planted pairs in ascending A, and the truth rule on the fixture must return the planted differences
    plus 0.78234655 MeV to 1e-9.
C-4 The Poisson integrator and the NUC-C reading (halt-grade for the F-C leg only; Q1 is unaffected). Three checks,
    run in this order, on registered numbers and synthetic fixtures only:
    (i) Calibration on two closed forms, both to 1e-6 relative: a uniform sphere of charge Z = 82 and radius
        R = 6.2213 fm (= 1.05 x 208^(1/3)) reproduces (3/5) Z^2 e^2 / R; a Gaussian profile rho(r) proportional
        to exp(-r^2 / (2 sigma^2)) with Z = 82 and sigma = 2.0 fm reproduces Z^2 e^2 / (2 sqrt(pi) sigma)
        (the self-energy of a Gaussian charge: the interaction of two such charges at separation s is
        Z^2 e^2 erf(s / (2 sigma)) / s and the self-energy is half its s -> 0 limit). The Gaussian is the
        diffuse-tail check: an integrator that only handles a step edge cannot pass it. Both profiles are run on
        the same grid family the Fermi profile will use.
    (ii) Convergence: f_d,H(208) and f_d,V(208), and f_d,H(13) and f_d,V(13) (A = 13 is the rule's floor, a design
        constant, not a cell value), are each unchanged to 1e-6 under doubling of the radial grid and of the outer
        cutoff (cutoff at C + 20 a_d or more; the grid resolves a_d by at least 50 points).
    (iii) The gate: f_d,X(208) is in [-0.088, -0.068] for X = H, for X = V, or for both. The window is the
        registered -7.8 percent, quoted to one decimal, with a tolerance of 1.0 percentage point (ten times the
        quoting precision, enough for grid error, not enough to admit a different construction). If exactly one
        convention passes, F-C is instantiated under it. If both pass, F-C is instantiated under the one whose
        f_d(208) is closer to -0.078 (a rule on registered numbers, fixed here). If neither passes, F-C is not
        instantiated. The outcome is one of three: (a) (i), (ii) pass and (iii) selects a convention: F-C
        instantiated, the selected convention named in every output. (b) (i) or (ii) fails: the integrator is at
        fault; every F-C form (Q2 and Q3) is C-INSTRUMENT-OPEN; (iii) is not read; no f_d(208) is reported as a
        finding and no rider is written on NUC-C. (c) (i) and (ii) pass and (iii) selects nothing: the integrator
        is credentialed and no admissible reading reproduces NUC-C; every F-C form is C-NOT-REPRODUCED and the
        result records the converged f_d,H(208), f_d,V(208) and the diagnostic f_d,S(208) as the finding that
        NUC-C's construction is not reproducible from the registry. The reading is not revised in any case.
C-5 The set (halt-grade). n >= 15 (section 2); labels unique, ascending, odd A >= 13, each with both rows in the
    table; the labels hash recorded and equal between the manifest and the driver's own read of labels.txt.
C-6 Floors computed on the cell (not a credential: a pre-stated null procedure). The verdict computes phi_U, phi_C
    and psi from the sealed residuals with the seeds and percentiles of section 4 and prints them beside the
    statistics. No threshold is chosen or changed after the computation.
Diagnostics (recorded, gate nothing): the per-pair table (A, Z_p, CDE_meas, CDE_U, CDE_C, e_U, e_C); f_d,H(A) and
f_d,V(A) at every label; f_d,S(208); the effective Pb-208 coefficient of the instantiated F-C,
a_C,eff(208) = a_C0 [1 + f_d,X(208)] - c_ex / 82^(2/3), printed against the registered 0.704 (by construction it
equals 0.7044 when f_d,X(208) = -0.078 exactly).

Smoke run (LAB_SMOKE=1): every unit on a throwaway hold-out built from the C-3 fixture in a temporary directory;
pre-stated answers: fixture S1 plants CDE_meas = a_C A^(2/3) exactly for the five pairs, so the smoke verdict must
compute b_U = 0 and s_U = 0 to 1e-12; fixture S2 plants CDE_meas = 1.2 x a_C A^(2/3), so b_U = 1/1.2 - 1 =
-0.166667 and s_U = 0.166667 to 1e-9. The smoke runs C-4(i) and (ii) in full (they touch no evidence) and
withholds every FORM line (labkit's rule); it never opens analysis/holdout/NUC_MIRROR_COULOMB/ or the evidence
checkpoint.

## 6. THE FORMS

Q1 (F-U), exactly one:
  U-AGREES        |b_U| <= 0.085
  U-MISS-HIGH     b_U > 0.085 and b_U > phi_U
  U-MISS-LOW      b_U < -0.085 and |b_U| > phi_U
  U-NO-CALL       |b_U| > 0.085 and |b_U| <= phi_U
  INSTRUMENT-OPEN C-1, C-2, C-3 or C-5 failed, or any halt before the truth unit, or an exception in the verdict
Q2 (F-C), exactly one: C-AGREES, C-MISS-HIGH, C-MISS-LOW, C-NO-CALL by the same rules on b_C and phi_C;
  C-INSTRUMENT-OPEN if C-4(i) or C-4(ii) failed (integrator fault, no finding about NUC-C);
  C-NOT-REPRODUCED if C-4(i) and C-4(ii) passed and C-4(iii) selected no convention;
  INSTRUMENT-OPEN as for Q1.
Q3 (the discriminator), exactly one:
  PREFERS-U       D > 0 and |D| > psi
  PREFERS-C       D < 0 and |D| > psi
  NO-PREFERENCE   |D| <= psi
  C-INSTRUMENT-OPEN if Q2 is C-INSTRUMENT-OPEN; C-NOT-REPRODUCED if Q2 is C-NOT-REPRODUCED; INSTRUMENT-OPEN as
  for Q1. Under either of the first two, Q3 is open: no preference is read, because F-C has no prediction.
Possible combinations: any Q1 form with any Q2 form; Q3 carries the same open token as Q2 whenever Q2 is
C-INSTRUMENT-OPEN or C-NOT-REPRODUCED, and INSTRUMENT-OPEN whenever Q1 is. C-INSTRUMENT-OPEN and
C-NOT-REPRODUCED are mutually exclusive by the order of C-4 (a failure of (i) or (ii) stops before (iii) is read).
Every form is decided by the bars of section 4 and the checks of section 5 alone, on a buffer, printed once by
the verdict. Q1 is decided whatever happens to the F-C leg.

## 7. WHAT COUNTS

U-AGREES: rider on NUC-018 (and the scorecard's Coulomb cell): "The derived Coulomb term a_C = 0.7716 MeV on
Z^2 / A^(1/3), scored on the n T = 1/2 mirror pairs of AME2012 (A >= 13) where the calibrated bond depth, the
surface term and the symmetry energy cancel exactly: bias b_U, rms s_U (fractional, in CDE); within the
coefficient's registered 8.5 percent precision on a calibration-free channel (NUC-MIRROR-COULOMB)." Grade D3
unchanged (the term reproduces a measured quantity from a measured spacing); it strengthens the cell's evidence
and nothing else.
U-MISS-HIGH or U-MISS-LOW: rider on NUC-018 and the scorecard cell: "On the mirror channel the derived Coulomb term
misses by b_U (sign stated), above the pair-scatter floor phi_U: the Coulomb term is the named miss of the mirror
displacement energies (NUC-MIRROR-COULOMB)." Kept at full weight; never re-chartered to rescue it. The cell's text
"(+9%)" gains "(mirror channel: b_U)".
U-NO-CALL: a rider with the numbers and the floor; no sign is read.
C-AGREES / C-MISS-*: the same riders on NUC-C with b_C, s_C, phi_C and the convention named ("instantiated under
convention H" or "V", with f_d(208) as computed). C-INSTRUMENT-OPEN: NO rider on NUC-C and no finding about the
registry; the results file records that the design's Poisson integrator failed C-4(i) or C-4(ii), with the failing
check named, and that the F-C leg and Q3 are open for that reason; the commission's claim about NUC-C is "not
tested". C-NOT-REPRODUCED: rider on NUC-C: "NUC-C's Coulomb construction, instantiated from the claim text (Fermi
profile at a_d = 0.699 fm on the sphere R = 1.05 A^(1/3) fm) by a Poisson integrator that reproduces the uniform
sphere and a Gaussian to 1e-6 and is converged in grid and cutoff to 1e-6, gives f_d(208) = (value) under the
half-density convention and (value) under the constant-volume convention against the registered -0.078; neither
admissible reading reproduces NUC-C's number, the registry does not hold NUC-C's code, and the form is not
instantiable from the record (NUC-MIRROR-COULOMB)." That is a registrable fact about the record; Q3 is open under
it and nothing is said about which form is preferred.
PREFERS-U / PREFERS-C: a one-line note in the results file and in the scorecard cell naming the preferred form on
this channel, with D and psi and the convention F-C was instantiated under. It does not change which form M1 and
M2 carry. NO-PREFERENCE: the note says the channel does not separate them at n pairs.
Every form: targets moved blocked to derived 0; inputs retired 0; discriminators armed or adjudicated 1 (the mirror
channel between the two registered Coulomb forms). None of the five numbers of section 2b moves. The release note
says "infrastructure" in those words if that is what the delta is.
What no form establishes: a mechanism (correlation of a residual with A is not one); anything about the Z(Z-1)
self-energy question (not a registered form); anything about absolute masses, shells, pairing or the light
isotopes; anything blind; anything about AME2020; anything about NUC-C's exchange construction beyond the
registered fraction; under C-NOT-REPRODUCED, anything about whether NUC-C's number was right or wrong (only that
the record cannot reproduce it).

## 8. NOT ASSUMED

Not leaned on: the Director's registered expectation (U-MISS-HIGH and PREFERS-C). Not leaned on: the theorist's
prior, stated so the record has it. (1) From the public Nolen-Schiffer literature, a uniform sphere with a Z^2
term (self-energy included) tends to overpredict displacement energies and a realistic diffuse distribution to
underpredict them by several percent nearly flat in A. (2) From the leading-order expansion of a Fermi profile's
Coulomb energy, derived by first-order perturbation of the sharp sphere (the diffuse part of the profile is odd
about C with first moment pi^2 a_d^2 / 6, and the charge renormalisation contributes -(6/5) pi^2 (a_d/R)^2 while
the odd part contributes +(1/2) pi^2 (a_d/R)^2, both in units of Z^2 e^2 / R): under convention H,
f_d = -(7/6) pi^2 (a_d / C)^2; under convention V, f_d = -(5/6) pi^2 (a_d / R)^2; under convention S the
(a_d / R)^2 term vanishes. At Pb-208 with C = R = 6.2213 fm and a_d = 0.699 fm, (a_d / R)^2 = 0.012624, so
H gives -0.145, V gives -0.104, S gives 0 at this order, and none is -0.078. Higher orders in (a_d / R)^2 are
about one to two points at Pb-208, so my prior is that the gate C-4(iii) fails and the F-C leg ends
C-NOT-REPRODUCED, with Q1 deciding alone. The gate is run as written whatever the prior says; if the exact
integral under V lands in the window, F-C is instantiated and scored. Neither prior sets a bar: B1 is NUC-018's
registered offset, the F-C reading is NUC-C's registered text, the conventions are the two the text admits, the
window is the registered number with a stated tolerance, the floors are null procedures with fixed seeds. The
theorist read no mass of the cell while writing this; the AME2012 file was opened for its header and its first
five rows (A <= 3) to confirm the layout and the (0, 1) and (1, 0) constants.
Not assumed: that AME2012 and AME2020 agree on these pairs (irrelevant; AME2012 is the table scored); that the Z^2
form is the right form (it is the registered one); that NUC-C's base spacing should be corrected (it is scored as
registered, the inconsistency with NUC-017 disclosed in section 3 and not repaired); that a MISS is a
Nolen-Schiffer effect (the sub-reading describes a shape, it names no cause); that NUC-C's exchange coefficient is
the Fermi-gas one (the registered fraction pins it); that a constant effective coefficient represents NUC-C on
this channel (it does not, section 0).

## 9. AUTONOMY AND COMPUTE

No step waits on a person: the table is in the repository by hash; the build is a rule; no draw is needed (the set
is deterministic, so no beacon round is committed; the bootstrap and permutation seeds are design constants, not
hold-out selections); the verdict runs once from the sealed checkpoint under labkit's one-invocation rule.
Compute: under 0.1 cpu hours (two radial Poisson integrals per label plus the calibration, convergence and gate
runs at Z = 82 and A = 13 and 208; one bisection per label for convention V; 2 x 10000 bootstrap resamples and
2 x 1000 permutations on n of order 30), memory under 200 MB, wall time under ten minutes including the smoke run.
Resumable one-unit-per-invocation driver in the locked order: credential, manifest, predict, seal, truth; verdict
separate.
Dollar budget: the compute is on the lab machine at no marginal cost; the worker and model spend for writing the
kit, the lock review rounds and the run is capped at 30 dollars in total (three worker tasks at the lab's per-task
cap of 10 dollars each, the cap the digests record; the lab's cost per completed commission has run 4 to 20
dollars, analysis/lab/digests/2026-10-18.md and 2026-10-25.md). Stop rule: if the 30 dollar ceiling is reached
before the verdict has run, the commission is withdrawn at that point and said so in the digest; no verdict is
read from a partial kit, no fourth task is spent, and a successor must be proposed under a new name.
Instrument files that exist: benchmarks/lab/_kit/labkit.py (harness); benchmarks/lab/nuc_new_5/driver.py (a_c(),
binding(), CONFIG constants; imported, not modified); data/ame2012/AME2012.txt (the table).
Files the worker must write: tools/mirror_pairs.py (the build, rule of section 2, with the C-3 fixture);
benchmarks/lab/nuc_mirror_coulomb/driver.py (units, the Poisson integrator with its two closed-form calibrations,
the conventions H, V and the diagnostic S, the F-U and F-C arithmetic, the credentials, the smoke);
benchmarks/lab/nuc_mirror_coulomb/verdict.py (the statistics, floors, sub-reading and forms of sections 4 and 6).
CONFIG of the driver carries every number of sections 3 to 5 verbatim. The Poisson integrator is new and is
credentialed by C-4(i) and (ii) before any evidence-bearing number is computed; the smoke exercises both
calibrations.

## DISCLOSURES (what this redraft changes against NUC-MIRROR-CDE, and why)

1. The radius convention of NUC-C's Fermi profile is no longer a single choice of the theorist. The withdrawn
   design fixed C = R (convention H) and would have registered "not reproducible" if that one reading failed; the
   arithmetic of section 8 shows the choice matters by four points at Pb-208 and that the registered -7.8 percent
   is not reproduced at leading order by either admissible reading. This design pre-states both readings, gates
   instantiation on the registered number under a rule fixed before any computation, and excludes the third
   reading (equal rms) by arithmetic on the channel's own A-range rather than by prior.
2. The Poisson integrator is credentialed on two closed forms (uniform sphere and Gaussian), not one, before any
   evidence run, and its convergence is checked at both ends of the channel's A-range (A = 13 and 208), as the
   Director asked.
3. The C-3 fixture gains an even-A trap (a build that admits even A has misread the rule).
4. The theorist's prior now says plainly that the F-C leg is expected to end C-NOT-REPRODUCED and that Q1 decides
   alone in that case; the commission is worth its lock on Q1 alone (the one calibration-free channel on the row,
   never formed) and the F-C leg is kept because a C-NOT-REPRODUCED verdict is itself a registrable fact about
   NUC-C's standing in the record.
5. The seeds are the date of this design (20261103). No bar changed: B1, the floors' percentiles and resample
   counts, the C-4(iii) window and the count floor are those of the withdrawn design, each with the same
   provenance.
Nothing in the evidence cell was read in making this redraft.
