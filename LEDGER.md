# Provenance ledger

Use exactly this format for every entry. Write each entry when the work is done, one entry per reviewable change.

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

Add your entries below this line, starting with Entry 1.

---
