"""COMMISSION NYQ-CONTROL-2 -- verdict, computed ONCE from the sealed checkpoints by the forms
locked in analysis/NYQ_CONTROL_2_charter_LOCKED.md. Reads the per-cell summary fields only.
Arm S1: analysis/nyq_control_2_ckpt.pkl (the 09-16 solver, de-aliasing the only amendment).
Arm S2: analysis/nyq_control_v3_ckpt.pkl (the v3 sweep, sealed 2026-10-02; not re-run).

  NYQ2-CONTROL-FAIL    c1 or c2 fails (c1: wsNyq < 1e-4 and RMS < 1e-5; c2: GATED clean).
  NYQ2-IRREPRODUCIBLE  c3 does not gate (RMS < 1e-8, clos < 1e-6) with wsNyq > 1e-3.
  NYQ2-MEMBER          c3 passes and some sweep cell in S1 or S2 is GATED under the Nyquist bar.
  NYQ2-FLOOR           c3 passes and no sweep cell in S1 or S2 gates under the bar; sub-reading
                       FLOOR-LEVEL (every S1 cell reached RMS <= 1.3e-6) or FLOOR-STALL (some S1
                       cell ended on a rejected step above it). The sub-reading changes nothing.
  NYQ2-REFUSED         a cell has no near-null direction recorded.
"""
import pickle, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[2]
S1 = ROOT / 'analysis' / 'nyq_control_2_ckpt.pkl'
S2 = ROOT / 'analysis' / 'nyq_control_v3_ckpt.pkl'
SWEEP = ['B|b=-0.100', 'B|b=-0.200', 'B|b=-0.050', 'B|b=+0.050', 'B|b=+0.100', 'B|b=+0.200']
C1, C2, C3 = 'c1|b=+0.000', 'c2|aligned|b=+0.000', 'c3|b=-0.100|nodealias'
FLOOR_CLASS = 1.3e-6


def row(tag, lab, R):
    state = 'GATED (clean)' if R['gated'] else ('gates only WITH Nyquist' if R['gated_nobar'] else 'floor')
    print(f"[nyq2 verdict] {tag} {lab:26s} {state:24s} RMS {R['rms']:.1e} clos {R['clos']:.1e} wsNyq {R['nyq']:.1e} om2 {R['om2']:+.6f} rounds {len(R['hist'])} ended by {R.get('manner', '-')}")


def main(p1=S1, p2=S2):
    s1 = pickle.loads(pathlib.Path(p1).read_bytes()); s2 = pickle.loads(pathlib.Path(p2).read_bytes())
    print(f"[nyq2 verdict] frozen solver sha256 {s1.get('solver_sha256', 'MISSING')}")
    c3 = s1.get(C3)
    if c3 is None or 'c' not in c3: print("[nyq2 verdict] NYQ2-REFUSED (c3 has no near-null direction)"); return 'NYQ2-REFUSED'
    if not c3.get('done'): print("[nyq2 verdict] c3 not finished; checkpoint is not terminal"); return 'INCOMPLETE'
    row('S1', C3, c3)
    c3ok = bool(c3['gated_nobar']) and c3['nyq'] > 1e-3
    print(f"[nyq2 verdict] c3 fault reproduced on the 09-16 solver (gates with wsNyq > 1e-3): {c3ok}")
    if not c3ok:
        print("[nyq2 verdict] VERDICT: NYQ2-IRREPRODUCIBLE"); return 'NYQ2-IRREPRODUCIBLE'
    for lab in [C1, C2] + SWEEP:
        R = s1.get(lab)
        if R is None or 'c' not in R: print(f"[nyq2 verdict] {lab}: no near-null direction"); print("[nyq2 verdict] NYQ2-REFUSED"); return 'NYQ2-REFUSED'
        if not R.get('done'): print(f"[nyq2 verdict] {lab}: not finished; checkpoint is not terminal"); return 'INCOMPLETE'
        row('S1', lab, R)
    for lab in SWEEP:
        row('S2', lab, s2[lab])
    c1 = s1[C1]['nyq'] < 1e-4 and s1[C1]['rms'] < 1e-5; c2 = bool(s1[C2]['gated'])
    print(f"[nyq2 verdict] controls: c1 GN floor reproduced {c1}; c2 aligned member stays gated {c2}")
    if not (c1 and c2): print("[nyq2 verdict] VERDICT: NYQ2-CONTROL-FAIL"); return 'NYQ2-CONTROL-FAIL'
    clean = [('S1', l) for l in SWEEP if s1[l]['gated']] + [('S2', l) for l in SWEEP if s2[l]['gated']]
    withnyq = [('S1', l) for l in SWEEP if s1[l]['gated_nobar'] and not s1[l]['gated']] + [('S2', l) for l in SWEEP if s2[l]['gated_nobar'] and not s2[l]['gated']]
    print(f"[nyq2 verdict] sweep: clean members {clean or 'none'}; gated only with Nyquist content {withnyq or 'none'}")
    if clean: print("[nyq2 verdict] VERDICT: NYQ2-MEMBER"); return 'NYQ2-MEMBER'
    stall = [l for l in SWEEP if s1[l]['manner'] == 'rejected step' and s1[l]['rms'] > FLOOR_CLASS]
    sub = 'FLOOR-STALL' if stall else 'FLOOR-LEVEL'
    print(f"[nyq2 verdict] sub-reading {sub}" + (f" (S1 cells ending on a rejected step above the floor class: {stall})" if stall else ""))
    print("[nyq2 verdict] VERDICT: NYQ2-FLOOR"); return 'NYQ2-FLOOR'


if __name__ == '__main__':
    main(*(sys.argv[1:3] if len(sys.argv) > 1 else ()))
