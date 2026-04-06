---
id: mh-blueprint-skill-packager
title: Skill Packager
type: blueprint
status: stable
version: 1.0.0
summary: Bir blueprint'in paketlenmis skill olmaya ready olup olmadigini evaluates ve folder yapisini hazirlayan dogrulanmis evrensel packaging blueprint'i.
tags:
  - packaging
  - workflow
  - governance
depends_on:
  - mh-blueprint-prompt-library-curator
  - mh-module-repo-architecture
  - mh-module-action-summary
last_reviewed: 2026-04-04
portability: universal
adapter_support:
  claude-code: supported
  chatgpt: supported
  codex: supported
  generic-llm: supported
runtime_dependencies: []
tool_dependencies: []
input_contract: Belirli bir blueprint'in skill paketine promotion ettirilip ettirilmeyecegini ve how paketlenecegini evaluation requestleri.
output_contract: Terfi decisioni, onerilen skill folder structure, required `SKILL.md` ve `meta.yaml` unsurlari.
notes: Paketleme decisioni migration odaklidir; davranisi sifirdan yazmak yerine mevcut blueprint'i corete preserves. Repo icindeki skill promotion akislarinda tekrarli usage gordugu ve stable skill paketine kaynaklik ettigi icin stabilize edilmistir.
---

# Responsibility

Bir blueprint'i yeniden yazmadan, paketlenebilir core skill yapisina migrate et.

# Trigger Signals

- "This blueprint artik skill olsun mu?"
- "Paket yapisini hazirla"
- "Hangi yardimci klasorler lazim?"

# Workflow

1. Kaynak blueprint'in tetikleyici sinyallerini, workflow'unu ve dependenciesini incele.
2. Skill paketine tasinmasi gereken core talimati separate.
3. `meta.yaml` icin required governance alanlarini doldur.
4. Gerekliyse `references/`, `examples/`, `assets/` veya `scripts/` ihtiyacini acikla.
5. Adapter'e ait runtime notlarini cekirdege gommeden ayrica isaretle.
6. Sonucu promotion uygunlugu ve sonraki maintenance adimlariyla bitir.

# Promotion Criteria

- Blueprint tekrar eden usage desenine sahipse
- Giris ve output kontrati netse
- Bagimlilik zinciri saklanmadan paketlenebiliyorsa
- Core tanim provider-specific olmadan ayakta kalabiliyorsa
