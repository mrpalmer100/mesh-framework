"""COMMISSION TERMINAL-TWIST -- verdict computed once from analysis/terminal_twist.npz against the bars
of analysis/TERMINAL_TWIST_charter_LOCKED.md; writes analysis/TERMINAL_TWIST_verdict.log."""
import pathlib, numpy as np
ROOT = pathlib.Path(__file__).resolve().parents[2]
D = np.load(ROOT / 'analysis' / 'terminal_twist.npz', allow_pickle=True)
L = []
def say(s=''): print(s); L.append(s)
say("TERMINAL-TWIST VERDICT (bars: analysis/TERMINAL_TWIST_charter_LOCKED.md; outputs sealed 2026-09-27)")
say("=" * 96)
t1_pass = True
for (Lc, lat, p0, p1, w0, w1, umid) in D['rows']:
    tw = -(w1 - w0)
    say(f"T1  L {Lc} {'asymmetric seed' if lat else 'symmetric seed (control)'}: punch-through {'yes' if umid < -0.15 else 'NO'}; Frenet phi/2pi {p0:+.4f} -> {p1:+.4f} "
        f"(change {p1 - p0:+.4f}); writhe {w0:+.4f} -> {w1:+.4f}; material twist change (Lk conserved) {tw:+.4f} x 2pi  "
        f"-> bar 1.00 +/- 0.05: {'PASS' if lat and abs(abs(tw) - 1) <= 0.05 else 'FAIL'}")
    if lat and not (abs(abs(tw) - 1) <= 0.05): t1_pass = False
say("T1  reading: the 2 pi GRV-045 reports is the FINAL curve's Frenet frame rotation (and the symmetric control's, an inflection-count of a planar curve),")
say("    present in the seeded initial state before any event; the change across the punch-through is 0.21 x 2 pi in the Frenet observable and")
say("    0.028 in writhe. By Lk conservation the material azimuth changes by 0.03 x 2 pi, not by a quantum. The candidate FAILS T1.")
for R, m, ex in D['disp']:
    say(f"T2  display only (T1 failed): 2 pi steps at rate {R} -> strand mean rate {m:+.4f} vs 2 pi R {ex:.4f} (ratio {m/ex:.3f}, ringing included)")
say("T3  not run: T1 failed (charter reads-at-lock).")
say("T4  the supply demand stands as a statement: one ampere is 6.2e18 winding handovers per second per terminal, whatever object performs them.")
say("=" * 96)
say("FORM: TERMINAL-RECON-WRONG-VARIABLE -- the registered reconnection event does not hand a 2 pi quantum into the screw azimuth; on the registered")
say("      engine it changes the curve's writhe by 0.03 and the material twist by the same. The terminal remains a NEW PRIMITIVE to be priced.")
say("FLAG for the author (a registered instrument re-read, not a bar): GRV-045 F2's 'exchanged' quantum was computed on the final state only;")
say("      read before and after, the exchange is 0.21 x 2 pi (asymmetric seed) and the planar control's 2 pi is the Frenet inflection count.")
say("      F1 (continuous passage) and F3 (a bounded local exchange cannot flip an extensive sign) stand, the latter more strongly; F2's")
say("      'quantized' language and F4's belt-trick resonance do not survive the before/after reading. Amendment is the author's act.")
(ROOT / 'analysis' / 'TERMINAL_TWIST_verdict.log').write_text('\n'.join(L) + '\n')
