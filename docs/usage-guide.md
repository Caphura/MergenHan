# Usage Guide

This document explains step by step how to use skills, master prompts, and modules from the MergenHan library in any AI environment.

## Language and Source Note

- The repository root is the canonical English source.
- The Turkish usage mirror lives under `tr/README.md` and `tr/docs/`.
- `scripts/` is locale-aware and supports both EN and TR catalog and validation flows.

## Core Idea

Every `SKILL.md` file in MergenHan is a ready-made instruction set that tells an AI: "do this task in these steps and under these rules." No matter which AI you use, the same core instruction can be reused; only the way you place it changes.

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

## Use It in Three Steps

1. Find the skill you need under `catalog/skills.md`.
2. Copy the content of `skills/<skill-name>/SKILL.md`.
3. Paste it into your AI environment and give your task.

Every skill package carries at least two files:

- `SKILL.md`: the core working instruction
- `meta.yaml`: dependency, version, and source-blueprint context

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

## Using Master Prompts

Master prompts are orchestration files that combine multiple modules. Unlike skills, they are for broader task flows.

For example, to organize the prompt library itself:

```text
prompts/masters/active/prompt-library-orchestrator.md
```

Usage: paste the master prompt into the AI. The behavior of its modules is already documented through the `Assembly Map` inside the prompt.

## Session Composer Difference

Skills such as `game-strategy-session-composer` and `real-estate-valuation-session-composer` do not perform the full analysis themselves. They first select the correct analysis session and then generate a copy-paste opening message for another AI session.

## Core Rules

- Keep runtime-specific syntax out of the core layer; put provider-specific notes under `adapters/`.
- Follow skill workflow steps in order.
- Skills such as `resume-composer` and the real-estate set explicitly forbid unsupported claims.
- Default output is text-based unless the user explicitly asks for a visual or file artifact.

## Advanced: Adding New Content

This guide focuses on using existing skills. If you want to add new prompts, modules, or skills:

- Quick start: the "30-Second Start" section in the README
- Detailed rules: [`docs/conventions.md`](conventions.md)
- Composition and promotion flow: [`docs/composition-guide.md`](composition-guide.md)
- Skill package spec: [`docs/skill-package-spec.md`](skill-package-spec.md)
