# GRV-2PI: can the coefficient kappa in g_dagger = kappa c^2 / L be derived from the registered statics? (executor's derivation reading, 2026-10-26)

A derivation reading, done outside the lab after GRV-2PI-DERIVE-2 was withdrawn (2026-10-25, three rounds: a
response harness cannot distinguish a derived coefficient from a typed one; the reviewers were right). The
discipline is the lab's, kept by hand: the premise list and the forms were written before the attempt (sections 1
and 2), nothing outside the list enters, and the result is a reading in analysis/, not a registered claim. The
registry changes only if a later confrontation tests what follows from this.

## 1. Premises (sealed before the attempt; registered claims only)
P1  GRV-005. A mass-knot is a stressed defect in the medium; static force balance div(stress) = -f is the
    conservation law; the Poisson equation and the 1/r conditioning field are FORCED by three-dimensional
    elastostatics. The statics are LINEAR (the Poisson operator; the 1/r field is its Green function).
P2  GRV-006. The medium's rigidity is c^4 / (4 pi G) = 9.6e42 N; G is not derivable from current commitments.
P3  FND-006. mu = T / c^2: the medium's inertia per length is its tension over c^2 (the only registered place c
    enters a static quantity).
P4  GRV-028 / GRV-029. The scalar channel is screened at strand range and the metric sector is Einstein-Hilbert;
    the corpus owns NO galaxy-scale modification channel except the horizon coupling (GRV-030's structural
    sharpening).
P5  XSEC-001 / XSEC-002 / XSEC-003. The medium has a FIXED total extent L, laid down at formation, numerically
    c / H0 today (the coincidence inherited, not solved); g_dagger is universal across SPARC and does not track
    H(z); the surviving reading of GRV-030's formula is g_dagger = c^2 / (2 pi L).
P6  GRV-030 (the formula as registered, with its caveat quoted): "the form cH0 / 2 pi from the horizon coupling.
    HONEST CAVEAT: the 2 pi is motivated by horizon-sphere geometry but is not uniquely forced; the alternative
    cH0 / 6 performs comparably against SPARC." GRV-030 registers a FORMULA and a data confirmation of its scale;
    it registers no mechanism producing the formula.
P7  GRV-031 (retired). The one registered deep-regime MECHANISM: gravitational conditioning carried by strand
    alignment fighting horizon-scale randomization, giving the Langevin law mu(x) = coth(3x) - 1 / (3x), "the 3
    fixed by the deep-MOND asymptotic". Retired as a shape by SPARC. Its scale was set by the asymptote (that is,
    by g_dagger itself), not derived; usable here only as a record of what was tried.

FORBIDDEN as steps: SPARC or any rotation-curve data; the measured g_dagger; the values 2 pi and 6 as targets;
MOND's interpolation functions; Unruh, Verlinde, Milgrom or any outside argument that is not a registered claim.

## 2. Forms (stated before the attempt)
DERIVED               kappa a pure number following from P1 to P7 with the crossover criterion itself forced by
                      the premises.
DERIVED-CONDITIONAL   kappa follows once ONE named criterion is adopted that the premises do not fix; every
                      natural criterion listed with its kappa; the registry's silence on the choice named.
NOT-DERIVED           the attempt fails at an identified step; the first failing step named, and what it would
                      take (a grant, a mechanism) to pass it.
The executor's prior, disclosed: NOT-DERIVED (the Director's expectation too). Written before section 3.

## 3. The attempt
3.1 What the formula asks for. g_dagger is an ACCELERATION at which the medium's response to a stressed defect
departs from Newton. For a source of strength M the departure sets in where g_N = G M / r^2 falls to g_dagger,
that is at the transition radius
    r_t = sqrt(G M / g_dagger) = sqrt(G M L / (kappa c^2)),
which scales as sqrt(M). For the Sun r_t is about 4e14 m (2700 AU); for a galaxy of 1e11 solar masses, about
1e20 m (3 kpc). The scale the formula names is therefore NOT a length of the medium; it is an acceleration, and
the length at which it acts depends on the source.

3.2 The registered statics are linear (P1). In a linear medium of extent L, the field of a defect of strength M is
M times the Green function of the bounded domain, G_L(r; boundary condition at L). Whatever the boundary
condition (free surface, clamped surface, anything in between), the correction to the infinite-medium 1/r
field is M times a function of r / L alone:
    phi(r) = -G M [1 / r - h(r / L) / L],    g(r) = G M [1 / r^2 - h'(r / L) / L^2].
The departure from Newton, g / g_N - 1 = -(r / L)^2 h'(r / L), depends on r / L and NOT on M. A linear bounded
medium has one length, L, and the departure sets in at r of order L for every source. It cannot produce a
departure at r_t proportional to sqrt(M), which is what an acceleration scale means. This is not a matter of the
boundary condition or of the shape of the extent; it is linearity. (For instance: a centre of dilatation in a
sphere with a stress-free surface is corrected by a uniform dilatation u = B r with B proportional to M / L^3, so
h'(x) is proportional to x and g / g_N - 1 is proportional to -(r / L)^3, M-independent; a clamped surface gives
a constant shift of the potential and no force correction at all.)

3.3 Therefore no acceleration scale exists in P1 to P5. An acceleration crossover requires the response to depend
on the FIELD AMPLITUDE, that is, a nonlinearity of the medium's response in g (equivalently in the conditioning
strain), with c^2 / L as the amplitude at which it switches on. The premises contain one candidate reading of
why c^2 / L would be that amplitude: the conditioning field's potential drop across the whole extent, g L, reaches
c^2 (by P3 the medium's energy per inertia is c^2, so g L = c^2 is the acceleration whose work across the medium
equals the medium's own rest energy per unit inertia; the accumulated strain across the extent is then of order
one). That reading gives kappa = 1 if the drop is taken across the radius L, kappa = 1 / 2 pi if across the great
circle 2 pi L ("horizon-sphere geometry", P6's own phrase), kappa = 1 / 4 pi if the surface 4 pi L^2 / L enters,
kappa = 1 / 2 if across the diameter. None of these is forced: the premises say nothing about WHICH extent the
drop is taken across, because they say nothing about a response that saturates at all.

3.4 The one registered mechanism (P7) does not help. GRV-031's alignment-versus-randomization law has the right
structure (a response that saturates in the field amplitude), but its scale was set by matching the deep-MOND
asymptote, that is, by g_dagger; it produced a shape at a given scale, never the scale. And it is retired as a
shape. It cannot be a step without re-admitting a retired law, and it would not derive kappa if it were.

3.5 The step that fails, named. Step: "the medium's response to conditioning is nonlinear in the field amplitude
at the amplitude c^2 / L". Status in the registry: NOT PRESENT. P1 registers linear statics; P4 says the horizon
coupling is the only channel but registers it as a formula (P6), not a mechanism; P5 fixes L and the formula's
reading, not the response. The 2 pi cannot be derived because there is nothing registered for it to be derived
FROM: the coefficient is a property of a nonlinear response law, and the registry has no such law.

## 4. Form
NOT-DERIVED. First failing step: no registered nonlinear response of the medium at field amplitude c^2 / L
(section 3.5). The linearity argument of 3.2 is the content: a linear medium of any extent gives Newton with
M-independent corrections at r of order L, never an acceleration scale. Recorded for the conditional ladder, not
as a form: under the "potential drop across the extent reaches c^2" reading, kappa = 1, 1 / 2, 1 / 2 pi or 1 / 4 pi
by the choice of extent, the registry silent on the choice; GRV-030's 2 pi corresponds to the great circle.

## 5. What would pass the step (the author's decisions, not the executor's)
(a) A registered response law: the medium's conditioning response saturating in the field amplitude, with the
saturation amplitude fixed by the medium's own constants (T, mu, L) and not by the data. GRV-031's alignment
picture was one such candidate and failed as a shape; a successor would have to derive the scale and the shape
together, and be tested as a shape again on the same bars. This is a grant-class decision: it adds a law.
(b) Alternatively, the formula stays what it is: a Modeled relation (GRV-030, as DERIVED_GRADES.md already files
it) with its coefficient chosen, confirmed at zero parameters on SPARC and RC100, and its coefficient question
degenerate with H0 (GRV-032) until the z-drift test is sharper. That is an honest standing and loses nothing by
being left alone. The predictions paper's caveat is exactly right as written.
(c) Not a route: hunting a geometric factor that lands on 2 pi (or 6) without a response law. That is the
coefficient supplied as input, the thing the lab's external reviewer refused to let a harness call DERIVED.

## 6. Consequence for the two declined proposals
GRV-NU-DERIVE-2 (the shape nu(y) from the statics) fails at the same step: with no nonlinear response registered,
the statics fix only the Newtonian limit and the retired candidate; the crossover shape, like its scale, is not in
the premises. GRV-EFE-DERIVE-2 (the external-field response of a local medium) presupposes a local nonlinear
response law to vary; absent one, it has nothing to derive from. The declines stand on this reading, not only on
the harness ground.
