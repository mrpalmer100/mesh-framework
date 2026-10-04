"""holdout_draw.py -- the blind hold-out instrument for section W (STRATEGIC_TARGETS, adopted 2026-10-04).

Draws a pre-registered TEST SET from a measured table before a commission's charter locks, seals it by sha256,
and writes the TRAINING remainder the commission is allowed to read. The commission reads train.txt only; the
verdict tool (tools/holdout_verdict.py) is the only reader of test.txt, and it reads it once.

    python tools/holdout_draw.py --name NUC_BLIND_1 --seed 20261004 --n 50 --drawn-by "author"
    python tools/holdout_draw.py --name NUC_BLIND_1 --seed 20261004 --n 50 --drawn-by "author" --exclude 20,20

Writes analysis/holdout/<name>/{train.txt, sealed/test.txt, MANIFEST.json} and prints the three sha256 lines to
paste into the locked charter. Rows are the table's rows with A >= 12 (the registered nuclear-sector scope,
NUC-005/018); the calibrator rows named by --exclude (default Ca-40, Z=20 N=20) are never drawn into the test set
because a held-out calibrator is not a prediction. The draw is uniform over the eligible rows with a seeded
numpy Generator; the seed, the table's hash and the drawer's name are in the manifest, so the draw is
reproducible and attributable. Refuses to overwrite an existing hold-out (a redraw after a look is a leak).
"""
import argparse, hashlib, json, pathlib, sys, time
import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[1]
DEFAULT_TABLE = ROOT / 'data' / 'ame2012' / 'AME2012.txt'


def sha256(p):
    return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()


def load(table):
    lines = pathlib.Path(table).read_text().splitlines()
    header, rows = lines[0], [l.split() for l in lines[1:] if l.strip()]
    return header, rows


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--name', required=True, help='hold-out name, becomes analysis/holdout/<name>/')
    ap.add_argument('--seed', required=True, type=int, help='recorded; the draw is reproducible from it')
    ap.add_argument('--n', type=int, default=50, help='test-set size (section W standing size for AME: 50)')
    ap.add_argument('--drawn-by', required=True, help='who ran the draw (section W1: a process other than the commission)')
    ap.add_argument('--table', default=str(DEFAULT_TABLE))
    ap.add_argument('--min-a', type=int, default=12, help='eligible rows have A >= this (registered scope)')
    ap.add_argument('--exclude', default='20,20', help='Z,N pairs never drawn (calibrators); semicolon-separated')
    a = ap.parse_args()

    out = ROOT / 'analysis' / 'holdout' / a.name
    if out.exists():
        sys.exit(f'[holdout] REFUSED: {out} exists. A redraw after a look is a leak; use a new --name.')
    header, rows = load(a.table)
    excl = {tuple(int(x) for x in pair.split(',')) for pair in a.exclude.split(';') if pair.strip()}
    Z = np.array([int(r[0]) for r in rows]); N = np.array([int(r[1]) for r in rows])
    eligible = np.where((Z + N >= a.min_a) & np.array([(z, n) not in excl for z, n in zip(Z, N)]))[0]
    if a.n > len(eligible):
        sys.exit(f'[holdout] REFUSED: n={a.n} exceeds {len(eligible)} eligible rows')
    rng = np.random.default_rng(a.seed)
    test_idx = np.sort(rng.choice(eligible, size=a.n, replace=False))
    test_set = set(test_idx.tolist())

    (out / 'sealed').mkdir(parents=True)
    train = out / 'train.txt'; test = out / 'sealed' / 'test.txt'
    train.write_text('\n'.join([header] + [' '.join(rows[i]) for i in range(len(rows)) if i not in test_set]) + '\n')
    test.write_text('\n'.join([header] + [' '.join(rows[i]) for i in test_idx]) + '\n')
    man = {
        'name': a.name, 'section': 'W (STRATEGIC_TARGETS, 2026-10-04)', 'drawn_by': a.drawn_by,
        'drawn_at_utc': time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
        'table': str(pathlib.Path(a.table).relative_to(ROOT)) if str(a.table).startswith(str(ROOT)) else a.table,
        'table_sha256': sha256(a.table), 'table_rows': len(rows), 'eligible_rows': int(len(eligible)),
        'min_a': a.min_a, 'excluded_calibrators': sorted(list(x) for x in excl),
        'seed': a.seed, 'n_test': a.n, 'n_train': len(rows) - a.n,
        'train_sha256': sha256(train), 'test_sha256': sha256(test),
        'test_zn': [[int(Z[i]), int(N[i])] for i in test_idx],
        'rule': 'The commission reads train.txt only. test.txt is read once, by tools/holdout_verdict.py, after '
                'the predictions file is sealed. No redraw.',
        'prediction_sha256': None, 'prediction_sealed_at_utc': None, 'verdict': None,
    }
    (out / 'MANIFEST.json').write_text(json.dumps(man, indent=1) + '\n')
    print(f'[holdout] {a.name}: {a.n} test rows held out of {len(eligible)} eligible (table {len(rows)} rows, A >= {a.min_a}, '
          f'calibrators excluded {sorted(excl)}); seed {a.seed}; drawn by {a.drawn_by}')
    print(f'[holdout] paste into the locked charter:')
    print(f'  table   sha256 {man["table_sha256"]}  ({man["table"]})')
    print(f'  train   sha256 {man["train_sha256"]}  (analysis/holdout/{a.name}/train.txt)')
    print(f'  test    sha256 {man["test_sha256"]}  (analysis/holdout/{a.name}/sealed/test.txt; NOT to be read)')


if __name__ == '__main__':
    main()
