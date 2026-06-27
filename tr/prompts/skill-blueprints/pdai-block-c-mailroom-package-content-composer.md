---
id: mh-blueprint-pdai-block-c-mailroom-package-content-composer
title: PDAI Block C Mailroom Package Content Composer
type: blueprint
status: draft
version: 0.1.0
summary: Existing PackageInspectionRecord data model'i ve mevcut Unity prefab reference'larini kullanarak PDAI Block C Mailroom package inspection content uretme, revize etme, validate etme veya localize etme workflow'u.
tags:
  - game-development
  - game-design
  - workflow
  - validation
  - anti-hallucination
depends_on:
  - mh-module-context-audit
  - mh-module-collaborative-guidance
  - mh-module-action-summary
last_reviewed: 2026-06-27
portability: universal
adapter_support:
  claude-code: planned
  chatgpt: planned
  codex: planned
  generic-llm: planned
runtime_dependencies:
  - access to the PDAI Unity project or exported package inspection database when authoring content
tool_dependencies:
  - file inspection capability for schema, validator, prefab, record, and localization review
input_contract: Existing PackageInspectionRecord data model'i ve mevcut Unity prefab reference'larini kullanarak PDAI Block C Mailroom package inspection content yaratma, revize etme, validate etme veya localize etme talebi.
output_contract: Existing package progression'i ve verdict logic'i koruyan package content brief'leri, JSON-ready package record patch'leri, localization key/value draft'lari ve validation checklist.
notes: Bu blueprint yalnizca content-authoring icindir. Kullanici ayri bir implementation task baslatmadikca yeni gameplay system, script, runtime mechanic, editor tool ve prefab creation kapsam disidir.
---

# Responsibility

Content author'lari PDAI Block C Mailroom package inspection content uzerinde calisirken existing data schema, package database, validator rules, localization surface'leri ve physical PackIns prefab'lari icinde tutmak.

# Trigger Signals

- Kullanici Block C Mailroom package record, inspection clue, package content, verdict logic, physical content veya package horror-tension concept istiyorsa.
- Kullanici PDAI, `PackageInspectionRecord`, `BCM_001` gibi package ID'leri veya 24-package mailroom progression'dan bahsediyorsa.
- Kullanici JSON-ready record patch, localization key/value draft veya package inspection content icin validation guidance istiyorsa.
- Task existing Unity content kullanmali ve yeni gameplay system, script, runtime feature, editor tooling veya prefab eklememeliyse.

# Workflow

1. Package content yazmadan once current PDAI repository'yi veya exported database'i incele.
2. Package schema, validator, database JSON utility, existing record'lar, localization key'leri ve available PackIns prefab source'larini oku.
3. Target package ID'lerini, package count'u, tone intensity'yi ve existing concept'lerin korunup korunmayacagini netlestir.
4. Content'i yalnizca existing record field'lari, localization string'leri ve existing prefab reference'lari uzerinden compose et.
5. Verdict rules'i tutarli uygula: release, return, quarantine ve destroy matching evidence ile desteklenmelidir.
6. Direct Unity `.asset` YAML edit yerine JSON export/import patch workflow'unu tercih et.
7. Order, enum name, prefab path, evidence consistency, localization coverage ve dry-run import readiness icin validation checklist ile bitir.

# Output Shape

- Design review icin content brief'leri.
- PDAI package database JSON utility ile compatible JSON-ready package record patch'leri.
- `Package.<PackageId>.*` key'leriyle localization key/value draft'lari.
- Unity import veya localization handoff oncesi validation checklist.

# Promotion Criteria

- Workflow Block C Mailroom content authoring icin tekrar tekrar kullanisliysa.
- Boundary'ler stable ise: existing schema, existing prefab'lar, existing localization ve yeni runtime system yok.
- Reference dosyalari contract'i, physical content inventory'yi ve output format'larini core skill'i sisirmeden tasiyabiliyorsa.
- Adapter davranisi provider-agnostic kalabiliyorsa; repository access ve Unity dry-run mekanikleri environment concern'dur.
