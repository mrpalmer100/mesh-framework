"""COMMISSION NUC-BLIND-1 -- the registered nuclear mass model scored on a pre-registered hold-out (section W).
Charter analysis/NUC_BLIND_1_charter_LOCKED.md. Step N1: predictions for the two pre-registered models at the held-out
(Z, N) labels. This script reads ONLY analysis/holdout/NUC_BLIND_1/train.txt (for the Ca-40 calibrator) and the
manifest's test_zn (labels, no masses). It never opens sealed/test.txt.

  M1  NUC-018, both corrections: B = a_V A - 1.34 a_V A^(2/3) - a_C Z^2 / A^(1/3); a_C derived at d0 = 2.026 fm
      (NUC-017; a_C = 0.6 * 1.44 / (r0/d0 * d0), the registered form in benchmarks/em/atomic_mass_predictor.py);
      a_V calibrated once on Ca-40 (the registered calibration). Asymmetry and pairing DECLARED OMITTED (NUC-005).
  M2  LAMED's registered baseline (benchmarks/nuclear/lamed_residual_classifier.py): a_S/a_V = 1.108, the same derived
      a_C, a_A = 19.85 MeV (NUC-A + NUC-B, derived), a_V calibrated once on Ca-40. Pairing omitted.
Writes analysis/NUC_BLIND_1_pred_M1.txt and analysis/NUC_BLIND_1_pred_M2.txt as 'Z N B_pred_MeV'. Nothing is fitted.
    python benchmarks/nuclear/nuc_blind_1.py
"""
import json, pathlib, sys
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[2]
NAME = sys.argv[1] if len(sys.argv) > 1 else 'NUC_BLIND_1'   # NUC-BLIND-2 (2026-10-08): the hold-out name is the one thing that changes
HD = ROOT / 'analysis' / 'holdout' / NAME
D_H, D_N = 7.28897059, 8.07131714          # the table's H-1 and n rows; B = Z D_H + N D_N - excess (house convention)
D0 = 2.026                                 # fm, NUC-017
R0_OVER_D0 = (3 / (4 * np.pi * np.sqrt(2))) ** (1 / 3)
A_C = 0.6 * 1.44 / (R0_OVER_D0 * D0)       # derived Coulomb coefficient (MeV)
MODELS = {'M1': dict(as_over_av=1.34, a_a=0.0), 'M2': dict(as_over_av=1.108, a_a=19.85)}


def ca40_binding():
    for l in (HD / 'train.txt').read_text().splitlines():
        t = l.split()
        if len(t) == 3 and t[0] == '20' and t[1] == '20':
            return 20 * D_H + 20 * D_N - float(t[2])
    raise SystemExit('Ca-40 not in the training table')


def binding(A, Z, a_v, as_over_av, a_a):
    N = A - Z
    return a_v * A - as_over_av * a_v * A ** (2 / 3) - A_C * Z ** 2 / A ** (1 / 3) - a_a * (N - Z) ** 2 / A


def main():
    man = json.loads((HD / 'MANIFEST.json').read_text())
    labels = [(int(z), int(n)) for z, n in man['test_zn']]
    b_ca = ca40_binding()
    print(f"[nb1] Ca-40 binding from train.txt: {b_ca:.3f} MeV; derived a_C = {A_C:.4f} MeV; {len(labels)} held-out labels")
    for name, m in MODELS.items():
        a_v = (b_ca + A_C * 20 ** 2 / 40 ** (1 / 3) + m['a_a'] * 0) / (40 - m['as_over_av'] * 40 ** (2 / 3))   # (N-Z) = 0 on Ca-40
        assert abs(binding(40, 20, a_v, m['as_over_av'], m['a_a']) - b_ca) < 1e-9
        out = HD.parent.parent / f'{NAME}_pred_{name}.txt'
        lines = ['Z N B_pred_MeV']
        for z, n in labels:
            lines.append(f"{z} {n} {binding(z + n, z, a_v, m['as_over_av'], m['a_a']):.6f}")
        out.write_text('\n'.join(lines) + '\n')
        print(f"[nb1 {name}] a_S/a_V {m['as_over_av']}, a_A {m['a_a']}, calibrated a_V {a_v:.4f} MeV -> {out.relative_to(ROOT)} ({len(labels)} rows)")
    print('[nb1] N1 COMPLETE -- seal both files (N2), then the verdict (N4) on the machine that holds the sealed test file')


if __name__ == '__main__':
    main()
