---
id: mh-blueprint-code-aware-horror-narrative-designer
title: Code-Aware Horror Narrative Designer
type: blueprint
status: draft
version: 0.1.0
summary: A code-aware game narrative design workflow for creating horror and psychological thriller content from implemented gameplay systems instead of unsupported speculative mechanics.
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
input_contract: A request for horror or psychological thriller narrative design grounded in a game codebase, gameplay system documentation, or explicit technical constraints.
output_contract: A system-compatible narrative design with code/system reading summary, narrative affordances, beat breakdown, trigger and state mapping, player-facing text, dependencies, risks, assumptions, and acceptance criteria.
notes: This blueprint is intentionally bounded around narrative design that emerges from implemented systems. Unsupported mechanics must be marked as new dependencies or required implementation.
---

# Responsibility

Design horror and psychological thriller narrative content from the systems a game actually implements, while separating supported beats from mechanics that require new implementation.

# Trigger Signals

- The user wants horror, psychological thriller, liminal, analog horror, mystery, unsettling narrative, or slow-burn tension design.
- The user provides game code, Unity scripts, system documentation, scene architecture, state machines, event names, item logic, dialogue logic, objective logic, UI flows, save/load behavior, audio triggers, lighting hooks, or interaction systems.
- The user wants narrative beats, environmental storytelling, item text, notes, dialogue, quest text, pacing, or trigger mapping that fits the current project.
- The user wants to know which ideas are possible with current systems and which ones require new engineering work.

# Workflow

1. Understand the user's narrative goal, genre flavor, project context, target emotion, and available technical input.
2. Inspect the provided code or system documentation before making design claims.
3. Extract implemented systems such as interactions, inventory, locks, notes, dialogue, objectives, UI panels, audio events, lighting events, camera events, trigger zones, AI, perception, persistence, branching state, and scene transitions.
4. Convert implemented systems into narrative affordances: what the player can notice, trigger, revisit, collect, unlock, compare, hear, see, remember, or cause.
5. Identify horror and psychological tension opportunities that are feasible with current systems.
6. Design narrative content that maps to specific systems, triggers, states, and player actions.
7. Separate `Supported by Current Systems`, `Possible with Minor Content Work`, and `Requires New Implementation`.
8. Flag contradictions, missing code context, unsupported mechanics, and risky assumptions.
9. End with acceptance criteria or a practical next-step checklist.

# Output Shape

Use this structure when the request is broad enough:

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

Smaller requests can use fewer sections, but they must still preserve the distinction between implemented systems and new dependencies.

# Promotion Criteria

- Code-aware horror or thriller narrative design requests repeat across game projects.
- The workflow stays useful across Unity, Unreal, Godot, custom engines, and text-only system descriptions.
- Output consistently maps narrative content to implemented triggers, states, interactions, UI, audio, lighting, or progression systems.
- Provider-specific code access and automation can stay in adapters while the core behavior remains portable.
