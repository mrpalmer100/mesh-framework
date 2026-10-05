# Documentation map

A guide to what to read, by why you are here. The full corpus is large; almost no
one needs all of it. Find your row below and start there.

Most of these documents are **generated from the claim registry** (`claims.yaml`)
and stay current by construction; the rest are hand-written and dated. Nothing here
needs to be read in full to evaluate the programme.

---

## If you are evaluating the programme (funder, reviewer, sceptic)

Read these, roughly in order. They are written to be read, not waded through.

- **[Programme overview](PROGRAMME_OVERVIEW.md)** — the front door: what the
  programme is, its structure, maturity by sector, and open problems. Generated.
- **[State of the programme](STATE_OF_THE_PROGRAMME.md)** — the honest narrative
  account: what works, what fails, what is predicted, where the edges are.
- **[Known limitations](../KNOWN_LIMITATIONS.md)** — every load-bearing caveat in
  one place, so you never have to hunt for the catch. (At the repository root.)
- **[External review package](EXTERNAL_REVIEW_PACKAGE.md)** — the curated
  eleven-paper reading set, in order, with the **[claim-status
  registry](rope_claim_status_registry.pdf)** as the map to navigate it.
- **[Surprises](SURPRISES.md)** — the results, wins and failures alike, that were
  not expected going in. A fast sense of what the programme actually does.
- **[How to criticize](../HOW_TO_CRITICIZE.md)** — where the programme thinks it is
  most vulnerable, and how to attack it. (At the repository root.)

## If you want to understand the ideas

- **[Five Mesh Challenges](MESH_CHALLENGES.md)**: break one of five load-bearing derivations;
  frozen inputs, one command each, the bar and what falls.
- **[SM Emergence](SM_EMERGENCE.md)**: the Standard Model's structure in twelve
  rows, each derived, partial or unexplained, cited by claim id.
- **[Where it stands](WHERE_IT_STANDS.md)** — strengths, edges, and the
  committed bets, in full (the README carries the short version).
- **[Philosophy](philosophy.md)** — why the rope model; the motivation.
- **[Ontology](ontology.md)** — what each phenomenon *is* under the rope reading.
- **[Plain-language guide](../papers/rope_plain_language_guide.pdf)** — "The Rope
  Picture of the Universe": the concepts without the machinery. (Built from
  `guide/topics/`; see `guide/README.md` for the build system.)
- **[How 1/α was derived](HOW_ALPHA_WAS_DERIVED.md)**, **[the detector,
  understood](DETECTOR_KINETICS_PLAIN_LANGUAGE.md)**, and **[the number that
  wasn't there](EXACT_D_ARC_PLAIN_LANGUAGE.md)** — worked results in plain
  language (the third is the six-commission exact-D gravity arc).
- **[Attribution](attribution.md)** — intellectual origin; the core hypothesis is
  due to Bill Gaede, developed and formalised here.

## If you want to contribute

- **[Contributing](../CONTRIBUTING.md)** — how the corpus is kept honest, and the
  freshness gate that keeps the docs from drifting. (At the repository root.)
- **[Suggested issues](SUGGESTED_ISSUES.md)** — the live open frontier as research
  questions you could pick up. Generated from the registry.
- **[Roadmap](ROADMAP.md)** — sector maturity, computed from claim status and
  benchmark coverage. Generated.
- **[Constraints for mechanical substrate theories](CONSTRAINTS_FOR_MECHANICAL_SUBSTRATE_THEORIES.md)**
  — the disciplines a finite-scale mechanical theory must respect.

## If you want to verify a specific claim

- **[Papers index](PAPERS.md)** — every paper, what it establishes, and its status.
- **[Benchmarks](BENCHMARKS.md)** — the stable-ID benchmark catalogue; papers cite
  the ID so any number traces to a regression-tested quantity.
- **[Parameter card](ROPE_PARAMETERS.md)** — every quantity describing a strand,
  with its status, provenance, and value. Self-verified.
- **[Quantum-input ledger](QUANTUM_LEDGER.md)** — which claims genuinely depend on a
  quantum input, and which only borrow the vocabulary. Generated.
- **[Instruments](INSTRUMENTS.md)** — the external tests and apparatus the framework
  points at.
- **[API reference](API.md)** / **[API stability](API_STABILITY.md)** — the
  `rope_solver` interface.
- **[Provenance](PROVENANCE.md)** and **[manifest](MANIFEST.md)** — which documents
  are generated vs hand-written, and the file inventory.

---

## Subfolders

- **`technical/`** — machine-facing work records: sector-closure notes, campaign
  syntheses, sealed-commission audits, methodology and standing rules, AI task
  prompts. Provenance and traceability, not reading for a newcomer.
- **`history/`** — per-release notes for every version, including the current one,
  plus superseded state documents. Each is a frozen snapshot (never updated); the
  newest matches the current release, and `README.md` links straight to it.
- **`commissions/`** — the commission audit records (the `A`–`F` and later series).
- **`api/`** — generated API reference detail.
- **`figures/`** — figures referenced by the docs and papers.
- **`_superseded/`** — renders that no longer match their source, kept for
  traceability.
