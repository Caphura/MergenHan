---
name: feature-spec-composer
description: Use when a user has a rough or partially defined game feature idea and wants it turned into a structured, reusable feature specification.
---

# Feature Spec Composer

## Use When

- Kullanici daginik veya yari tanimli bir oyun ozelligi fikrini feature spec'e donusturmek istediginde
- Bir mekanigin rules, edge case'leri veya acceptance criteria'si net olmadiginda
- Ekipte paylasilabilir, taranabilir ve profesyonel bir feature dokumani gerektiğinde
- Fikrin tasarim amacini, oyuncu deneyimini ve sistem davranisini separatemak istediginde

## Workflow

1. Ozellik fikrini ve mevcut netlik seviyesini anla; hangi kisimlarin tanimli, hangilerinin belirsiz oldugunu separate.
2. Eksik, zayif veya celiskili kisimlari gorunur yap; purpose, scope, oyuncu etkisi ve rules tarafindaki uncertaintyleri explicitly listele.
3. Feature'in amacini, oyuncu icin degerini ve hangi problemi cozmeye calistigini netlestir.
4. Sonucu yapisal feature spec formatina donustur: ozet, hedefler, oyuncu deneyimi, fonksiyonel tanim ve rules bolumlerini doldur.
5. Edge case, dependency ve open question kisimlarini ayir; hangi kosulda what olacagini belirsiz birakma.
6. Acceptance criteria ile bitir; feature'in what zaman "yeterince net" sayilacagini test edilebilir bicimde yaz.

## Output Expectations

- Cikti `Feature Summary`, `Design Goals`, `Player Experience`, `Functional Description`, `Rules and Logic`, `UI / UX Notes`, `Technical / Implementation Notes`, `Edge Cases`, `Dependencies`, `Open Questions`, `Acceptance Criteria` basliklarini icermeli.
- `Technical / Implementation Notes` yuksek seviyede kalmali; detayli engineering task dagilimina donusmemeli.
- Belirsizlikler gizlenmemeli; gerekiyorsa assumption veya clear soru olarak isaretlenmeli.
- Acceptance criteria somut ve test edilebilir olmali.

## References

- Short test oturumu example icin `examples/session-example.md` dosyasina bak.

## Portability Notes

- This skill'in core davranisi provider-agnostiktir.
- Runtime'a specific session acilisi, proje talimati veya tool secimi adapter katmaninda belgelenmelidir.
- Varsaylisting task feature fikrini yapisal documentationa donusturmektir; tam teknik uygulama plani yazmak degil.
