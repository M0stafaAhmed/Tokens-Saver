# Token Efficiency

## Objective

Reduce unnecessary context consumption and repeated work while preserving correctness, evidence, and useful detail. Token savings are secondary to accurate project output.

## Work from the smallest useful context

1. Search filenames, headings, metadata, and targeted terms before opening documents in full.
2. Read only the sections needed for the current decision. Use line ranges or bounded excerpts when available.
3. For a multi-file task, inspect the inventory and relationship reports before opening every document.
4. Do not reread an unchanged file already inspected in the current conversation unless its contents are genuinely needed again.
5. After a file changes, inspect only the changed region or the specific validation result unless a full review is necessary.
6. Do not echo raw tool output back into the conversation. Report conclusions and point to the relevant file and section.
7. Bound command and tool output at its source. Prefer counts, summaries, selected fields, and error excerpts over unrestricted listings.
8. Run independent read-only inspections together when the environment supports it. Do not parallelize dependent operations or conflicting writes.
9. For repetitive counting or format checks, prefer a deterministic, read-only operation over manually reading every file. Explain what was checked and the limits of the check.
10. Do not install tools or create reusable scripts solely to save a few tokens. Do not use an unreviewed script to modify project files.

## Editing discipline

- Make the smallest possible edit to an existing file.
- Prefer a targeted edit when the available interface supports it.
- Avoid replacing an entire document to change a small section.
- Do not produce duplicate copies of large files in chat.
- Keep original inputs and a recoverable checkpoint before batch transformations.
- Validate modified files without dumping their entire contents into the conversation.

## Conversation and checkpoint discipline

- Keep each task limited to one phase and its stated deliverables.
- Maintain PROJECT_STATE.md as the compact record of current phase, workspace, completed work, pending work, decisions, issues, and exact next task.
- At major phase boundaries, use a fresh chat when the user chooses to do so; provide a compact handoff and the latest verified checkpoint.
- Do not assume that a new chat can see previous chat history or files unless they are explicitly available through project knowledge or attached files.
- Do not assume that a cloud workspace persists across sessions. A workspace path is not a backup.
- Do not regenerate or reread the entire project context when a verified state file and checkpoint provide the necessary information.

## Compression safety

- Never apply lossy compression to source notes, YAML, commands, flags, hashes, IP addresses, credentials, code, or evidence.
- Do not paraphrase exact evidence when exact preservation is required.
- Summarize repetitive diagnostic output only when the original remains preserved and the summary retains the facts needed for the decision.
- Do not claim a fixed percentage of token savings. Measure actual savings in the actual environment when measurement is available.

## Environment limitations

Use only tools that are visibly available in the current Claude Desktop session. Do not assume Claude Code hooks, subagents, shell commands, persistent filesystem access, MCP compression tools, or paid features are available. If an operation depends on an unavailable capability, report the limitation and use the simplest supported alternative.
