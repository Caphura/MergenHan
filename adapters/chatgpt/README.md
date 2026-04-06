# ChatGPT Adapter

This folder explains how MergenHan core content can be used in ChatGPT projects, Custom GPT-like setups, or manual prompt-injection workflows.

## Scope

- project instructions and similar persistent context
- Custom GPT style packaging notes
- manual copy-paste usage flows
- how a core skill or blueprint is carried into a ChatGPT session

## Examples

- [`mapping.md`](./mapping.md): how a core asset is represented in ChatGPT
- [`project-instructions-example.md`](./project-instructions-example.md): a short project-instructions example
- [`apartment-investment-analyzer-project-instructions-example.md`](./apartment-investment-analyzer-project-instructions-example.md): a short session or project-instructions example for the apartment investment analysis skill
- [`feature-spec-composer-project-instructions-example.md`](./feature-spec-composer-project-instructions-example.md): a short session or project-instructions example for the feature spec skill
- [`nano-banana-project-instructions-example.md`](./nano-banana-project-instructions-example.md): a short session or project-instructions example for the text-only image prompt skill
- [`meshy-3d-prompt-composer-project-instructions-example.md`](./meshy-3d-prompt-composer-project-instructions-example.md): a short session or project-instructions example for the 800-character Meshy 3D prompt skill
- [`resume-composer-project-instructions-example.md`](./resume-composer-project-instructions-example.md): a short session or project-instructions example for the ATS-friendly English resume skill

## Boundary

ChatGPT-specific behavior is not stored in the core. The core definition stays under `prompts/` and `skills/`; runtime-specific usage notes live in this adapter.
