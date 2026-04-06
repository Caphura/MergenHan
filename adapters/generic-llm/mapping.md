# Generic LLM Mapping

## What Does the Adapter Expect?

- A portable core prompt or skill definition in plain text
- Explicit dependencies and constraints
- A workflow description that does not assume tools or permissions

## How Is the Core Skill Represented Here?

- `SKILL.md` is treated as a directly usable core instruction
- `meta.yaml` provides context and governance information
- Blueprint or master explanations can be added manually to the session context when needed

## What Must Remain Unchanged from the Core?

- Identity, scope, and dependencies
- Core workflow
- Constraints and output expectations

## What Can Be Adapted at the Runtime Level?

- Whether context is provided in a single message or step by step
- Shortening or expanding the session opener
- Adjusting the output template to fit the interface

## Short Note

- Skills like the text-only image prompt composer port directly through `SKILL.md`.
- In Gemini-like environments, even if visual tools exist, the default behavior should still preserve text output.
