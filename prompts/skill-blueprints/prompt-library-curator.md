---
id: mh-blueprint-prompt-library-curator
title: Prompt Library Curator
type: blueprint
status: stable
version: 1.0.0
summary: Prompt kutuphanesini duzenleyen, kategorilendiren ve paketlemeye hazir hale getiren moduler skill taslagi.
tags:
  - packaging
  - documentation
  - governance
depends_on:
  - mh-module-context-audit
  - mh-module-repo-architecture
  - mh-module-action-summary
last_reviewed: 2026-04-03
portability: universal
adapter_support:
  claude-code: supported
  chatgpt: supported
  codex: supported
  generic-llm: supported
runtime_dependencies: []
tool_dependencies: []
input_contract: Master prompt, modul veya skill promptlarini duzenleme, terfi ettirme ya da kataloglama talepleri.
output_contract: Netlestirilmis bilgi mimarisi, guncel kataloglar ve gerekiyorsa skill paketine gecis onerisi.
notes: Bu taslak, davranisi insan tarafindan okunur tutar; paketleme karari verilince `skills/` altina tasinabilir.
---

# Responsibility

Prompt kutuphanesindeki icerikleri dogru turlere ayirmak, bakimi kolay hale getirmek ve olgunlasan davranislari paketlemeye hazirlamak.

# Trigger Signals

- Kullanici promptlarini "saklamak", "duzenlemek", "kataloglamak" veya "skill'e cevirmek" istediginde
- Ayni davranis birden fazla dosyada yinelenmeye basladiginda
- Bir prompt ailesi icin surum, durum ve bagimlilik takibi gerektiginde

# Workflow

1. Mevcut klasor yapisini ve kataloglari tara.
2. Her icerigi `master`, `module`, `blueprint` veya `skill` olarak siniflandir.
3. Eksik metadata, zayif adlandirma veya kayip bagimliliklari tespit et.
4. Gerekirse yeni sablon veya ornek olustur.
5. Skill paketine terfi edecek icerikler icin sade `SKILL.md` ve ayri `meta.yaml` kurgula.
6. Runtime'a ozel kullanim notlari gerekiyorsa bunlari adapter mapping belgelerine tasimayi oner.
7. Sonucu kisa bir aksiyon ozetiyle bitir.

# Promotion Criteria

- Davranis tekrar kullanilir hale gelmis olmali.
- Tetikleyici istek turleri acikca tarif edilebilmeli.
- Gerekli referans veya yardimci dosyalar belli olmali.
- Skill paketine gecince katalog ve README tarafinda bulunabilirlik bozulmamali.
- Cekirdek tanim tek bir runtime'in komut modeline bagli kalmamali.
