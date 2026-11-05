"""COMMISSION NUC-MIRROR-LEAN-3 -- the derived uniform-sphere Coulomb term scored alone on the AME2012 T = 1/2 mirror
displacement energies. Design sealed before this file was written: analysis/NUC_MIRROR_LEAN_3_design_SEALED.md
(commit 361340c). Harness: benchmarks/lab/_kit/labkit.py; verdict in verdict.py; one CONFIG shared.

Units, in the locked order, one per invocation (resumable):
  credential  C-1 the imported a_c() is the sealed code's own value; C-2 the cancellation identity on the sealed
              binding(); C-3 the filter, the statistic, the floor and the form rule on synthetic tables in a
              temporary directory (fixture T under payloads F1 to F5, and T4 which must halt at the count rule with
              zero mass conversions, counted),
              with the same functions the evidence unit calls. A failure is a Halt (INSTRUMENT-OPEN).
  predict     bar W: CDE_U(A) = a_c() A^(2/3) for every odd A from 13 to 299 written to
              analysis/NUC_MIRROR_LEAN_3_pred.txt, the array sealed and the file's sha256 recorded, BEFORE the
              table is opened. The evidence unit scores from this sealed array and never recomputes it.
  evidence    C-4 the table's sha256 equals the pin; labels by the one filter (every odd A >= 13 with both mirror
              rows present); C-5 n >= 5 before any M is read; C-6 the sealed prediction file's hash reproduces and
              every scored A is in the sealed array; the ONE read of the 2n labelled rows into one raw array,
              sealed before any statistic; delta_i, mean, rms, the diagnostic, h_boot, h_inst, h, all sealed.
The driver never prints a mass, a displacement energy, a delta, a mean or n; the verdict prints the FORM line once.

LAB_SMOKE=1: every unit in one process; the credential unit as in evidence; the predict unit writes its file under
benchmarks/lab/nuc_mirror_lean_3/scratch/; the evidence unit scores fixture T's F1 table in a temporary directory
(checkpoint analysis/nuc_mirror_lean_3_smoke.pkl). The smoke never opens data/ame2012/AME2012.txt and never
touches the evidence checkpoint.
"""
import hashlib
import os
import pathlib
import sys
import tempfile

import numpy as np

ROOT = pathlib.Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from benchmarks.lab._kit import labkit as K                       # noqa: E402
from benchmarks.lab.nuc_new_5 import driver as M5                 # noqa: E402  the sealed instrument, unchanged

SLUG = 'nuc_mirror_lean_3'
NAME = 'NUC_MIRROR_LEAN_3'
MANIFEST = ['benchmarks/lab/_kit/labkit.py', 'benchmarks/lab/nuc_mirror_lean_3/driver.py',
            'benchmarks/lab/nuc_mirror_lean_3/verdict.py', 'benchmarks/lab/nuc_new_5/driver.py',
            'data/ame2012/AME2012.txt', 'analysis/NUC_MIRROR_LEAN_3_design_SEALED.md']
CONFIG = dict(
    table='data/ame2012/AME2012.txt',
    table_sha256='88c6272c9e4117d68ac1317e2590c9e376d25f77c9bf68fd6062bbb4e238cb13',   # design section 2 (the NUC-NEW-5 pin)
    min_a=13, pred_a_max=299,                                                            # the domain (section 2); the sealed prediction span
    # the registered term, pinned at the sealed code's own value (section 5, C-1)
    a_c_code=0.7716295256894924, a_c_tol=1e-9, a_c_registered=0.7716, a_c_registered_tol=1e-4,
    d_n_minus_d_h=0.78234655, d_n_minus_d_h_tol=1e-8, d0_fm=2.026, coulomb_factor=0.864, const_tol=1e-12,
    # C-2 (section 5)
    c2_a=[13, 17, 21, 25, 33, 45, 61, 75], c2_triples=[[15.0, 1.34, 0.0], [17.77, 1.108, 19.85], [16.21, 1.34, 19.85]],
    c2_tol=1e-9,
    # the floor (section 4)
    floor_seed=20261104, floor_resamples=10000, floor_percentile=99.0, audit_tol_MeV=0.100,
    # the band and the count rule (section 4)
    band_b1=0.085, min_pairs=5,
    # C-3 (section 5): fixture T's labels and the planted payloads (f_i per pair, ascending A)
    fixture_a=[13, 17, 21, 25, 33, 45, 61, 75],
    payloads={'F1': [1 / 0.9 - 1] * 8, 'F2': [0.0] * 8, 'F3': [1 / 1.2 - 1] * 8,
              'F4': [0.05, 0.11] * 4, 'F5': [0.0, 0.5] * 4},
    expected={'F1': dict(mean=0.11111111111111116, h_boot=0.0, form='U-MISS-HIGH'),
              'F2': dict(mean=0.0, h_boot=0.0, form='U-AGREES'),
              'F3': dict(mean=-0.16666666666666663, h_boot=0.0, form='U-MISS-LOW'),
              'F4': dict(mean=0.08, h_boot=0.0225, form='U-OPEN-BAND'),
              'F5': dict(mean=0.25, h_boot=0.1875, form='U-NULL-FLOOR')},
    expected_h_inst_8=0.011720125593549844, fixture_tol=1e-9, zero_tol=1e-12,
)
SMOKE = os.environ.get('LAB_SMOKE') == '1'
TAG = '[nuc-mirror-lean-2]'


def say(*a):
    print(TAG, *a, flush=True)


# ------------------------------------------------------------------------------------------ the channel (section 3)
def cde_u(A):
    return M5.a_c() * np.asarray(A, dtype=float) ** (2 / 3)


def d_n_minus_d_h():
    return M5.CONFIG['d_n'] - M5.CONFIG['d_h']


# ------------------------------------------------------------------------------------------ the filter (section 2)
CONVERSIONS = [0]                                   # every float conversion of a mass token, counted (T4 reads it)


def mass_float(token):
    CONVERSIONS[0] += 1
    return float(token)


def parse_tokens(path):
    """Rows exactly as ca40_binding_from() parses them, but the mass token is KEPT AS TEXT: three tokens, Z and N as
    integer strings. No mass is converted here; the count rule and the prediction coverage are applied to the
    labels first, and only the selected tokens are converted (score_table). Also returns the row count."""
    rows = {}
    for l in pathlib.Path(path).read_text().splitlines():
        t = l.split()
        if len(t) == 3:
            try:
                rows[(int(t[0]), int(t[1]))] = t[2]
            except ValueError:
                continue
    return rows


def mirror_labels(rows, min_a):
    """Every odd A >= min_a with Z_p = (A + 1)/2 such that both (Z_p, Z_p - 1) and (Z_p - 1, Z_p) are present; ascending A."""
    out = []
    a_max = max((z + n for z, n in rows), default=0)
    for A in range(min_a if min_a % 2 else min_a + 1, a_max + 1, 2):
        zp = (A + 1) // 2
        if (zp, zp - 1) in rows and (zp - 1, zp) in rows:
            out.append((A, zp))
    return out


# ------------------------------------------------------------------------------------- the statistics (section 4)
def deltas(A, m_hi, m_lo, pred):
    """delta_i = CDE_U(A_i)/CDE_meas,i - 1 with CDE_meas = (d_n - d_h) + M(Z_p, Z_p - 1) - M(Z_p - 1, Z_p); pred the
    sealed CDE_U values at the pairs' A (never recomputed here)."""
    meas = d_n_minus_d_h() + np.asarray(m_hi, float) - np.asarray(m_lo, float)
    K.finite_array(meas, 'CDE_meas')
    K.require(np.all(meas != 0), 'a measured displacement energy of exactly zero')
    d = np.asarray(pred, float) / meas - 1
    K.finite_array(d, 'delta')
    diag = np.asarray(pred, float) * (1 - 1 / np.asarray(A, float)) / meas - 1
    return meas, d, diag


def h_boot(delta):
    rng = np.random.default_rng(CONFIG['floor_seed'])
    n, m = len(delta), float(np.mean(delta))
    dev = np.empty(CONFIG['floor_resamples'])
    for i in range(CONFIG['floor_resamples']):
        dev[i] = abs(float(np.mean(rng.choice(delta, size=n, replace=True))) - m)
    return float(np.percentile(dev, CONFIG['floor_percentile']))


def h_inst(n):
    return CONFIG['audit_tol_MeV'] * np.sqrt(2) / float(cde_u(CONFIG['min_a'])) / np.sqrt(n)


def statistics(A, m_hi, m_lo, pred):
    meas, d, diag = deltas(A, m_hi, m_lo, pred)
    n = len(d)
    hb, hi = h_boot(d), h_inst(n)
    return dict(n=n, mean=float(np.mean(d)), rms=float(np.sqrt(np.mean(d ** 2))), dmin=float(d.min()), dmax=float(d.max()),
                a_min=int(A[int(np.argmin(d))]), a_max=int(A[int(np.argmax(d))]), diag_mean=float(np.mean(diag)),
                h_boot=hb, h_inst=float(hi), h=float(max(hb, hi)), meas=meas, delta=d)


def form_of(mean, h, b1=None):
    """Section 4's rule, in order; the first that holds decides."""
    b1 = CONFIG['band_b1'] if b1 is None else b1
    if h > b1:
        return 'U-NULL-FLOOR'
    if abs(mean) + h <= b1:
        return 'U-AGREES'
    if mean - h > b1:
        return 'U-MISS-HIGH'
    if mean + h < -b1:
        return 'U-MISS-LOW'
    return 'U-OPEN-BAND'


# ------------------------------------------------------------------------------------------- fixtures (section 5)
def write_fixture(path, f_per_pair, a_list=None):
    """Fixture T: planted pairs with M(Z_p - 1, Z_p) = 0 and M(Z_p, Z_p - 1) = CDE_U(A)/(1 + f) - (d_n - d_h), written with
    repr(float(M)); plus the distractors (A = 11 pair, a partner-less row, a T_z = 3/2 pair, two N = Z rows)."""
    a_list = CONFIG['fixture_a'] if a_list is None else a_list
    lines = ['6 5 0.0', '5 6 0.0', '8 7 0.0', '9 6 0.0', '6 9 0.0', '20 20 0.0', '8 8 0.0']
    for A, f in zip(a_list, f_per_pair):
        zp = (A + 1) // 2
        m = float(cde_u(A)) / (1 + f) - d_n_minus_d_h()
        lines.append(f'{zp - 1} {zp} 0.0')
        lines.append(f'{zp} {zp - 1} {repr(float(m))}')
    pathlib.Path(path).write_text('\n'.join(lines) + '\n')


def score_table(path, pred_by_a, min_pairs=None):
    """The evidence routine, shared by C-3 and the evidence unit, in the locked order: labels from the tokens, the
    count rule (C-5), the prediction coverage (C-6), and only then the one read, the 2n selected tokens converted.
    Returns the labels, A, the two mass arrays, the predictions and the row count from the same pass."""
    min_pairs = CONFIG['min_pairs'] if min_pairs is None else min_pairs
    rows = parse_tokens(path)
    labels = mirror_labels(rows, CONFIG['min_a'])
    n = len(labels)
    K.require(n >= min_pairs, f'C-5: {n} mirror pairs, fewer than the {min_pairs} the count rule requires')
    A = np.array([a for a, _ in labels], float)
    for a in A:
        K.require(int(a) in pred_by_a, f'C-6: A = {int(a)} has no sealed prediction')
    pred = np.array([pred_by_a[int(a)] for a in A])
    m_hi = np.array([mass_float(rows[(zp, zp - 1)]) for _, zp in labels])
    m_lo = np.array([mass_float(rows[(zp - 1, zp)]) for _, zp in labels])
    return labels, A, m_hi, m_lo, pred, len(rows)


# ------------------------------------------------------------------------------------------------------- units
def unit_credential(ck):
    c = CONFIG
    ac = float(M5.a_c())
    K.require(abs(ac - c['a_c_code']) < c['a_c_tol'], f'C-1: a_c() = {ac!r}, not the sealed code value {c["a_c_code"]!r}')
    diag = dict(a_c_registered_ok=bool(abs(ac - c['a_c_registered']) < c['a_c_registered_tol']),
                d0_ok=bool(abs(M5.CONFIG['d0_fm'] - c['d0_fm']) < c['const_tol']),
                coulomb_factor_ok=bool(abs(M5.CONFIG['coulomb_factor'] - c['coulomb_factor']) < c['const_tol']),
                d_n_minus_d_h_ok=bool(abs(d_n_minus_d_h() - c['d_n_minus_d_h']) < c['d_n_minus_d_h_tol']))
    worst = 0.0
    for A in c['c2_a']:
        Z = (A - 1) // 2
        for av, asv, aa in c['c2_triples']:
            worst = max(worst, abs(M5.binding(A, Z, av, asv, aa) - M5.binding(A, Z + 1, av, asv, aa) - ac * A ** (2 / 3)))
    K.require(worst < c['c2_tol'], f'C-2: cancellation identity off by {worst:.2e}')
    # C-3: the fixtures, in a temporary directory, through the same functions the evidence unit calls
    pred_by_a = {int(a): float(v) for a, v in zip(c['fixture_a'], cde_u(c['fixture_a']))}
    results = {}
    with tempfile.TemporaryDirectory() as td:
        for name, f in c['payloads'].items():
            p = pathlib.Path(td) / f'{name}.txt'
            write_fixture(p, f)
            labels, A, m_hi, m_lo, pred, _ = score_table(p, pred_by_a)
            K.require([a for a, _ in labels] == list(c['fixture_a']), f'C-3 {name}: labels {labels}')
            st = statistics(A, m_hi, m_lo, pred)
            e = c['expected'][name]
            K.require(abs(st['mean'] - e['mean']) < c['fixture_tol'], f'C-3 {name}: mean {st["mean"]!r} vs {e["mean"]!r}')
            tol = c['zero_tol'] if e['h_boot'] == 0.0 else c['fixture_tol']
            K.require(abs(st['h_boot'] - e['h_boot']) < tol, f'C-3 {name}: h_boot {st["h_boot"]!r} vs {e["h_boot"]!r}')
            K.require(abs(st['h_inst'] - c['expected_h_inst_8']) < c['fixture_tol'], f'C-3 {name}: h_inst {st["h_inst"]!r}')
            form = form_of(st['mean'], st['h'])
            K.require(form == e['form'], f'C-3 {name}: form {form}, expected {e["form"]}')
            results[name] = dict(mean=st['mean'], h_boot=st['h_boot'], h=st['h'], form=form)
        p4 = pathlib.Path(td) / 'T4.txt'
        write_fixture(p4, c['payloads']['F1'][:4], c['fixture_a'][:4])
        halted = False
        CONVERSIONS[0] = 0
        try:
            score_table(p4, pred_by_a)
        except K.Halt as e:
            halted = str(e).startswith('C-5')
        K.require(halted, 'C-3 T4: four pairs did not raise the C-5 count halt')
        K.require(CONVERSIONS[0] == 0, f'C-3 T4: {CONVERSIONS[0]} mass tokens were converted before the C-5 halt')
        results['T4'] = 'C-5 halt, 0 mass conversions'
    return dict(a_c=ac, c2_worst=worst, diagnostics=diag, fixtures=results)


def pred_file(ck):
    return (K.smoke_fixture_path(ROOT, SLUG) / f'{NAME}_pred.txt') if ck.smoke else (ROOT / 'analysis' / f'{NAME}_pred.txt')


def unit_predict(ck):
    """Bar W: the frozen predictions written and sealed before the table is opened."""
    A = np.arange(CONFIG['min_a'], CONFIG['pred_a_max'] + 1, 2, dtype=float)
    pred = cde_u(A)
    K.finite_array(pred, 'predictions')
    ck.seal('pred_a', A); ck.seal('pred_cde_u', pred)
    path = pred_file(ck)
    path.parent.mkdir(parents=True, exist_ok=True)
    text = f'# {NAME}: CDE_U(A) = a_c() A^(2/3) MeV, a_c() = {float(M5.a_c())!r}, sealed before the table is read\n'
    text += ''.join(f'{int(a)} {repr(float(v))}\n' for a, v in zip(A, pred))
    K.atomic_write_bytes(path, text.encode())
    h = hashlib.sha256(path.read_bytes()).hexdigest()
    return dict(n_pred=int(len(A)), pred_path=str(path.relative_to(ROOT)), pred_sha256=h)


def unit_evidence(ck):
    rec = ck.state['records']['predict']
    path = pred_file(ck)
    K.require(hashlib.sha256(path.read_bytes()).hexdigest() == rec['pred_sha256'], 'C-6: the sealed prediction file changed')
    pred_by_a = {int(a): float(v) for a, v in zip(ck.sealed('pred_a'), ck.sealed('pred_cde_u'))}
    if ck.smoke:
        td = tempfile.mkdtemp()
        table = pathlib.Path(td) / 'smoke_F1.txt'
        write_fixture(table, CONFIG['payloads']['F1'])
        table_sha = None
    else:
        table = ROOT / CONFIG['table']
        table_sha = M5.sha256_file(table)
        K.require(table_sha == CONFIG['table_sha256'], 'C-4: the table is not the pinned AME2012 file')
    CONVERSIONS[0] = 0
    labels, A, m_hi, m_lo, pred, rows_in_table = score_table(table, pred_by_a)
    K.require(CONVERSIONS[0] == 2 * len(labels), f'{CONVERSIONS[0]} mass conversions for {len(labels)} pairs: not the one read')
    raw = np.array([(float(a), float(zp), float(hi), float(lo)) for (a, zp), hi, lo in zip(labels, m_hi, m_lo)])
    ck.seal('raw', raw)                                           # the one payload, sealed before any statistic
    st = statistics(A, m_hi, m_lo, pred)
    ck.seal('delta', st['delta']); ck.seal('meas', st['meas']); ck.seal('pred_scored', pred)
    summary = {k: v for k, v in st.items() if k not in ('meas', 'delta')}
    summary.update(table_sha256=table_sha, rows_in_table=int(rows_in_table) if not ck.smoke else None,
                   sign_resolved=bool(abs(st['mean']) > st['h']))
    return summary


UNITS = [('credential', unit_credential), ('predict', unit_predict), ('evidence', unit_evidence)]

if __name__ == '__main__':
    sys.exit(K.Driver(ROOT, SLUG, UNITS, MANIFEST, config=CONFIG).run())
