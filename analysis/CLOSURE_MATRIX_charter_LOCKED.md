# COMMISSION CLOSURE-MATRIX -- HOW MANY INDEPENDENT GAPS DOES THE REGISTRY HAVE?
# (CHARTER, LOCKED 2026-10-04 on the author's word, before any machine step)

North Star line (section 5): names no scorecard target, input or discriminator; it is a reading
that corrects the front door. Section 4 states that every road goes to ONE fence, and its evening
bracket of 2026-10-04 says V_0 "now has a registered source"; JUNCTION-LOCK emptied that source the
same night and GAUGE-INVENTORY counted a gauge gap that is not the action gap. This commission
builds the matrix of registered relations between the programme's remaining primitives and its
closure targets, computes the number of mutually independent gaps by machine, and amends section 4
to say that number. If the number is one, section 4 is confirmed rather than asserted.

## The objects

ROWS, the primitives and open quantities (each with the claim id that makes it one; nothing admitted
without an id): hbar (GRV-014 import; FND-183); a, equivalently m_e (FND-MATTER-044/005); Sigma
(FND-030); T0 on the degeneracy line (ROPE_PARAMETERS); d_c (HBAR-005); the nucleon mass unit
(PM-005); eps, the Ca-40 bond depth (NUC-005); k/T0 = 2 (FND-129); Pi = 2 (PRED-003-LOCK); g = l_q/a
(FND-044); kappa_pack (floor, FND-030 note); the Poisson ratio import; the contact convention
(FND-184); V_0, the on-site orientation potential (STRAND-MASS-SCALE, NODE-STANDOFF, JUNCTION-LOCK);
the internal dimension d (FND-185); the electron model (ELEC-062, unbuilt); rho = 2.6348 (ELEC-083);
the kink width w (FND-STRAND-002); the junction fraction f (NODE-STANDOFF); the large number of
order 1e21 (FND-183; LARGE-NUMBER price sheet).

COLUMNS, the closure targets: hbar derived; a (m_e) derived; G's absolute value; alpha (rho);
m_p/m_e and the spectrum; the strand mass scale in eV; FND-182's number; gauge structure beyond
U(1); quantum dynamics (the guidance flow, QGATE-011); the magnet strength (electron moment);
the nuclear shell/pairing and light isotopes (FND-BOUND-001); dispersion forces (London C6);
frame-dragging magnitude (GRV-126).

CELLS, typed and cited, one of exactly:
  IDENTITY   an exact registered relation (e.g. E_c = (4 pi/5) V_0/(e a), STRAND-MASS-SCALE)
  EXPONENT   a registered scaling law with coefficient (e.g. G ~ a^2, zeta = 1.208, GRV-075)
  BOUND      a registered inequality (e.g. A_c/(T0 a) > 0.40, EM-RECON-018)
  BLOCKED    the target is registered as blocked at this primitive (e.g. M2/M3 at V_0, FND-183)
  NONE       no registered relation; written as NONE, never left blank
A cell that would need a reading of two claims together is NONE unless a claim already made that
reading (ACTION-BRIDGE, STRAND-MASS-SCALE and GAUGE-INVENTORY made several; those count).

## Steps

  M1  THE MATRIX. Fill every cell from the registry with its id and type. B-1: no cell is filled by
      inference the executor makes tonight; a relation that "obviously follows" and is not in a claim
      is NONE and is listed as a candidate reading at the end.
  M2  THE GRAPH. From the matrix, the directed dependency graph: primitive -> target with the cell
      type as edge label, and target -> target where a registered identity makes one target a function
      of another (e.g. the strand mass scale and FND-182 are one unknown, STRAND-MASS-SCALE).
  M3  THE GAP COUNT, BY MACHINE. Two primitives are DEPENDENT if a registered IDENTITY or EXPONENT
      cell relates them (directly or through a chain of such cells); otherwise independent. The gaps
      are the equivalence classes of unsourced primitives under that relation; the count is the
      verdict. Computed by union-find over the typed edges; BOUND and BLOCKED edges do not join
      classes (a bound is not a relation that would let one primitive supply another).
  M4  LEVERAGE, FOR THE RECORD ONLY. For each unsourced primitive, the set of columns that would
      close if it were supplied, propagating IDENTITY and EXPONENT edges only, with AND-dependencies
      respected (a column needing two primitives does not close on one). Reported as a table; B-3
      forbids ranking it as a queue.
  M5  THE AMENDMENT. The text of NORTH_STAR section 4 rewritten to state the gap count and name the
      gaps, with the stale evening bracket replaced by what JUNCTION-LOCK found; delivered for the
      author's adoption, not applied.

## Bars (LOCKED)
B-1  Every cell cites a claim id or is NONE. No cell is filled by tonight's reasoning.
B-2  The gap count uses IDENTITY and EXPONENT edges only. BOUND and BLOCKED do not join gaps.
B-3  The leverage table is recorded and not read as priority; the charter and the results say so in
     the same sentence. The author selects charters.
B-4  The prior is stated and not leaned on: THREE gaps (the action scale with a and G through it; the
     on-site potential V_0 with the strand mass scale and FND-182; the internal dimension d), with the
     electron model behind the first.
B-5  If the machine count disagrees with the reading of section 4, section 4 is amended, not the count.

## Verdict forms (LOCKED)
ONE-FENCE       the count is 1: every unsourced primitive is joined to every other by registered
                identities or exponent laws; section 4 is confirmed and the bracket corrected.
N-GAPS          the count is N > 1: section 4 is amended to name the N gaps and their members; the
                input ledger (section 3) gains a column "gap" so each input shows which it belongs to.
REFUSED         a cell cannot be typed from the registry as written (two claims contradict on a
                relation): the contradiction is registered as the result and the count is not computed.

## Rules
No rescue; cells before the count; NONE written as NONE; registrations, riders and the section 4
amendment the author's; the prior stated and not leaned on.

## Reads owed at lock
NORTH_STAR sections 3 and 4 verbatim; FND-183's dimension matrix and the six enumerated mechanisms;
FND-MATTER-039/040 (the constants ledger as an over-determined system: which relations it holds);
GRV-074/075 (G's exponent pair and coefficient; a_Sak); HBAR-005 (the mesoscopic patch); FND-044
(N = 2g^2); PRED-003 and PRED-003-LOCK (alpha's chain to primitives; Pi = 2); STRAND-MASS-SCALE,
NODE-STANDOFF, JUNCTION-LOCK results (the V_0 chain); FND-185 (the internal dimension); FND-BOUND-001
(the four residuals naming the zero-point layer); ELEC-062 (the electron sector); GRV-126 (frame
dragging and a_f).

## Cost
Sandbox; one session; the machine part is a union-find over at most a few dozen edges.

## Author's lock
Locked on the author's word on 2026-10-04 ("lock CLOSURE-MATRIX"). No machine step had run.

## READS AT LOCK
NORTH_STAR section 4 (verbatim): "every target on the scorecard is blocked at that fence, so the fence
  is the programme"; the evening bracket says V_0 "now has a registered source" (stale: JUNCTION-LOCK
  found the source empty in the vacuum, f = 0).
FND-MATTER-039 (the constants ledger): R1 hbar = T0 l_q^2/(4 pi alpha c) (GRV-093); R2 c^4/16 pi G =
  zeta D hbar c/a^2 (GRV-095/025/029; a adopted at eight Planck lengths); R5 m c^2 = T0 L a + lambda dE_zp
  (the two-term mass model, lambda blocked); R7 the snap-action band; R8 the hierarchy identity logged
  as an identity so it is not used as a constraint. FND-MATTER-040: the pipeline a (R2) -> T0 (R5 on
  m_e) -> l_q (R1) gives l_q/a = 2.9e10 against a 1 to 100 window: the three identities are jointly
  inconsistent by about seventeen orders, a REGISTERED TENSION whose fingerprint points at R2's
  identification. So the identities JOIN primitives (B-2 joins on IDENTITY) while their joint
  numerical closure FAILS; both facts are typed and recorded; neither is a REFUSED contradiction
  (both claims stand, the tension is itself registered).
FND-MATTER-044: a = 6.0e-17 m and T0 = 434 J/m from m_e and the registered Sigma with zero adjustable
  choices (the M-point). FND-MATTER-005: a irreducible within the framework (theorem).
GRV-074/075: G = c^3 a^2/(16 pi zeta hbar), exponents (0, 2), zeta = 1.208, a_Sak = 1.26e-34 m,
  conditional on P1 to P3. GRV-006: G not derivable from current commitments (theorem).
FND-044: N = 2 g^2 exactly; g = l_q/a the single mesoscopic unknown. ELEC-083: 1/alpha = 2 pi^2 rho^2
  under the shared-origin hypothesis (a conditional identity), rho = 2.6348 required.
PRED-003 / PRED-003-LOCK: alpha ~ 2 T^2/(kappa a) is the derived director stiffness; kappa = 2T/(eta a),
  eta = 1, so Pi = 2 is registered (sourced by lock, not a gap).
FND-183: hbar = N A*, A* = T0 a^2 g(Pi)/c, N of order 1e21 the one pure number; six mechanisms refused.
HBAR-005: two independent lengths (a, d_c), no combination with T and c gives hbar; d_c a calibration.
STRAND-MASS-SCALE: w^2 = T0 r^2/(2 a V_0), E_c = (4 pi/5) V_0/(e a) exactly. NODE-STANDOFF: V_0 = f J,
  J = T0 a/2. JUNCTION-LOCK: f = 0 at the registered level; the extension priced at f = 3.5, not granted.
FND-185: the registered continuous internal space has dimension 1; SU(2)/SU(3) need 3 to 8; no relation
  between d and any other primitive is registered.
FND-BOUND-001: four residuals (post-Newtonian tensor half, nuclear saturation, light isotopes,
  dispersion forces) name the zero-point layer, which needs hbar and the absolute scale.
ELEC-062: the electron sector contributes nothing at any tier; the electron model is unbuilt and sits
  behind the quantum layer (BLOCKED, not joined by any identity).
GRV-126 / FND-087: frame dragging waits on the fine scale a_f = a/n_sub with n_sub and m underived
  (GRANT-SUBSTRUCTURE-TIGHT). n_sub and m are NOT rows of this charter; they are listed at the end as
  candidate rows found at lock (B-1), not counted.
EM-RECON-017/018: A_c/(T0 a) > 0.40, the nuclear import that would fix it "waiting for a go" (BOUND and
  BLOCKED; no identity joins eps or the nucleon unit to V_0 or A_c).
