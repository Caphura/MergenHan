---
id: mh-blueprint-adapter-mapper
title: Adapter Mapper
type: blueprint
status: stable
version: 1.0.0
summary: Core prompt, skill veya blueprint'i Claude Code, ChatGPT, Codex ve generic LLM usageina esleyen dogrulanmis evrensel mapper blueprint'i.
tags:
  - portability
  - documentation
  - workflow
depends_on:
  - mh-module-context-audit
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
input_contract: Bir core the asset different runtime'larda how temsil edilecegini description requestleri.
output_contract: Her adapter icin neyin degismeden kaldigi ve neyin runtime seviyesinde uyarlanabilecegi clear bir mapping ozeti.
notes: This blueprint core davranisi cevirir; provider'a specific uygulama ayrintilarini related adapter belgelerine birakir. Repo icindeki adapter mapping akislarinda tekrarli usage gordugu ve stable skill paketine kaynaklik ettigi icin stabilize edilmistir.
---

# Responsibility

Core the asset portable mantigini koruyarak runtime'a specific usage rehberi uret.

# Trigger Signals

- "Bunu Claude Code'a how tasiriz?"
- "Ayni skill ChatGPT ve Codex'te how temsil edilir?"
- "Hangi kisim core, hangi kisim adapter?"

# Workflow

1. Core the asset degismemesi gereken kimligini, amacini ve dependenciesini cikar.
2. Runtime'a specific beklentileri coreten ayir.
3. Her adapter icin temsil form, degismeyecek kisimlar ve adaptable kisimlari listele.
4. Provider-specific davranisin adapter belgesine gitmesi gerektigini explicitly belirt.
5. Sonucu adapter bazli short mapping tablosu veya maddeleriyle sun.

# Promotion Criteria

- Ayni core asset icin birden fazla runtime rehberine tekrar tekrar ihtiyac varsa
- Mapping dili core davranisi degistirmeden adaptation yapiyorsa
- Yeni adapter eklemeyi kolaylastiran sabit bir iskelet sagliyorsa
