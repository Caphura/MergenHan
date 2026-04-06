# Blueprint'ten Skill'e Terfi Ornegi

This document okunur bir skill taslaginin how paketlenmis bir beceriye donustugunu summarizes.

## Kaynak Blueprint

- [`prompts/skill-blueprints/prompt-library-curator.md`](../../prompts/skill-blueprints/prompt-library-curator.md)

## Paketlenmis Skill

- [`skills/prompt-library-curator/SKILL.md`](../../skills/prompt-library-curator/SKILL.md)
- [`skills/prompt-library-curator/meta.yaml`](../../skills/prompt-library-curator/meta.yaml)

## Donusum Mantigi

1. Blueprint icindeki davranis tanimi is preserved.
2. Runtime-agnostik, sade bir `SKILL.md` is written.
3. Versiyon, durum, etiket ve source baglantisi `meta.yaml` icine tasinir.
4. Gerekli ayrintilar yardimci kaynaklara bolunur.
5. Runtime'a specific usage notlari if needed `adapters/` altina tasinir.

## Neden Bu Ayrim?

- `SKILL.md` usagea odakli remains.
- Yonetisim bilgisi kaybolmaz.
- Ayni davranisin yazili taslagi ile paketlenmis surumu birlikte traceable.
- Claude Code, ChatGPT, Codex ve generic LLM eslemeleri cekirdegi bozmadan ayrica tanimlanabilir.
