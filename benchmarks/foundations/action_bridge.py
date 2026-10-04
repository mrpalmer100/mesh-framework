"""COMMISSION ACTION-BRIDGE (charter analysis/ACTION_BRIDGE_charter_LOCKED.md, locked 2026-10-04).
S1  the one-power theorem reproduced by machine on R1 (hbar = T0 l_q^2/(4 pi alpha c)), GRV-092's snap
    action A* = (3 beta/(0.23 chi)) T0 a h / c, and the count N = hbar/A*; N evaluated at the registered
    scale sets (F-LOR) and at the adopted fork (F-SAK, a = 8 l_P) BEFORE any mechanism is evaluated.
S2  the pre-committed enumeration M0..M5 (clean room: hbar, alpha, l_q, m_e forbidden as inputs).
S4  the bounded theorem: what any bridge must supply, by dimension-matrix rank on the postulates.
Outputs to analysis/action_bridge.npz (numbers) and stdout (the derivation trail).
Inputs (registered): beta_phys 35.4 (GRV-091/092), the 0.23 (GRV-040), chi in [1, 3] (GRV-092 bars),
h = d_c = 1.87e-19 m (HBAR-005; fork-invariant per GRV-094), Sigma = 3 T0/a^2 (FND-017), the three
scale sets (ROPE_PARAMETERS: T0 434/1599/2734 J/m at a 6.0e-17/1.63e-17/9.53e-18 m, kappa_pack
1/50/250), F-SAK a = 1.293e-34 m (GRV-095, FND-MATTER-040), hbar 1.0546e-34 J s (the TARGET; never an
input to a count), c 2.998e8."""
import sys, pathlib, numpy as np, sympy as sp
ROOT = pathlib.Path(__file__).resolve().parents[2]; OUT = ROOT / 'analysis' / 'action_bridge.npz'
BETA, P023, CHI = 35.4, 0.23, (1.0, 3.0); H = 1.87e-19; HBAR = 1.0546e-34; C = 2.998e8
SETS = [('kappa_pack 1', 434.0, 6.0e-17), ('kappa_pack 50', 1599.0, 1.63e-17), ('kappa_pack 250', 2734.0, 9.53e-18)]
A_SAK = 1.293e-34


def S1():
    a, T0, h, lq, al, c, beta, chi = sp.symbols('a T0 h l_q alpha c beta chi', positive=True)
    hbar_R1 = T0 * lq ** 2 / (4 * sp.pi * al * c)
    Astar = 3 * beta / (P023 * chi) * T0 * a * h / c          # = (beta/0.23) Sigma a^3 h/(chi c) with Sigma = 3 T0/a^2
    N = sp.simplify(hbar_R1 / Astar)
    pw = lambda e: sp.Poly(sp.expand_power_base(sp.powsimp(e, force=True)), a).degree() if e.has(a) else 0
    # a-exponents with the invariants (T0, h, l_q, alpha, c) held fixed
    exps = {'hbar (R1)': sp.degree(sp.simplify(hbar_R1 * a ** 0), a) if hbar_R1.has(a) else 0,
            'A*': sp.degree(sp.simplify(Astar), a), 'N = hbar/A*': sp.degree(sp.simplify(1 / N), a) * -1}
    print(f"[ab S1] R1: hbar = {hbar_R1};  A* = {Astar};  N = hbar/A* = {N}")
    print(f"[ab S1] a-exponents (invariants fixed): hbar 0, A* {exps['A*']}, N {exps['N = hbar/A*']}  -> one-power theorem reproduced: {exps['A*'] == 1 and exps['N = hbar/A*'] == -1}")
    rows = []
    for lab, T0v, av in SETS + [('F-SAK (a = 8 l_P), T0 kappa_pack 1', 434.0, A_SAK), ('F-SAK (a = 8 l_P), T0 kappa_pack 250', 2734.0, A_SAK)]:
        for chi_v in CHI:
            Av = 3 * BETA / (P023 * chi_v) * T0v * av * H / C; nq = Av / HBAR
            rows.append((lab, chi_v, Av, nq, 1 / nq))
            print(f"[ab S1] {lab:36s} chi {chi_v:.0f}: A* {Av:.3e} J s  n_q {nq:.2e}  N = 1/n_q {1 / nq:.2e}")
    return exps['A*'] == 1 and exps['N = hbar/A*'] == -1, rows


def S2(rows):
    out = {}
    # M0 the bending area: FND-005's coupling Pi = kappa a / T is dimensionless, so kappa = Pi T / a.
    M, L, T = sp.symbols('M L T'); dimT0 = M * L * T ** -2; dima = L; dimc = L / T
    dimkappa = dimT0 / dima                      # from Pi = kappa a / T dimensionless
    dim_action = M * L ** 2 / T
    cand = dimkappa / dimc
    out['M0'] = ('REFUSED (dimensions)', f"kappa = Pi T0/a has dimensions {sp.simplify(dimkappa)}; kappa/c has {sp.simplify(cand)}, not action {dim_action}; kappa/T0 = Pi/a is a length^-1, not an area")
    # M1 the snap-overlap count: GRV-040 gates the whisper luminosity by feeding; the snap RATE per shell area is set
    # by the accretion rate, so the number of snaps coherent within one emitted period is accretion-dependent, not a
    # medium constant; the only universal number in the chain is beta (barriers per bit), already inside A*.
    out['M1'] = ('REFUSED (no universal count)', "the overlap count scales with the accretion rate (GRV-040: luminosity gated by feeding); the universal number in the chain, beta = 35.4, is already a factor of A* (e_bit = beta N h), so it cannot also be the bridge")
    # M2, M3 blocked at V_0
    out['M2'] = ('BLOCKED (unregistered input)', "omega_min in physical units needs V_0; the registered contact form has dV/dphi = 0 (FND-179 B) and GRV-072 records FND-STRAND-002 fixes only kt/V_0; no registered source for V_0 (V_0 note 2026-10-04)")
    out['M3'] = ('BLOCKED (unregistered input)', "2 pi I_T omega_min needs the same V_0")
    # M4 registered pure counts against N at F-LOR and F-SAK
    Nlor = [r[4] for r in rows if r[0].startswith('kappa_pack')]; Nsak = [r[4] for r in rows if r[0].startswith('F-SAK')]
    counts = {'kappa_pack': (1, 50, 250), 'n_sub (fine over coarse spacing, scale sets)': (6.0e-17 / 1.63e-17, 6.0e-17 / 9.53e-18), 'beta': (35.4,), '1/0.23': (1 / 0.23,), 'chi': CHI}
    lines = []
    for k, vals in counts.items():
        for v in vals:
            hit_lor = any(abs(np.log10(v / n)) < 0.5 for n in Nlor); hit_sak = any(abs(np.log10(v / n)) < 0.5 for n in Nsak)
            lines.append(f"{k} = {v:.3g}: within half a decade of N at F-LOR {hit_lor}, at F-SAK {hit_sak}")
    out['M4'] = ('NO COINCIDENCE' if not any('True' in l for l in lines) else 'COINCIDENCE', '; '.join(lines))
    out['M5'] = ('EXCLUDED', "l_q^2/a^2 is the target (GRV-093's geometry question), not a mechanism")
    for k, (v, why) in out.items(): print(f"[ab S2] {k}: {v} -- {why}")
    return out


def S4():
    # Dimension matrix of the postulate set {T0, a, c} (Pi dimensionless) over (M, L, T): rank 3 -> every dimensioned
    # quantity built from the postulates is unique up to a function of Pi; the only length is a g(Pi); the only action is
    # T0 a^2 g(Pi)/c, which carries TWO powers of a. hbar carries zero (a measured constant is fork-invariant).
    D = sp.Matrix([[1, 1, -2], [0, 1, 0], [0, 1, -1]])   # rows T0, a, c; columns M, L, T
    rank = D.rank()
    # solve for exponents (p, q, r) with T0^p a^q c^r = action [M L^2 T^-1]
    p, q, r = sp.symbols('p q r'); sol = sp.solve([p - 1, p + q + r - 2, -2 * p - r + 1], [p, q, r])
    print(f"[ab S4] dimension matrix rank {rank} of 3: no dimensionless combination of (T0, a, c); lengths are a g(Pi) only")
    print(f"[ab S4] the postulate set's action: T0^{sol[p]} a^{sol[q]} c^{sol[r]} g(Pi) -> {sol[q]} powers of a; A* has one (h supplies a length anchored to the electron); hbar has zero")
    print("[ab S4] therefore: no action built from the postulates alone is fork-invariant; a bridge needs a fork-invariant length from outside the postulates (the registry holds d_c, electron-anchored through m_e, and l_q, alpha-anchored), or a pure number g(Pi) equal to N(a), which then pins a. The registry holds no pure number of the required size (S2 M4) and no mechanism producing one.")
    return int(rank), (int(sol[p]), int(sol[q]), int(sol[r]))


def main():
    ok, rows = S1(); enum = S2(rows); rank, exps = S4()
    np.savez(OUT, s1_ok=ok, rows=np.array(rows, dtype=object), enum=np.array([(k, v[0]) for k, v in enum.items()], dtype=object), rank=rank, action_exponents=np.array(exps))
    print(f"[ab] sealed -> {OUT.name}")


if __name__ == '__main__':
    main()
