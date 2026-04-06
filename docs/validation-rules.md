# Validation Rules

This document defines the lightweight validation checks used to preserve repository integrity.

## Catalog Checks

- Broken catalog entries are reported.
- If a file listed in a catalog does not exist, it counts as an error.
- Prompt or skill files that exist in the repo but are missing from the catalog are reported.
- Catalog row ID and path mismatches are detected.

## Dependency Checks

- Every ID under `depends_on` must resolve in the repo or the relevant catalog.
- Broken dependency references are reported.
- Duplicate records or duplicate IDs are treated as errors.
- The `source_blueprint` link between a skill and its blueprint must remain valid.
- Adapter mapping notes do not change core dependency ownership.

## Metadata Checks

- Missing required frontmatter or `meta.yaml` fields are reported.
- Empty or invalid core fields such as `id`, `title`, `type`, `status`, or `version` count as problems.
- Packaged skill folders must contain both `SKILL.md` and `meta.yaml`.
- `name` and `description` inside `SKILL.md` frontmatter must be valid.
- New-standard fields such as `portability`, `adapter_support`, `runtime_dependencies`, and `tool_dependencies` may be reported as warnings when missing.
- That portability-warning layer is especially relevant for new blueprints, packaged skills, and actively evolving core assets.

## Link Checks

- Relative markdown links must resolve.
- Missing target files or folders are marked as broken links.
- Links provided by catalogs and the README are checked with extra care.

## Scope

Our minimum validation scope includes:

- `README.md`
- `catalog/*.md`
- `docs/*.md`
- `prompts/**/*.md`
- `skills/**/SKILL.md`
- `skills/**/meta.yaml`
- `adapters/**/*.md`

## Implementation Note

These rules do not require heavy CI or external packages. `scripts/validate_catalog.py`, `scripts/validate_metadata.py`, `scripts/check_missing_links.py`, and `scripts/validate_localization.py` are the lightweight, readable implementations of these checks.
