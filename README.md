# cs690-a3-intent-spec

Starter repository for Assignment 3, Evidence to Executable Specification. `HANDOUT.md` says what to do, and `RUBRIC.md` says how it is graded. This file covers setup and commands.

## Requirements

- Python 3.11 or later.
- pytest 9.1.1, pinned in `requirements.txt`.
- Git and a GitHub account.
- Any AI chat assistant you may use under the course policy, for Part 6. No API key is needed.

## Make your own private copy

Create a new, empty, private repository on GitHub. Then copy this starter into it:

```bash
git clone <starter repository URL from Canvas> cs690-a3-intent-spec
cd cs690-a3-intent-spec
git remote set-url origin <your private repository URL>
git push -u origin HEAD:main
```

On GitHub, open your repository's Settings, then Collaborators, and add the instructor's GitHub account named on Canvas. A repository the instructor cannot open counts as missing.

## Setup

Create and activate a virtual environment, then install the pinned dependency:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

On Windows PowerShell, activate with `.venv\Scripts\Activate.ps1` instead. On macOS or Linux, if `python` is not found, use `python3` for the first command; inside the activated environment, `python` works.

## Verification command

Use this single command throughout the assignment:

```bash
python -m pytest -q
```

The starter begins with one smoke test. Your final repository must add exactly three student-written acceptance tests to `tests/test_student_acceptance.py`, and all tests must pass.

## Calling the reference module

The module exports two functions. Both take named arguments only, and return plain values:

```python
from reference import can_offer_to_waitlist, reservation_disposition

state = reservation_disposition(minutes_after_start=5, grace_minutes=10, checked_in=False)
assert state == "held"   # one of "active", "held", "releasable"

ready = can_offer_to_waitlist(disposition="releasable", preparation_complete=False)
assert ready is False
```

The return type is `Disposition = Literal["active", "held", "releasable"]`, the Literal type from the Week 6 lecture. Times are whole minutes after the reservation start.

## Submitting

Commit and push your final work, then print the commit SHA to put in your PDF:

```bash
git rev-parse HEAD
```

The repository on GitHub must be at this commit when you submit.

## Repository map

- `HANDOUT.md` and `RUBRIC.md`: the assignment and its grading.
- `transcripts/interview.txt`: the real-user interview for this assignment, case INT-01.
- `synthetic/synthetic_user_output.md`: a pre-generated synthetic-user response to critique, SYN-01.
- `evidence/schema.md`: the E, A, and Q evidence-log scheme plus an unrelated worked example.
- `spec/spec_template.md`: the implementation-ready specification template.
- `traceability/template.csv`: the traceability matrix shell.
- `reference/`: small reference behavior used only as the executable target for your acceptance tests.
- `tests/test_student_acceptance.py`: your three-test file.
- `prompts/ambiguity_audit_prompt.txt`: the required Part 6 audit prompt.
- `results/ambiguity_audit.md`: store the complete model response here.
- `report/REPORT_TEMPLATE.md`: optional structure for the PDF report.
- `LEDGER.md`: the required provenance ledger.

Do not edit files under `reference/` or `tests/test_reference_smoke.py`. Your job is to derive requirements and tests from evidence, not to reverse-engineer or modify the reference implementation.
