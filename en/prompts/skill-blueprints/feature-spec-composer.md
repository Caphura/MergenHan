---
id: mh-blueprint-feature-spec-composer
title: Feature Spec Composer
type: blueprint
status: stable
version: 1.0.0
summary: Daginik veya yari tanimli oyun ozelligi fikirlerini profesyonel, tekrar kullanilabilir ve clear feature specification yapisina donusturen game design odakli draft.
tags:
  - game-design
  - feature-design
  - documentation
  - workflow
depends_on:
  - mh-module-context-audit
  - mh-module-collaborative-guidance
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
input_contract: Ham, eksik veya yari tanimli bir oyun ozelligi fikrini aciklastirma ve bunu yapisal feature spec formatina donusturme istegi.
output_contract: Feature Summary, Design Goals, Player Experience, Functional Description, Rules and Logic, UI / UX Notes, Technical / Implementation Notes, Edge Cases, Dependencies, Open Questions ve Acceptance Criteria bolumlerini iceren taranabilir feature specification.
notes: This blueprint feature fikrini yapisal documentationa turns into; tam GDD, lore writing veya uygulama odakli teknik tasarim sistemi yerine net feature davranisina odaklanir. Farkli AI ortamlari uzerindeki denemelerde basarili sonuc vermistir ve paketlenmeye hazirdir.
---

# Responsibility

Belirsiz veya yarim tanimli bir oyun ozelligi fikrini, oyuncu deneyimi ve tasarim logic clear olan profesyonel bir feature spec haline getirmek.

# Trigger Signals

- "Bu feature fikrini spec'e donustur."
- "Bu mekanigin rules net degil, aciklastir."
- "Bunu ekipte paylasilabilir feature dokumani haline getir."
- "Bu sistemin edge case'lerini ve acceptance criteria'sini yaz."

# Workflow

1. Ozellik fikrini ve mevcut netlik seviyesini anla; hangi kisimlarin zaten tanimli, hangilerinin belirsiz oldugunu separate.
2. Eksik, zayif veya celiskili kisimlari explicitly listele; purpose, scope ve oyuncu etkisi tarafindaki uncertaintyleri gorunur yap.
3. Feature'in amacini, oyuncu icin degerini ve hangi problem veya ihtiyaci cozdugunu netlestir.
4. Ozelligi profesyonel bir spec yapisina donustur: ozet, hedefler, oyuncu deneyimi ve fonksiyonel tanim bolumlerini doldur.
5. Kurallari, durumlari, logic ve edge case'leri aciklastir; hangi kosulda what oldugunu belirsiz birakma.
6. Bagimliliklari ve clear sorulari separate; baska sistemler, UI ihtiyaclari veya veri baglari varsa bunlari surface.
7. Acceptance criteria ve short uygulanabilir ozet ile bitir; feature'in what zaman "yeterince net" sayilacagini explicitly soyle.

# Output Shape

Sonucu mumkun oldugunca su yapida toplula:

- Feature Summary
- Design Goals
- Player Experience
- Functional Description
- Rules and Logic
- UI / UX Notes
- Technical / Implementation Notes
- Edge Cases
- Dependencies
- Open Questions
- Acceptance Criteria

`Technical / Implementation Notes` bolumu only feature davranisini anlamak icin required yuksek seviyeli notlari icermelidir; detayli uygulama plani veya engineering task dagilimi uretmemelidir.

# Promotion Criteria

- Ayni tip "feature fikrini spec'e cevir" ihtiyaci tekrarliyorsa
- Uretilen spec structure different feature'larda da tutarli ve kullanisli kaliyorsa
- Acceptance criteria, edge case ve dependency gorunurlugu tekrar usagea value hale geliyorsa
- Core davranis provider-specific olmadan different adapterlerde temsil edilebiliyorsa
