---
id: mh-blueprint-catalog-validator
title: Catalog Validator
type: blueprint
status: draft
version: 0.1.0
summary: Kataloglar, dosyalar, ID'ler ve goreli baglantilar arasindaki tutarliligi denetleyen evrensel validator taslagi.
tags:
  - validation
  - governance
  - documentation
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
input_contract: Repo butunlugunu katalog, dosya, kimlik ve link acisindan denetleme talepleri.
output_contract: Tespit edilen tutarsizliklar, eksik girdiler, duplicate ID'ler ve link sorunlari icin taranabilir rapor.
notes: Bu blueprint runtime'a ozel validator syntax'i uretmez; cekirdek kontrol mantigini tanimlar.
---

# Responsibility

Repo icindeki katalog ve metadata butunlugunu denetle, kirik referanslari gorunur hale getir.

# Trigger Signals

- "Kataloglar guncel mi?"
- "Eksik link veya duplicate ID var mi?"
- "Repo yapisinda kirik referanslari bul"

# Workflow

1. Kataloglarda listelenen yollarin gercekte var olup olmadigini kontrol et.
2. `prompts/` ve `skills/` altindaki dosyalari katalog girdileriyle karsilastir.
3. `depends_on`, `source_blueprint` ve goreli markdown linklerini dogrula.
4. Duplicate ID veya eksik metadata alanlarini tespit et.
5. Bulgulari hata, uyari ve takip notu olarak sirala.

# Promotion Criteria

- Kontrol listesi betiklestirilebilir duzeyde netlesmisse
- Katalog ve metadata bakiminda tekrar eden bir ihtiyaci cozuyorsa
- Cikti formati insanlar ve scriptler icin okunur kaliyorsa
