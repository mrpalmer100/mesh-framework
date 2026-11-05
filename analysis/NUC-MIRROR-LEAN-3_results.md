# NUC-MIRROR-LEAN-3: results write-up (revision 2)

Verdict rendered once, 2026-11-05 (analysis/NUC-MIRROR-LEAN-3_verdict.lock: 2026-11-05 06:44:43-0500), from sealed data. Form: **U-MISS-HIGH** (Q1).

Files, so the names cannot be confused. This task may write only to analysis/NUC-MIRROR-LEAN-3_results.md (hyphens), so the write-up keeps that path; the reviewers' separate-name request could not be met by a rename, and it is met here by labelling. THIS file is the account. The kit's one-shot file, with the per-pair table and the fixture record, is analysis/NUC_MIRROR_LEAN_3_results.md (underscores) and is cited below only as "the kit results file".
- Governing charter, as locked: analysis/NUC-MIRROR-LEAN-3_charter_LOCKED.md (same byte size as the draft, 16701; the quotations below are from the charter text as given in the commission).
- Sealed design: analysis/NUC_MIRROR_LEAN_3_design_SEALED.md (commit 361340c). Section 7 is the "WHAT COUNTS" wording quoted verbatim in section 6 below.
- Verdict output: analysis/NUC-MIRROR-LEAN-3_verdict.log (four lines).
- Interior work under NORTH_STAR section 5 (the one interior session permitted after NUC-NEW-5, promoted as NUC-031).

## 1. What was asked

Q1, the only question: does the registered uniform-sphere Coulomb term, a_C = 0.7716 MeV on Z^2/A^(1/3) from d0 = 2.026 fm (NUC-018, NUC-017) with no constant fitted to any mass, reproduce the Coulomb displacement energies of the AME2012 T = 1/2 mirror pairs at A >= 13, as they stand in the pinned table, to within the coefficient's own registered offset B1 = 0.085 (a_c()/0.711 - 1 to three figures, NUC-018's comparison of the derived 0.772 with the empirical SEMF 0.711)?

Why this channel (design section 0): for a T = 1/2 mirror pair at odd A, the volume, surface and symmetry terms of the registered models (NUC-018 three-term; NUC-A plus NUC-B four-term) are identical for the two members and there is no pairing term, so the binding difference is a_C A^(2/3) alone. Credential C-2 verifies this identity on the sealed code (worst deviation 3.0e-14 MeV, from the verdict log). The channel model is CDE_U(A) = a_c() A^(2/3), a_c() = 0.7716295256894924 MeV. The measured channel is CDE_meas = (d_n - d_h) + M(Z_p, Z_p - 1) - M(Z_p - 1, Z_p), Z_p = (A + 1)/2.

## 2. What was computed

- Evidence set (deterministic rule, no draw): every odd A >= 13 for which both rows (Z_p, Z_p - 1) and (Z_p - 1, Z_p) are present in data/ame2012/AME2012.txt (sha256 88c6272c9e4117d68ac1317e2590c9e376d25f77c9bf68fd6062bbb4e238cb13, the NUC-NEW-5 pin). Result: n = 31 pairs, A = 13 to 75. The per-pair table in the kit results file lists A = 13 to 71 at every odd value (30 pairs) and A = 75; A = 73 is not in the set. Why A = 73 is absent was not computed; the rule is presence-only.
- Predictions were written and sealed before the table was opened: analysis/NUC_MIRROR_LEAN_3_pred.txt, sha256 51c713ba12657100c0b4eb7fa84b92b411baa766c7b699b90ac7ae8e712a599a (the verdict log prints the first 16 hex digits, 51c713ba12657100; the kit results file prints the full hash).
- Statistic: delta_i = CDE_U(A_i)/CDE_meas,i - 1 (positive means the sphere overshoots the pinned-table value). Decision statistic: mean_delta, equal weight per pair.

## 3. Numbers (verdict log and the kit results file)

| quantity | value |
|---|---|
| n | 31 |
| mean_delta | +0.246423 |
| rms_delta | 0.256005 |
| min delta | +0.168872 (A = 69) |
| max delta | +0.439992 (A = 17) |
| diagnostic mean with Z(Z - 1) in place of Z^2 (no form) | +0.208843 |
| h_boot (seed 20261104, 10000 pair bootstraps, 99.0th percentile) | 0.032841 |
| h_inst (0.100 MeV sqrt 2 / CDE_U(13) / sqrt n) | 0.005954 |
| floor h = max(h_boot, h_inst) | 0.032841 |
| band B1 | 0.085 |
| mean - h | +0.21358 |
| mean + h | +0.27926 |
| sign_resolved (\|mean\| > h; decides nothing) | True |

Rule applied in the locked order: (1) h > B1? No (0.03284 < 0.085), so not U-NULL-FLOOR. (2) |mean| + h <= B1? No (0.27926 > 0.085), so not U-AGREES. (3) mean - h > B1? Yes (+0.21358 > 0.085): U-MISS-HIGH.

Floor test (house discipline 5), read against the band edge as the design requires: h = 0.03284 is below B1 = 0.085, and the lower end of the floor-widened interval (+0.21358) lies above B1 by 0.12858. The effect is not floor-bound. The recorded minimum single-pair delta (+0.169, A = 69) is also above B1; this is one of the locked recorded statistics and is reported as such, not as a trend or a per-pair verdict.

Instrument record. What the verdict log shows directly: C-1 ok and C-2 worst 3.0e-14; the table sha256 equal to the pin; the prediction hash printed; a rendered FORM line other than INSTRUMENT-OPEN. What the kit results file (lines 47 and 48) records directly: "C-1, C-2, C-3 (F1 to F5 and T4), C-4, C-5, C-6 all passed (the driver halts otherwise)", and the fixture record F1 U-MISS-HIGH (mean 0.111111), F2 U-AGREES (0.0), F3 U-MISS-LOW (-0.166667), F4 U-OPEN-BAND (0.08), F5 U-NULL-FLOOR (0.25), T4 "C-5 halt, 0 mass conversions". That C-4, C-5 and C-6 passed in the evidence run therefore rests on the kit's own record plus the fact that a halt would have rendered INSTRUMENT-OPEN. This write-up did not open the checkpoint and did not rerun any unit.

## 4. What this establishes

- The registered uniform-sphere term a_C A^(2/3) with a_C = 0.7716 MeV exceeds the CDE_meas values formed from the pinned AME2012 table at A = 13 to 75 by a mean fractional amount of +0.246 (+24.6%; equal weight per pair; rms 0.256), with the whole floor-widened interval (+0.214 to +0.279) above the registered band B1 = 0.085. The charter does not assume every pinned row is experimental (the pin is the hash), so this is a comparison with the pinned table values; it is not a verified statement about the experimental status of each of the 31 pairs.
- Two different quantities are on the page and no ratio is drawn between them. B1 = 0.085 is the offset of the derived coefficient a_C = 0.772 from the empirical SEMF coefficient 0.711, itself a whole-table fit. The +0.246 is a fractional miss of the term on a single channel against the pinned table. The sealed wording states the relation: the cell's "+9%" is a coefficient comparison and this is the term's own miss.
- The predictions were frozen and hash-bound before the table was read, with no constant in CDE_U that could be fitted afterwards (bar W met by construction, as NUC-NEW-5 met it, under the NORTH_STAR section 5 reading recorded for this commission).
- The Z(Z - 1) diagnostic line (CDE_U (1 - 1/A) in place of CDE_U) has mean +0.208843. It is one diagnostic line with no form and is reported as a number only.

## 5. What this does not establish

- The cause of the miss. Candidates, listed without preference: the uniform-sphere self-energy form (Z^2 against Z(Z - 1)); the diffuseness and exchange corrections of NUC-C (no code in the repository, not scored); coherent charge-symmetry breaking of the nuclear force (part of the measured channel and not in the floor, per the charter and design section 4); and, named by design section 7 and not by the charter, the odd nucleon's orbit. The locked statistics do not separate any of these, and none is scored here. Correlation is not mechanism.
- Any trend in A. No trend statistic was locked. The per-pair table is in the kit results file; the equal-weight mean says nothing about light-A against heavy-A behaviour.
- Anything about A < 13, T = 1 or 3/2 multiplets, A > 75 (no pair beyond A = 75 passed the presence rule), or the mass models' absolute accuracy. NUC-BLIND-1, NUC-BLIND-2 and NUC-NEW-5 are absolute-mass scores and are not changed.
- That every pinned AME2012 row is an experimental value (charter, NOT ASSUMED). The scored quantity is the pinned table's.
- The floor h_inst treats the 2n mass errors as independent with a 0.100 MeV tolerance class, not a per-mass standard deviation; the file has no uncertainty column. The verdict is decided by h_boot, the larger floor.
- The blindness of the channel rests on the programme's non-formation of these differences, which the record cannot externally verify (design section 2 and DISCLOSURES 1). The defence is the construction (frozen function, sealed before the read, hash-bound), not the order of reading.
- Not a T1 prediction (AME2012 predates the model). Not externally adjudicated.

## 6. Scorecard and the registered wording

Weights of atoms row, Coulomb cell: grade D2 unchanged under every form (design section 7).

Rider on NUC-018 and cell text, design section 7, with the fields filled: date 2026-11-05, n = 31, X = +0.246 (+24.6%), Y = 0.256, h = 0.033. The sealed template, verbatim from analysis/NUC_MIRROR_LEAN_3_design_SEALED.md section 7:

> U-AGREES (the sentence the miss entry reuses): "NUC-MIRROR-LEAN-3 (date, analysis/NUC_MIRROR_LEAN_3_results.md): the derived uniform-sphere Coulomb term, a_C = 0.7716 MeV from d0 = 2.026 fm with no constant fitted to a mass, scored on the n AME2012 T = 1/2 mirror displacement energies at A >= 13, the channel in which the calibrated bond depth, the surface term and the symmetry term cancel exactly, the predictions sealed before the table was read: mean fractional miss X, rms Y (floor h); the floor-widened interval |X| + h lies inside the coefficient's registered 8.5 percent band B1; U-AGREES. X is an equal-weight average over the pairs and says nothing about the light-A versus heavy-A behaviour, which this commission does not read; the measured displacement energies carry whatever charge-symmetry breaking nature puts in them, unadjudicated here. The channel's blindness rests on the programme's non-formation of the differences, which the record cannot externally verify. Grade D2 unchanged."
>
> U-MISS-HIGH / U-MISS-LOW: "the same sentence with "mean fractional miss X, rms Y (floor h); the whole floor-widened interval lies outside the registered 8.5 percent band; U-MISS-<HIGH/LOW>: on the calibration-free channel the uniform sphere <overshoots/undershoots> the measured displacement energies by X; the cell's '+9%' is a coefficient comparison and this is the term's own miss. Grade D2 unchanged." The cell's text gains "(mirror channel: X)". Kept at full weight; never re-chartered to rescue it.

The rider with X filled in (the miss entry's middle clause substituted into the U-AGREES sentence; the equal-weight, charge-symmetry-breaking and non-formation sentences are carried because the design says "the same sentence"). The same text appears in analysis/lab/drafts/NUC-MIRROR-LEAN-3/claim_1.yaml:

> "NUC-MIRROR-LEAN-3 (2026-11-05, analysis/NUC_MIRROR_LEAN_3_results.md): the derived uniform-sphere Coulomb term, a_C = 0.7716 MeV from d0 = 2.026 fm with no constant fitted to a mass, scored on the 31 AME2012 T = 1/2 mirror displacement energies at A >= 13, the channel in which the calibrated bond depth, the surface term and the symmetry term cancel exactly, the predictions sealed before the table was read: mean fractional miss +0.246, rms 0.256 (floor 0.033); the whole floor-widened interval lies outside the registered 8.5 percent band; U-MISS-HIGH: on the calibration-free channel the uniform sphere overshoots the measured displacement energies by +0.246; the cell's '+9%' is a coefficient comparison and this is the term's own miss. +0.246 is an equal-weight average over the pairs and says nothing about the light-A versus heavy-A behaviour, which this commission does not read; the measured displacement energies carry whatever charge-symmetry breaking nature puts in them, unadjudicated here. The channel's blindness rests on the programme's non-formation of the differences, which the record cannot externally verify. Grade D2 unchanged."

Cell text, sealed form with X filled: "(mirror channel: +0.246)", that is +24.6%, appended to the cell's "(+9%)".

Scope qualifier, the writer's addition and not sealed text, to travel with the rider and the cell line: "+0.246 is scored against the pinned AME2012 table values (sha256 88c6272c...cb13); the design does not assume every pinned row is experimental."

(The sealed rider text cites the kit's file analysis/NUC_MIRROR_LEAN_3_results.md as its source for the per-pair table; that is the kit file, not this write-up.)

Targets moved from blocked to derived: 0. Inputs retired: 0. Discriminators armed: 0. The five numbers of NORTH_STAR 2b do not move. This is reconstruction work on a target row; the registered consequence is a kept miss, not progress. By NORTH_STAR section 5 the session after this one must be target-facing.

## 7. No-rescue note

Per the charter's no-rescue rule: no pair was excluded for its residual, no regional re-scoring was done, and no amended term is scored under this name. The miss is kept at full weight on the Coulomb cell. Any follow-up that scores a different term (for example a diffuseness or exchange-corrected form, or the Z(Z - 1) form) or reads the A-dependence asks a different question, needs its own name, sealed design and locked bars, and cannot be presented as a repair of this verdict.

## 8. Natural next question

This verdict does not choose among the candidate causes in section 5, and this document states no preference among them. Two constraints bind whatever follows. (a) NORTH_STAR section 5: the session after NUC-MIRROR-LEAN-3 must be target-facing, so an interior follow-up on this channel cannot be that session; the lab selects the next target-facing commission itself, under that section, and promotion of any result is a separate step. (b) The 31 pairs have now been read: a different term scored on the same pairs would be in-sample for that term and could only be read as such, and a candidate that needs code (NUC-C has none in the repository) would need a credentialed instrument and a design sealed before any re-read.

## Review record (written by the lab)

| Stage | Reviewer | Model | Result |
|---|---|---|---|
| lock r1 | skeptical | anthropic/claude-opus-5-5 | pass |
| lock r1 | external | openai/gpt-6-astra | pass |
| verdict r1 | skeptical | anthropic/claude-opus-5-5 | not passed |
| verdict r1 | external | openai/gpt-6-astra | not passed |
| verdict r1 | skeptical | anthropic/claude-opus-5-5 | pass |
| verdict r1 | external | openai/gpt-6-astra | pass |
