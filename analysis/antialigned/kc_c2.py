"""KERNEL-CONT control c2: the bordered solve at b = 0 on an ALIGNED gated member (4/3 waypoint 1,
144x36, RMS 1.9e-9) must leave it gated with no material change. One bordered round per call."""
import numpy as np, pickle, sys, pathlib; sys.path.insert(0,'.')
from benchmarks.foundations import qsweep_stage1 as q1, sparsej_instrument as SJ
from benchmarks.foundations import kernel_continuation as KC
import scipy.sparse as sp
P=pathlib.Path('analysis/antialigned/kc_c2.pkl'); st=pickle.loads(P.read_bytes()) if P.exists() else {}
mem=pickle.load(open('analysis/qsweep_stage1_ckpt.pkl','rb'))['q4/3']['members'][0]
x0=np.asarray(mem['x'],float); T=q1.QTGrid(144,36,3,4); pin=float(mem['A2']); iom=len(x0)-1
sj,_=SJ.make_instrument(T,x0,'a2',pin,50.0,cache='analysis/sparsej_pattern_144x36.pkl'); bs=SJ.BandedTorusSolver(144,36,nglob=2)
if 'c' not in st:
    J,_=sj(x0,'a2',pin,50.0); J=sp.csr_matrix(J); c,sig=KC.near_null(T,J,x0,iom); st.update(c=c,sig=float(sig),x=x0,hist=[]); P.write_bytes(pickle.dumps(st))
    print(f"c2: aligned member RMS {T.field_rms(x0,'a2',pin):.2e} om2 {T.geom(x0)[10]:+.6f}; smallest (1,1)-subspace direction |Jc|/row = {sig:.2e} (NOT null: the aligned member is non-degenerate)")
x,hist=KC.bordered_gn(T,np.asarray(st['x'],float),pin,np.asarray(st['c'],float),0.0,x0,sj,bs,rounds=1,log=lambda s: None)
st['x']=x; st['hist']+=hist; P.write_bytes(pickle.dumps(st))
m=q1.metrics(T,x); print(f"c2 after {len(st['hist'])} bordered round(s) at b=0: RMS {m['rms']:.2e} clos {m['clos']:.1e} om2 {m['om2']:+.6f} A2 {m['A2']:.7f} |x-x0|/|x0| {np.linalg.norm(x-x0)/np.linalg.norm(x0):.1e}  -> {'GATED, unchanged' if m['rms']<q1.RMS_BAR and m['clos']<q1.CLOSURE_BAR else 'NOT gated'}")
