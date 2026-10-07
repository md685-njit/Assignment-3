# A3 report template

Name:
Commit SHA:

## Part 1. Evidence log

Insert 8 to 10 E, A, and Q entries using the table in `evidence/schema.md`.

## Part 2. Evidence audit

One row for each item: contradiction, ambiguity 1, ambiguity 2, missing stakeholder, compliment, prediction about future use, strongest past event.

| Item | Location | Classification | Why it matters |
| --- | --- | --- | --- |

## Part 3. Requirements, INVEST, and acceptance criteria

### Four requirement slices

For each of R-1 to R-4: user story, structured requirement, and evidence trace, or `Assumption` plus a clarifying question.

### INVEST check

| Requirement | I | N | V | E | S | T | Named problem for any fail |
| --- | --- | --- | --- | --- | --- | --- | --- |

### Three acceptance criteria

AC-1 to AC-3 in Given-When-Then form, each traced to a different requirement.

## Part 4. Implementation-ready specification

Paste your completed `spec/spec_template.md`.

## Part 5. Tests

| Test name | AC ID | Requirement ID | Evidence ID |
| --- | --- | --- | --- |

## Part 6. AI audit and synthetic-user critique

### Audit adjudication

For every finding in `results/ambiguity_audit.md`: true positive or false positive, the paragraph IDs, and one sentence explaining the decision.

### Synthetic-user critique

Every claim in `synthetic/synthetic_user_output.md` that INT-01 does not establish. Quote the claim and explain why the interview does not support it.

## Part 7. Traceability and ledger

Paste the completed matrix from `traceability/template.csv`. The ledger stays in `LEDGER.md` in the repository.

## Verification

Paste the final output of `python -m pytest -q`.
