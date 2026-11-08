---
name: oscp-project-operator
description: "Use when working on the OSCP-Exam-PoC vault or website: inspect, document, validate, transform, or build project content."
---

# OSCP Project Operator

Apply this Skill only to the OSCP-Exam-PoC Obsidian vault, its documentation, or its website. Do not apply it to unrelated tasks.

## Operating rules

1. Read the current PROJECT_STATE.md before starting a multi-step task. Confirm the workspace and current phase from the latest state; never assume a path from an earlier chat.
2. Follow only the phase or task explicitly requested. Do not advance to another phase, expand scope, or perform unrelated cleanup.
3. Treat the original archive and source-vault/ as immutable. Make changes only in the designated working copy. Never overwrite the only backup.
4. Inspect actual files and current reports before making claims. Do not invent filenames, folders, frontmatter, commands, outputs, flags, dates, results, or completed work.
5. Preserve examination evidence and distinguish confirmed results, failed attempts, hypotheses, proposed techniques, and unverified material.
6. Make the smallest necessary change. Preserve existing filenames, folder structure, document meaning, and useful detail unless the user explicitly authorizes a change.
7. Do not create additional scripts, install dependencies, introduce tools, or automate file modifications merely because they might be useful. The bundled scripts are optional, read-only inspection utilities; use them only when the current environment can access them and the task warrants them.
8. Do not run bundled scripts blindly. Read the relevant script first, use synthetic fixtures when validating behavior, and report limitations. Never use them to modify source notes.
9. When a material ambiguity cannot be resolved from the files, report it rather than guessing. Ask one concise question only when the task cannot safely proceed.
10. Report completion only after verifying the actual output. State blockers and limitations plainly.
11. The user chooses Claude model and effort separately from task prompts. Do not embed model-selection advice or effort settings in project execution instructions, and do not attempt to change account settings.

## Load references selectively

Do not load every reference file by default. Read only the reference required by the current task:

- Editing or rewriting vault documents: references/Documentation-Voice.md
- Handling flags, commands, outputs, credentials, or examination claims: references/Evidence-Integrity.md
- YAML, frontmatter, tags, wikilinks, or Obsidian links: references/Obsidian-YAML-Standards.md
- Website architecture, content ingestion, visual design, or deployment: references/Project-Architecture.md
- Multi-file work, large outputs, repeated reads, or context pressure: references/Token-Efficiency.md

If a task spans multiple areas, load only the relevant references. Do not summarize or paste entire reference files into the conversation.

## Optional read-only scripts

The scripts/ directory contains three inspection utilities:

- inventory.py: filesystem inventory and optional JSON/CSV reports.
- validate_yaml.py: YAML frontmatter validation; requires PyYAML already to be installed.
- audit_links.py: read-only Obsidian wikilink and Markdown-link audit.

They do not edit source notes or repair metadata/links. They may write report files only when explicit output paths are supplied. Do not install dependencies if a script cannot run. A script result is an aid to inspection, not a substitute for understanding its limitations or reviewing important findings.

## Phase discipline

Before acting, identify:
- The exact requested phase/task.
- Its input files.
- Its permitted operations.
- Its prohibited operations.
- Its required deliverables.
- Its stopping condition.

If the phase is not explicit, use the latest PROJECT_STATE.md and ask for clarification rather than assuming authorization.

## Completion report

Keep the final report concise. Include:
1. Status.
2. Files created or modified.
3. Validation actually performed and its result.
4. Warnings or unresolved issues.
5. Checkpoint location, when required.
6. Exact next task.

Do not reproduce large command outputs or entire documents unless specifically requested.
