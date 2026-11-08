# OSCP Project Operator

A custom Claude Skill for the OSCP-Exam-PoC vault and its instructor-facing website.

The Skill is designed for Claude Desktop and should be used only for this project. It emphasizes accurate documentation, evidence preservation, controlled phase execution, selective reference loading, and low-overhead file inspection.

## Package contents

- SKILL.md — activation and operating rules.
- references/ — selectively loaded project guidance.
- scripts/ — read-only inventory, YAML validation, and Obsidian link auditing.
- tests/ — synthetic tests for the scripts.

## Safety model

The scripts never modify source Markdown, YAML, or links. They can write reports only to explicitly provided output paths. No automatic repair mode is provided.

The YAML validator uses PyYAML when already installed. It does not install dependencies. If PyYAML is unavailable, it reports that YAML parsing was not performed.

The link auditor is filename-based. It deliberately reports duplicate basenames as ambiguous and documents its limitations. It does not replace Obsidian's full resolver.

## Test

Python 3.10 or later is recommended. PyYAML 6.x is needed for the YAML validator test.

From this directory, run:

    python -m py_compile scripts/*.py tests/*.py
    python -m unittest discover -s tests -v

The tests create temporary synthetic vaults. They do not use or modify the examination vault.

## Example usage

Inventory a vault and write reports outside the source directory:

    python scripts/inventory.py /path/to/vault --json-out /path/to/reports/inventory.json --csv-out /path/to/reports/inventory.csv

Validate frontmatter without changing notes:

    python scripts/validate_yaml.py /path/to/vault --json-out /path/to/reports/frontmatter.json

Audit links without repairing them:

    python scripts/audit_links.py /path/to/vault --json-out /path/to/reports/links.json

Review the script and its limitations before running it in any new environment.

## Install as a Claude Skill

1. Download the repository ZIP or copy the oscp-project-operator directory.
2. Keep the directory name oscp-project-operator; it must match the Skill name in SKILL.md.
3. Create a ZIP containing the oscp-project-operator folder at its root.
4. In Claude, open Customize → Skills and upload the ZIP.
5. Enable the Skill if Claude presents an enable toggle.

Availability of file execution depends on the tools exposed in the current Claude Desktop session. The Skill does not assume Claude Code, subagents, hooks, or paid features.
