# The Mesh Lab: a guide for new reviewers

*Written 11 October 2026 for readers new to the project. No physics background is assumed. Part 8 is a dated snapshot; everything else describes how the lab works.*

---

## In one paragraph

The Mesh Programme is an independent physics research project led by Mark Palmer. It asks whether a single mechanical picture of the vacuum can explain light, electricity, magnetism, gravity and the masses of atoms, using as few adjustable numbers as possible. Until October 2026 the work was done by Mark directly, in working sessions with an AI research assistant. The **Mesh Lab** is the next step: a small computer in Mark's home that runs the research around the clock with no one at the keyboard. AI agents propose experiments, write them up, have them checked by independent AI reviewers, run the calculations, and record the results. Mark's role is to approve what goes into the project's official record. This guide explains what the lab does, how it is kept honest, and where a reviewer should look.

---

## Part 1. The research the lab serves

### The idea

Most of modern physics describes nature with very accurate formulas, but some of its explanations are hard to picture. Why does a magnet pull? What is gravity, mechanically? The Standard Model of particle physics is extremely successful, but it needs about nineteen numbers that have to be measured, not explained.

The mesh framework explores a different starting point: the vacuum is a physical mesh of strands, and matter and light are things the mesh does. Light is a ripple travelling through it. Electric charge relates to the handedness of strands that are wound together. Gravity is the shape the mesh takes around a mass. The project works out, in detail and with computer checks, how far that one idea can be pushed.

The project's stated goal, kept in the repository as [`docs/NORTH_STAR.md`](NORTH_STAR.md), is a model that makes sense mechanically and predicts measured quantities, such as the weights of atoms, the strength of gravity and the strength of magnets, with fewer fitted inputs than the Standard Model.

### The house rules

The project is unusual less for its idea than for its discipline. Anyone reviewing it should understand four rules, because the lab is built to enforce them.

1. **The pass/fail line is drawn before the experiment runs.** Every investigation starts with a written plan called a **charter**. It states the question, the exact calculation, and what result counts as success or failure. The charter is **locked** before any data is produced, much as a clinical trial registers its endpoints in advance. You cannot move the goalposts once you have seen where the ball landed.

2. **Every finding becomes a numbered claim.** Results are entered in a public registry ([`claims.yaml`](../claims.yaml)) with an identifier such as `GRV-045` or `FND-163`. Each claim has a status: *Derived*, *Modeled*, *Open*, *Failed*, and so on. The registry holds about 780 claims today.

3. **Failures are kept.** When a prediction fails, it is not deleted or quietly reworded. It stays in the registry marked *Failed*, with its explanation. There are about 49 such entries today, and the project counts them as evidence of honesty, not embarrassment.

4. **"Reproduces known physics" is not the same as "predicts new physics."** The project grades its own results (D0 to D3, see [`docs/DERIVED_GRADES.md`](DERIVED_GRADES.md)), separating true derivations from reconstructions that use measured inputs. The README states plainly that the corpus establishes reproducibility and internal consistency, not physical truth.

### The bottleneck

Before the lab existed, every step waited on Mark: drafting a charter, reviewing it, launching a calculation, reading the result. Some calculations take hours or days of computer time. The lab exists so this work continues while Mark is at his day job, asleep, or travelling, without loosening any of the rules above.

---

## Part 2. What the lab is

### The machine

The lab runs on a Mac mini (Apple M5 Pro, 18 processor cores, 64 GB of memory) in Mark's home. It is set up to run without a screen and to restart by itself after a power cut. Mark can reach it remotely from his laptop or phone over a private encrypted network.

The software has two halves:

- **The runner** is the compute side. It runs the long physics calculations, watches them, restarts them if they crash, and keeps them from overloading the machine.
- **The agents** are the thinking side. AI models play defined roles, coordinated by a scheduler that hands out one task at a time.

Everything the lab does is recorded in a database on the machine and in a version-controlled copy of the project on GitHub.

### The cast

| Role | Played by | What it does |
|---|---|---|
| **Research Director** | Claude Fable 5.1 (Anthropic) | Reads the state of the project and proposes the next experiments. It must say what question each one answers and what result it expects. It does not get to run anything. |
| **Worker** | Claude Sonnet (Anthropic) | Turns an approved proposal into a full charter, writes the calculation code and the scoring script, and tests them on a small scale. Later it writes up results. |
| **Skeptical reviewer** | Claude Fable 5.1 (Anthropic) | Reads every charter before it is locked and every result before it is recorded, looking for flaws, loopholes and overclaiming. |
| **External reviewer** | GPT-6 Astra (OpenAI) | Does the same job independently, from a different AI company's model. The point is that two different model families are less likely to share the same blind spots. |
| **Decider** | Claude Fable 5.1 (Anthropic) | Settles any commission that cannot proceed as written, without asking anyone, and records why (Part 3, step 5). |
| **Digest writer** | Claude Haiku (Anthropic) | Writes a short daily summary of what happened. |
| **The runner** | Ordinary software, no AI | Runs calculations, enforces limits, keeps the record. |
| **Mark** | A human | Decides what enters the official record. |

The decisions that matter most (what to try next, whether a charter is sound, how to settle a stuck commission) go to the strongest models available; each role falls back to the next model on its list if one is unavailable. If OpenAI is ever unavailable (for example, the account runs out of credit), the external review falls back to a Claude model, Opus. Each time that happens it is flagged in the daily summary and in the request Mark approves, so a reader always knows which reviews lacked a reviewer from outside the Claude family.

---

## Part 3. The life of an experiment

The lab calls each experiment a **commission**. Every commission passes through the same stages, and the system will not let it skip one.

```
 PROPOSED --> DRAFT --> REVIEWED --> LOCKED --> RUNNING --> VERDICT --> PROVISIONAL --> PROMOTED
 Director     Worker    both          plan       runner      scoring     result         Mark
 proposes     writes    reviewers     frozen     computes    script      recorded on    approves
              charter   approve                              runs once   lab branch     into main
```

**1. Proposal.** The Director reviews the project's open questions and proposes a commission. It must name the question, the claims involved, and its own prediction of the outcome, registered *before* anything is computed. It may also leave slots empty if nothing is worth doing. Its first proposal did exactly that: it put forward one commission and explained why it left the second slot open.

**2. Drafting.** The Worker writes the charter in the project's house format, along with the calculation code and a scoring script. It tests the code on a tiny version of the problem inside a sealed sandbox.

**3. Review.** Both reviewers read the charter against a fixed checklist. Is the question well posed? Is the pass/fail line stated precisely enough that it cannot be argued with afterwards? Could the code quietly change something it should not? Are the claims properly cited? If either reviewer objects, the charter goes back to the Worker with the objections, for up to three rounds. If it still fails, the commission is shelved and the Director moves on.

*A real example from the lab's first weekend:* the first commission, `GRV-BLIND-2` in the gravity series, was sent back after GPT-5 objected that the code needed safeguards around its irreversible steps. The Worker revised it, and the revised charter went back for review. This is the system working as designed.

**4. Locking.** Once both reviewers approve, the charter is locked: the plan, the code and the scoring script are frozen, given a digital fingerprint, and committed to the project's history. From this point nothing that affects the result can be changed silently. A genuine fix (for example, a crash in the code) needs a formal, recorded amendment and its own review, and the rules distinguish fixes made before any data exists from fixes made after.

**5. Running.** The runner executes the calculation. Big runs can take days and are broken into steps that can be paused and resumed. If a run gets stuck, a Worker diagnoses it and may restart it or propose a reviewed fix, a limited number of times. Anything it cannot fix, and any commission whose code refuses to continue because something is missing, goes to the **Decider**, which settles it without asking anyone: either it replaces a missing outside step with the public randomness beacon (below), through a charter amendment that both reviewers must pass, or it withdraws the commission. The lock stays on the record either way, and the decision is written up for Mark to review later.

*Blind draws without a person.* Some tests need a random choice that nobody involved controlled, such as which galaxies to hold back as a blind test set. The lab uses the drand public randomness beacon, a value published every 30 seconds by an independent network and checkable by anyone. The lab commits to a specific future round on GitHub before that round exists, then uses its published value as the seed. Neither Mark, the lab nor any agent can choose or predict it. It is independent, but it is not the same as a human adjudicator, and the lab never presents it as one.

**6. Verdict.** When the calculation finishes, the locked scoring script runs **once** and prints its verdict, a pre-declared label such as `BLIND-AGREES` or `FAILED`. The lab checks that the fingerprints still match the locked versions before it accepts the verdict.

**7. Write-up and second review.** The Worker writes a plain account of the result and drafts any claims for the registry. Both reviewers check that the write-up says what the verdict says and nothing more. If the result confirms the Director's own prediction, an extra outside review is required, to guard against the lab grading its own homework.

**8. Provisional record.** Claims enter the registry marked **Provisional**. They live on a separate branch of the project called `lab`, not on the main version the public sees.

**9. Promotion.** Once a week the lab bundles everything new into a single request on GitHub, listing every commission, verdict, claim, amendment and anything flagged. Mark reads it and merges it into the main project if he agrees. Only then do Provisional claims become registered. He can also veto any claim or reverse any decision.

---

## Part 4. How the lab is kept honest

An autonomous system that writes its own experiments and grades its own results needs guard rails. These are the main ones, and each is enforced by the software, not by good intentions.

| Risk | Safeguard |
|---|---|
| Moving the goalposts after seeing data | Charters are locked and fingerprinted before running. Changes need recorded amendments. Verdict scripts run once. |
| Fishing: retrying a question until it gives the wanted answer | A question can be attempted at most twice per project version. Every proposal records its prediction up front. |
| One AI reviewing its own work | Two reviewers, one from a different company. Extra review when a result confirms the proposer. Every fallback to a Claude reviewer is flagged. |
| Too much happening too fast for a human to follow | At most two charters can be locked per week, a limit Mark can raise as trust grows. |
| AI-written code doing something unintended | All agent-written code, and every commission run, executes in a sandbox with no internet access and no access to passwords or keys. |
| The record being edited after the fact | The ledgers of events, verdicts, seals and reviews are append-only in the database: the software refuses to alter or delete entries. |
| Lab output reaching the public record unchecked | The lab works on its own branch. Only Mark's merge moves anything to the main project. |
| Runaway spending | Hard daily and monthly dollar caps per AI provider. At a cap, agent work pauses and the calculations keep running. |
| Breaking the project's integrity checks | Every commit runs the project's own corpus verifier first, and is undone if it fails. |
| The lab quietly taking decisions meant for a person | Every decision the lab makes on its own (settling a stuck commission, a beacon draw, a withdrawal) is written up with its full reasoning in `analysis/lab/decisions/`, listed in the daily digest and listed again in the weekly promotion request for Mark's review. Any of them can be reversed. |

Some limits a reviewer should keep in mind:

- **The reviewers are AI models.** They are careful and they follow a checklist, but they can miss things, and two models can sometimes share a misconception. Human review of anything that matters is still the final check, which is why promotion goes through Mark.
- **Passing review is not the same as being right.** The lab's machinery protects the *process*, so that results are pre-registered, reproducible and honestly reported. Whether the physics is correct is a separate question, which outside scrutiny exists to answer.
- **The lab inherits the project's open problems.** It does not solve them by being automated. The project's own list of weaknesses is in [`KNOWN_LIMITATIONS.md`](../KNOWN_LIMITATIONS.md).

---

## Part 5. The lab's memory

The project is large: about 780 claims, hundreds of charters and results documents, and years of history. The agents cannot read all of it every time. The lab keeps a searchable index of the whole project, updated automatically as it changes, so an agent can find the claims, charters and past results relevant to a question. Each agent receives that context with its task. When a charter cites a claim, the reviewers see the claim's actual text.

---

## Part 6. What Mark does, and what he does not do

Mark's involvement is deliberately small:

- He **merges the weekly promotion request** (or doesn't). This is the human gate.
- He **can veto** any claim or commission at any time.
- He **sets the budget caps** and the weekly lock limit.
- He reads the **daily digest** if he wants to, and reviews the **decisions the lab made on its own** when he merges.

He does not need to approve each proposal, charter or run, and the lab never stops to ask him. The design aim is a lab that keeps working when he is busy and never waits on him, while nothing reaches the official record without his merge.

---

## Part 7. How to review the lab's work

If you are evaluating the project or the lab, these are the places to look.

| What | Where |
|---|---|
| What the lab did each day | `analysis/lab/digests/YYYY-MM-DD.md` on the [`lab` branch](https://github.com/mrpalmer100/mesh-framework/tree/lab) |
| Each weekly bundle of new work | [Pull requests](https://github.com/mrpalmer100/mesh-framework/pulls?q=is%3Apr+%22Promote+lab+version%22) titled "Promote lab version lab-YYYYMMDD-N" |
| Locked charters | `analysis/<NAME>_charter_LOCKED.md` |
| Verdicts, with fingerprints | `analysis/lab/verdicts/<NAME>.json` |
| Decisions the lab made on its own, with reasons | `analysis/lab/decisions/` on the `lab` branch |
| Committed beacon rounds for blind draws | `analysis/lab/beacons/` on the `lab` branch |
| Results write-ups | `analysis/<NAME>_results.md` |
| The claims registry | [`claims.yaml`](../claims.yaml) (Provisional entries are the lab's, pending approval) |
| The project's goal and scorecard | [`docs/NORTH_STAR.md`](NORTH_STAR.md) |
| The project's own list of weaknesses | [`KNOWN_LIMITATIONS.md`](../KNOWN_LIMITATIONS.md) |
| Guidance for critics | [`HOW_TO_CRITICIZE.md`](../HOW_TO_CRITICIZE.md) |

Useful questions to ask of any commission:

1. **Was the bar set before the data?** Compare the lock date of the charter with the dates of the results.
2. **Did the verdict follow the bar exactly?** The verdict label should follow mechanically from the locked scoring script, with no judgment call added afterwards.
3. **Were there amendments, and when?** Amendments made after data existed deserve the closest reading.
4. **Did the external reviewer actually come from outside?** Check the promotion request for the "Reviewed without the outside model family" section.
5. **Does the write-up claim more than the verdict?** This is the most common failure in any research programme, human or automated.
6. **What would have counted as failure, and did failure happen?** A programme that never records a failure is not testing anything.

---

## Part 8. Status as of 11 October 2026

- The lab went live on 10 to 11 October 2026.
- **The runner** is running a long calculation carried over from Mark's earlier manual work, part of a commission called COMPOSITE-SELECT (Leg B). It is in its last cells and needs about 25 GB of memory.
- **The agents** completed their first full cycle on their own. The Director proposed `GRV-BLIND-2`, the Worker drafted it, the external reviewer sent it back with objections, and the revised draft went back into review.
- **Spending** in the first two days ran about $12 to $15 a day on AI services, inflated by start-up costs and one bug, since fixed. A typical day is expected to cost less.
- **Nothing produced by the lab has yet been promoted** into the main project.

---

## Glossary

**Charter.** The written plan for a commission: question, method, pass/fail lines and possible verdicts, fixed in advance.

**Claim.** A numbered finding in the registry, such as `NUC-018`, with a status and an explanation.

**Commission.** One experiment or investigation, from proposal to recorded result.

**Corpus.** The whole body of the project: claims, charters, code, results and papers.

**Digest.** The lab's daily plain-language summary.

**Lab branch.** The separate copy of the project where the lab records its work, kept apart from the public main version until Mark merges it.

**Lock.** The moment a charter is frozen and fingerprinted. After it, results cannot be steered.

**Promotion.** Mark's merge of the lab's weekly work into the main project.

**Provisional.** The status of a lab-produced claim that Mark has not yet approved.

**Runner.** The non-AI software that runs and supervises calculations.

**Sandbox.** A locked-down environment in which code runs with no internet and no access to secrets.

**Seal.** A recorded fingerprint of a finished calculation's outputs, checked before the verdict is accepted.

**Verdict.** The pre-declared label a commission's scoring script prints when the calculation is done.
