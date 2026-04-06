# AGENTS.md

## Purpose

This repository contains reusable prompt assets, blueprints, skills, adapters, and documentation for the MergenHan library.

Your job is to make precise, minimal, repo-consistent changes.
Do not behave like a generic assistant.
Behave like a repository-aware implementation agent.

## Core Operating Model

Use the following working model for all tasks unless the user explicitly overrides it:

1. Read the user request.
2. Interpret it internally using MergenHan Symbolism as a hidden working representation.
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

If the user asks you to "learn" or "use" MergenHan Symbolism, read the official repo documentation for it before applying it.

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
- do not fabricate completed integrations, tests, or adapters

If information is missing:
- infer only when the inference is low-risk and consistent with nearby repo patterns
- otherwise leave a clear TODO or note the uncertainty in the response

## Output Style for User-Facing Responses

When responding to the user:
- use natural language
- be direct and clear
- keep explanations concise unless the task requires depth
- do not dump internal working notation unless requested
- state uncertainty honestly
- summarize what changed and where

## File Authoring Rules

When creating or updating markdown assets:
- keep sections clean and named consistently
- prefer explicit headings over vague prose
- avoid unnecessary verbosity
- avoid decorative filler
- keep examples realistic and implementation-oriented

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

## Validation Rules

Before finishing:
- check that the chosen file location matches the task
- check naming consistency
- check metadata consistency where relevant
- check for duplicate concepts or conflicting terms
- check whether related docs, examples, or adapters should also be updated

If the repo provides validation scripts, checks, or linters:
- run the relevant ones for the changed scope
- report what was run
- report failures clearly
- do not claim success without evidence

If no automated validation exists:
- perform a manual consistency pass against nearby files

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
- the final response tells the user exactly what changed