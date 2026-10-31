"""RING-WAVE-STABILITY-4 verdict: reads the checkpoint only, through labkit.Verdict.

form_rule recomputes every locked statistic from the sealed series (ser/, fn/, D/ seals) and the unit records, and
returns exactly one decision per question (Q1, Q1b, Q2). Every form is conditional on action (i) (charter P1).
LAB_SMOKE=1: reads the smoke checkpoint, checks the plumbing (seal read-back, array shapes, that the statistic
functions run) and prints counts only: no rho, sigma or D_shape, and no form (the kit withholds them).
"""
import json
import math
import pathlib
import sys

import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from benchmarks.lab._kit import labkit as K                                              # noqa: E402
from benchmarks.lab.ring_wave_stability_4 import stats as ST                             # noqa: E402
from benchmarks.lab.ring_wave_stability_4.driver import (SLUG, MANIFEST, CONFIG, UNITS, SPECS, SMOKE, SMOKE_RUNS)   # noqa: E402

NAME = 'RING-WAVE-STABILITY-4'
FORMS = ['RING-STABLE', 'RING-UNSTABLE', 'RING-SLOW', 'Q1-NO-CALL', 'NEUTRAL-HOLDS', 'NEUTRAL-DRIFTS', 'NEUTRAL-WOBBLES',
         'Q1B-NO-CALL', 'END-FOLD', 'END-OTHER', 'END-NOT-TRIGGERED', 'Q2-NO-CALL', 'HARNESS-OPEN']
OPEN_FORM = 'HARNESS-OPEN'
QUESTIONS = ('Q1', 'Q1b', 'Q2')


def load(ck, name):
    rec = ck.state['records'][name]
    ser = ck.sealed(f'ser/{name}').reshape(-1, len(ST.COLS))
    cols = {c: ser[:, i] for c, i in ST.CI.items()}
    return rec, cols


def verify_runs(ck, out):
    """From the sealed RAW series, verify every run's completion or failure record: a complete run must scan v5-clean; a
    failed run must show its retained breach row at fail_step with the recorded kind and a v5-clean prefix that excludes it
    (a Newton failure: no breach row, clean prefix, all samples before fail_step). Any mismatch halts (HARNESS-OPEN)."""
    nfail = 0
    for name in SPECS:
        rec = ck.state['records'][name]
        ser = ck.sealed(f'ser/{name}').reshape(-1, len(ST.COLS)); br = ck.sealed(f'breach/{name}').reshape(-1, len(ST.COLS))
        if rec['complete']:
            i, kind = ST.v5_scan(ser, CONFIG)
            K.require(i is None and len(br) == 0, f'{name}: complete run does not scan v5-clean from its raw series (sample {i}, {kind})')
            continue
        ok, txt = ST.verify_failure(ser, br, rec['fail_step'], rec['fail_reason'], CONFIG)
        K.require(ok, f'{name}: failure record not verified from the retained raw series: {txt}')
        nfail += 1
        out.append(f'failure record {name}: {txt}')
    out.append(f'raw-series check: {len(SPECS) - nfail} complete runs scan v5-clean; {nfail} failure record(s) verified from the retained breach row / prefix')


def c_ser(ck, name):
    return ck.sealed(f'ser/{name}').reshape(-1, len(ST.COLS))


def amp_series(probe, cols, Rd):
    if probe == 'W1':
        return cols['aw1']
    if probe == 'W2':
        return cols['aw2']
    if probe == 'R0':
        return np.abs(cols['R_mean'] - Rd)
    raise K.Halt(f'no Q1 amplitude for {probe}')


def base_rate(probe, Rd):
    return 1.0 / Rd if probe[0] == 'W' else Rd


def form_rule(ck, out):
    recs = ck.state['records']
    if ck.smoke:
        return smoke_rule(ck, out)
    cfg = CONFIG; Ms = cfg['Ms']; nb = cfg['n_per']
    cred = json.loads(ck.sealed('cred/record').decode())
    out.append('UNDER ACTION (i) throughout (charter P1). Interior work (NORTH_STAR section 5, exception of 28 October 2026).')
    out.append('credential bars: ' + ' '.join(f'{k}={"PASS" if v else "FAIL"}' for k, v in sorted(cred['bars'].items())))
    K.require(all(cred['bars'].values()), 'credential bar failed')
    verify_runs(ck, out)
    st = recs['static']
    out.append(f'D6 static cross-check (Leg C functional, no Coulomb term) M={st["M"]}: S={st["S"]:.3e} (bar {cfg["static_S"]}: '
               f'{"met" if st["S_below_bar"] else "NOT met, a finding"}), negative constrained modes {st["nneg"]}, null {st["nnull"]}, dim {st["dim"]}')
    Rd = {M: recs['setup']['Rd'][str(M)] for M in Ms}
    # controls
    ctrl = {}
    for key in ('ctrl_M48', 'ctrl_M96', 'ctrl_M48_h'):
        r, c = load(ck, key); ctrl[key] = (r, c)
    # ---- Q1 -----------------------------------------------------------------------------------------------
    q1 = {}; q1h = {}
    for p in ST.Q1_PROBES:
        for M in Ms:
            cr, cc = ctrl[f'ctrl_M{M}']
            for a in ('s', 'c'):
                r, c = load(ck, f'{p}_M{M}_{a}')
                s = ST.q1_class(c['m'], amp_series(p, c, Rd[M]), cc['m'], amp_series(p, cc, Rd[M]), r['spp'], base_rate(p, Rd[M]), cfg,
                                fail_step=r['fail_step'], ctrl_ok=cr['complete'])
                s['marks'] = ST.end_marks(c['m'], c['R_end_ratio'], c['beta'], c['E'], r['spp'], cfg, fail_step=r['fail_step'])
                q1[(p, M, a)] = s
                out.append(f'Q1 {p} M={M} amp={a}: {s["cls"]} rho={s["rho"]:.4g} sigma={s["sigma"]:.4g}/period'
                           + (f' prefix of {s["n_full"]} blocks' if s['prefix'] else '') + (f' [{s["why"]}]' if s['why'] else ''))
        r, c = load(ck, f'{p}_M48_h'); cr, cc = ctrl['ctrl_M48_h']
        q1h[p] = ST.q1_class(c['m'], amp_series(p, c, Rd[48]), cc['m'], amp_series(p, cc, Rd[48]), r['spp'], base_rate(p, Rd[48]), cfg,
                             fail_step=r['fail_step'], ctrl_ok=cr['complete'])
        out.append(f'Q1 {p} half-step run: {q1h[p]["cls"]} rho={q1h[p]["rho"]:.4g} sigma={q1h[p]["sigma"]:.4g}')
    half1 = {p: ST.half_blocked_q1(q1[(p, 48, 's')]['cls'], q1h[p]['cls']) for p in ST.Q1_PROBES}
    out.append('Q1 half-blocked: ' + str(half1))
    for p in ST.Q1_PROBES:                                                            # reported, not scored
        for M in Ms:
            r, c = load(ck, f'{p}_M{M}_s')
            b0 = c['beta'][0] if len(c['beta']) else float('nan')
            out.append(f'Q1 {p} M={M} reported (not scored): max |beta - beta0| {np.nanmax(np.abs(c["beta"] - b0)):.3e}, '
                       f'largest Phidot mode of n=1..6 over the run {max(np.nanmax(c[f"aw{n}"]) for n in range(1, 7)):.3e}')
    f1, why1, wit1 = ST.decide_q1(q1, half1, Ms)
    # WU family check, reported, never a form
    from benchmarks.lab.ring_wave_stability_4.driver import _rwd
    rwd = _rwd()
    for M in Ms:
        for a in ('s', 'c'):
            r, c = load(ck, f'WU_M{M}_{a}'); cr, cc = ctrl[f'ctrl_M{M}']
            if not r['complete'] or not cr['complete']:
                out.append(f'WU M={M} {a}: anomaly (run incomplete)'); continue
            sh = c['m'] >= 20 * r['spp']; csh = cc['m'] >= 20 * cr['spp']
            bJ = float(np.mean(c['Jz'])) / float(cc['Jz'][0])
            Rp = rwd.discrete_ring_radius(M, cfg['kappa'], 1, bJ)
            e1 = abs(float(np.mean(c['R_mean'][sh])) / Rp - 1)
            e2 = abs(float(np.mean(c['beta'][sh])) / float(np.mean(cc['beta'][csh])) / bJ - 1)
            ok = e1 <= cfg['wu_R'] and e2 <= cfg['wu_beta']
            out.append(f'WU M={M} {a}: beta_J {bJ:.6f}, |R/R_pred-1| {e1:.3e} (bar {cfg["wu_R"]}), beta-ratio error {e2:.3e} (bar {cfg["wu_beta"]}): '
                       + ('FAMILY-DRIFT-AS-EXPECTED' if ok else 'anomaly of the instrument on the face (blocks nothing)'))
    # ---- Q1b ----------------------------------------------------------------------------------------------
    sh = {}; shh = {}; ctrl_sh = {}; g4 = {}
    spp0 = cfg['steps_per_period']
    for M in Ms:
        r, c = ctrl_rec = load(ck, f'ctrl_M{M}')
        if r['complete']:
            D = ck.sealed(f'D/ctrl_M{M}'); fn = ck.sealed(f'fn/ctrl_M{M}')
            ctrl_sh[M] = ST.ctrl_shape_stats(fn, D / Rd[M], r['spp'], cfg)
        else:
            ctrl_sh[M] = dict(maxD_rel=float('inf'), slope_rel=float('nan'))
        f1b = cred['K6'][str(M)]['F1b']['D_max'] / (cfg['eps_scored'] * Rd[M])
        g4[M] = bool(f1b < cfg['g4_floor'])
        out.append(f'Q1b M={M}: control D_shape max {ctrl_sh[M]["maxD_rel"] / cfg["eps_scored"]:.3e} (bar {cfg["g1_D"]}), control slope per block '
                   f'{ctrl_sh[M]["slope_rel"] / cfg["eps_scored"]:.3e}; g4 observable floor (K6 F1b) {f1b:.3e} (bar {cfg["g4_floor"]})')
        for p in ST.SHAPE_ALL:
            for a, e in (('s', cfg['eps_scored']), ('c', cfg['eps_check'])):
                r, c = load(ck, f'{p}_M{M}_{a}')
                D = ck.sealed(f'D/{p}_M{M}_{a}'); fn = ck.sealed(f'fn/{p}_M{M}_{a}')
                s = ST.shape_class(fn, D / (e * Rd[M]), r['spp'], cfg, failed=not r['complete'])
                s['marks'] = ST.end_marks(c['m'], c['R_end_ratio'], c['beta'], c['E'], r['spp'], cfg, fail_step=r['fail_step'])
                sh[(p, M, a)] = s
                out.append(f'Q1b {p} M={M} amp={a}{" (DIAGNOSTIC ONLY)" if p == "S2" else ""}: {s["cls"]} max D_shape {s["maxD"]:.4g} '
                           f'second-half slope {s["slope"]:.4g} (se {s["se"]:.3g}) per block' + (f' [{s["why"]}]' if s['why'] else ''))
    half2 = {}
    for p in ST.SHAPE_ALL:
        r, c = load(ck, f'{p}_M48_h')
        D = ck.sealed(f'D/{p}_M48_h'); fn = ck.sealed(f'fn/{p}_M48_h')
        s = ST.shape_class(fn, D / (cfg['eps_scored'] * Rd[48]), r['spp'], cfg, failed=not r['complete'])
        half2[p] = not ST.g2_agree(sh[(p, 48, 's')], s, cfg)
        out.append(f'Q1b {p} half-step run: {s["cls"]} max {s["maxD"]:.4g} slope {s["slope"]:.4g}; g2 {"blocked" if half2[p] else "agrees"}')
    fb, whyb, witb = ST.decide_q1b(sh, {p: half2[p] for p in ST.SHAPE_BEARING}, ctrl_sh, g4, cfg, Ms)
    f2, why2, qual = ST.decide_q2(f1, wit1, q1, fb, witb, sh, Ms)
    def ua(w):
        return w if w.startswith('under action (i)') else 'under action (i): ' + w
    return [('Q1', f1, ua(why1)), ('Q1b', fb, ua(whyb)), ('Q2', f2, ua(why2))]


def smoke_rule(ck, out):
    recs = ck.state['records']
    out.append(f'smoke plumbing: units {len(ck.units)}, all done {all(ck.done(u) for u in ck.units)}, seals read back {ck.verify_seals()}')
    cred = json.loads(ck.sealed('cred/record').decode())
    out.append(f'smoke credential record read back (keys {sorted(cred["bars"])}), static record M={recs["static"]["M"]}, nneg field present {"nneg" in recs["static"]}')
    for name in SMOKE_RUNS:
        r, c = load(ck, name)
        Rd = recs['setup']['Rd'][str(SMOKE['M'])]
        spp = r['spp']
        bm = ST.block_max(c['m'], c['E'], spp, SMOKE['n_per'])
        mk = ST.end_marks(c['m'], c['R_end_ratio'], c['beta'], c['E'], spp, dict(CONFIG, n_per=SMOKE['n_per']))
        D = ck.sealed(f'D/{name}'); fn = ck.sealed(f'fn/{name}')
        br = ck.sealed(f'breach/{name}').reshape(-1, len(ST.COLS))
        out.append(f'smoke breach seal {name}: read back, {len(br)} rows; v5 replay on the raw series ran ({len(c_ser(ck, name))} samples; result withheld in smoke)')
        ST.v5_scan(c_ser(ck, name), CONFIG)
        out.append(f'smoke run {name}: complete {r["complete"]}, {len(c["m"])} samples x {len(ST.COLS)} columns, {len(fn)} frames, '
                   f'D_shape array {D.shape} finite {bool(np.all(np.isfinite(D)))}, block-max finite {bool(np.any(np.isfinite(bm)))}, '
                   f'end-marks computed {mk["R"] is not None}')
    out.append(f'smoke stat_credential fixtures: {recs["stat_credential"]["n"]}, all passed {recs["stat_credential"]["all_pass"]}')
    return [(q, OPEN_FORM, 'smoke') for q in QUESTIONS]


if __name__ == '__main__':
    v = K.Verdict(ROOT, SLUG, NAME, [u for u, _ in UNITS], MANIFEST, FORMS, open_form=OPEN_FORM, config=CONFIG, questions=QUESTIONS)
    sys.exit(v.render(form_rule))
