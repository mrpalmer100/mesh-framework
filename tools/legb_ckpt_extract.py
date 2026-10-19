"""COMPOSITE-SELECT Leg B: the repository extract of the sealed checkpoint (2026-10-19).
The full checkpoint analysis/composite_legB_ckpt.pkl on the machine of record is 122 MB (sha256
557d071b57e897d1bd6490b39616084f384689a5c933ab01f3efb43e823169f0), above the repository's file limit. This
script writes analysis/composite_legB_ckpt_verdict_extract.pkl: the six 'cell|*' records with every per-point
measurement, member scalars, phase and halt, and of the solver states only the one composite_legB_verdict.py
prices per profile (index i + 2 of the deepest full-bar member), the rest replaced by None with a note. The
runner's continuation entries ('lb|*') are dropped. The verdict script run on the extract reproduces the log of
record byte for byte. Usage: python tools/legb_ckpt_extract.py FULL.pkl OUT.pkl"""
import hashlib, pathlib, pickle, sys
ROOT = pathlib.Path(__file__).resolve().parents[1]; sys.path.insert(0, str(ROOT))
from benchmarks.foundations import qsweep_stage1 as q1       # noqa


def full_bar(m):
    return m['rms'] < q1.RMS_BAR and m['clos'] < q1.CLOSURE_BAR


def extract(full):
    d = pickle.loads(pathlib.Path(full).read_bytes())
    sha = hashlib.sha256(pathlib.Path(full).read_bytes()).hexdigest()
    out = {}
    for k, c in d.items():
        if not k.startswith('cell|'):
            continue
        cc = dict(c)
        for key in ('prof36', 'prof54'):
            P = dict(c[key]); pts = [(m['A2'], i) for i, m in enumerate(P['meas']) if full_bar(m)]
            keep = max(pts)[1] + 2 if pts else None
            P['states'] = [s if i == keep else None for i, s in enumerate(P['states'])]
            P['states_note'] = (f'solver states dropped from the repository extract except index {keep} (the deepest '
                                f'full-bar member, priced by QC); the full checkpoint (sha256 {sha}) holds all '
                                f'{len(c[key]["states"])}')
            cc[key] = P
        cc['cont54'] = {kk: None for kk in c['cont54']}
        cc['l1'] = {'ok': c['l1'].get('ok'), 'x': None}
        cc['members'] = [{kk: (None if kk == 'x' else vv) for kk, vv in m.items()} for m in c['members']]
        out[k] = cc
    return out, sha


if __name__ == '__main__':
    out, sha = extract(sys.argv[1])
    b = pickle.dumps(out, protocol=4)
    pathlib.Path(sys.argv[2]).write_bytes(b)
    print(f'full checkpoint sha256 {sha}; extract {len(b)} bytes sha256 {hashlib.sha256(b).hexdigest()}')
