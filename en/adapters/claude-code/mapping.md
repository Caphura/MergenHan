# Claude Code Mapping

## What Does the Adapter Expect?

- A readable core prompt, blueprint, or skill definition
- A clear `depends_on` chain
- `portability` and `adapter_support` information when needed

## How Is the Core Skill Represented Here?

- `SKILL.md` is read as the core instruction
- `meta.yaml` provides dependency and package information
- Claude-Code-specific slash commands, hooks, settings, and permission notes are described in this adapter document

## What Must Remain Unchanged from the Core?

- ID, title, and purpose
- Dependency chain
- Trigger usage logic
- Core workflow steps

## What Can Be Adapted at the Runtime Level?

- Command invocation style
- Tool usage and permission model
- Agent distribution or task orchestration
- Converting the session opener into Claude Code format
