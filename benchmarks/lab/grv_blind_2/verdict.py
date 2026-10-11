"""GRV-BLIND-2 verdict. Reads ONLY the checkpoint (analysis/grv_blind_2_ckpt.pkl; with LAB_SMOKE=1 the smoke checkpoint);
computes only the statistics locked in the charter (analysis/GRV_BLIND_2_charter_LOCKED.md; draft
analysis/lab/drafts/GRV-BLIND-2/charter.md); runs once. Writes analysis/GRV-BLIND-2_verdict.log (smoke:
analysis/GRV-BLIND-2_smoke_verdict.log, never the evidence log).

Q1 (the physics, the rms bar alone): BLIND-AGREES | BLIND-FAILS | BLIND-INCOMPLETE | BLIND-OPEN-FLOOR | BLIND-CALIB-FAIL
Q2 (what counts toward NORTH_STAR 2b):  DRAW-EXTERNAL | DRAW-NOT-EXTERNAL
Q3 (the worst-galaxy bar, recorded; it changes neither Q1 nor Q2 nor the scorecard): OUTLIER-WITHIN-BAR | OUTLIER-EXCEEDS-BAR | OUTLIER-OPEN

This module is also imported by driver.py for the pre-truth gate (pre_truth_gate below), so the driver's gate and the
verdict use the same constants and the same code: there is one copy of every locked tolerance.
"""
import os, pathlib, pickle, sys
import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[3]
SMOKE = os.environ.get('LAB_SMOKE') == '1'
CKPT = ROOT / 'analysis' / ('grv_blind_2_smoke.pkl' if SMOKE else 'grv_blind_2_ckpt.pkl')
LOG = ROOT / 'analysis' / ('GRV-BLIND-2_smoke_verdict.log' if SMOKE else 'GRV-BLIND-2_verdict.log')

# ------------------------------------------------------------------ the locked constants (charter sections 4, 5, 6)
TOL_BARS = 1e-6                 # C-1: reproduced GRV-BLIND-1 bars, dex
TOL_PRED = 1e-5                 # C-2: max relative difference of reproduced predictions
TOL_STAT = 5e-5                 # C-4: reproduced BLIND-1 rms / worst-galaxy rms against the tool's, dex
TOL_TOOL = 1e-9                 # tool-vs-script agreement on the BLIND-2 statistics, dex
F1_MIN_RATIO = 2.0              # F-1: Newtonian-null training rms >= 2.0 x bar_rms
F2_MIN_SEP = 0.30               # F-2: held-out rms of log10(g_pred/g_bar), dex
F2_MIN_BELOW = 0.40             # F-2: fraction of held-out input radii with g_bar < g_dagger
# B-6 (charter section 6, the same list, character for character; compared after strip() and lower())
EXCLUDED = {'', 'palmer', 'mark', 'mark palmer', 'mrpalmer100', 'author', 'the author', 'lab', 'mesh lab', 'sandbox',
            'commission', 'the commission', 'agent', 'worker', 'claude'}
EXCLUDED_SEEDS = {52525254, 777}   # GRV-BLIND-1's seed; the smoke's throwaway seed
B1_SEED = 52525254
GD_FIT = 1.134e-10              # the registered data-fitted g_dagger (GRV-030), descriptive sub-reading only
KPC, KMS = 3.086e19, 1e3


def nu(y):
    return 1.0 / (1.0 - np.exp(-np.sqrt(y)))


def stats(rows):
    """rows: [(galaxy, gobs, gpred)] -> (rms over points, worst per-galaxy rms, mean residual, n)."""
    res, per = [], {}
    for g, go, gp in rows:
        x = np.log10(go) - np.log10(gp); res.append(x); per.setdefault(g, []).append(x)
    res = np.array(res)
    return float(np.sqrt(np.mean(res ** 2))), max(float(np.sqrt(np.mean(np.square(v)))) for v in per.values()), float(np.mean(res)), len(res)


# ------------------------------------------------------------------ the pre-truth gate (shared with driver.py)
def pre_truth_gate(st):
    """C-1..C-5 and F-1, F-2 from the checkpoint's pre-truth units, with the locked tolerances. No truth is read or needed.
    Returns a dict of pass flags and the numbers behind them; 'passed' is True only if every one of the seven passes."""
    g = dict(have_calib='calib' in st, have_manifest='manifest' in st, have_predict='predict' in st)
    g.update(ok1=None, ok2=None, ok3=None, ok4=None, ok5=None, okf1=None, okf2=None)
    if g['have_calib']:
        cal = st['calib']; c1, c2, c3, c4 = cal['c1'], cal['c2'], cal['c3'], cal['c4']
        g['d1'] = max(abs(c1['bar_rms_new'] - c1['bar_rms_ref']), abs(c1['bar_gal_new'] - c1['bar_gal_ref']))
        g['ok1'] = bool(g['d1'] <= TOL_BARS)
        g['ok2'] = bool(c2['keys_equal'] and c2['n_ref'] > 0 and c2['max_rel_diff'] <= TOL_PRED)
        g['ok3'] = bool(c3['test_equal']) and c3['eligible_new'] == c3['eligible_ref'] and c3['n_test'] == 30
        rms4, worst4, mean4, n4 = stats(c4['rows'])
        form4 = 'BLIND-AGREES' if (rms4 <= c4['bar_rms'] and worst4 <= c4['bar_gal']) else 'BLIND-FAILS'
        g['c4'] = (rms4, worst4, n4, form4)
        g['ok4'] = bool(abs(rms4 - c4['tool_rms']) <= TOL_STAT and abs(worst4 - c4['tool_worst']) <= TOL_STAT
                        and n4 == c4['n_points'] and form4 == c4['tool_verdict'])
    if g['have_manifest']:
        man = st['manifest']
        g['ok5'] = bool(man['repro_test_equal'] and man['repro_eligible_equal'] and man['repro_train_equal'] and man['inputs_ok']
                        and man['n_test'] == 30 and man['train_file_sha256'] == man['train_sha256'])
    if g['have_predict']:
        pr = st['predict']; f1, f2, bars = pr['f1'], pr['f2'], pr['bars']
        g['ratio'] = f1['newton_train_rms'] / bars['bar_rms']
        g['okf1'] = bool(g['ratio'] >= F1_MIN_RATIO)
        g['okf2'] = bool(f2['sep_rms'] >= F2_MIN_SEP and f2['frac_below'] >= F2_MIN_BELOW and f2['n_unpredicted_or_gbar_le_0'] == 0)
    g['calib_ok'] = bool(g['ok1'] and g['ok2'] and g['ok3'] and g['ok4'] and g['ok5'])
    g['floor_ok'] = bool(g['okf1'] and g['okf2'])
    g['passed'] = bool(g['calib_ok'] and g['floor_ok'])
    return g


def is_external(man):
    drawer = str(man['drawn_by']).strip().lower()
    return bool(drawer not in EXCLUDED and man['seed'] not in EXCLUDED_SEEDS and set(man['test_galaxies']) != set(man['b1_test']))


def main():
    if not CKPT.exists():
        print(f'no checkpoint at {CKPT}'); sys.exit(2)
    st = pickle.loads(CKPT.read_bytes())
    out = []

    def P(s=''):
        out.append(s); print(s)

    def finish(q1, why1, q2, why2, q3, why3, score):
        P(f'FORM (Q1): {q1} -- {why1}')
        P(f'FORM (Q2): {q2} -- {why2}')
        P(f'FORM (Q3): {q3} -- {why3}')
        P(score)
        LOG.write_text('\n'.join(out) + '\n')

    P(f"GRV-BLIND-2 verdict ({'SMOKE, not evidence' if SMOKE else 'evidence checkpoint'}); checkpoint {CKPT.relative_to(ROOT)}; units done {st.get('done')}")
    cal, man, pr = st.get('calib'), st.get('manifest'), st.get('predict')
    sl, t = st.get('seal'), st.get('truth')
    gate = pre_truth_gate(st)
    SC_NO = 'SCORECARD: 2b unchanged by this verdict'

    # ---------------------------------------------------------------- calibration leg
    P('')
    P('CALIBRATION LEG (pass bars locked; every one must pass; C-1 to C-5 are evaluated before the seal and the truth)')
    if cal is not None:
        c1, c2, c3 = cal['c1'], cal['c2'], cal['c3']
        rms4, worst4, n4, form4 = gate['c4']; c4 = cal['c4']
        P(f"  C-1 bars rule reproduces GRV-BLIND-1: |d| = {gate['d1']:.2e} dex (bar {TOL_BARS:.0e}); new {c1['bar_rms_new']:.6f}/{c1['bar_gal_new']:.6f}; ref {c1['bar_rms_ref']:.6f}/{c1['bar_gal_ref']:.6f}: {'PASS' if gate['ok1'] else 'FAIL'}")
        P(f"  C-2 predictor reproduces GRV_BLIND_1_pred.txt: {c2['n_new']}/{c2['n_ref']} points, keys equal {c2['keys_equal']}, max rel diff {c2['max_rel_diff']:.2e} (bar {TOL_PRED:.0e}); file sha equal {c2['pred_sha_new'] == c2['pred_sha_ref']} (informational): {'PASS' if gate['ok2'] else 'FAIL'}")
        P(f"  C-3 draw tool reproduces GRV-BLIND-1's 30 galaxies from seed {B1_SEED}: {c3['test_equal']}; eligible {c3['eligible_new']} vs {c3['eligible_ref']}: {'PASS' if gate['ok3'] else 'FAIL'}")
        P(f"  C-4 verdict arithmetic on GRV-BLIND-1's recorded rows: rms {rms4:.4f} (tool {c4['tool_rms']:.4f}), worst {worst4:.4f} (tool {c4['tool_worst']:.4f}), n {n4} (tool {c4['n_points']}), form {form4} (tool {c4['tool_verdict']}); bar {TOL_STAT:.0e}: {'PASS' if gate['ok4'] else 'FAIL'}")
    else:
        P('  C-1 to C-4: calib unit not in the checkpoint')
    if man is not None:
        P(f"  C-5 the adjudicator's draw reproduces from its seed {man['seed']} (test {man['repro_test_equal']}, eligible {man['repro_eligible_equal']}, train {man['repro_train_equal']}); inputs present {man['inputs_ok']}; train file sha matches manifest {man['train_file_sha256'] == man['train_sha256']}: {'PASS' if gate['ok5'] else 'FAIL'}")
    else:
        P('  C-5: manifest unit not in the checkpoint')
    ok6 = bool(sl is not None and sl['matches_predict'] and sl['sha256'])
    P(f"  C-6 one seal, on the file the driver wrote (evaluated after the seal; not part of the pre-truth gate): " + (f"{sl['sha256'][:16]}...: {'PASS' if ok6 else 'FAIL'}" if sl is not None else 'no seal in the checkpoint'))

    # ---------------------------------------------------------------- floor leg (training and inputs only; no truth)
    P('')
    P('FLOOR LEG (computed before the seal and before the truth; training data and held-out inputs only)')
    bars = None
    if pr is not None:
        f1, f2, bars = pr['f1'], pr['f2'], pr['bars']
        P(f"  F-1 power against the null: Newtonian (g_pred = g_bar) training rms {f1['newton_train_rms']:.4f} dex = x{gate['ratio']:.2f} the bar {bars['bar_rms']:.4f} (bar x{F1_MIN_RATIO}); prediction's training rms {f1['pred_train_rms']:.4f}: {'PASS' if gate['okf1'] else 'FAIL'}")
        P(f"  F-2 the draw is in the regime where the prediction differs from the null: held-out rms of log10(g_pred/g_bar) {f2['sep_rms']:.3f} dex (bar >= {F2_MIN_SEP}); fraction of input radii with g_bar < g_dagger {f2['frac_below']:.3f} (bar >= {F2_MIN_BELOW}); input radii unpredicted or g_bar <= 0: {f2['n_unpredicted_or_gbar_le_0']} (bar 0): {'PASS' if gate['okf2'] else 'FAIL'}")
        P(f"  worst-galaxy bar origin (recorded): bar {bars['bar_gal']:.4f}; worst TRAINING galaxy rms at the prediction {f1.get('train_worst_gal_rms', float('nan')):.4f} ({f1.get('train_worst_gal', '?')}): the bar is that one training galaxy's rms")
    else:
        P('  F-1, F-2: predict unit not in the checkpoint')

    # ---------------------------------------------------------------- Q2
    if man is not None:
        external = is_external(man)
        P('')
        P(f"DRAW: seed {man['seed']}; drawn by '{man['drawn_by']}' at {man['drawn_at_utc']}; {man['n_test']} of {man['eligible']} eligible; train sha256 {man['train_sha256']}; test sha256 {man['test_sha256']}")
        P(f"  overlap with GRV-BLIND-1's test set: {len(man['overlap_with_b1'])} galaxies {man['overlap_with_b1']} (recorded, not removed)")
        q2 = 'DRAW-EXTERNAL' if external else 'DRAW-NOT-EXTERNAL'
        why2 = (f"drawn by '{man['drawn_by']}' (seed {man['seed']}); not in the locked excluded-drawer list, seed not in {sorted(EXCLUDED_SEEDS)}, set is not GRV-BLIND-1's"
                if external else f"drawn by '{man['drawn_by']}' (seed {man['seed']}); matches the locked excluded-drawer list, an excluded seed, or GRV-BLIND-1's set")
    else:
        external = False
        q2, why2 = 'DRAW-NOT-EXTERNAL', 'no manifest in the checkpoint'

    # ---------------------------------------------------------------- gate-driven forms (no truth needed or used)
    P('')
    if sl is not None or t is not None:
        gr = st.get('gate')
        if not (gr and gr.get('passed') and gate['passed']):
            P('PROTOCOL BREACH: a seal or truth step is in the checkpoint without a passing pre-truth gate record; the held-out statistics are not used.')
            finish('BLIND-CALIB-FAIL', 'the seal or truth was taken without a passing pre-truth gate (driver protocol breach)', q2, why2,
                   'OUTLIER-OPEN', 'no valid truth step', SC_NO)
            return
    if gate['have_calib'] and not (gate['ok1'] and gate['ok2'] and gate['ok3'] and gate['ok4']) or (gate['have_manifest'] and not gate['ok5']):
        bad = [n for n, k in (('C-1', 'ok1'), ('C-2', 'ok2'), ('C-3', 'ok3'), ('C-4', 'ok4'), ('C-5', 'ok5')) if gate[k] is False]
        P(f"GATE: calibration failed ({', '.join(bad)}); the sealed truth was never read by the driver; no verdict on the prediction.")
        finish('BLIND-CALIB-FAIL', f"calibration pass bar failed ({', '.join(bad)}); the truth was never read", q2, why2, 'OUTLIER-OPEN',
               'the truth was never read', SC_NO)
        return
    if gate['have_predict'] and not gate['floor_ok']:
        bad = [n for n, k in (('F-1', 'okf1'), ('F-2', 'okf2')) if gate[k] is False]
        P(f"GATE: floor test failed ({', '.join(bad)}); the sealed truth was never read by the driver; the draw cannot discriminate.")
        finish('BLIND-OPEN-FLOOR', f"floor test failed ({', '.join(bad)}); the draw or the instrument cannot discriminate; the truth was never read; not a pass and not a fail",
               q2, why2, 'OUTLIER-OPEN', 'the truth was never read', SC_NO)
        return
    if not gate['passed'] or sl is None or t is None:
        P('The pre-truth gate has not been completed, or the seal or truth step is missing; no verdict on the prediction.')
        finish('BLIND-INCOMPLETE', 'a unit is missing from the checkpoint (calib, manifest, predict, seal or truth); nothing failed that was run', q2, why2,
               'OUTLIER-OPEN', 'no truth step', SC_NO)
        return

    # ---------------------------------------------------------------- truth leg (gate passed)
    P('HELD-OUT STATISTICS (recomputed from the kept rows; the tool\'s own numbers are cross-checked)')
    rows = [(g, go, gp) for g, r, go, gp in t['rows']]
    rms, worst, mean, n = stats(rows)
    pergal = {}
    for g, go, gp in rows:
        pergal.setdefault(g, []).append(np.log10(go) - np.log10(gp))
    pergal = {g: float(np.sqrt(np.mean(np.square(v)))) for g, v in pergal.items()}
    worst_g = max(pergal, key=pergal.get)
    agree_tool = (abs(rms - t['tool_rms']) <= TOL_TOOL and abs(worst - t['tool_worst']) <= TOL_TOOL and n == t['n_points'])
    bars_match = (t['tool_bar_rms'] == bars['bar_rms'] and t['tool_bar_gal'] == bars['bar_gal'])
    rms_ok, gal_ok = rms <= bars['bar_rms'], worst <= bars['bar_gal']
    tool_form_script = 'BLIND-AGREES' if (rms_ok and gal_ok) else 'BLIND-FAILS'     # the unchanged tool's form uses both bars
    form_agree = (tool_form_script == t['tool_verdict']) if not t['missing'] else (t['tool_verdict'] == 'BLIND-INCOMPLETE')
    P(f"  {n} kept points in {len(pergal)} galaxies; rms {rms:.4f} dex (bar <= {bars['bar_rms']:.4f}); worst galaxy {worst_g} {worst:.4f} (bar <= {bars['bar_gal']:.4f}); mean residual {mean:+.4f}")
    P(f"  tool agreement: rms/worst/n match to {TOL_TOOL:.0e}: {agree_tool}; tool's bars equal the checkpoint's: {bars_match}; tool verdict {t['tool_verdict']} (both bars) vs script {tool_form_script}: {form_agree}; missing {len(t['missing'])}")
    top = sorted(pergal.items(), key=lambda kv: -kv[1])[:5]
    P('  worst five: ' + ', '.join(f'{g} {x:.3f}' for g, x in top))

    # ---------------------------------------------------------------- descriptive sub-readings (change nothing)
    gb = {(g, r): x for g, lst in pr['gbar'].items() for r, x in lst}
    pts = [(g, round(r, 4), go) for g, r, go, gp in t['rows']]
    overlap = man['overlap_with_b1']

    def rms_with(gd, skip=()):
        res = [np.log10(go) - np.log10(gb[(g, r)] * nu(gb[(g, r)] / gd)) for g, r, go in pts if g not in skip and (g, r) in gb]
        return float(np.sqrt(np.mean(np.square(res)))), float(np.mean(res))
    gd0 = pr['g_dagger']
    r_fit, m_fit = rms_with(GD_FIT)
    scan = [(f, rms_with(gd0 * f)[0]) for f in [2.0 ** (k / 4.0) for k in range(-8, 9)]]
    f_best = min(scan, key=lambda a: a[1])
    inwin = [f for f, v in scan if v <= bars['bar_rms']]
    r_nov = rms_with(gd0, skip=set(overlap))[0] if len(overlap) < len(pergal) else float('nan')
    P('')
    P('SUB-READINGS (descriptive; locked as recorded-not-read; they change no form)')
    P(f"  rms at the registered data-fitted g_dagger {GD_FIT:.3e}: {r_fit:.4f} (mean {m_fit:+.4f}) against {rms:.4f} at the predicted {gd0:.3e}")
    P((f"  held-out rms best on the factor grid x2^(k/4), k -8..8: x{f_best[0]:.3f} ({f_best[1]:.4f}); factors whose held-out rms is within the bar: x{min(inwin):.3f} to x{max(inwin):.3f}") if inwin else '  no factor on the grid within the bar')
    P(f"  training pass window (set before the truth): g_dagger x{pr['window']['lo_factor']:.3f} to x{pr['window']['hi_factor']:.3f} of the predicted value keep the training rms within the bar: a BLIND-AGREES does not discriminate c H0 / 2 pi from values inside this window")
    P(f"  rms excluding the {len(overlap)} galaxies shared with GRV-BLIND-1: {r_nov:.4f}")

    # ---------------------------------------------------------------- forms
    P('')
    P(f"BARS: rms <= {bars['bar_rms']:.4f} dex (decides Q1) and worst galaxy <= {bars['bar_gal']:.4f} dex (recorded as Q3 only), 95th percentiles over 20000 random 30-galaxy subsets of the {bars['n_train_used']} training galaxies at the predicted g_dagger")
    if not (agree_tool and form_agree and ok6):
        why = 'the C-6 seal check failed' if not ok6 else 'the script and the tool disagree on the held-out statistics'
        q1, why1 = 'BLIND-CALIB-FAIL', why
    elif t['missing']:
        q1, why1 = 'BLIND-INCOMPLETE', f"{len(t['missing'])} kept held-out points were unpredicted"
    elif rms_ok:
        q1, why1 = 'BLIND-AGREES', f"rms {rms:.4f} <= {bars['bar_rms']:.4f}; calibration and floor legs pass (the worst-galaxy bar carries no weight in this form)"
    else:
        q1, why1 = 'BLIND-FAILS', f"rms {rms:.4f} > {bars['bar_rms']:.4f}"
    if t['missing'] or not agree_tool or not form_agree or not ok6:
        q3, why3 = 'OUTLIER-OPEN', 'held-out statistics incomplete or not agreed with the tool'
    elif gal_ok:
        q3, why3 = 'OUTLIER-WITHIN-BAR', f"worst galaxy {worst_g} {worst:.4f} <= {bars['bar_gal']:.4f} (carries no evidential weight; the bar is one training galaxy's rms)"
    else:
        q3, why3 = 'OUTLIER-EXCEEDS-BAR', f"worst galaxy {worst_g} {worst:.4f} > {bars['bar_gal']:.4f} (recorded; changes neither Q1 nor the scorecard)"
    sc = ('SCORECARD: NORTH_STAR 2b externally adjudicated predictions 1 -> 2 (the author ratifies); GRV-030 rider; no target moved, no input retired'
          if (q1 == 'BLIND-AGREES' and external) else SC_NO)
    finish(q1, why1, q2, why2, q3, why3, sc)


if __name__ == '__main__':
    main()
