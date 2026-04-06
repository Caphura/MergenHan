# How to Use MergenHan on Any AI

This document explains step by step how to use skills, master prompts, blueprints, and modules from the MergenHan library in any AI environment.

## Language and Source Note

- The repository root is the canonical English source.
- The Turkish usage mirror lives under `tr/README.md` and `tr/docs/`.
- `scripts/` is locale-aware and supports both EN and TR catalog and validation flows.

## Core Idea

MergenHan separates portable core content from runtime-specific adapter notes.

The usual flow is:

1. Choose the smallest correct core asset.
2. Give that core asset to the AI.
3. Add your task, inputs, and constraints.
4. Keep runtime-specific behavior in the adapter layer, not inside the core asset.

## Start With the Right Asset

| If you need | Use | Why |
| --- | --- | --- |
| A repeatable bounded task | `skills/` | Already packaged for direct reuse |
| A broader orchestrated workflow | `prompts/masters/` | Combines multiple modules for one task family |
| A pre-packaging workflow draft | `prompts/skill-blueprints/` | Useful when no packaged skill exists yet |
| A reusable behavior fragment | `prompts/modules/` | Best for composing or extending other assets |

If you are unsure, start with `onboarding-router`.

## Universal Workflow

1. Find the closest asset in `catalog/skills.md` or under `prompts/`.
2. Give the AI the core source:
   - repo-aware AI: reference the file path
   - instruction-based AI: paste the asset content into instructions
   - plain chat AI: paste only the minimum relevant asset into the chat
3. Add your task, source material, and constraints.
4. Add optional context only when it helps:
   - skill: `meta.yaml`
   - master: `depends_on` and `Assembly Map`
   - blueprint: input/output contract and notes
5. Tell the AI to follow the workflow in order and report missing inputs instead of inventing them.
6. If the runtime needs special commands, tools, or permissions, use the relevant adapter notes under `adapters/`.

## Fastest Copy-Paste Template

Use this when the AI cannot read repository files directly:

```md
You are using the MergenHan library.

Core source:
- skills/resume-composer/SKILL.md

Optional context:
- skills/resume-composer/meta.yaml

Task:
- Draft an ATS-friendly resume from the notes below.

Rules:
- Follow the core workflow in order.
- Keep runtime-specific assumptions out of the core skill.
- If information is missing, say so instead of inventing it.

Expected output:
- Candidate Summary
- Resume Draft
- Weak Spots / Missing Inputs
```

## Which Skill Fits My Need?

Check `catalog/skills.md`. Current packaged skills include:

| Need | Skill |
| --- | --- |
| Writing a CV / resume | `resume-composer` |
| Building image prompts | `nano-banana-image-prompt-composer` |
| Writing 3D asset prompts | `meshy-3d-prompt-composer` |
| Evaluating game ideas strategically | `game-strategy-session-composer` |
| Writing game feature specs | `feature-spec-composer` |
| Real-estate valuation | `real-estate-valuation-session-composer` |
| Apartment investment analysis | `apartment-investment-analyzer` |
| Library maintenance | `prompt-library-curator` |
| Packaging blueprints into skills | `skill-packager` |
| Routing requests to the right asset | `onboarding-router` |
| Adapter mapping | `adapter-mapper` |
| Catalog validation | `catalog-validator` |

If you are unsure, start with `onboarding-router`.

Note: Skills marked `archived` may remain in the catalog as historical references, but they should not be preferred for new use.

## Pasting by Platform

### ChatGPT

Put the `SKILL.md` content into project instructions or the Instructions field of a custom GPT.

Example project instructions:

```md
You are using MergenHan as a portable prompt and skill library.
Use the core behavior from `skills/resume-composer/SKILL.md`.
Use `skills/resume-composer/meta.yaml` for dependency and source-blueprint context.
Do not invent ChatGPT-specific runtime rules inside the core skill.
If a request is ChatGPT-specific, keep that adaptation in the adapter layer only.
```

See [`adapters/chatgpt/project-instructions-example.md`](../adapters/chatgpt/project-instructions-example.md) for more detail.

### Claude Code

Because Claude Code is repository-aware, it can see skill files directly. It is enough to reference the relevant file inside the session:

```text
This repository is the MergenHan prompt library.
Use the core behavior from `skills/resume-composer/SKILL.md`.
```

See [`adapters/claude-code/README.md`](../adapters/claude-code/README.md) and [`adapters/claude-code/settings.example.json`](../adapters/claude-code/settings.example.json) for more detail.

### Codex

Define the core skill as a task packet:

```md
Objective: Draft an ATS-friendly resume using the MergenHan resume-composer skill.
Core source: skills/resume-composer/SKILL.md
Working set:
- skills/resume-composer/SKILL.md
- skills/resume-composer/meta.yaml
Constraints:
- Follow the skill's workflow steps exactly
- Keep output in English unless instructed otherwise
Expected output:
- Candidate Summary
- Resume Draft
- Weak Spots / Missing Inputs
```

See [`adapters/codex/task-packet-example.md`](../adapters/codex/task-packet-example.md) for more detail.

### Any LLM (Minimum Path)

1. Copy `SKILL.md` into the session.
2. Summarize `meta.yaml` if dependency or source context helps.
3. Add a simple instruction such as:

```text
Use the core behavior from MergenHan's `resume-composer` skill.
Follow the workflow steps in order.
Keep runtime-specific assumptions out of the core recommendation.
```

This is the lowest-common-denominator route. It assumes no special tools, hooks, or permissions.

See [`adapters/generic-llm/minimal-usage-example.md`](../adapters/generic-llm/minimal-usage-example.md) for more detail.

## Using Master Prompts

Master prompts are orchestration files that combine multiple modules. Unlike skills, they are for broader task flows.

For example, to organize the prompt library itself:

```text
prompts/masters/active/prompt-library-orchestrator.md
```

Usage: paste the master prompt into the AI. The behavior of its modules is already documented through the `Assembly Map` inside the prompt.

## Using Blueprints

Blueprints are stabilized pre-packaging drafts. Use them when no packaged skill exists yet, but expect them to evolve faster than packaged skills.

When using a blueprint:

1. Paste the blueprint itself first.
2. Keep its `depends_on`, contracts, and notes visible if they affect the task.
3. Do not treat it as a fully frozen package unless it has been promoted into `skills/`.

## Using Modules

Modules are reusable support fragments. They are usually not pasted alone unless you are composing a new master prompt or adapting an existing workflow.

Typical module roles include:

- capability behavior
- domain knowledge
- tone guidance
- constraints
- output formatting

## Session Composer Difference

Skills such as `game-strategy-session-composer` and `real-estate-valuation-session-composer` do not perform the full analysis themselves. They first select the correct analysis session and then generate a copy-paste opening message for another AI session.

## Example Scenario: Writing a Resume

1. Open `skills/resume-composer/SKILL.md` and copy it.
2. Paste it into the AI session.
3. Provide your raw career notes, current resume text, or screenshots.
4. The AI will follow the workflow and produce a structured resume draft.

Expected output shape:

- Candidate Summary
- Target Role Fit (optional)
- Resume Draft (ATS-friendly)
- Weak Spots / Missing Inputs
- Optional Tailoring Notes (if there is a job post)

## Example Scenario: Evaluating a Game Idea

1. Open `skills/game-strategy-session-composer/SKILL.md` and copy it.
2. Paste it into the AI session and describe your game idea.
3. The skill selects the right analysis session:
   - Steam potential: `Core + Steam Market Validation`
   - MVP reduction: `Core + MVP Scope Reduction`
   - Production risk: `Core + Production Risk Strategy`
   - Full evaluation: all of them together
4. It gives you a copy-paste session opening that you can move into another AI session.

## Example Scenario: Building an Image Prompt

1. Open `skills/nano-banana-image-prompt-composer/SKILL.md` and copy it.
2. Paste it into the AI session and say what scene you want.
3. The skill asks 2-4 clarifying questions.
4. It then produces a directly copyable Nano Banana prompt.

## Core Rules

- Keep runtime-specific syntax out of the core layer; put provider-specific notes under `adapters/`.
- Follow skill workflow steps in order.
- Skills such as `resume-composer` and the real-estate set explicitly forbid unsupported claims.
- Default output is text-based unless the user explicitly asks for a visual or file artifact.

## Advanced: Adding New Content

This guide focuses on using existing library assets. If you want to add new prompts, modules, or skills:

- Quick start: the "30-Second Start" section in the README
- Detailed rules: [`docs/conventions.md`](conventions.md)
- Composition and promotion flow: [`docs/composition-guide.md`](composition-guide.md)
- Skill package spec: [`docs/skill-package-spec.md`](skill-package-spec.md)
