# AGENTS.md

## Purpose

This repository contains reusable prompt assets, blueprints, skills, adapters, and documentation for the MergenHan library.

Your job is to make precise, minimal, repo-consistent changes.
Do not behave like a generic assistant.
Behave like a repository-aware implementation agent.

## Core Operating Model

Use the following working model for all tasks unless the user explicitly overrides it:

1. Read the user request.
2. When helpful, interpret it internally using MergenHan Symbolism as a hidden working representation.
3. Select the appropriate repository layer and output type.
4. Write or update the smallest correct set of files.
5. Validate consistency with nearby files and repository conventions.
6. Respond to the user in natural language, not in Symbolism, unless the user explicitly asks to see the Symbolism form.

Do not expose internal Symbolism blocks by default.

## Internal Protocol: MergenHan Symbolism

Treat MergenHan Symbolism as an internal control language for:
- task normalization
- intent compression
- constraint tracking
- uncertainty marking
- verification planning

Default interpretation rule:
- user speaks in normal language
- you normalize internally
- you execute using repo rules and relevant skills
- you return output in the user's normal language

If the user asks you to "learn" or "use" MergenHan Symbolism:
- first read the official repo documentation for it if it exists
- the current official repository document is `docs/mergenhan-symbolism.md`
- if the official documentation does not exist yet, use the Symbolism rules defined in this AGENTS.md as the temporary source of truth
- if you rely on this fallback, say so in the final response

## Skill Usage

Use skills for reusable workflows, not AGENTS.md.

When a task matches an existing skill:
- load and follow that skill
- do not re-invent the workflow from scratch
- preserve the skill's intended boundaries

When the user says:
- "learn X from the repo"
- "use X blueprint"
- "use X skill"
- "follow X composer"

you must locate and read the relevant repo asset before writing output.

Example:
If the user asks to use Nano Banana Image Prompt Composer, read its skill or blueprint source first, then apply it.

## Repository Layer Selection

Choose the correct destination before editing.

### docs/
Use for:
- standards
- conventions
- language specifications
- workflow explanations
- architecture notes
- validation rules
- usage models

### templates/
Use for:
- reusable file skeletons
- starter layouts
- section scaffolds

### prompts/masters/
Use for:
- composed task flows
- multi-module orchestration
- broader reusable prompt assemblies

### prompts/modules/
Use for:
- reusable building blocks
- capability, domain, tone, constraint, or output fragments
- behaviors extracted for reuse across masters and blueprints

### prompts/skill-blueprints/
Use for:
- reusable behaviors that are not yet fully stabilized
- candidate workflows
- experimental but structured prompt assets

### skills/
Use for:
- stable reusable workflows
- packaged behaviors with a clear execution purpose
- assets that should be invoked repeatedly by the agent

### adapters/
Use for:
- runtime-specific mappings
- environment-specific usage notes
- how a core behavior maps to a specific AI surface

### examples/
Use for:
- reference usage
- concrete sample compositions
- demonstration assets

## Blueprint vs Skill Rule

If a behavior is reusable but still evolving, prefer a blueprint.
If a behavior is stable, bounded, repeatable, and worth invoking directly, package it as a skill.

Do not promote a blueprint to a skill unless the workflow is already clear and reusable.

## Localization Rule

The repository root is the canonical English source.
Content under `tr/` is a maintained Turkish localization mirror.

When updating canonical documentation or reusable assets:
- check whether the Turkish mirror should also be updated
- do not silently let root and `tr/` drift apart when the meaning should remain aligned
- if localization is intentionally deferred, state that clearly in the final response

`scripts/` stays single-copy and locale-aware.

## Commands

Use these commands when relevant:

- Regenerate catalogs:
  - `python scripts/generate_catalog.py`
  - `python scripts/generate_catalog.py --locale tr`

- Create new prompt assets:
  - `python scripts/new_prompt.py master your-slug`
  - `python scripts/new_prompt.py module your-slug --category capability`
  - `python scripts/new_prompt.py blueprint your-slug`
  - `python scripts/new_prompt.py blueprint your-slug --mirror-locale tr`

- Validate repo integrity:
  - `python scripts/validate_catalog.py`
  - `python scripts/validate_catalog.py --locale tr`
  - `python scripts/validate_metadata.py`
  - `python scripts/validate_metadata.py --locale tr`
  - `python scripts/validate_localization.py`
  - `python scripts/check_missing_links.py`
  - `python scripts/check_missing_links.py --locale tr`

Do not claim validation success unless the relevant commands were run and their results were checked.

## Editing Rules

Before creating new files:
- inspect nearby files
- match naming, metadata, and structural patterns
- avoid duplicate concepts under slightly different names

When editing:
- preserve existing style unless the task is explicitly to refactor
- make minimal, targeted changes
- do not silently rewrite unrelated sections
- do not invent repository facts
- do not fabricate completed integrations, tests, adapters, or validations

If information is missing:
- infer only when the inference is low-risk and consistent with nearby repo patterns
- otherwise leave a clear TODO in the file or note the uncertainty in the final response

## Output Style for User-Facing Responses

When responding to the user:
- use natural language
- be direct and clear
- keep explanations concise unless the task requires depth
- do not dump internal working notation unless requested
- state uncertainty honestly
- summarize what changed and where
- mention validation steps that were run
- mention deferred localization updates when relevant

## File Authoring Rules

When creating or updating markdown assets:
- keep sections clean and named consistently
- prefer explicit headings over vague prose
- avoid unnecessary verbosity
- avoid decorative filler
- keep examples realistic and implementation-oriented

When creating prompt assets:
- use the appropriate template when possible
- include required metadata fields
- keep metadata aligned with nearby examples and repo conventions

When creating skills:
- ensure the skill has a clear purpose
- ensure name and description are specific
- keep instructions actionable
- avoid overloaded or ambiguous triggers

When creating docs for MergenHan Symbolism:
- define symbols once
- keep one symbol = one meaning
- define grammar explicitly
- include validity rules
- include examples
- distinguish internal representation from user-facing output

## Metadata Expectations

For a first-draft prompt asset, preserve required metadata fields unless the target file type follows a different established pattern:

- `id`
- `title`
- `type`
- `status`
- `version`
- `summary`
- `tags`
- `depends_on`
- `last_reviewed`

Add optional fields only when they improve the asset and match repo conventions.

## Validation Rules

Before finishing:
- check that the chosen file location matches the task
- check naming consistency
- check metadata consistency where relevant
- check for duplicate concepts or conflicting terms
- check whether related docs, examples, adapters, or localization files should also be updated

If the repo provides validation scripts, checks, or linters:
- run the relevant ones for the changed scope
- report what was run
- report failures clearly
- do not claim success without evidence

If no automated validation exists:
- perform a manual consistency pass against nearby files

If catalogs may be affected:
- regenerate them instead of editing them manually

## Task Prompt Interpretation

Treat each user request as containing these fields, even if implicit:
- goal
- context
- constraints
- done-when

If any of these are missing:
- infer conservatively
- do not over-assume
- keep the implementation scoped

For complex work:
- first form a short internal plan
- then execute
- then verify

## Do-Not Rules

Do not:
- expose chain-of-thought
- use Symbolism as the default outward response format
- create broad repo rewrites unless explicitly requested
- spread the same concept across multiple competing files
- invent adapter support that does not exist
- promote unstable ideas to stable skills too early
- turn every request into a new skill
- edit generated catalogs manually when regeneration is the correct path
- silently skip validation on tasks that affect structure, metadata, catalogs, or localization

## Preferred MergenHan Behavior

Default behavior for this repo:
- internal structure should be strict
- external communication should feel natural
- repo artifacts should be modular
- reusable workflows should migrate toward skills
- runtime-specific behavior should stay in adapters
- documentation should explain intent without bloating the asset

## Done Criteria

A task is complete when:
- the correct files were chosen
- the requested content was added or updated
- the change matches local repository patterns
- the result is understandable and reusable
- any relevant validation was run or clearly reported
- localization impact was checked or explicitly deferred
- the final response tells the user exactly what changed
