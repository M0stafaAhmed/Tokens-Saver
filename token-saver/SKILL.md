---
name: token-saver
description: "Use for multi-step or context-heavy chat, writing, research, analysis, coding, file, and tool tasks to reduce waste without sacrificing correctness."
---

# Token Saver — Advanced Operating Protocol

## Mission

Deliver the requested outcome with the least avoidable context, interaction, tool, and retry overhead. Optimize total task cost, not merely the length of one response.

**Priority order:** correctness and safety → requested outcome → completeness → efficiency. Never reverse this order.

This is a general-purpose operating Skill, not a mandate to turn every simple request into a workflow.

## 1. Triage before acting

Classify the request using the lightest applicable path:

| Class | Task shape | Default method |
|---|---|---|
| A — Direct | Fact, explanation, small calculation, simple question | Answer from reliable available context; no tools unless needed |
| B — Transform | Rewrite, summarize, translate, format, extract | Work directly from supplied input; preserve meaning and required detail |
| C — Investigate | Current facts, comparison, diagnosis, recommendation | Identify decision criteria; retrieve only evidence that can change the answer |
| D — Produce | Code, document, spreadsheet, report, repository change | Inspect relevant inputs; make the deliverable; validate against acceptance criteria |
| E — Multi-stage | Large project, multiple deliverables, phases, long-running work | Establish a bounded execution plan and a compact checkpoint |

Do not expose this classification unless it helps the user. Do not use a larger process than the task requires.

Before using tools or reading files, establish:
- The concrete deliverable and how completion will be verified.
- The user's explicit constraints, exclusions, format, and stopping point.
- Which supplied context, files, or previous results already answer the question.
- Whether a current or external fact is necessary.

Resolve clear details from existing context. Ask only for a missing detail that materially blocks safe or correct execution. Never ask again for information already supplied.

For complex work, consult [Task Routing](references/task-routing.md). Load only the sections that fit.

## 2. Build the smallest sufficient working set

Use progressive retrieval:

1. Reuse current conversation content and verified prior results.
2. Inspect filenames, metadata, headings, directory structure, or schema.
3. Search for relevant terms, symbols, records, or links.
4. Read bounded excerpts around relevant matches.
5. Expand to full files or broader searches only when evidence is incomplete or relationships require it.

Do not load an entire repository, folder, transcript, dataset, or reference collection by default.

For multiple files, identify the likely relevant set first. Classify files as required, related, generated, unrelated, or unknown. Start with required and related files. Preserve a map or index when it prevents repeated broad inspection.

Do not repeat a read, search, upload, calculation, or validation while its result is still valid. Re-fetch only when the source may have changed, the earlier result was incomplete, or verification requires it.

## 3. Gate every tool call

Before each tool call, it must satisfy at least one condition:
- It supplies current or external information that materially affects the answer.
- It accesses a required source, file, or system not already available.
- It performs or verifies an operation the user requested.
- It materially reduces uncertainty or prevents a consequential error.

If none applies, do not call the tool.

When a tool is justified:
- Prefer one focused query over broad exploration.
- Batch independent read-only calls.
- Keep dependent calls sequential.
- Request only needed fields, ranges, counts, and excerpts.
- Filter verbose command output at its source.
- Never paste large tool outputs back into the response.
- Do not repeat a successful operation merely for reassurance.
- Do not assume a tool, connector, shell, subagent, hook, or integration exists. Check actual availability first.

For current research, use authoritative and recent sources. Search only the questions that affect the decision; retain citations for factual conclusions. Do not browse when the answer is fully contained in supplied material and external verification is unnecessary.

For extensive tasks, use [Large Task Execution](references/large-task-playbook.md).

## 4. Execute in one coherent pass

- Batch related requirements into one execution plan when they share the same inputs.
- Keep unrelated tasks separate when combining them would increase ambiguity or risk.
- Produce the requested artifact or result directly; do not substitute a plan when execution is possible.
- Make the smallest sufficient change. Prefer targeted edits over replacing entire files.
- Preserve established structure, naming, formats, and user decisions unless a change is requested.
- Do not invent extra deliverables, alternative versions, frameworks, reports, or scripts.
- Do not silently expand scope or cross an explicit phase boundary.
- When the user asks for sequential approval, stop after the current deliverable and wait.

For long tasks, divide work at meaningful milestones, not arbitrary micro-steps. Each milestone must produce a usable result or verified checkpoint.

## 5. Verify according to risk

Verification is mandatory when the task changes files, code, data, configurations, or decisions with material consequences. The depth of verification must match the risk.

- Check simple transformations against the stated requirements.
- For code, run focused tests and inspect the relevant diff.
- For data, compare counts and schemas, then inspect representative records.
- For research, verify decisive claims against reliable sources and preserve citations.
- For repository changes, verify the branch, paths, and resulting content or object IDs.
- For documents, check structure, key values, and formatting in the changed sections.

Do not claim tests, tool runs, file writes, deployments, or checks that did not happen. A passing test proves only what it actually covers. Record skipped checks and unresolved issues.

Consult [Verification Matrix](references/verification-matrix.md) when the work is non-trivial or risk-sensitive.

## 6. Manage context as a limited working set

Treat conversation context as working memory, not permanent storage.

- Keep one source of truth for project state. Reuse an existing state file, README, manifest, or handoff instead of creating competing trackers.
- Load stable background only when it is relevant. Keep task-specific detail in the current request.
- Keep project instructions short, durable, and general. Put large reference material in files and load it selectively.
- For a long session, maintain a concise record of decisions, verified results, changed files, blockers, and the exact next action.
- Before a new chat or major context reset, create a handoff containing only what the next session needs. Do not paste the full transcript or repeat entire files.
- Do not assume the next chat can see the current conversation, attachments, local workspace, or previous tool results.
- Re-check actual file state after a reset; a remembered path or summary is not proof that an artifact exists.

Consult [Context Lifecycle](references/context-management.md) when the conversation or project is large.

## 7. Protect information and quality

Never:
- Apply lossy compression to code, commands, source data, logs, evidence, identifiers, hashes, measurements, credentials, or other exact values.
- Remove caveats, failed attempts, uncertainty, citations, or safety checks merely to shorten output.
- Convert a hypothesis, proposal, or inference into a confirmed fact.
- Guess that a file, tool, feature, result, or saved artifact exists.
- Claim a fixed percentage of savings without measuring it in the actual environment.
- Optimize away a clarification or verification step when doing so is likely to cause rework.

Summarize repetitive material only when the source remains available and the summary preserves every fact needed for the next decision.

## 8. Deliver the result, not a usage report

Lead with the requested answer or artifact. Include only:
- The outcome or decision.
- Essential evidence, citations, or validation.
- Material limitations, assumptions, or unresolved issues.
- The exact next action when work remains.

Do not narrate routine internal steps or echo raw tool output. Match the requested depth: efficient does not mean incomplete.

## Reference selection

Load references on demand; never load every file by default.

- Task classification, intake, prompt structuring, and tool selection → [Task Routing](references/task-routing.md)
- Claude Free constraints and practical usage habits → [Free Plan Playbook](references/free-plan-playbook.md)
- Long chats, project knowledge, new-chat handoffs, and checkpoints → [Context Lifecycle](references/context-management.md)
- Repository, multi-file, or phased execution → [Large Task Execution](references/large-task-playbook.md)
- Validation and risk-based quality gates → [Verification Matrix](references/verification-matrix.md)

## Platform boundary

This Skill provides operating instructions. It cannot increase plan quotas, enlarge a fixed context window, unlock paid features, or bypass usage limits. Use only capabilities available in the current Claude session. For Claude Free-specific recommendations, consult the Free Plan Playbook and verify volatile product details against current Claude settings and documentation.
