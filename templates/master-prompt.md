---
id: mh-master-your-slug
title: Your Master Prompt Title
type: master
status: draft
version: 0.1.0
summary: Describe in one sentence what this master prompt achieves.
tags:
  - composition
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

# Goal

Clarify the main job this prompt is responsible for.

# Assembly Map

- List which modules you use and why.
- This section should help another person understand the prompt quickly.

# Prompt Body

Write the actual master prompt text here.

# Maintenance Notes

- In which cases should pieces be extracted into modules?
- When should this be archived?
- Move runtime-specific notes into `adapters/` instead of the core prompt.
