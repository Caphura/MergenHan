# Output Formats

## Content Briefs For Design Review

Kullanici concept, reviewable package idea veya pre-implementation pass istediginde bu format'i kullan:

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

Current `PackageInspectionDatabaseJsonUtility` DTO'sundan JSON field name'leri kullan. Review icin patch-style snippet tercih et; direct dry-run import icin utility'nin gerektirdigi complete JSON document ve complete record'lari uret.

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

- JSON field name, enum name ve nested structure'lari current `PackageInspectionDatabaseJsonUtility` DTO ile match et.
- Multi-record patch icinde package order'i intact tut.
- Unity veya `AssetDatabase` ile toplanmadikca GUID ekleme.
- Current schema'da olmayan field ekleme.
- Unchanged field'lari sadece review patch'lerinde omit et. Real dry-run import document hazirlarken unchanged field'lari da ekle.

## Localization Key/Value Drafts

Existing localization file format'ini ve key naming pattern'ini kullan. Draft key'ler sunu izlemelidir:

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

- Yeni draft eklemeden once existing localization key'lerini inspect et.
- Existing key style, casing, separator ve locale file format'ini koru.
- Player-facing text'i requested tone intensity ile tutarli tut.
- Current project zaten yapmiyorsa internal-only field'lari localize etme.

## Validation Checklist Before Import

Unity import veya handoff oncesi bu checklist'i ekle:

- Package ID'leri ve order `BCM_001` through `BCM_024` progression'ini koruyor.
- Explicitly request edilmediyse existing `PrimaryLessonId` value'lari korunuyor.
- Enum name'ler current `PackageInspectionData.cs` schema ile match ediyor.
- Evidence tag'leri var ve selected verdict'i destekliyor.
- `Release` record'larinda clean registry, weight, seal ve content match var.
- `Return` record'larinda administrative issue evidence, ordinary contents ve no physical hazard var.
- `Quarantine` record'lari isolation evidence iceriyor ve `NoRoutingValue` icermiyor.
- `Destroy` record'lari `NoRoutingValue` ve disposal evidence iceriyor.
- Physical content `assetPath` value'lari `Assets/BlockCMailroom/Prefabs/PackIns` altinda var.
- Localization key'leri `Package.<PackageId>.*` pattern'ini izliyor ve current locale file format ile match ediyor.
- Hicbir package concept yeni script, runtime mechanic, editor tool, validator change veya prefab creation gerektirmiyor.
- Real import oncesi `PackageInspectionDatabaseJsonUtility.DryRunImportJson` veya equivalent Unity menu item ile JSON dry-run import basarili oluyor.
