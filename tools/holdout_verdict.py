"""holdout_verdict.py -- seal a prediction file, then read the held-out truth once and compute the verdict once.

Section W (STRATEGIC_TARGETS, adopted 2026-10-04). Two subcommands, in this order:

    python tools/holdout_verdict.py seal    --name NUC_BLIND_1 --predictions analysis/NUC_BLIND_1_pred.txt
    python tools/holdout_verdict.py verdict --name NUC_BLIND_1 --predictions analysis/NUC_BLIND_1_pred.txt \
           --bar-rms 0.5 --bar-max 2.0 --unit percent

seal:    records the predictions file's sha256 and the time into MANIFEST.json. After this the file may not change.
         Refuses if a prediction hash is already sealed (one seal, one verdict).
verdict: checks the sealed test file's hash against the manifest, checks the predictions file's hash against the
         seal, reads both ONCE, computes the residuals on the held-out rows and the verdict against the bars given
         on the command line (which the locked charter must also carry), writes analysis/holdout/<name>/VERDICT.json
         and prints it. Refuses to run if VERDICT.json exists: a verdict is computed once and kept.

Predictions file format: 'Z N value' per line, header line allowed, one row per held-out (Z, N). The value is the
predicted quantity in the units the charter names; --unit says how residuals are reported:
  --unit percent : residual = 100 (pred - truth) / truth, where truth is the binding energy B = Z*D_H + N*D_N - M
                   (the house convention; the predictions are then binding energies in MeV)
  --unit mev     : residual = pred - truth with truth = B in MeV
  --unit excess  : residual = pred - M (the table's mass excess, MeV)
Forms: BLIND-AGREES (rms <= bar_rms and max |residual| <= bar_max); BLIND-FAILS otherwise; BLIND-INCOMPLETE if any
held-out row has no prediction (a missing row is a miss, kept, and the verdict is not AGREES).
"""
import argparse, hashlib, json, pathlib, sys, time
import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[1]
D_H, D_N = 7.28897059, 8.07131714   # the table's own H-1 and n rows (data/ame2012/AME2012.txt)


def sha256(p):
    return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()


def read_zn_table(p):
    out = {}
    for l in pathlib.Path(p).read_text().splitlines():
        t = l.split()
        if len(t) < 3:
            continue
        try:
            z, n, v = int(t[0]), int(t[1]), float(t[2])
        except ValueError:
            continue   # header
        out[(z, n)] = v
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('cmd', choices=['seal', 'verdict'])
    ap.add_argument('--name', required=True)
    ap.add_argument('--predictions', required=True)
    ap.add_argument('--bar-rms', type=float, help='verdict: rms residual bar (charter value)')
    ap.add_argument('--bar-max', type=float, help='verdict: max |residual| bar (charter value)')
    ap.add_argument('--unit', choices=['percent', 'mev', 'excess'], default='percent')
    a = ap.parse_args()

    hd = ROOT / 'analysis' / 'holdout' / a.name
    mp = hd / 'MANIFEST.json'
    if not mp.exists():
        sys.exit(f'[holdout] no hold-out named {a.name} (run tools/holdout_draw.py first)')
    man = json.loads(mp.read_text())
    ph = sha256(a.predictions)

    if a.cmd == 'seal':
        if man.get('prediction_sha256'):
            sys.exit(f'[holdout] REFUSED: predictions already sealed ({man["prediction_sha256"][:16]}...). One seal.')
        man['prediction_sha256'] = ph; man['prediction_file'] = str(a.predictions)
        man['prediction_sealed_at_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
        mp.write_text(json.dumps(man, indent=1) + '\n')
        print(f'[holdout] sealed predictions sha256 {ph}  ({a.predictions}); the held-out truth may now be read, once, by verdict')
        return

    # verdict
    if (hd / 'VERDICT.json').exists():
        sys.exit('[holdout] REFUSED: VERDICT.json exists. A verdict is computed once and kept.')
    if a.bar_rms is None or a.bar_max is None:
        sys.exit('[holdout] verdict needs --bar-rms and --bar-max (the locked charter values)')
    if not man.get('prediction_sha256'):
        sys.exit('[holdout] REFUSED: predictions not sealed. Run seal first; the truth is not read before the seal.')
    if ph != man['prediction_sha256']:
        sys.exit(f'[holdout] REFUSED: predictions file changed since seal ({ph[:16]} != {man["prediction_sha256"][:16]})')
    test = hd / 'sealed' / 'test.txt'
    th = sha256(test)
    if th != man['test_sha256']:
        sys.exit(f'[holdout] REFUSED: sealed test file hash mismatch ({th[:16]} != {man["test_sha256"][:16]})')

    truth = read_zn_table(test); pred = read_zn_table(a.predictions)
    rows, missing = [], []
    for (z, n), m in truth.items():
        if (z, n) not in pred:
            missing.append([z, n]); continue
        b = z * D_H + n * D_N - m
        p = pred[(z, n)]
        if a.unit == 'percent':
            r = 100.0 * (p - b) / b
        elif a.unit == 'mev':
            r = p - b
        else:
            r = p - m
        rows.append({'Z': z, 'N': n, 'A': z + n, 'truth_B_MeV': b, 'truth_excess_MeV': m, 'pred': p, 'residual': r})
    res = np.array([r['residual'] for r in rows]) if rows else np.array([np.nan])
    rms = float(np.sqrt(np.mean(res ** 2))); mx = float(np.max(np.abs(res)))
    if missing:
        verdict = 'BLIND-INCOMPLETE'
    elif rms <= a.bar_rms and mx <= a.bar_max:
        verdict = 'BLIND-AGREES'
    else:
        verdict = 'BLIND-FAILS'
    out = {'name': a.name, 'verdict': verdict, 'unit': a.unit, 'bar_rms': a.bar_rms, 'bar_max': a.bar_max,
           'rms': rms, 'max_abs': mx, 'n_test': len(truth), 'n_predicted': len(rows), 'missing_zn': missing,
           'prediction_sha256': ph, 'test_sha256': th,
           'computed_at_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), 'rows': rows}
    (hd / 'VERDICT.json').write_text(json.dumps(out, indent=1) + '\n')
    man['verdict'] = verdict; mp.write_text(json.dumps(man, indent=1) + '\n')
    print(f'[holdout] {a.name}: {len(rows)}/{len(truth)} held-out rows predicted; residual ({a.unit}) rms {rms:.4g}, '
          f'max |r| {mx:.4g}; bars rms <= {a.bar_rms}, max <= {a.bar_max}')
    for r in sorted(rows, key=lambda r: -abs(r['residual']))[:5]:
        print(f'[holdout]   worst: Z={r["Z"]:3d} N={r["N"]:3d} A={r["A"]:3d}  residual {r["residual"]:+.4g}')
    print(f'[holdout] VERDICT: {verdict}  -> analysis/holdout/{a.name}/VERDICT.json (kept)')


if __name__ == '__main__':
    main()
