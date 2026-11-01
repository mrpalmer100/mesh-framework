"""COMMISSION NUC-NEW-3 -- the two adjudicated nuclear mass models on the 128 nuclides first measured between AME2012
and AME2020. Design sealed before this file was amended: analysis/NUC_NEW_3_design_SEALED.md (supersedes NUC_NEW_2's
design, whose sealed C-6(b) bar failed on the real-file audit; NUC_NEW_2's superseded NUC_NEW_1's after its three-round
lock rejection; the set, the models and Q1 are unchanged throughout and pinned by hash).
Harness: benchmarks/lab/_kit/labkit.py (Driver / Checkpoint / Halt); verdict in verdict.py; one CONFIG shared.
Nothing here waits on a person: the hold-out analysis/holdout/NUC_NEW_1/ (built 2026-10-31, commit 7d23981) and its
AUDIT.json are in the repository; there is no adjudicated variant and no ingestion path.

Units, in the locked order, one per invocation (resumable):
  credential  C-1 the model arithmetic reproduces NUC-BLIND-2's sealed prediction files byte for byte;
              C-2 the residual rule reproduces NUC-BLIND-1's and NUC-BLIND-2's published VERDICT rows, rms and max;
              C-3 tools/ame2020_newset.py (build and audit) on a SYNTHETIC mas20-layout fixture recovers the planted
              set and counts exactly; and the Q2 sampling floor F per model (design section 6: bootstrap, seed
              20261031, 10000 resamples, on the 100 published in-sample residuals, at |T| = 128) is computed and
              recorded BEFORE any evidence file is opened. A failure is a Halt (INSTRUMENT-OPEN).
  manifest    reads MANIFEST.json, labels.txt and AUDIT.json. The manifest's ame2020/labels/test hashes and n_test must
              equal the PINS in CONFIG (never trusted); C-4 anchors; C-5 labels; C-6 the audit bars. Never opens
              sealed/. A missing file is a Halt, not a wait.
  predict     M1 and M2 at the labels from AME2012's Ca-40; arrays sealed; analysis/NUC_NEW_3_pred_M*.txt written.
  seal        the two prediction files' sha256 recorded in the hold-out MANIFEST (one seal each; refuses a second).
  truth       the ONE read of sealed/test.txt, whose sha256 must equal the pin AND the hash the manifest unit recorded:
              parsed once into one raw array (Z, N, M), labels unique and equal to the sealed label set, sealed raw;
              both models' rows derive from that one payload; VERDICT_M*.json written as a record (the NUC-BLIND-2
              schema); the rows sealed.
The driver never prints a FORM line, a residual, an rms or a max; the verdict does, once.

LAB_SMOKE=1: every unit in one process on a THROWAWAY hold-out built in a temporary directory from the synthetic
fixture (its truth is the fixture's planted numbers; the pins are the fixture's own hashes, recorded by the
credential unit), checkpoint analysis/nuc_new_3_smoke.pkl; the evidence hold-out and checkpoint are never touched.
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

SLUG = 'nuc_new_3'
NAME = 'NUC_NEW_3'
HOLDOUT = 'NUC_NEW_1'          # the hold-out keeps its name: the design fixes the set, not the commission name
MANIFEST = ['benchmarks/lab/_kit/labkit.py', 'benchmarks/lab/nuc_new_3/driver.py', 'benchmarks/lab/nuc_new_3/verdict.py',
            'tools/ame2020_newset.py', 'benchmarks/nuclear/nuc_blind_1.py', 'data/ame2012/AME2012.txt',
            'analysis/NUC_NEW_3_design_SEALED.md', 'analysis/NUC_NEW_2_design_SEALED.md', 'analysis/NUC_NEW_1_design_SEALED.md',
            'analysis/holdout/NUC_BLIND_2/MANIFEST.json', 'analysis/holdout/NUC_BLIND_2/train.txt',
            'analysis/NUC_BLIND_2_pred_M1.txt', 'analysis/NUC_BLIND_2_pred_M2.txt',
            'analysis/holdout/NUC_BLIND_1/VERDICT_M1.json', 'analysis/holdout/NUC_BLIND_1/VERDICT_M2.json',
            'analysis/holdout/NUC_BLIND_2/VERDICT_M1.json', 'analysis/holdout/NUC_BLIND_2/VERDICT_M2.json',
            'analysis/holdout/NUC_NEW_1/labels.txt', 'analysis/holdout/NUC_NEW_1/AUDIT.json']
CONFIG = dict(
    # the models (design section 3; nuc_blind_1.py's constants, copied, credentialed by C-1)
    d_h=7.28897059, d_n=8.07131714, d0_fm=2.026, coulomb_factor=0.6 * 1.44,
    models={'M1': dict(as_over_av=1.34, a_a=0.0), 'M2': dict(as_over_av=1.108, a_a=19.85)},
    calibrator=[20, 20], min_a=12,
    # the house unit (design section 5)
    m_p=938.272, m_n=939.565, m_e=0.511,
    # bars (design section 6)
    bar_rms=0.25, bar_max=0.60, extrap_factor=2.0, min_rows=30,
    # the Q2 sampling floor (design section 6): bootstrap on the pooled NUC-BLIND-1 + NUC-BLIND-2 residuals per model
    floor_seed=20261031, floor_resamples=10000, floor_ref_n=50, floor_percentile=99.0,
    # the Q3 permutation null (design section 5): no form, no claim
    q3_seed=20261031, q3_permutations=1000, q3_percentile=99.0,
    # credentials (design section 4)
    c1_sha={'M1': 'edb67e2410176d86ef15f4644e58e6932a912efab6104ff32fe8b3af7d30b363',
            'M2': 'a5f3f8e01f6c213efcbd4e44c934db33e400b0b6dca68f2f0d94dc4dd44a51c9'},
    c2_tol=1e-9, anchor_tol_MeV=0.010, bind_tol=1e-9,
    # C-6 audit bars (NUC_NEW_3 design section 4(b), fixed with the NUC-NEW-2 audit disclosed; (a), (c) from NUC_NEW_2's)
    audit_tol_MeV=0.100, audit_min_fraction_within=0.90, audit_max_shift_MeV=5.0, audit_min_shared=2389,
    audit_experimental_band=[2400, 2700], audit_max_absent=50,
    # the pins (design section 2): the evidence as built on 2026-10-31 (commit 7d23981); the manifest must equal them
    pins=dict(n_test=128,
              ame2020_sha256='e8599c6d7f724fac91934e59f1b9de8fb8f63e820f4b39456b790665ed2a3307',
              ame2012_sha256='88c6272c9e4117d68ac1317e2590c9e376d25f77c9bf68fd6062bbb4e238cb13',
              labels_sha256='2387278737460b207fc8b4d5637ad5426cfe4f0981686ee187fac20f2012298a',
              test_sha256='71658bb61b80507f68e2d1e19b5cc56fa4853447c848a4568137771b37b6534b'),
    # the sub-reading channels (design Q3)
    asym_coeff=23.0,
)
SMOKE = os.environ.get('LAB_SMOKE') == '1'
TAG = '[nuc-new-3]'


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
    header = ['1   AME2020 synthetic fixture (NUC-NEW-3 credential C-3): AME2012 rows in the mas20 layout plus planted rows',
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
    return ROOT / 'analysis' / 'holdout' / HOLDOUT


def pins(ck):
    """The evidence pins: CONFIG's (design section 2); in the smoke, the fixture's own hashes recorded by the credential
    unit, so the same equality checks run on the throwaway hold-out."""
    if ck.smoke:
        p = ck.state['records'].get('credential', {}).get('smoke_pins')
        K.require(p is not None, 'smoke: no pins recorded by the credential unit')
        return p
    return CONFIG['pins']


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
    # C-2: the residual rule on the published VERDICT rows of both blind sets; the pooled residuals feed the floor
    n_test_pin = CONFIG['pins']['n_test']
    for label in CONFIG['models']:
        pool = []
        for blind in ('NUC_BLIND_1', 'NUC_BLIND_2'):
            v = json.loads((ROOT / 'analysis' / 'holdout' / blind / f'VERDICT_{label}.json').read_text())
            res = []
            for r in v['rows']:
                rr, b = residual_mass(r['Z'], r['N'], r['pred'], r['truth_excess_MeV'])
                K.require(abs(rr - r['residual']) < CONFIG['c2_tol'], f'C-2 {blind} {label}: row residual differs at Z={r["Z"]} N={r["N"]}')
                res.append(rr)
            res = np.array(res)
            rms, mx = float(np.sqrt(np.mean(res ** 2))), float(np.max(np.abs(res)))
            K.require(abs(rms - v['rms']) < CONFIG['c2_tol'] and abs(mx - v['max_abs']) < CONFIG['c2_tol'],
                      f'C-2 {blind} {label}: rms/max {rms:.9f}/{mx:.9f} differ from the published {v["rms"]:.9f}/{v["max_abs"]:.9f}')
            if blind == 'NUC_BLIND_2':
                out[f'c2_{label}_rms_ref'] = float(v['rms'])          # the Q2 reference, read from the file (design section 6)
                out[f'c2_{label}_max_ref'] = float(v['max_abs'])
            pool.extend(res.tolist())
        pool = np.array(pool)
        K.require(pool.shape[0] == 100, f'C-2 {label}: the pooled in-sample residuals are {pool.shape[0]} rows, not 100')
        ck.seal(f'pool_{label}', pool)
        # the Q2 sampling floor F (design section 6), from the disjoint resource, before any evidence file is opened
        rng = np.random.default_rng(CONFIG['floor_seed'])
        ratios = np.empty(CONFIG['floor_resamples'])
        for i in range(CONFIG['floor_resamples']):
            ref = rng.choice(pool, size=CONFIG['floor_ref_n'], replace=True)
            tst = rng.choice(pool, size=n_test_pin, replace=True)
            ratios[i] = np.sqrt(np.mean(tst ** 2)) / np.sqrt(np.mean(ref ** 2))
        F = float(np.percentile(ratios, CONFIG['floor_percentile']))
        K.finite(F, f'floor {label}')
        out[f'floor_{label}'] = F
        out[f'floor_{label}_median'] = float(np.median(ratios))
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
    au = NS.audit(text, ame2012, CONFIG['audit_tol_MeV'])
    K.require(au['shared'] == len(ame2012) - 1 and au['beyond'] == 0 and au['max_abs_shift_MeV'] < 1e-6,
              f"C-3 audit: shared {au['shared']} (expected {len(ame2012) - 1}), beyond {au['beyond']}, max shift {au['max_abs_shift_MeV']}")
    K.require(au['counts']['ame2012_absent_from_ame2020'] == 1 and au['counts']['ame2020_systematics'] == 2, 'C-3 audit: counts not recovered')
    out['c3'] = 'PASS'
    out['c3_n_test'] = len(r['test'])
    if ck.smoke:
        # the throwaway hold-out and its audit, built by the tool's main() so the smoke runs the same path the lab machine ran
        import subprocess
        sroot = tmp / 'smoke_root'
        (sroot / 'analysis').mkdir(parents=True)
        base = [sys.executable, str(ROOT / 'tools' / 'ame2020_newset.py'), '--ame2020', str(tmp / 'synthetic.mas20'),
                '--run-by', 'smoke', '--name', HOLDOUT, '--out-root', str(sroot)]
        p = subprocess.run(base, capture_output=True, text=True)
        K.require(p.returncode == 0, f'smoke: the set tool failed: {p.stderr[-500:]}')
        p = subprocess.run(base + ['--audit'], capture_output=True, text=True)
        K.require(p.returncode == 0, f'smoke: the audit failed: {p.stderr[-500:]}')
        hd = sroot / 'analysis' / 'holdout' / HOLDOUT
        out['smoke_holdout'] = str(hd)
        out['smoke_pins'] = dict(n_test=len(r['test']), ame2020_sha256=hashlib.sha256(text.encode()).hexdigest(),
                                 ame2012_sha256=sha256_file(NS.AME2012), labels_sha256=sha256_file(hd / 'labels.txt'),
                                 test_sha256=sha256_file(hd / 'sealed' / 'test.txt'))
    return out


def unit_manifest(ck):
    hd = holdout_dir(ck)
    mp = hd / 'MANIFEST.json'
    K.require(mp.exists(), f'hold-out {hd} is not in the repository (design section 2: built 2026-10-31, commit 7d23981)')
    man = json.loads(mp.read_text())
    P = pins(ck)
    K.require(man.get('name') == HOLDOUT, 'manifest: wrong hold-out name')
    for k in ('ame2020_sha256', 'ame2012_sha256', 'labels_sha256', 'test_sha256'):
        K.require(man.get(k) == P[k], f'pin: manifest {k} {str(man.get(k))[:16]} differs from the pinned {P[k][:16]}')
    K.require(int(man['n_test']) == P['n_test'], f"pin: manifest n_test {man['n_test']} differs from the pinned {P['n_test']}")
    K.require(sha256_file(NS.AME2012) == P['ame2012_sha256'], 'pin: data/ame2012/AME2012.txt differs from the pinned table')
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
    K.require(len(labels) == P['n_test'], 'C-5: the label count differs from the pin')
    ck.seal('labels', np.array(labels, dtype=np.int64))
    # C-6: the real-file audit, written once by the tool on the machine holding the file; bars from CONFIG
    ap = hd / 'AUDIT.json'
    K.require(ap.exists(), f'C-6: {ap} is not in the repository (tools/ame2020_newset.py --audit)')
    au = json.loads(ap.read_text())
    K.require(au.get('name') == HOLDOUT and au.get('ame2020_sha256') == P['ame2020_sha256'], 'C-6: the audit is not of the pinned file')
    K.require(au.get('labels_sha256') == P['labels_sha256'] and au.get('test_sha256') == P['test_sha256'], 'C-6: the audit is not of this hold-out')
    K.require(abs(float(au['tol_MeV']) - CONFIG['audit_tol_MeV']) < 1e-12, 'C-6: the audit tolerance is not the locked one')
    K.require(au['shared'] >= CONFIG['audit_min_shared'], f"C-6: shared rows {au['shared']} < {CONFIG['audit_min_shared']}")
    K.require(au['fraction_within'] >= CONFIG['audit_min_fraction_within'],
              f"C-6: {au['fraction_within']:.4f} of the shared rows within {CONFIG['audit_tol_MeV']} MeV (bar {CONFIG['audit_min_fraction_within']})")
    K.require(float(au['max_abs_shift_MeV']) <= CONFIG['audit_max_shift_MeV'],
              f"C-6: largest shift among the shared rows {au['max_abs_shift_MeV']:.4f} MeV > {CONFIG['audit_max_shift_MeV']}")
    lo, hi = CONFIG['audit_experimental_band']
    K.require(lo <= au['counts']['ame2020_experimental'] <= hi, f"C-6: experimental rows {au['counts']['ame2020_experimental']} outside [{lo}, {hi}]")
    K.require(au['counts']['ame2012_absent_from_ame2020'] <= CONFIG['audit_max_absent'], 'C-6: too many AME2012 rows absent')
    K.require(au['counts'] == {k: man['counts'][k] for k in au['counts']}, 'C-6: the audit counts differ from the manifest counts')
    out = dict(c4='PASS', c5='PASS', c6='PASS', n_test=len(labels), test_sha256=man['test_sha256'], ame2020_sha256=man['ame2020_sha256'],
               run_by=man['run_by'], too_small=len(labels) < CONFIG['min_rows'], counts=man['counts'],
               audit=dict(shared=au['shared'], within=au['within'], beyond=au['beyond'], max_abs_shift_MeV=au['max_abs_shift_MeV']))
    say(f"hold-out {HOLDOUT}: {len(labels)} labels, run by {man['run_by']}; pins equal; anchors and audit within the bars; sealed/ not opened")
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
    for c in ('c4', 'c5', 'c6'):
        K.require(rec['manifest'].get(c) == 'PASS', f'gate: {c} did not pass; nothing sealed')
    for label in CONFIG['models']:
        K.require(f'floor_{label}' in rec['credential'], f'gate: the Q2 floor for {label} was not recorded; nothing sealed')
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
    P = pins(ck)
    test = hd / 'sealed' / 'test.txt'
    K.require(test.exists(), f'{test} is not in the repository; the truth is read here or not at all')
    for label in CONFIG['models']:
        K.require(man.get(f'prediction_sha256_{label}') == rec['seal'][f'{label}_sha256'], f'truth {label}: seal mismatch; not read')
        K.require(not (hd / f'VERDICT_{label}.json').exists(), f'truth {label}: VERDICT_{label}.json exists; a verdict is computed once')
    h = sha256_file(test)
    K.require(h == P['test_sha256'] == rec['manifest']['test_sha256'], 'truth: sealed test file hash differs from the pin or the manifest record; not read')
    # the ONE read: one raw payload, parsed once, bound to the sealed labels before any residual
    raw = test.read_bytes()
    K.require(hashlib.sha256(raw).hexdigest() == h, 'truth: the bytes read differ from the file hashed')
    truth = []
    for l in raw.decode().splitlines():
        t = l.split()
        if len(t) == 3 and t[0].isdigit():
            truth.append((int(t[0]), int(t[1]), float(t[2])))
    labels = [tuple(int(v) for v in row) for row in ck.sealed('labels')]
    tl = [(z, n) for z, n, _ in truth]
    K.require(len(set(tl)) == len(tl), 'truth: duplicate label in the truth file')
    K.require(set(tl) == set(labels) and len(tl) == len(labels), 'truth: the truth labels are not the sealed labels')
    truth_arr = np.array(truth, dtype=np.float64)
    K.finite_array(truth_arr, 'truth payload')
    ck.seal('truth_raw', truth_arr)
    out = dict(mode='read-once', test_sha256=h, n_truth=len(truth))
    for label in CONFIG['models']:
        preds = ck.sealed(f'pred_{label}')
        pm = dict(zip(labels, preds.tolist()))
        rows, missing = [], []
        for z, n, m in truth:
            p = pm.get((z, n))
            if p is None or not np.isfinite(p):
                missing.append([z, n]); continue
            r, b = residual_mass(z, n, p, m)
            rows.append({'Z': z, 'N': n, 'A': z + n, 'truth_B_MeV': b, 'truth_excess_MeV': m, 'pred': p, 'residual': r})
        v = {'name': NAME, 'holdout': HOLDOUT, 'label': label, 'unit': 'mass', 'bar_rms': CONFIG['bar_rms'], 'bar_max': CONFIG['bar_max'],
             'n_test': len(truth), 'n_predicted': len(rows), 'missing_zn': missing,
             'prediction_sha256': man[f'prediction_sha256_{label}'], 'test_sha256': h,
             'computed_at_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'rows': rows,
             'note': 'a record only; the verdict (BLIND-*, EXTRAPOLATES/WITHIN-FLOOR/DRIFTS) is rendered once by benchmarks/lab/nuc_new_3/verdict.py from the sealed arrays'}
        (hd / f'VERDICT_{label}.json').write_text(json.dumps(v, indent=1) + '\n')
        arr = np.array([[r['Z'], r['N'], r['pred'], r['truth_excess_MeV'], r['residual']] for r in rows], dtype=np.float64) if rows else np.zeros((0, 5))
        ck.seal(f'rows_{label}', arr)
        ck.seal(f'missing_{label}', np.array(missing, dtype=np.int64).reshape(-1, 2))
        out[f'{label}_n_predicted'] = len(rows)
    say('truth read once: raw payload and rows sealed; no statistic computed here')
    return out


UNITS = [('credential', unit_credential), ('manifest', unit_manifest), ('predict', unit_predict), ('seal', unit_seal), ('truth', unit_truth)]

if __name__ == '__main__':
    sys.exit(K.Driver(ROOT, SLUG, UNITS, MANIFEST, config=CONFIG).run())
