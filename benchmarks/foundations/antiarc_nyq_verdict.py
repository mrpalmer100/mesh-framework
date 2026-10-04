"""COMMISSION ANTI-ARC-NYQ -- verdict, computed ONCE from the sealed checkpoint by the forms locked
in analysis/ANTIARC_NYQ_charter_LOCKED.md. Opens the sealed per-point measurements (this is the
one read), prints the per-arm table, applies the forms.

  ANTI-NYQ-CONTROL-FAIL  c2 fails under either arm (not gated clean), or c1 fails RMS/closure.
  ANTI-FLAT-CLEAN        some arm: >= 8 points gated clean, C1 f_dir rise < +0.15 over its clean
                         span, licence span A2_max >= 0.0052 covered.
  ANTI-COLLAPSE-CLEAN    some arm: >= 8 points gated clean, C1 rise >= +0.15.
  ANTI-FLAT-NYQ          no arm has 8 clean points; A1 has >= 8 points gated on RMS and closure.
  ANTI-NYQ-REFUSED       no arm has 8 points gated even on RMS and closure.
Sub-readings (recorded, change nothing): c1's wsNyq; per point, whether A2's state is A1's.
"""
import pickle, pathlib, sys, numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[2]
CKPT = ROOT / 'analysis' / 'antiarc_nyq_ckpt.pkl'
MIN_PTS, RISE, A2MAX, NYQ_BAR = 8, 0.15, 0.0052, 1e-4


def arm_table(name, P):
    meas = [m for m in P['meas'] if not m.get('halt')]
    clean = [m for m in meas if m['gated_clean']]
    print(f"[aan verdict] arm {name}: {len(meas)} points gated on RMS/closure, {len(clean)} gated clean; halt {P.get('halt')}")
    for i, m in enumerate(meas):
        print(f"[aan verdict]   {name} p{i:02d} A2 {m['A2']:.7f} rate {m['rate']:+.4e} V_pt {m['vpt']:.4e} f_dir {m['fdir']:.4f} om2 {m['om2']:+.6f} RMS {m['rms']:.1e} clos {m['clos']:.1e} wsNyq {m['nyq']:.1e} {'CLEAN' if m['gated_clean'] else 'over bar'} rounds {m.get('rounds', '-')}")
    return meas, clean


def c1_rise(pts):
    if len(pts) < 2: return float('nan')
    return pts[-1]['fdir'] - pts[0]['fdir']


def main(path=CKPT):
    st = pickle.loads(pathlib.Path(path).read_bytes())
    c1 = st.get('c1')
    if c1 is None: print("[aan verdict] c1 missing; checkpoint not terminal"); return 'INCOMPLETE'
    print(f"[aan verdict] c1 FND-173 member: stored wsNyq {c1['m0']['nyq']:.1e}; re-gated RMS {c1['m']['rms']:.1e} clos {c1['m']['clos']:.1e} wsNyq {c1['m']['nyq']:.1e} gated_rc {c1['m']['gated_rc']} (sub-reading: member {'carries' if c1['m']['nyq'] > NYQ_BAR else 'does not carry'} Nyquist content above the bar)")
    c2ok = True
    for arm in ('A1', 'A2'):
        R = st.get(f'c2{arm}')
        if R is None or not R.get('done'): print(f"[aan verdict] c2{arm} not finished; checkpoint not terminal"); return 'INCOMPLETE'
        m = R['m']; ok = bool(m.get('gated_clean', False))
        print(f"[aan verdict] c2 aligned arc point under {arm}: RMS {m['rms']:.1e} clos {m['clos']:.1e} wsNyq {m['nyq']:.1e} gated_clean {ok}")
        c2ok &= ok
    if not (c2ok and c1['m']['gated_rc']):
        print("[aan verdict] VERDICT: ANTI-NYQ-CONTROL-FAIL"); return 'ANTI-NYQ-CONTROL-FAIL'
    if 'seeds' not in st or st['seeds'].get('halt'):
        print("[aan verdict] s1 refused; VERDICT: ANTI-NYQ-REFUSED"); return 'ANTI-NYQ-REFUSED'
    print(f"[aan verdict] seeds: s1 RMS {st['seeds']['s1m']['rms']:.1e} wsNyq {st['seeds']['s1m']['nyq']:.1e}")
    arms = {}
    for arm in ('A1', 'A2'):
        P = st.get(arm)
        if P is None: print(f"[aan verdict] arm {arm} missing; checkpoint not terminal"); return 'INCOMPLETE'
        if not P.get('halt') and len(P['meas']) < 20: print(f"[aan verdict] arm {arm} unfinished ({len(P['meas'])} points); checkpoint not terminal"); return 'INCOMPLETE'
        arms[arm] = arm_table(arm, P)
    # sub-reading: are A2's states A1's?
    A1s, A2s = st['A1']['states'], st['A2']['states']
    for i in range(2, min(len(A1s), len(A2s))):
        a, b = np.asarray(A1s[i], float), np.asarray(A2s[i], float)
        print(f"[aan verdict]   sub-reading p{i - 2:02d}: |x_A2 - x_A1| / |x| = {np.linalg.norm(a - b) / np.linalg.norm(a):.2e}")
    verdict = None
    for arm in ('A2', 'A1'):
        meas, clean = arms[arm]
        if len(clean) >= MIN_PTS:
            rise = c1_rise(clean); span = max(m['A2'] for m in clean)
            print(f"[aan verdict] arm {arm}: clean points {len(clean)}, C1 f_dir rise {rise:+.4f} (rule {RISE}), A2_max {span:.4f} (licence {A2MAX})")
            if rise >= RISE: verdict = ('ANTI-COLLAPSE-CLEAN', arm)
            elif span >= A2MAX: verdict = ('ANTI-FLAT-CLEAN', arm)
            else: verdict = ('ANTI-FLAT-CLEAN (provisional by scope: licence span not covered)', arm)
            break
    if verdict is None:
        meas1, _ = arms['A1']
        if len(meas1) >= MIN_PTS:
            rise = c1_rise(meas1); print(f"[aan verdict] A1 on RMS/closure alone: {len(meas1)} points, C1 rise {rise:+.4f}, wsNyq range {min(m['nyq'] for m in meas1):.1e} to {max(m['nyq'] for m in meas1):.1e}")
            verdict = ('ANTI-FLAT-NYQ' if rise < RISE else 'ANTI-COLLAPSE-NYQ (collapse with Nyquist content; reads as ANTI-FLAT-NYQ for FND-174, the flatness is not reproduced clean)', 'A1')
        else:
            verdict = ('ANTI-NYQ-REFUSED', None)
    print(f"[aan verdict] VERDICT: {verdict[0]}" + (f" (arm {verdict[1]})" if verdict[1] else ""))
    return verdict[0]


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else CKPT)
