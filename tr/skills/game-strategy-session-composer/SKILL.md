---
name: game-strategy-session-composer
description: Use when a user wants the right game-evaluation session setup selected before running a Steam, MVP, risk, or full strategic review.
---

# Game Strategy Session Composer

## Use When

- Kullanici bir oyun fikrini belirli bir stratejik amacla degerlendirmek istediginde
- Once dogru analiz oturumunun secilmesi, sonra kopyala-yapistir bir acilis mesaji uretilmesi gerektiginde
- Steam potansiyeli, MVP indirgeme, production risk veya tam greenlight odakli session secimi istendiginde
- Gerektiginde daha sert ve ticari gercekcilik odakli bir ust katman eklenmesi beklendiginde

## Workflow

1. Kullanici talebinin asil amacini belirle; market, MVP, risk, tam stratejik degerlendirme veya bunlarin kombinasyonu olup olmadigini ayristir.
2. Uygun session composition'i sec:
   - `Core + Steam Market Validation + Full Concept Greenlight`
   - `Core + MVP Scope Reduction`
   - `Core + Production Risk Strategy`
   - `Core + Steam Market Validation + MVP Scope Reduction + Production Risk Strategy + Full Concept Greenlight`
3. Gerekiyorsa sert mod ust katmanini ekle.
4. Sonucu taranabilir yapida ver: session goal, aktif moduller, neden bu kompozisyon ve copy-paste session opening.
5. Analizi kullanici yerine tamamlamaya calisma; once dogru oturum setup'ini ver.

## Output Expectations

- Session goal tek cumlede acik olmali.
- Hangi modullerin aktif oldugu net ve dogru secilmis olmali.
- `Why This Composition` bolumu secimin nedenini kisa ve mantikli aciklamali.
- `Copy-Paste Session Opening` gercekten kullanilabilir, dogrudan AI oturumuna yapistirilabilir olmali.
- Gerektiginde sert mod ust katmani eklenmeli, gerekmiyorsa zorlanmamalidir.

## References

- Kisa test oturumu ve secim kalibi icin `examples/session-example.md` dosyasina bak.

## Portability Notes

- Bu skill'in cekirdek davranisi provider-agnostiktir.
- Runtime'a ozel proje talimati, task packet veya oturum acilis bicimi adapter katmaninda belgelenmelidir.
- Varsayilan gorev tam analiz yapmak degil; dogru analiz oturumunu best-fit composition olarak secmektir.
