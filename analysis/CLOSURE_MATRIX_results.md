# COMMISSION CLOSURE-MATRIX -- RESULTS (sandbox, 2026-10-04, night; verdict computed once)

Charter: analysis/CLOSURE_MATRIX_charter_LOCKED.md (locked before any machine step; reads at lock recorded
there). Instrument: benchmarks/foundations/closure_matrix.py (the typed matrix as data; union-find; leverage);
log analysis/CLOSURE_MATRIX_run.log; sealed analysis/closure_matrix.npz and closure_matrix.json (the full
matrix with every cell's type and id).

## VERDICT: N-GAPS, N = 5 (nine classes in all, five load-bearing)

Twenty primitives, thirteen closure targets, every cell typed from a claim or written NONE. Union-find
over IDENTITY and EXPONENT edges only (B-2) gives nine classes; five of them have a closure target
that depends on them. North Star section 4's "one fence" is therefore not what the registered relations
say. The prior stated at lock (three gaps) was also wrong: it joined two primitives to the action
scale because they are BLOCKED behind it, and a blocked-by is not an identity.

## The five gaps, with members and the columns that depend on them

| gap | members (joined by registered identities) | columns depending on it | joined by |
|---|---|---|---|
| 1. The action scale | hbar, a (m_e), T0, Sigma, g = l_q/a, rho (alpha), N ~ 1e21, Pi = 2, k/T0 = 2 | hbar derived; a derived; G's absolute value; alpha; and, as BLOCKED consumers, m_p/m_e, quantum dynamics, magnet strength, nuclear shell/pairing and light isotopes, dispersion forces, frame dragging | R1 hbar = T0 l_q^2/(4 pi alpha c) (GRV-093); R2 G = c^3 a^2/(16 pi zeta hbar) (GRV-095/075); a, T0 from m_e and Sigma (FND-MATTER-044); hbar = N A* (FND-183); 1/alpha = 2 pi^2 rho^2 (ELEC-083, conditional); Pi and k/T0 by lock and adoption |
| 2. The on-site potential | V_0, w (kink width), f (junction fraction), the contact convention (FND-184) | the strand mass scale in eV; FND-182's number | w^2 = T0 r^2/(2 a V_0) (STRAND-MASS-SCALE); V_0 = f T0 a/2 (NODE-STANDOFF); V_0 = n_x V_sec (FND-184, CROSSING-PRICE) |
| 3. The internal dimension | d | gauge structure beyond U(1) | nothing joins it to anything (FND-185) |
| 4. The electron model | the electron model | magnet strength (with gap 1) | nothing; BLOCKED behind hbar (ELEC-062), not joined |
| 5. The proton | the nucleon mass unit | m_p/m_e and the spectrum (with gap 1) | nothing; R5's mass form has the proton's L unregistered (FND-MATTER-066), BLOCKED |

Four inputs form classes with no column depending on them and are not gaps: d_c (calibration, HBAR-005),
eps (the Ca-40 bond depth, a calibration inside a D3 result), kappa_pack (a floor), the Poisson ratio
(an import that moves gamma by a factor of a few). They are inputs to retire, not gaps to close.

## The tension inside gap 1, recorded as the charter requires

Gap 1 is joined by three registered identities whose joint numerical closure is registered as FAILING
by about seventeen orders (FND-MATTER-040: a from R2, T0 from R5 on m_e, l_q from R1 gives l_q/a = 2.9e10
against a 1 to 100 window; the fingerprint points at R2's identification of a with the Sakharov cutoff).
So gap 1 is one class by the rule and is not one consistent system: the registry holds a = 6.0e-17 m
(the M-point, FND-MATTER-044) and a_Sak = 1.26e-34 m (GRV-075) as two values of the same primitive from
two identities, with the tension registered. Supplying hbar would close hbar, a, G and alpha only if that
tension is resolved first; this is the fence's content restated as a matrix fact. The matrix does not
resolve it and does not choose between the two a's.

## Leverage (M4), recorded and not ranked (B-3)

| supply | closes by identity | touches (blocked-by, or AND with another gap) |
|---|---|---|
| gap 1 (any resolution of the action scale) | hbar, a (m_e), G, alpha | m_p/m_e (with gap 5), quantum dynamics, magnet strength (with gap 4), nuclear shell and light isotopes, dispersion forces, frame dragging (also n_sub, a candidate row) |
| gap 2 (V_0) | the strand mass scale in eV, FND-182's number | nothing further |
| gap 3 (d) | nothing by identity | gauge structure (necessary, not sufficient: gauging is a second question) |
| gap 4 (electron) | nothing by identity | magnet strength (with gap 1) |
| gap 5 (proton) | nothing by identity | m_p/m_e (with gap 1) |

The table says what each gap would unlock; it does not say which to work on. The author selects
charters; three of the five gaps (1, 3, and by JUNCTION-LOCK's reading 2) have a grant, not a
computation, as their next step, and the matrix does not change that.

## What section 4 should say instead (the amendment, for the author's adoption, not applied)

Replace the opening of section 4 and the stale evening bracket with:

> ## 4. Where every road goes: five gaps, one of them the fence
>
> CLOSURE-MATRIX (2026-10-04) typed every registered relation between the programme's twenty remaining
> primitives and its thirteen closure targets and counted the mutually independent gaps: five.
> (1) THE ACTION SCALE: hbar, a (m_e), T0, Sigma, g, alpha and the pure number N ~ 1e21 are one class,
> joined by the constants ledger's identities (R1, R2, the M-point), and that class is registered as
> numerically inconsistent by seventeen orders (FND-MATTER-040) between the matter sector's a and the
> Sakharov a. This is the fence of FND-BOUND-001 and ACTION-BRIDGE; every scorecard target is blocked
> behind it; its next step is a primitive (a large-number mechanism from Pi, or a fork-invariant length),
> not a computation. (2) THE ON-SITE POTENTIAL V_0, with the kink width and the junction fraction: the
> strand mass scale and FND-182's number depend on it and nothing else does; its vacuum source is empty
> at the registered level (JUNCTION-LOCK, f = 0) and the fourth grant lives in the matter sector. (3) THE
> INTERNAL DIMENSION d: the gauge structure beyond U(1) depends on it and nothing joins it to the rest
> (FND-185). (4) THE ELECTRON MODEL, blocked behind (1) and joined to nothing. (5) THE PROTON's topology,
> blocked behind (1) and joined to nothing. Gaps 2 to 5 are not the fence under other names: no
> registered identity connects them to it, and supplying the action scale would leave each of them where
> it is. Four more inputs (d_c, eps, kappa_pack, the Poisson ratio) are calibrations and imports with no
> target depending on them: things to retire, not gaps.
>
> The standing plan for gap 1 is unchanged (Tasks 1 and 2, the five acceptance tests, one calibration).
> [The 2026-10-04 evening bracket on V_0 is superseded: the fourth grant gave V_0 a source in form, and
> the same night's chain (STRAND-MASS-SCALE, CROSSING-PRICE, NODE-STANDOFF, JUNCTION-LOCK) found that
> source empty in the registered vacuum. The extension that would fill it is priced and not granted.]

And in section 3, a "gap" column on the input ledger: hbar, a, d_c, Sigma, T0, g, kappa_pack: gap 1 (d_c
and kappa_pack as inputs on its edge); the nucleon unit: gap 5; eps: calibration; the contact convention:
gap 2; the Poisson ratio: import.

## Candidate rows found at lock and not counted (B-1)

n_sub and m, the fine strand's underived parameters (FND-087), on which frame dragging waits through
a_f = a/n_sub (GRV-126); A_c, the contact energy (EM-RECON-017, bounded by EM-RECON-018), which would
join gap 2 by V_0 = n_x V_sec if read as a primitive rather than a bound. Both are readings for the
author, not cells filled tonight.

## Consequences (on the author's word)

NORTH_STAR section 4 amended as above and section 3 given the gap column; SM_EMERGENCE's reading
paragraph updated to say the Partial rows stop at gap 1 and rows 7 and 8 at gap 3. No claim changes
status. Registration FND-186 (the closure matrix and the count) if the author wants it on an id, in the
same spirit as FND-183's rank and FND-185's dimension: the count is what the next grant is priced
against.
