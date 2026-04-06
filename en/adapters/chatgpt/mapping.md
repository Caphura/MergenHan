# ChatGPT Mapping

## What Does the Adapter Expect?

- A copyable core prompt or skill summary
- Clear wording for the dependencies and constraints that must travel with the session
- An instruction structure that can be placed at the project or Custom GPT level when needed

## How Is the Core Skill Represented Here?

- `SKILL.md` is read as the core skill instruction to carry into the user or project context
- `meta.yaml` shows the source blueprint and dependencies
- ChatGPT-specific injection shape or project-instructions format is explained by this adapter

## What Must Remain Unchanged from the Core?

- Identity and purpose
- Input and output contract
- Core workflow
- Provider-agnostic behavior principles

## What Can Be Adapted at the Runtime Level?

- Whether the prompt is given as one block or in parts
- Project instructions, Custom GPT packaging, or manual session usage
- How the output format is presented inside the ChatGPT interface

## Short Note

- Skills like the text-only image prompt composer port cleanly through `SKILL.md`.
- Even if ChatGPT has image-generation capabilities, the default behavior may still be to produce a text prompt as output.
- Feature-spec-focused skills can also travel through `SKILL.md` and `meta.yaml` as project instructions or a manual session opener.
- Apartment-investment analysis skills can travel the same way, but preserving the distinction between evidence, assumptions, and unknowns is critical.
