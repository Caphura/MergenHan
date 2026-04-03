---
name: apartment-investment-analyzer
description: Use when a user wants one or more apartment sale listings turned into an investment-focused, evidence-first analysis with rental, yield, risk, and shortlist guidance.
---

# Apartment Investment Analyzer

## Use When

- Kullanici tek bir apartman satis ilaninin yatirim icin mantikli olup olmadigini hizli ama yapisal sekilde gormek istediginde
- Birden fazla apartman ilanini kira getirisi, fiyatlama riski ve karar mantigi acisindan karsilastirmak istediginde
- Bir ilan grubundan yatirim shortlist'i cikarmak gerektiginde
- Kanit ile varsayimi ayiran, sahte kesinlikten kacinan ve belirsizligi gorunur kilan bir apartment investment analizi beklendiginde

## Workflow

1. Talebin kapsamini belirle; tek ilan, coklu ilan karsilastirma veya shortlist cikarma istegi olup olmadigini ayristir.
2. Ilanlardan gelen kaniti normalize et; fiyat, brut/net m2, oda sayisi, kat, bina yasi, konum, durum ve ilan kalitesini ayir.
3. Eksik veya zayif veri noktalarini hemen isaretle; ilan sloganlarini kanit gibi kullanma.
4. Her ilan icin olasi piyasa konumunu kabaca degerlendir; piyasanin altinda, civarinda, ustunde veya belirsiz oldugunu acikla.
5. Yatirim mantigini kur; kira potansiyeli, brut getiri / geri donus hissi, kiralanabilirlik, likidite ve gerekiyorsa pazarlik hassasiyetini ele al.
6. Sonucu karar dostu bolumlere ayir: kapsam ozeti, piyasa anlik gorunumu, ilan bazli analiz, kira potansiyeli, getiri mantigi, riskler, guclu adaylar ve sonraki kontroller.
7. Tum cikti boyunca kanit, varsayim ve bilinmeyen ayrimini koru; garanti yatirim dili veya sahte hassasiyet kullanma.

## Output Expectations

- Cikti `Scope Summary`, `Market Snapshot`, `Listing-by-Listing Analysis`, `Rental Potential`, `Payback / Yield Estimate`, `Risks and Unknowns`, `Top Candidates`, `Recommended Next Checks` basliklarini icermeli.
- Tek ilan ise karar mantigi asiri uzun olmadan net kalmali; coklu ilan ise karsilastirma okunabilir kalmali.
- Rental ve yield yorumlari kaba mantik seviyesinde verilmeli; kesin kira, kesin cap rate veya garanti geri donus dili kullanilmamali.
- `Top Candidates` ve `Recommended Next Checks` bolumleri gercekten eyleme donuk olmali.

## References

- Kisa test oturumu ornegi icin `examples/session-example.md` dosyasina bak.

## Portability Notes

- Bu skill'in cekirdek davranisi provider-agnostiktir.
- Runtime'a ozel oturum acilisi, proje talimati veya tool secimi adapter katmaninda belgelenmelidir.
- Varsayilan gorev genel emlak danismanligi degil; apartman satis ilanlarini yatirim bakisiyla yapisal ve dikkatli bicimde analiz etmektir.
