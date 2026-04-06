# Codex Adapter

This folder documents how MergenHan core skills and blueprints are translated into Codex-friendly repo task packets.

## Scope

- repo task packet format
- agent expectations and execution boundaries
- task packet or repository-aware usage notes
- how core behavior is mapped into the Codex workflow

## Examples

- [`mapping.md`](./mapping.md): how a core asset is represented in Codex
- [`task-packet-example.md`](./task-packet-example.md): a short task packet example
- [`meshy-3d-prompt-composer-task-packet-example.md`](./meshy-3d-prompt-composer-task-packet-example.md): a short task packet example for the Meshy 3D prompt skill
- [`resume-composer-task-packet-example.md`](./resume-composer-task-packet-example.md): a short task packet example for the ATS-friendly English resume skill

## Boundary

Codex-specific tool conventions, permissions, and task-packet language do not live in the core. They are documented only in this adapter layer.
