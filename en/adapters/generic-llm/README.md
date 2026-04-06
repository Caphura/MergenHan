# Generic LLM Adapter

This folder defines the minimum portable usage shape for any LLM environment that does not provide runtime-specific features.

## Scope

- plain-text prompt usage scenarios
- manual context collection and injection
- the minimum working form of core content in environments without tool or hook support

## Examples

- [`mapping.md`](./mapping.md): how a core asset is represented in a generic LLM environment
- [`minimal-usage-example.md`](./minimal-usage-example.md): the shortest usage example

## Boundary

This adapter behaves as if no runtime-specific capabilities exist. That keeps MergenHan core content usable even at the lowest common denominator.
