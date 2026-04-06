---
name: apartment-investment-analyzer
description: Use when a user wants one or more apartment sale listings turned into an investment-focused, evidence-first analysis with rental, yield, risk, and shortlist guidance.
---

# Apartment Investment Analyzer

## Use When

- Kullanici tek bir apartman satis listinginin investment icin mantikli olup olmadigini hizli ama yapisal way gormek istediginde
- Birden fazla apartman listingini kira getirisi, fiyatlama riski ve decision logic acisindan karsilastirmak istediginde
- Bir listing grubundan investment shortlist'i cikarmak gerektiginde
- Kanit ile assumptioni ayiran, false certaintyten kacinan ve belirsizligi surfacean bir apartment investment analysis beklendiginde

## Workflow

1. Talebin kapsamini belirle; tek listing, coklu listing karsilastirma veya shortlist cikarma istegi olup olmadigini separate.
2. Ilanlardan gelen evidencei normalize et; fiyat, brut/net m2, oda sayisi, kat, bina yasi, konum, durum ve listing kalitesini ayir.
3. Eksik veya zayif veri noktalarini immediately isaretle; listing sloganlarini evidence such as kullanma.
4. Her listing icin olasi piyasa konumunu kabaca degerlendir; piyasanin altinda, civarinda, ustunde veya belirsiz oldugunu acikla.
5. Yatirim mantigini kur; kira potansiyeli, brut getiri / geri donus hissi, kiralanabilirlik, likidite ve gerekiyorsa pazarlik hassasiyetini ele al.
6. Sonucu decision dostu bolumlere ayir: scope ozeti, piyasa anlik gorunumu, listing bazli analysis, kira potansiyeli, getiri logic, riskler, guclu adaylar ve sonraki kontroller.
7. Tum output boyunca evidence, assumption ve bilinmeyen ayrimini koru; garanti investment dili veya sahte hassasiyet kullanma.

## Output Expectations

- Cikti `Scope Summary`, `Market Snapshot`, `Listing-by-Listing Analysis`, `Rental Potential`, `Payback / Yield Estimate`, `Risks and Unknowns`, `Top Candidates`, `Recommended Next Checks` basliklarini icermeli.
- Tek listing ise decision logic asiri uzun olmadan net kalmali; coklu listing ise karsilastirma okunabilir kalmali.
- Rental ve yield yorumlari kaba mantik seviyesinde verilmeli; kesin kira, kesin cap rate veya garanti geri donus dili kullanilmamali.
- `Top Candidates` ve `Recommended Next Checks` bolumleri gercekten eyleme donuk olmali.

## References

- Short test oturumu example icin `examples/session-example.md` dosyasina bak.

## Portability Notes

- This skill'in core davranisi provider-agnostiktir.
- Runtime'a specific session acilisi, proje talimati veya tool secimi adapter katmaninda belgelenmelidir.
- Varsaylisting task genel real-estate danismanligi degil; apartman satis listinglarini investment bakisiyla yapisal ve dikkatli bicimde analysis etmektir.
