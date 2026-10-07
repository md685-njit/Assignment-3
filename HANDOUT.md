# CS 690 Assignment 3: Evidence to Executable Specification

**100 points. Individual assignment.**

## Learning goals

By completing this assignment, you will be able to:

1. Turn raw stakeholder input into bounded requirements and acceptance criteria (Week 5, requirements).
2. Tell real-user evidence apart from assumptions and synthetic-user output, and judge AI-generated ambiguity findings yourself (Week 5, requirements).
3. Trace every executable test back through an acceptance criterion and a requirement to a piece of evidence (Week 5, requirements).
4. Write a compact, implementation-ready specification with a typed interface, preconditions, postconditions, an invariant where one applies, a non-goal, and explicit open questions (Week 6, specifications).

## Context

The Week 5 lecture covered the path from an interview to evidence notes, user stories, Given-When-Then acceptance criteria, and tests. The Week 6 lecture added types, contracts, and the design doc that separates settled decisions from open questions, so an implementation agent does not invent product behavior nobody decided. This assignment puts both lectures together on one small case.

The same skills carry over to your team project in Milestone 1, but this assignment is individual practice. Use the provided case. Do not substitute your team project for any part of it.

## Why this matters at work

- Product teams interview users before they build. The notes that reach engineers often contain the mistakes you will catch here: a compliment read as demand, a prediction read as behavior, one person's view read as everyone's.
- Agile teams turn conversations into user stories and Given-When-Then criteria every sprint, and those criteria become the tests that decide when a ticket is done.
- When an AI coding agent writes the code, a short spec with its open questions marked is what stops the agent from guessing and shipping the guess with passing tests.
- Checking an AI summary or an AI review against the source is now routine work, and it is the same true or false positive judgment you make in Part 6.
- Aviation, automotive, and medical-device software standards require tracing every requirement to its tests. The ledger adds a record of what AI produced and how it was checked, which is what lets a reviewer trust the work.


## What you are given

This repository contains:

- `transcripts/interview.txt`, one interview, case INT-01, with paragraph IDs P01 to P21.
- `synthetic/synthetic_user_output.md`, one pre-generated synthetic-user response, SYN-01.
- `evidence/schema.md`, the E, A, and Q evidence-log scheme and an unrelated worked row.
- `spec/spec_template.md`, the required specification structure.
- `traceability/template.csv`, the traceability matrix shell.
- `reference/`, a small reference module. Policy values such as the grace period are inputs to it, not choices it makes for you.
- `tests/test_student_acceptance.py`, the file in which you write exactly three tests.
- `prompts/ambiguity_audit_prompt.txt`, the required prompt for Part 6.
- `results/ambiguity_audit.md`, where you store the complete Part 6 model response.
- `report/REPORT_TEMPLATE.md`, an optional structure for the PDF report.
- `LEDGER.md`, the required provenance ledger.
- `RUBRIC.md`, how the 100 points are awarded.

`README.md` covers setup, and how to call the reference module. The only verification command you need is:

```bash
python -m pytest -q
```

You do not need to build a product, frontend, backend, API, database, or deployment. You do not need to run the AI more than once or run any experiment.

## The task

### Part 1. Build an evidence log

In lecture we covered writing down quotes with IDs: E for evidence, A for assumptions, and Q for open questions.

Read `transcripts/interview.txt`. Create an evidence log with **8 to 10 entries total** using the table in `evidence/schema.md`.

1. Use `E-<n>` for something the real interview establishes.
2. Use `A-<n>` for an assumption the interview does not establish.
3. Use `Q-<n>` for an open question that must be answered before a related decision is settled.
4. Give every entry a source. Transcript citations use `INT-01:Pxx`, or a comma-separated list such as `INT-01:P06, INT-01:P12`.
5. Do not cite `SYN-01` as real-user evidence.

Keep the uncertainty. If the interview does not support one answer, record the uncertainty instead of picking a plausible answer.

### Part 2. Audit the evidence

In lecture we covered the Mom Test (compliments and predictions are not evidence; past events are), ambiguous words, contradictions, and stakeholders.

Create a seven-row audit table, one row for each item below. Each item appears in the interview.

1. **The direct factual contradiction:** two speakers state different facts about the same thing. Do not decide which speaker is right. As in lecture, a conflict is a question for a stakeholder, not a choice for you or an agent.
2. **Ambiguous statement 1.**
3. **Ambiguous statement 2, of a different kind from the first.** For example, one may be a vague amount or time and the other an unclear who or what, like the "one day before" and "patients" examples from the Week 5 lecture.
4. **The missing stakeholder:** a group the interview keeps mentioning, whose work the requirements depend on, but who was never interviewed.
5. **The compliment** that must not be treated as evidence.
6. **The prediction about future use** that must not be treated as evidence of current behavior.
7. **The strongest account of a specific past event** in the transcript.

For every row, give the paragraph ID or IDs, classify the item, and write at most two sentences on why it matters to requirements quality.

### Part 3. Write four requirements and three acceptance criteria

In lecture we covered user stories in Connextra form, structured requirements, INVEST, and Given-When-Then acceptance criteria.

Write **exactly four requirement slices**, `R-1` through `R-4`. Each slice contains:

1. One user story in Connextra form: `As a <role>, I want <capability>, so that <benefit>.`
2. One structured requirement that states a behavior someone can observe.
3. A trace to one or more evidence IDs from Part 1, or the label `Assumption` plus a clarifying question if the interview does not settle the decision.

Do not hard-code a disputed interview value as settled policy. Use a configured value instead, or leave the choice open with a clarifying question.

For each slice, complete a compact INVEST check: mark Independent, Negotiable, Valuable, Estimable, Small, and Testable as pass or fail. Any failure must name the problem, such as `couples waitlist notification to technician workflow`, not just the letter.

For **three different requirements**, write exactly three acceptance criteria, `AC-1` through `AC-3`, in Given-When-Then form. Each has concrete starting conditions in Given, one event or action in When, and an observable result in Then. A criterion must not quietly settle an open product-policy question. It may use a configured value instead, for example "Given the lab's configured grace period is G minutes".

**Your three acceptance criteria become tests in Part 5, so write them about behavior the reference module can check:** reservation status (grace period, check-in, staff hold) or whether a kit may be offered to the waitlist. A requirement about messages or notifications is fine in R-1 to R-4, but nothing in this assignment can test it, so do not choose it for an acceptance criterion.

### Part 4. Make one requirement implementation-ready

In lecture we covered preconditions, postconditions, invariants, types as specifications, and the design doc sections for non-goals, edge cases, and decisions and open questions.

Choose one of your four requirements whose core behavior is settled enough to specify without inventing product policy. Complete `spec/spec_template.md` for it. Your specification must contain:

1. A typed Python function signature, using the types from lecture where they fit (for example `Literal` or `int | None`).
2. Explicit preconditions: what the caller must make true first.
3. Explicit postconditions: what the function promises at the end.
4. One invariant if the behavior has stored or repeated state. If no invariant applies, write `Not applicable` and one sentence explaining why.
5. Edge cases an implementation agent must handle.
6. Exactly one non-goal.
7. Settled decisions.
8. Open questions the implementation agent is not allowed to answer by guessing.

Do not write the implementation. The goal is to constrain a later implementation, not to start a second coding task.

### Part 5. Turn three criteria into tests

In lecture we covered turning each condition into one pytest test, and putting policy values in a named setting rather than inventing them.

In `tests/test_student_acceptance.py`, write **exactly three pytest test functions**, one for each of `AC-1`, `AC-2`, and `AC-3`.

1. Take each expected result from the acceptance criterion, not from reading the reference code.
2. Use only `reservation_disposition` and `can_offer_to_waitlist` from `reference`, called with named arguments as shown in `README.md`.
3. Put any policy value, such as the grace period, in a named constant marked as a configured value.
4. Do not edit `reference/` or `tests/test_reference_smoke.py`.
5. Make the AC ID visible in the test name or an adjacent comment.
6. In your report, give the chain for each test: test name, AC ID, requirement ID, evidence ID.
7. Run `python -m pytest -q` and include the final output in the PDF.

A test that only runs code without asserting the acceptance criterion does not count.

If a test fails, do not change its expected value to match the code. As in lecture, decide which one is wrong: check whether your criterion settled something the interview leaves open, such as exactly when a staff hold ends. If it did, revise the criterion, then the test, and record the change in your ledger.

### Part 6. Run one AI ambiguity audit and critique the synthetic user

In lecture we covered using AI to find ambiguous words and contradictions, judging every finding as a true or false positive, and why a synthetic user cannot stand in for a real one.

Run **one** AI audit over `transcripts/interview.txt` using the exact text in `prompts/ambiguity_audit_prompt.txt`. Paste or attach the transcript, whichever your tool needs.

1. Save the complete model response, unchanged, in `results/ambiguity_audit.md`.
2. Classify every finding as `true positive` (a real problem in the transcript) or `false positive` (a finding the transcript does not support).
3. For every classification, cite the paragraph or paragraphs and give one sentence explaining the decision.
4. Do not reward the model for sounding plausible. A finding the transcript does not support is a false positive.
5. Then read `synthetic/synthetic_user_output.md` and list **every distinct product or user claim in it that INT-01 does not establish**. Quote the synthetic claim and explain why the real transcript does not support it.

The synthetic response is a source of hypotheses, not another interview. Do not generate more personas.

### Part 7. Complete traceability and the provenance ledger

In lecture we covered the chain from quote to code, and the seven-field provenance ledger.

Complete `traceability/template.csv` with one row per test, filling in its four columns: evidence ID, requirement ID, acceptance criterion ID, and test name. If a test traces to more than one evidence ID, put them in the one cell separated by semicolons, for example `E-1;E-3`.

Fill in `LEDGER.md` as you work. At minimum, record the Part 6 AI audit and any other AI-assisted change or analysis you keep in the submission. Every prompt the ledger references must exist under `prompts/`.

## Deliverables

1. One PDF report containing Parts 1 through 7, the final `python -m pytest -q` output, and the submitted commit SHA.
2. Your private repository made from this starter, containing the completed artifacts, exactly three student acceptance tests, the raw Part 6 model response, all prompts the ledger references, the completed traceability matrix, and `LEDGER.md`.

## Turn-in instructions

Submit exactly these two items on Canvas:

1. One PDF report with your name, the submitted commit SHA, Parts 1 through 7, and the final pytest output.
2. A link to your public repository.

A repository link the instructor cannot open counts as a missing repository submission.

## AI policy

AI tools are permitted and expected on this assignment. You must submit a provenance ledger recording which tools you used, a summary of what you asked them, and what you did to review the output. Submitting AI-generated work you have not reviewed misrepresents authorship and is an academic-integrity violation under the course syllabus, as is fabricating ledger entries. You are responsible for every line you submit, including lines you did not type. You may be asked in class to explain any part of your submission.

Part 6 requires one AI audit. AI tools may also help you draft or review other parts, but AI output never becomes interview evidence because you kept it. Every evidence claim must trace to INT-01, and any AI help you keep must be recorded in the ledger.

## Provenance ledger requirements

Every submission includes `LEDGER.md` at the repository root, using exactly this format, the one from lecture:

```text
## Entry <n>
artifact:  what this entry covers: a file, a commit SHA, a document, or an experiment
tool:      product name, model name, model version, and the date of use
prompts:   one-line summary each; the verbatim prompts live in prompts/ and are
           referenced here by file path
review:    what you read, what you changed, what you rejected, and why
checks:    the commands you ran and their results
evidence:  the requirement, test, or evidence ID this traces to
risk:      what remains unverified after this change

For an experiment, add three fields:
dataset:   task set identifier and its commit SHA or version
result:    metric, N, and the result table or its file path
changed:   what you did differently as a result
```

Write each entry when the work is done, not at submission time. Write one entry per reviewable change, not one per work session.

## Grading

The assignment is graded out of 100 points, item by item, as listed in `RUBRIC.md`. Points reward evidence discipline, explicit uncertainty, precise specification, traceable tests, and careful review of AI output. Extra features, extra tests, extra AI calls, and extra polish earn no additional points.
