"""holdout_galaxies.py -- the blind hold-out instrument for section W applied to a table of ROTATION CURVES (SPARC).

The AME tool (holdout_draw.py / holdout_verdict.py) holds out rows of one file. A galaxy table is one file per galaxy
and the truth (Vobs, errV) sits in the same file as the inputs (r, Vgas, Vdisk, Vbul), so this tool SPLITS each
held-out galaxy: the inputs go to analysis/holdout/<name>/inputs/<galaxy>.dat (the commission may read them), the
observed velocities go to analysis/holdout/<name>/sealed/<galaxy>_vobs.dat (read once, by verdict, after the seal).
The training galaxies are listed in train.txt (their files stay where they are; the commission may read them whole).

    python tools/holdout_galaxies.py draw    --name GRV_BLIND_1 --seed 20261009 --n 30 --drawn-by "author"
    python tools/holdout_galaxies.py seal    --name GRV_BLIND_1 --predictions analysis/GRV_BLIND_1_pred.txt
    python tools/holdout_galaxies.py verdict --name GRV_BLIND_1 --predictions analysis/GRV_BLIND_1_pred.txt \
           --bar-rms 0.16 --bar-gal 0.40

draw:    eligible galaxies are those the registered confrontation keeps (benchmarks/gravity/sparc_rar_confrontation.py:
         at least three points passing errV/Vobs < 0.1 with r > 0 and Vobs > 0; the cut is applied here, at draw time,
         because it needs Vobs); n of them are drawn uniformly with a seeded numpy Generator; the manifest records the
         seed, the drawer, the sha256 of every input and sealed file and of the concatenated sealed truth; refuses to
         overwrite an existing hold-out.
seal:    records the predictions file's sha256 (one seal).
verdict: checks the hashes, reads the sealed truth ONCE, applies the registered quality cut, computes the RAR residual
         log10(g_obs) - log10(g_pred) at every kept point of every held-out galaxy, the rms over points and the rms per
         galaxy, the verdict against the two bars (rms over points <= bar_rms; max per-galaxy rms <= bar_gal), writes
         VERDICT.json and refuses to run twice.
Predictions file: 'galaxy r_kpc gpred_SI' per line (one per radius of the inputs file), header line allowed.
"""
import argparse, glob, hashlib, json, os, pathlib, sys, time
import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[1]
TABLE = ROOT / 'data' / 'sparc_rotmod'
KPC, KMS = 3.086e19, 1e3


def sha256(p):
    return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()


def load(f):
    d = np.loadtxt(f)
    return d[None, :] if d.ndim == 1 else d


def kept_mask(r, Vobs, eV):
    return (Vobs > 0) & (eV / np.maximum(Vobs, 1e-9) < 0.1) & (r > 0)


def draw(a):
    hd = ROOT / 'analysis' / 'holdout' / a.name
    if hd.exists():
        sys.exit(f'[holdout] REFUSED: {hd} exists. A redraw after a look is a leak.')
    files = sorted(glob.glob(str(TABLE / '*_rotmod.dat')))
    eligible = []
    for f in files:
        try:
            d = load(f)
        except Exception:
            continue
        if kept_mask(d[:, 0], d[:, 1], d[:, 2]).sum() >= 3:
            eligible.append(os.path.basename(f).replace('_rotmod.dat', ''))
    rng = np.random.default_rng(a.seed)
    test = sorted(rng.choice(eligible, size=a.n, replace=False).tolist())
    train = [g for g in eligible if g not in test]
    (hd / 'inputs').mkdir(parents=True); (hd / 'sealed').mkdir()
    (hd / 'train.txt').write_text('\n'.join(train) + '\n', newline='\n')          # LF on every platform (2026-10-09): hashes must agree across machines
    hashes = {}
    for g in test:
        d = load(TABLE / f'{g}_rotmod.dat')
        inp = hd / 'inputs' / f'{g}.dat'; sl = hd / 'sealed' / f'{g}_vobs.dat'
        np.savetxt(inp, d[:, [0, 3, 4, 5]], fmt='%.6g', newline='\n', header='r_kpc Vgas Vdisk Vbul (km/s); the observed velocities are sealed')
        np.savetxt(sl, d[:, [0, 1, 2]], fmt='%.6g', newline='\n', header='r_kpc Vobs errV (km/s); NOT to be read before the seal')
        hashes[g] = dict(inputs=sha256(inp), sealed=sha256(sl))
    truth_cat = b''.join((hd / 'sealed' / f'{g}_vobs.dat').read_bytes() for g in test)
    man = dict(name=a.name, kind='galaxies', section='W (STRATEGIC_TARGETS, 2026-10-04)', drawn_by=a.drawn_by,
               drawn_at_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), table=str(TABLE.relative_to(ROOT)),
               n_files=len(files), eligible=len(eligible), seed=a.seed, n_test=a.n, n_train=len(train),
               test_galaxies=test, train_sha256=sha256(hd / 'train.txt'), files=hashes,
               test_sha256=hashlib.sha256(truth_cat).hexdigest(),
               rule='The commission reads train.txt, the training galaxies\' files and inputs/<galaxy>.dat only. sealed/ is read once, by verdict, after the predictions are sealed. No redraw.',
               prediction_sha256=None, prediction_sealed_at_utc=None, verdict=None)
    (hd / 'MANIFEST.json').write_text(json.dumps(man, indent=1) + '\n')
    print(f'[holdout] {a.name}: {a.n} galaxies held out of {len(eligible)} eligible ({len(files)} files); seed {a.seed}; drawn by {a.drawn_by}')
    print('[holdout] paste into the locked charter:')
    print(f"  train   sha256 {man['train_sha256']}  (analysis/holdout/{a.name}/train.txt)")
    print(f"  test    sha256 {man['test_sha256']}  (the concatenated sealed truth; NOT to be read)")
    print(f"  held out: {', '.join(test)}")


def seal(a):
    hd = ROOT / 'analysis' / 'holdout' / a.name; mp = hd / 'MANIFEST.json'; man = json.loads(mp.read_text())
    if man.get('prediction_sha256'):
        sys.exit('[holdout] REFUSED: predictions already sealed. One seal.')
    man['prediction_sha256'] = sha256(a.predictions); man['prediction_file'] = str(a.predictions)
    man['prediction_sealed_at_utc'] = time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())
    mp.write_text(json.dumps(man, indent=1) + '\n')
    print(f"[holdout] sealed predictions sha256 {man['prediction_sha256']}  ({a.predictions}); the sealed truth may now be read, once, by verdict")


def verdict(a):
    hd = ROOT / 'analysis' / 'holdout' / a.name; mp = hd / 'MANIFEST.json'; man = json.loads(mp.read_text())
    if (hd / 'VERDICT.json').exists():
        sys.exit('[holdout] REFUSED: VERDICT.json exists. A verdict is computed once and kept.')
    if not man.get('prediction_sha256'):
        sys.exit('[holdout] REFUSED: predictions not sealed.')
    if sha256(a.predictions) != man['prediction_sha256']:
        sys.exit('[holdout] REFUSED: predictions file changed since seal.')
    test = man['test_galaxies']
    truth_cat = b''.join((hd / 'sealed' / f'{g}_vobs.dat').read_bytes() for g in test)
    if hashlib.sha256(truth_cat).hexdigest() != man['test_sha256']:
        sys.exit('[holdout] REFUSED: sealed truth hash mismatch.')
    pred = {}
    for l in pathlib.Path(a.predictions).read_text().splitlines():
        t = l.split()
        if len(t) < 3:
            continue
        try:
            pred.setdefault(t[0], {})[round(float(t[1]), 4)] = float(t[2])
        except ValueError:
            continue
    rows, missing, pergal = [], [], {}
    for g in test:
        tr = load(hd / 'sealed' / f'{g}_vobs.dat'); r, Vobs, eV = tr[:, 0], tr[:, 1], tr[:, 2]
        keep = kept_mask(r, Vobs, eV)
        res = []
        for ri, vo, k in zip(r, Vobs, keep):
            if not k:
                continue
            gp = pred.get(g, {}).get(round(float(ri), 4))
            if gp is None or not gp > 0:
                missing.append([g, float(ri)]); continue
            gobs = (vo * KMS) ** 2 / (ri * KPC)
            res.append(np.log10(gobs) - np.log10(gp)); rows.append(dict(galaxy=g, r=float(ri), gobs=float(gobs), gpred=float(gp), residual_dex=float(res[-1])))
        if res:
            pergal[g] = float(np.sqrt(np.mean(np.square(res))))
    allres = np.array([x['residual_dex'] for x in rows])
    rms = float(np.sqrt(np.mean(allres ** 2))); mean = float(np.mean(allres)); galmax = max(pergal.values())
    if missing:
        v = 'BLIND-INCOMPLETE'
    elif rms <= a.bar_rms and galmax <= a.bar_gal:
        v = 'BLIND-AGREES'
    else:
        v = 'BLIND-FAILS'
    out = dict(name=a.name, verdict=v, bar_rms=a.bar_rms, bar_gal=a.bar_gal, rms_dex=rms, mean_dex=mean, n_points=len(rows),
               n_galaxies=len(test), per_galaxy_rms=pergal, max_galaxy_rms=galmax, missing=missing,
               computed_at_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()), rows=rows)
    (hd / 'VERDICT.json').write_text(json.dumps(out, indent=1) + '\n'); man['verdict'] = v; mp.write_text(json.dumps(man, indent=1) + '\n')
    print(f'[holdout] {a.name}: {len(rows)} kept points in {len(test)} held-out galaxies; RAR residual rms {rms:.4f} dex (mean {mean:+.4f}); '
          f'worst galaxy rms {galmax:.4f}; bars rms <= {a.bar_rms}, galaxy <= {a.bar_gal}')
    for g, x in sorted(pergal.items(), key=lambda kv: -kv[1])[:5]:
        print(f'[holdout]   worst: {g:12s} rms {x:.4f} dex')
    print(f'[holdout] VERDICT: {v}  -> analysis/holdout/{a.name}/VERDICT.json (kept)')


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('cmd', choices=['draw', 'seal', 'verdict'])
    ap.add_argument('--name', required=True); ap.add_argument('--seed', type=int); ap.add_argument('--n', type=int, default=30)
    ap.add_argument('--drawn-by'); ap.add_argument('--predictions'); ap.add_argument('--bar-rms', type=float); ap.add_argument('--bar-gal', type=float)
    a = ap.parse_args()
    {'draw': draw, 'seal': seal, 'verdict': verdict}[a.cmd](a)


if __name__ == '__main__':
    main()
