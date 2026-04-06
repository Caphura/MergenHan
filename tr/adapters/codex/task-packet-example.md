# Codex Task Packet Example

Bu ornek, cekirdek bir blueprint'in Codex tarafinda repo gorev paketi olarak nasil kullanilabilecegini gosterir.

## Core Kaynaklar

- [`prompts/skill-blueprints/catalog-validator.md`](../../prompts/skill-blueprints/catalog-validator.md)
- [`catalog/prompts.md`](../../catalog/prompts.md)
- [`catalog/skills.md`](../../catalog/skills.md)
- [`catalog/dependencies.md`](../../catalog/dependencies.md)

## Ornek Gorev Paketi

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

## Kisa Not

Codex'e ozel gorev paketleme dili bu adapter dosyasinda kalir; cekirdek karar mantigi blueprint'ten gelir.