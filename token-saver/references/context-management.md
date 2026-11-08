# Context Lifecycle and Continuity

Load this reference for long conversations, large projects, repeated document work, or handoffs between chats.

## 1. Treat context as a working set

The goal is not to keep everything in the conversation. The goal is to keep the information needed for the next correct action.

Keep these separate:
- **Stable context:** durable project facts, architecture, conventions, source-of-truth locations.
- **Task context:** the current deliverable, immediate inputs, constraints, and acceptance checks.
- **Transient context:** raw logs, search results, temporary errors, discarded alternatives, and old narration.

Stable context belongs in a concise project instruction or maintained reference. Task context belongs in the current request. Transient context should not be copied forward unless it changes a decision.

## 2. Establish one source of truth

Before creating a tracker, state file, or index, look for an existing equivalent.

For a project that needs continuity, prefer:
- One compact project index or manifest.
- One current state / handoff record.
- The existing source files and reports.

Do not create parallel trackers that disagree. Do not duplicate the content of source documents into the state file.

## 3. Keep project instructions lean

Project instructions should contain only long-lived rules:
- What the project is.
- Which source is authoritative.
- Critical constraints and prohibited operations.
- Naming, formatting, and output conventions.
- Where current state is recorded.

Move detailed procedures into separate references. Do not put a full task plan into persistent project instructions; it becomes stale and consumes context on unrelated tasks.

## 4. Use selective project knowledge

- Store only material likely to be reused.
- Prefer a concise index plus focused files over a large undifferentiated upload.
- Avoid duplicate versions of the same document.
- Separate authoritative source files from summaries, generated reports, and experimental material.
- Update the index when paths or source-of-truth decisions change.
- Do not assume every uploaded file will be relevant to every question.
- Do not assume RAG, unlimited storage, or identical project behavior across plans.

## 5. Checkpoint at meaningful boundaries

Create or update a checkpoint only when it will prevent repeated work across a phase, session, or context reset.

Use this compact schema:

```markdown
# Work State

- Objective:
- Active workspace / source of truth:
- Constraints and decisions:
- Relevant files:
- Verified results:
- Changes made:
- Unresolved issues:
- Exact next action:
```

Keep facts exact. Link to artifacts rather than copying them. Do not include passwords, API keys, private tokens, or other secrets.

A useful checkpoint is a compact operational handoff, not a conversation summary.

## 6. Start a new chat when it is cheaper and safer

Start a fresh chat when:
- The active deliverable changes substantially.
- The current conversation contains a large amount of irrelevant history.
- The context is near its limit or prior context has become unreliable.
- A completed phase has a verified checkpoint and the next phase has different inputs.

Continue the current chat when:
- The same files and decisions remain active.
- The immediate next step depends on detailed recent context.
- A fresh chat would require re-uploading or re-establishing more information than it saves.

Do not restart reflexively. Compare the cost of carrying relevant context with the cost of rebuilding it.

## 7. Handoff protocol

A new-chat handoff should include, in this order:

1. Current objective and requested next deliverable.
2. Active workspace and source-of-truth paths.
3. Non-negotiable constraints and decisions.
4. What is complete, with verification evidence.
5. What remains unresolved.
6. The exact next action and stopping condition.

Do not paste full logs, entire documents, or old assistant/user messages unless an exact excerpt is essential.

After receiving a handoff, inspect the actual files and state before claiming the prior work still exists. A handoff is a map, not proof of filesystem state.
