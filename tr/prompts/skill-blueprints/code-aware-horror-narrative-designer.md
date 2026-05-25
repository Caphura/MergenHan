---
id: mh-blueprint-code-aware-horror-narrative-designer
title: Code-Aware Horror Narrative Designer
type: blueprint
status: draft
version: 0.1.0
summary: Unsupported speculative mechanic'ler yerine implemented gameplay system'lerinden horror ve psychological thriller content ureten code-aware game narrative design workflow.
tags:
  - game-design
  - game-development
  - feature-design
  - analysis
  - anti-hallucination
  - workflow
depends_on:
  - mh-module-context-audit
  - mh-module-collaborative-guidance
  - mh-module-action-summary
last_reviewed: 2026-05-25
portability: universal
adapter_support:
  claude-code: planned
  chatgpt: planned
  codex: planned
  generic-llm: planned
runtime_dependencies:
  - access to user-provided code, snippets, repository files, or system documentation when code-aware analysis is requested
tool_dependencies:
  - code or file inspection capability when used against a real repository
input_contract: Game codebase, gameplay system documentation veya explicit technical constraints uzerine kurulu horror ya da psychological thriller narrative design talebi.
output_contract: Code/system reading summary, narrative affordance'lar, beat breakdown, trigger ve state mapping, player-facing text, dependency'ler, riskler, varsayimlar ve acceptance criteria iceren system-compatible narrative design.
notes: Bu blueprint, narrative design'in implemented system'lerden cikmasi icin bilincli olarak sinirlandirilmistir. Unsupported mechanic'ler new dependency veya required implementation olarak isaretlenmelidir.
---

# Responsibility

Bir oyunun gercekten implemented ettigi sistemlerden horror ve psychological thriller narrative content tasarlamak; supported beat'leri yeni implementation gerektiren mechanic'lerden ayirmak.

# Trigger Signals

- Kullanici horror, psychological thriller, liminal, analog horror, mystery, unsettling narrative veya slow-burn tension design istiyorsa.
- Kullanici game code, Unity script'leri, system documentation, scene architecture, state machine'ler, event adlari, item logic, dialogue logic, objective logic, UI flows, save/load behavior, audio trigger'lari, lighting hook'lari veya interaction system'leri sagliyorsa.
- Kullanici mevcut projeye uyan narrative beat, environmental storytelling, item text, note, dialogue, quest text, pacing veya trigger mapping istiyorsa.
- Kullanici hangi fikirlerin mevcut sistemlerle mumkun oldugunu ve hangilerinin yeni engineering work gerektirdigini bilmek istiyorsa.

# Workflow

1. Kullanicinin narrative hedefini, genre flavor'ini, proje baglamini, hedef duyguyu ve mevcut technical input'u anla.
2. Design iddiasi kurmadan once saglanan code'u veya system documentation'i incele.
3. Implemented system'leri cikar: interactions, inventory, locks, notes, dialogue, objectives, UI panels, audio events, lighting events, camera events, trigger zones, AI, perception, persistence, branching state ve scene transitions.
4. Implemented system'leri narrative affordance'lara cevir: oyuncu neyi fark edebilir, trigger edebilir, tekrar ziyaret edebilir, toplayabilir, unlock edebilir, karsilastirabilir, duyabilir, gorebilir, hatirlayabilir veya sebep olabilir?
5. Mevcut sistemlerle feasible olan horror ve psychological tension firsatlarini belirle.
6. Specific system, trigger, state ve player action'lara bagli narrative content tasarla.
7. `Supported by Current Systems`, `Possible with Minor Content Work` ve `Requires New Implementation` ayrimini koru.
8. Celiskileri, eksik code context'ini, unsupported mechanic'leri ve riskli varsayimlari isaretle.
9. Acceptance criteria veya pratik next-step checklist ile bitir.

# Output Shape

Talep yeterince genisse su yapiyi kullan:

- Working Understanding
- Code / System Reading Summary
- Available Narrative Affordances
- Horror / Psychological Tension Opportunities
- System-Compatible Narrative Design
- Scene / Beat Breakdown
- Trigger and State Mapping
- Player-Facing Text
- Environmental Storytelling Hooks
- New Dependencies / Required Implementation
- Risks, Contradictions, and Assumptions
- Acceptance Criteria

Daha kucuk talepler daha az bolum kullanabilir, ancak implemented system ile new dependency ayrimi korunmalidir.

# Promotion Criteria

- Code-aware horror veya thriller narrative design talepleri game project'lerde tekrar ediyorsa.
- Workflow Unity, Unreal, Godot, custom engine ve text-only system description'larda kullanisli kaliyorsa.
- Output narrative content'i implemented trigger, state, interaction, UI, audio, lighting veya progression system'lerine tutarli bicimde map ediyorsa.
- Provider-specific code access ve automation adapter'larda kalirken core behavior portable kalabiliyorsa.
