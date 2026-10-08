# COMMISSION NUC-BLIND-2 -- RESULTS (the PC, 2026-10-08; each verdict computed once; the adjudicator's draw)

Charter: analysis/NUC_BLIND_2_charter_LOCKED.md (locked 2026-10-08 after the adjudicator's draw and before any seal).
Draw: seed 1969 chosen by and drawn by mike (not the author, not the commission), 50 of 2397 eligible AME2012 rows,
Ca-40 excluded; test sha256 ca176a47...; train sha256 97b69011.... Predictions: benchmarks/nuclear/nuc_blind_1.py
NUC_BLIND_2 (the hold-out name the one change; models, calibration and arithmetic identical to NUC-BLIND-1),
sealed M1 edb67e24..., M2 a5f3f8e0... before the truth was read. Verdicts on the PC, --unit mass, bars rms <= 0.25
and max <= 0.60 percent of mass; VERDICT_M1.json and VERDICT_M2.json kept under analysis/holdout/NUC_BLIND_2/.
Verdict log: analysis/NUC_BLIND_2_verdict.log.

## VERDICTS: M1 BLIND-AGREES; M2 BLIND-AGREES (externally adjudicated)

| model | form | rms (% of mass) | max abs (% of mass) | worst rows (+: overbound by the model) | sub-reading (N5) |
|---|---|---|---|---|---|
| M1 NUC-018 three-term (a_S/a_V 1.34, a_C 0.7716, a_V 17.770; asymmetry and pairing omitted) | BLIND-AGREES | 0.1380 | 0.2271 | Cd-130 +0.227, Sr-102 +0.219, Pu-246 +0.219, I-140 +0.212, Y-103 +0.206 | corr(residual, 23 (N-Z)^2/A) = +0.829 |
| M2 LAMED baseline four-term (a_S/a_V 1.108, a_C 0.7716, a_A 19.85 derived, a_V 15.987; pairing omitted) | BLIND-AGREES | 0.0160 | 0.0350 | Mg-31 +0.035, Na-26 +0.035, P-39 +0.032, P-37 +0.031, O-14 -0.030 | corr(residual, pairing indicator) = -0.221 |

50 of 50 rows predicted by both models. Against NUC-BLIND-1 (the author's draw): M1 0.121/0.219 there, 0.138/0.227
here; M2 0.011/0.026 there, 0.016/0.035 here. The two draws agree with each other to the second digit, which is what
two independent samples of the same residual distribution should do; mike's draw happened to include more light
neutron-rich rows (Na-26, Mg-31, P-37/39), where M2's smooth form is weakest, and the numbers moved accordingly and
stayed an order of magnitude inside the bars.

## What the result is

Under charter B-6, locked before the draw: the programme's first externally adjudicated prediction. Both
pre-registered models predicted the masses of 50 isotopes chosen by someone who is not the author, with one constant
calibrated on Ca-40, inside the registered accuracy, and the person who chose them is named. Section 2b's
"externally adjudicated predictions" moves from 0 to 1 (one adjudicated confrontation; both models pass it; the
count is of adjudicated predictions, not of models, and stays 1). The sub-reading repeats NUC-BLIND-1's: M1's
residual is the declared asymmetry omission (corr +0.83), M2's is not pairing-shaped (corr -0.22) and is largest on
the lightest neutron-rich rows, where a liquid-drop form has no shell or zero-point term to lean on.

What this does not do. Grade D3 on the scorecard row stands: the row is still a calibrated reconstruction with one
fitted constant, now blind-scored twice and adjudicated once. It does not touch the nucleon mass unit or m_e as
inputs, the He-4 miss, or the m_p/m_e gate (FND-MATTER-066). It is one adjudicated confrontation in the matter
sector, not a prediction of a new number nature has not yet measured; PRED-003 remains the programme's only firm T1
prediction of that kind. The draw was run on the author's PC by the adjudicator; a stronger adjudication would have
the adjudicator hold the sealed file on his own machine, which costs nothing and is named below.

## Consequences (on the author's word)

NUC-018: rider "externally adjudicated 2026-10-08 (NUC-BLIND-2, draw by mike, seed 1969): BLIND-AGREES at rms 0.138
  and max 0.227 percent of mass on 50 held-out AME2012 isotopes; residual 0.83 correlated with the declared asymmetry
  omission; the second blind pass, the first adjudicated."
NUC-A and NUC-B: rider "the derived a_A = 19.85 MeV externally adjudicated 2026-10-08 (NUC-BLIND-2, draw by mike):
  BLIND-AGREES at rms 0.016 and max 0.035 percent of mass on 50 held-out isotopes; residual not pairing-shaped."
docs/NORTH_STAR.md section 2b: "Externally adjudicated predictions" 0 -> 1 (NUC-BLIND-2; adjudicator mike; both
  pre-registered models pass; the k-string self-adjudication still does not count); section 1 row "Weights of
  atoms" grade column: "blind-scored twice, externally adjudicated once (NUC-BLIND-2)".
docs/STRATEGIC_TARGETS.md section AE: closed with the adjudicated result.
No status change on any claim; the release note for 3.33 says which number moved and why.

## Named next-order (not chartered)

NUC-BLIND-3, only if the author wants the adjudication stronger rather than repeated: the adjudicator draws and
KEEPS the sealed test file on his own machine, receives the sealed prediction files, and runs the verdict himself;
the author never holds the truth. Same models, same bars. Otherwise the blind line of this row is finished: a third
draw of the same two models would add a digit, not a fact. The row's next real question is not blind-scoring but
the He-4 and O-16 class of misses (shell and zero-point), which is a different commission.
