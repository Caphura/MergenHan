# Skill Package Specification

This document defines the official folder and metadata standard for skill packages inside MergenHan.

## Package Goal

A skill package:

- makes a core workflow reusable
- preserves blueprint lineage
- stays mappable across adapters without embedding runtime-specific behavior into the core layer

## Minimum Package Structure

```text
skills/<skill-slug>/
|-- SKILL.md
`-- meta.yaml
```

These folders can be added when needed:

- `references/`
- `examples/`
- `assets/`
- `scripts/`
- `agents/`

They are added only for real needs; they are not mandatory for every skill.

## Required Fields in `SKILL.md`

`SKILL.md` must include these frontmatter fields:

- `name`
- `description`

The body should include at least these sections:

- `# <Skill Title>`
- `## Use When`
- `## Workflow`
- `## Output Expectations`

Optional sections include:

- `## References`
- `## Portability Notes`
- other core usage notes that do not belong to adapters

`SKILL.md` is the core skill definition; provider-specific behavior does not live there.

## Required Fields in `meta.yaml`

Every skill package must include these fields:

- `id`
- `title`
- `type`
- `status`
- `version`
- `summary`
- `tags`
- `depends_on`
- `last_reviewed`
- `source_blueprint`
- `input_contract`
- `output_contract`

These fields are strongly recommended and treated as the standard for new packages:

- `portability`
- `adapter_support`
- `runtime_dependencies`
- `tool_dependencies`
- `notes`

## Support Folders

### `references/`

- Holds checklists, background notes, and longer explanations.
- Provides supporting context without bloating the core skill.

### `examples/`

- Holds expected usage examples or mini scenarios.
- Especially useful for onboarding and quality control.

### `assets/`

- Holds visuals, templates, static data, or other portable resources.
- Should not be used for platform-specific temporary files.

### `scripts/`

- Holds lightweight automation, transformation helpers, or small validation tools.
- Heavy dependency chains should be avoided.

## Promotion Criteria: Blueprint to Skill

A blueprint is ready to become a skill package when:

- trigger scenarios repeat in a recognizable pattern
- the workflow can be explained as ordered steps
- the input and output contract is clear
- the required helper-folder structure is visible
- catalogs and dependency records are ready to be updated
- the core behavior is not tied to a single provider or runtime syntax

## Portability Rules

- The core skill definition always stays provider-agnostic.
- The same skill may be represented by multiple adapter mappings.
- Markers such as `portability: universal` express core intent; adapters handle runtime realization.
- If `runtime_dependencies` and `tool_dependencies` are present, they explain general conditions required by the core skill. They are not a place for provider-specific command lists.
- Adapter settings examples or task-packet notes belong in the adapter layer, not inside the skill package.

## Validation Compatibility

The lightweight validation layer in this repository can verify:

- the existence of `skills/<skill-slug>/SKILL.md`
- the `name` and `description` frontmatter fields
- the matching `meta.yaml` file
- the validity of the `source_blueprint` link

## Provider-Specific Behavior Rule

Provider-specific behavior must not live in the core skill definition.

The following do not belong inside `SKILL.md` or core `meta.yaml`:

- slash-command names for a specific runtime
- hook definitions
- permission-policy details
- agent wiring or tool-selection syntax

That information belongs in `adapters/<runtime>/mapping.md` or the relevant adapter README.
