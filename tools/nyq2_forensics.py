"""NYQ-CONTROL-2 forensics (read-only; instrument, not physics). Compares the INPUTS of FND-175's
stage B (analysis/kernel_cont_ckpt.pkl, sealed 2026-09-16) with the inputs NYQ-CONTROL-2's c3 used
(analysis/nyq_control_2_ckpt.pkl): the source state, the near-null direction, and the per-round
RMS history of the b = -0.10 run in each. Prints hashes, norms and the registered run's own
convergence history (FND-175 is registered; its numbers are published). Writes nothing."""
import pickle, pathlib, hashlib, numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[2] if 'benchmarks' in str(pathlib.Path(__file__).resolve()) else pathlib.Path.cwd()
kc = pickle.loads((ROOT / 'analysis' / 'kernel_cont_ckpt.pkl').read_bytes())
n2 = pickle.loads((ROOT / 'analysis' / 'nyq_control_2_ckpt.pkl').read_bytes())
aa = pickle.loads((ROOT / 'analysis' / 'antiarc_s288_ckpt.pkl').read_bytes())
h = lambda a: hashlib.sha256(np.ascontiguousarray(np.asarray(a, float)).tobytes()).hexdigest()[:16]
B = kc['B']; C3 = n2['c3|b=-0.100|nodealias']
x_kc, x_n2, x_aa = np.asarray(B['x_floor'], float), np.asarray(C3['x0'], float), np.asarray(aa['s288|s0']['x'], float)
print(f"source state  stage B x_floor {h(x_kc)}  | nyq2 c3 x0 {h(x_n2)}  | antiarc s0 today {h(x_aa)}")
print(f"  max|x_kc - x_n2| {np.abs(x_kc - x_n2).max():.3e}   max|x_aa - x_n2| {np.abs(x_aa - x_n2).max():.3e}   |x| {np.linalg.norm(x_n2):.4e}")
print(f"  pin stage B {B['pin']:.7f}  nyq2 {C3['pin']:.7f};  rms_floor stage B {B.get('rms_floor', float('nan')):.3e}  nyq2 rms0 {C3['rms0']:.3e}")
c_kc, c_n2 = np.asarray(B['c'], float), np.asarray(C3['c'], float)
print(f"near-null c   |c_kc| {np.linalg.norm(c_kc):.4f} |c_n2| {np.linalg.norm(c_n2):.4f}  cos(c_kc, c_n2) {float(c_kc @ c_n2 / (np.linalg.norm(c_kc) * np.linalg.norm(c_n2))):+.6f}  sigma {B['sigma']:.2e} / {C3['sigma']:.2e}")
run = B['runs'].get('b=-0.100')
if run is not None:
    print(f"stage B b=-0.100: rounds {len(run['hist'])} gated {run.get('gated')} RMS {run['rms']:.2e} clos {run['clos']:.1e} om2 {run['om2']:+.6f}")
    print("  per-round RMS (registered run):", ' '.join(f"{r[1]:.1e}" for r in run['hist']))
    print("  per-round |mu|               :", ' '.join(f"{abs(r[4]):.1e}" for r in run['hist']))
    print("  b reached per round          :", ' '.join(f"{r[3]:+.3f}" for r in run['hist'][:5]), '...')
print(f"nyq2 c3 b=-0.100: rounds {len(C3['hist'])} RMS {C3['rms']:.2e} clos {C3['clos']:.1e} wsNyq {C3['nyq']:.1e} ended by {C3['manner']}")
print("  per-round RMS (this run)      :", ' '.join(f"{r[1]:.1e}" for r in C3['hist']))
r0 = B['runs'].get('b=+0.000')
if r0 is not None: print(f"stage B c1 b=0: rounds {len(r0['hist'])} RMS {r0['rms']:.2e}; per-round RMS:", ' '.join(f"{r[1]:.1e}" for r in r0['hist']))
