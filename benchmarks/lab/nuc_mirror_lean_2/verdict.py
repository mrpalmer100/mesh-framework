"""COMMISSION NUC-MIRROR-LEAN-2 verdict: reads the checkpoint only, through labkit.Verdict. Recomputes the locked
statistics (design section 4) from the sealed raw payload and the sealed predictions, requires them to agree with
the driver's record, decides Q1 by the rule in its locked order, prints one FORM line, and writes
analysis/NUC_MIRROR_LEAN_2_results.md once with the per-pair table. In smoke it withholds the form and writes no
results file. The open form INSTRUMENT-OPEN names the unit that halted, so a halt before any evidence was read is
told from one after it.
"""
import pathlib
import sys

import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from benchmarks.lab._kit import labkit as K                                                   # noqa: E402
from benchmarks.lab.nuc_mirror_lean_2.driver import SLUG, NAME, MANIFEST, CONFIG, UNITS, statistics, form_of  # noqa: E402

COMMISSION = 'NUC-MIRROR-LEAN-2'
FORMS = ['U-AGREES', 'U-MISS-HIGH', 'U-MISS-LOW', 'U-OPEN-BAND', 'U-NULL-FLOOR', 'INSTRUMENT-OPEN']
RESULTS = ROOT / 'analysis' / f'{NAME}_results.md'


def form_rule(ck, out):
    rec = ck.state['records']
    raw = ck.sealed('raw')                                         # (A, Z_p, M(Z_p, Z_p-1), M(Z_p-1, Z_p)) per pair
    pred = ck.sealed('pred_scored')
    A, zp, m_hi, m_lo = raw[:, 0], raw[:, 1], raw[:, 2], raw[:, 3]
    st = statistics(A, m_hi, m_lo, pred)                           # recomputed from the seals, not read from the record
    ev = rec['evidence']
    for k in ('n', 'mean', 'rms', 'h_boot', 'h_inst', 'h', 'diag_mean'):
        K.require(abs(float(st[k]) - float(ev[k])) < 1e-12, f'verdict recomputation of {k} disagrees with the driver record')
    K.require(np.max(np.abs(st['delta'] - ck.sealed('delta'))) < 1e-12, 'sealed deltas disagree with the recomputation')
    tok = form_of(st['mean'], st['h'])
    b1 = CONFIG['band_b1']
    out.append(f'{COMMISSION}: n = {st["n"]} T = 1/2 mirror pairs, A = {int(A.min())} to {int(A.max())}; a_c() = {rec["credential"]["a_c"]!r} MeV '
               f'(C-1 ok, C-2 worst {rec["credential"]["c2_worst"]:.1e}); table sha256 {ev["table_sha256"]}; predictions sealed '
               f'{rec["predict"]["pred_sha256"][:16]} before the table was read')
    out.append(f'mean_delta = {st["mean"]:+.5f}, rms_delta = {st["rms"]:.5f}, min {st["dmin"]:+.5f} (A = {st["a_min"]}), '
               f'max {st["dmax"]:+.5f} (A = {st["a_max"]}); diagnostic Z(Z-1) mean {st["diag_mean"]:+.5f} (no form)')
    out.append(f'floor h = max(h_boot {st["h_boot"]:.5f}, h_inst {st["h_inst"]:.5f}) = {st["h"]:.5f}; band B1 = {b1}; '
               f'|mean| + h = {abs(st["mean"]) + st["h"]:.5f}; mean - h = {st["mean"] - st["h"]:+.5f}; mean + h = {st["mean"] + st["h"]:+.5f}; '
               f'sign_resolved = {abs(st["mean"]) > st["h"]} (decides nothing)')
    why = {'U-NULL-FLOOR': f'h = {st["h"]:.5f} > B1 = {b1}: no sign read',
           'U-AGREES': f'|mean| + h = {abs(st["mean"]) + st["h"]:.5f} <= B1 = {b1}',
           'U-MISS-HIGH': f'mean - h = {st["mean"] - st["h"]:+.5f} > B1 = {b1}',
           'U-MISS-LOW': f'mean + h = {st["mean"] + st["h"]:+.5f} < -B1 = {-b1}',
           'U-OPEN-BAND': f'the floor straddles a band edge: |mean| + h = {abs(st["mean"]) + st["h"]:.5f} > B1 and the interval is not wholly outside'}[tok]
    if not ck.smoke and not RESULTS.exists():                      # written once; a second invocation is refused by the kit anyway
        write_results(ck, st, tok, why, A, zp)
    return [('Q1', tok, why)]


def write_results(ck, st, tok, why, A, zp):
    rec = ck.state['records']
    lines = [f'# {COMMISSION}: results (verdict rendered {rec["evidence"]["at"][:10]}; design analysis/NUC_MIRROR_LEAN_2_design_SEALED.md)', '',
             f'FORM (Q1): {tok} -- {why}', '',
             f'n = {st["n"]} T = 1/2 mirror pairs at odd A >= {CONFIG["min_a"]}, every pair with both rows in the pinned AME2012 table '
             f'(sha256 {rec["evidence"]["table_sha256"]}); predictions CDE_U(A) = a_c() A^(2/3) with a_c() = {rec["credential"]["a_c"]!r} MeV '
             f'sealed before the table was read (file {rec["predict"]["pred_path"]}, sha256 {rec["predict"]["pred_sha256"]}).', '',
             f'mean_delta = {st["mean"]:+.6f}; rms_delta = {st["rms"]:.6f}; min {st["dmin"]:+.6f} at A = {st["a_min"]}; max {st["dmax"]:+.6f} at A = {st["a_max"]}; '
             f'diagnostic Z(Z-1) mean {st["diag_mean"]:+.6f} (no form).', '',
             f'Floor: h_boot = {st["h_boot"]:.6f} (seed {CONFIG["floor_seed"]}, {CONFIG["floor_resamples"]} resamples, {CONFIG["floor_percentile"]}th percentile); '
             f'h_inst = {st["h_inst"]:.6f} (0.100 MeV sqrt 2 / CDE_U(13) / sqrt n); h = {st["h"]:.6f}; band B1 = {CONFIG["band_b1"]}; '
             f'sign_resolved = {abs(st["mean"]) > st["h"]} (decides nothing).', '',
             'Rule applied in the locked order: (1) h > B1 U-NULL-FLOOR; (2) |mean| + h <= B1 U-AGREES; (3) mean - h > B1 U-MISS-HIGH; '
             '(4) mean + h < -B1 U-MISS-LOW; (5) otherwise U-OPEN-BAND.', '',
             '| A | Z_p | CDE_meas (MeV) | CDE_U (MeV) | delta |', '|---|---|---|---|---|']
    pred = ck.sealed('pred_scored')
    for a, z, m, p, d in zip(A, zp, st['meas'], pred, st['delta']):
        lines.append(f'| {int(a)} | {int(z)} | {m:.6f} | {p:.6f} | {d:+.6f} |')
    lines += ['', 'Credentials: C-1, C-2, C-3 (F1 to F5 and T4), C-4, C-5, C-6 all passed (the driver halts otherwise).',
              f'Fixtures: {rec["credential"]["fixtures"]}', '',
              'What this does not establish: the cause of any miss (self-energy, exchange, diffuseness, the odd nucleon, '
              'charge-symmetry breaking); NUC-C; the mass models\' absolute accuracy; anything about A < 13, T = 1 or 3/2, or a '
              'trend in A. The rider wording is the design\'s section 7 for this form. Grade D2 unchanged; no North Star number moves.']
    K.atomic_write_bytes(RESULTS, ('\n'.join(lines) + '\n').encode())


if __name__ == '__main__':
    v = K.Verdict(ROOT, SLUG, COMMISSION, [u for u, _ in UNITS], MANIFEST, FORMS, open_form='INSTRUMENT-OPEN', config=CONFIG)
    sys.exit(v.render(form_rule))
