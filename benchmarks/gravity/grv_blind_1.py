"""COMMISSION GRV-BLIND-1 -- the SPARC radial-acceleration confrontation under bar W: the registered zero-parameter
prediction g_obs = g_bar nu(g_bar / g_dagger), g_dagger = c H0 / 2 pi (GRV-030), at the radii of held-out galaxies
whose observed velocities are sealed. Charter analysis/GRV_BLIND_1_charter_LOCKED.md.

Reads ONLY analysis/holdout/<name>/inputs/<galaxy>.dat (r, Vgas, Vdisk, Vbul); never the sealed/ files. Nothing is
fitted: g_bar from the registered mass-to-light convention (gas, 0.5 disk, 0.7 bulge, exactly as
benchmarks/gravity/sparc_rar_confrontation.py), nu the registered simple interpolation, g_dagger from c and H0 = 70
(H0 a measured input, declared, as GRV-030 declares it). Writes analysis/<name>_pred.txt as 'galaxy r_kpc gpred_SI'.
    python benchmarks/gravity/grv_blind_1.py GRV_BLIND_1
"""
import json, pathlib, sys
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[2]
KPC, KMS = 3.086e19, 1e3
H0 = 70 * KMS / 3.086e22
G_DAGGER = 3e8 * H0 / (2 * np.pi)                      # 1.083e-10 m/s^2, GRV-030's prediction 1


def nu_simple(y):
    return 1.0 / (1.0 - np.exp(-np.sqrt(y)))


def main(name):
    hd = ROOT / 'analysis' / 'holdout' / name
    man = json.loads((hd / 'MANIFEST.json').read_text())
    lines = ['galaxy r_kpc gpred_SI']; n = 0
    for g in man['test_galaxies']:
        d = np.loadtxt(hd / 'inputs' / f'{g}.dat'); d = d[None, :] if d.ndim == 1 else d
        r, Vgas, Vdisk, Vbul = d[:, 0], d[:, 1], d[:, 2], d[:, 3]
        gbar = (np.sign(Vgas) * Vgas ** 2 + 0.5 * Vdisk ** 2 + 0.7 * Vbul ** 2) * KMS ** 2 / (np.maximum(r, 1e-9) * KPC)
        for ri, gb in zip(r, gbar):
            gp = gb * nu_simple(gb / G_DAGGER) if gb > 0 else float('nan')
            lines.append(f'{g} {ri:.4f} {gp:.6e}'); n += 1
    out = ROOT / 'analysis' / f'{name}_pred.txt'
    out.write_text('\n'.join(lines) + '\n')
    print(f'[gb1] {name}: g_dagger = {G_DAGGER:.4e} m/s^2 (c H0 / 2 pi, H0 = 70); {n} predicted points in {len(man["test_galaxies"])} galaxies -> {out.relative_to(ROOT)}; seal it, then the verdict')
    bars(name, man)


def bars(name, man, nboot=20000, q=0.95):
    """the bars by the locked rule: the q-quantile, over nboot random subsets of n_test TRAINING galaxies, of the
    subset rms and of the subset's worst per-galaxy rms, at the predicted g_dagger (training files read whole; no
    sealed file touched). Printed and written to analysis/<name>_bars.json before the seal."""
    import glob
    train = (ROOT / 'analysis' / 'holdout' / name / 'train.txt').read_text().split()
    per = {}
    for g in train:
        d = np.loadtxt(ROOT / 'data' / 'sparc_rotmod' / f'{g}_rotmod.dat'); d = d[None, :] if d.ndim == 1 else d
        r, Vobs, eV, Vgas, Vdisk, Vbul = d[:, 0], d[:, 1], d[:, 2], d[:, 3], d[:, 4], d[:, 5]
        m = (Vobs > 0) & (eV / np.maximum(Vobs, 1e-9) < 0.1) & (r > 0)
        gobs = (Vobs[m] * KMS) ** 2 / (r[m] * KPC)
        gbar = (np.sign(Vgas[m]) * Vgas[m] ** 2 + 0.5 * Vdisk[m] ** 2 + 0.7 * Vbul[m] ** 2) * KMS ** 2 / (r[m] * KPC)
        ok = gbar > 0
        res = np.log10(gobs[ok]) - np.log10(gbar[ok] * nu_simple(gbar[ok] / G_DAGGER))
        if len(res):
            per[g] = (float(np.sum(res ** 2)), len(res), float(np.sqrt(np.mean(res ** 2))))
    names = list(per); rng = np.random.default_rng(man['seed'])
    sub_rms, sub_max = [], []
    for _ in range(nboot):
        pick = rng.choice(names, size=man['n_test'], replace=False)
        ss = sum(per[g][0] for g in pick); nn = sum(per[g][1] for g in pick)
        sub_rms.append(np.sqrt(ss / nn)); sub_max.append(max(per[g][2] for g in pick))
    b = dict(rule=f'{q:.2f} quantile over {nboot} subsets of {man["n_test"]} training galaxies at the predicted g_dagger',
             n_train_used=len(names), train_rms=float(np.sqrt(sum(v[0] for v in per.values()) / sum(v[1] for v in per.values()))),
             bar_rms=float(np.quantile(sub_rms, q)), bar_gal=float(np.quantile(sub_max, q)))
    (ROOT / 'analysis' / f'{name}_bars.json').write_text(json.dumps(b, indent=1) + '\n')
    print(f"[gb1 bars] training rms {b['train_rms']:.4f} dex over {len(names)} galaxies; bars by the locked rule: rms <= {b['bar_rms']:.4f}, worst galaxy <= {b['bar_gal']:.4f} dex -> analysis/{name}_bars.json")


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'GRV_BLIND_1')
