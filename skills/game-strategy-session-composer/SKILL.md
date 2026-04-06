---
name: game-strategy-session-composer
description: Use when a user wants the right game-evaluation session setup selected before running a Steam, MVP, risk, or full strategic review.
---

# Game Strategy Session Composer

## Use When

- Kullanici bir oyun fikrini belirli bir stratejik amacla degerlendirmek istediginde
- Once correct analysis oturumunun secilmesi, sonra kopyala-paste bir acilis mesaji uretilmesi gerektiginde
- Steam potansiyeli, MVP indirgeme, production risk veya tam greenlight odakli session secimi istendiginde
- Gerektiginde daha sert ve ticari gercekcilik odakli bir ust katman eklenmesi beklendiginde

## Workflow

1. Kullanici talebinin asil amacini belirle; market, MVP, risk, tam stratejik evaluation veya bunlarin kombinasyonu olup olmadigini separate.
2. Uygun session composition'i sec:
   - `Core + Steam Market Validation + Full Concept Greenlight`
   - `Core + MVP Scope Reduction`
   - `Core + Production Risk Strategy`
   - `Core + Steam Market Validation + MVP Scope Reduction + Production Risk Strategy + Full Concept Greenlight`
3. Gerekiyorsa sert mod ust katmanini ekle.
4. Sonucu taranabilir yapida ver: session goal, aktif modules, neden bu kompozisyon ve copy-paste session opening.
5. Analizi user yerine tamamlamaya working; once correct session setup'ini ver.

## Output Expectations

- Session goal tek cumlede clear olmali.
- Hangi modullerin aktif oldugu net ve correct secilmis olmali.
- `Why This Composition` bolumu secimin nedenini short ve mantikli aciklamali.
- `Copy-Paste Session Opening` gercekten kullanilabilir, directly AI oturumuna yapistirilabilir olmali.
- Gerektiginde sert mod ust katmani eklenmeli, gerekmiyorsa zorlanmamalidir.

## References

- Short test oturumu ve secim kalibi icin `examples/session-example.md` dosyasina bak.

## Portability Notes

- This skill'in core davranisi provider-agnostiktir.
- Runtime'a specific proje talimati, task packet veya session acilis format adapter katmaninda belgelenmelidir.
- Varsaylisting task tam analysis yapmak degil; correct analysis oturumunu best-fit composition olarak secmektir.
