# Composition and Promotion Guide

This document clarifies how to build master prompts from modules, how to promote a blueprint into a packaged skill, and how to map that skill into adapters when needed.

## From Module to Master Prompt

A master prompt should be treated as an explicit composition of modules around a concrete task, not as one long block of text.

### Recommended Order

1. Define the core goal of the task.
2. Select the required modules:
   - capability behavior
   - domain knowledge
   - tone
   - constraints
   - output format
3. List the selected modules under `depends_on`.
4. Document how the modules are used through a short `Assembly Map` section inside the master prompt.
5. Update the catalogs.

### When Should I Extract a New Module?

- When you start copying the same paragraph for a second time
- When you want the same quality standard across multiple master prompts
- When the behavior, tone, or constraint is useful in more than one context

## From Blueprint to Skill

A blueprint is the written thinking version of a skill. A skill package turns that into a reusable folder contract that can travel across AI runtimes.

### Promotion Checklist

It is probably time to package when most of these questions are answered with yes:

- Do the trigger scenarios repeat?
- Is the input/output contract clear enough?
- Can the main workflow be explained as ordered steps?
- Is the need for helper references, scripts, or assets now visible?
- If this were added to the catalog, could another person understand and use it?

### Packaging Flow

1. Review the blueprint one last time.
2. Move the simplified working instructions into `skills/<skill-slug>/SKILL.md`.
3. Put governance data into `meta.yaml`.
4. Add helper folders such as `references/`, `scripts/`, `assets/`, or `agents/` when needed.
5. Create the `catalog/skills.md` entry.
6. Document a usage flow under `examples/compositions/`.

## From Skill to Adapter

Once the skill core exists, runtime-specific adaptations live under `adapters/`.

### Adapter Flow

1. Extract the constraints from the core skill or blueprint that must not change.
2. Define runtime-specific commands, tools, permissions, and automation expectations inside the adapter.
3. Keep provider-specific syntax out of the core skill definition.
4. Add mapping notes to the relevant README and `mapping.md` files.
5. If support for a new runtime is added, update `adapter_support` without breaking the core content.

## What Should I Not Package?

- One-off notes that are still taking shape
- Temporary experiments tied to a single project session
- Text that contains only background explanation without a clear workflow

## Lightweight Validation

This repository prefers lightweight validation scripts over heavy CI dependencies.

- `scripts/validate_catalog.py`: checks catalog and file alignment
- `scripts/validate_metadata.py`: checks frontmatter and `meta.yaml` fields
- `scripts/check_missing_links.py`: validates relative markdown links
