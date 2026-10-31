"""COMMISSION NUC-NEW-1 -- the two adjudicated nuclear mass models on the nuclides measured between AME2012 and AME2020.
Design sealed before this file existed: analysis/NUC_NEW_1_design_SEALED.md. Charter analysis/NUC_NEW_1_charter_DRAFT.md.
Harness: benchmarks/lab/_kit/labkit.py (Driver / Checkpoint / Halt / Blocked); verdict in verdict.py; one CONFIG shared.

Units, in the locked order, one per invocation (resumable):
  credential  C-1 the model arithmetic reproduces NUC-BLIND-2's sealed prediction files byte for byte;
              C-2 the residual rule reproduces NUC-BLIND-2's published rms and max from VERDICT_M1/M2.json rows;
              C-3 tools/ame2020_newset.py on a SYNTHETIC mas20-layout fixture (AME2012 rows reformatted plus planted
              rows) recovers the planted set exactly. A failure is a Halt: the verdict renders INSTRUMENT-OPEN and the
              truth is never read.
  manifest    reads analysis/holdout/NUC_NEW_1/MANIFEST.json and labels.txt (Z N only). C-4 the recorded anchor
              deltas are all within the tolerance; C-5 no label is an AME2012 row, none has A < 12, no duplicate, the
              labels hash is the manifest's. Blocked (exit 3, the runner waits) while the hold-out does not exist on
              this machine. Never opens sealed/. Records n_test; fewer than CONFIG['min_rows'] is recorded, not halted
              (the verdict renders NEW-SET-TOO-SMALL).
  predict     M1 and M2 at the labels from AME2012's Ca-40 (the registered calibration); the arrays sealed in the
              checkpoint; analysis/NUC_NEW_1_pred_M1.txt and _M2.txt written (the same layout as NUC-BLIND-2's).
  seal        the two prediction files' sha256 recorded in the hold-out MANIFEST (one seal each; refuses a second).
  truth       the ONE read of sealed/test.txt: residuals per row in the house unit, VERDICT_M1.json and VERDICT_M2.json
              written in the NUC-BLIND-2 schema, the rows sealed in the checkpoint. Blocked when sealed/test.txt is not
              on this machine (the adjudicator-holds-the-file case: then VERDICT_M*.json written there are ingested
              instead, after their prediction hash is checked against the seal).
The driver never prints a FORM line and never prints a residual, an rms or a max; the verdict does, once.

LAB_SMOKE=1: every unit in one process on a THROWAWAY hold-out built in a temporary directory from the synthetic
fixture (the truth there is synthetic: the fixture's planted excesses), checkpoint analysis/nuc_new_1_smoke.pkl; the
evidence hold-out and checkpoint are never touched. Evidence-free by construction: no AME2020 value exists in the
sandbox or in the fixture.
"""
import hashlib
import json
import os
import pathlib
import sys
import tempfile
import time

import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / 'tools'))
from benchmarks.lab._kit import labkit as K                 # noqa: E402
import ame2020_newset as NS                                 # noqa: E402  (the set tool; its parser is credentialed here)

SLUG = 'nuc_new_1'
NAME = 'NUC_NEW_1'
MANIFEST = ['benchmarks/lab/_kit/labkit.py', 'benchmarks/lab/nuc_new_1/driver.py', 'benchmarks/lab/nuc_new_1/verdict.py',
            'tools/ame2020_newset.py', 'benchmarks/nuclear/nuc_blind_1.py', 'data/ame2012/AME2012.txt',
            'analysis/NUC_NEW_1_design_SEALED.md', 'analysis/holdout/NUC_BLIND_2/MANIFEST.json',
            'analysis/holdout/NUC_BLIND_2/train.txt', 'analysis/NUC_BLIND_2_pred_M1.txt', 'analysis/NUC_BLIND_2_pred_M2.txt',
            'analysis/holdout/NUC_BLIND_2/VERDICT_M1.json', 'analysis/holdout/NUC_BLIND_2/VERDICT_M2.json']
CONFIG = dict(
    # the models (design section 3; nuc_blind_1.py's constants, copied, credentialed by C-1)
    d_h=7.28897059, d_n=8.07131714, d0_fm=2.026, coulomb_factor=0.6 * 1.44,
    models={'M1': dict(as_over_av=1.34, a_a=0.0), 'M2': dict(as_over_av=1.108, a_a=19.85)},
    calibrator=[20, 20], min_a=12,
    # the house unit (design section 5)
    m_p=938.272, m_n=939.565, m_e=0.511,
    # bars (design section 6)
    bar_rms=0.25, bar_max=0.60, extrap_factor=2.0, min_rows=30,
    # credentials (design section 4)
    c1_sha={'M1': 'edb67e2410176d86ef15f4644e58e6932a912efab6104ff32fe8b3af7d30b363',
            'M2': 'a5f3f8e01f6c213efcbd4e44c934db33e400b0b6dca68f2f0d94dc4dd44a51c9'},
    c2_tol=1e-9, anchor_tol_MeV=0.010,
    # the sub-reading channels (design Q3)
    asym_coeff=23.0,
)
SMOKE = os.environ.get('LAB_SMOKE') == '1'
TAG = '[nuc-new-1]'


def say(*a):
    print(TAG, *a, flush=True)


def sha256_file(p):
    return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()


# ---------------------------------------------------------------------------------------------- the models
def a_c():
    r0_over_d0 = (3 / (4 * np.pi * np.sqrt(2))) ** (1 / 3)
    return CONFIG['coulomb_factor'] / (r0_over_d0 * CONFIG['d0_fm'])


def binding(A, Z, a_v, as_over_av, a_a):
    N = A - Z
    return a_v * A - as_over_av * a_v * A ** (2 / 3) - a_c() * Z ** 2 / A ** (1 / 3) - a_a * (N - Z) ** 2 / A


def calibrate(b_ca, m):
    zc, nc = CONFIG['calibrator']
    A = zc + nc
    a_v = (b_ca + a_c() * zc ** 2 / A ** (1 / 3) + m['a_a'] * (nc - zc) ** 2 / A) / (A - m['as_over_av'] * A ** (2 / 3))
    K.require(abs(binding(A, zc, a_v, m['as_over_av'], m['a_a']) - b_ca) < 1e-9, 'calibration does not reproduce the calibrator')
    return a_v


def ca40_binding_from(table_path):
    zc, nc = CONFIG['calibrator']
    for l in pathlib.Path(table_path).read_text().splitlines():
        t = l.split()
        if len(t) == 3 and t[0] == str(zc) and t[1] == str(nc):
            return zc * CONFIG['d_h'] + nc * CONFIG['d_n'] - float(t[2])
    raise K.Halt(f'calibrator {zc},{nc} not in {table_path}')


def prediction_lines(labels, b_ca, m):
    a_v = calibrate(b_ca, m)
    lines = ['Z N B_pred_MeV']
    for z, n in labels:
        lines.append(f"{z} {n} {binding(z + n, z, a_v, m['as_over_av'], m['a_a']):.6f}")
    return '\n'.join(lines) + '\n', a_v


def residual_mass(z, n, b_pred, excess):
    """The house unit: 100 (B_pred - B_truth) / m_atom (design section 5; holdout_verdict.py --unit mass)."""
    b = z * CONFIG['d_h'] + n * CONFIG['d_n'] - excess
    m_atom = z * CONFIG['m_p'] + n * CONFIG['m_n'] + z * CONFIG['m_e'] - b
    return 100.0 * (b_pred - b) / m_atom, b


# ---------------------------------------------------------------------------------------------- the synthetic fixture
def mas20_line(z, n, excess_mev, flag=None):
    """One line in the mas20 fixed-width layout. flag None: experimental; 'tail': '#' as the field's last character;
    'point': '#' replacing the decimal point (both conventions the AME files have used)."""
    a = z + n
    kev = excess_mev * 1000.0
    if flag is None:
        field = f'{kev:14.6f}'
    elif flag == 'tail':
        field = f'{kev:13.3f}#'
    else:
        field = f'{kev:14.6f}'.replace('.', '#')
    return (f'0{n - z:3d}{n:5d}{z:5d}{a:5d} {"Xx":<3}{"":<4} {field}{0.5:12.6f}{8000.0:13.5f} {1.0:10.5f} {"B-":<2}'
            f'{1000.0:13.5f}{1.0:11.5f} {a:3d} {0.0:13.6f}{0.0:12.6f}')


def synthetic_fixture(ame2012):
    """AME2012 reformatted as a mas20-layout text, minus one removed row, plus planted rows. Returns (text, expected)
    where expected is the planted test set with planted excesses (synthetic numbers; no AME2020 value anywhere)."""
    rows = dict(ame2012)
    removed = (50, 70)                                           # an AME2012 row absent from the synthetic 'AME2020'
    K.require(removed in rows, 'fixture: the removed row must be an AME2012 row')
    del rows[removed]
    planted = {(50, 90): -45.123, (8, 20): 36.5, (118, 176): 194.9, (28, 50): -1.75, (3, 11): 60.7}   # experimental
    light = {(2, 9): 50.1}                          # A < 12: excluded by the rule
    flagged = {(50, 92): ('tail', -40.0), (119, 177): ('point', 200.0)}
    K.require(all(k not in ame2012 for k in list(planted) + list(light) + list(flagged)), 'fixture: planted rows must be new')
    header = ['1   AME2020 synthetic fixture (NUC-NEW-1 credential C-3): AME2012 rows in the mas20 layout plus planted rows',
              'format : a1,i3,i5,i5,i5,1x,a3,a4,1x,f14.6,f12.6,f13.5,1x,f10.5,1x,a2,f13.5,f11.5,1x,i3,1x,f13.6,f12.6', '']
    lines = [mas20_line(z, n, m) for (z, n), m in sorted(rows.items(), key=lambda kv: (kv[0][0] + kv[0][1], kv[0][0]))]
    lines += [mas20_line(z, n, m) for (z, n), m in planted.items()]
    lines += [mas20_line(z, n, m) for (z, n), m in light.items()]
    lines += [mas20_line(z, n, m, flag) for (z, n), (flag, m) in flagged.items()]
    expected = dict(test=sorted(k for k in planted if k[0] + k[1] >= CONFIG['min_a']), excess=planted,
                    counts=dict(ame2012_absent_from_ame2020=1, new_a_below_12=len(light), ame2020_systematics=len(flagged)))
    return '\n'.join(header + lines) + '\n', expected


# ---------------------------------------------------------------------------------------------- hold-out location
def holdout_dir(ck):
    if ck.smoke:
        d = ck.state['records'].get('credential', {}).get('smoke_holdout')
        K.require(d is not None, 'smoke: no throwaway hold-out recorded by the credential unit')
        return pathlib.Path(d)
    return ROOT / 'analysis' / 'holdout' / NAME


def pred_path(ck, label):
    base = holdout_dir(ck).parent.parent if ck.smoke else ROOT / 'analysis'
    return base / f'{NAME}_pred_{label}.txt'


# ---------------------------------------------------------------------------------------------- units
def unit_credential(ck):
    out = {}
    # C-1: byte-for-byte reproduction of NUC-BLIND-2's sealed prediction files
    man2 = json.loads((ROOT / 'analysis' / 'holdout' / 'NUC_BLIND_2' / 'MANIFEST.json').read_text())
    labels2 = [(int(z), int(n)) for z, n in man2['test_zn']]
    b_ca2 = ca40_binding_from(ROOT / 'analysis' / 'holdout' / 'NUC_BLIND_2' / 'train.txt')
    for label, m in CONFIG['models'].items():
        text, a_v = prediction_lines(labels2, b_ca2, m)
        h = hashlib.sha256(text.encode()).hexdigest()
        ref = sha256_file(ROOT / 'analysis' / f'NUC_BLIND_2_pred_{label}.txt')
        K.require(h == CONFIG['c1_sha'][label] == ref, f'C-1 {label}: reproduction hash {h[:16]} != sealed {ref[:16]}')
        out[f'c1_{label}_a_v'] = float(a_v)
    out['c1'] = 'PASS'
    # C-2: the residual rule on the published VERDICT rows
    for label in CONFIG['models']:
        v = json.loads((ROOT / 'analysis' / 'holdout' / 'NUC_BLIND_2' / f'VERDICT_{label}.json').read_text())
        res = []
        for r in v['rows']:
            rr, b = residual_mass(r['Z'], r['N'], r['pred'], r['truth_excess_MeV'])
            K.require(abs(rr - r['residual']) < CONFIG['c2_tol'], f'C-2 {label}: row residual differs at Z={r["Z"]} N={r["N"]}')
            res.append(rr)
        res = np.array(res)
        rms, mx = float(np.sqrt(np.mean(res ** 2))), float(np.max(np.abs(res)))
        K.require(abs(rms - v['rms']) < CONFIG['c2_tol'] and abs(mx - v['max_abs']) < CONFIG['c2_tol'],
                  f'C-2 {label}: rms/max {rms:.9f}/{mx:.9f} differ from the published {v["rms"]:.9f}/{v["max_abs"]:.9f}')
        out[f'c2_{label}_rms_ref'] = float(v['rms'])          # the Q2 reference, read from the file (design section 6)
        out[f'c2_{label}_max_ref'] = float(v['max_abs'])
    out['c2'] = 'PASS'
    # C-3: the parser on the synthetic fixture, through the tool itself
    ame2012 = NS.read_ame2012()
    text, expected = synthetic_fixture(ame2012)
    tmp = pathlib.Path(tempfile.mkdtemp(prefix='nuc_new_1_fixture_'))
    (tmp / 'synthetic.mas20').write_text(text)
    r = NS.build(text, ame2012)
    K.require(r['test'] == expected['test'], f"C-3: recovered set {r['test']} != planted {expected['test']}")
    for k, val in expected['counts'].items():
        K.require(r['counts'][k] == val, f"C-3: count {k} = {r['counts'][k]} != planted {val}")
    K.require(all(abs(r['test_excess'][k] - expected['excess'][k]) < 1e-6 for k in expected['test']), 'C-3: planted excess not recovered')
    K.require(all(x['pass'] for x in r['anchors']), 'C-3: the anchor check did not pass on AME2012 rows reformatted')
    out['c3'] = 'PASS'
    out['c3_n_test'] = len(r['test'])
    if ck.smoke:
        # the throwaway hold-out, built by the tool's main() so the smoke runs the same path as the lab machine will
        import subprocess
        sroot = tmp / 'smoke_root'
        (sroot / 'analysis').mkdir(parents=True)
        cmd = [sys.executable, str(ROOT / 'tools' / 'ame2020_newset.py'), '--ame2020', str(tmp / 'synthetic.mas20'),
               '--run-by', 'smoke', '--name', NAME, '--out-root', str(sroot)]
        p = subprocess.run(cmd, capture_output=True, text=True)
        K.require(p.returncode == 0, f'smoke: the set tool failed: {p.stderr[-500:]}')
        out['smoke_holdout'] = str(sroot / 'analysis' / 'holdout' / NAME)
    return out


def unit_manifest(ck):
    hd = holdout_dir(ck)
    mp = hd / 'MANIFEST.json'
    if not mp.exists():
        raise K.Blocked(f'hold-out {hd} does not exist on this machine (run tools/ame2020_newset.py on the AME2020 file)')
    man = json.loads(mp.read_text())
    K.require(man.get('name') == NAME, 'manifest: wrong hold-out name')
    K.require(all(abs(x['delta_MeV']) <= CONFIG['anchor_tol_MeV'] and x['pass'] for x in man['anchors']), 'C-4: an anchor delta exceeds the tolerance')
    K.require(len(man['anchors']) == 5, 'C-4: five anchors expected')
    labels_p = hd / 'labels.txt'
    K.require(sha256_file(labels_p) == man['labels_sha256'], 'C-5: labels.txt hash differs from the manifest')
    labels = []
    for l in labels_p.read_text().splitlines():
        t = l.split()
        if len(t) == 2 and t[0].isdigit():
            labels.append((int(t[0]), int(t[1])))
    K.require(labels == [(int(z), int(n)) for z, n in man['test_zn']], 'C-5: labels.txt differs from the manifest test_zn')
    K.require(len(set(labels)) == len(labels), 'C-5: duplicate label')
    K.require(all(z + n >= CONFIG['min_a'] for z, n in labels), 'C-5: a label with A < 12')
    ame2012 = NS.read_ame2012()
    K.require(all(k not in ame2012 for k in labels), 'C-5: a label is an AME2012 row')
    K.require(tuple(CONFIG['calibrator']) not in labels, 'C-5: the calibrator is a label')
    ck.seal('labels', np.array(labels, dtype=np.int64))
    out = dict(c4='PASS', c5='PASS', n_test=len(labels), test_sha256=man['test_sha256'], ame2020_sha256=man['ame2020_sha256'],
               run_by=man['run_by'], too_small=len(labels) < CONFIG['min_rows'], counts=man['counts'])
    say(f"hold-out {NAME}: {len(labels)} labels, run by {man['run_by']}; anchors within tolerance; sealed/ not opened")
    return out


def unit_predict(ck):
    labels = [tuple(int(v) for v in row) for row in ck.sealed('labels')]
    b_ca = ca40_binding_from(ROOT / 'data' / 'ame2012' / 'AME2012.txt')
    out = dict(b_ca40=float(b_ca), a_c=float(a_c()))
    for label, m in CONFIG['models'].items():
        text, a_v = prediction_lines(labels, b_ca, m)
        p = pred_path(ck, label)
        p.write_text(text)
        preds = np.array([float(l.split()[2]) for l in text.splitlines()[1:]])
        K.finite_array(preds, f'{label} predictions')
        ck.seal(f'pred_{label}', preds)
        out[f'{label}_a_v'] = float(a_v)
        out[f'{label}_file'] = str(p)
        out[f'{label}_sha256'] = hashlib.sha256(text.encode()).hexdigest()
    say(f"predictions written for {len(labels)} labels (M1, M2); sealed in the checkpoint")
    return out


def unit_seal(ck):
    rec = ck.state['records']
    for c in ('c1', 'c2', 'c3'):
        K.require(rec['credential'].get(c) == 'PASS', f'gate: credential {c} did not pass; nothing sealed')
    for c in ('c4', 'c5'):
        K.require(rec['manifest'].get(c) == 'PASS', f'gate: {c} did not pass; nothing sealed')
    hd = holdout_dir(ck)
    mp = hd / 'MANIFEST.json'
    man = json.loads(mp.read_text())
    out = {}
    for label in CONFIG['models']:
        key = f'prediction_sha256_{label}'
        h = sha256_file(pred_path(ck, label))
        K.require(h == rec['predict'][f'{label}_sha256'], f'seal {label}: the prediction file changed since predict')
        if man.get(key):
            K.require(man[key] == h, f'seal {label}: already sealed on a different file; refused')
        else:
            man[key] = h
            man[f'prediction_file_{label}'] = str(pred_path(ck, label).relative_to(ROOT)) if not ck.smoke else str(pred_path(ck, label))
            man[f'prediction_sealed_at_utc_{label}'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
        out[f'{label}_sha256'] = h
    mp.write_text(json.dumps(man, indent=1) + '\n')
    say('predictions sealed in the hold-out manifest (one seal per model)')
    return out


def unit_truth(ck):
    hd = holdout_dir(ck)
    mp = hd / 'MANIFEST.json'
    man = json.loads(mp.read_text())
    rec = ck.state['records']
    test = hd / 'sealed' / 'test.txt'
    out = {}
    if not test.exists():
        ingested = all((hd / f'VERDICT_{label}.json').exists() for label in CONFIG['models'])
        if not ingested:
            raise K.Blocked(f'{test} is not on this machine and no VERDICT_M*.json to ingest (the adjudicator runs the truth step)')
        out['mode'] = 'ingested'
    else:
        K.require(sha256_file(test) == man['test_sha256'], 'truth: sealed test file hash differs from the manifest; not read')
        out['mode'] = 'read-once'
    for label in CONFIG['models']:
        K.require(man.get(f'prediction_sha256_{label}') == rec['seal'][f'{label}_sha256'], f'truth {label}: seal mismatch; not read')
        vfile = hd / f'VERDICT_{label}.json'
        if out['mode'] == 'read-once':
            K.require(not vfile.exists(), f'truth {label}: {vfile.name} exists; a verdict is computed once')
            truth = {}
            for l in test.read_text().splitlines():
                t = l.split()
                if len(t) == 3 and t[0].isdigit():
                    truth[(int(t[0]), int(t[1]))] = float(t[2])
            labels = [tuple(int(v) for v in row) for row in ck.sealed('labels')]
            preds = ck.sealed(f'pred_{label}')
            rows, missing = [], []
            pm = dict(zip(labels, preds.tolist()))
            for (z, n), m in truth.items():
                if (z, n) not in pm:
                    missing.append([z, n]); continue
                r, b = residual_mass(z, n, pm[(z, n)], m)
                rows.append({'Z': z, 'N': n, 'A': z + n, 'truth_B_MeV': b, 'truth_excess_MeV': m, 'pred': pm[(z, n)], 'residual': r})
            v = {'name': NAME, 'label': label, 'unit': 'mass', 'bar_rms': CONFIG['bar_rms'], 'bar_max': CONFIG['bar_max'],
                 'n_test': len(truth), 'n_predicted': len(rows), 'missing_zn': missing,
                 'prediction_sha256': man[f'prediction_sha256_{label}'], 'test_sha256': man['test_sha256'],
                 'computed_at_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'rows': rows,
                 'note': 'residuals only; the verdict (BLIND-*, EXTRAPOLATES/DRIFTS) is rendered once by benchmarks/lab/nuc_new_1/verdict.py'}
            vfile.write_text(json.dumps(v, indent=1) + '\n')
        else:
            v = json.loads(vfile.read_text())
            K.require(v.get('prediction_sha256') == man[f'prediction_sha256_{label}'], f'ingest {label}: VERDICT file is not on the sealed predictions')
            K.require(v.get('test_sha256') == man['test_sha256'], f'ingest {label}: VERDICT file is not on the sealed test set')
        rows = v['rows']
        arr = np.array([[r['Z'], r['N'], r['pred'], r['truth_excess_MeV'], r['residual']] for r in rows], dtype=np.float64) if rows else np.zeros((0, 5))
        ck.seal(f'rows_{label}', arr)
        ck.seal(f'missing_{label}', np.array(v['missing_zn'], dtype=np.int64).reshape(-1, 2))
        out[f'{label}_n_predicted'] = int(v['n_predicted']); out[f'{label}_n_test'] = int(v['n_test'])
    say(f"truth {out['mode']}: rows sealed; no statistic computed here")
    return out


UNITS = [('credential', unit_credential), ('manifest', unit_manifest), ('predict', unit_predict), ('seal', unit_seal), ('truth', unit_truth)]

if __name__ == '__main__':
    sys.exit(K.Driver(ROOT, SLUG, UNITS, MANIFEST, config=CONFIG).run())
