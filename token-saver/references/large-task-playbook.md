# Large Task Execution Playbook

Load this reference for multi-file, repository, coding, research, or phased work that cannot be completed reliably in one simple pass.

## 1. Establish the execution boundary

Write a compact internal task contract:

- Deliverable.
- Inputs and authoritative sources.
- Permitted operations.
- Prohibited operations.
- Acceptance checks.
- Stop condition.

Respect explicit sequencing and approval gates. If the user says one task at a time, finish the current task and stop. Do not treat a related improvement as implicit authorization.

## 2. Inspect before planning in detail

Start with the cheapest useful view:
- Repository root or directory listing.
- README, manifest, project state, or index.
- Relevant configuration and entry points.
- Existing tests and validation scripts.

Then search for the actual symbols, filenames, headings, or data fields related to the request.

Do not read every file just because it exists. Build the working set from observed relevance. Read unknown or related files only when dependencies or scope require them.

## 3. Make a dependency-aware plan

Keep the plan to meaningful deliverables. For each one, identify:
- Required inputs.
- The smallest necessary operation.
- Dependencies on earlier steps.
- Verification method.
- Whether it is reversible.
- Stop condition.

Batch independent read-only inspections. Sequence writes, dependent calls, builds, and tests. Never parallelize writes to the same file or branch.

## 4. Execute incrementally

- Preserve the original input or a recoverable checkpoint before bulk or destructive changes.
- Prefer a small targeted edit.
- Avoid unrelated refactoring or cleanup.
- Do not add dependencies or helper scripts unless they are necessary for the requested outcome.
- Keep generated artifacts separate from source inputs when practical.
- Capture useful outputs at source using filters, selected fields, line ranges, or summaries.
- Stop and reassess when actual files contradict assumptions.

Do not silently skip a failing step. Report the failure, its effect on the deliverable, and the next least-risk action.

## 5. Use one reliable verification pass

Choose checks that can catch the likely failure:
- Inspect the diff for unintended scope.
- Run targeted tests or validators.
- Verify output files, commit refs, or destination paths.
- Compare source and output counts, hashes, or stable identifiers where appropriate.
- Check representative transformed records and edge cases.

Do not rerun a successful check unchanged. Repeat only after a relevant change, a flaky result, or evidence that the earlier check was insufficient.

## 6. Maintain a checkpoint only when needed

Use an existing state file if available. Otherwise create a compact checkpoint at phase boundaries or before a likely context reset.

Record verified state, not intentions. Include exact paths and identifiers. Keep the checkpoint smaller than the material it replaces.

See [Context Lifecycle](context-management.md).

## 7. Completion report

Report:
1. Deliverable status.
2. Files or resources created, modified, or removed.
3. Validation actually performed.
4. Material blockers or limitations.
5. Exact next action, if any.

Do not reproduce full logs or narrate every tool call.

## 8. Anti-patterns

Stop doing these:
- Repeatedly listing the same directory.
- Reading large files in full to find one symbol.
- Repeating the same search with slightly different wording but no new hypothesis.
- Rewriting whole files for small edits.
- Running a full suite when a targeted check is sufficient, unless the change's risk demands it.
- Creating more process documents than the project needs.
- Producing a lengthy plan instead of doing the first safe step.
- Continuing after the agreed stop point.
- Compressing evidence and then spending more work recovering it.
