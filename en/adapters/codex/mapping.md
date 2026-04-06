# Codex Mapping

## What Does the Adapter Expect?

- A core prompt, blueprint, or skill with clear task logic
- A traceable dependency chain
- Target file or catalog links inside the repo when needed

## How Is the Core Skill Represented Here?

- `SKILL.md` is read as the core execution instruction
- `meta.yaml` provides dependency, source blueprint, and compatibility information
- Codex-specific task packaging, tool usage, and workflow shape are described in this adapter

## What Must Remain Unchanged from the Core?

- The skill's purpose and scope boundary
- Dependency relationships
- Trigger signals and workflow logic
- Core portability rules

## What Can Be Adapted at the Runtime Level?

- How the work is turned into a repo task
- Tool choice, command-execution discipline, and workflow format
- Output presentation and closeout summary style
