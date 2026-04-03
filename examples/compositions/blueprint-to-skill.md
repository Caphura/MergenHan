# Blueprint'ten Skill'e Terfi Ornegi

Bu belge, okunur bir skill taslaginin nasil paketlenmis bir beceriye donustugunu ozetler.

## Kaynak Blueprint

- [`prompts/skill-blueprints/prompt-library-curator.md`](../../prompts/skill-blueprints/prompt-library-curator.md)

## Paketlenmis Skill

- [`skills/prompt-library-curator/SKILL.md`](../../skills/prompt-library-curator/SKILL.md)
- [`skills/prompt-library-curator/meta.yaml`](../../skills/prompt-library-curator/meta.yaml)

## Donusum Mantigi

1. Blueprint icindeki davranis tanimi korunur.
2. Codex tarafinda tetikleme icin sade bir `SKILL.md` yazilir.
3. Versiyon, durum, etiket ve kaynak baglantisi `meta.yaml` icine tasinir.
4. Gerekli ayrintilar yardimci kaynaklara bolunur.

## Neden Bu Ayrim?

- `SKILL.md` kullanima odakli kalir.
- Yonetisim bilgisi kaybolmaz.
- Ayni davranisin yazili taslagi ile paketlenmis surumu birlikte izlenebilir.
