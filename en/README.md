# MergenHan Prompt Library

## Language Switch

- Turkish canonical source: [`../README.md`](../README.md)
- English mirror: [`README.md`](README.md)

Note: Turkish remains the canonical repository language. Content under `en/` is a maintained English mirror; `scripts/` stays single-copy and locale-aware.

MergenHan is a portable AI prompt and skill library designed to stay readable, maintainable, and resilient as it grows. Core content is not locked to a single provider; adaptations for Claude Code, ChatGPT, Codex, and generic LLM environments live in the `adapters/` layer.

## What Is This Repo For?

- Manage master prompts as versioned assets instead of one-off notes
- Split reusable modules and combine them across multiple workflows
- Turn mature skill drafts into portable skill packages
- Map the same core content into different AI runtimes through adapters
- Grow the library without losing structure, taxonomy, or examples

## Repo Map

```text
.
|-- adapters/
|   |-- claude-code/
|   |-- chatgpt/
|   |-- codex/
|   `-- generic-llm/
|-- catalog/
|   |-- dependencies.md
|   |-- prompts.md
|   |-- skills.md
|   `-- taxonomy.md
|-- docs/
|   |-- adapter-model.md
|   |-- composition-guide.md
|   |-- conventions.md
|   |-- lifecycle.md
|   |-- orchestration-rules.md
|   |-- skill-package-spec.md
|   |-- usage-guide.md
|   `-- validation-rules.md
|-- examples/
|   `-- compositions/
|-- prompts/
|   |-- masters/
|   |   |-- active/
|   |   `-- archived/
|   |-- modules/
|   |   |-- capability/
|   |   |-- constraints/
|   |   |-- domain/
|   |   |-- output/
|   |   `-- tone/
|   `-- skill-blueprints/
|-- scripts/
|-- skills/
`-- templates/
    `-- skill-package/
```

## Using Existing Skills

For a step-by-step guide to using packaged skills from this repository in any AI environment such as ChatGPT, Claude Code, or Codex, see [`docs/usage-guide.md`](docs/usage-guide.md).

## 30-Second Start

The shortest path:

1. Copy the closest template from `templates/`.
2. Fill only the required metadata fields.
3. Place the file under the right location in `prompts/`.
4. Regenerate the catalogs: `python scripts/generate_catalog.py`
5. Run the validation scripts.

If you do not want to copy files manually:

- `python scripts/new_prompt.py master your-slug`
- `python scripts/new_prompt.py module your-slug --category capability`
- `python scripts/new_prompt.py blueprint your-slug`

Required prompt fields for a first draft:

- `id`
- `title`
- `type`
- `status`
- `version`
- `summary`
- `tags`
- `depends_on`
- `last_reviewed`

Fields such as `input_contract`, `output_contract`, `notes`, `portability`, `adapter_support`, `runtime_dependencies`, and `tool_dependencies` can be added when needed.

## Quick Start

1. Start new content from the correct template under `templates/`.
2. Place it under the right category in `prompts/`.
3. If you introduce new tags, align them with [`catalog/taxonomy.md`](catalog/taxonomy.md).
4. Regenerate catalogs instead of editing them manually: `python scripts/generate_catalog.py`
5. When a skill behavior stabilizes, promote the draft from `prompts/skill-blueprints/` into `skills/<skill-slug>/`.
6. If runtime-specific notes are needed, add them under the relevant adapter instead of changing the core content.

## Where Should I Start?

If you only want to use existing skills:

1. Usage guide: [`docs/usage-guide.md`](docs/usage-guide.md)
2. Skill catalog: [`catalog/skills.md`](catalog/skills.md)

If you want to write content or understand the library structure:

1. This README
2. An example master prompt: [`prompts/masters/active/prompt-library-orchestrator.md`](prompts/masters/active/prompt-library-orchestrator.md)
3. Rules and conventions: [`docs/conventions.md`](docs/conventions.md)

If you want to go deeper:

- Reusable module example: [`prompts/modules/capability/context-audit.md`](prompts/modules/capability/context-audit.md)
- Unpackaged skill draft: [`prompts/skill-blueprints/prompt-library-curator.md`](prompts/skill-blueprints/prompt-library-curator.md)
- Packaged skill example: [`skills/prompt-library-curator/SKILL.md`](skills/prompt-library-curator/SKILL.md)
- Visual-prompt skill example: [`skills/nano-banana-image-prompt-composer/SKILL.md`](skills/nano-banana-image-prompt-composer/SKILL.md)
- Adapter model: [`docs/adapter-model.md`](docs/adapter-model.md)
- Lifecycle: [`docs/lifecycle.md`](docs/lifecycle.md)
- Composition and promotion flow: [`docs/composition-guide.md`](docs/composition-guide.md)

## Starting in a New AI Environment

1. Pick the right core source first: `skills/` for reusable packaged behavior, `prompts/skill-blueprints/` for pre-packaging skill drafts, and `prompts/masters/` for orchestration flows.
2. Then pick the relevant adapter. Runtime-specific usage notes live under `adapters/`.
3. When adding a new runtime, create at least `adapters/<runtime>/README.md` and `adapters/<runtime>/mapping.md`; add examples or optional settings files when useful.
4. Do not move core IDs, dependency ownership, or workflow logic into the adapter layer. The adapter only explains execution style.

Practical adapter examples:

- Claude Code settings example: [`adapters/claude-code/settings.example.json`](adapters/claude-code/settings.example.json)
- ChatGPT project-instructions example: [`adapters/chatgpt/project-instructions-example.md`](adapters/chatgpt/project-instructions-example.md)
- Codex task-packet example: [`adapters/codex/task-packet-example.md`](adapters/codex/task-packet-example.md)
- Generic LLM minimal-usage example: [`adapters/generic-llm/minimal-usage-example.md`](adapters/generic-llm/minimal-usage-example.md)

## Content Types

- `master`: a composed version of multiple modules for a specific task
- `module`: a reusable behavior, constraint, tone, or output fragment
- `blueprint`: a stabilized skill draft before packaging
- `skill`: a packaged capability that can be mapped into multiple runtimes
- `adapter`: the layer that adapts core content to a runtime's command, tool, and permission model

## Working Flow

### 1. From Idea to Prompt

- New ideas begin from templates.
- Reusable parts are split into `prompts/modules/`.
- Full task flows live under `prompts/masters/active/`.

### 2. From Prompt to Blueprint

- Once modular skill behavior becomes clear, it moves into `prompts/skill-blueprints/`.
- Packaging does not happen until input and output contracts are clear.

### 3. From Blueprint to Skill

- Write a concise `SKILL.md` for the packaged skill.
- Keep governance metadata in `meta.yaml`.
- Add helper folders such as `references/`, `scripts/`, or `assets/` when needed.

### 4. From Skill to Adapter

- Core prompt, blueprint, and skill definitions remain under `prompts/` and `skills/`.
- Runtime-specific slash-command, hook, tool, permission, or agent-wiring details move into `adapters/`.
- One skill can be supported by multiple adapters.

## Repository Principles

- File and folder names always use `kebab-case`.
- The repository root remains Turkish-first; English lives in the maintained `en/` mirror.
- Prompt content is versioned through YAML frontmatter.
- Secrets, customer data, and non-shareable variants do not enter the repo.
- Readability and manual maintenance come first; automation stays limited to lightweight generation and validation scripts.
- Core content must not depend on one provider's syntax or runtime assumptions.

## First Example Flows

- From module to master prompt: [`examples/compositions/module-to-master.md`](examples/compositions/module-to-master.md)
- From blueprint to skill package: [`examples/compositions/blueprint-to-skill.md`](examples/compositions/blueprint-to-skill.md)

## Lightweight Maintenance and Validation

The `scripts/` folder includes dependency-light helper scripts to regenerate catalogs and check repository integrity:

- `python scripts/new_prompt.py master your-slug`
- `python scripts/new_prompt.py module your-slug --category capability`
- `python scripts/new_prompt.py blueprint your-slug`
- `python scripts/generate_catalog.py`
- `python scripts/validate_catalog.py`
- `python scripts/validate_metadata.py`
- `python scripts/check_missing_links.py`
- `python scripts/validate_localization.py`

Recommended flow:

1. Add or update content.
2. Run `python scripts/generate_catalog.py`.
3. Check catalog, metadata, links, and localization consistency with the other scripts.

These scripts do not impose mandatory CI. They exist to accelerate maintenance and reduce manual mistakes.
