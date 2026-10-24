"""Write the two retained 13/9 cell members of COMPOSITE-SELECT Leg B (432 x 36 solver states and scalars) from the
sealed checkpoint on the machine of record to analysis/qp_hull_13_9_members.npz, so that a lab driver can bind them
in its manifest (QP-HULL-2's abandonment, defect 3: the repository extract composite_legB_ckpt_verdict_extract.pkl
drops every member state, x = None). The states are float64 vectors of length 3 N + 2 with N = 432 x 36 x 3 fields;
two of them are about 1 MB. The checkpoint's sha256 is recorded in the file.
Usage: python tools/qp_hull_members_extract.py ~/mesh-compute/.../composite_legB_ckpt.pkl"""
import hashlib, pathlib, pickle, sys
import numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[1]

def main(full):
    raw = pathlib.Path(full).read_bytes()
    d = pickle.loads(raw)
    members = d['cell|13/9']['members']
    out = dict(n=np.int64(len(members)), sha256_of_checkpoint=np.array(hashlib.sha256(raw).hexdigest()),
               source=np.array('COMPOSITE-SELECT Leg B sealed checkpoint, cell|13/9 retained members'))
    for i, m in enumerate(members):
        x = np.asarray(m['x'], float)
        if x.ndim != 1:
            raise SystemExit(f'member {i}: state is not a vector ({x.shape})')
        for k in ('A2', 'rms', 'om2', 'gam'):
            out[f'{k}_{i}'] = np.float64(m[k])
        out[f'x_{i}'] = x
        print(f'member {i}: A2 {m["A2"]:.7f} om2 {m["om2"]:.7f} rms {m["rms"]:.1e} state {x.shape}')
    p = ROOT / 'analysis' / 'qp_hull_13_9_members.npz'
    np.savez(p, **out)
    print(f'written {p} ({p.stat().st_size / 1e6:.2f} MB)')

if __name__ == '__main__':
    main(sys.argv[1])
