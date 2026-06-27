# Output Formats

## Content Briefs For Design Review

Use this format when the user wants concepts, reviewable package ideas, or a pre-implementation pass:

```md
## Package <PackageId>

- Current concept:
- Proposed concept:
- Correct verdict:
- Primary lesson:
- Declared contents:
- Actual contents:
- Physical contents:
- Evidence tags:
- Inspection clue flow:
- Decision rationale:
- Localization impact:
- Validation notes:
```

## JSON-Ready Package Record Patches

Use JSON field names from the current `PackageInspectionDatabaseJsonUtility` DTO. Prefer patch-style snippets for review; for direct dry-run import, emit the complete JSON document and complete records required by the utility.

```json
{
  "packageId": "BCM_001",
  "declaredContents": "",
  "actualContents": "",
  "physicalContents": [
    {
      "guid": "",
      "assetPath": "Assets/BlockCMailroom/Prefabs/PackIns/...",
      "displayNameOverride": ""
    }
  ],
  "evidenceTags": "RegistryClean, WeightInRange, SealClean, ContentsMatch",
  "correctVerdict": "Release",
  "decisionRationale": "",
  "inspectionInfoSubtitle": "",
  "inspectionInfoBody": "",
  "inspectionInfoRows": []
}
```

Rules:

- Match JSON field names, enum names, and nested structures to the current `PackageInspectionDatabaseJsonUtility` DTO.
- Keep package order intact in any multi-record patch.
- Do not include GUIDs unless gathered from Unity or `AssetDatabase`.
- Do not include fields that do not exist in the current schema.
- Mark unchanged fields as omitted only for review patches. Include unchanged fields when preparing a real dry-run import document.

## Localization Key/Value Drafts

Use the existing localization file format and key naming pattern. Draft keys should follow:

```text
Package.<PackageId>.<FieldOrPurpose>
```

Example draft shape:

```text
Package.BCM_001.DeclaredContents = ...
Package.BCM_001.ActualContents = ...
Package.BCM_001.DecisionRationale = ...
Package.BCM_001.InspectionInfo.Subtitle = ...
Package.BCM_001.InspectionInfo.Body = ...
```

Rules:

- Inspect existing localization keys before adding new drafts.
- Preserve existing key style, casing, separators, and locale file format.
- Keep player-facing text consistent with the requested tone intensity.
- Do not localize fields that are internal-only unless the current project already does.

## Validation Checklist Before Import

Include this checklist before any Unity import or handoff:

- Package IDs and order preserve `BCM_001` through `BCM_024`.
- Existing `PrimaryLessonId` values are preserved unless explicitly changed by request.
- Enum names match the current `PackageInspectionData.cs` schema.
- Evidence tags exist and support the selected verdict.
- `Release` records have clean registry, weight, seal, and content match.
- `Return` records have administrative issue evidence, ordinary contents, and no physical hazard.
- `Quarantine` records include isolation evidence and do not include `NoRoutingValue`.
- `Destroy` records include `NoRoutingValue` and disposal evidence.
- Physical content `assetPath` values exist under `Assets/BlockCMailroom/Prefabs/PackIns`.
- Localization keys follow `Package.<PackageId>.*` and match the current locale file format.
- No package concept requires new scripts, runtime mechanics, editor tools, validator changes, or prefab creation.
- JSON dry-run import succeeds through `PackageInspectionDatabaseJsonUtility.DryRunImportJson` or the equivalent Unity menu item before real import.
