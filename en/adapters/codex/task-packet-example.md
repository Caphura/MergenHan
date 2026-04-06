# Codex Task Packet Example

This example core bir blueprint'in Codex side repo task package olarak how kullanilabilecegini shows.

## Core Sources

- [`prompts/skill-blueprints/catalog-validator.md`](../../prompts/skill-blueprints/catalog-validator.md)
- [`catalog/prompts.md`](../../catalog/prompts.md)
- [`catalog/skills.md`](../../catalog/skills.md)
- [`catalog/dependencies.md`](../../catalog/dependencies.md)

## Example Task Packet

```md
Objective: Run a repository consistency review using the core `catalog-validator` blueprint.
Core source: `prompts/skill-blueprints/catalog-validator.md`
Working set:
- `catalog/prompts.md`
- `catalog/skills.md`
- `catalog/dependencies.md`
- `scripts/validate_catalog.py`
- `scripts/check_missing_links.py`
Constraints:
- Keep edits minimal and documentation-first.
- Preserve IDs, titles, and dependency chains unless inconsistent.
- Do not move provider-specific behavior into the core blueprint.
Expected output:
- short findings list
- proposed or applied minimal fixes
- validation result summary
```

## Short Note

Codex'e specific task packaging dili bu adapter dosyasinda remains; core decision logic blueprint'ten gelir.