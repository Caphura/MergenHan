# Generic LLM Minimal Usage Example

Bu ornek, ozel runtime ozelligi olmayan bir LLM ortaminda cekirdek bir skill'in minimum baglamla nasil kullanilabilecegini gosterir.

## Core Kaynaklar

- [`skills/prompt-library-curator/SKILL.md`](../../skills/prompt-library-curator/SKILL.md)
- [`skills/prompt-library-curator/meta.yaml`](../../skills/prompt-library-curator/meta.yaml)

## Minimal Kullanim

1. `SKILL.md` icerigini oturuma ekleyin.
2. Gerekirse `meta.yaml` icinden bagimlilik ve kaynak blueprint bilgisini ozetleyin.
3. Asagidaki gibi basit bir istem kullanin:

```text
Use the core behavior from MergenHan's `prompt-library-curator` skill.
Organize the provided repository content into the correct type: master, module, blueprint, or skill.
Preserve existing IDs and dependency chains unless there is a real inconsistency.
Keep runtime-specific assumptions out of the core recommendation.
```

## Kisa Not

Bu en dusuk ortak payda ornegidir; ozel arac, hook veya permission varsayimi yapmaz.