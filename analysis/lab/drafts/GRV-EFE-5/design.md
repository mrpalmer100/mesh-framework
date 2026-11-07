# GRV-EFE-5: SEALED EVIDENCE DESIGN (written before any instrument is touched)

Commission GRV-EFE-5, kind discriminator, question key grv030-external-field-locality. Theorist's design, 2026-11-06.
The fifth design of this question; none has locked, so this is not a re-try under the two-tries rule. GRV-EFE-1 (the
author's draft of 2026-10-18, analysis/queue/parked/GRV_EFE_1_charter_DRAFT.md) was abandoned by its worker; GRV-EFE-2
was withdrawn before lock; GRV-EFE-3 died on its floor F-3 (Delta added twice); GRV-EFE-4 (sealed design
analysis/lab/drafts/GRV-EFE-4/design.md) died in the kit on fixture X-4, a single replicate that passed with probability
about 0.43. This design keeps GRV-EFE-4's question, evidence file, hold-out rule, cell rules, strata, placebo, F-3, S1,
P1, Q2 and forms to the digit, and changes only the synthetic fixtures (section 5): every fixture whose pass depended
on a draw is now either a rate fixture of 400 seeded replicates whose bar sits so far from the pre-measured rate that a
correct kit fails it with binomial probability below 1e-6, or is removed from the halt list. The cure is stated in
DISCLOSURES, first item. Nothing below changes after this file is committed; a change is a new name.

Every number below is a registered number, a value returned by sealed code (from the scratch run
analysis/lab/drafts/GRV-EFE-5/scratch_design.py, which imports benchmarks/gravity/grv_blind_1.py, reads data/sparc_rotmod
and synthetic e only, and never opens anything under data/sparc_efe/; and scratch_tails.py, scipy binomial tails only),
stated arithmetic, a value fixed in the author's 2026-10-18 draft before the evidence file existed, or a synthetic
fixture rate measured on seeds disjoint from the kit's.

## 0. WHY

The Director's proposal, in my words: the registered gravity sector has one galaxy-scale channel, the horizon coupling
that fixes g_dagger = c H0 / 2 pi (GRV-030, Modeled; D1 on the scorecard; no shape, GRV-031). The registry does not say
what the coupling responds to. Two readings are live and untested:

- H-LOCAL: the medium at a point responds to the total field there, so the coupling acts on the galaxy's internal
  Newtonian field plus the environmental field of surrounding structure. Prediction: at low internal acceleration the
  observed acceleration falls below the registered no-environment prediction, more so the stronger the environment.
- H-SOURCE (the global reading): the coupling references the galaxy's own field, as the registered predictor computes
  it. Prediction: low-acceleration residuals do not depend on the environment.

The test pairs per-galaxy residuals of the registered prediction with the environmental field e_env of Chae et al. 2020,
already committed under a hash written before anyone opened it, on a beacon hold-out of SPARC galaxies. Row served:
Gravitational force, the D1 cell (g_dagger = c H0 / 2 pi, GRV-030), as a section 5 rule (c) discriminator. Gear: depth.
The lead it follows is this question's own record: four designs, none locked, the last (GRV-EFE-4) sound except for one
fixture, per the worker's abandonment record of 2026-11-06 01:39 quoted in the commission prompt; its evidence
(data/sparc_efe/chae2020_eN.csv) is in the repository and has never been read. A sub-reading only: GRV-BLIND-2's miss
(GRV-129) sat on two low-acceleration dwarfs (PGC51017, UGC04305; analysis/GRV-BLIND-2_verdict.log; GRV-130), which is
where H-LOCAL predicts an environmental effect.

## 1. THE QUESTION

Q1 (the discriminator). Over the matched low-acceleration galaxies of the beacon hold-out, do the per-galaxy mean
residuals D of the registered no-environment prediction fall with e_env (one-sided rank test against a within-stratum
permutation null at the locked alpha), with no such decline in the high-acceleration placebo?
- Would change: a rider on GRV-030 recording which reading of the coupling the data favour; a constraint any future
  derivation of the coupling (or of nu) must respect.
- Would not change: g_dagger, the D1 grade, any number of NORTH_STAR section 2b; GRV-030, GRV-031, GRV-129 stand.

Q2 (the amplitude; read only on EFE-LOCAL-FAVOURED). Does the zero-parameter one-dimensional local response (section 3),
with the registered g_dagger and nu, carry the effect at its own amplitude (regression slope of D on the predicted shift
Delta whose 99 percent interval contains 1 and excludes 0)?
- Would change: whether H-LOCAL's simplest algebraic form survives as the working form, or only its sign.
- Would not change: anything derived; the form is H-LOCAL's algebra, not a mesh derivation (the author declined
  derivation commissions, GRV-EFE-DERIVE-2, GRV-NU-DERIVE-2).

## 2. THE EVIDENCE SET

Unchanged from GRV-EFE-4 except the commission name in paths and labels.

What is scored. The pairing of (i) per-galaxy residuals from the public SPARC table data/sparc_rotmod (175 Rotmod_LTG
files, shipped since GRV-030, whole-table exposed: inputs and observed velocities have been read by the programme many
times) with (ii) the column e_env of Chae, Lelli, Desmond, McGaugh, Li and Schombert 2020 (ApJ 904, 51; arXiv:2009.11525v2,
erratum-corrected Table 2): the Newtonian environmental field from large-scale structure in the authors' a0 = 1.2e-10
m/s^2, NOT the field e fitted to each rotation curve (that would be circular).

How it is obtained with no person acting. The file data/sparc_efe/chae2020_eN.csv is in the repository. It must have
sha256 f18ee3c7eac92b248a1e7eea0f62e4e706bb749c648ecdb9b8947570c54248e7, the value the author's 2026-10-18 draft wrote
when tools/extract_chae2020_eenv.py produced it. The extractor's sha256 is
6623da6f494bccbc81d5eeef21f99781b9f3e15e6ca5ffb60a395a683558f288 (scratch_design.py, recomputed today; equal to
GRV-EFE-3's and GRV-EFE-4's). The scored galaxies are chosen by the lab's public randomness beacon (bar W, below). Cell
rules, all from pre-evidence sources:
- eligible: at least three kept points (Vobs > 0, errV/Vobs < 0.1, r > 0). Provenance: GRV-030's table rule as coded in
  tools/holdout_galaxies.py and grv_blind_1.py, used by GRV-BLIND-1/2.
- low-acceleration galaxy: at least three kept points with 0 < g_bar < 0.3 g_dagger. Provenance: the author's 2026-10-18
  draft, section 2, verbatim.
- high-acceleration placebo galaxy: at least three kept points with g_bar > g_dagger. Provenance: g_dagger is the model's
  only acceleration scale; the three-point minimum is the registered eligibility minimum; the section 3 form puts its
  smallest shift there (ratio in section 4, P1).
- matched: exact string equality of the file's galaxy name with the Rotmod file stem (name less "_rotmod.dat").
No exclusion after the file is read; a galaxy that misses is a miss. Galaxies outside the hold-out are never paired.

Pinned now (public table and code only, whole table, before any draw; code values from scratch_design.py): 155 eligible
galaxies, 2788 kept points with g_bar > 0; low-acceleration rule 136 galaxies holding 1524 such points (1537 kept points
over all 155 galaxies satisfy 0 < g_bar < 0.3 g_dagger); placebo 39 galaxies, 652 points; strict set (at least three
points with 0 < g_bar < 0.1 g_dagger) 104 galaxies.

Read once. The evidence file, by the driver's sealed-read unit, once; its values go to the checkpoint and to no screen.
The run records the row count, matched counts and unmatched names at run time. None of those is in this design; the
halts of section 4 are rules the run applies to them.

What the programme has and has not inspected, told exactly. On 2026-10-18 the executor ran the extractor on the authors'
LaTeX source; the extractor prints a row count, "names unique", "e_env in [0,1]", an erratum flag for NGC5033/NGC5055 and
the sha256, never a value. The parked GRV-EFE-1 draft records that row count and that every row matched a SPARC name.
This design does not repeat the count and no bar, halt or fixture uses it. No per-galaxy e_env value has been printed,
read or computed on by anyone in the programme; nothing pairing e_env with a residual has run. GRV-EFE-3's worker ran its
kit only on a synthetic SPARC-shaped table; GRV-EFE-4's worker wrote no kit (its simulation sim_x4.py was pure numeric).
This theorist's scratch scripts read data/sparc_rotmod and synthetic e only. The author, the executor and this theorist
know the source paper's headline (an external-field detection under the authors' MOND fits); none has seen the table.
The SPARC residuals are exposed, and GRV-BLIND-2's log names the two dwarfs carrying its miss.

Bar W, met by a beacon hold-out. GRV-030's nu was selected on this table (the simple form over the tanh family by 0.0086
dex, GRV-030), so W applies as written: the scored set is a pre-registered hold-out chosen by a process other than the
commission, and every prediction is frozen before the held-out pairing is read.
- The draw. At lock the lab commits a future drand round to the lab branch (a beacon_draw entry, as GRV-BLIND-2 section
  11). When the round is published, the lab runs, with the unchanged tool (sha256
  87fa200c1145f9d8b87922f272544b6c18a09bab1cd657ff59f99e3f87e25d7a, scratch_design.py),
      python tools/holdout_galaxies.py draw --name GRV_EFE_5 --seed {seed} --n 78 --drawn-by "drand beacon round {round}"
  where {seed} is the round's 32-byte randomness read as a non-negative base-16 integer, exactly as GRV-BLIND-2's
  amendment, recorded verbatim in analysis/holdout/GRV_EFE_5/MANIFEST.json. The kit reads only the held-out name list
  and records the manifest's sha256; the tool's split files are not used. No redraw for any reason.
- Size 78 = ceil(155/2): half the eligible table held out; the power cost is measured (X-1 at this size; F-3 on the
  hold-out itself).
- BLOCKED. If the manifest is absent, the driver prints BLOCKED with the exact command and exits 2. Not a form; it is the
  wait the beacon resolves with no person acting. No unit pairing e with a residual runs before the manifest passes C-6.
- What the hold-out protects: the commission's hand in which galaxies are scored. It does not make the residuals
  unseen; the rider says so.

## 3. THE MODELS OR PREMISES

Unchanged from GRV-EFE-4.

- The registered no-environment prediction (H-SOURCE's predictor): GRV-030 as implemented in
  benchmarks/gravity/grv_blind_1.py (sha256 4c407e9e732c431909b3bf8bc0e6abcf214083f8fe2c480c526ae921503aa634), imported
  unchanged: g_bar = (sign(Vgas) Vgas^2 + 0.5 Vdisk^2 + 0.7 Vbul^2)/r; g_pred = g_bar nu(g_bar/g_dagger),
  nu(y) = 1/(1 - exp(-sqrt y)); G_DAGGER = 1.0830375259007784e-10 m/s^2 (code value; registry 1.083e-10).
- The residual: r_i = log10(g_obs,i) - log10(g_pred,i), g_obs = Vobs^2/r, on kept points with g_bar > 0.
- The noise scale of F-3 and the fixtures: sigma_F = max(0.1423, sd_low) dex, where 0.1423 is GRV-030's whole-table
  point rms at the predicted g_dagger (code value 0.14225775) and sd_low is the population sd (ddof 0) of D_g over the
  136 whole-table low-acceleration galaxies of the public SPARC table (D_g as in section 4, computed on all 136, before
  any draw, with no file under data/sparc_efe/ opened): code value 0.1492612735 (scratch_design.py; mean D_g -0.00107).
  So sigma_F = 0.14926 dex. It is computed on the whole, already-exposed table, independent of e and of the draw. Any
  true Delta variance already present in the whole-table D_g is inside sd_low, so the choice can only enlarge the noise
  and err toward UNDERPOWERED; it never adds Delta to a reading (the GRV-EFE-3 defect).
- The conversion: e_N = eN_a0 x 1.2e-10 m/s^2; e = e_N/g_dagger = 1.1079948 x eN_a0 (code 1.1079948490260687).
- H-LOCAL's form, frozen (the author's draft section 6): with internal Newtonian field g_N = g_bar and an aligned
  environmental field e_N, total observed field nu(z)(g_N + e_N) with z = (g_N + e_N)/g_dagger, of which nu(e) e_N is the
  environment's own; the galaxy's internal observed field is
      g_local = g_N nu(z) + e_N [nu(z) - nu(e)],
  equal to the registered prediction at e_N = 0 (the kit uses g_pred directly there). Per galaxy,
      Delta_g = mean over its low-acceleration points of [log10(g_local) - log10(g_pred)]   (negative for e_N > 0),
      Delta_hi_h = the same mean over a placebo galaxy's points with g_bar > g_dagger.
- Premise carried by provenance, not checkable in the sandbox: the extractor's cell index is e_env and not the fitted e
  (the authors' TeX source is not in the repository). Stated in every rider.
- Disclosed nature of e_env: built from 2M++ dynamical masses with LCDM infill, so it estimates a total external field
  under LCDM, not a baryonic Newtonian field. Q1 (a rank statistic) does not depend on that reading; Q2 uses e_env as
  e_N, and a slope below 1 is read with that caveat.

Nothing is calibrated, fitted or re-fit.

## 4. THE STATISTICS AND BARS

Unchanged from GRV-EFE-4 to the digit, except the seed labels (now "GRV-EFE-5 ...") and the scratch rates quoted, which
are re-measured by this design's own scratch run.

Seeds: s(label) = int(sha256(label)[:8], 16) & 0x7fffffff with labels "GRV-EFE-5 S1", "GRV-EFE-5 F3", "GRV-EFE-5 P1",
"GRV-EFE-5 Q2" and, for the fixtures, "GRV-EFE-5 FIX X-1" ... "GRV-EFE-5 FIX X-9" (one label per fixture; rule written
here; the strings are the seeds' only source). The scratch rates in this design were measured on the disjoint labels
"GRV-EFE-5 SCRATCH ...", so the kit's fixture realizations are independent of the ones that set the bars. Ranks:
average ranks for ties (scipy.stats.rankdata, "average"); rho = Pearson correlation of the ranks (Spearman).

Per-galaxy quantities, over the beacon hold-out only. For each matched held-out low-acceleration galaxy g:
D_g = mean of r_i over its points with 0 < g_bar < 0.3 g_dagger; Delta_g (section 3); e_g from the file. For each
matched held-out placebo galaxy h: H_h = mean of r_i over its points with g_bar > g_dagger; Delta_hi_h; e_h. Galaxies are
the units; points are not pseudo-replicated.

Acceleration strata. For the low-acceleration set, x_g = median of log10(g_bar/g_dagger) over the galaxy's
low-acceleration points; for the placebo set, x_h = the same median over its points with g_bar > g_dagger. Galaxies are
sorted by name, then stably by x; the ordered list is split into three consecutive strata by numpy.array_split (sizes
differ by at most one, larger strata first). x comes from the SPARC inputs only, never from e. Provenance: three is the
least number of strata separating the low, middle and upper parts of a cell; at the hold-out's expected 68.4
low-acceleration galaxies (78 x 136/155) each stratum holds about 23, and at the H-2 floor of 10 placebo galaxies the
strata 4, 3, 3 still admit 4! 3! 3! = 864 distinct arrangements, enough for p < 0.01.

Stratified permutation (used by S1, P1, F-3 and the fixtures): e is permuted across galaxies within each stratum
independently; D (or H, or D_syn) is never permuted, shifted or added to.

Halts (rules applied at run time; values recorded then). Disclosed: the GRV-EFE-1 record (every row matched) makes these
foregone in practice; under full matching the hypergeometric probability that a 78-of-155 draw holds fewer than 30 of
the 136 low-acceleration galaxies is below 1e-15, and fewer than 10 of the 39 placebo galaxies 6.87e-5 (GRV-EFE-4's
scratch, hypergeometric arithmetic on the pinned counts). They are fail-closed guards against a broken join or file and
carry no evidential weight.
- H-1 coverage: matched held-out galaxies >= 50 and matched held-out low-acceleration galaxies >= 30, else
  EFE-OPEN-COVERAGE. Provenance: the author's draft (100 eligible, 30 low-acceleration); the first scaled by 78/155
  (50.3, floored), the second as written.
- H-2 placebo coverage: matched held-out placebo galaxies >= 10, else EFE-OPEN-COVERAGE. Provenance: p < 0.01 needs at
  least 5 galaxies unstratified (5! = 120); 10 is twice that, and is attainable under the three strata (864 > 100).

F-3, the floor (principle 5), on the hold-out, read after the sealed read and before any statistic pairs e with D.
Computed over the matched held-out low-acceleration galaxies from their e_g, their Delta_g (computed from e_g and the
SPARC inputs) and their strata, and from nothing else: F-3 never reads D, H or any residual. Seed s("GRV-EFE-5 F3").
2,000 replicates; in each, D_syn = Delta + n, with n drawn independently per galaxy from N(0, sigma_F^2),
sigma_F = 0.14926 dex (section 3, credential C-9); p_syn = (1 + #{rho_perm <= rho(D_syn, e)})/1,001 over 1,000
stratified permutations of e; a hit if p_syn < 0.01. Power = hits/2,000. Bar: power >= 0.80, else
EFE-OPEN-UNDERPOWERED. Provenance: the conventional design power 0.80 at the test's alpha 0.01. Delta enters D_syn
exactly once and the base n is Delta-free by construction. Scale stated: on synthetic e log-uniform on
[10^-2, 10^-0.5] a0, at sigma_F, F-3 at the fixture count (100 x 500) run inside 2,400 synthetic hold-outs
(scratch_design.py, all fixture settings) gives power from 0.87 to 1.00, mean 0.990; the real e distribution is not
known to anyone, and F-3 is what reads it.

S1 (Q1): rho_obs = rho(D, e) over the matched held-out low-acceleration galaxies; 10,000 stratified permutations of e,
seed s("GRV-EFE-5 S1"); p_minus = (1 + #{rho_perm <= rho_obs})/10,001, p_plus = (1 + #{rho_perm >= rho_obs})/10,001 on
the same permutations. Bars: effect present if p_minus < 0.01; reversed if p_plus < 0.01; absent if p_minus >= 0.05 and
p_plus >= 0.01; 0.01 <= p_minus < 0.05 is not read. Provenance: the author's draft section 6 (0.01, 0.05), unchanged;
the reversed branch uses the same 0.01.

P1 (placebo, a veto on Q1's present branch): rho_hi = rho(H, e) over matched held-out placebo galaxies; 10,000
stratified permutations, seed s("GRV-EFE-5 P1"); p_hi = (1 + #{perm <= rho_hi})/10,001; fires if p_hi < 0.01. Why the
veto is honest: H-LOCAL's form predicts a small shift at high acceleration too; on synthetic e the mean |Delta_hi| over a
hold-out's placebo galaxies is 0.130 of the mean |Delta| over its low-acceleration galaxies (largest 0.186; 400 synthetic
hold-outs, scratch_design.py), and X-1 measures the price: 0.020 of 400 planted replicates render EFE-CONFOUNDED (GRV-EFE-4
measured 0.0175). About one true effect in 50 is converted to CONFOUNDED, stated. A significant decline at high
acceleration is read as a systematic (distance, inclination, selection) correlated with e. The veto's reach is measured,
not assumed (scratch_design.py, 400 replicates each, the X-4 world of section 5 at three planted trend sizes c): P1 fires
in 0.425 of replicates at c = 0.3, 0.9325 at c = 0.6, 1.000 at c = 1.0. So a confound at high acceleration of total
span 0.3 dex across the placebo set would slip the veto more often than not; a non-firing placebo does not exclude every
confound, and the EFE-LOCAL-FAVOURED rider says so.

Q2: OLS slope of D on Delta, with intercept, over the matched held-out low-acceleration galaxies; 10,000 bootstrap
resamples of galaxies with replacement, seed s("GRV-EFE-5 Q2"); [L, U] = 0.5th and 99.5th percentiles of the slope.
Bars: CARRIES if L > 0 and L <= 1 <= U; UNDER if L > 0 and U < 1; OVER if L > 1; FORM-OPEN if L <= 0. Provenance: 1 is
H-LOCAL's own amplitude, 0 is no response; 99 percent matches S1's alpha.

## 5. THE CREDENTIALS

All halt-grade unless marked diagnostic; a halt renders EFE-INSTRUMENT-OPEN and stops. Units C and X read nothing
under data/sparc_efe/. C-0 to C-9 are GRV-EFE-4's, unchanged; the fixtures are rebuilt (DISCLOSURES).

- C-0 hashes: grv_blind_1.py, tools/extract_chae2020_eenv.py and tools/holdout_galaxies.py equal the sha256 values of
  sections 2 and 3 (recomputed today by scratch_design.py: all three equal).
- C-1 G_DAGGER from the imported module: |G - 1.083e-10| <= 5e-14 (the registry's four digits; code
  1.0830375259007784e-10).
- C-2 whole-table rms at the predicted g_dagger over the 2788 kept points of the 155 eligible galaxies equals GRV-030's
  0.1423 within 1e-4 (code 0.14225775).
- C-3 counts, exact integers (code values, whole table): 155; 2788; 136 galaxies holding 1524 points; 1537; 39 galaxies,
  652 points; strict 104.
- C-4 local form: Delta at e_N = 0 is exactly 0; at g_N = 0.1 g_dagger, e_N = 0.05 g_dagger,
  log10(g_local/g_pred) = -0.22922 within 1e-4 (code -0.2292214260).
- C-5 conversion 1.2e-10/G_DAGGER = 1.10799 within 1e-4 (code 1.1079948490).
- C-6 the hold-out (before any pairing): analysis/holdout/GRV_EFE_5/MANIFEST.json exists (else BLOCKED, exit 2), names
  the committed drand round, n = 78, 78 distinct names all among the 155 eligible; the draw reproduced from the
  manifest's seed by the unchanged tool in a scratch directory gives the same 78 names; the manifest sha256 goes to the
  checkpoint.
- C-7 stratification: on a synthetic set of 23 galaxies with tied and untied x, the strata have sizes 8, 8, 7, are
  ordered by x with name order breaking ties, and in 1,000 stratified permutations every permuted e vector has, in each
  stratum, exactly the multiset of e that stratum started with; the D vector passed in is returned bit-identical.
  Certain: every clause is a property of the code, true for every draw.
- C-8 F-3 reads no residual: F-3 is a function whose only arguments are e, Delta, strata, sigma_F and seeds; called twice
  with the same arguments and two different (synthetic) D vectors present in the checkpoint, it returns the identical
  power. Certain: same arguments and seed give the same output.
- C-9 noise scale: the population sd (ddof 0) of D_g over the 136 whole-table low-acceleration galaxies equals 0.14926
  within 1e-4 (code 0.1492612735), and the sigma_F passed to F-3 and the fixtures equals max(0.1423, that value)
  bit-identically. Computed from data/sparc_rotmod and the imported predictor only.
- Sealed-read structural checks (evidence unit, harness-only; prints pass/fail and counts, never a value): S-1 sha256
  equals f18ee3c7...248e7 in full (else exit 3, EFE-INSTRUMENT-OPEN); S-2 header exactly "galaxy,eN_a0"; S-3 row count
  in [150, 175] (the extractor's own range); S-4 names unique; S-5 every value a finite float in [0, 1] (the extractor's
  range); S-6 the join computed and its counts recorded.

Synthetic fixtures (unit X, before the evidence; synthetic e only; fixture k seeded by s("GRV-EFE-5 FIX X-k"); each runs
the whole form logic, F-3 included). Common law: each replicate draws a synthetic 78-of-155 subset of the eligible
galaxies (all names treated as matched unless the fixture says otherwise); e_N in a0 units log-uniform on
[10^-2, 10^-0.5], one value per galaxy; noise per galaxy from N(0, sigma_F^2), sigma_F = 0.14926; fixture S1 and P1 use
2,000 stratified permutations, fixture Q2 1,000 bootstrap resamples, and the F-3 inside every fixture replicate runs at
the reduced count of 100 replicates x 500 permutations with the same p_syn < 0.01 hit rule and power bar 0.80 (the
evidence counts are section 4's, F-3 there at 2,000 x 1,000).

THE CERTAINTY RULE (the cure). A fixture is either deterministic (its answer is a property of the code, the same for
every seed) or a rate fixture: 400 seeded replicates, a bar on the rate, and the bar placed so that a correct kit fails
it with binomial probability below 1e-6 even if the true rate sits a stated margin worse than the pre-measured one.
Every rate below was measured by scratch_design.py on seeds disjoint from the kit's, at the fixture counts, with F-3
inside every replicate; every tail is scipy.stats.binom from scratch_tails.py. No fixture is a single replicate whose
pass is a draw. A fixture bar is never relaxed after the kit runs; a fixture that fails is a kit fault, rendered
EFE-INSTRUMENT-OPEN.

- X-1 planted, a true H-LOCAL world, Delta planted exactly once on a Delta-free base: D = Delta + n and
  H = Delta_hi + n', n and n' independent per galaxy; no residual of the real table enters. 400 replicates. Bars:
  (i) rate of EFE-LOCAL-FAVOURED >= 0.90 (count >= 360); (ii) rate of EFE-CONFOUNDED <= 0.08 (count <= 32); (iii) among
  EFE-LOCAL-FAVOURED, rate of Q2 CARRIES >= 0.90. Measured (this design's scratch, 400 replicates): FAVOURED 0.970,
  CONFOUNDED 0.020, GAP 0.0075, SOURCE 0.0025, UNDERPOWERED 0 (F-3 0.87 to 1.00); Q2 CARRIES 385 of 391 FAVOURED, 0.985
  (a separate 400-replicate scratch run). GRV-EFE-4's scratch measured 0.9725, 0.0175 and 0.982 among 389: two
  independent measurements agree. Failure probability of a correct kit: (i) P(count < 360 | 400, 0.96) = 5.6e-8, at the
  measured 0.97 1.5e-11; (ii) P(count > 32 | 400, 0.03) = 2.5e-7, at the measured 0.02 1.4e-11; (iii) with 360
  FAVOURED and true rate 0.97, P(< 0.90) = 1.3e-10. Bars unchanged from GRV-EFE-4 ((i) is the Director's registered
  power bar).
- X-2 null: the same law with D = n, H = n' (nothing planted); 400 replicates; S1 computed in every replicate whatever
  F-3 returns. Bar: rate of p_minus < 0.01 <= 0.045 (count <= 18). Why the pass is certain: D is independent of e within
  every stratum by construction, so the permutation p-value (1 + count)/(N + 1) is super-uniform and the per-replicate
  probability of p_minus < 0.01 is at most 0.01 as a theorem; P(count > 18 | 400, 0.01) = 3.9e-8. Measured 0.0100.
  CHANGED from GRV-EFE-4's 0.03 (count <= 12), whose failure probability at the exact rate 0.01 is 2.5e-4, a coin by
  this design's rule; disclosed. What the looser bar costs: a kit whose null runs at twice nominal (0.02) would pass
  with probability 1 - 5.6e-4; X-2 detects a grossly broken null, not a mildly miscalibrated one, and the permutation
  construction, checked by C-7, is the main guard.
- X-3 reversed: as X-1 with D = -Delta + n. 400 replicates (was one). Bar: rate of EFE-REVERSED >= 0.90 (count >= 360).
  Measured 0.985 (SOURCE 0.015, F-3 0.89 to 1.00). P(count < 360 | 400, 0.97) = 1.5e-11.
- X-4 confound: as X-1 (D = Delta + n), with H_h = n'_h - c x (average rank of e_h)/n_placebo, c = 1.0. 400 replicates
  (was one, at c = 0.3). Bar: rate of EFE-CONFOUNDED >= 0.90 (count >= 360). Measured 0.995 (GAP 0.0025, SOURCE 0.0025;
  P1 fires in 1.000 of replicates; F-3 0.91 to 1.00). P(count < 360 | 400, 0.97) = 1.5e-11. Why c = 1.0: the fixture
  checks that the veto logic is wired (a strong high-acceleration decline must turn a present Q1 into CONFOUNDED), and
  the planted trend must be detected at >= 0.95 by the design's own arithmetic before sealing; c was chosen from
  {0.3, 0.6, 1.0} on that rule alone, on synthetic data only (rates 0.4225, 0.93, 0.995 of CONFOUNDED). The weaker
  trends' rates are the veto's measured reach, disclosed in section 4, P1, and in the FAVOURED rider.
- X-5 coverage: only 20 synthetic names match; pre-stated EFE-OPEN-COVERAGE. Deterministic: H-1 compares a count of 20
  with 50 before any draw-dependent step runs.
- X-6 underpowered, two clauses, neither depending on section 3's form at small e.
  (a) Deterministic, the form logic on a planted power: the instrument-line function that maps the F-3 power to a token
  is called with planted power 0.795 and must return EFE-OPEN-UNDERPOWERED; called with planted power 0.800 and with
  1.000 it must not return EFE-OPEN-UNDERPOWERED (it proceeds to the Q1 line). Exact comparisons against the bar 0.80;
  the same output for every seed.
  (b) Exact null power through F-3 itself: one synthetic 78-of-155 subset drawn by the common law, with e_N per galaxy
  log-uniform on [1e-7, 1e-6] a0 (continuous draw, so the ranks of e are untied with probability 1, and the kit checks
  that the e vector has no ties before calling, re-seeding nothing: a tie is a halt, and its probability under a
  continuous float64 draw of about 70 values is below 1e-12), and F-3 called (C-8's interface) with the Delta argument
  set to the zero vector exactly, not computed from section 3. Pre-stated: power < 0.80, and the instrument line returns
  EFE-OPEN-UNDERPOWERED. Why the pass is certain: with Delta = 0, D_syn = n is independent of e within every stratum, so
  each F-3 replicate's permutation p-value is super-uniform and P(hit) <= 0.01 exactly as in X-2 (a theorem, not a
  measurement); replicates are independent given e, so P(power >= 0.80) = P(>= 80 hits of 100) <= C(100, 80) x 0.01^80
  < 5.4e20 x 1e-160 < 1e-139.
  Disclosed correction: the earlier X-6 set every e_N to 1e-6 a0, which ties every rank of e and leaves rho undefined, and
  its premise "Delta within 1e-6 of 0" was false. By section 3's form at small e, nu(e) is about e^-1/2, so the
  environment's term e_N nu(e) is about g_dagger sqrt(e) (e = 1.108e-6 gives about 1.05e-3 g_dagger), against
  g_pred = 0.369 g_dagger at g_N = 0.1 g_dagger and 0.105 g_dagger at g_N = 0.01 g_dagger (nu(0.1) = 3.69,
  nu(0.01) = 10.5, stated arithmetic): |Delta| of order 1e-3 to 5e-3 dex, as the reviewer computed. No bar uses that
  size; clause (b) plants Delta = 0 exactly instead.
- X-7 tamper: one byte of a copy of a synthetic file changed against its recorded hash; pre-stated
  EFE-INSTRUMENT-OPEN. Deterministic.
- X-8 hold-out gate: with no manifest the driver exits 2 printing BLOCKED and runs no pairing unit; with a synthetic
  manifest whose seed does not reproduce its names, C-6 fails and the token is EFE-INSTRUMENT-OPEN. Deterministic.
- X-9 the GRV-EFE-3 regression: in one X-1 world, F-3 at the fixture count is called with D = 2 Delta + n present in the
  checkpoint and again with D = Delta + n; it returns the identical power for both. Deterministic (C-8's property on
  the fixture world). CHANGED: GRV-EFE-4's second clause ("and that power is >= 0.80") is removed, because on a single
  world it is a draw; the power of F-3 in planted worlds is credentialed by X-1's rate instead.
- Diagnostic (recorded, not a halt): the extractor's git history if git is available.
- Smoke (LAB_SMOKE=1): C-0 to C-5, C-7 to C-9 and X-5 to X-9 on synthetic tables and manifests, and X-1 to X-4 at 10
  replicates with reduced counts, their tallies printed and NOT checked against the bars (a smoke rate is not a
  credential); writes analysis/grv_efe_5_smoke.pkl, prints "smoke: forms withheld" and no form token, never opens
  data/sparc_efe/.

## 6. THE FORMS

GRV-EFE-4's forms, unchanged. Reached in this order; the first that applies is rendered for its line.

Instrument line: EFE-INSTRUMENT-OPEN (any halt-grade credential, structural check or fixture fails) / EFE-OPEN-COVERAGE
(H-1 or H-2) / EFE-OPEN-UNDERPOWERED (F-3 power < 0.80 on the hold-out) / INCOMPLETE-OPEN (a unit did not finish).
BLOCKED (exit 2, no manifest yet) is a wait for the beacon, not a form.

Q1 line (only if the instrument line is clean):
- EFE-REVERSED: p_plus < 0.01.
- EFE-CONFOUNDED: p_minus < 0.01 and P1 fires.
- EFE-LOCAL-FAVOURED: p_minus < 0.01 and P1 does not fire.
- EFE-SOURCE-FAVOURED: p_minus >= 0.05 and p_plus >= 0.01.
- EFE-OPEN-GAP: 0.01 <= p_minus < 0.05 and p_plus >= 0.01.
(p_minus < 0.01 and p_plus < 0.01 cannot both hold; the five are exhaustive.)

Q2 line (only on EFE-LOCAL-FAVOURED; otherwise "Q2 not read", no token): EFE-FORM-CARRIES / EFE-FORM-UNDER /
EFE-FORM-OVER / EFE-FORM-OPEN, by section 4's bars (exhaustive: L <= 0, or L > 0 with U < 1, or 1 in [L, U], or L > 1).

Possible combinations: one instrument-line form alone; or one of five Q1 forms, with EFE-LOCAL-FAVOURED exactly one of
four Q2 forms. The Director registered EFE-LOCAL-FAVOURED or EFE-OPEN-UNDERPOWERED as expected; the bars do not know it.

## 7. WHAT COUNTS

Riders on GRV-030. Each ends with the scope clause: "on the 78 SPARC galaxies drawn by drand round {round} (whose
residuals the programme had seen on the whole table; the draw removed the commission's choice of galaxies, not that
exposure), with Chae et al. 2020's e_env taken as the environmental field by the committed extractor's cell index,
under the registered g_dagger, nu and mass-to-light convention, against a null permuting e within three acceleration
strata".

- EFE-LOCAL-FAVOURED: "GRV-EFE-5: the low-acceleration residuals of the registered prediction fall with the
  environmental field (Spearman rho_obs, p_minus, n galaxies), with no decline at high acceleration at the same alpha
  (a placebo whose measured reach misses a high-acceleration trend of 0.3 dex span more often than not); the data favour
  H-LOCAL (the horizon coupling responds to the total field at the galaxy) over H-SOURCE." Plus: CARRIES "and the
  zero-parameter one-dimensional local form carries the effect at its own amplitude (slope interval [L, U] contains
  1)"; UNDER "but the effect is smaller than the local form predicts (U < 1), which the total-field nature of e_env may
  account for"; OVER "and the effect exceeds the local form's amplitude (L > 1)"; FORM-OPEN "and the amplitude is not
  resolved (L <= 0)".
- EFE-SOURCE-FAVOURED: "GRV-EFE-5: at a measured power of at least 0.80 (F-3, the value) to detect H-LOCAL's own
  predicted effect on these galaxies' e_env, under Gaussian galaxy-mean noise of 0.14926 dex (the whole-table
  between-galaxy sd of the low-acceleration mean residual), the low-acceleration residuals do not fall with the
  environmental field (p_minus >= 0.05); the data favour H-SOURCE, and the low-acceleration misses of GRV-BLIND-2 are
  not environmental at this test's reach."
- EFE-CONFOUNDED: "GRV-EFE-5: residuals fall with the environmental field at low acceleration and also at high
  acceleration, where H-LOCAL predicts almost no effect; the correlation is attributed to a systematic shared with e_env
  and neither reading is favoured."
- EFE-REVERSED: "GRV-EFE-5: low-acceleration residuals rise with the environmental field (p_plus < 0.01), contrary to
  both readings; recorded as an anomaly, neither favoured."
- EFE-OPEN-GAP, EFE-OPEN-COVERAGE, EFE-OPEN-UNDERPOWERED, EFE-INSTRUMENT-OPEN, INCOMPLETE-OPEN: "GRV-EFE-5 did not read
  the question (reason, with the failing number)"; no reading favoured. An UNDERPOWERED rider records F-3's power, so
  the record says how far the real e_env spread is from resolving H-LOCAL's own effect.

Grades and numbers. No form moves a grade (GRV-030 stays Modeled, D1) or any of the five numbers of NORTH_STAR section
2b: no target moves from blocked to derived, no input is retired, no prediction is externally adjudicated (the hold-out
is drawn by a public beacon, which is not an adjudicator). Said plainly: neither progress number moves; what the
commission buys is an armed and adjudicated discriminator on the D1 cell. Any form does NOT establish: a mechanism
(correlation is not mechanism; section 3's form is H-LOCAL's algebra, not a mesh derivation); that e_env is the baryonic
Newtonian field; that the extractor read the right column (a premise); anything beyond SPARC; anything about MOND's
external field effect as such; anything about the 77 eligible galaxies outside the hold-out. Bar W is met by the beacon
hold-out as written; no form is exploratory.

SECTION 5 LINE: this commission names (c), the discriminator it adjudicates between H-LOCAL and H-SOURCE, the two live
readings of the horizon coupling behind the Gravitational force row's D1 cell (GRV-030); it is target-facing, and it is
the target-facing session section 5 requires after NUC-MIRROR-LEAN-3, the last locked session, which was interior under
the author's named reading of 4 and 5 November 2026.

## 8. NOT ASSUMED

- Not assumed that the effect exists: the published detection used per-galaxy fitted fields under MOND; this test uses
  only e_env and the registered prediction, and the null is live.
- Not assumed that 0.1423 is the galaxy-mean scale: sigma_F is the larger of it and the measured whole-table
  between-galaxy sd of D_g (0.14926, C-9), which already contains any true Delta variance, so F-3 errs toward
  UNDERPOWERED. Not assumed Gaussian tails: if the held-out D carry heavier tails than a Gaussian at sigma_F, power may
  be overstated, and the rank statistic's robustness is the only protection (disclosed).
- Not assumed that three strata remove every acceleration-linked confound; they coarsen it, and P1 is the second guard,
  whose reach is measured (section 4) and stated in the rider.
- Not assumed that a fixture's synthetic rate is the real data's behaviour: the fixtures credential the kit's logic on
  a synthetic law; they say nothing about e_env.
- Not assumed that e_env is the right field for the mesh (LCDM infill); hence Q2 UNDER is a named outcome.
- Not assumed that the extractor's column index is right; carried in every rider.
- No re-run, no alternative cut (0.1 g_dagger is a sub-reading only), no exclusion after the read.
- Priors, stated and not leaned on: the Director expects EFE-LOCAL-FAVOURED or EFE-OPEN-UNDERPOWERED. The theorist
  expects Q1 present if powered (the source paper) and then EFE-FORM-UNDER, at no better than even odds; the theorist
  does not know the e_env distribution and so has no prior on F-3.

Sub-readings (printed after the forms; change no form; held-out galaxies only): e and D for PGC51017 and UGC04305
against the held-out median e, if drawn (else "not drawn"); S1 on the held-out strict set; S1 with the unstratified
null (to show what the strata changed); the low-acceleration point rms under the registered and the local prediction;
the ten galaxies of largest e with D and Delta.

## 9. AUTONOMY AND COMPUTE

No step waits on a person. The one independent choice, the hold-out, is a beacon draw (section 2); until the manifest
exists the driver exits 2 with BLOCKED. The evidence file is already committed.

Units, one per invocation, checkpoint analysis/grv_efe_5_ckpt.pkl (atomic, resumable): U0 credentials C-0 to C-5, C-7
to C-9 and fixtures X-1 to X-9 (no file under data/sparc_efe/); U1 SPARC residuals D, H, x and the inputs for Delta,
whole table; UH the hold-out (C-6; BLOCKED, exit 2, if no manifest); U2 sealed read (S-1 to S-6 on the whole file; H-1,
H-2 on the hold-out; e of held-out galaxies only to the checkpoint, nothing printed, the rest discarded); U3 F-3 (reads
e, Delta, strata; no residual); U4 S1, P1, Q2, sub-readings; terminal line "GRV-EFE-5 COMPLETE: run the verdict". U0
may be split into sub-units per fixture for resumability. The verdict script reads only the checkpoint, validates
status, units, hashes and finiteness, creates analysis/GRV-EFE-5_verdict.log with O_EXCL, and renders the instrument
line, Q1, Q2 in that order.

Compute, with the arithmetic. Per rate-fixture replicate: F-3 at 100 x 500 = 50,000 stratified permutation correlations,
plus S1 and P1 at 2,000 each, 54,000 in all; X-1 to X-4 at 400 replicates each give 1,600 x 54,000 = 8.64e7, plus X-1's
Q2 bootstraps (about 390 x 1,000 fits). At GRV-EFE-4's measured unvectorized rate (about 3.8e4 per second on one core)
that is about 38 cpu minutes; this design's vectorized scratch ran 2,400 such replicates in 153 s. The evidence adds F-3
at 2,000 x 1,000 = 2e6, S1 and P1 at 10,000 each, Q2's 10,000 fits and X-5 to X-9: under 3 minutes at the slower
rate. Budget 2 cpu hours (a margin near 3x on the slower rate), under 1 GB, under 3 hours wall.

Existing files: tools/holdout_galaxies.py and the lab's beacon tool (the GRV-BLIND-2 path),
benchmarks/gravity/grv_blind_1.py, tools/extract_chae2020_eenv.py, data/sparc_rotmod/, data/sparc_efe/chae2020_eN.csv,
benchmarks/lab/_kit/labkit.py. The worker writes benchmarks/lab/grv_efe_5/driver.py (with core functions in
benchmarks/lab/grv_efe_5/core.py if wanted) and benchmarks/lab/grv_efe_5/verdict.py. The theorist's scratch files are
not imported; the worker may copy code from them, but every function is credentialed here.

## DISCLOSURES (the cures)

- GRV-EFE-4's death, cured. Its X-4 was one replicate with a planted trend of c = 0.3 against noise sd 0.149, so the
  P1 veto fired in about 0.44 of replicates (the worker's sim_x4.py; this design's scratch 0.425) and the fixture would
  have returned its pre-stated EFE-CONFOUNDED with probability about 0.43, killing the kit at U0 on a fixture fault. The
  cure: (1) X-4 is a rate fixture of 400 replicates at c = 1.0, detected at 0.995 by the design's own arithmetic before
  sealing, with bar 0.90 whose failure probability for a correct kit is below 1e-10; (2) the same treatment for the
  other fixture GRV-EFE-4 left as a single random replicate, X-3 (now 400 replicates, measured 0.985, bar 0.90); (3) X-9's
  draw-dependent clause removed, its deterministic identity kept; (4) X-2's bar moved from 0.03 to 0.045 because the old
  bar failed a correct kit with probability 2.5e-4 at the exact null rate; (5) a written certainty rule (section 5) under
  which every remaining fixture is deterministic or carries a stated binomial tail below 1e-6. X-1's bars are unchanged;
  their tails are stated. Nothing else in GRV-EFE-4 is changed: question, evidence file and hash, hold-out rule and size,
  cells, strata, placebo, F-3, S1, P1, Q2, forms and riders (commission name aside).
- What the cure discloses about the instrument: the placebo veto's reach is now measured and stated (section 4, P1;
  the FAVOURED rider). This is new information against the instrument, not for it.
- GRV-EFE-3's death (Delta added twice in F-3) stays cured as in GRV-EFE-4: F-3's noise base is synthetic and
  Delta-free, F-3 takes no residual (C-8), and X-9 checks the property on a fixture world.
- GRV-EFE-1's death (the sealed input could not be credentialed in the sandbox) stays cured: the credential is what the
  sandbox can check (file hash written before anyone opened it, extractor hash, header, row range, uniqueness, value
  range, join); the column identity is a premise in every rider.
- A count in the record: the parked GRV-EFE-1 draft records the extractor's row count; no bar, halt or fixture here uses
  it, and section 4 discloses that H-1 and H-2 are foregone in practice because of that record.
- Constants are code values recomputed today by scratch_design.py and agree with GRV-EFE-4's to every digit quoted;
  pinned no tighter than the registry's digits (C-1, C-2) or at 1e-4 where five or more digits are quoted.
- No evidence was opened while writing this design; the scratch scripts read only data/sparc_rotmod, code and synthetic
  e, and scipy's binomial distribution.

## DISCLOSURES, REVISION 1 (the skeptical reviewer's objections)

- Objection (X-6 not certain: a constant e_N ties every rank and leaves rho undefined, so a correct kit either scores
  every replicate a hit or raises): what changed. X-6 no longer uses a constant e. Clause (a) is deterministic: the
  instrument-line function is called with planted powers 0.795, 0.800 and 1.000 and must return
  EFE-OPEN-UNDERPOWERED for the first only. Clause (b) draws e_N log-uniform on [1e-7, 1e-6] a0 per galaxy (untied
  ranks; a tie is checked and would halt, probability below 1e-12) and calls F-3 with Delta set to the zero vector
  exactly, so each replicate's hit probability is at most 0.01 by the permutation test's super-uniformity (the X-2
  theorem), and the chance of power >= 0.80 is below 1e-139. No pass depends on an undefined statistic or on a
  measured rate.
- Objection (X-6's arithmetic wrong: Delta is of order 1e-3 to 4e-3 dex at e_N = 1e-6 a0, not 1e-6): what changed. The
  false premise is withdrawn and the correct size is stated in X-6 with its arithmetic (e_N nu(e) about g_dagger
  sqrt(e), about 1.05e-3 g_dagger; |Delta| of order 1e-3 to 5e-3 dex). No bar rests on it: clause (b) plants Delta = 0
  exactly through F-3's Delta argument (the interface C-8 already credentials), which removes the dependence on the
  section 3 form at small e. Nothing else in the design changed; no evidence was read for this revision.
