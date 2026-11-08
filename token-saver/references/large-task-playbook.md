# Large Task Playbook

Use this reference only when the task has a large working set, several phases, substantial tool use, or a meaningful risk of context loss.

## 1. Establish the working set

Before reading content, identify:

- The requested deliverable and explicit exclusions.
- The active repository, folder, or source of truth.
- Existing inventories, status files, reports, tests, and prior decisions.
- The smallest set of files or sources likely to determine the next action.

Do not inventory the same workspace repeatedly unless it may have changed.

## 2. Retrieve in layers

Use this order where it fits the environment:

1. List relevant directories or search filenames.
2. Search for exact terms, symbols, headings, or references.
3. Read the smallest useful excerpts around the matches.
4. Expand to full files only when relationships, omitted context, or correctness require it.
5. After a change, inspect the diff or changed range first.

When reviewing many files, classify them before opening them all: required, related, unrelated, generated, or unknown. Read required and related files first.

## 3. Control tool calls

- Combine independent read-only checks into one batch when the tool supports it.
- Keep read-after-write verification and other dependent operations sequential.
- Ask tools to return only fields needed for the decision.
- Limit search results and command output; narrow the query rather than repeatedly processing oversized results.
- Avoid repeated broad searches. Refine a query using what the first result established.
- Do not use a script for a one-off task when a direct, bounded operation is simpler.
- Review a script before running it, especially if it can modify or delete files.

Example shell patterns, only when shell access exists and is appropriate:

```bash
# Find relevant files instead of printing the entire tree.
find src -type f | sort | head -80

# Locate a symbol and then inspect only its surrounding code.
rg -n "TargetSymbol" src
sed -n '120,190p' src/path/to/file.py

# Review the size and substance of changes without dumping every file.
git diff --stat
git diff -- path/to/changed-file
```

Adapt commands to the actual environment. Do not assume these utilities are installed.

## 4. Choose validation by risk

| Change or task | Efficient validation |
|---|---|
| Small text edit | Inspect the changed section and surrounding context |
| Multi-file documentation change | Review changed files, links, and relevant metadata |
| Code change | Focused tests, relevant static checks, and diff review |
| Data transformation | Compare input/output counts, schema, and representative records |
| Repository-wide operation | Dry run or preview, bounded summary, then targeted verification |
| Destructive operation | Confirm scope, preserve recovery point, execute, verify affected targets |

A passing check proves only what that check actually covers. State skipped checks and tool limitations.

## 5. Maintain one compact checkpoint

Use an existing project state file or task log when available. Otherwise create a checkpoint only when another session, phase, or context reset is likely.

Suggested structure:

```markdown
# Task State

- Objective:
- Active workspace:
- Relevant inputs:
- Constraints and decisions:
- Verified results:
- Files changed:
- Unresolved issues:
- Exact next action:
```

Keep the checkpoint factual and compact. Link to reports or artifacts instead of copying their contents. Never store credentials or secrets in a checkpoint.

## 6. Avoid common sources of waste

- Reading every file before defining the deliverable.
- Repeating directory listings and searches that have not become stale.
- Printing complete logs, datasets, API responses, or diffs when a focused excerpt is sufficient.
- Rewriting entire documents to change a small passage.
- Creating a new plan, tracker, script, or report that duplicates an existing one.
- Reconstructing previous work from conversation history when a verified project state already records it.
- Compressing exact technical evidence and later having to recover or revalidate it.

## 7. Completion report

For substantial work, report only:

1. What was completed.
2. Which files or outputs changed.
3. What was actually verified.
4. Material limitations or unresolved issues.
5. The exact next action, if the task is not finished.

Do not include raw logs or a play-by-play of routine tool calls.
