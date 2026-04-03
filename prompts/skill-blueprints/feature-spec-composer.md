---
id: mh-blueprint-feature-spec-composer
title: Feature Spec Composer
type: blueprint
status: draft
version: 0.1.0
summary: Daginik veya yari tanimli oyun ozelligi fikirlerini profesyonel, tekrar kullanilabilir ve acik feature specification yapisina donusturen game design odakli taslak.
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
notes: Bu blueprint feature fikrini yapisal dokumantasyona donusturur; tam GDD, lore yazimi veya uygulama odakli teknik tasarim sistemi yerine net feature davranisina odaklanir.
---

# Responsibility

Belirsiz veya yarim tanimli bir oyun ozelligi fikrini, oyuncu deneyimi ve tasarim mantigi acik olan profesyonel bir feature spec haline getirmek.

# Trigger Signals

- "Bu feature fikrini spec'e donustur."
- "Bu mekanigin kurallari net degil, aciklastir."
- "Bunu ekipte paylasilabilir feature dokumani haline getir."
- "Bu sistemin edge case'lerini ve acceptance criteria'sini yaz."

# Workflow

1. Ozellik fikrini ve mevcut netlik seviyesini anla; hangi kisimlarin zaten tanimli, hangilerinin belirsiz oldugunu ayristir.
2. Eksik, zayif veya celiskili kisimlari acikca listele; amac, kapsam ve oyuncu etkisi tarafindaki belirsizlikleri gorunur yap.
3. Feature'in amacini, oyuncu icin degerini ve hangi problem veya ihtiyaci cozdugunu netlestir.
4. Ozelligi profesyonel bir spec yapisina donustur: ozet, hedefler, oyuncu deneyimi ve fonksiyonel tanim bolumlerini doldur.
5. Kurallari, durumlari, mantigi ve edge case'leri aciklastir; hangi kosulda ne oldugunu belirsiz birakma.
6. Bagimliliklari ve acik sorulari ayristir; baska sistemler, UI ihtiyaclari veya veri baglari varsa bunlari gorunur kil.
7. Acceptance criteria ve kisa uygulanabilir ozet ile bitir; feature'in ne zaman "yeterince net" sayilacagini acikca soyle.

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

`Technical / Implementation Notes` bolumu yalnizca feature davranisini anlamak icin gerekli yuksek seviyeli notlari icermelidir; detayli uygulama plani veya engineering gorev dagilimi uretmemelidir.

# Promotion Criteria

- Ayni tip "feature fikrini spec'e cevir" ihtiyaci tekrarliyorsa
- Uretilen spec yapisi farkli feature'larda da tutarli ve kullanisli kaliyorsa
- Acceptance criteria, edge case ve dependency gorunurlugu tekrar kullanima deger hale geliyorsa
- Cekirdek davranis provider-specific olmadan farkli adapterlerde temsil edilebiliyorsa