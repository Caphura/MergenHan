---
id: mh-blueprint-pdai-block-c-mailroom-package-content-composer
title: PDAI Block C Mailroom Package Content Composer
type: blueprint
status: draft
version: 0.1.0
summary: A content-authoring workflow for creating, revising, validating, or localizing PDAI Block C Mailroom package inspection content using the existing PackageInspectionRecord data model and existing Unity prefab references.
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
input_contract: A request to create, revise, validate, or localize PDAI Block C Mailroom package inspection content using the existing PackageInspectionRecord data model and existing Unity prefab references.
output_contract: Package content briefs, JSON-ready package record patches, localization key/value drafts, and a validation checklist that preserve existing package progression and verdict logic.
notes: This blueprint is intentionally content-authoring only. New gameplay systems, scripts, runtime mechanics, editor tools, and prefab creation are out of scope unless the user starts a separate implementation task.
---

# Responsibility

Guide content authors through PDAI Block C Mailroom package inspection content work while staying inside the existing data schema, package database, validator rules, localization surfaces, and physical PackIns prefabs.

# Trigger Signals

- The user asks for Block C Mailroom package records, inspection clues, package contents, verdict logic, physical contents, or package horror-tension concepts.
- The user references PDAI, `PackageInspectionRecord`, package IDs such as `BCM_001`, or the 24-package mailroom progression.
- The user wants JSON-ready record patches, localization key/value drafts, or validation guidance for package inspection content.
- The task must use existing Unity content and must not add new gameplay systems, scripts, runtime features, editor tooling, or prefabs.

# Workflow

1. Inspect the current PDAI repository or exported database before writing package content.
2. Read the package schema, validator, database JSON utility, existing records, localization keys, and available PackIns prefab sources.
3. Clarify target package IDs, package count, tone intensity, and whether existing concepts should be preserved or replaced.
4. Compose content only through existing record fields, localization strings, and existing prefab references.
5. Apply verdict rules consistently: release, return, quarantine, and destroy must be supported by matching evidence.
6. Prefer JSON export/import patches over direct Unity `.asset` YAML edits.
7. End with a validation checklist for order, enum names, prefab paths, evidence consistency, localization coverage, and dry-run import readiness.

# Output Shape

- Content briefs for design review.
- JSON-ready package record patches compatible with the PDAI package database JSON utility.
- Localization key/value drafts using `Package.<PackageId>.*` keys.
- A validation checklist before Unity import or localization handoff.

# Promotion Criteria

- The workflow is repeatedly useful for Block C Mailroom content authoring.
- The boundaries are stable: existing schema, existing prefabs, existing localization, and no new runtime systems.
- Reference files can carry the contract, physical content inventory, and output formats without bloating the core skill.
- Adapter behavior can remain provider-agnostic because repository access and Unity dry-run mechanics are environment concerns.
