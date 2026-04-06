---
name: real-estate-valuation-session-composer
description: Use when a user wants the right evidence-first real-estate valuation session selected before running market, comparable, valuation, risk, or investment analysis.
---

# Real Estate Valuation Session Composer

## Use When

- Kullanici bir gayrimenkul, listing grubu veya bolge icin valuation ya da piyasa yorumu istediginde
- Once correct real-estate analysis oturumunun secilmesi, sonra kopyala-paste bir acilis mesaji verilmesi gerektiginde
- Veri kalitesi, emsal tabanli valuation, investment decisioni veya tam disiplinli analysis arasinda uygun kompozisyon secimi beklendiginde
- Governance katmaninin required olarak korunmasi gereken real-estate arastirmasi requestlerinde

## Workflow

1. Kullanici talebinin asil amacini belirle; veri tarama, emsal valuation, investment decisioni veya tam disiplinli analysis olup olmadigini separate.
2. `Real Estate No Hallucination Governance` modulunu required aktif tut.
3. Uygun session composition'i sec:
   - `Core + Real Estate Market Data Validation + Real Estate No Hallucination Governance`
   - `Core + Real Estate Market Data Validation + Real Estate Comparable Analysis + Real Estate Valuation Logic + Real Estate Risk and Uncertainty + Real Estate No Hallucination Governance`
   - `Core + Real Estate Market Data Validation + Real Estate Comparable Analysis + Real Estate Valuation Logic + Real Estate Risk and Uncertainty + Real Estate Investment Decision Support + Real Estate No Hallucination Governance`
   - tam disiplinli analysis kompozisyonu
4. Sonucu taranabilir yapida ver: session goal, aktif modules, neden bu kompozisyon ve copy-paste session opening.
5. Analizi user yerine tamamlamaya working; once correct evidence-first session setup'ini ver.
6. Cikti boyunca veri, assumption, tahmin ve bilinmeyen ayrimini vurgula.

## Output Expectations

- Governance modulunun aktif oldugu explicitly yazilmali.
- Session goal tek cumlede net olmali.
- Hangi modullerin aktif oldugu correct ve eksiksiz secilmis olmali.
- `Why This Composition` secimi short ve mantikli bicimde aciklamali.
- `Copy-Paste Session Opening` gercekten kullanilabilir olmali ve false certaintyten kacinma davranisini yansitmali.

## References

- Short test oturumu example icin `examples/session-example.md` dosyasina bak.

## Portability Notes

- This skill'in core davranisi provider-agnostiktir.
- Runtime'a specific session acilisi, proje talimati veya tool secimi adapter katmaninda belgelenmelidir.
- Varsaylisting task tam real-estate analysis yapmak degil; correct governance-first analysis oturumunu secmektir.
