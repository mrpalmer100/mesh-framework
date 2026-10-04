"""COMMISSION ACTION-BRIDGE -- verdict once from analysis/action_bridge.npz by the locked forms.
BRIDGE-FOUND if any candidate is marked BRIDGE; BRIDGE-SCALE-TENSION if marked BRIDGE-OUTSIDE-R2;
BRIDGE-COINCIDENCE if any is COINCIDENCE; REFUSED if S1 failed; else BRIDGE-NO-MECHANISM."""
import numpy as np, pathlib, sys
P = pathlib.Path(__file__).resolve().parents[2] / 'analysis' / 'action_bridge.npz'
d = np.load(sys.argv[1] if len(sys.argv) > 1 else P, allow_pickle=True)
if not bool(d['s1_ok']): print("[ab verdict] S1 failed; VERDICT: REFUSED"); sys.exit()
st = {k: v for k, v in d['enum']}
for k, v in st.items(): print(f"[ab verdict] {k}: {v}")
print(f"[ab verdict] action exponents of the postulate set (T0, a, c): {tuple(int(x) for x in d['action_exponents'])}; dimension-matrix rank {int(d['rank'])}")
if any(v == 'BRIDGE' for v in st.values()): v = 'BRIDGE-FOUND'
elif any(v == 'BRIDGE-OUTSIDE-R2' for v in st.values()): v = 'BRIDGE-SCALE-TENSION'
elif any(v.startswith('COINCIDENCE') for v in st.values()): v = 'BRIDGE-COINCIDENCE'
else: v = 'BRIDGE-NO-MECHANISM'
print(f"[ab verdict] VERDICT: {v}")
