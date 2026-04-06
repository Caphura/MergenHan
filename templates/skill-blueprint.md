---
id: mh-blueprint-your-slug
title: Your Skill Blueprint Title
type: blueprint
status: draft
version: 0.1.0
summary: Summary of the skill behavior stabilized before packaging.
tags:
  - packaging
  - workflow
depends_on: []
last_reviewed: 2026-04-03
---

Add optional metadata fields when needed:

- `input_contract`
- `output_contract`
- `notes`
- `portability`
- `adapter_support`
- `runtime_dependencies`
- `tool_dependencies`

# Responsibility

Write the main responsibility this blueprint takes on.

# Trigger Signals

- What kind of user request makes this behavior necessary?
- Which signals show that it is worth packaging?

# Workflow

1. Write the working order.
2. List the context sources you need.
3. Clarify the likely outputs.

# Promotion Criteria

- When should it move into `skills/`?
- Which helper folders will be needed?
- Can its representation in adapters be explained without breaking core behavior?
