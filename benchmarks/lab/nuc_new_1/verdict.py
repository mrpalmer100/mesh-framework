"""COMMISSION NUC-NEW-1 -- verdict: reads the checkpoint only, through labkit.Verdict. Renders once.

Questions (design analysis/NUC_NEW_1_design_SEALED.md section 6), one FORM line each:
  Q1-M1, Q1-M2   BLIND-AGREES (rms <= 0.25 and max <= 0.60 percent of mass) / BLIND-FAILS / BLIND-INCOMPLETE
  Q2-M1, Q2-M2   EXTRAPOLATES (rms <= 2 x the model's NUC-BLIND-2 adjudicated rms, read from VERDICT_M*.json by the
                 driver's credential unit) / DRIFTS
  NEW-SET-TOO-SMALL on every question when the set has fewer than 30 rows; INSTRUMENT-OPEN when the harness could not
  evaluate. Q3 (the pre-registered sub-reading: correlations of the residual with the declared omission channels) is
  published as text, bears no form, and is computed only after the Q1/Q2 tokens are decided.
Every statistic is recomputed here from the sealed rows (Z, N, pred, truth excess) with the driver's residual rule, and
the driver's stored residual must agree to 1e-9; nothing is read from any file but the checkpoint.
"""
import pathlib
import sys

import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from benchmarks.lab._kit import labkit as K                                     # noqa: E402
from benchmarks.lab.nuc_new_1.driver import SLUG, NAME, MANIFEST, CONFIG, UNITS, residual_mass   # noqa: E402

COMMISSION = 'NUC-NEW-1'
FORMS = ['BLIND-AGREES', 'BLIND-FAILS', 'BLIND-INCOMPLETE', 'EXTRAPOLATES', 'DRIFTS', 'NEW-SET-TOO-SMALL', 'INSTRUMENT-OPEN']
QUESTIONS = ['Q1-M1', 'Q1-M2', 'Q2-M1', 'Q2-M2']


def pearson(x, y):
    x, y = np.asarray(x, float), np.asarray(y, float)
    if len(x) < 3 or np.std(x) == 0 or np.std(y) == 0:
        return float('nan')
    return float(np.corrcoef(x, y)[0, 1])


def form_rule(ck, out):
    rec = ck.state['records']
    n_test = int(rec['manifest']['n_test'])
    out.append(f"{COMMISSION}: {n_test} nuclides measured between AME2012 and AME2020 (A >= 12; run by {rec['manifest']['run_by']}; "
               f"ame2020 sha256 {rec['manifest']['ame2020_sha256'][:16]}...; truth {rec['truth']['mode']})")
    out.append(f"credential: C-1 {rec['credential']['c1']}, C-2 {rec['credential']['c2']}, C-3 {rec['credential']['c3']}, "
               f"C-4 {rec['manifest']['c4']}, C-5 {rec['manifest']['c5']}; a_C {rec['predict']['a_c']:.4f} MeV; "
               f"a_V M1 {rec['predict']['M1_a_v']:.4f}, M2 {rec['predict']['M2_a_v']:.4f} (Ca-40, AME2012)")
    min_rows = 1 if ck.smoke else CONFIG['min_rows']          # the smoke's throwaway set is five planted rows
    if n_test < min_rows:
        return [(q, 'NEW-SET-TOO-SMALL', f'{n_test} rows, fewer than {CONFIG["min_rows"]}') for q in QUESTIONS]
    decisions, stats = [], {}
    for label in ('M1', 'M2'):
        rows = ck.sealed(f'rows_{label}')
        missing = ck.sealed(f'missing_{label}')
        K.require(rows.shape[0] + missing.shape[0] == n_test, f'{label}: sealed rows plus missing do not account for the set')
        res = []
        for z, n, pred, exc, r_stored in rows:
            r, _ = residual_mass(int(z), int(n), pred, exc)
            K.require(abs(r - r_stored) < 1e-9, f'{label}: verdict recomputation disagrees with the driver record')
            res.append(r)
        res = np.array(res)
        K.finite_array(res, f'{label} residuals')
        rms, mx = float(np.sqrt(np.mean(res ** 2))), float(np.max(np.abs(res)))
        ref = float(rec['credential'][f'c2_{label}_rms_ref'])
        q2_bar = CONFIG['extrap_factor'] * ref
        stats[label] = (rows, res, rms, mx, ref, q2_bar)
        if missing.shape[0] > 0:
            tok1, why1 = 'BLIND-INCOMPLETE', f'{missing.shape[0]} of {n_test} rows unpredicted'
        elif rms <= CONFIG['bar_rms'] and mx <= CONFIG['bar_max']:
            tok1, why1 = 'BLIND-AGREES', f'rms {rms:.4f} <= {CONFIG["bar_rms"]} and max {mx:.4f} <= {CONFIG["bar_max"]} percent of mass on {len(res)} rows'
        else:
            tok1, why1 = 'BLIND-FAILS', f'rms {rms:.4f} (bar {CONFIG["bar_rms"]}), max {mx:.4f} (bar {CONFIG["bar_max"]}) percent of mass on {len(res)} rows'
        if rms <= q2_bar:
            tok2, why2 = 'EXTRAPOLATES', f'rms {rms:.4f} <= {q2_bar:.4f} (2 x the adjudicated in-sample rms {ref:.4f})'
        else:
            tok2, why2 = 'DRIFTS', f'rms {rms:.4f} > {q2_bar:.4f} (2 x the adjudicated in-sample rms {ref:.4f}); ratio {rms / ref:.2f}'
        decisions += [(f'Q1-{label}', tok1, why1), (f'Q2-{label}', tok2, why2)]
    # published after the tokens are decided: the table and the pre-registered sub-reading (no form)
    for label in ('M1', 'M2'):
        rows, res, rms, mx, ref, q2_bar = stats[label]
        out.append(f'{label}: rms {rms:.4f}, max {mx:.4f} percent of mass on {len(res)} rows (in-sample adjudicated {ref:.4f} / '
                   f'{rec["credential"][f"c2_{label}_max_ref"]:.4f}); ratio of rms {rms / ref:.2f}')
        order = np.argsort(-np.abs(res))[:5]
        out.append(f'{label} worst five (+: overbound by the model): ' + ', '.join(
            f'Z={int(rows[i, 0])} N={int(rows[i, 1])} {res[i]:+.4f}' for i in order))
        Z, N = rows[:, 0], rows[:, 1]
        A = Z + N
        m_atom = Z * CONFIG['m_p'] + N * CONFIG['m_n'] + Z * CONFIG['m_e'] - (Z * CONFIG['d_h'] + N * CONFIG['d_n'] - rows[:, 3])
        asym = CONFIG['asym_coeff'] * (N - Z) ** 2 / A / m_atom * 100.0
        quart = (N - Z) ** 4 / A ** 3 / m_atom * 100.0
        pair = np.where((Z % 2 == 0) & (N % 2 == 0), 1.0, np.where((Z % 2 == 1) & (N % 2 == 1), -1.0, 0.0))
        if label == 'M1':
            out.append(f'Q3 M1 (informative): corr(residual, 23 (N-Z)^2/A) = {pearson(res, asym):+.3f} (in-sample +0.83)')
        else:
            out.append(f'Q3 M2 (informative): corr(residual, (N-Z)^4/A^3) = {pearson(res, quart):+.3f}; '
                       f'corr(residual, pairing indicator) = {pearson(res, pair):+.3f} (in-sample -0.22)')
    return decisions


if __name__ == '__main__':
    v = K.Verdict(ROOT, SLUG, COMMISSION, [u for u, _ in UNITS], MANIFEST, FORMS, open_form='INSTRUMENT-OPEN',
                  config=CONFIG, questions=QUESTIONS)
    sys.exit(v.render(form_rule))
