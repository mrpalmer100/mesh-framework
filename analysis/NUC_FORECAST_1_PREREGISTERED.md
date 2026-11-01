# NUC-FORECAST-1 -- A SEALED FORECAST OF UNMEASURED NUCLEAR MASSES, PRE-REGISTERED (2026-10-31)

Registration document. Committed to the queue branch before the forecast files exist (queue rule 3: the design is
sealed before the instrument is touched). Nothing below changes after this commit; a change is a new name. The
forecast itself is built once by tools/nuc_forecast.py on the author's machine from the pinned AME2020 file and
committed under analysis/forecast/NUC_FORECAST_1/; its hashes are then recorded in the claim.

## 0. Why

NUC-NEW-5 (verdict 8a9b25b; results analysis/NUC_NEW_5_results.md) scored the two frozen adjudicated nuclear mass
models on the 128 AME2020 nuclides absent from AME2012 and rendered BLIND-AGREES and EXTRAPOLATES for both. Its
rider concedes that the blindness of that test rests on the programme's non-inspection of values already
published, which the record cannot externally verify. A forecast of masses that nobody has measured removes that
doubt: the predictions are hashed and committed before the measurements exist, and anyone can check the clock.
The Director's advice memo of 2026-10-31 17:15 proposed this (NUC-FORECAST-NEXT-AME, novel_prediction); the
author directed that it be filed as a sealed registration rather than a commission, because its verdict waits
on a publication, not on the lab, and a job that blocks for years is not a commission.

This is the Weights of atoms row's first prediction of unmeasured quantities. It is not a unique prediction:
standard mass models (FRDM, HFB, WS4 and their successors) are more accurate than a three- or four-term
liquid-drop form, and the forecast discriminates nothing against them. Its value is that its blindness can be
checked from outside.

## 1. The models (frozen; nothing re-fit)

Exactly the models of NUC-BLIND-2 and NUC-NEW-5, byte-bound by NUC-NEW-5's credential C-1 and its run binding:
- M1 (NUC-018): three-term, a_S/a_V = 1.34, a_C = 0.7716 MeV from d0 = 2.026 fm, asymmetry and pairing omitted.
- M2 (NUC-A + NUC-B): four-term, a_S/a_V = 1.108, a_C as M1, a_A = 19.85 MeV, pairing omitted.
Each carries one constant, a_V, calibrated on AME2012's Ca-40 binding B = 342.0521406 MeV (data/ame2012/AME2012.txt,
sha256 88c6272c9e4117d68ac1317e2590c9e376d25f77c9bf68fd6062bbb4e238cb13): a_V = 17.770286909889982 MeV (M1) and
15.987072226683638 MeV (M2), the values recorded in NUC-NEW-5's checkpoint (analysis/nuc_new_5_ckpt.pkl,
records.credential.c1_M1_a_v and c1_M2_a_v). The forecast tool imports the arithmetic from
benchmarks/lab/nuc_new_5/driver.py (a_c, binding, calibrate, ca40_binding_from, prediction_lines) rather than
copying it, and refuses to write anything unless its recomputed a_V equals each recorded value to 1e-12.

## 2. The forecast set F

From the pinned AME2020 table (mass_1.mas20, sha256 e8599c6d7f724fac91934e59f1b9de8fb8f63e820f4b39456b790665ed2a3307,
the file NUC-NEW-1's hold-out was built from): every (Z, N) whose mass excess is from systematics (the '#' flag),
with A = Z + N >= 12, and which is not a row of data/ame2012/AME2012.txt. The tool reads the flag of every row
and the value of none of them; no AME2020 mass value enters the forecast or this document. The set is sorted by
(Z, N), written to labels.txt, counted, and pinned by hash. F is disjoint from the 128 scored by NUC-NEW-5 (those
are experimental rows) and from every AME2012 row (excluded by rule). The tool refuses if any label of F is in
analysis/holdout/NUC_NEW_1/labels.txt or in AME2012.txt, or if the AME2020 file's hash is not the pin.

The counts (|F|, the A < 12 systematics rows excluded, the AME2012 rows excluded) are whatever the file yields;
no band is placed on them. The NUC-NEW-1 build counted 1008 systematics rows in the file; |F| is at most that.

## 3. The files

analysis/forecast/NUC_FORECAST_1/
- labels.txt: "Z N" per line, sorted.
- pred_M1.txt, pred_M2.txt: "Z N B_pred_MeV" per line, six decimals, in the format of NUC-NEW-5's prediction files.
- MANIFEST.json: the pins (ame2020, ame2012, labels, pred_M1, pred_M2 sha256), |F| and the excluded counts, the
  model constants and a_V per model, the rule below verbatim, the registration document's commit, built_at_utc,
  built_by. Written once; the tool refuses to overwrite.
The claim NUC-032 is registered in claims.yaml with these hashes once the files are committed.

## 4. The scoring rule (fixed here; the scoring commission may not change it)

- The adjudicating evaluation E: the first Atomic Mass Evaluation published by the AMDC after the forecast commit
  (AME2024 or later), taken as its mass table file pinned by sha256 in the scoring commission's design. If more
  than one evaluation has appeared, the FIRST one is E; later ones may be scored under a further name.
- The scored set S: every row of F whose mass excess in E is experimental (no '#'). Rows still from systematics are
  not scored and are not failures. No row is added to or removed from F; a label of S not in F is refused.
- Residual per row, the house unit: r = 100 (B_pred - B_truth) / m_atom, B_truth from E's mass excess with the
  constants of NUC-NEW-5's CONFIG (d_h 7.28897059, d_n 8.07131714, m_p 938.272, m_n 939.565, m_e 0.511 MeV).
- Q1 per model, bar W (NORTH_STAR section 2, the bars of NUC-BLIND-1/2 and NUC-NEW-5): rms <= 0.25 and max <= 0.60
  percent of atomic mass on S.
- Q2 per model, the extrapolation ratio of NUC-NEW-5: rho = rms_S / rms_ref with rms_ref the adjudicated in-sample
  rms of NUC-BLIND-2 (0.13799 for M1, 0.01600 for M2, from analysis/holdout/NUC_BLIND_2/VERDICT_M*.json); the
  floor F computed as NUC-NEW-5's design fixes it (bootstrap on the pooled NUC-BLIND-1 + NUC-BLIND-2 residuals,
  seed 20261031, 10000 resamples, 50 against |S|, 99th percentile). Q2 is a fixed rms ratio, not a test of equal
  error distributions.
- Minimum |S| = 30 (NUC-NEW-5's min_rows). Below it every question renders SET-TOO-SMALL and the forecast stays
  armed for the next evaluation.
- Forms: FORECAST-AGREES (Q1 both bars met), FORECAST-FAILS (either bar missed; the numbers kept), FORECAST-INCOMPLETE
  (a row of S without a prediction, which cannot happen if F is unchanged); EXTRAPOLATES (rho <= 2), WITHIN-FLOOR
  (2 < rho <= F), DRIFTS (rho > 2 and rho > F); SET-TOO-SMALL; INSTRUMENT-OPEN (any credential failure). Each form
  is decided by these bars alone.
- The scoring commission: a new name with its own sealed design, on the lab's queue, whose credential C-1 is byte
  equality of its prediction arrays with pred_M1.txt and pred_M2.txt at the hashes in the claim, and whose
  manifest unit refuses if labels.txt's hash is not the pin. It reads E once, after the credential. It is not a
  commission until E exists; nothing waits on a person, and nothing runs until then.

## 5. What counts

- FORECAST-AGREES for a model: a rider on that model's claim (NUC-018; NUC-A and NUC-B): "forecast sealed
  2026-10-31 (NUC-032, analysis/forecast/NUC_FORECAST_1/, pred sha256 ...): scored on the |S| nuclides of the
  forecast set first measured in <E>: rms/max percent of mass, FORECAST-AGREES under bar W; rho against the
  adjudicated in-sample rms; a prediction of quantities unmeasured at the time of the seal, checkable from the
  commit clock." The scorecard row's grade column adds "forecast of unmeasured masses sealed 2026-10-31, scored
  on <E>". A fail is a kept rider with the numbers. No status change either way; the grade stays D3 (Ca-40
  calibration, nucleon mass unit and m_e as inputs) whatever the forms. None of the five North Star numbers
  moves; section 2b (externally adjudicated predictions) is unchanged, since the author built the set and no
  adjudicator holds anything. The AMDC is not an adjudicator of this programme; it is the world.
- Until E exists the claim NUC-032 is a sealed forecast, status Modeled with the grammar FORECAST-SEALED, and
  nothing cites it as evidence for anything.

## 6. Not assumed, not established

- No unique prediction; no discrimination against standard mass models (census T1 unchanged).
- Nothing about which rows of F will be measured first, or where within F the models do better or worse.
- The executor's prior, stated and not leaned on: M2 FORECAST-AGREES; M1 marginal at the most neutron-rich edge
  where the omitted asymmetry term grows (the Director's registered expectation, 2026-10-31).
- The '#' flag is read from the pinned file; a later evaluation may re-flag rows either way. Only E's flags
  decide S.

## 7. Hygiene

No em-dashes. The tool prints hashes and counts and no mass value. The author commits the files with the tool's
output in the commit message. The registration document's commit hash is recorded in MANIFEST.json.
