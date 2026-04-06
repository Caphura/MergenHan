# MergenHan Symbolism

## Purpose

MergenHan Symbolism is a lightweight symbolic intermediate representation used inside the MergenHan library for:

- task normalization
- intent compression
- constraint tracking
- uncertainty marking
- verification planning

It is not designed to replace normal user language.  
It is designed to make internal agent work more structured, repeatable, and validation-friendly.

## What It Is

MergenHan Symbolism is a compact control notation for turning freeform requests into a stricter internal task form.

Typical usage model:

1. The user speaks in normal language.
2. The agent normalizes the request into MergenHan Symbolism internally.
3. The agent selects the correct workflow, prompt asset, blueprint, or skill.
4. The agent returns the result in natural language unless the user explicitly asks to see the Symbolism form.

## What It Is Not

MergenHan Symbolism is not:

- a public-facing response format by default
- a replacement for full prompt assets
- a replacement for repository metadata
- a runtime adapter
- a guarantee of zero error

It is a control layer, not a full standalone prompt system.

## Design Principles

### 1. One Symbol, One Meaning

Each symbol has one primary meaning.  
A symbol must not carry multiple unrelated roles.

### 2. Stable Block Order

Blocks should appear in a predictable order so that parsing and validation remain simple.

### 3. Minimal Symbol Set

The language should remain small, readable, and easy to apply.  
Do not add symbols unless they solve a recurring structural problem.

### 4. Internal First

The default use of Symbolism is internal.  
Natural language remains the preferred interface for users.

### 5. Validation-Friendly Structure

The notation should make it easier to detect:

- missing fields
- conflicting constraints
- overreach
- unsupported assumptions
- incomplete outputs

## Core Symbol Set

| Symbol | Meaning |
|---|---|
| `@` | task |
| `#` | goal |
| `>` | input |
| `<` | output |
| `!` | constraint |
| `~` | assumption |
| `?` | unknown |
| `+` | include |
| `-` | exclude |
| `&` | verify |
| `x` | fail policy |
| `=` | key-value binding |

## Line Grammar

In v1, Symbolism is line-oriented.

- One clause should occupy one line.
- Blank lines are allowed between clauses.
- Leading and trailing whitespace may be trimmed.
- Inline comments are not part of the v1 grammar; if commentary is needed, place it outside the Symbolism block.
- The default clause shape is `symbol key=value`.
- The shorthand forms `@=task` and `#=goal` remain canonical for the top-level task and goal lines.
- Unknowns may appear either as `? field_name` or `? key=value`; use `? field_name` when the missing item is best expressed as a bare unresolved field.
- Escaping is not part of the v1 spec. If a value would require embedded separators such as extra `=` or ambiguous commas, rewrite it into a simpler stable token instead of relying on escaping rules.

## Recommended Block Order

The preferred block order is:

1. `@` task
2. `#` goal
3. `>` input
4. `<` output
5. `!` constraint
6. `~` assumption
7. `?` unknown
8. `+` include
9. `-` exclude
10. `&` verify
11. `x` fail policy

Not every block is required in every use case, but the order should stay stable when blocks are present.

## Minimum Valid Form

A minimum valid Symbolism block should include:

- one task
- one goal
- at least one input or output expectation

A block that has `@` and `#` but contains neither `>` nor `<` should be treated as invalid rather than merely weak.

Example:

```text
@=feature_spec
#=define_system
> topic=stealth_alarm
< format=structured_doc
```

## Semantics

### `@=task`

Defines the main task type.

Examples:

- `@=feature_spec`
- `@=boss_fight_doc`
- `@=routing_decision`
- `@=adapter_mapping`
- `@=prompt_normalization`

### `#=goal`

Defines the intended result state.

Examples:

- `#=implementation_ready`
- `#=decision_support`
- `#=portable_output`
- `#=structured_prompt`

### `> key=value`

Represents input facts, context, or request parameters.

Examples:

```text
> topic=chain_quest_ui
> engine=unity6
> audience=ui_artist
```

### `< key=value`

Represents output expectations.

Examples:

```text
< format=technical_doc
< language=tr
< length=short
```

### `! key=value`

Represents hard constraints.

Examples:

```text
! fluff=off
! emojis=off
! tone=professional
```

### `~ key=value`

Represents assumptions used by the agent.  
Assumptions must not be presented as confirmed facts.

Examples:

```text
~ platform=pc
~ audience=internal_team
```

### `? key=value`

Represents missing, uncertain, or unresolved fields.

Examples:

```text
? final_reward_values
? exact_runtime_target
```

### `+ key=value`

Represents mandatory inclusion targets.

Examples:

```text
+ include=edge_cases
+ include=phase_transitions
```

### `- key=value`

Represents explicit exclusion targets.

Examples:

```text
- exclude=lore_expansion
- exclude=marketing_copy
```

### `& key=value`

Represents checks to run before considering the task complete.

Examples:

```text
& check=missing_sections
& check=contradictions
& check=metadata_alignment
```

### `x key=value`

Represents failure behavior when validation or completeness conditions are not met.

Examples:

```text
x on_fail=report_missing_fields
x on_fail=emit_partial
x on_fail=block_output
```

## Type Conventions

### Scalar

```text
key=value
```

Example:

```text
> engine=unity6
```

### List

Two list encodings are allowed, but they do not serve the same purpose.

Canonical repeated-line form:

```text
+ include=edge_cases
+ include=phase_transitions
& check=missing_sections
& check=contradictions
```

Use repeated lines as the canonical form for multi-value control targets such as:

- `+ include=...`
- `- exclude=...`
- `& check=...`

Comma-separated form:

```text
< sections=overview,core_loop,edge_cases,ui_flow
```

Use comma-separated values only when one field naturally owns an ordered list, such as:

- `< sections=...`
- `< outputs=...`
- `> artifacts=...`

Do not mix repeated-line and comma-separated encodings for the same field within the same block.

### Repeated Keys

Repeated keys are valid only when the field is intentionally multi-valued.

Preferred valid examples:

```text
+ include=edge_cases
+ include=dependencies
& check=missing_sections
& check=contradictions
```

Structurally weak example:

```text
! tone=direct
! tone=playful
```

Guideline:

- repeated `@` or `#` is always invalid
- repeated `+ include`, `- exclude`, and `& check` is valid and canonical
- repeated scalar-style fields under `>`, `<`, `!`, `~`, `?`, or `x` should be avoided unless the field is explicitly list-like
- if the same scalar field is repeated with conflicting meanings, treat that as structural weakness or conflict

### Boolean-Like Values

Use stable values such as:

- `true` / `false`
- `on` / `off`

Do not mix multiple boolean styles within the same block when avoidable.

### Enum-Like Values

Prefer short, repeatable values over freeform prose.

Good:

```text
! tone=direct
```

Less preferred:

```text
! tone=very clear and somewhat professional but not too dry
```

## Validity Rules

### Hard Fail Conditions

A block should be considered invalid if:

- `@` is missing
- `#` is missing
- `@` appears more than once
- `#` appears more than once
- neither `>` nor `<` appears anywhere in the block
- a symbol is used with no value
- `=` binding is broken
- `&` checks exist but failure handling is impossible or contradictory in context

### Soft Fail Conditions

A block should be considered structurally weak if:

- assumptions are used as facts
- unknowns exist but the response pretends full certainty
- the same field is given conflicting values
- a required output is implied but never specified
- `+ include=` and `- exclude=` conflict on the same target
- the block becomes so compressed that human review is difficult

## Working Model

Recommended internal flow:

1. Read freeform request.
2. Normalize into Symbolism.
3. Select repo layer or skill.
4. Execute the task.
5. Run checks.
6. Return natural-language output.

Default outward behavior:

- internal representation: Symbolism
- user-facing representation: natural language

The Symbolism block should only be exposed if the user asks for it or if debugging requires it.

## Example Blocks

### Example 1: Feature Spec

```text
@=feature_spec
#=implementation_ready
> topic=launcher_download_flow
> engine=unity6
< format=technical_spec
< language=tr
! fluff=off
! emojis=off
+ include=edge_cases
+ include=dependencies
& check=missing_sections
& check=contradictions
x on_fail=report_missing_fields
```

### Example 2: Boss Fight Document

```text
@=boss_fight_doc
#=implementation_ready
> game=olpamis
> boss=alaz
< format=technical_doc
< sections=summary,phases,attacks,rewards
! tone=clear
! fluff=off
? final_reward_values
+ include=phase_transitions
+ include=fail_states
& check=reward_difficulty_match
& check=missing_sections
x on_fail=emit_partial
```

### Example 3: Repo Routing Decision

```text
@=routing_decision
#=correct_repo_placement
> asset=mergenhan_symbolism_normalizer
> maturity=early
< destination=prompts/skill-blueprints
! preserve_repo_conventions=true
& check=duplicate_concepts
& check=layer_fit
x on_fail=report_conflict
```

## Recommended Use Cases

MergenHan Symbolism is especially useful for:

- prompt normalization
- task routing
- skill triggering
- blueprint shaping
- adapter mapping preparation
- validation planning
- orchestration tasks

## Less Suitable Use Cases

It is less suitable as a primary surface for:

- expressive creative writing
- high-emotion conversational writing
- exploratory freeform ideation with no structure
- public-facing prose by default

## Adapter Notes

Adapters should not redefine the meaning of core symbols.

Adapters may define:

- how Symbolism is introduced to a runtime
- whether Symbolism stays hidden or visible
- how validation is phrased in that environment
- how repo assets are loaded before execution

Core symbol semantics must stay stable across runtimes.

## Authoring Guidance

When expanding this language:

- prefer adding examples before adding new symbols
- prefer new conventions before new grammar
- keep expansion conservative
- do not introduce synonyms for existing symbols
- preserve backward readability where possible

## Status

This document defines the first formal public specification for MergenHan Symbolism.

Initial target status:

- lightweight
- internal-first
- repo-oriented
- adapter-friendly

Future revisions may add:

- stricter typed fields
- canonical task enums
- formal validation profiles
- mapping examples for specific runtimes