# Lifecycle

This document defines how content in MergenHan evolves over time. Adapter mapping is not a stage in that lifecycle; it is a separate compatibility layer.

## Two-Axis Model

MergenHan's lifecycle is read across two axes:

- structural type: `module`, `master`, `blueprint`, `skill`
- maturity status: `draft`, `active`, `stable`, `deprecated`, `archived`

This means every asset carries both a type and a maturity state.

## Structural Types

### `module`

- A reusable support unit
- Can be a behavior, constraint, tone, domain-knowledge piece, or output fragment

### `master`

- Orchestrates multiple modules for one task family
- Must clearly show its dependencies

### `blueprint`

- A stabilized skill draft that is a candidate for packaging
- Still remains open to human discussion and refinement

### `skill`

- A packaged, reusable core capability
- Can be mapped into multiple runtimes through adapters

## Maturity States

### `draft`

- Initial draft level
- Open to fast change

### `active`

- Currently used content
- May still be evolving, but it is the preferred version

### `stable`

- Behavior is settled and reused repeatedly
- A good candidate for packaging or broader distribution

### `deprecated`

- Replaced by something better
- Not recommended for new use, but kept for transition

### `archived`

- Preserved as historical reference
- Not deleted; still discoverable

## Typical Transitions Between Types

Common evolution paths include:

- a new reusable behavior begins as a `draft module`
- a flow that combines multiple modules becomes an `active master`
- repeated, packageable task logic becomes a `blueprint`
- a stable blueprint is promoted into a packaged `skill`
- over time, mature assets become `stable`
- if replaced they become `deprecated`, and if kept only for history they become `archived`

## Why Is Adapter Mapping Separate?

Adapter mapping is not a lifecycle stage because it:

- does not change the core asset type
- only carries compatibility information for a specific runtime
- may exist multiple times for the same core asset

So support for `claude-code`, `chatgpt`, `codex`, or `generic-llm` is not a status like `draft` or `stable`; it is a separate compatibility layer.
