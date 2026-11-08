# Token Saver — Advanced Claude Efficiency Skill

A general-purpose, modular Claude Skill for completing work with less avoidable context, tool overhead, repeated work, and usage consumption—without sacrificing correctness.

It is designed to remain useful on Claude Free. It does not require Claude Code, paid models, subagents, hooks, external MCP services, or scripts.

## Operating model

The Skill uses a lightweight core protocol and optional playbooks:

1. **Triage:** classify the task and choose the lightest reliable execution path.
2. **Retrieve:** reuse existing context, search selectively, and read only what is needed.
3. **Execute:** batch related requirements, minimize unnecessary tool calls, and make targeted changes.
4. **Verify:** use risk-based validation; never claim checks that were not performed.
5. **Preserve context:** keep one source of truth and compact checkpoints for long work.
6. **Deliver:** return the requested outcome, evidence, limitations, and next action—without raw-output dumps.

## Package structure

- `SKILL.md` — core operating protocol and reference-selection rules.
- `references/task-routing.md` — task classification, intake, tool gating, research, and troubleshooting.
- `references/free-plan-playbook.md` — Claude Free usage constraints, Projects, tools, and practical habits.
- `references/context-management.md` — project knowledge, long conversations, checkpoints, and fresh-chat handoffs.
- `references/large-task-playbook.md` — repository, multi-file, and phased execution.
- `references/verification-matrix.md` — risk-based validation and evidence integrity.

References are loaded only when relevant. Do not ask Claude to read every file at the start of a task.

## Claude Free design constraints

- No assumption of Claude Code, Research, Cowork, paid-only models, subagents, or hooks.
- No scripts or external dependencies.
- No claim that a Skill can increase quotas or context limits.
- Uses selective retrieval, concise persistent instructions, curated project knowledge, batched related requests, and proportionate tool usage.
- Protects exact code, evidence, data, and source material from lossy compression.

Claude's plan features and usage policies change. The Free Plan Playbook links to official guidance and explicitly treats plan limits as variable.

## Install in Claude

1. Download this `token-saver` folder from the repository.
2. Create a ZIP with `token-saver/` as the ZIP's top-level directory.
3. In Claude, open **Customize → Skills**.
4. Select **+ Create skill → Upload a skill**.
5. Upload the ZIP and enable the Skill. Skills require code execution to be enabled in Claude.

Do not ZIP the repository root when installing this Skill.

## How to use it

Claude may invoke the Skill when it identifies a matching multi-step or context-heavy task. Automatic selection is not guaranteed.

You can invoke it explicitly:

- `Use Token Saver for this task. First inspect the relevant project state, then execute and verify the requested change.`
- `Apply Token Saver. Keep the working set small, batch related checks, and preserve exact technical evidence.`
- `Use Token Saver for this research. Search only decisive questions, prefer authoritative current sources, and cite the conclusions.`
- `Use Token Saver to continue from this checkpoint. Verify the actual files before assuming prior work still exists.`

For simple one-line questions, the Skill should not add process overhead. For complex tasks, it should reduce repeated clarification, broad reads, unnecessary searches, and unverified retries.

## Official Anthropic references

- [What are Skills?](https://support.claude.com/en/articles/12512176-what-are-skills)
- [Usage limit best practices](https://support.claude.com/en/articles/9797557-usage-limit-best-practices)
- [How usage and length limits work](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work)
- [What are Projects?](https://support.claude.com/en/articles/9517075-what-are-projects)
