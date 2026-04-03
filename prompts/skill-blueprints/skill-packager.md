---
id: mh-blueprint-skill-packager
title: Skill Packager
type: blueprint
status: draft
version: 0.1.0
summary: Bir blueprint'in paketlenmis skill olmaya hazir olup olmadigini degerlendiren ve klasor yapisini hazirlayan evrensel taslak.
tags:
  - packaging
  - workflow
  - governance
depends_on:
  - mh-blueprint-prompt-library-curator
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
input_contract: Belirli bir blueprint'in skill paketine terfi ettirilip ettirilmeyecegini ve nasil paketlenecegini degerlendirme talepleri.
output_contract: Terfi karari, onerilen skill klasor yapisi, gerekli `SKILL.md` ve `meta.yaml` unsurlari.
notes: Paketleme karari migration odaklidir; davranisi sifirdan yazmak yerine mevcut blueprint'i cekirdekte korur.
---

# Responsibility

Bir blueprint'i yeniden yazmadan, paketlenebilir cekirdek skill yapisina migrate et.

# Trigger Signals

- "Bu blueprint artik skill olsun mu?"
- "Paket yapisini hazirla"
- "Hangi yardimci klasorler lazim?"

# Workflow

1. Kaynak blueprint'in tetikleyici sinyallerini, workflow'unu ve bagimliliklarini incele.
2. Skill paketine tasinmasi gereken cekirdek talimati ayristir.
3. `meta.yaml` icin zorunlu yonetisim alanlarini doldur.
4. Gerekliyse `references/`, `examples/`, `assets/` veya `scripts/` ihtiyacini acikla.
5. Adapter'e ait runtime notlarini cekirdege gommeden ayrica isaretle.
6. Sonucu terfi uygunlugu ve sonraki bakim adimlariyla bitir.

# Promotion Criteria

- Blueprint tekrar eden kullanim desenine sahipse
- Giris ve cikis kontrati netse
- Bagimlilik zinciri saklanmadan paketlenebiliyorsa
- Cekirdek tanim provider-specific olmadan ayakta kalabiliyorsa
