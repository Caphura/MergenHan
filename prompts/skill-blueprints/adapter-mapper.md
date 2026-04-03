---
id: mh-blueprint-adapter-mapper
title: Adapter Mapper
type: blueprint
status: draft
version: 0.1.0
summary: Cekirdek prompt, skill veya blueprint'i Claude Code, ChatGPT, Codex ve generic LLM kullanimina esleyen evrensel mapper taslagi.
tags:
  - portability
  - documentation
  - workflow
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
input_contract: Bir cekirdek varligin farkli runtime'larda nasil temsil edilecegini aciklama talepleri.
output_contract: Her adapter icin neyin degismeden kaldigi ve neyin runtime seviyesinde uyarlanabilecegi acik bir mapping ozeti.
notes: Bu blueprint cekirdek davranisi cevirir; provider'a ozel uygulama ayrintilarini ilgili adapter belgelerine birakir.
---

# Responsibility

Cekirdek varligin tasinabilir mantigini koruyarak runtime'a ozel kullanim rehberi uret.

# Trigger Signals

- "Bunu Claude Code'a nasil tasiriz?"
- "Ayni skill ChatGPT ve Codex'te nasil temsil edilir?"
- "Hangi kisim core, hangi kisim adapter?"

# Workflow

1. Cekirdek varligin degismemesi gereken kimligini, amacini ve bagimliliklarini cikar.
2. Runtime'a ozel beklentileri cekirdekten ayir.
3. Her adapter icin temsil sekli, degismeyecek kisimlar ve uyarlanabilir kisimlari listele.
4. Provider-specific davranisin adapter belgesine gitmesi gerektigini acikca belirt.
5. Sonucu adapter bazli kisa mapping tablosu veya maddeleriyle sun.

# Promotion Criteria

- Ayni cekirdek varlik icin birden fazla runtime rehberine tekrar tekrar ihtiyac varsa
- Mapping dili cekirdek davranisi degistirmeden uyarlama yapiyorsa
- Yeni adapter eklemeyi kolaylastiran sabit bir iskelet sagliyorsa
