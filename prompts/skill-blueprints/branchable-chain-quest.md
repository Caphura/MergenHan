---
id: mh-blueprint-branchable-chain-quest
title: Branchable Chain Quest
type: blueprint
status: stable
version: 1.0.0
summary: Turns branching quest-chain ideas into a clear quest graph with unlock gates, chain completion rules, and daily quest activation logic.
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
input_contract: A request to design or clarify a quest system where tasks can branch, multiple tasks can unlock later chains, and completed chains can activate daily quests.
output_contract: A readable quest-chain specification with node definitions, branch rules, multi-task gates, daily quest unlock conditions, edge cases, open questions, and acceptance criteria.
notes: This blueprint focuses on system design and quest logic. It does not assume a specific engine, database schema, live-ops backend, or quest scripting format unless the user provides one.
---

# Responsibility

Transform a rough branchable quest-chain idea into a precise, reusable quest logic specification.

# Trigger Signals

- "Design a branching quest chain."
- "Some tasks split into branches and later unlock another chain."
- "A later quest should unlock only after several previous quests are complete."
- "Daily quests should open after the main chain is finished."
- "Make this quest progression clearer for implementation."

# Workflow

1. Identify the progression goal, player context, and any known quest beats.
2. Separate one-time quest chains from repeatable daily quest loops.
3. Define atomic quest nodes with stable names, purpose, completion condition, reward intent, and unlock dependencies.
4. Map branches as parallel or alternative paths; do not treat every side task as a linear chain step.
5. Define gates explicitly:
   - `ALL` gates require every listed prerequisite.
   - `ANY` gates require one listed prerequisite.
   - `COUNT` gates require a specified number from a set.
6. Connect gates to later chains and mark whether they unlock immediately, after claim, after turn-in, or after a reset boundary.
7. Define the daily quest unlock as a separate activation rule at the end of the relevant chain or gate.
8. Surface edge cases: abandoned quests, replayed steps, partial completion, skipped branches, reset timing, reward duplication, and daily unlock persistence.
9. Produce a compact implementation-oriented spec rather than narrative-only quest text.

# Output Shape

Use this structure unless the user asks for a different format:

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

Prefer tables or adjacency lists for quest graphs. Use Mermaid, JSON, YAML, or engine-specific formats only when requested or clearly useful.

# Promotion Criteria

- The same branching quest and daily-unlock design pattern is requested repeatedly.
- The workflow remains useful across RPG, survival, MMO, live-ops, and progression-heavy game systems.
- The output can stay provider-agnostic while still being implementation-oriented.
- Engine-specific quest data formats can be handled later through adapters or task-specific implementation work.
