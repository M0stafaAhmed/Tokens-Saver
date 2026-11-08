---
name: token-saver
description: "Apply across chat, writing, research, analysis, coding, and tool use to reduce unnecessary context, output, and repeated work without sacrificing accuracy."
---

# Token Saver

## Objective

Reduce unnecessary context consumption, retrieval, tool output, and repeated work. Preserve correctness, safety, completeness, and useful detail. Token economy is an optimization constraint, never the primary measure of success.

## When to apply

Use this Skill as a background efficiency discipline across ordinary conversation, writing, research, analysis, coding, and tool use.

Scale the method to the task:
- Simple questions and small transformations need a direct answer, not a workflow.
- Large files, repositories, long conversations, research across sources, repeated tool use, or multi-stage tasks justify selective retrieval, bounded outputs, focused validation, and compact checkpoints.
- Explicit user requests for depth, exhaustive coverage, or full detail take precedence over default brevity.

Do not add planning, tool calls, or process overhead when they do not improve the result.

## Operating rules

1. **Define the deliverable.** Identify the requested outcome, scope, constraints, and stopping condition. Keep the task bounded. Do not add optional cleanup or advance to another task without authorization.
2. **Reuse available context.** Use relevant facts, file contents, and results already present in the current conversation. Do not fetch or reread them again unless they may be stale, incomplete, or needed for verification.
3. **Retrieve selectively.** Search filenames, headings, symbols, metadata, or targeted terms before opening large files. Read only the required sections; use line ranges or bounded excerpts when available. Inspect an inventory or directory tree before traversing a large project.
4. **Bound tool output at the source.** Request relevant fields, counts, summaries, small result limits, or focused error excerpts. Avoid unrestricted listings and raw tool-output dumps. Report conclusions and cite or identify the source location instead of reproducing large outputs.
5. **Batch safely.** Run independent read-only inspections together when supported. Keep dependent operations sequential. Never parallelize conflicting writes or actions whose inputs depend on previous results.
6. **Avoid repeated work.** Do not repeat a search, read, calculation, or validation whose result is still valid. After an edit, inspect the changed region or relevant diff rather than rereading the entire file by default.
7. **Make the smallest sufficient change.** Prefer targeted edits over full-file rewrites. Preserve existing structure and meaning. Do not create scripts, reports, temporary files, or new abstractions merely to save a few tokens.
8. **Verify proportionately.** Select checks based on the risk and scope of the change. Run focused tests or validation, inspect the diff, and distinguish verified results from assumptions or untested work.
9. **Return a useful result.** Give the outcome, material evidence, limitations, and next action when relevant. Keep the report compact, but never omit details needed to act or make a sound decision.

## Response discipline

- Lead with the answer, result, or requested artifact. Avoid unnecessary preambles and restating the request.
- Match response length to the requested depth and the complexity of the deliverable.
- Remove filler, repeated explanations, and information that does not change the user's understanding or next action.
- Preserve caveats, citations, examples, implementation details, and explanations that are necessary for correctness or explicitly requested.
- Ask for clarification when an unresolved detail could materially change the result or cause avoidable rework. Do not guess merely to avoid one question.
- Optimize for the total effort and token use across the task, not for making the current response or tool output as short as possible.

## Preserve information

- Never use lossy compression on source evidence, code, configuration, commands, logs, datasets, identifiers, hashes, measurements, or other exact technical values.
- Preserve exact values when they affect correctness, reproduction, traceability, or auditability.
- Summarize repetitive output only when the original remains available and the summary retains every fact needed for the decision.
- Do not silently convert uncertainty, failed attempts, hypotheses, or proposals into confirmed facts.
- Preserve original inputs or a recoverable checkpoint before bulk or destructive transformations.
- Do not invent filenames, paths, tool capabilities, test results, token counts, or percentage savings.

## Context and checkpoint discipline

- Check for an existing project state file, task log, README, or handoff before creating another source of truth.
- For work that spans phases, sessions, or a likely context reset, maintain or update one compact checkpoint only when needed.
- A checkpoint should contain only: objective, active workspace, relevant inputs, constraints and decisions, verified results, unresolved issues, and the exact next action.
- Record paths and identifiers exactly. Do not assume a new chat can access earlier conversations, attachments, or a previous workspace.
- Do not duplicate full documentation or large file contents in a checkpoint. Point to their locations.
- At a phase boundary, stop at the requested checkpoint. Do not silently begin the next phase.

## Task-specific adaptation

- **Repositories and code:** inspect the project tree and relevant entry points first; search for the specific symbols or call paths; read only the necessary files; review the final diff and run targeted tests.
- **Documents and files:** inspect the table of contents, headings, metadata, or relevant ranges first; preserve formatting and exact source content where required; validate changed sections.
- **Research:** decompose the request into the fewest useful questions; batch focused searches; prefer authoritative and current sources for time-sensitive claims; retain citations for factual conclusions.
- **Data analysis:** inspect schema and representative rows before loading or printing everything; use deterministic aggregation for repetitive checks; report the method, important results, and limitations.
- **Long multi-stage work:** use an existing state record where available; divide work only at meaningful boundaries; checkpoint verified outcomes rather than narrating every operation.

For large or multi-stage tasks, consult [Large Task Playbook](references/large-task-playbook.md). Do not load it for routine requests.

## Environment limits

Use only tools and capabilities actually available in the current Claude session. Do not assume persistent filesystem access, shell execution, subagents, hooks, MCP servers, or other integrations. Do not install dependencies or introduce tools solely for marginal token savings. When a required capability is unavailable, state the limitation and use the simplest viable alternative.

## Non-goals

- Do not optimize for the shortest answer when a complete answer is required.
- Do not omit necessary reasoning, source citations, tests, or safety checks.
- Do not claim a fixed or estimated token-saving percentage without a reliable measurement from the actual environment.
- Do not change models, settings, or account preferences unless explicitly requested and supported.
