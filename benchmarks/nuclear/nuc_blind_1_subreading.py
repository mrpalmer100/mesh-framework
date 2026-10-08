"""COMMISSION NUC-BLIND-1 step N5 -- the pre-registered sub-reading, run AFTER the verdicts and changing nothing (B-3).
Reads analysis/holdout/NUC_BLIND_1/VERDICT_M1.json and VERDICT_M2.json (the verdict tool's kept residual rows; the only
place the held-out truth is ever read from). For M1: Pearson correlation of the mass residual with 23 (N - Z)^2 / A
(NUC-005's declared omission). For M2: with the pairing indicator (+1 even-even, 0 odd-A, -1 odd-odd). A correlation
>= 0.8 in magnitude is reported as FAILS AS DECLARED, below as FAILS FOR ANOTHER REASON (only meaningful for a model
whose verdict is BLIND-FAILS; printed for both). Fixed before the seal; not tuned after.
    python benchmarks/nuclear/nuc_blind_1_subreading.py
"""
import json, pathlib, sys
import numpy as np
NAME = sys.argv[1] if len(sys.argv) > 1 else 'NUC_BLIND_1'
HD = pathlib.Path(__file__).resolve().parents[2] / 'analysis' / 'holdout' / NAME


def main():
    for lab in ('M1', 'M2'):
        v = json.loads((HD / f'VERDICT_{lab}.json').read_text())
        Z = np.array([r['Z'] for r in v['rows']], float); N = np.array([r['N'] for r in v['rows']], float); A = Z + N
        res = np.array([r['residual'] for r in v['rows']])
        if lab == 'M1':
            x = 23.0 * (N - Z) ** 2 / A; xname = '23 (N-Z)^2/A'
        else:
            x = np.where((Z % 2 == 0) & (N % 2 == 0), 1.0, np.where((Z % 2 == 1) & (N % 2 == 1), -1.0, 0.0)); xname = 'pairing indicator'
        c = float(np.corrcoef(res, x)[0, 1]) if np.std(x) > 0 else float('nan')
        tag = 'FAILS AS DECLARED' if abs(c) >= 0.8 else 'FAILS FOR ANOTHER REASON'
        print(f"[nb1 N5 {lab}] verdict {v['verdict']} (rms {v['rms']:.4f}, max {v['max_abs']:.4f} {v['unit']}); corr(residual, {xname}) = {c:+.3f} -> {tag if v['verdict'] == 'BLIND-FAILS' else 'sub-reading recorded, verdict not FAILS'}")


if __name__ == '__main__':
    main()
