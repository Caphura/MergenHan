---
name: pdai-block-c-mailroom-package-content-composer
description: Use when creating, revising, validating, or localizing PDAI / Block C Mailroom package records, physical package contents, inspection clues, verdict logic, and horror-tension package concepts using existing Unity prefabs and the existing `PackageInspectionRecord` schema only.
---

# PDAI Block C Mailroom Package Content Composer

## Use When

- The user asks for PDAI or Block C Mailroom package inspection content.
- The work involves package records, declared or actual contents, physical PackIns contents, clues, evidence tags, verdict logic, localization text, or horror-tension package concepts.
- The content must fit the existing `PackageInspectionRecord` schema, existing package database, existing validator, and existing Unity prefab references.
- The user needs design-review briefs, JSON-ready record patches, localization drafts, or validation checklists before import.

## Workflow

1. Inspect the current PDAI repository or exported database before writing content.
2. Read the contract in `references/package-content-contract.md`.
3. Locate and read the current package schema, validator, database asset or JSON export, JSON utility, package reveal profile, PackIns prefabs, and localization keys.
4. If the request does not specify them, ask for package count, target package IDs, tone intensity, and whether to replace or preserve existing package concepts.
5. Read `references/physical-content-inventory.md` before assigning `PhysicalContents`.
6. Read `references/output-formats.md` before producing final content.
7. Compose only through existing fields: `DeclaredContents`, `ActualContents`, `PhysicalContents`, `EvidenceTags`, `CorrectVerdict`, `DecisionRationale`, `InspectionInfo*`, and optional terminal, handbook, or signage mutation fields already present in the schema.
8. Preserve `BCM_001` through `BCM_024` order and existing `PrimaryLessonId` values unless the user explicitly requests validator changes.
9. Prefer the JSON export/import workflow over direct Unity `.asset` YAML edits: export current database, edit JSON, dry-run import in Unity, then import only after dry-run validation succeeds.
10. Keep physical content references as `assetPath` first. Include GUID only when gathered from Unity or `AssetDatabase`.

## Output Expectations

- Cite the PDAI files, records, prefab paths, and localization sources inspected before making content claims.
- Keep all suggestions within existing schema fields, existing localization keys or key patterns, and existing prefab references.
- Do not propose new gameplay features, scripts, runtime mechanics, editor tools, custom validators, or new prefabs as part of this skill.
- Make verdict/evidence logic explicit enough for `PackageDecisionValidator` review.
- Mark any missing repository context as an assumption or blocker instead of inventing facts.

## Guardrails

- Do not directly edit Unity `.asset` YAML when a JSON export/import path is available.
- Do not change the 24-package progression, package IDs, or `PrimaryLessonId` values unless the user has explicitly requested a validator or progression change.
- Do not use physical content prefab names that were not found under `Assets/BlockCMailroom/Prefabs/PackIns`.
- Do not include `NoRoutingValue` in `Quarantine` packages.
- Do not create new scripts, Unity components, mechanics, clues, UI states, or prefabs to support a package concept.

## References

- Use `references/package-content-contract.md` for schema, progression, and verdict constraints.
- Use `references/physical-content-inventory.md` for approved physical content source groups.
- Use `references/output-formats.md` for content brief, JSON patch, localization, and validation output shapes.

## Portability Notes

- The core workflow is provider-agnostic.
- Codex, Claude Code, ChatGPT, and generic LLM adapters may differ in how they inspect files or run Unity dry-runs, but the content contract remains the same.
- Runtime-specific commands, Unity menu paths, and permission details belong in adapters or task-specific instructions, not in this core skill.
