---
id: mh-blueprint-branchable-chain-quest
title: Branchable Chain Quest
type: blueprint
status: stable
version: 1.0.0
summary: Branchlere ayrilabilen gorev zinciri fikirlerini unlock gate'leri, zincir tamamlama kurallari ve daily quest aktivasyon logic'i olan net bir quest graph'ina donusturur.
tags:
  - game-design
  - feature-design
  - logic
  - workflow
depends_on:
  - mh-module-context-audit
  - mh-module-action-summary
last_reviewed: 2026-04-30
portability: universal
adapter_support:
  claude-code: supported
  chatgpt: supported
  codex: supported
  generic-llm: supported
runtime_dependencies: []
tool_dependencies: []
input_contract: Gorevlerin branchlere ayrildigi, birden fazla gorevin sonraki zincirleri actigi ve tamamlanan zincirlerin daily questleri aktive ettigi quest sistemi tasarlama veya netlestirme istegi.
output_contract: Quest node tanimlari, branch kurallari, coklu gorev gate'leri, daily quest unlock kosullari, edge case'ler, acik sorular ve acceptance criteria iceren taranabilir quest-chain specification.
notes: Bu blueprint system design ve quest logic'e odaklanir. Kullanici vermedikce belirli bir engine, database schema, live-ops backend veya quest scripting formati varsaymaz.
---

# Responsibility

Ham veya yari tanimli branchable quest-chain fikrini kesin, tekrar kullanilabilir bir quest logic specification haline getirmek.

# Trigger Signals

- "Branchlenen bir gorev zinciri tasarla."
- "Bazi taskler branchlere ayrilsin ve sonra baska zinciri acsin."
- "Sonraki quest birden fazla onceki gorev bitince acilsin."
- "Ana zincir bitince daily questler acilsin."
- "Bu quest progression'i implementasyona hazir netlestir."

# Workflow

1. Progression hedefini, oyuncu baglamini ve bilinen quest beat'lerini belirle.
2. Tek seferlik quest chain'leri repeatable daily quest loop'larindan ayir.
3. Atomic quest node'larini stable isim, amac, completion condition, reward intent ve unlock dependency ile tanimla.
4. Branchleri paralel veya alternatif yol olarak map et; her yan gorevi otomatik linear chain step sayma.
5. Gate'leri explicitly tanimla:
   - `ALL` gate listelenen tum prerequisite'leri ister.
   - `ANY` gate listelenen prerequisite'lerden birini ister.
   - `COUNT` gate belirli bir setten belirli sayida completion ister.
6. Gate'leri sonraki chain'lere bagla ve unlock'in hemen mi, claim sonrasi mi, turn-in sonrasi mi, yoksa reset boundary sonrasi mi oldugunu belirt.
7. Daily quest unlock'ini ilgili chain veya gate sonunda ayri bir activation rule olarak tanimla.
8. Edge case'leri gorunur yap: abandoned quests, replayed steps, partial completion, skipped branches, reset timing, reward duplication ve daily unlock persistence.
9. Narrative-only quest metni yerine kompakt, implementation-oriented bir spec uret.

# Output Shape

Kullanici baska format istemedikce su yapiyi kullan:

- Quest System Summary
- Quest Node List
- Branch Map
- Unlock Gates
- Chain Completion Rules
- Daily Quest Unlock Plan
- Rewards and Progression Notes
- Edge Cases
- Open Questions
- Acceptance Criteria

Quest graph'lari icin tablo veya adjacency list tercih et. Mermaid, JSON, YAML veya engine-specific formatlari sadece istendiginde ya da acikca faydaliysa kullan.

# Promotion Criteria

- Ayni branching quest ve daily-unlock design pattern'i tekrar tekrar isteniyorsa
- Workflow RPG, survival, MMO, live-ops ve progression-heavy game systems genelinde kullanisli kaliyorsa
- Cikti provider-agnostic kalirken implementation-oriented olabiliyorsa
- Engine-specific quest data formatlari daha sonra adapter veya task-specific implementation isiyle ele alinabiliyorsa
