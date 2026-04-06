---
id: mh-blueprint-prompt-library-curator
title: Prompt Library Curator
type: blueprint
status: stable
version: 1.0.0
summary: Prompt librarysini duzenleyen, kategorilendiren ve paketlemeye ready hale getiren moduler skill taslagi.
tags:
  - packaging
  - documentation
  - governance
depends_on:
  - mh-module-context-audit
  - mh-module-repo-architecture
  - mh-module-action-summary
last_reviewed: 2026-04-03
portability: universal
adapter_support:
  claude-code: supported
  chatgpt: supported
  codex: supported
  generic-llm: supported
runtime_dependencies: []
tool_dependencies: []
input_contract: Master prompt, modul veya skill promptlarini editing, promotion ettirme ya da kataloglama requestleri.
output_contract: Netlestirilmis bilgi mimarisi, current kataloglar ve gerekiyorsa skill paketine gecis onerisi.
notes: Bu draft, davranisi insan by okunur tutar; packaging decisioni verilince `skills/` altina portable.
---

# Responsibility

Prompt librarysindeki content correct turlere ayirmak, maintenancei kolay hale getirmek ve olgunlasan davranislari paketlemeye hazirlamak.

# Trigger Signals

- Kullanici promptlarini "saklamak", "editingk", "kataloglamak" veya "skill'e cevirmek" istediginde
- Ayni davranis birden fazla dosyada yinelenmeye basladiginda
- Bir prompt ailesi icin surum, durum ve dependency takibi gerektiginde

# Workflow

1. Mevcut folder yapisini ve kataloglari tara.
2. Her content `master`, `module`, `blueprint` veya `skill` olarak siniflandir.
3. Eksik metadata, zayif adlandirma veya kayip dependenciesi tespit et.
4. Gerekirse yeni template veya example olustur.
5. Skill paketine promotion edecek icerikler icin sade `SKILL.md` ve ayri `meta.yaml` kurgula.
6. Runtime'a specific usage notlari gerekiyorsa bunlari adapter mapping belgelerine tasimayi oner.
7. Sonucu short bir aksiyon ozetiyle bitir.

# Promotion Criteria

- Davranis tekrar kullanilir hale gelmis olmali.
- Tetikleyici request types explicitly tarif edilebilmeli.
- Gerekli referans veya yardimci dosyalar belli olmali.
- Skill paketine gecince katalog ve README side bulunabilirlik bozulmamali.
- Core tanim tek bir runtime'in command modeline bagli kalmamali.
