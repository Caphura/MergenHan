---
name: feature-spec-composer
description: Use when a user has a rough or partially defined game feature idea and wants it turned into a structured, reusable feature specification.
---

# Feature Spec Composer

## Use When

- Kullanici daginik veya yari tanimli bir oyun ozelligi fikrini feature spec'e donusturmek istediginde
- Bir mekanigin kurallari, edge case'leri veya acceptance criteria'si net olmadiginda
- Ekipte paylasilabilir, taranabilir ve profesyonel bir feature dokumani gerektiğinde
- Fikrin tasarim amacini, oyuncu deneyimini ve sistem davranisini ayristirmak istediginde

## Workflow

1. Ozellik fikrini ve mevcut netlik seviyesini anla; hangi kisimlarin tanimli, hangilerinin belirsiz oldugunu ayristir.
2. Eksik, zayif veya celiskili kisimlari gorunur yap; amac, kapsam, oyuncu etkisi ve kurallar tarafindaki belirsizlikleri acikca listele.
3. Feature'in amacini, oyuncu icin degerini ve hangi problemi cozmeye calistigini netlestir.
4. Sonucu yapisal feature spec formatina donustur: ozet, hedefler, oyuncu deneyimi, fonksiyonel tanim ve kurallar bolumlerini doldur.
5. Edge case, dependency ve open question kisimlarini ayir; hangi kosulda ne olacagini belirsiz birakma.
6. Acceptance criteria ile bitir; feature'in ne zaman "yeterince net" sayilacagini test edilebilir bicimde yaz.

## Output Expectations

- Cikti `Feature Summary`, `Design Goals`, `Player Experience`, `Functional Description`, `Rules and Logic`, `UI / UX Notes`, `Technical / Implementation Notes`, `Edge Cases`, `Dependencies`, `Open Questions`, `Acceptance Criteria` basliklarini icermeli.
- `Technical / Implementation Notes` yuksek seviyede kalmali; detayli engineering gorev dagilimina donusmemeli.
- Belirsizlikler gizlenmemeli; gerekiyorsa varsayim veya acik soru olarak isaretlenmeli.
- Acceptance criteria somut ve test edilebilir olmali.

## References

- Kisa test oturumu ornegi icin `examples/session-example.md` dosyasina bak.

## Portability Notes

- Bu skill'in cekirdek davranisi provider-agnostiktir.
- Runtime'a ozel oturum acilisi, proje talimati veya tool secimi adapter katmaninda belgelenmelidir.
- Varsayilan gorev feature fikrini yapisal dokumantasyona donusturmektir; tam teknik uygulama plani yazmak degil.
