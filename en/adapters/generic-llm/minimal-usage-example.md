# Generic LLM Minimal Usage Example

This example specific runtime ozelligi olmayan bir LLM ortaminda core bir skill'in minimum contextla how kullanilabilecegini shows.

## Core Sources

- [`skills/prompt-library-curator/SKILL.md`](../../skills/prompt-library-curator/SKILL.md)
- [`skills/prompt-library-curator/meta.yaml`](../../skills/prompt-library-curator/meta.yaml)

## Minimal Usage

1. `SKILL.md` icerigini oturuma ekleyin.
2. Gerekirse `meta.yaml` icinden dependency ve source blueprint bilgisini ozetleyin.
3. Asagidaki such as basit bir istem kullanin:

```text
Use the core behavior from MergenHan's `prompt-library-curator` skill.
Organize the provided repository content into the correct type: master, module, blueprint, or skill.
Preserve existing IDs and dependency chains unless there is a real inconsistency.
Keep runtime-specific assumptions out of the core recommendation.
```

## Short Note

Bu en dusuk ortak payda ornegidir; specific vehicle, hook veya permission assumptioni yapmaz.