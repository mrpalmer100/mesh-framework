[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21430784.svg)](https://doi.org/10.5281/zenodo.21430784)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Verify](https://img.shields.io/badge/verify-640%2F641%20passing-brightgreen.svg)](#verify-it-yourself)
[![verify-corpus](https://github.com/mrpalmer100/mesh-framework/actions/workflows/verify.yml/badge.svg)](https://github.com/mrpalmer100/mesh-framework/actions/workflows/verify.yml)

# The Mesh Programme (mesh framework)

Repository: `mesh-framework` (renamed from `rope-framework` on 9 September 2026; the old URL redirects). See the naming note below.

**Published:** [https://doi.org/10.5281/zenodo.21430784](https://doi.org/10.5281/zenodo.21430784) · **Author ORCID:** [https://orcid.org/0009-0007-2454-5573](https://orcid.org/0009-0007-2454-5573) 

**Version:**
<!-- BEGIN GENERATED: version -->
3.31.0
<!-- END GENERATED: version -->

A machine-verified development of the Rope Hypothesis into the mesh framework: a classical, mechanical model in which the vacuum is a mesh of physical filaments and matter and light are its configurations, put into falsifiable, independently checkable form.

> **Naming (5 September 2026):** this programme is now **the Mesh Programme**, and the theory it develops **the mesh framework**. The vacuum object in every derivation is the mesh of strands (the mesh spacing a, the fine mesh a_f, mesh compression); "rope" remains the name of one specific thing in the theory, the two-strand wound object that is a particle, and the Rope Hypothesis credited to Bill Gaede keeps its name. The repository was renamed `mesh-framework` on 9 September 2026 (the old `rope-framework` URL redirects; the Zenodo concept DOI is unchanged). The `rope_solver` package, file names and claim IDs are identifiers and stay as they are.


> **This corpus establishes numerical reproducibility and internal consistency, not physical truth.** Whether the underlying physics is correct is exactly what external scrutiny is invited to decide.

> **What this is:** Imagine that everything in physics is one object — a rope — doing different things. Light is a ripple racing along it. Electric charge is the handedness of its two strands. Gravity is the shape the network takes around a mass. The Rope Hypothesis takes that single idea seriously and works out how far it goes: one physical substrate, three plainly stated assumptions (*the pair is one thing; the weave is warm; the quantum arrives whole*), and a mechanical picture you can actually visualise behind the equations. Where it reproduces known physics, it says so and claims no new prediction; where it reaches something new, it stakes a falsifiable bet.
>
> **What makes it unusual is the discipline.** Every claim is registered with a pass/fail line drawn *before* the computation runs, and the failures are kept on permanent display rather than quietly dropped. As of this release:
<!-- BEGIN GENERATED: corpus_stats -->
*766 registered claims, 641 code-backed and passing, 121 Derived, 47 registered Failed and kept.*
<!-- END GENERATED: corpus_stats --> A dealbreaker, if one exists, should be findable in about five minutes — start with [`KNOWN_LIMITATIONS.md`](KNOWN_LIMITATIONS.md).
>
> **Where it is strong (the five-line version):** electromagnetism and optics derive from one wave equation on the weave; the classic gravity tests (light bending, Mercury, clock rates) come out exact; the fine-structure constant lands at 178 ppm from geometry; chemistry and the nuclear mass table are full mechanical layers; and the exact quantum ceiling (the Tsirelson bound) is a theorem. Full account: [`docs/WHERE_IT_STANDS.md`](docs/WHERE_IT_STANDS.md); how it unfolded: [`docs/SURPRISES.md`](docs/SURPRISES.md).
>
> **The edges (the four-line version):** the k-string sector is parked on external lattice clocks after its own exact coefficient was killed at a blind checkpoint and kept; frame dragging has its form derived and its amplitude gated on the fine-strand scale; the quantum boundary (what guides the funneling) is the deepest open item; and gravity's raw strength (the ~40-order suppression) is located, not solved. Every edge carries a falsifier. Full account: [`docs/WHERE_IT_STANDS.md`](docs/WHERE_IT_STANDS.md); every caveat: [`KNOWN_LIMITATIONS.md`](KNOWN_LIMITATIONS.md).

> **Corpus state:**
<!-- BEGIN GENERATED: status_breakdown -->
766 registered claims (121 Derived, 556 Modeled, 4 EFT-constrained, 2 Conjecture, 7 Open, 47 Failed-and-kept, 29 registered); 641 code-backed.
<!-- END GENERATED: status_breakdown -->
> Counts regenerate from `claims.yaml` — the authority is the registry, not this line.

**📄 [THE QUEUE, PROCESSED, 5 Sep 2026](docs/history/RELEASE_NOTES_v3.31.0.md)** -- *v3.31.0*: seven charters executed in a day -- the PeV coincidence reduced to an identity (FND-166); LEAD-RAD's fence held by computation, 37-2000x (FND-167); bending-neutrality a theorem and the c-orbital identity a saturation (FND-168); the two E-identifications reconciled, A = -rho kappa_0 (s x z) (EM-023); no principle selects the level-2 amplitude, Sigma_wave retreats to 2.598 (FND-169); EW-001 and PM-001 demoted. Prior release: [THE FOURTH CELL AND THE REFINED GRID](docs/history/RELEASE_NOTES_v3.30.0.md).

**📄 [THE FOURTH CELL AND THE REFINED GRID, 5 Sep 2026](docs/history/RELEASE_NOTES_v3.30.0.md)** -- *v3.30.0*: the committed q = 5/4 FLAT prediction falsified at 144x36 (FND-163); every line mechanism down on re-pricing (proximity 0/12, j = n falsified, first-order coupling null); the 54-grid replication finds the 5/4 collapse physical and displaced 0.0003 deeper (FND-164, after a rescinded ARTIFACT verdict) and the founding 4/3 collapse NOT FOUND to A2 0.0055 (FND-165); the r discriminator retired for f_dir alone. Prior release: [THE WHY-WINDING ARC](docs/history/RELEASE_NOTES_v3.29.0.md).

**📄 [THE WHY-WINDING ARC, 29 Aug 2026](docs/history/RELEASE_NOTES_v3.29.0.md)** -- *v3.29.0*: six claims interrogating WHY the collapsing cell demands winding -- the collapse motion identified as a migration to a single high harmonic one step below the phi-Nyquist edge (FND-156), found NOT grid-stable (FND-157), and re-priced exactly: FND-152's registered f_dir rise is carried entirely by Nyquist-band content, the resolved-band share FALLING through the collapse while the flat control's band stays at zero (FND-158, RP-FALLS). Riders on FND-152/153; rates and D bounds untouched; the committed q = 5/4 FLAT prediction is the out-of-sample adjudicator. Prior release: [THE MECHANISM CLOSES](docs/history/RELEASE_NOTES_v3.28.1.md).

**📄 [Release history](docs/history/)** — every release note, per release, back to v3.0; the day summaries live there too.

**🪜 [The Ladder and the Frontier](figures/rope_ladder.png)** — the whole corpus in one image: three layers, every result placed by status, and the coherent frontier where the open problems cluster. The best single-glance answer to "what is this?" *(Hand-drawn architecture snapshot; for claim-level currency use the auto-generated Roadmap below, which rebuilds from the registry.)*

**🎨 [Figure gallery](figures/README.md)** — conceptual diagrams, each labeled with its corpus status (derived / modeled / hypothesis).

**✨ START HERE: [Thirteen Results We Did Not Expect](docs/SURPRISES.md)** — how the investigation actually unfolded: derived emergences, kept failures, labeled coincidences, and the day the framework eliminated its own favorite hypothesis. The best answer to "why spend an afternoon here?"

**🗺️ [Roadmap of Knowledge](docs/ROADMAP.md)** — the whole corpus at a glance: [wall chart](docs/roadmap.png) and [interactive dependency explorer](docs/roadmap.html) (click any claim; see its dependencies, dependents, and full downstream), all generated from claims.yaml by `tools/build_roadmap.py`.


<!-- BEGIN GENERATED: current_release -->
**Current release: v3.31.0** (5 Sep 2026), 766 claims.
<!-- END GENERATED: current_release -->
Headline: THE ENERGY BILL — priced and payable. The vacuum's constituents orbit at exactly c (two registered numbers multiplying to one), and the wave's dynamical share [0.62, 0.78] fits inside the matter sector's registered zero-point window (< 0.889): zero-point energy IS the winding's rotation. Full account: [`docs/history/RELEASE_NOTES_v3.26.77.md`](docs/history/RELEASE_NOTES_v3.26.77.md); prior: [`docs/history/RELEASE_NOTES_v3.26.76.md`](docs/history/RELEASE_NOTES_v3.26.76.md).

**Plain-language guide to the 17 Aug findings** (the vacuum as a rotating wave, the magic angle's triple duty, the energy bill): [`docs/VACUUM_WAVE_PLAIN_LANGUAGE.md`](docs/VACUUM_WAVE_PLAIN_LANGUAGE.md). Canonical constants card, revised: [`docs/ROPE_PARAMETERS.md`](docs/ROPE_PARAMETERS.md).

**If the mesh model is wrong**, the transferable result is
`docs/CONSTRAINTS_FOR_MECHANICAL_SUBSTRATE_THEORIES.md` — universal programme
disciplines, constraints on finite-scale mechanical substrates, and
rope-specific findings, kept in three explicitly separate tiers.

**Using a rope constant?** `docs/ROPE_PARAMETERS.md` is the canonical card —
every strand parameter, both scale branches, with a verifier
(`benchmarks/foundations/rope_parameter_card.py`) that fails if it drifts.

**New reader?** Start with `docs/STATE_OF_THE_PROGRAMME.md` — a short, current
account of what the framework claims, what it predicts, what was retired and why.

**Looking for something specific?** `docs/README.md` is a documentation map that
routes you by why you are here — evaluating the programme, understanding the ideas,
contributing, or verifying a specific claim.

## The committed bets and the prediction inventory

The full falsifiable inventory stands at **thirty-three live entries** (plus one
declared retrodiction and two retired-and-kept), maintained under one standard
in the predictions paper, re-rendered 17 Aug 2026 (paper edition 2.3.0):
[`papers/falsifiable_predictions.pdf`](papers/falsifiable_predictions.pdf)
(detailed audit: [`docs/PREDICTIONS_RECONCILIATION_v3_26_77.md`](docs/PREDICTIONS_RECONCILIATION_v3_26_77.md)).

Filtered strictly to **bets** (quantitative, distinctive in observable outcome,
checkable, live — a prediction any rival also makes is a commitment, not a
bet), the ledger holds four:

**1 — ADJUDICATED (13 Aug 2026): the k-string binding law.** Pre-registered
blind bands; external continuum data REJECTED the rival sine law's class and
KILLED the corpus's exact coefficient at 4.3σ past its own threshold — honored
without adjustment (FND-101/102, kept). A bet made, called, and paid.

**2 — ARMED AND WAITING: the adjoint Casimir-scaling pin.** Two committed
numbers, no freedom, bands pre-registered, blindness proven (no deciding
measurement exists, FND-105/106); the spec is shipped
([`docs/ADJOINT_CS_MEASUREMENT_SPEC.md`](docs/ADJOINT_CS_MEASUREMENT_SPEC.md)).
Waits on the field, not the corpus.

**3 — LIVE AND CONFRONTED: the coupling-drift ratio** d ln α = −2 d ln G
(PRED-003). Survives published clock and lunar-ranging data at 0.93σ — banked
honestly as null-versus-null, not as a win; it becomes discriminating when
either drift resolves.

**4 — NEW (17 Aug 2026): the zero-point share band.** The forced rotating-wave
vacuum commits the zero-point fraction of the vacuum energy budget to
**[0.615, 0.779]**, two-sided, lower edge exact, zero measured inputs
(Prediction 32; FND-130/131/132). Below 0.615 kills the wave reading
outright; above 0.779 breaks the two-level bracket. A one-sided survival
condition became a committed band in one day.

Full ledger and the census history: [`docs/WHERE_IT_STANDS.md`](docs/WHERE_IT_STANDS.md).

## Frame dragging (status: 17 Aug 2026)

**Form derived; amplitude gated.** The gravitomagnetic ratio is derived exactly
as Λ × J sin²θ/(Mc) — linear in spin, the Lense-Thirring angular form, correct
parity, radial dependence cancelling natively (GRV-120) — so frame dragging
exists in this framework with the correct shape and one dimensionless amplitude.
That amplitude factorizes as Λ = χ × Λ_nat: **frame dragging is a chirality
meter** — a parity-symmetric vacuum drags nothing (GRV-121). After the 17 Aug
arc the ceilings stand at Λ_nat ≤ 1.18e35 (GRV-128 chain, dynamical k_f) and
≤ 3.3e34 (FND-122 chain, reverted bound), both linear in a_f, with GR-strength
dragging demanding χ ≥ 8.5e-36 / ≥ 3.0e-35 respectively. Λ_nat remains gated
on the fine-strand scale (FND-110); whether cosmic birefringence shares the
vacuum's handedness is open, neither excluded nor confirmed (GRV-127). No
LARES comparison is quotable until the gate moves; condition 4 (one-parameter
measurement framing) is in force. Details:
[`KNOWN_LIMITATIONS.md`](KNOWN_LIMITATIONS.md).

## Two branches carry validated machinery and no target

Read before interpreting the quantum or gauge sectors as active physics.

- **The pilot-wave sub-quantum branch (QGATE-011..017)** is mathematically
  sound and empirically silent. Its results (flow uniqueness, CHSH 2.724 with
  verified no-signaling, the M=2-64 relaxation family, transport-over-chaos
  discrimination) are dimensionless and stand as registered, but ELEC-056
  showed by machine-checked audit that the branch never depended on the
  sub-quantum length it was said to inherit, and that length has since been
  corrected and its nuclear consequence excluded (ELEC-054/055). The branch
  has no current empirical content of its own.
- **The physical Aharonov-Bohm branch is CLOSED as unsupported**
  (ROPE-SOURCE-AUDIT-002). Nothing in the corpus sources a flux, and the one
  derived topological circulation (2 pi N) is exactly spectrally trivial in a
  2 pi periodic instrument. ROPE-VALIDATION-001..004 are retained as a
  validated gauge instrument with no internally sourced target. Reopening
  requires a new, explicitly labeled postulate.

The lesson from both is recorded as a standing rule:
docs/technical/STANDING_RULE_SOURCE_BEFORE_INSTRUMENT.md

## Start here

- **New to the corpus?** Read [`docs/PROGRAMME_OVERVIEW.md`](docs/PROGRAMME_OVERVIEW.md) — the generated front door (assumptions, the continuum chain, computed maturity, open problems, reading order).
- **Non-specialist?** Read [`papers/rope_plain_language_guide.pdf`](papers/rope_plain_language_guide.pdf) — "The Rope Picture of the Universe," a figures-first, no-mathematics tour that flags every honest limit.
- **Curious what the detector-kinetics campaign found?** Read [`papers/the_detector_understood.pdf`](papers/the_detector_understood.pdf) (source: [`docs/DETECTOR_KINETICS_PLAIN_LANGUAGE.md`](docs/DETECTOR_KINETICS_PLAIN_LANGUAGE.md)) — three questions answered in plain language: how a single-photon detector works (the medium is its own metronome), why small detectors appear to have memory without anything remembering (the switch-on echo, plus the zero-parameter size law at Derived), and how single photons build interference patterns one dot at a time (the wave delivers the odds; the bath delivers the dot) -- with the measured boundary stated and every sentence traced to a benchmark.
- **Reviewer or skeptic?** Read [`HOW_TO_CRITICIZE.md`](HOW_TO_CRITICIZE.md) and [`KNOWN_LIMITATIONS.md`](KNOWN_LIMITATIONS.md) first, then verify (below).
- **Want to contribute?** The programme is open to building, not only breaking. Pick an `Open` problem from the registry (`claims.yaml`, mirrored as GitHub Issues via [`docs/SUGGESTED_ISSUES.md`](docs/SUGGESTED_ISSUES.md)) — e.g. the reaction-coherence fraction (CHEM-DYN-002's registered next step), the strand-level transport instantiation (FND-KIN-001's named residual), or the two theorems slated for Lean formalization. The standing open challenge is [`docs/technical/FUTURE_MODEL_PROMPT_one_fence.md`](docs/technical/FUTURE_MODEL_PROMPT_one_fence.md): derive the missing quantum-kinetic layer the whole corpus triangulates. New results are welcome as claim + rerunnable benchmark (the one rule: no hidden fitted parameters); see [`CONTRIBUTING.md`](CONTRIBUTING.md).

## Verify it yourself

This is a reproducible research programme, not just a set of papers. The entire suite runs on a laptop in about 90 seconds — no GPU, no cluster, no large data.

```bash
pip install -e .
python tools/verify_corpus.py     # runs every registry benchmark; exit 0 iff all pass
```

`verify_corpus.py` runs each code-backed claim's benchmark and reports pass/fail per claim, plus which claims are paper-only (status-labelled, not machine-verified). This "laptop invariant" is a deliberate methodology choice that keeps the corpus independently checkable.

## How the corpus is organized

Every claim carries a status label and, where code-backed, a rerunnable benchmark. The three artifacts are tied together by the registry:

- **`claims.yaml`** — the machine-readable registry, the single source of truth. Every claim names its status (Derived / Modeled / EFT-constrained / Conjecture / Open / Failed), its paper, and its benchmark.
- **`/papers`** — the physics papers (PDF), with editable sources in `/papers/_sources`.
- **`/benchmarks`** — one rerunnable check per code-backed claim.

**How the corpus guards against motivated derivation.** [`docs/technical/METHODOLOGY_target_free_questions.md`](docs/technical/METHODOLOGY_target_free_questions.md) — the rule that when a candidate factor is worth approximately what the gap needs, the question to ask first is the one whose answer is wrong *wherever it lands*, because such a question cannot be biased by knowing the target. Written from a worked case (FND-MATTER-058/059/060) in which it reversed the answer: a sound argument for a gap-closing factor turned out to prove the opposite of its conclusion, and the session that found this answered against its own prior position. Also carries the stopping-rule requirement — a sequence of individually-blind sessions without a pre-committed terminal condition is a fit with extra steps.

**How to read the honesty of the corpus.** The registry makes the `Failed` and `Open` claims as visible as the `Derived` ones. Losses are preserved as findings: the classical weak-field gravity no-go (derived deflection 0.44″ vs measured 1.75″), the PVLAS vacuum-birefringence exclusion (~570×), and and the quantum boundary documented as explicit limits rather than solved problems — now mapped to high precision by the measurement arc (Born-rate scaling benchmarked-but-conditional, entanglement localized to one imported object, γ = 1 identified), with Pauli still Conjecture-level.

## What is derived, what is adopted

A sector earns "Derived" status only where it follows from the strand mechanics, and the corpus is explicit where it instead *adopts* an established description:

- **Electromagnetism / optics** — Maxwell's equations, charge as winding, optics (10/10 benchmarks); the strongest derived sectors.
- **Chemistry** — a full mechanical layer: covalent bonding from a mode-overlap functional, the ionic-force sign theorem, first-principles molecular geometry (the 90° heavy-hydride asymptote, with registered predictions for H₂Po and BiH₃), hydrogen bonding, metallic bonding, and reaction dynamics (activation barriers from phase-frustration; Hammond and catalysis emergent). **The Schrödinger equation is adopted, not derived** — ℏ and the absolute atomic scale are inherited inputs (see the chemistry paper, §3.1a). Several energies are "consistency-tier" against quantum chemistry, and labeled as such.
- **Gravity** — Newtonian gravity is recovered; the relativistic completion is falsified under stated assumptions (a theorem-grade no-go, not a fixable discrepancy).
- **Nuclear** — an exact Yukawa force law and two mass tracks that meet in the middle: a discrete bond-counting model from A=2..16 (one He-4-calibrated constant, r = 0.978; the A=5 instability, the Be-8 maximum, and C-12's three-alpha structure all emerge rather than being imposed — NUC-007/008/009), and a semi-empirical mass formula now derived from classical physics across all five terms (volume, surface, Coulomb with diffuseness and exchange, asymmetry, pairing) spanning A~8 through U-238 with the heavy-table binding gap closed to ~1%; H-1 remains inputs-by-construction and a quantum shell/pairing tier remains the registered frontier.
- **Particle sector** — lepton mass ratios (Koide) and the Weinberg angle DEMOTED to kept coincidences (v3.31.0: sensitivity 71; three choice points); no derived Weinberg angle; the absolute mass scale is an open problem.

## Repository structure

```
mesh-framework/
  README.md                 you are here
  CITATION.cff              "Cite this repository" metadata (DOI + ORCID)
  CONTRIBUTING.md           how to verify, and how to criticize
  HOW_TO_CRITICIZE.md       where the programme is most vulnerable
  KNOWN_LIMITATIONS.md      every load-bearing caveat in one place
  CHANGELOG.md              full revision history
  claims.yaml               THE REGISTRY — single source of truth for every claim
  /papers                   physics papers (PDF); sources in /papers/_sources
  /docs                     overview, registry docs, methodology, glossary
  /rope_solver              the Python package
  /benchmarks               one rerunnable check per code-backed claim
  /tests                    regression tests
  /examples                 worked examples
  /figures                  diagrams
```

## Install

```bash
pip install -e .          # installs `rope_solver` (numpy, scipy, sympy)
```

After install, imports work from anywhere:

```python
from rope_solver.psi.solver import solve_psi, ring_source, field_energy
from rope_solver.topology.linking import hopf_curves, linking_number
```

## The reference-implementation principle

Every physical number cited in a rope paper comes from an installed `rope_solver` function or a registry benchmark with a regression test pinning it — never from a one-off script. There is exactly one place each quantity is computed, which is what keeps the papers consistent with one another and with the code.

## Contributing and criticizing

The programme welcomes both kinds of contribution. **To criticize:** the highest-value find is a claim labeled `Derived` that actually requires a hidden fitted parameter — the failure mode the entire methodology is built to prevent. **To build:** take an `Open` problem from the registry and contribute a claim plus a rerunnable benchmark, under the one rule that no `Derived` result may hide a fitted parameter. Open problems are tracked in the registry and mirrored as GitHub Issues (templates in [`docs/SUGGESTED_ISSUES.md`](docs/SUGGESTED_ISSUES.md)); the standing open challenge is [`docs/technical/FUTURE_MODEL_PROMPT_one_fence.md`](docs/technical/FUTURE_MODEL_PROMPT_one_fence.md). See [`CONTRIBUTING.md`](CONTRIBUTING.md) for setup and the issue-priority list.

## Citation

See [`CITATION.cff`](CITATION.cff) (GitHub renders a "Cite this repository" button). To cite the evolving project rather than this snapshot, use the Zenodo *concept* DOI, which always resolves to the latest version. Intellectual origin of the rope concept: Bill Gaede; this is an independent, mathematized development that departs from his formulation (see [`docs/attribution.md`](docs/attribution.md)).

## License

MIT — see [`LICENSE`](LICENSE).
