"""COMMISSION NUC-NEW-3 -- verdict: reads the checkpoint only, through labkit.Verdict. Renders once.

Questions (design analysis/NUC_NEW_3_design_SEALED.md section 6), one FORM line each:
  Q1-M1, Q1-M2   BLIND-AGREES (rms <= 0.25 and max <= 0.60 percent of mass) / BLIND-FAILS / BLIND-INCOMPLETE
  Q2-M1, Q2-M2   BLIND-INCOMPLETE if any label is unpredicted; else on rho = rms / rms_ref (rms_ref the model's
                 NUC-BLIND-2 adjudicated rms, read from its VERDICT file by the credential unit):
                 EXTRAPOLATES rho <= 2; WITHIN-FLOOR 2 < rho <= F; DRIFTS rho > 2 and rho > F,
                 F the sampling floor the credential unit recorded before any evidence file was opened.
  NEW-SET-TOO-SMALL on every question when the set has fewer than 30 rows (cannot render: |T| = 128 is pinned);
  INSTRUMENT-OPEN when the harness could not evaluate.
Binding, before any statistic: the sealed rows plus the missing labels equal the sealed label set (unique, disjoint);
each scored prediction equals its sealed prediction to 1e-9; each truth excess equals the sealed raw payload's; the
residual recomputed here equals the driver's record to 1e-9. Q3 (the pre-registered sub-reading) is printed with a
permutation null after the tokens are decided; it bears no form and no claim, and no rider may quote it.
"""
import pathlib
import sys

import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from benchmarks.lab._kit import labkit as K                                     # noqa: E402
from benchmarks.lab.nuc_new_3.driver import SLUG, NAME, MANIFEST, CONFIG, UNITS, residual_mass   # noqa: E402

COMMISSION = 'NUC-NEW-3'
FORMS = ['BLIND-AGREES', 'BLIND-FAILS', 'BLIND-INCOMPLETE', 'EXTRAPOLATES', 'WITHIN-FLOOR', 'DRIFTS', 'NEW-SET-TOO-SMALL',
         'INSTRUMENT-OPEN']
QUESTIONS = ['Q1-M1', 'Q1-M2', 'Q2-M1', 'Q2-M2']
NO_CLAIM = 'Q3 carries no claim; no rider may quote it'


def pearson(x, y):
    x, y = np.asarray(x, float), np.asarray(y, float)
    if len(x) < 3 or np.std(x) == 0 or np.std(y) == 0:
        return float('nan')
    return float(np.corrcoef(x, y)[0, 1])


def perm_null(x, y, rng):
    """|r| under label permutation of x: the null's 99th percentile and the percentile of the observed |r| in it."""
    r_obs = abs(pearson(x, y))
    null = np.array([abs(pearson(rng.permutation(x), y)) for _ in range(CONFIG['q3_permutations'])])
    null = null[np.isfinite(null)]
    if not np.isfinite(r_obs) or null.size == 0:
        return r_obs, float('nan'), float('nan')
    return r_obs, float(np.percentile(null, CONFIG['q3_percentile'])), float(100.0 * np.mean(null < r_obs))


def bind(ck, label, labels_set, truth):
    """The sealed rows for a model, bound to the seals; returns (rows, residuals, missing_count)."""
    rows = ck.sealed(f'rows_{label}')
    missing = ck.sealed(f'missing_{label}')
    labels = [tuple(int(v) for v in row) for row in ck.sealed('labels')]
    preds = ck.sealed(f'pred_{label}')
    pm = dict(zip(labels, preds.tolist()))
    scored = [(int(r[0]), int(r[1])) for r in rows]
    miss = [(int(r[0]), int(r[1])) for r in missing]
    K.require(len(set(scored)) == len(scored) and len(set(miss)) == len(miss), f'{label}: duplicate label among the scored or missing rows')
    K.require(not (set(scored) & set(miss)), f'{label}: a label is both scored and missing')
    K.require(set(scored) | set(miss) == labels_set and len(scored) + len(miss) == len(labels_set),
              f'{label}: scored plus missing rows are not exactly the sealed label set')
    res = []
    for z, n, pred, exc, r_stored in rows:
        zn = (int(z), int(n))
        K.require(abs(pred - pm[zn]) < CONFIG['bind_tol'], f'{label}: a scored prediction differs from the sealed prediction at Z={zn[0]} N={zn[1]}')
        K.require(abs(exc - truth[zn]) < CONFIG['bind_tol'], f'{label}: a truth excess differs from the sealed raw payload at Z={zn[0]} N={zn[1]}')
        r, _ = residual_mass(zn[0], zn[1], pred, exc)
        K.require(abs(r - r_stored) < CONFIG['bind_tol'], f'{label}: verdict recomputation disagrees with the driver record')
        res.append(r)
    return rows, np.array(res), len(miss)


def form_rule(ck, out):
    rec = ck.state['records']
    n_test = int(rec['manifest']['n_test'])
    out.append(f"{COMMISSION}: {n_test} nuclides first measured between AME2012 and AME2020 (A >= 12; hold-out built by "
               f"{rec['manifest']['run_by']}; ame2020 sha256 {rec['manifest']['ame2020_sha256'][:16]}...; truth {rec['truth']['mode']})")
    out.append(f"credential: C-1 {rec['credential']['c1']}, C-2 {rec['credential']['c2']}, C-3 {rec['credential']['c3']}, "
               f"C-4 {rec['manifest']['c4']}, C-5 {rec['manifest']['c5']}, C-6 {rec['manifest']['c6']} (shared rows "
               f"{rec['manifest']['audit']['shared']}, beyond {CONFIG['audit_tol_MeV']} MeV: {rec['manifest']['audit']['beyond']}, largest shift "
               f"{rec['manifest']['audit']['max_abs_shift_MeV']:.3f} MeV); "
               f"a_C {rec['predict']['a_c']:.4f} MeV; a_V M1 {rec['predict']['M1_a_v']:.4f}, M2 {rec['predict']['M2_a_v']:.4f} (Ca-40, AME2012)")
    min_rows = 1 if ck.smoke else CONFIG['min_rows']          # the smoke's throwaway set is five planted rows
    if n_test < min_rows:
        return [(q, 'NEW-SET-TOO-SMALL', f'{n_test} rows, fewer than {CONFIG["min_rows"]}') for q in QUESTIONS]
    # binding to the seals, before any statistic
    labels_set = {tuple(int(v) for v in row) for row in ck.sealed('labels')}
    K.require(len(labels_set) == n_test, 'the sealed labels are not unique or not n_test')
    traw = ck.sealed('truth_raw')
    truth = {(int(z), int(n)): float(m) for z, n, m in traw}
    K.require(set(truth) == labels_set and traw.shape[0] == n_test, 'the sealed raw truth does not cover the sealed labels exactly')
    decisions, stats = [], {}
    for label in ('M1', 'M2'):
        rows, res, n_missing = bind(ck, label, labels_set, truth)
        ref = float(rec['credential'][f'c2_{label}_rms_ref'])
        F = float(rec['credential'][f'floor_{label}'])
        if n_missing > 0:
            why = f'{n_missing} of {n_test} rows unpredicted; no statistic on the remainder'
            decisions += [(f'Q1-{label}', 'BLIND-INCOMPLETE', why), (f'Q2-{label}', 'BLIND-INCOMPLETE', why)]
            stats[label] = None
            continue
        K.finite_array(res, f'{label} residuals')
        rms, mx = float(np.sqrt(np.mean(res ** 2))), float(np.max(np.abs(res)))
        rho = rms / ref
        stats[label] = (rows, res, rms, mx, ref, F, rho)
        if rms <= CONFIG['bar_rms'] and mx <= CONFIG['bar_max']:
            tok1, why1 = 'BLIND-AGREES', f'rms {rms:.4f} <= {CONFIG["bar_rms"]} and max {mx:.4f} <= {CONFIG["bar_max"]} percent of mass on {len(res)} rows'
        else:
            tok1, why1 = 'BLIND-FAILS', (f'rms {rms:.4f} (bar {CONFIG["bar_rms"]}), max {mx:.4f} (bar {CONFIG["bar_max"]}) percent of mass on {len(res)} rows'
                                         + ('; the max bar was fixed for 50-row samples and is applied unchanged to these rows' if rms <= CONFIG['bar_rms'] else ''))
        two = CONFIG['extrap_factor']
        if rho <= two:
            tok2, why2 = 'EXTRAPOLATES', f'rho {rho:.3f} <= {two} (rms {rms:.4f} / adjudicated in-sample {ref:.4f}); floor F {F:.3f}'
        elif rho <= F:
            tok2, why2 = 'WITHIN-FLOOR', f'rho {rho:.3f} > {two} but <= the sampling floor F {F:.3f} (99th percentile of the bootstrap ratio)'
        else:
            tok2, why2 = 'DRIFTS', f'rho {rho:.3f} > {two} and > the sampling floor F {F:.3f} (rms {rms:.4f} / adjudicated in-sample {ref:.4f})'
        decisions += [(f'Q1-{label}', tok1, why1), (f'Q2-{label}', tok2, why2)]
    # published after the tokens are decided: the table and the sub-reading (no form, no claim)
    rng = np.random.default_rng(CONFIG['q3_seed'])
    for label in ('M1', 'M2'):
        if stats[label] is None:
            continue
        rows, res, rms, mx, ref, F, rho = stats[label]
        out.append(f'{label}: rms {rms:.4f}, max {mx:.4f} percent of mass on {len(res)} rows; adjudicated in-sample {ref:.4f} / '
                   f'{rec["credential"][f"c2_{label}_max_ref"]:.4f}; rho {rho:.3f}; sampling floor F {F:.3f} '
                   f'(bootstrap median {rec["credential"][f"floor_{label}_median"]:.3f}); Q2 is a fixed rms ratio, not a test of equal error distributions')
        order = np.argsort(-np.abs(res))[:5]
        out.append(f'{label} worst five (+: overbound by the model): ' + ', '.join(
            f'Z={int(rows[i, 0])} N={int(rows[i, 1])} {res[i]:+.4f}' for i in order))
        Z, N = rows[:, 0], rows[:, 1]
        A = Z + N
        m_atom = Z * CONFIG['m_p'] + N * CONFIG['m_n'] + Z * CONFIG['m_e'] - (Z * CONFIG['d_h'] + N * CONFIG['d_n'] - rows[:, 3])
        asym = CONFIG['asym_coeff'] * (N - Z) ** 2 / A / m_atom * 100.0
        quart = (N - Z) ** 4 / A ** 3 / m_atom * 100.0
        pair = np.where((Z % 2 == 0) & (N % 2 == 0), 1.0, np.where((Z % 2 == 1) & (N % 2 == 1), -1.0, 0.0))
        chans = [('23 (N-Z)^2/A', asym)] if label == 'M1' else [('(N-Z)^4/A^3', quart), ('pairing indicator', pair)]
        parts = []
        for name, ch in chans:
            r = pearson(res, ch)
            r_abs, null99, pct = perm_null(res, ch, rng)
            parts.append(f'corr(residual, {name}) = {r:+.3f}; permutation null 99th percentile of |r| {null99:.3f}, observed at the '
                         f'{pct:.1f}th percentile ({"above" if r_abs > null99 else "not above"} the null floor)')
        out.append(f'Q3 {label} (sub-reading; {NO_CLAIM}): ' + '; '.join(parts))
    return decisions


if __name__ == '__main__':
    v = K.Verdict(ROOT, SLUG, COMMISSION, [u for u, _ in UNITS], MANIFEST, FORMS, open_form='INSTRUMENT-OPEN',
                  config=CONFIG, questions=QUESTIONS)
    sys.exit(v.render(form_rule))
