---
name: pdai-block-c-mailroom-package-content-composer
description: Use when creating, revising, validating, or localizing PDAI / Block C Mailroom package records, physical package contents, inspection clues, verdict logic, and horror-tension package concepts using existing Unity prefabs and the existing `PackageInspectionRecord` schema only.
---

# PDAI Block C Mailroom Package Content Composer

## Use When

- Kullanici PDAI veya Block C Mailroom package inspection content istiyorsa.
- Calisma package record, declared veya actual content, physical PackIns content, clue, evidence tag, verdict logic, localization text veya horror-tension package concept iceriyorsa.
- Content existing `PackageInspectionRecord` schema'ya, existing package database'e, existing validator'a ve existing Unity prefab reference'larina uymak zorundaysa.
- Kullanici import oncesi design-review brief, JSON-ready record patch, localization draft veya validation checklist istiyorsa.

## Workflow

1. Content yazmadan once current PDAI repository'yi veya exported database'i incele.
2. `references/package-content-contract.md` dosyasindaki contract'i oku.
3. Current package schema, validator, database asset veya JSON export, JSON utility, package reveal profile, PackIns prefab'lari ve localization key'lerini bulup oku.
4. Talep belirtmiyorsa package count, target package ID'leri, tone intensity ve existing concept'lerin replace mi preserve mi edilecegini sor.
5. `PhysicalContents` atamadan once `references/physical-content-inventory.md` dosyasini oku.
6. Final content uretmeden once `references/output-formats.md` dosyasini oku.
7. Sadece existing field'lari kullan: `DeclaredContents`, `ActualContents`, `PhysicalContents`, `EvidenceTags`, `CorrectVerdict`, `DecisionRationale`, `InspectionInfo*` ve schema'da zaten bulunan optional terminal, handbook veya signage mutation field'lari.
8. Kullanici acikca validator change istemedikce `BCM_001` through `BCM_024` order'ini ve existing `PrimaryLessonId` value'larini koru.
9. Direct Unity `.asset` YAML edit yerine JSON export/import workflow'unu tercih et: current database'i export et, JSON'u edit et, Unity'de dry-run import yap, dry-run validation basarili olduktan sonra import et.
10. Physical content reference'larini once `assetPath` olarak tut. GUID'i yalnizca Unity veya `AssetDatabase` ile toplandiysa ekle.

## Output Expectations

- Content claim kurmadan once inspect edilen PDAI file'larini, record'lari, prefab path'lerini ve localization source'larini belirt.
- Tum onerileri existing schema field'lari, existing localization key'leri veya key pattern'leri ve existing prefab reference'lari icinde tut.
- Bu skill kapsaminda yeni gameplay feature, script, runtime mechanic, editor tool, custom validator veya yeni prefab onermeyin.
- Verdict/evidence logic'i `PackageDecisionValidator` review icin yeterince acik yap.
- Missing repository context'i fact uydurmak yerine assumption veya blocker olarak isaretle.

## Guardrails

- JSON export/import path mevcutsa Unity `.asset` YAML'i direct edit etme.
- Kullanici acikca validator veya progression change istemedikce 24-package progression'i, package ID'leri veya `PrimaryLessonId` value'larini degistirme.
- `Assets/BlockCMailroom/Prefabs/PackIns` altinda bulunmayan physical content prefab adlarini kullanma.
- `Quarantine` package'larinda `NoRoutingValue` kullanma.
- Package concept'i desteklemek icin yeni script, Unity component, mechanic, clue, UI state veya prefab yaratma.

## References

- Schema, progression ve verdict constraint'leri icin `references/package-content-contract.md` kullan.
- Approved physical content source group'lari icin `references/physical-content-inventory.md` kullan.
- Content brief, JSON patch, localization ve validation output shape'leri icin `references/output-formats.md` kullan.

## Portability Notes

- Core workflow provider-agnostic'tir.
- Codex, Claude Code, ChatGPT ve generic LLM adapter'lari file inspection veya Unity dry-run calistirma bicimlerinde farkli olabilir; content contract ayni kalir.
- Runtime-specific command'ler, Unity menu path'leri ve permission detaylari core skill'de degil adapter'larda veya task-specific instruction'larda yer almalidir.
