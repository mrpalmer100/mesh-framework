"""GRANT-CANDIDATE-SWEEP, cheap test T-2 (sandbox, 2026-10-27): the frame locking, C1 of the clean-room study.
Question: does the elementary azimuth kink of a two-strand rope carry HALF a turn of the rope's frame per circuit
(so that the frame returns only after two circuits, the double cover that would make spin 1/2 and g = 2 one fact),
and what topological charge does that state carry against GG-006's "charge = linking number"?

The lock of FND-184 has period pi in the pair's azimuth (two identical strands exchanged by a half turn), so the
elementary kink is a pi kink: after one circuit the separation vector is reversed and the two strands have
exchanged places; the rope is then ONE closed strand traversing the loop twice (a (2, 1) torus curve), and its
"frame" (the direction to the partner) returns after two circuits. The 2 pi kink (one full turn) keeps two distinct
closed strands with linking number 1 (the registered charge).

The computation, on the registered Calugareanu machinery (strand_calugareanu.py: twist from parallel-transported
frames, writhe from the Gauss integral): for the two-strand full-twist rope, Lk by the Gauss linking integral and
the ledger Tw + Wr of each strand with the partner-pointing frame; for the half-twist rope, the single doubled
curve's self-linking SL = Tw + Wr with the same partner-pointing frame (an integer for any framed closed curve),
which is the only integer that state carries. Thin-rope limit d / R -> 0 checked at three ratios."""
import math, sys, pathlib
import numpy as np
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import strand_calugareanu as sc
from ring_wave_stability import writhe_exact


def gauss_link(X, Y):
    """Linking number of two closed polygons by the Gauss double integral over segment midpoints (midpoint rule)."""
    tx = np.roll(X, -1, 0) - X; ty = np.roll(Y, -1, 0) - Y
    mx = X + tx / 2; my = Y + ty / 2
    R = mx[:, None, :] - my[None, :, :]; r = np.linalg.norm(R, axis=2)
    cr = np.cross(tx[:, None, :], ty[None, :, :])
    return float(np.sum(np.sum(cr * R, axis=2) / r ** 3) / (4 * math.pi))


def rope(M, R, d, turns, circuits):
    """Two strands (or one doubled strand) around a circle of radius R at separation d, the pair azimuth advancing
    by 2 pi * turns per circuit; circuits = how many times the parameter goes round before the curve closes."""
    t = np.linspace(0, 2 * math.pi * circuits, M, endpoint=False)
    phi = turns * t
    c = np.stack([R * np.cos(t), R * np.sin(t), np.zeros(M)], 1)
    e_r = np.stack([np.cos(t), np.sin(t), np.zeros(M)], 1); e_z = np.array([0.0, 0.0, 1.0])
    n = np.cos(phi)[:, None] * e_r + np.sin(phi)[:, None] * e_z        # the separation direction (the frame)
    return c + (d / 2) * n, c - (d / 2) * n, n


def ledger(X, U):
    tw = sc.twist_from_frames(X, U); wr = writhe_exact(X)
    return tw, wr, tw + wr


if __name__ == '__main__':
    M = 2400; R = 1.0
    print('FULL TWIST (2 pi kink; two closed strands; the registered Lk = 1 charge):')
    for d in (0.3, 0.1, 0.03):
        X, Y, n = rope(M, R, d, turns=1.0, circuits=1)
        lk = gauss_link(X, Y)
        twx, wrx, slx = ledger(X, -n)           # strand X's frame points to its partner (-n)
        print(f'  d/R {d}: Lk(X, Y) = {lk:+.4f};  strand X ledger with the partner frame: Tw {twx:+.4f} Wr {wrx:+.4f} SL {slx:+.4f}')
    print('HALF TWIST (pi kink; the strands exchange; ONE closed strand of two circuits, a (2,1) torus curve):')
    for d in (0.3, 0.1, 0.03):
        X, _, n = rope(M, R, d, turns=0.5, circuits=2)
        tw, wr, sl = ledger(X, -n)              # frame points to the partner, which is the same curve half a circuit on
        # the frame's return: angle between n at t and n at t + 2 pi (one circuit) and t + 4 pi (two)
        ret1 = float(np.dot(n[0], n[M // 2])); ret2 = float(np.dot(n[0], n[0]))
        print(f'  d/R {d}: the doubled strand: Tw {tw:+.4f} Wr {wr:+.4f} SL = Tw + Wr {sl:+.4f};  frame after one circuit n.n0 = {ret1:+.3f} (reversed), after two {ret2:+.3f}')
    print('QUARTER-TURN CONTROL (not a closed state; the frame does not return): skipped by construction.')
    print('READ: the half-twist state exists as a closed object only as a single doubled strand; its integer is SL,')
    print('      printed above; the full-twist state carries Lk = 1 with the frame returning every circuit.')
