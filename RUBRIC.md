# CS 690 Assignment 3 Rubric

100 points. Each item is checked on its own. Points per item are in brackets.

## Part 1. Evidence log (10)

- [2] 8 to 10 entries, and every ID starts with E-, A-, or Q-.
- [2] Every entry has a source, and transcript sources use the form `INT-01:Pxx`.
- [3] Every E entry is supported by the paragraph it cites.
- [1] No entry cites SYN-01 as evidence.
- [2] The conflicting fact in the interview is logged as uncertainty (an A or Q entry), not as a settled E fact.

## Part 2. Evidence audit (14)

- [7] Each of the seven rows gives the correct paragraph or paragraphs and a correct classification (1 point per row).
- [5] Every row explains in at most two sentences why the item matters to requirements quality.
- [2] The contradiction row does not decide which speaker is right.

## Part 3. Requirements, INVEST, and acceptance criteria (20)

- [1] Exactly four requirement slices, R-1 to R-4.
- [4] Each user story is in Connextra form with a role, a capability, and a benefit (1 per story).
- [4] Each structured requirement states a behavior someone can observe (1 per requirement).
- [2] Each slice traces to evidence IDs, or is labeled `Assumption` with a clarifying question.
- [2] No requirement hard-codes a disputed interview value as settled policy.
- [2] All six INVEST checks are marked pass or fail for all four slices.
- [1] Every INVEST failure names the specific problem.
- [1] Exactly three acceptance criteria, AC-1 to AC-3, on three different requirements.
- [2] Each criterion has concrete starting conditions in Given, one event in When, and an observable result in Then.
- [1] No criterion settles an open product-policy question.

## Part 4. Implementation-ready specification (16)

- [2] A typed Python signature with every parameter and the return value typed.
- [2] Preconditions are explicit and checkable.
- [3] Postconditions are explicit and checkable.
- [1] One invariant, or `Not applicable` with a one-sentence reason that holds.
- [2] At least two edge cases that matter for this behavior.
- [1] Exactly one non-goal.
- [2] Settled decisions are supported by evidence from Part 1.
- [2] Open questions include every unsettled policy the requirement depends on, and tell the agent not to guess.
- [1] No implementation code.

## Part 5. Tests (14)

- [1] Exactly three test functions in `tests/test_student_acceptance.py`.
- [1] Each test shows its AC ID in its name or an adjacent comment.
- [3] Each test's inputs match its criterion's Given and When (1 per test).
- [3] Each test asserts its criterion's Then (1 per test).
- [2] Tests use only the public reference functions, and `reference/` and `tests/test_reference_smoke.py` are unchanged.
- [1] Policy values such as the grace period are in a named constant marked as a configured value.
- [2] `python -m pytest -q` passes in the submitted repository, and its output is in the PDF.
- [1] The report gives the chain for each test: test name, AC ID, requirement ID, evidence ID.

## Part 6. AI audit and synthetic-user critique (14)

- [2] The complete, unedited model response is in `results/ambiguity_audit.md`, produced with the provided prompt or a saved copy of the prompt actually used.
- [2] Every finding is classified as a true positive or a false positive.
- [2] Every classification cites paragraph IDs and gives one sentence of reasoning.
- [3] The classifications are correct against the transcript.
- [4] The synthetic-user critique lists every distinct claim INT-01 does not establish (1 point off per missed claim, down to 0).
- [1] The critique does not list a claim the transcript actually supports.

## Part 7. Traceability and ledger (8)

- [3] The traceability matrix has one row per test, with all four columns filled with IDs that appear in the report.
- [2] `LEDGER.md` uses the seven-field course format.
- [1] The ledger has an entry for the Part 6 AI audit.
- [1] Every prompt the ledger references exists under `prompts/`.
- [1] Entries are one per reviewable change, with specific review and risk fields.

## Submission (4)

- [2] The PDF includes your name, the commit SHA, and the final pytest output.
- [2] The repository link opens for the instructor and is at the commit SHA in the PDF.
