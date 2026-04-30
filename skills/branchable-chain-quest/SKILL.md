---
name: branchable-chain-quest
description: Use when a user wants to design, clarify, or specify a game quest system with branching tasks, multi-task unlock gates, chained quest progression, and daily quests that unlock after one-time chains are completed.
---

# Branchable Chain Quest

## Use When

- The user wants a quest chain that can split into branches or parallel task groups.
- A later quest or chain should unlock after multiple prior quests are complete.
- Quest progression needs explicit `ALL`, `ANY`, or `COUNT` prerequisite logic.
- Daily quests should unlock only after a main, side, faction, tutorial, or onboarding chain is completed.
- The desired output is a readable quest logic spec, not final quest dialogue or engine-specific data.

## Workflow

1. Identify the player's progression context, the chain purpose, and the desired end-state.
2. Separate one-time chain content from repeatable daily quest content.
3. Break the system into atomic quest nodes; give each node a stable name, purpose, completion condition, reward intent, and dependency.
4. Map branches as parallel paths, optional alternatives, or required subchains.
5. Define unlock gates explicitly:
   - `ALL`: every prerequisite must be complete.
   - `ANY`: at least one prerequisite must be complete.
   - `COUNT`: a specific number of quests from a set must be complete.
6. Define when each unlock fires: on objective complete, on quest turn-in, on reward claim, or after a reset boundary.
7. Attach later chains to their gates and make daily quest activation a separate final rule.
8. Check edge cases: abandoning quests, skipped branches, partial completion, replay, reset timing, reward duplication, account-wide versus character-specific unlocks, and persistence of daily unlocks.
9. If critical information is missing, ask one short round of high-impact questions; otherwise make conservative assumptions and mark them.

## Output Expectations

- Use this default structure: `Quest System Summary`, `Quest Node List`, `Branch Map`, `Unlock Gates`, `Chain Completion Rules`, `Daily Quest Unlock Plan`, `Rewards and Progression Notes`, `Edge Cases`, `Open Questions`, `Acceptance Criteria`.
- Quest nodes should be implementation-friendly and compact.
- Unlock rules must be testable; avoid vague conditions like "after doing enough quests."
- Distinguish branch, chain, gate, and daily loop as separate concepts.
- Include daily quest reset timing and persistence assumptions when relevant.
- Do not invent engine, backend, database, or live-ops support that the user did not provide.

## Portability Notes

- This skill's core behavior is provider-agnostic.
- Runtime-specific quest data schemas, Unity/Unreal implementation steps, editor automation, or backend scheduling details belong in adapters or task-specific implementation work.
- The default task is quest logic specification; final narrative writing, localization, and code generation are separate follow-up tasks unless requested.
