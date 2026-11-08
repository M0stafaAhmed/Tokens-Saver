# Claude Free — Efficiency Playbook

This reference is specific to Claude's Free plan. Product limits and interface labels change; verify current behavior in Claude rather than hard-coding assumptions.

## 1. Understand what can and cannot be optimized

There are two separate constraints:

- **Usage allowance:** how much Claude interaction is available over the plan's time window.
- **Context / length allowance:** how much information can fit and remain useful in one conversation.

Conversation length and complexity, attachment size, tool usage, model choice, effort, artifact creation, and multi-step work can affect usage. A Skill cannot raise the quota, enlarge a fixed context window, unlock paid features, or bypass a reset.

The target is fewer avoidable interactions and less irrelevant context for the same verified result—not artificially short answers.

Official references:
- https://support.claude.com/en/articles/9797557-usage-limit-best-practices
- https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work

## 2. Prepare a high-value first message

For non-trivial requests, give Claude the key requirements together:
- The exact outcome.
- Relevant source material or where to find it.
- Constraints and exclusions.
- Required output format.
- Definition of done and stop condition.

Batch related questions that share the same context. Do not bundle unrelated work if doing so creates ambiguity or makes verification difficult.

Avoid sending an incomplete prompt followed by multiple messages that provide obvious missing requirements.

## 3. Keep model and effort proportional

- Use the least expensive / least intensive option actually available that can complete the task reliably.
- For routine or reversible work, use normal or lower effort when the interface exposes that control.
- Reserve extended or higher-effort reasoning for difficult debugging, consequential decisions, complex trade-offs, and work where careful reasoning materially improves correctness.
- Do not assume a particular model, effort selector, or paid-only feature is available on Free.
- Do not sacrifice essential validation to save usage. A preventable failed attempt often costs more than one focused check.

## 4. Treat tools as a budget

- Do not use web search when the answer is already in the supplied material or is stable and known.
- Use web search for current facts, niche details, changing product behavior, external recommendations, and claims that require sources.
- Disable or avoid connected apps and tools that are irrelevant to the current task when the interface permits.
- Do not ask Claude to search the web and then separately ask it to research the same question again.
- Avoid unnecessary Artifacts, code execution, file generation, or elaborate tool workflows when a direct response is enough.
- Use one focused search, then follow up only to close a real evidence gap.
- Do not assume Research, Claude Code, Cowork, subagents, hooks, or other paid capabilities exist in a Free session.

## 5. Use Projects deliberately

Claude's current documentation states that Projects are available on Free, with a limit of five projects. Project knowledge can be reused across chats and benefits from caching, but enhanced Project knowledge with RAG is documented as a paid-plan feature.

Practical implications:
- Reserve Projects for recurring bodies of work, not one-off questions.
- Keep project instructions short: stable role, source-of-truth locations, core constraints, and output conventions.
- Put task-specific steps in the current message.
- Upload a curated set of high-value reference files rather than an entire repository or archive.
- Keep a compact index or manifest that points to the detailed files.
- Remove stale, duplicate, or irrelevant project knowledge.
- Do not assume Free has RAG or unlimited project knowledge. Search and inspect the relevant files directly when needed.
- Reuse the same stable project materials rather than repeatedly attaching duplicate copies. Caching behavior and limits can change.

Project documentation:
https://support.claude.com/en/articles/9517075-what-are-projects

## 6. Handle long conversations before they become expensive

- Keep one chat focused on one deliverable or a coherent workstream.
- Avoid mixing unrelated questions into a project execution chat.
- Reuse prior facts by referring to them instead of pasting them again.
- Track decisions and verified state outside the conversation when work spans sessions.
- When the chat becomes large or the task changes substantially, create a compact handoff and open a fresh chat if that reduces irrelevant history.
- Do not restart a chat merely because it is long if important working context is still actively needed.
- Do not assume automatic context management eliminates usage costs.

A handoff should preserve the objective, constraints, decisions, exact file paths, verified results, unresolved issues, and next action. It should not reproduce the transcript.

## 7. Practical operating checklist

Before sending a large request:
- [ ] Have I stated the deliverable and completion criteria?
- [ ] Have I included the essential context once?
- [ ] Have I removed unrelated attachments and instructions?
- [ ] Can related requirements be handled together safely?
- [ ] Is every requested tool necessary?

During execution:
- [ ] Am I reusing valid results?
- [ ] Am I searching and reading selectively?
- [ ] Can I narrow this tool's output?
- [ ] Am I doing the next necessary step rather than planning indefinitely?

Before stopping:
- [ ] Is the requested result complete?
- [ ] Did I perform proportionate validation?
- [ ] Did I preserve important evidence and caveats?
- [ ] Is the next action clear?

## Important boundary

Efficiency practices can help stretch a Free allowance; they cannot guarantee a fixed number of messages, a percentage saving, or uninterrupted access. Check current Claude documentation and the account's own interface for current availability and limits.
