"""COMMISSION NYQ-CONTROL -- verdict, computed ONCE from the sealed checkpoint
(analysis/nyq_control_v3_ckpt.pkl) by the forms locked in analysis/NYQ_CONTROL_charter_LOCKED.md.
Reads only the per-cell summary fields the driver wrote at each cell's stop (done, gated,
gated_nobar, rms, clos, nyq, om2, round count); the state vectors are not opened.

Forms (locked 2026-09-23; unchanged by v2/v3 shakedown):
  controls   c1: b = 0 reproduces the GN floor: wsNyq stays < 1e-4 and RMS at the floor class
                 (< 1e-5; the source floored at 1.3e-7).
             c2: the aligned 4/3 member stays GATED under the de-aliased bordered solve.
             c3: b = -0.10 with dealias=False gates (RMS/closure bars) with wsNyq > 1e-3.
  NYQ-CONTROL-FAIL  any control fails.
  NYQ-MEMBER        some sweep b is GATED under the bar (RMS < 1e-8, clos < 1e-6, wsNyq <= 1e-4).
  NYQ-FLOOR         no sweep b gates under the bar.
  NYQ-REFUSED       a cell never found its near-null direction (no 'c' recorded).
"""
import pickle, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[2]
CKPT = ROOT / 'analysis' / 'nyq_control_v3_ckpt.pkl'
SWEEP = ['B|b=-0.100', 'B|b=-0.200', 'B|b=-0.050', 'B|b=+0.050', 'B|b=+0.100', 'B|b=+0.200']
C1, C2, C3 = 'c1|b=+0.000', 'c2|aligned|b=+0.000', 'c3|b=-0.100|nodealias'


def main(path=CKPT):
    st = pickle.loads(pathlib.Path(path).read_bytes())
    rows = {}
    for lab in [C1] + SWEEP + [C3, C2]:
        R = st.get(lab)
        if R is None or 'c' not in R:
            print(f"[nyq verdict] {lab}: near-null direction not recorded"); print("[nyq verdict] NYQ-REFUSED"); return 'NYQ-REFUSED'
        if not R.get('done'):
            print(f"[nyq verdict] {lab}: cell not finished ({len(R['hist'])} rounds); checkpoint is not terminal"); return 'INCOMPLETE'
        rows[lab] = R
        state = 'GATED (clean)' if R['gated'] else ('gates only WITH Nyquist' if R['gated_nobar'] else 'floor')
        print(f"[nyq verdict] {lab:26s} {state:24s} RMS {R['rms']:.1e} clos {R['clos']:.1e} wsNyq {R['nyq']:.1e} om2 {R['om2']:+.6f} rounds {len(R['hist'])}")
    c1 = rows[C1]['nyq'] < 1e-4 and rows[C1]['rms'] < 1e-5
    c2 = bool(rows[C2]['gated'])
    c3 = bool(rows[C3]['gated_nobar']) and rows[C3]['nyq'] > 1e-3
    print(f"[nyq verdict] controls: c1 GN floor reproduced {c1}; c2 aligned member stays gated {c2}; c3 fault reproduced (gates with wsNyq > 1e-3) {c3}")
    if not (c1 and c2 and c3):
        v = 'NYQ-CONTROL-FAIL'
    else:
        clean = [lab for lab in SWEEP if rows[lab]['gated']]
        withnyq = [lab for lab in SWEEP if rows[lab]['gated_nobar'] and not rows[lab]['gated']]
        print(f"[nyq verdict] sweep: clean members {clean or 'none'}; gated only with Nyquist content {withnyq or 'none'}")
        v = 'NYQ-MEMBER' if clean else 'NYQ-FLOOR'
    print(f"[nyq verdict] VERDICT: {v}")
    return v


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else CKPT)
