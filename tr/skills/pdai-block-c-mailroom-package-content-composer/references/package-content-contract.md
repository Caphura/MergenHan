# Package Content Contract

## Core PDAI Path Anchors

Content authoring veya revision oncesi current PDAI repository icinde su file'lari locate et:

- `PackageInspectionData.cs`: `PackageInspectionRecord`, verdict enum'lari, evidence field'lari, inspection text field'lari ve optional mutation field'lari icin schema source.
- `PackageInspectionDatabase.asset`: project icinde calisirken canonical Unity database asset.
- `PackageContentsRevealProfile.cs`: package content reveal rules ve data shape.
- `PackageDecisionValidator.cs`: verdict, evidence, progression ve package consistency check'leri.
- `PackageInspectionDatabaseJsonUtility.cs`: preferred JSON export/import ve dry-run import surface.

Stale remembered path'lere dayanma. Current PDAI repo'da file location'larini bul ve inspect ettigin kaynaklari belirt.

## Authoring Constraint

Bu skill sadece sunlari modify edebilir veya onerebilir:

- package content data
- localization text
- existing prefab reference'lari

Bu skill sunlari eklememeli veya istememelidir:

- yeni gameplay feature
- yeni script veya runtime system
- yeni editor tool
- yeni Unity component
- yeni validator
- yeni physical prefab
- package concept'i calistirmak icin gereken yeni mechanic

Bir concept yeni system gerektiriyorsa out of scope olarak isaretle ve ya existing field'lara uyacak sekilde sadelestir ya da kullanicidan ayri feature-spec task baslatmasini iste.

## Required Progression

- `BCM_001` through `BCM_024` canonical 24-package demo progression'i koru.
- Kullanici acikca progression veya validator change istemedikce package order'i koru.
- Kullanici acikca validator change istemedikce existing `PrimaryLessonId` value'larini koru.
- Package ID'lerini sessizce ekleme, silme, renumber etme veya split etme.

## Verdict Rules

### `Release`

`Release` yalnizca tum condition'lar clean ise kullan:

- registry clean
- weight in range
- seal clean
- actual contents declared contents ile match ediyor
- evidence isolation, disposal veya administrative return ima etmiyor

### `Return`

Problem administrative ve physical contents ordinary ise `Return` kullan:

- admin, registry, routing, recipient, address, documentation veya intake issue var
- contents ordinary veya non-hazardous
- physical hazard yok
- evidence isolation veya disposal'i justify etmiyor

### `Quarantine`

Isolation evidence varsa `Quarantine` kullan:

- evidence containment, contamination, infection, supernatural bleed-through, unstable contents veya unresolved package risk'i destekliyor
- package `NoRoutingValue` icermiyor
- disposal primary supported action degil

### `Destroy`

`Destroy` yalnizca disposal evidence explicit ise kullan:

- evidence `NoRoutingValue` iceriyor
- package unrecoverable contamination, forbidden routing value, terminal hazard veya validator-supported destruction rationale gibi disposal evidence'a sahip
- rationale destruction'i quarantine'den ayiriyor

## Consistency Checks

Content sunmadan once kontrol et:

- package ID requested range icinde kaliyor
- enum name'ler current schema ile match ediyor
- evidence tag'leri selected verdict'i destekliyor
- `DeclaredContents` ve `ActualContents` intended clue relationship'i olusturuyor
- `PhysicalContents` path'leri approved PackIns source altinda var
- localization key'leri `Package.<PackageId>.*` kullaniyor
- proposed content yeni script, system, mechanic veya prefab gerektirmiyor
