"""GRV-BARS-OC (EXPLORATORY, NO LOCK) -- the operating characteristic of bar W's bars rule B-1 on the SPARC table.

Exposure, disclosed first: this cell (the rule's exceedance rate on this table) was previewed before any lock could
be written (the withdrawn GRV-BLIND-OC's 60-split pilot and 12 previewed seeds; the round-1 GRV-BARS-OC-1 smoke on
six real splits whose forms were printed; both on the lab's record, 2026-10-15 to 10-17). The lab's external
reviewer ruled that no fresh schedule could make a lock on this cell a prospective adjudication, and the author
agreed. This script is therefore an exploratory instrument study: it renders NO verdict form, locks nothing, and
its result is registered (if at all) as a Modeled instrument claim with this paragraph attached. It does not
re-read, re-bar or soften GRV-BLIND-1 or GRV-BLIND-2.

What it measures. B-1 (benchmarks/gravity/grv_blind_1.py, bars) sets, for a draw of 30 of the 155 eligible
galaxies, the 0.95 quantile over 20,000 random 30-galaxy subsets of the 125 TRAINING galaxies of (a) the subset
rms of log10(g_obs) - log10(g_pred) at the predicted g_dagger and (b) the subset's worst per-galaxy rms. A draw
passed (BLIND-AGREES) if its rms <= (a); (b) rendered a recorded outlier form only. Over N disjoint, uninspected
splits (seed_i = int(sha256('GRV-BARS-OC-1 split i')[:8], 16) & 0x7fffffff, a rule fixed in the author's draft of
2026-10-16 before this script existed), the script records the exceedance rate of (a), of (b), of (a) given not
(b) and vice versa, and the same under bars computed ONCE from all 155 galaxies and held fixed (the candidate rule
of STRATEGIC_TARGETS section AL), with Wilson 95 percent intervals; a synthetic iid-Gaussian control with the
table's point counts and pooled residual sd checks the instrument at the nominal 5 percent; the credentials
reproduce GRV-BLIND-1's and GRV-BLIND-2's recorded bars and draws exactly before anything else runs.

Implementation note (disclosed): the registered bars() draws its 20,000 subsets with a Python loop over
rng.choice; the split loop here draws the same statistic vectorised (argpartition of a uniform matrix), which is
the same rule and the same quantile but not the same random stream, so split bars are not bit-identical to what
bars() would print for that seed. The credentials use the registered loop verbatim.

    python benchmarks/gravity/grv_bars_oc_exploratory.py [N=1000] -> analysis/GRV_BARS_OC_exploratory.json, _results.md
"""
import glob, hashlib, json, os, pathlib, sys, time
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'benchmarks' / 'gravity'))
from grv_blind_1 import nu_simple, G_DAGGER, KPC, KMS                     # noqa: E402

TABLE = ROOT / 'data' / 'sparc_rotmod'
NBOOT, Q, NTEST = 20000, 0.95, 30


def kept_mask(r, Vobs, eV):
    return (Vobs > 0) & (eV / np.maximum(Vobs, 1e-9) < 0.1) & (r > 0)


def per_galaxy():
    """(names, ss, n, rms, residual vectors) for every eligible galaxy at the predicted g_dagger, exactly as
    grv_blind_1.bars reads them; eligibility exactly as holdout_galaxies.draw."""
    out = {}
    for f in sorted(glob.glob(str(TABLE / '*_rotmod.dat'))):
        d = np.loadtxt(f); d = d[None, :] if d.ndim == 1 else d
        r, Vobs, eV, Vgas, Vdisk, Vbul = (d[:, i] for i in range(6))
        m = kept_mask(r, Vobs, eV)
        if m.sum() < 3:
            continue
        gobs = (Vobs[m] * KMS) ** 2 / (r[m] * KPC)
        gbar = (np.sign(Vgas[m]) * Vgas[m] ** 2 + 0.5 * Vdisk[m] ** 2 + 0.7 * Vbul[m] ** 2) * KMS ** 2 / (r[m] * KPC)
        ok = gbar > 0
        res = np.log10(gobs[ok]) - np.log10(gbar[ok] * nu_simple(gbar[ok] / G_DAGGER))
        if len(res):
            out[os.path.basename(f).replace('_rotmod.dat', '')] = res
    return out


def bars_registered(per, train, seed):
    """The registered loop, verbatim from grv_blind_1.bars (for the credentials)."""
    rng = np.random.default_rng(seed); names = list(train)
    ss = {g: float(np.sum(per[g] ** 2)) for g in names}; nn = {g: len(per[g]) for g in names}
    wr = {g: float(np.sqrt(np.mean(per[g] ** 2))) for g in names}
    sub_rms, sub_max = [], []
    for _ in range(NBOOT):
        pick = rng.choice(names, size=NTEST, replace=False)
        s = sum(ss[g] for g in pick); n = sum(nn[g] for g in pick)
        sub_rms.append(np.sqrt(s / n)); sub_max.append(max(wr[g] for g in pick))
    return float(np.quantile(sub_rms, Q)), float(np.quantile(sub_max, Q))


def bars_fast(ss, nn, wr, pool_idx, rng):
    """The same rule, vectorised: 20,000 subsets of 30 from pool_idx."""
    U = rng.random((NBOOT, len(pool_idx)))
    pick = pool_idx[np.argpartition(U, NTEST - 1, axis=1)[:, :NTEST]]
    s = ss[pick].sum(1); n = nn[pick].sum(1); mx = wr[pick].max(1)
    return float(np.quantile(np.sqrt(s / n), Q)), float(np.quantile(mx, Q)), pick


def wilson(k, n, z=1.959964):
    p = k / n; d = 1 + z * z / n; c = (p + z * z / (2 * n)) / d
    h = z * np.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return float(p), float(c - h), float(c + h)


def seed_of(i, tag='GRV-BARS-OC-1 split '):
    return int(hashlib.sha256(f'{tag}{i}'.encode()).hexdigest()[:8], 16) & 0x7fffffff


def splits(ss, nn, wr, names, N, fixed, tag, control_rng=None):
    """N splits; returns per-split rows. If control_rng is given the per-galaxy statistics are replaced by
    synthetic iid-Gaussian ones (same point counts, pooled sd) drawn fresh for every split."""
    G = len(names); rows = []
    for i in range(1, N + 1):
        sd = seed_of(i, tag)
        if control_rng is not None:
            sig = float(np.sqrt(ss.sum() / nn.sum()))
            res = [control_rng.normal(0, sig, int(k)) for k in nn]
            ss_i = np.array([np.sum(r * r) for r in res]); wr_i = np.sqrt(ss_i / nn)
        else:
            ss_i, wr_i = ss, wr
        rng = np.random.default_rng(sd)
        test = np.sort(rng.choice(G, size=NTEST, replace=False))      # the same call shape as holdout_galaxies.draw
        train = np.setdiff1d(np.arange(G), test)
        b_rms, b_gal, pick = bars_fast(ss_i, nn, wr_i, train, np.random.default_rng(sd))
        t_rms = float(np.sqrt(ss_i[test].sum() / nn[test].sum())); t_gal = float(wr_i[test].max())
        # which training galaxy set the worst-galaxy bar: the galaxy whose rms equals the quantile most nearly
        setter = int(train[np.argmin(np.abs(wr_i[train] - b_gal))])
        row = dict(i=i, seed=sd, test=[int(t) for t in test], bar_rms=b_rms, bar_gal=b_gal, rms=t_rms, gal=t_gal,
                   ex_rms=t_rms > b_rms, ex_gal=t_gal > b_gal, setter=setter)
        if fixed is not None:
            row.update(fx_rms=t_rms > fixed[0], fx_gal=t_gal > fixed[1])
        rows.append(row)
    return rows


def summarise(rows, key):
    k = sum(r[key] for r in rows); return dict(k=k, n=len(rows), rate=wilson(k, len(rows)))


def main(N=1000):
    t0 = time.time()
    per = per_galaxy(); names = sorted(per)
    ss = np.array([np.sum(per[g] ** 2) for g in names]); nn = np.array([len(per[g]) for g in names], float)
    wr = np.sqrt(ss / nn)
    out = dict(N=N, eligible=len(names), kept_points=int(nn.sum()), exposure='see the module docstring; no lock, no forms',
               rule='0.95 quantile over 20000 subsets of 30 training galaxies at the predicted g_dagger (B-1)',
               schedule="seed_i = int(sha256('GRV-BARS-OC-1 split i')[:8], 16) & 0x7fffffff, i = 1..N")
    # credentials: the registered loop on the recorded draws
    cred = {}
    for name, seed, ref in (('GRV_BLIND_1', 52525254, 'GRV_BLIND_1_bars.json'), ('GRV_BLIND_2', 1083026663, 'GRV_BLIND_2_bars.json')):
        man = json.loads((ROOT / 'analysis' / 'holdout' / name / 'MANIFEST.json').read_text())
        rng = np.random.default_rng(seed)
        test = sorted(rng.choice(names, size=NTEST, replace=False).tolist())
        draw_ok = test == man['test_galaxies']
        train = [g for g in names if g not in test]
        b = bars_registered(per, train, seed)
        rb = json.loads((ROOT / 'analysis' / ref).read_text())
        cred[name] = dict(draw_reproduced=bool(draw_ok), bars=b, recorded=(rb['bar_rms'], rb['bar_gal']),
                          bars_ok=bool(abs(b[0] - rb['bar_rms']) < 1e-6 and abs(b[1] - rb['bar_gal']) < 1e-6))
        print(f'[oc] credential {name}: draw {"ok" if draw_ok else "MISMATCH"}; bars {b[0]:.6f}/{b[1]:.6f} vs recorded '
              f'{rb["bar_rms"]:.6f}/{rb["bar_gal"]:.6f} -> {"ok" if cred[name]["bars_ok"] else "MISMATCH"}', flush=True)
    out['credentials'] = cred
    if not all(c['draw_reproduced'] and c['bars_ok'] for c in cred.values()):
        print('[oc] CREDENTIAL FAILURE; stopping'); return out
    # the fixed bars (the candidate rule): the quantile rule once over all 155, fixed seed 0
    fixed = bars_fast(ss, nn, wr, np.arange(len(names)), np.random.default_rng(0))[:2]
    out['fixed_bars'] = dict(bar_rms=fixed[0], bar_gal=fixed[1], rule='B-1 applied once to all eligible galaxies, held fixed')
    print(f'[oc] fixed bars over all {len(names)}: rms <= {fixed[0]:.4f}, worst galaxy <= {fixed[1]:.4f}', flush=True)
    # the evidence splits
    rows = splits(ss, nn, wr, names, N, fixed, 'GRV-BARS-OC-1 split ')
    S = {k: summarise(rows, k) for k in ('ex_rms', 'ex_gal', 'fx_rms', 'fx_gal')}
    both = sum(r['ex_rms'] and r['ex_gal'] for r in rows); gal_only = sum(r['ex_gal'] and not r['ex_rms'] for r in rows)
    rms_only = sum(r['ex_rms'] and not r['ex_gal'] for r in rows)
    S['either_split'] = dict(k=both + gal_only + rms_only, n=N, rate=wilson(both + gal_only + rms_only, N))
    S['gal_given_rms_pass'] = dict(k=gal_only, n=N - S['ex_rms']['k'], rate=wilson(gal_only, N - S['ex_rms']['k']))
    out['split_bars'] = dict(rms=S['ex_rms'], gal=S['ex_gal'], either=S['either_split'], gal_given_rms_pass=S['gal_given_rms_pass'])
    out['fixed'] = dict(rms=S['fx_rms'], gal=S['fx_gal'])
    # the setters of the worst-galaxy bar, and the outlier coupling
    from collections import Counter
    setters = Counter(names[r['setter']] for r in rows).most_common(5)
    out['bar_gal_setters'] = setters
    top = [names.index(g) for g, _ in setters[:2]]
    with_top = [r for r in rows if any(t in r['test'] for t in top)]; without = [r for r in rows if not any(t in r['test'] for t in top)]
    out['coupling'] = dict(top_two=[g for g, _ in setters[:2]],
                           gal_exceed_when_top_in_test=wilson(sum(r['ex_gal'] for r in with_top), max(len(with_top), 1)) + (len(with_top),),
                           gal_exceed_when_top_in_train=wilson(sum(r['ex_gal'] for r in without), max(len(without), 1)) + (len(without),),
                           rms_exceed_when_top_in_test=wilson(sum(r['ex_rms'] for r in with_top), max(len(with_top), 1)) + (len(with_top),),
                           rms_exceed_when_top_in_train=wilson(sum(r['ex_rms'] for r in without), max(len(without), 1)) + (len(without),),
                           mean_bar_gal_top_in_test=float(np.mean([r['bar_gal'] for r in with_top])),
                           mean_bar_gal_top_in_train=float(np.mean([r['bar_gal'] for r in without])))
    # the synthetic control
    crows = splits(ss, nn, wr, names, N, None, 'GRV-BARS-OC-1 control ', control_rng=np.random.default_rng(4242))
    out['control'] = dict(rms=summarise(crows, 'ex_rms'), gal=summarise(crows, 'ex_gal'))
    out['seconds'] = time.time() - t0
    out['rows'] = rows
    (ROOT / 'analysis' / 'GRV_BARS_OC_exploratory.json').write_text(json.dumps(out, indent=1, default=str) + '\n')
    for k, v in (('split rms bar', S['ex_rms']), ('split worst-galaxy bar', S['ex_gal']), ('either split bar', S['either_split']),
                 ('fixed rms bar', S['fx_rms']), ('fixed worst-galaxy bar', S['fx_gal']),
                 ('control rms bar', out['control']['rms']), ('control worst-galaxy bar', out['control']['gal'])):
        p, lo, hi = v['rate']; print(f'[oc] {k:24s} exceeded {v["k"]:4d}/{v["n"]}  = {100*p:5.2f}%  Wilson [{100*lo:5.2f}, {100*hi:5.2f}]', flush=True)
    print(f'[oc] worst-galaxy bar set by: {setters}')
    print(f'[oc] {time.time()-t0:.0f} s')
    return out


if __name__ == '__main__':
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 1000)
