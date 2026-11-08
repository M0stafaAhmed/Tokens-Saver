# PROJECT_PROFILE.md

> Stable project operating context. Fill only values supported by the actual project. Delete unused sections rather than leaving invented defaults.

## Project identity

- **Project name:** [Confirmed name]
- **Purpose:** [One or two sentences]
- **Primary deliverable(s):** [What this project is expected to produce]
- **Status:** [Current confirmed status]

## Workspace and source of truth

- **Active workspace:** [Exact path or Claude Project name]
- **Authoritative source:** [Exact path/repository/branch/document]
- **Original / immutable inputs:** [Exact paths, or "None identified"]
- **Working copy:** [Exact path, or "Not established"]
- **Output location:** [Exact path, or "Not established"]
- **State file:** [Exact path, normally PROJECT_STATE.md]

## Source hierarchy

Describe which source wins if records conflict.

1. [Highest-authority source]
2. [Secondary source]
3. [Derived summaries or reports]

Do not treat generated outputs or chat summaries as authoritative unless explicitly designated.

## Stable decisions and architecture

- [Confirmed decision]
- [Confirmed architecture or design]
- [Important version or compatibility constraints]

## Conventions

- **Naming:** [Confirmed convention]
- **File formats:** [Confirmed convention]
- **Documentation voice:** [Confirmed convention]
- **Code/style:** [Confirmed convention]
- **Metadata/schema:** [Confirmed convention]

## Protected material and prohibited operations

- **Never modify:** [Exact files/directories or "Not established"]
- **Requires explicit approval:** [Destructive operations, public deployment, dependency additions, etc.]
- **Out of scope:** [Explicit exclusions]
- **Secrets handling:** Never copy credentials, API keys, access tokens, or passwords into project notes, state files, or handoffs.

## Available tools and validation

- **Available environment/tools:** [Only verified tools]
- **Existing tests/validators:** [Exact paths or commands]
- **Acceptance criteria:** [How deliverables are judged]
- **Known limitations:** [Confirmed limitations]

## Reference map

| Reference | Purpose | Load when |
|---|---|---|
| [Path] | [Purpose] | [Trigger] |

## Profile maintenance

Update this file only when stable project facts, paths, architecture, or operating rules change. Keep active task progress in PROJECT_STATE.md instead.
