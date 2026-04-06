# Adapter Model

MergenHan is an AI-agnostic prompt and skill library. Core content in this repository is not locked to one provider, one runtime, or one tool family.

## Three-Layer Model

| Layer | Content | Why It Is Separate |
| --- | --- | --- |
| `core` | Prompts, modules, masters, blueprints, skills, catalogs, templates, and core documentation | The longest-lived knowledge lives here and stays portable |
| `adapter` | Runtime mappings for Claude Code, ChatGPT, Codex, or generic LLM usage | Each environment has a different command, tool, permission, and automation model |
| `validation` | Lightweight scripts and validation rules | Improves maintenance quality without owning the meaning of the core content |

## What Counts as Core Content?

Core content is written with these principles:

- It is not tied to one provider syntax.
- It allows the same skill to be represented by multiple adapters.
- It preserves portable task logic and the dependency chain.
- It stays readable and easy to maintain by hand.

Things that should not live inside core content:

- Slash-command patterns valid only in one runtime
- Platform-specific tool-call syntax
- Hooks, permission rules, agent wiring, or similar execution-environment details
- Platform-specific settings semantics

## What Does the Adapter Layer Do?

The adapter layer explains how a core prompt or skill should be carried into a specific runtime.

Typical responsibilities include:

- Claude Code slash-command, settings, hooks, and permission conventions
- ChatGPT project-instructions, custom-GPT, or manual prompt-injection packaging
- Codex task packets, tool expectations, and execution notes
- Minimal usage for generic LLM environments

These details do not belong in the core layer; they are documented under the relevant adapter.

## One Skill Can Map to Multiple Adapters

A packaged skill does not need to have exactly one runtime representation. The expected model is:

- one core skill definition in the core layer
- one or more adapter mappings for that skill
- adapters that translate execution style without changing core behavior

## Adding a New Adapter

When you add a new runtime, the minimum skeleton is:

- `adapters/<runtime>/README.md`
- `adapters/<runtime>/mapping.md`
- compact examples or optional settings files when useful

This does not change ownership of the core content. It only adds a new runtime transition layer.

## Why Is Validation Separate?

The validation layer is not a runtime. Its job is to:

- detect broken references in catalogs
- reveal missing metadata
- catch maintenance issues such as duplicate IDs or broken relative links

Validation supports repository discipline, but it does not replace the core content itself.

## Core Rules

- MergenHan is AI-agnostic.
- Core content must not be locked to Claude Code or any other single provider.
- Runtime-specific commands, hooks, permission rules, and tool conventions belong to the adapter layer.
- One skill may have multiple adapter mappings.
- Adapter mappings do not change core dependency ownership; they reference core IDs and dependency chains.
