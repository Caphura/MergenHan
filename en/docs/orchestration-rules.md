# Orchestration Rules

This document defines how core asset types inside MergenHan relate to one another and how they evolve across the repository.

## General Principles

- Core content should stay readable, portable, and explicit about its dependencies.
- When behavior starts repeating, consider a `module` first.
- Runtime-specific behavior must not be hidden inside the core layer; move it to adapters.
- A promotion is not complete until catalogs and dependency records are updated.

## Master Rules

- A `master` is an explicit composition of multiple modules for one task family.
- Masters should use an `Assembly Map` or a similar section to show which dependencies they use and why.
- If behavior inside a master becomes reusable, extract it into a separate module.

## Module Rules

- Modules are reusable support units.
- They should stay close to the single-responsibility principle.
- A module does not represent a full task; it provides a reusable support fragment for tasks.
- As long as they can remain independent, modules should avoid unnecessary mandatory links to other modules.

## Blueprint Rules

- A blueprint is a stabilized pre-packaging skill draft.
- Every blueprint must declare its dependencies explicitly through `depends_on`.
- Even when a blueprint is ready for packaging, it should not contain runtime-specific syntax.
- Promotion criteria should remain traceable inside the document or the relevant packaging spec.

## Skill Rules

- Skill packages are promoted into `skills/` without losing blueprint lineage.
- Skills must not hide the dependency chain; `meta.yaml` or catalog records should show it.
- Provider-specific behavior belongs in adapter mappings, not the core skill definition.
- One skill can be supported by multiple adapters.

## Catalog Rules

- Every new or moved asset should remain traceable in the relevant catalog.
- Promotions update `catalog/prompts.md`, `catalog/skills.md`, and when needed `catalog/dependencies.md`.
- `catalog/taxonomy.md` controls new tag needs in a deliberate way.
- Catalogs are indexes, not owners; the real source of truth is the repository asset itself.

## Archive Rules

- Archived content is not deleted; it remains discoverable.
- Archived entries are not fully removed from catalogs; their status stays visible.
- If a new variant supersedes older content, that relationship should remain visible in notes or catalogs.

## Adapter Relationship

- Adapter mapping is not a lifecycle stage.
- An adapter is the runtime compatibility layer for existing core content.
- The same core asset may appear in multiple adapters with different execution notes, but identity, purpose, and dependency chain continue to come from the core layer.
