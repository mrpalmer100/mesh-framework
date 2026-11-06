# GRV-EFE-4: SEALED EVIDENCE DESIGN (written before any instrument is touched)

Commission GRV-EFE-4, kind discriminator, question key grv030-external-field-locality. Theorist's design, 2026-11-06.
The fourth attempt at this question; none has locked, so this is not a re-try under the two-tries rule. GRV-EFE-1 (the
author's draft of 2026-10-18, analysis/queue/parked/GRV_EFE_1_charter_DRAFT.md) was abandoned by its worker; GRV-EFE-2
was withdrawn before lock; GRV-EFE-3 (sealed design analysis/lab/drafts/GRV-EFE-3/design.md) was abandoned by its worker
on one fixture defect, before any lock and before any evidence was read. This design keeps GRV-EFE-3's question, evidence
file, hold-out rule, cell rules, placebo, Q2 and forms, and replaces the parts the defect touched: the floor F-3, the null
of S1 and fixture X-1. The cure is stated in DISCLOSURES, first item. Nothing below changes after this file is committed;
a change is a new name.

Every number below is a registered number, a value returned by sealed code (from the scratch run
analysis/lab/drafts/GRV-EFE-4/scratch_design.py, which imports benchmarks/gravity/grv_blind_1.py, reads data/sparc_rotmod
and synthetic e only, and never opens anything under data/sparc_efe/), stated arithmetic, a value fixed in the author's
2026-10-18 draft before the evidence file existed, or a synthetic fixture rate.

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
Gravitational force, the D1 cell (g_dagger = c H0 / 2 pi, GRV-030). Gear: breadth. The Director's reason: this is the one
target-facing question whose evidence is already in the repository and has never been read; no statistic pairing e_env
with a SPARC residual has ever been computed. A sub-reading only: GRV-BLIND-2's miss (GRV-129) sat on two low-acceleration
dwarfs (PGC51017, UGC04305; analysis/GRV-BLIND-2_verdict.log), which is where H-LOCAL predicts an environmental effect.

## 1. THE QUESTION

Q1 (the discriminator). Over the matched low-acceleration galaxies of the beacon hold-out, do the per-galaxy mean
residuals D of the registered no-environment prediction fall with e_env (one-sided rank test against a within-stratum
permutation null at the locked alpha), with no such decline in the high-acceleration placebo?
- Would change: a rider on GRV-030 recording which reading of the coupling the data favour; a constraint any future
  derivation of the coupling (or of nu) must respect.
- Would not change: g_dagger, the D1 grade, any number of NORTH_STAR section 2b; GRV-030, GRV-031, GRV-BLIND-1/2 stand.

Q2 (the amplitude; read only on EFE-LOCAL-FAVOURED). Does the zero-parameter one-dimensional local response (section 3),
with the registered g_dagger and nu, carry the effect at its own amplitude (regression slope of D on the predicted shift
Delta whose 99 percent interval contains 1 and excludes 0)?
- Would change: whether H-LOCAL's simplest algebraic form survives as the working form, or only its sign.
- Would not change: anything derived; the form is H-LOCAL's algebra, not a mesh derivation (the author declined
  derivation commissions, GRV-EFE-DERIVE-2, GRV-NU-DERIVE-2).

## 2. THE EVIDENCE SET

What is scored. The pairing of (i) per-galaxy residuals from the public SPARC table data/sparc_rotmod (175 Rotmod_LTG
files, shipped since GRV-030, whole-table exposed: inputs and observed velocities have been read by the programme many
times) with (ii) the column e_env of Chae, Lelli, Desmond, McGaugh, Li and Schombert 2020 (ApJ 904, 51; arXiv:2009.11525v2,
erratum-corrected Table 2): the Newtonian environmental field from large-scale structure in the authors' a0 = 1.2e-10
m/s^2, NOT the field e fitted to each rotation curve (that would be circular).

How it is obtained with no person acting. The file data/sparc_efe/chae2020_eN.csv is in the repository. It must have
sha256 f18ee3c7eac92b248a1e7eea0f62e4e706bb749c648ecdb9b8947570c54248e7, the value the author's 2026-10-18 draft wrote
when tools/extract_chae2020_eenv.py produced it. The extractor's sha256 is
6623da6f494bccbc81d5eeef21f99781b9f3e15e6ca5ffb60a395a683558f288 (scratch_design.py, recomputed today; equal to
GRV-EFE-3's). The scored galaxies are chosen by the lab's public randomness beacon (bar W, below). Cell rules, all from
pre-evidence sources, unchanged from GRV-EFE-3:
- eligible: at least three kept points (Vobs > 0, errV/Vobs < 0.1, r > 0). Provenance: GRV-030's table rule as coded in
  tools/holdout_galaxies.py and grv_blind_1.py, used by GRV-BLIND-1/2.
- low-acceleration galaxy: at least three kept points with 0 < g_bar < 0.3 g_dagger. Provenance: the author's 2026-10-18
  draft, section 2, verbatim.
- high-acceleration placebo galaxy: at least three kept points with g_bar > g_dagger. Provenance: g_dagger is the model's
  only acceleration scale; the three-point minimum is the registered eligibility minimum; the section 3 form puts its
  smallest shift there (ratio computed in section 4, P1).
- matched: exact string equality of the file's galaxy name with the Rotmod file stem (name less "_rotmod.dat").
No exclusion after the file is read; a galaxy that misses is a miss. Galaxies outside the hold-out are never paired.

Pinned now (public table and code only, whole table, before any draw; code values from scratch_design.py): 155 eligible
galaxies, 2788 kept points with g_bar > 0; low-acceleration rule 136 galaxies holding 1524 such points (1537 kept points
over all 155 galaxies satisfy 0 < g_bar < 0.3 g_dagger, the author's tally of the same rule); placebo 39 galaxies, 652
points; strict set (at least three points with 0 < g_bar < 0.1 g_dagger) 104 galaxies.

Read once. The evidence file, by the driver's sealed-read unit, once; its values go to the checkpoint and to no screen.
The run records the row count, matched counts and unmatched names at run time. None of those is in this design; the
halts of section 4 are rules the run applies to them.

What the programme has and has not inspected, told exactly. On 2026-10-18 the executor ran the extractor on the authors'
LaTeX source; the extractor prints a row count, "names unique", "e_env in [0,1]", an erratum flag for NGC5033/NGC5055 and
the sha256, never a value. The parked GRV-EFE-1 draft records that row count and that every row matched a SPARC name.
This design does not repeat the count and no bar, halt or fixture uses it. No per-galaxy e_env value has been printed,
read or computed on by anyone in the programme; nothing pairing e_env with a residual has run. GRV-EFE-3's worker ran its
kit only on a synthetic SPARC-shaped table and stated that it read nothing under data/sparc_efe/. The author, the
executor and this theorist know the source paper's headline (an external-field detection under the authors' MOND fits);
none has seen the table. The SPARC residuals are exposed, and GRV-BLIND-2's log names the two dwarfs carrying its miss.

Bar W, met by a beacon hold-out (unchanged from GRV-EFE-3). GRV-030's nu was selected on this table (the simple form
over the tanh family by 0.0086 dex, GRV-030), so W applies as written: the scored set is a pre-registered hold-out chosen
by a process other than the commission, and every prediction is frozen before the held-out pairing is read.
- The draw. At lock the lab commits a future drand round to the lab branch (a beacon_draw entry, as GRV-BLIND-2 section
  11). When the round is published, the lab runs, with the unchanged tool (sha256
  87fa200c1145f9d8b87922f272544b6c18a09bab1cd657ff59f99e3f87e25d7a, scratch_design.py),
      python tools/holdout_galaxies.py draw --name GRV_EFE_4 --seed {seed} --n 78 --drawn-by "drand beacon round {round}"
  where {seed} is the round's 32-byte randomness read as a non-negative base-16 integer, exactly as GRV-BLIND-2's
  amendment, recorded verbatim in analysis/holdout/GRV_EFE_4/MANIFEST.json. The kit reads only the held-out name list
  and records the manifest's sha256; the tool's split files are not used. No redraw for any reason.
- Size 78 = ceil(155/2): half the eligible table held out; the power cost is measured (X-1 at this size; F-3 on the
  hold-out itself).
- BLOCKED. If the manifest is absent, the driver prints BLOCKED with the exact command and exits 2. Not a form; it is the
  wait the beacon resolves with no person acting. No unit pairing e with a residual runs before the manifest passes C-6.
- What the hold-out protects: the commission's hand in which galaxies are scored. It does not make the residuals
  unseen; the rider says so.

## 3. THE MODELS OR PREMISES

- The registered no-environment prediction (H-SOURCE's predictor): GRV-030 as implemented in
  benchmarks/gravity/grv_blind_1.py (sha256 4c407e9e732c431909b3bf8bc0e6abcf214083f8fe2c480c526ae921503aa634), imported
  unchanged: g_bar = (sign(Vgas) Vgas^2 + 0.5 Vdisk^2 + 0.7 Vbul^2)/r; g_pred = g_bar nu(g_bar/g_dagger),
  nu(y) = 1/(1 - exp(-sqrt y)); G_DAGGER = 1.0830375259007784e-10 m/s^2 (code value; registry 1.083e-10).
- The residual: r_i = log10(g_obs,i) - log10(g_pred,i), g_obs = Vobs^2/r, on kept points with g_bar > 0.
- The noise scale of F-3 and the fixtures: sigma_F = max(0.1423, sd_low) dex, where 0.1423 is GRV-030's whole-table
  point rms at the predicted g_dagger (code value 0.14225775) and sd_low is the population sd (ddof 0) of D_g over the
  136 whole-table low-acceleration galaxies of the public SPARC table (D_g as in section 4, computed on all 136, before
  any draw, with no file under data/sparc_efe/ opened): code value 0.1492612735 (scratch_design.py; mean D_g -0.00107).
  So sigma_F = 0.14926 dex, the between-galaxy scale of exactly the galaxy-mean residual F-3 models, applied as one
  draw per galaxy. It is not a statistic of the cell: it is computed on the whole, already-exposed table, independent of
  e and of the draw. Any true Delta variance already present in the whole-table D_g is inside sd_low, so the choice can
  only enlarge the noise and err toward UNDERPOWERED; it never adds Delta to a reading (the GRV-EFE-3 defect).
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

Seeds: s(label) = int(sha256(label)[:8], 16) & 0x7fffffff with labels "GRV-EFE-4 S1", "GRV-EFE-4 F3", "GRV-EFE-4 P1",
"GRV-EFE-4 Q2", "GRV-EFE-4 FIX" (rule written here; the strings are the seeds' only source). Ranks: average ranks for
ties (scipy.stats.rankdata, "average"); rho = Pearson correlation of the ranks (Spearman).

Per-galaxy quantities, over the beacon hold-out only. For each matched held-out low-acceleration galaxy g:
D_g = mean of r_i over its points with 0 < g_bar < 0.3 g_dagger; Delta_g (section 3); e_g from the file. For each
matched held-out placebo galaxy h: H_h = mean of r_i over its points with g_bar > g_dagger; Delta_hi_h; e_h. Galaxies are
the units; points are not pseudo-replicated.

Acceleration strata (new here, the Director's cure for the null). For the low-acceleration set, x_g = median of
log10(g_bar/g_dagger) over the galaxy's low-acceleration points; for the placebo set, x_h = the same median over its
points with g_bar > g_dagger. Galaxies are sorted by name, then stably by x; the ordered list is split into three
consecutive strata by numpy.array_split (sizes differ by at most one, larger strata first). x comes from the SPARC inputs
only, never from e. Provenance: three is the least number of strata separating the low, middle and upper parts of a
cell; at the hold-out's expected 68.4 low-acceleration galaxies (78 x 136/155) each stratum holds about 23, and at the
H-2 floor of 10 placebo galaxies the strata 4, 3, 3 still admit 4! 3! 3! = 864 distinct arrangements, enough for
p < 0.01. Purpose: the null no longer treats a galaxy of very low internal acceleration as exchangeable with one near
the cut, so an e that tracks a galaxy's acceleration level coarsely cannot by itself produce a significant rho.

Stratified permutation (used by S1, P1, F-3 and the fixtures): e is permuted across galaxies within each stratum
independently; D (or H, or D_syn) is never permuted, shifted or added to.

Halts (rules applied at run time; values recorded then). Disclosed: the GRV-EFE-1 record (every row matched) makes these
foregone in practice; under full matching the hypergeometric probability that a 78-of-155 draw holds fewer than 30 of
the 136 low-acceleration galaxies is below 1e-15 (scipy returns 0.0), and fewer than 10 of the 39 placebo galaxies
6.87e-5 (scratch_design.py). They are fail-closed guards against a broken join or file and carry no evidential weight.
- H-1 coverage: matched held-out galaxies >= 50 and matched held-out low-acceleration galaxies >= 30, else
  EFE-OPEN-COVERAGE. Provenance: the author's draft (100 eligible, 30 low-acceleration); the first scaled by 78/155
  (50.3, floored), the second as written.
- H-2 placebo coverage: matched held-out placebo galaxies >= 10, else EFE-OPEN-COVERAGE. Provenance: p < 0.01 needs at
  least 5 galaxies unstratified (5! = 120); 10 is twice that, and is attainable under the three strata (864 > 100).

F-3, the floor (principle 5), on the hold-out, read after the sealed read and before any statistic pairs e with D.
Computed over the matched held-out low-acceleration galaxies from their e_g, their Delta_g (computed from e_g and the
SPARC inputs) and their strata, and from nothing else: F-3 never reads D, H or any residual. Seed s("GRV-EFE-4 F3").
2,000 replicates; in each, D_syn = Delta + n, with n drawn independently per galaxy from N(0, sigma_F^2),
sigma_F = 0.14926 dex (section 3, credential C-9); p_syn = (1 + #{rho_perm <= rho(D_syn, e)})/1,001 over 1,000 stratified permutations
of e; a hit if p_syn < 0.01. Power = hits/2,000. Bar: power >= 0.80, else EFE-OPEN-UNDERPOWERED. Provenance: the
conventional design power 0.80 at the test's alpha 0.01. Delta enters D_syn exactly once and the base n is Delta-free by
construction, so a true H-LOCAL world in the real data cannot inflate F-3's noise (the GRV-EFE-3 defect). Scale stated:
on synthetic e log-uniform on [10^-2, 10^-0.5] a0, at sigma_F, F-3 run on each of 800 synthetic hold-outs (the X-1 and
X-2 replicates, at the fixture count of 100 replicates x 500 permutations; scratch_design.py) gives power from 0.90 to
1.00, mean 0.989; the real e distribution is not known to anyone, and F-3 is what reads it.

S1 (Q1): rho_obs = rho(D, e) over the matched held-out low-acceleration galaxies; 10,000 stratified permutations of e,
seed s("GRV-EFE-4 S1"); p_minus = (1 + #{rho_perm <= rho_obs})/10,001, p_plus = (1 + #{rho_perm >= rho_obs})/10,001 on
the same permutations. Bars: effect present if p_minus < 0.01; reversed if p_plus < 0.01; absent if p_minus >= 0.05 and
p_plus >= 0.01; 0.01 <= p_minus < 0.05 is not read. Provenance: the author's draft section 6 (0.01, 0.05), unchanged;
the reversed branch uses the same 0.01.

P1 (placebo, a veto on Q1's present branch): rho_hi = rho(H, e) over matched held-out placebo galaxies; 10,000
stratified permutations, seed s("GRV-EFE-4 P1"); p_hi = (1 + #{perm <= rho_hi})/10,001; fires if p_hi < 0.01. Why the
veto is honest: H-LOCAL's form predicts a small shift at high acceleration too; on synthetic e the mean |Delta_hi| over a
hold-out's placebo galaxies is 0.131 of the mean |Delta| over its low-acceleration galaxies (largest 0.177; 400 synthetic
hold-outs, scratch_design.py), and X-1 measures the price: 0.0375 of 400 planted replicates render EFE-CONFOUNDED. About
one true effect in 27 is converted to CONFOUNDED, stated. A significant decline at high acceleration is read as a
systematic (distance, inclination, selection) correlated with e. A non-firing placebo does not exclude every confound.

Q2: OLS slope of D on Delta, with intercept, over the matched held-out low-acceleration galaxies; 10,000 bootstrap
resamples of galaxies with replacement, seed s("GRV-EFE-4 Q2"); [L, U] = 0.5th and 99.5th percentiles of the slope.
Bars: CARRIES if L > 0 and L <= 1 <= U; UNDER if L > 0 and U < 1; OVER if L > 1; FORM-OPEN if L <= 0. Provenance: 1 is
H-LOCAL's own amplitude, 0 is no response; 99 percent matches S1's alpha.

## 5. THE CREDENTIALS

All halt-grade unless marked diagnostic; a halt renders EFE-INSTRUMENT-OPEN and stops. Units C and X read nothing
under data/sparc_efe/.

- C-0 hashes: grv_blind_1.py, tools/extract_chae2020_eenv.py and tools/holdout_galaxies.py equal the sha256 values of
  sections 2 and 3.
- C-1 G_DAGGER from the imported module: |G - 1.083e-10| <= 5e-14 (the registry's four digits).
- C-2 whole-table rms at the predicted g_dagger over the 2788 kept points of the 155 eligible galaxies equals GRV-030's
  0.1423 within 1e-4 (code 0.14225775).
- C-3 counts, exact integers (code values, whole table): 155; 2788; 136 galaxies holding 1524 points; 1537; 39 galaxies,
  652 points; strict 104.
- C-4 local form: Delta at e_N = 0 is exactly 0; at g_N = 0.1 g_dagger, e_N = 0.05 g_dagger,
  log10(g_local/g_pred) = -0.22922 within 1e-4 (code -0.2292214260).
- C-5 conversion 1.2e-10/G_DAGGER = 1.10799 within 1e-4 (code 1.1079948490).
- C-6 the hold-out (before any pairing): analysis/holdout/GRV_EFE_4/MANIFEST.json exists (else BLOCKED, exit 2), names
  the committed drand round, n = 78, 78 distinct names all among the 155 eligible; the draw reproduced from the
  manifest's seed by the unchanged tool in a scratch directory gives the same 78 names; the manifest sha256 goes to the
  checkpoint.
- C-7 stratification (new): on a synthetic set of 23 galaxies with tied and untied x, the strata have sizes 8, 8, 7,
  are ordered by x with name order breaking ties, and in 1,000 stratified permutations every permuted e vector has, in
  each stratum, exactly the multiset of e that stratum started with; the D vector passed in is returned bit-identical.
- C-9 noise scale (new): the population sd (ddof 0) of D_g over the 136 whole-table low-acceleration galaxies equals
  0.14926 within 1e-4 (code 0.1492612735), and the sigma_F passed to F-3 and the fixtures equals max(0.1423, that value)
  bit-identically. Computed from data/sparc_rotmod and the imported predictor only.
- C-8 F-3 reads no residual (new): F-3 is a function whose only arguments are e, Delta, strata, sigma_F and seeds;
  called twice with the same arguments and two different (synthetic) D vectors present in the checkpoint, it returns
  the identical power.
- Sealed-read structural checks (evidence unit, harness-only; prints pass/fail and counts, never a value): S-1 sha256
  equals f18ee3c7...248e7 in full (else exit 3, EFE-INSTRUMENT-OPEN); S-2 header exactly "galaxy,eN_a0"; S-3 row count
  in [150, 175] (the extractor's own range); S-4 names unique; S-5 every value a finite float in [0, 1] (the extractor's
  range); S-6 the join computed and its counts recorded.
- Synthetic fixtures (unit X, before the evidence; synthetic e only, seed s("GRV-EFE-4 FIX"); each runs the whole form
  logic, F-3 included, and must return its pre-stated token or rate). Common law: each replicate draws a synthetic
  78-of-155 subset of the eligible galaxies; e_N in a0 units log-uniform on [10^-2, 10^-0.5], one value per galaxy;
  noise per galaxy from N(0, sigma_F^2), sigma_F = 0.14926; fixture S1 and P1 use 2,000 stratified permutations,
  fixture Q2 1,000 bootstrap resamples, and the F-3 inside every fixture replicate runs at the reduced count of 100
  replicates x 500 permutations with the same p_syn < 0.01 hit rule and power bar 0.80 (counts as in scratch_design.py;
  the evidence counts are section 4's, F-3 there at 2,000 x 1,000).
  - X-1 planted, a true H-LOCAL world, Delta planted exactly once on a Delta-free base: D = Delta + n and
    H = Delta_hi + n', n and n' independent per galaxy from N(0, sigma_F^2); no residual of the real table enters.
    400 replicates, each running the whole form logic with F-3 first. Bars: (i) rate of EFE-LOCAL-FAVOURED >= 0.90;
    (ii) rate of EFE-CONFOUNDED <= 0.08; (iii) among EFE-LOCAL-FAVOURED, rate of Q2 CARRIES >= 0.90. Provenance, all
    measured at sigma_F with F-3 at 100 x 500 inside every replicate (scratch_design.py, 400 replicates): FAVOURED
    0.9725, CONFOUNDED 0.0175, GAP 0.010, UNDERPOWERED 0 (F-3 power in those worlds 0.91 to 1.00, mean 0.989). (i) is
    the Director's registered power bar; sd sqrt(0.9725 x 0.0275/400) = 0.0082, so 0.90 sits 8.9 sd below the measured
    rate. (ii) 0.08 is GRV-EFE-3's ceiling; measured 0.0175, sd 0.0066, 9.5 sd above. (iii) measured 0.982 among 389,
    sd 0.0067; 0.90 is 12 sd below.
  - X-2 null: the same law with D = n, H = n' (nothing planted), F-3 included at the fixture count; 400 replicates. Bar:
    rate of p_minus < 0.01 <= 0.03. Provenance: nominal 0.01, binomial sd sqrt(0.01 x 0.99/400) = 0.005, 0.03 = 0.01 +
    4 sd. (Scratch at sigma_F: 0.0075; F-3 power 0.90 to 1.00, none UNDERPOWERED.)
  - X-3 reversed: D = -Delta + n, one replicate; pre-stated EFE-REVERSED.
  - X-4 confound: as X-1, and H_h = n'_h - 0.3 x (average rank of e_h)/n_placebo; one replicate; pre-stated
    EFE-CONFOUNDED.
  - X-5 coverage: only 20 synthetic names match; pre-stated EFE-OPEN-COVERAGE.
  - X-6 underpowered: every e_N = 1e-6 a0 (Delta near zero); pre-stated EFE-OPEN-UNDERPOWERED.
  - X-7 tamper: one byte of a copy of a synthetic file changed against its recorded hash; pre-stated EFE-INSTRUMENT-OPEN.
  - X-8 hold-out gate: with no manifest the driver exits 2 printing BLOCKED and runs no pairing unit; with a synthetic
    manifest whose seed does not reproduce its names, C-6 fails and the token is EFE-INSTRUMENT-OPEN.
  - X-9 the GRV-EFE-3 regression (new, names the cure): the X-1 world, one replicate with the planted Delta doubled in
    the checkpoint's D (D = 2 Delta + n) and once with D = Delta + n: F-3, at the fixture count of 100 x 500, returns the
    identical power for both (C-8's property on the fixture world), and that power is >= 0.80.
- Diagnostic (recorded, not a halt): the extractor's git history if git is available.
- Smoke (LAB_SMOKE=1): C-0 to C-5, C-7 to C-9 and X-3 to X-9 on synthetic tables and manifests, with reduced counts;
  writes analysis/grv_efe_4_smoke.pkl, prints "smoke: forms withheld" and no form token, never opens data/sparc_efe/.

## 6. THE FORMS

Reached in this order; the first that applies is rendered for its line.

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
four Q2 forms. The Director expects EFE-OPEN-UNDERPOWERED, then EFE-LOCAL-FAVOURED; the bars do not know it.

## 7. WHAT COUNTS

Riders on GRV-030. Each ends with the scope clause: "on the 78 SPARC galaxies drawn by drand round {round} (whose
residuals the programme had seen on the whole table; the draw removed the commission's choice of galaxies, not that
exposure), with Chae et al. 2020's e_env taken as the environmental field by the committed extractor's cell index,
under the registered g_dagger, nu and mass-to-light convention, against a null permuting e within three acceleration
strata".

- EFE-LOCAL-FAVOURED: "GRV-EFE-4: the low-acceleration residuals of the registered prediction fall with the
  environmental field (Spearman rho_obs, p_minus, n galaxies), with no decline at high acceleration at the same alpha;
  the data favour H-LOCAL (the horizon coupling responds to the total field at the galaxy) over H-SOURCE." Plus:
  CARRIES "and the zero-parameter one-dimensional local form carries the effect at its own amplitude (slope interval
  [L, U] contains 1)"; UNDER "but the effect is smaller than the local form predicts (U < 1), which the total-field
  nature of e_env may account for"; OVER "and the effect exceeds the local form's amplitude (L > 1)"; FORM-OPEN "and
  the amplitude is not resolved (L <= 0)".
- EFE-SOURCE-FAVOURED: "GRV-EFE-4: at a measured power of at least 0.80 (F-3, the value) to detect H-LOCAL's own
  predicted effect on these galaxies' e_env, under Gaussian galaxy-mean noise of 0.14926 dex (the whole-table
  between-galaxy sd of the low-acceleration mean residual), the low-acceleration residuals do not fall with the environmental field
  (p_minus >= 0.05); the data favour H-SOURCE, and the low-acceleration misses of GRV-BLIND-2 are not environmental at
  this test's reach."
- EFE-CONFOUNDED: "GRV-EFE-4: residuals fall with the environmental field at low acceleration and also at high
  acceleration, where H-LOCAL predicts almost no effect; the correlation is attributed to a systematic shared with e_env
  and neither reading is favoured."
- EFE-REVERSED: "GRV-EFE-4: low-acceleration residuals rise with the environmental field (p_plus < 0.01), contrary to
  both readings; recorded as an anomaly, neither favoured."
- EFE-OPEN-GAP, EFE-OPEN-COVERAGE, EFE-OPEN-UNDERPOWERED, EFE-INSTRUMENT-OPEN, INCOMPLETE-OPEN: "GRV-EFE-4 did not read
  the question (reason, with the failing number)"; no reading favoured. An UNDERPOWERED rider records F-3's power, so
  the record says how far the real e_env spread is from resolving H-LOCAL's own effect.

Grades and numbers. No form moves a grade (GRV-030 stays Modeled, D1) or any of the five numbers of NORTH_STAR section
2b: no target moves from blocked to derived, no input is retired, no prediction is externally adjudicated (the hold-out
is drawn by a public beacon, which is not an adjudicator). Said plainly: neither progress number moves. Any form does
NOT establish: a mechanism (correlation is not mechanism; section 3's form is H-LOCAL's algebra, not a mesh
derivation); that e_env is the baryonic Newtonian field; that the extractor read the right column (a premise); anything
beyond SPARC; anything about MOND's external field effect as such; anything about the 77 eligible galaxies outside the
hold-out. Bar W is met by the beacon hold-out as written; no form is exploratory.

SECTION 5 LINE: this commission names (c), the discriminator it adjudicates between H-LOCAL and H-SOURCE, the two live
readings of the horizon coupling behind the Gravitational force row's D1 cell (GRV-030); it is target-facing, and it is
the target-facing session section 5 requires after NUC-MIRROR-LEAN-3, the last locked session, which was interior under
the author's named reading of 4 and 5 November 2026.

## 8. NOT ASSUMED

- Not assumed that the effect exists: the published detection used per-galaxy fitted fields under MOND; this test uses
  only e_env and the registered prediction, and the null is live.
- Not assumed that 0.1423 is the galaxy-mean scale: sigma_F is the larger of it and the measured whole-table
  between-galaxy sd of D_g over the 136 low-acceleration galaxies (0.14926, C-9). That sd already contains any true
  Delta variance, so F-3 can only understate power and err toward UNDERPOWERED. Not assumed Gaussian tails: if the
  held-out D carry heavier tails than a Gaussian at sigma_F, power may be overstated, and the rank statistic's robustness
  is the only protection (disclosed).
- Not assumed that three strata remove every acceleration-linked confound; they coarsen it, and P1 is the second guard.
- Not assumed that e_env is the right field for the mesh (LCDM infill); hence Q2 UNDER is a named outcome.
- Not assumed that the extractor's column index is right; carried in every rider.
- No re-run, no alternative cut (0.1 g_dagger is a sub-reading only), no exclusion after the read.
- Priors, stated and not leaned on: the Director expects EFE-OPEN-UNDERPOWERED, then EFE-LOCAL-FAVOURED with Q2 NO-CALL
  (in this design's tokens, Q2 not resolved is EFE-FORM-OPEN). The theorist expects Q1 present if powered (the source
  paper) and then Q2 UNDER, at no better than even odds; the theorist does not know the e_env distribution and so has no
  prior on F-3.

Sub-readings (printed after the forms; change no form; held-out galaxies only): e and D for PGC51017 and UGC04305
against the held-out median e, if drawn (else "not drawn"); S1 on the held-out strict set; S1 with the unstratified
null (to show what the strata changed); the low-acceleration point rms under the registered and the local prediction;
the ten galaxies of largest e with D and Delta.

## 9. AUTONOMY AND COMPUTE

No step waits on a person. The one independent choice, the hold-out, is a beacon draw (section 2); until the manifest
exists the driver exits 2 with BLOCKED. The evidence file is already committed.

Units, one per invocation, checkpoint analysis/grv_efe_4_ckpt.pkl (atomic, resumable): U0 credentials C-0 to C-5, C-7
to C-9 and fixtures X-1 to X-9 (no file under data/sparc_efe/); U1 SPARC residuals D, H, x and the inputs for Delta, whole
table; UH the hold-out (C-6; BLOCKED, exit 2, if no manifest); U2 sealed read (S-1 to S-6 on the whole file; H-1, H-2
on the hold-out; e of held-out galaxies only to the checkpoint, nothing printed, the rest discarded); U3 F-3 (reads e,
Delta, strata; no residual); U4 S1, P1, Q2, sub-readings; terminal line "GRV-EFE-4 COMPLETE: run the verdict". The
verdict script reads only the checkpoint, validates status, units, hashes and finiteness, creates
analysis/GRV-EFE-4_verdict.log with O_EXCL, and renders the instrument line, Q1, Q2 in that order.

Compute, with the arithmetic. Per fixture replicate: F-3 at 100 x 500 = 50,000 stratified permutation correlations, plus
S1 and P1 at 2,000 each, 54,000 in all; X-1 and X-2 at 400 replicates each give 800 x 54,000 = 4.32e7. The scratch ran
exactly this (scratch_design.py, sigma_F, F-3 inside every replicate) in 1,141 s on one core, about 3.8e4 per second.
The evidence adds F-3 at 2,000 x 1,000 = 2e6 (about 53 s at that rate), S1 and P1 at 10,000 each, Q2's 10,000 fits
and X-3 to X-9 (single replicates, X-9's two F-3 calls at 1e5 together): under 2 minutes. Total about 21 cpu minutes;
budget 1 cpu hour (a margin near 3x), under 1 GB, under 90 minutes wall. Had X-1 and X-2 run F-3 at the evidence
count (2 x 400 x 2,000 x 1,000 = 1.6e9) the figure would be about 12 cpu hours, which is why the fixture count is
reduced and its rates measured at that count.

Existing files: tools/holdout_galaxies.py and the lab's beacon tool (the GRV-BLIND-2 path),
benchmarks/gravity/grv_blind_1.py, tools/extract_chae2020_eenv.py, data/sparc_rotmod/, data/sparc_efe/chae2020_eN.csv,
benchmarks/lab/_kit/labkit.py. The worker writes benchmarks/lab/grv_efe_4/driver.py (with core functions in
benchmarks/lab/grv_efe_4/core.py if wanted) and benchmarks/lab/grv_efe_4/verdict.py. GRV-EFE-3's kit files under
benchmarks/lab/grv_efe_3/ (if present) are not imported; the worker may copy code but every function is re-credentialed
here.

## DISCLOSURES (the cures)

- GRV-EFE-3's death, cured. Its F-3 built D_syn = Delta + (the read D permuted across galaxies); in a true H-LOCAL world
  that D already carries Delta, so Delta was added twice and the noise variance became var(Delta) + var(noise); X-1 bar
  (i) could not be met and a real effect would have read as UNDERPOWERED. The cure has three parts. (1) F-3's noise base
  is synthetic and Delta-free: n ~ N(0, sigma_F^2) per galaxy at sigma_F = 0.14926 dex (section 3), and Delta is added to
  it exactly once; F-3 takes no residual as input (C-8 checks this as a property of the code, X-9 on the fixture world
  with D doubled). (2) The S1 and P1 nulls permute e within three acceleration strata and add nothing to D or H (the
  Director's rule). (3) X-1 plants Delta once on the same Delta-free base, with no real residual in it, and must reach
  FAVOURED >= 0.90 before the evidence unit opens; the scratch measures 0.9725 at 400 replicates at sigma_F.
- What the cure costs, stated: F-3's power is now a model statement (Delta-free Gaussian noise at sigma_F), not an
  empirical one from the held-out residual multiset. sigma_F is at least the whole-table between-galaxy sd of the
  low-acceleration mean residual, which already holds any true Delta variance, so F-3 errs toward UNDERPOWERED; if real
  residuals carry heavy tails that a Gaussian lacks, power may be overstated, and the rank statistic's robustness to
  tails is the only protection. Said here, not discovered later.
- GRV-EFE-1's death (the sealed input could not be credentialed in the sandbox) stays cured as in GRV-EFE-3: the
  credential is what the sandbox can check (the file hash written before anyone opened it, the extractor hash, header,
  row range, uniqueness, value range, join); the column identity is a premise in every rider. The author's decline of
  GRV-EFE-DERIVE-2 noted that its data test lacked a credentialed sealed input; this design does not claim more
  credential than that list.
- A count in the record: the parked GRV-EFE-1 draft records the extractor's row count; no bar, halt or fixture here uses
  it, and section 4 discloses that H-1 and H-2 are foregone in practice because of that record.
- Constants are code values recomputed today by scratch_design.py (GRV-EFE-3's scratch files are not in the repository;
  every value it quoted that this design uses was recomputed and agrees), pinned no tighter than the registry's digits
  (C-1, C-2) or at 1e-4 where five or six digits are quoted.
- No evidence was opened while writing this design; scratch_design.py reads only data/sparc_rotmod, code and synthetic e.

Revision 1 (answers to the skeptical review):
- Objection, noise scale asserted as an upper scale, not shown (sections 3 and 8; also the floor_test objection): the
  "upper" wording is removed. scratch_design.py computed, on the public SPARC table only (no file under data/sparc_efe/,
  no draw), the population sd of D_g over the 136 whole-table low-acceleration galaxies: 0.1492612735, above 0.1423. F-3
  and every fixture now use sigma_F = max(0.1423, that sd) = 0.14926 dex, credentialed as new halt-grade item C-9 at
  1e-4 (sections 3, 4, 5). Because the whole-table D_g already holds any true Delta variance, this can only enlarge the
  noise and err toward UNDERPOWERED. X-1 and X-2 were re-measured at sigma_F (section 5): FAVOURED 0.9725, CONFOUNDED
  0.0175, Q2 CARRIES 0.982 among 389, null false-positive rate 0.0075. Bars unchanged (0.90, 0.08, 0.90, 0.03), each
  re-derived from those synthetic rates and binomial sds. The SOURCE-FAVOURED rider now names the 0.14926 dex
  galaxy-mean noise its power is computed under (section 7).
- Objection, budget (section 9; also the budget objection): the second cure was taken. The F-3 inside every X-1 and
  X-2 replicate runs at a named reduced count, 100 replicates x 500 permutations (section 5); the evidence F-3 stays at
  2,000 x 1,000. X-1 bar (i)'s rate was re-measured at that count with F-3 inside every replicate, on synthetic fixtures
  only: 0.9725, none UNDERPOWERED. Section 9 now gives the arithmetic: 800 x 54,000 = 4.32e7 permutation correlations
  measured in 1,141 s on one core, plus under 2 minutes for the evidence units; about 21 cpu minutes, budget 1 cpu hour.
  At the evidence count the fixtures would have cost about 12 cpu hours, stated.
