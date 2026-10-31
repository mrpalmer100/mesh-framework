#!/usr/bin/env python3
"""NUC-FORECAST-1: build the sealed forecast of unmeasured nuclear masses, once.

Registration: analysis/NUC_FORECAST_1_PREREGISTERED.md (sealed before this tool existed). The forecast set F is
every (Z, N) in the pinned AME2020 table whose mass excess is from systematics ('#'), with A >= 12 and not a row of
data/ame2012/AME2012.txt. The two frozen models of NUC-NEW-5 (M1 NUC-018 three-term; M2 NUC-A/B four-term) predict
the binding of every row of F from (Z, N) and AME2012's Ca-40 alone; the arithmetic is imported from
benchmarks/lab/nuc_new_5/driver.py, and the tool refuses unless each recomputed a_V equals the value recorded in
NUC-NEW-5's checkpoint to 1e-12 (the run binding of credential C-1).

The tool reads the '#' flag of every AME2020 row and the mass value of none of them: no AME2020 value enters the
forecast. It prints counts and hashes, never a mass. It refuses if the file's hash is not the pin, if the output
directory already holds a manifest, or if any label of F is in NUC-NEW-1's hold-out labels or in AME2012.

    python3 tools/nuc_forecast.py --ame2020 /path/to/mass_1.mas20 [--run-by NAME]
"""
import argparse
import hashlib
import json
import pathlib
import pickle
import subprocess
import sys
import time

ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / 'tools'))
import ame2020_newset as NS                                     # noqa: E402  the credentialed parser (NUC-NEW-5, C-3 and C-7)
from benchmarks.lab.nuc_new_5 import driver as D                # noqa: E402  the models, byte-bound by NUC-NEW-5's C-1

NAME = 'NUC_FORECAST_1'
OUT = ROOT / 'analysis' / 'forecast' / NAME
REG = 'analysis/NUC_FORECAST_1_PREREGISTERED.md'
HOLDOUT_LABELS = ROOT / 'analysis' / 'holdout' / 'NUC_NEW_1' / 'labels.txt'
CKPT = ROOT / 'analysis' / 'nuc_new_5_ckpt.pkl'
PINS = dict(ame2020_sha256='e8599c6d7f724fac91934e59f1b9de8fb8f63e820f4b39456b790665ed2a3307',
            ame2012_sha256='88c6272c9e4117d68ac1317e2590c9e376d25f77c9bf68fd6062bbb4e238cb13')
MIN_A = 12
BIND_TOL = 1e-12
RULE = ('F: every (Z, N) of the pinned AME2020 table whose mass excess is from systematics, A >= 12, not a row of '
        'AME2012.txt. Predictions by the frozen NUC-NEW-5 models (a_V on AME2012 Ca-40 only). Scored on the first '
        'Atomic Mass Evaluation published after this commit, on the rows of F it lists as experimental, under bar W '
        '(rms <= 0.25, max <= 0.60 percent of mass) and the extrapolation ratio rho <= 2 against NUC-BLIND-2\'s '
        'in-sample rms, min 30 rows; no row added or removed; a new scoring commission with its own sealed design. '
        'See analysis/NUC_FORECAST_1_PREREGISTERED.md.')


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def refuse(msg):
    print(f'[forecast] REFUSED: {msg}', flush=True)
    sys.exit(2)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--ame2020', required=True, help='path to mass_1.mas20 (AME2020)')
    ap.add_argument('--run-by', default='mark')
    a = ap.parse_args()

    if (OUT / 'MANIFEST.json').exists():
        refuse(f'{OUT / "MANIFEST.json"} exists; the forecast is built once (a change is a new name)')
    raw = pathlib.Path(a.ame2020).read_bytes()
    h20 = sha256_bytes(raw)
    if h20 != PINS['ame2020_sha256']:
        refuse(f'AME2020 sha256 {h20[:16]}... is not the pin {PINS["ame2020_sha256"][:16]}...')
    h12 = sha256_bytes((ROOT / 'data' / 'ame2012' / 'AME2012.txt').read_bytes())
    if h12 != PINS['ame2012_sha256']:
        refuse(f'AME2012 sha256 {h12[:16]}... is not the pin')
    ame2012 = NS.read_ame2012()
    rows = NS.parse_mas20(raw.decode('utf-8', errors='replace'))
    if len(rows) < NS.MIN_ROWS_PARSED:
        refuse(f'parsed only {len(rows)} rows; the layout was not recognised')
    # the flag of every row is read; the value of none is used past this line
    syst = sorted(k for k, (v, flagged) in rows.items() if flagged)
    light = [k for k in syst if k[0] + k[1] < MIN_A]
    in2012 = [k for k in syst if k[0] + k[1] >= MIN_A and k in ame2012]
    F = [k for k in syst if k[0] + k[1] >= MIN_A and k not in ame2012]
    held = {tuple(int(v) for v in l.split()[:2]) for l in HOLDOUT_LABELS.read_text().splitlines() if l.strip() and not l.startswith('Z')}
    clash = [k for k in F if k in held]
    if clash:
        refuse(f'{len(clash)} labels of F are in NUC-NEW-1\'s hold-out: {clash[:5]}')
    if not F:
        refuse('F is empty')

    # the models, bound to NUC-NEW-5's credentialed constants
    st = pickle.loads(CKPT.read_bytes())
    rec = st['records']['credential']
    b_ca = D.ca40_binding_from(ROOT / 'data' / 'ame2012' / 'AME2012.txt')
    if abs(float(b_ca) - float(rec['c1_b_ca40'])) > BIND_TOL:
        refuse(f'Ca-40 binding {b_ca!r} differs from NUC-NEW-5\'s credentialed {rec["c1_b_ca40"]!r}')
    preds, a_vs = {}, {}
    for label, m in D.CONFIG['models'].items():
        text, a_v = D.prediction_lines(F, b_ca, m)
        if abs(float(a_v) - float(rec[f'c1_{label}_a_v'])) > BIND_TOL:
            refuse(f'{label} a_V {a_v!r} differs from NUC-NEW-5\'s credentialed {rec[f"c1_{label}_a_v"]!r}')
        preds[label], a_vs[label] = text, float(a_v)

    reg_commit = subprocess.run(['git', 'log', '-1', '--format=%H', '--', REG], cwd=ROOT, capture_output=True,
                                text=True).stdout.strip()
    OUT.mkdir(parents=True, exist_ok=False)
    labels_text = 'Z N\n' + ''.join(f'{z} {n}\n' for z, n in F)
    (OUT / 'labels.txt').write_text(labels_text)
    man = dict(name=NAME, registration=REG, registration_commit=reg_commit, built_at_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
               built_by=a.run_by, ame2020_sha256=h20, ame2012_sha256=h12, labels_sha256=sha256_bytes(labels_text.encode()),
               n_forecast=len(F), counts=dict(ame2020_rows=len(rows), ame2020_systematics=len(syst), systematics_a_below_12=len(light),
                                               systematics_in_ame2012=len(in2012), n_forecast=len(F)),
               a_range=[min(z + n for z, n in F), max(z + n for z, n in F)], z_max=max(z for z, n in F),
               models={label: dict(**D.CONFIG['models'][label], a_v=a_vs[label], a_c=float(D.a_c()), calibrator='Ca-40 AME2012',
                                   b_ca40=float(b_ca), bound_to='analysis/nuc_new_5_ckpt.pkl records.credential', bind_tol=BIND_TOL)
                       for label in preds},
               rule=RULE)
    for label, text in preds.items():
        (OUT / f'pred_{label}.txt').write_text(text)
        man[f'pred_{label}_sha256'] = sha256_bytes(text.encode())
        man[f'pred_{label}_file'] = f'analysis/forecast/{NAME}/pred_{label}.txt'
    (OUT / 'MANIFEST.json').write_text(json.dumps(man, indent=1) + '\n')
    print(f'[forecast] |F| = {len(F)} (systematics rows {len(syst)}; A < 12 excluded {len(light)}; in AME2012 excluded {len(in2012)}); '
          f'A {man["a_range"][0]} to {man["a_range"][1]}, Z <= {man["z_max"]}')
    print(f'[forecast] a_V M1 {a_vs["M1"]!r}  M2 {a_vs["M2"]!r}  (equal to NUC-NEW-5\'s credentialed values to {BIND_TOL})')
    print(f'[forecast] labels sha256 {man["labels_sha256"]}')
    for label in preds:
        print(f'[forecast] pred_{label} sha256 {man[f"pred_{label}_sha256"]}')
    print(f'[forecast] manifest sha256 {sha256_bytes((OUT / "MANIFEST.json").read_bytes())}')
    print(f'[forecast] registration commit {reg_commit[:10]}; written to {OUT}; no mass value printed or read')


if __name__ == '__main__':
    main()
