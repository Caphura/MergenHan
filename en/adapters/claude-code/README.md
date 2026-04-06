# Claude Code Adapter

This folder holds the runtime mapping notes required to use MergenHan core prompts and skills in a Claude Code style workflow.

## Scope

The following topics are documented here:

- slash-command or command-entry patterns
- settings, hooks, and permission model
- agent wiring or task-distribution notes
- how core assets are executed inside Claude Code

## Examples

- [`mapping.md`](./mapping.md): how a core asset is represented in Claude Code
- [`settings.example.json`](./settings.example.json): a safe, optional settings example for the adapter layer

## Boundary

Core behavior is not rewritten here. The actual prompt or skill logic stays under `prompts/` and `skills/`. Claude-Code-specific syntax and automation live in this adapter layer.
