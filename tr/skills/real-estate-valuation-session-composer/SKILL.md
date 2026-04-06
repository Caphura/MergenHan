---
name: real-estate-valuation-session-composer
description: Use when a user wants the right evidence-first real-estate valuation session selected before running market, comparable, valuation, risk, or investment analysis.
---

# Real Estate Valuation Session Composer

## Use When

- Kullanici bir gayrimenkul, ilan grubu veya bolge icin degerleme ya da piyasa yorumu istediginde
- Once dogru emlak analiz oturumunun secilmesi, sonra kopyala-yapistir bir acilis mesaji verilmesi gerektiginde
- Veri kalitesi, emsal tabanli degerleme, yatirim karari veya tam disiplinli analiz arasinda uygun kompozisyon secimi beklendiginde
- Governance katmaninin zorunlu olarak korunmasi gereken emlak arastirmasi taleplerinde

## Workflow

1. Kullanici talebinin asil amacini belirle; veri tarama, emsal degerleme, yatirim karari veya tam disiplinli analiz olup olmadigini ayristir.
2. `Real Estate No Hallucination Governance` modulunu zorunlu aktif tut.
3. Uygun session composition'i sec:
   - `Core + Real Estate Market Data Validation + Real Estate No Hallucination Governance`
   - `Core + Real Estate Market Data Validation + Real Estate Comparable Analysis + Real Estate Valuation Logic + Real Estate Risk and Uncertainty + Real Estate No Hallucination Governance`
   - `Core + Real Estate Market Data Validation + Real Estate Comparable Analysis + Real Estate Valuation Logic + Real Estate Risk and Uncertainty + Real Estate Investment Decision Support + Real Estate No Hallucination Governance`
   - tam disiplinli analiz kompozisyonu
4. Sonucu taranabilir yapida ver: session goal, aktif moduller, neden bu kompozisyon ve copy-paste session opening.
5. Analizi kullanici yerine tamamlamaya calisma; once dogru evidence-first oturum setup'ini ver.
6. Cikti boyunca veri, varsayim, tahmin ve bilinmeyen ayrimini vurgula.

## Output Expectations

- Governance modulunun aktif oldugu acikca yazilmali.
- Session goal tek cumlede net olmali.
- Hangi modullerin aktif oldugu dogru ve eksiksiz secilmis olmali.
- `Why This Composition` secimi kisa ve mantikli bicimde aciklamali.
- `Copy-Paste Session Opening` gercekten kullanilabilir olmali ve sahte kesinlikten kacinma davranisini yansitmali.

## References

- Kisa test oturumu ornegi icin `examples/session-example.md` dosyasina bak.

## Portability Notes

- Bu skill'in cekirdek davranisi provider-agnostiktir.
- Runtime'a ozel oturum acilisi, proje talimati veya tool secimi adapter katmaninda belgelenmelidir.
- Varsayilan gorev tam emlak analizi yapmak degil; dogru governance-first analiz oturumunu secmektir.
