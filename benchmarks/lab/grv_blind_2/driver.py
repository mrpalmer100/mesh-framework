"""COMMISSION GRV-BLIND-2 -- GRV-030's zero-parameter prediction g_dagger = c H0 / 2 pi on a fresh 30-galaxy SPARC draw
whose seed was chosen and run by an adjudicator who is neither the author nor the commission. Charter
analysis/GRV_BLIND_2_charter_LOCKED.md (drafted at analysis/lab/drafts/GRV-BLIND-2/charter.md).

Nothing new is invented: the predictor and the bars rule are benchmarks/gravity/grv_blind_1.py (GRV-BLIND-1's, called
unchanged) and the draw, seal and verdict instrument is tools/holdout_galaxies.py (unchanged). This driver orchestrates
them, one unit per invocation, state in analysis/grv_blind_2_ckpt.pkl (atomic write; resumes on every start):

  calib     credential the instruments against GRV-BLIND-1's recorded answers (bars, predictions, the draw, the
            verdict arithmetic): C-1 to C-4. Reads no BLIND-2 file.
  manifest  read the adjudicator's MANIFEST.json (analysis/holdout/GRV_BLIND_2/); refuse to proceed without it; verify the
            draw is reproducible from its seed (C-5). Never opens sealed/.
  predict   the frozen prediction at every radius of every held-out inputs file, the bars from the training galaxies,
            the floor tests F-1 and F-2 (training and inputs only; no truth), the descriptive g_dagger window.
  seal      GATED. tools/holdout_galaxies.py seal (one seal).
  truth     GATED. the ONE read of the sealed truth, by the unchanged tool's verdict (bars from the checkpoint), or ingestion
            of the VERDICT.json that tool already wrote on the machine holding sealed/ (NUC-BLIND-2 pattern). BLOCKED
            (exit 2, not COMPLETE) when neither is possible on this machine.

THE GATE (charter section 4): unit_seal and unit_truth call verdict.pre_truth_gate(), the same function and the same locked
tolerances the verdict script uses. Unless C-1 to C-5 and F-1 and F-2 ALL pass in the checkpoint, they print the reason,
record the failed gate in the checkpoint, and exit 2 with no COMPLETE line: nothing is sealed and the sealed truth is never
read, so a calibration or floor failure cannot consume the one-shot truth of the adjudicator's draw.

LAB_SMOKE=1: runs every unit in one process against a THROWAWAY draw in a temporary directory (seed 777, drawn by
'smoke-adjudicator'), writes analysis/grv_blind_2_smoke.pkl and never the evidence checkpoint; evidence-free.
LAB_SMOKE_FAULT=calib|floor (honoured only with LAB_SMOKE=1) corrupts one gate input in memory so the refusal path can be
tested. This driver never prints FORM lines.
"""
import argparse, contextlib, hashlib, importlib.util, io, json, os, pathlib, pickle, shutil, sys, tempfile, time
import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[3]
for p in (ROOT, ROOT / 'benchmarks' / 'gravity', ROOT / 'tools'):
    sys.path.insert(0, str(p))
import grv_blind_1 as gb1                      # noqa: E402  (the predictor and the bars rule, unchanged)
import holdout_galaxies as hg                  # noqa: E402  (the draw / seal / verdict instrument, unchanged)

_spec = importlib.util.spec_from_file_location('grv_blind_2_verdict', pathlib.Path(__file__).with_name('verdict.py'))
V = importlib.util.module_from_spec(_spec)      # the verdict module: one copy of every locked tolerance and of the gate
_spec.loader.exec_module(V)

NAME, B1 = 'GRV_BLIND_2', 'GRV_BLIND_1'
SMOKE = os.environ.get('LAB_SMOKE') == '1'
FAULT = os.environ.get('LAB_SMOKE_FAULT', '') if SMOKE else ''
CKPT = ROOT / 'analysis' / ('grv_blind_2_smoke.pkl' if SMOKE else 'grv_blind_2_ckpt.pkl')
UNITS = ['calib', 'manifest', 'predict', 'seal', 'truth']
KPC, KMS = gb1.KPC, gb1.KMS
GD = gb1.G_DAGGER
FACTORS = [2.0 ** (k / 4.0) for k in range(-16, 17)]        # descriptive g_dagger window grid, 1/16 to 16
TAG = '[grv-blind-2]'


def say(*a):
    print(TAG, *a, flush=True)


def atomic(path, obj):
    path = pathlib.Path(path); tmp = path.with_name(path.name + '.tmp')
    tmp.write_bytes(pickle.dumps(obj)); os.replace(tmp, path)


def sha256(p):
    return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()


@contextlib.contextmanager
def bound(root):
    """point the unchanged modules at a root (temporary directories for the credential legs and the smoke draw)."""
    old = (gb1.ROOT, hg.ROOT, hg.TABLE)
    gb1.ROOT = root; hg.ROOT = root; hg.TABLE = root / 'data' / 'sparc_rotmod'
    try:
        yield
    finally:
        gb1.ROOT, hg.ROOT, hg.TABLE = old


def quiet(fn, *a, **k):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        out = fn(*a, **k)
    return out, buf.getvalue()


def scratch(with_b1=False):
    """a temporary repo-shaped root: the SPARC table copied, optionally GRV_BLIND_1's non-sealed files."""
    sc = pathlib.Path(tempfile.mkdtemp(prefix='grv_b2_'))
    shutil.copytree(ROOT / 'data' / 'sparc_rotmod', sc / 'data' / 'sparc_rotmod')
    (sc / 'analysis' / 'holdout').mkdir(parents=True)
    if with_b1:
        src = ROOT / 'analysis' / 'holdout' / B1
        dst = sc / 'analysis' / 'holdout' / B1
        dst.mkdir(parents=True)
        shutil.copy(src / 'MANIFEST.json', dst / 'MANIFEST.json'); shutil.copy(src / 'train.txt', dst / 'train.txt')
        shutil.copytree(src / 'inputs', dst / 'inputs')                      # never sealed/, never VERDICT.json
    return sc


def parse_pred(path):
    out = {}
    for l in pathlib.Path(path).read_text().splitlines():
        t = l.split()
        if len(t) < 3:
            continue
        try:
            out[(t[0], round(float(t[1]), 4))] = float(t[2])
        except ValueError:
            continue
    return out


def load(f):
    d = np.loadtxt(f)
    return d[None, :] if d.ndim == 1 else d


def train_points(names):
    """training galaxies, whole files, the registered cut: {galaxy: (gobs, gbar)} over kept points with gbar > 0."""
    out = {}
    for g in names:
        d = load(ROOT / 'data' / 'sparc_rotmod' / f'{g}_rotmod.dat')
        r, Vo, eV, Vg, Vd, Vb = (d[:, i] for i in range(6))
        m = (Vo > 0) & (eV / np.maximum(Vo, 1e-9) < 0.1) & (r > 0)
        go = (Vo[m] * KMS) ** 2 / (r[m] * KPC)
        gb = (np.sign(Vg[m]) * Vg[m] ** 2 + 0.5 * Vd[m] ** 2 + 0.7 * Vb[m] ** 2) * KMS ** 2 / (r[m] * KPC)
        ok = gb > 0
        if ok.any():
            out[g] = (go[ok], gb[ok])
    return out


def rms_at(tp, fn):
    s = n = 0
    for go, gb in tp.values():
        x = np.log10(go) - np.log10(fn(gb)); s += float(np.sum(x ** 2)); n += len(x)
    return float(np.sqrt(s / n))


def worst_gal_at(tp, fn):
    best = ('', 0.0)
    for g, (go, gb) in tp.items():
        v = float(np.sqrt(np.mean((np.log10(go) - np.log10(fn(gb))) ** 2)))
        if v > best[1]:
            best = (g, v)
    return best


# ------------------------------------------------------------------------------------------------------------- the gate
def require_gate(st, unit):
    """refuse (exit 2, no COMPLETE) unless C-1..C-5 and F-1, F-2 pass with the locked tolerances. Called before anything
    irreversible: the seal and the one read of the sealed truth."""
    if FAULT == 'calib' and 'calib' in st:
        st['calib']['c1'] = dict(st['calib']['c1'], bar_rms_new=st['calib']['c1']['bar_rms_new'] + 1e-3)
        say('SMOKE FAULT injected: C-1 bar_rms_new shifted by 1e-3 (in memory, smoke only)')
    if FAULT == 'floor' and 'predict' in st:
        st['predict']['f2'] = dict(st['predict']['f2'], sep_rms=0.10)
        say('SMOKE FAULT injected: F-2 held-out separation set to 0.10 dex (in memory, smoke only)')
    g = V.pre_truth_gate(st)
    keys = ('ok1', 'ok2', 'ok3', 'ok4', 'ok5', 'okf1', 'okf2')
    st['gate'] = dict(unit=unit, passed=bool(g['passed']), at_utc=time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime()),
                      flags={k: g[k] for k in keys})
    if g['passed']:
        say(f"gate before {unit}: C-1..C-5, F-1, F-2 all PASS (locked tolerances); proceeding")
        return
    names = dict(ok1='C-1', ok2='C-2', ok3='C-3', ok4='C-4', ok5='C-5', okf1='F-1', okf2='F-2')
    failed = [names[k] for k in keys if g[k] is not True]
    atomic(CKPT, st)
    say(f"REFUSED at {unit}: pre-truth gate failed or incomplete ({', '.join(failed)}). Nothing is sealed and the sealed truth is "
        f"NOT read; the failed gate is recorded in the checkpoint and the verdict script will render BLIND-CALIB-FAIL or "
        f"BLIND-OPEN-FLOOR from it. Not COMPLETE (exit 2).")
    raise SystemExit(2)


# ---------------------------------------------------------------------------------------------------------------- units
def unit_calib(st, W):
    sc = scratch(with_b1=True)
    try:
        # C-1 / C-2: the predictor and the bars rule reproduce GRV-BLIND-1's recorded files from its own inputs and train.txt
        with bound(sc):
            _, log = quiet(gb1.main, B1)
        bars_new = json.loads((sc / 'analysis' / f'{B1}_bars.json').read_text())
        bars_ref = json.loads((ROOT / 'analysis' / f'{B1}_bars.json').read_text())
        new = parse_pred(sc / 'analysis' / f'{B1}_pred.txt'); ref = parse_pred(ROOT / 'analysis' / f'{B1}_pred.txt')
        keys_equal = set(new) == set(ref)
        maxrel = max((abs(new[k] - ref[k]) / abs(ref[k]) for k in ref if k in new and ref[k] > 0), default=float('nan')) if keys_equal else float('nan')
        c1 = dict(bar_rms_new=bars_new['bar_rms'], bar_rms_ref=bars_ref['bar_rms'], bar_gal_new=bars_new['bar_gal'], bar_gal_ref=bars_ref['bar_gal'])
        c2 = dict(n_ref=len(ref), n_new=len(new), keys_equal=bool(keys_equal), max_rel_diff=float(maxrel),
                  pred_sha_new=sha256(sc / 'analysis' / f'{B1}_pred.txt'), pred_sha_ref=sha256(ROOT / 'analysis' / f'{B1}_pred.txt'))
        # C-3: the unchanged draw tool reproduces GRV-BLIND-1's draw from its seed
        b1man = json.loads((ROOT / 'analysis' / 'holdout' / B1 / 'MANIFEST.json').read_text())
        with bound(sc):
            quiet(hg.draw, argparse.Namespace(name='REPRO_B1', seed=b1man['seed'], n=b1man['n_test'], drawn_by='repro'))
        rm = json.loads((sc / 'analysis' / 'holdout' / 'REPRO_B1' / 'MANIFEST.json').read_text())
        c3 = dict(test_equal=rm['test_galaxies'] == b1man['test_galaxies'], eligible_new=rm['eligible'], eligible_ref=b1man['eligible'],
                  n_test=len(rm['test_galaxies']))
    finally:
        shutil.rmtree(sc, ignore_errors=True)
    # C-4: the verdict arithmetic, on GRV-BLIND-1's recorded VERDICT.json rows (a kept past verdict; no BLIND-2 file)
    vj = json.loads((ROOT / 'analysis' / 'holdout' / B1 / 'VERDICT.json').read_text())
    c4 = dict(rows=[[x['galaxy'], x['gobs'], x['gpred']] for x in vj['rows']], tool_rms=vj['rms_dex'], tool_worst=vj['max_galaxy_rms'],
              tool_verdict=vj['verdict'], n_points=vj['n_points'], bar_rms=bars_ref['bar_rms'], bar_gal=bars_ref['bar_gal'])
    st['calib'] = dict(c1=c1, c2=c2, c3=c3, c4=c4, g_dagger=GD)
    say(f"calib: bars new {bars_new['bar_rms']:.6f}/{bars_new['bar_gal']:.6f} vs ref {bars_ref['bar_rms']:.6f}/{bars_ref['bar_gal']:.6f}; "
        f"predictions keys_equal {keys_equal}, max rel diff {maxrel:.2e}, sha equal {c2['pred_sha_new'] == c2['pred_sha_ref']}; "
        f"draw reproduced {c3['test_equal']} (eligible {c3['eligible_new']}/{c3['eligible_ref']}); BLIND-1 rows {len(c4['rows'])}")


def unit_manifest(st, W):
    hd = W / 'analysis' / 'holdout' / NAME; mp = hd / 'MANIFEST.json'
    if not mp.exists():
        say(f"BLOCKED: no adjudicator draw at {mp.relative_to(W)}; the draw is a precondition of the lock (charter, 'The draw'). "
            f"Not COMPLETE; rerun after the adjudicator's draw is in the repo.")
        raise SystemExit(2)
    man = json.loads(mp.read_text())
    sc = scratch()
    try:
        with bound(sc):
            quiet(hg.draw, argparse.Namespace(name='REPRO', seed=man['seed'], n=man['n_test'], drawn_by='repro'))
        rm = json.loads((sc / 'analysis' / 'holdout' / 'REPRO' / 'MANIFEST.json').read_text())
        repro_train = (sc / 'analysis' / 'holdout' / 'REPRO' / 'train.txt').read_text().split()
    finally:
        shutil.rmtree(sc, ignore_errors=True)
    train_listed = (hd / 'train.txt').read_text().split()
    inputs_ok = all((hd / 'inputs' / f'{g}.dat').exists() for g in man['test_galaxies'])
    b1man = json.loads((ROOT / 'analysis' / 'holdout' / B1 / 'MANIFEST.json').read_text())
    overlap = sorted(set(man['test_galaxies']) & set(b1man['test_galaxies']))
    st['manifest'] = dict(
        name=man['name'], kind=man.get('kind'), seed=man['seed'], drawn_by=man['drawn_by'], drawn_at_utc=man['drawn_at_utc'],
        n_test=man['n_test'], n_train=man['n_train'], eligible=man['eligible'], test_galaxies=list(man['test_galaxies']),
        train_sha256=man['train_sha256'], test_sha256=man['test_sha256'],
        train_file_sha256=sha256(hd / 'train.txt'),
        repro_test_equal=(rm['test_galaxies'] == man['test_galaxies']), repro_eligible_equal=(rm['eligible'] == man['eligible']),
        repro_train_equal=(repro_train == train_listed), inputs_ok=bool(inputs_ok),
        already_sealed=bool(man.get('prediction_sha256')), already_verdict=man.get('verdict'),
        b1_seed=b1man['seed'], b1_test=list(b1man['test_galaxies']), overlap_with_b1=overlap)
    m = st['manifest']
    say(f"manifest: seed {m['seed']} drawn by {m['drawn_by']} at {m['drawn_at_utc']}; {m['n_test']} of {m['eligible']} eligible; "
        f"draw reproduced from seed: test {m['repro_test_equal']}, eligible {m['repro_eligible_equal']}, train {m['repro_train_equal']}; "
        f"train file sha matches manifest {m['train_file_sha256'] == m['train_sha256']}; overlap with GRV-BLIND-1's test set: {len(overlap)} {overlap}")


def unit_predict(st, W):
    hd = W / 'analysis' / 'holdout' / NAME; man = json.loads((hd / 'MANIFEST.json').read_text())
    predfile = W / 'analysis' / f'{NAME}_pred.txt'; barsfile = W / 'analysis' / f'{NAME}_bars.json'
    if man.get('prediction_sha256') and predfile.exists() and barsfile.exists():
        say('predict: manifest already sealed; reading the existing prediction and bars files, rewriting nothing')
    else:
        with bound(W):
            quiet(gb1.main, NAME)                       # the unchanged predictor + the locked bars rule (nboot 20000, q 0.95, seed = the draw's)
    bars = json.loads(barsfile.read_text())
    pred = parse_pred(predfile)
    # gbar at every input radius (the same formula as the predictor), from inputs/ only
    gbar_map, n_nan, logs, below = {}, 0, [], 0
    for g in man['test_galaxies']:
        d = load(hd / 'inputs' / f'{g}.dat'); r, Vg, Vd, Vb = d[:, 0], d[:, 1], d[:, 2], d[:, 3]
        gbv = (np.sign(Vg) * Vg ** 2 + 0.5 * Vd ** 2 + 0.7 * Vb ** 2) * KMS ** 2 / (np.maximum(r, 1e-9) * KPC)
        gbar_map[g] = [[round(float(ri), 4), float(x)] for ri, x in zip(r, gbv)]
        for ri, x in zip(r, gbv):
            if x > 0:
                p = pred.get((g, round(float(ri), 4)))
                if p is None or not p > 0:
                    n_nan += 1
                    continue
                logs.append(np.log10(p / x)); below += int(x < GD)
            else:
                n_nan += 1
    logs = np.array(logs)
    f2 = dict(n=int(len(logs)), sep_rms=float(np.sqrt(np.mean(logs ** 2))), frac_below=float(below / len(logs)), n_unpredicted_or_gbar_le_0=int(n_nan))
    # floor leg F-1 and the descriptive window, on the TRAINING galaxies only
    train = (hd / 'train.txt').read_text().split()
    tp = train_points(train)
    newton = rms_at(tp, lambda gb: gb)
    fpred = lambda gb: gb * gb1.nu_simple(gb / GD)
    at_pred = rms_at(tp, fpred)
    wg, wv = worst_gal_at(tp, fpred)
    scan = [(f, rms_at(tp, lambda gb, f=f: gb * gb1.nu_simple(gb / (GD * f)))) for f in FACTORS]
    k0 = FACTORS.index(1.0); lo = hi = k0
    while lo - 1 >= 0 and scan[lo - 1][1] <= bars['bar_rms']:
        lo -= 1
    while hi + 1 < len(scan) and scan[hi + 1][1] <= bars['bar_rms']:
        hi += 1
    window = dict(lo_factor=FACTORS[lo], hi_factor=FACTORS[hi], scan=[[float(a), float(b)] for a, b in scan])
    st['predict'] = dict(bars=bars, n_pred_points=len(pred), pred_sha256=sha256(predfile), gbar=gbar_map, f2=f2,
                         f1=dict(newton_train_rms=newton, pred_train_rms=at_pred, n_train=len(tp), train_worst_gal=wg, train_worst_gal_rms=wv),
                         window=window, g_dagger=GD)
    say(f"predict: g_dagger {GD:.4e}; {len(pred)} predicted points; pred sha256 {st['predict']['pred_sha256'][:12]}...; bars rms <= {bars['bar_rms']:.4f}, "
        f"worst galaxy <= {bars['bar_gal']:.4f} (worst training galaxy {wg} {wv:.4f}; training rms {bars['train_rms']:.4f}); floor F-1 Newtonian null training rms {newton:.4f} "
        f"(x{newton / bars['bar_rms']:.2f} the bar); F-2 held-out separation rms {f2['sep_rms']:.3f} dex, fraction g_bar < g_dagger {f2['frac_below']:.3f}; "
        f"training pass window g_dagger x{window['lo_factor']:.3f} to x{window['hi_factor']:.3f}")


def unit_seal(st, W):
    require_gate(st, 'seal')                              # GATED: nothing irreversible unless C-1..C-5, F-1, F-2 pass
    hd = W / 'analysis' / 'holdout' / NAME; mp = hd / 'MANIFEST.json'; man = json.loads(mp.read_text())
    predfile = W / 'analysis' / f'{NAME}_pred.txt'
    arg = str(predfile) if SMOKE else f'analysis/{NAME}_pred.txt'
    if man.get('prediction_sha256'):
        if man['prediction_sha256'] != sha256(predfile):
            say('REFUSED: the manifest is sealed on a different predictions file than the one on disk; one seal, no redo.')
            raise SystemExit(3)
        say(f"seal: already sealed at {man.get('prediction_sealed_at_utc')} sha256 {man['prediction_sha256'][:12]}... (matches the file)")
    else:
        with bound(W):
            quiet(hg.seal, argparse.Namespace(name=NAME, predictions=arg))
        man = json.loads(mp.read_text())
        say(f"seal: sealed predictions sha256 {man['prediction_sha256'][:12]}... at {man['prediction_sealed_at_utc']}; the truth may now be read, once")
    st['seal'] = dict(sha256=man['prediction_sha256'], at_utc=man['prediction_sealed_at_utc'], matches_predict=(man['prediction_sha256'] == st['predict']['pred_sha256']))


def unit_truth(st, W):
    require_gate(st, 'truth')                             # GATED again: the one read of the sealed truth
    if not st.get('seal', {}).get('matches_predict'):
        atomic(CKPT, st)
        say('REFUSED at truth: the seal is missing or is not on the predictions file the driver wrote (C-6). Truth not read. Not COMPLETE (exit 2).')
        raise SystemExit(2)
    hd = W / 'analysis' / 'holdout' / NAME; man = json.loads((hd / 'MANIFEST.json').read_text())
    vjp = hd / 'VERDICT.json'
    predfile = W / 'analysis' / f'{NAME}_pred.txt'
    arg = str(predfile) if SMOKE else f'analysis/{NAME}_pred.txt'
    if not vjp.exists():
        have = all((hd / 'sealed' / f'{g}_vobs.dat').exists() for g in man['test_galaxies'])
        if not have:
            say(f"BLOCKED (the gate passed): sealed/ is not on this machine and no VERDICT.json exists; run `python tools/holdout_galaxies.py verdict --name {NAME} "
                f"--predictions analysis/{NAME}_pred.txt --bar-rms {st['predict']['bars']['bar_rms']!r} --bar-gal {st['predict']['bars']['bar_gal']!r}` "
                f"once on the machine that holds sealed/, put analysis/holdout/{NAME}/VERDICT.json in the repo, and rerun. Not COMPLETE.")
            raise SystemExit(2)
        say('truth: reading the sealed truth ONCE, through the unchanged tool, with the locked bars from the checkpoint')
        try:
            with bound(W):
                _, out = quiet(hg.verdict, argparse.Namespace(name=NAME, predictions=arg, bar_rms=st['predict']['bars']['bar_rms'],
                                                              bar_gal=st['predict']['bars']['bar_gal']))
        except SystemExit as e:
            say(f'tool REFUSED: {e}'); raise SystemExit(3)
        for l in out.splitlines():
            say('tool:', l)
    else:
        say('truth: VERDICT.json already exists (the tool refuses a second read); ingesting it (the gate passed)')
    vj = json.loads(vjp.read_text())
    st['truth'] = dict(tool_verdict=vj['verdict'], tool_rms=vj['rms_dex'], tool_mean=vj['mean_dex'], tool_worst=vj['max_galaxy_rms'],
                       n_points=vj['n_points'], n_galaxies=vj['n_galaxies'], missing=vj['missing'], pergal=vj['per_galaxy_rms'],
                       tool_bar_rms=vj['bar_rms'], tool_bar_gal=vj['bar_gal'], computed_at_utc=vj['computed_at_utc'], verdict_json_sha256=sha256(vjp),
                       rows=[[x['galaxy'], x['r'], x['gobs'], x['gpred']] for x in vj['rows']])
    t = st['truth']
    say(f"truth: {t['n_points']} kept points in {t['n_galaxies']} galaxies; rms {t['tool_rms']:.4f} dex (mean {t['tool_mean']:+.4f}); worst galaxy {t['tool_worst']:.4f}; "
        f"missing {len(t['missing'])}; tool bars used {t['tool_bar_rms']!r}/{t['tool_bar_gal']!r}")


FN = dict(calib=unit_calib, manifest=unit_manifest, predict=unit_predict, seal=unit_seal, truth=unit_truth)


def main():
    os.chdir(ROOT)
    st = pickle.loads(CKPT.read_bytes()) if (CKPT.exists() and not SMOKE) else dict(done=[], schema=2)
    smoke_tmp = None
    W = ROOT
    if SMOKE:
        smoke_tmp = scratch(with_b1=False); W = smoke_tmp
        with bound(W):
            quiet(hg.draw, argparse.Namespace(name=NAME, seed=777, n=30, drawn_by='smoke-adjudicator'))
        say(f"SMOKE: throwaway draw seed 777 in a temporary directory; no evidence file is touched{' (fault: ' + FAULT + ')' if FAULT else ''}")
    try:
        todo = [u for u in UNITS if u not in st['done']]
        if not todo:
            say('GRV-BLIND-2 COMPLETE -- run the verdict'); return
        for u in (todo if SMOKE else todo[:1]):
            t0 = time.time()
            FN[u](st, W)
            st['done'].append(u); st[f'{u}_seconds'] = time.time() - t0
            atomic(CKPT, st)
            say(f'unit {u} done in {time.time() - t0:.1f} s; checkpoint written ({CKPT.relative_to(ROOT)})')
        if all(u in st['done'] for u in UNITS):
            say('GRV-BLIND-2 COMPLETE -- run the verdict')
        else:
            say(f"units remaining: {[u for u in UNITS if u not in st['done']]}; rerun")
    finally:
        if smoke_tmp is not None:
            shutil.rmtree(smoke_tmp, ignore_errors=True)


if __name__ == '__main__':
    main()
