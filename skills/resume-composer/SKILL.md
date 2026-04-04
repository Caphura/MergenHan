---
name: resume-composer
description: Use when a user wants an ATS-friendly English resume drafted, reconstructed, compressed, reviewed, or tailored from resumes, raw notes, screenshots, public evidence, local artifacts, and optionally a job post.
---

# Resume Composer

## Use When

- Kullanici mevcut resume / CV metnini daha guclu ve ATS-friendly hale getirmek istediginde
- Kullanici ham kariyer notlarindan sifirdan English resume taslagi cikarmak istediginde
- Kullanici ekran goruntusu, PDF, repo, profil linki veya daginik kanitlardan resume reconstruct etmek istediginde
- Bir job post'a gore tailoring istendiginde
- Bullet'larin daha sonuc, etki ve ownership odakli yeniden yazilmasi gerektiginde
- Tek sayfalik final resume copy veya nihai export review istenildiginde
- Kullanicinin profili klasik white-collar baseline yerine game, technical, research, builder veya project-led positioning gerektirdiginde

## Workflow

1. Girdinin mevcut resume, ham not, inspectable evidence pack veya hybrid oldugunu ayristir; ayrica istegin draft, final one-page, section rewrite, tailoring veya export review oldugunu belirle.
2. Kullanicinin verdigi inspectable materyalleri once tara: ekran goruntuleri, PDF exportlar, repo readme'leri, local docs, profil linkleri, public sources ve onceki draftlar. Kullanici zaten gorulebilir kanit verdiyse gereksiz netlestirme sorma.
3. Kanitlari tier'la: `user-asserted`, `screenshot-or-document-verified`, `local-artifact-verified`, `public-source-verified`, `inferred`. Final copy'de yalnizca desteklenen iddialari sertlestir; kesinlik onemliyse provenance farkini koru.
4. Kritik eksikleri ayikla: target role, seniority, title progression, somut basari, metric, tarih sinirlari, ownership, teknik stack, domain positioning ve egitim kesinligi.
5. Gercekten gerekiyorsa en fazla 1 kisa turda 2-4 yuksek etkili soru sor; inspectable kanit varsa once ondan maksimum fayda cikarmayi tercih et.
6. Evidence-only bullet rewrite yap; net olmayan bilgileri guclendir ama uydurma metric, degree, title, teknoloji veya ownership ekleme.
7. Domain'e uygun positioning kur: game / technical / product / operations / research gibi baglama gore ozel baseline sec; kullaniciyi varsayilan generic white-collar profile'a zorlama.
8. ATS-friendly section drafting yap ve job post varsa desteklenen keyword / responsibility seviyesinde tailoring uygula.
9. Talep final one-page ise en guclu sinyalleri sikistir, tekrar eden maddeleri kaldir, stacked-role progression'i koru ve taranabilir tek sayfalik copy uret.
10. Talep export review ise placeholder contact bilgileri, unsupported degree claims, generic filler, merged satirlar, ATS'i bozacak layout copy sorunlari ve evidence drift icin audit yap.
11. Sonucu su yapida ver: Candidate Summary, gerekiyorsa Target Role Fit, Resume Draft, Weak Spots / Missing Inputs ve gerekiyorsa Optional Tailoring Notes. Review modunda findings-first davran.
12. Varsayilan final ciktiyi English yaz; kullanici acikca baska dil istemedikce EN-first davranisini koru.

## Output Expectations

- Resume Draft concise ATS-friendly professional resume tonunda olmali.
- Final bullet'lar action, ownership ve outcome mantigini gostermeli.
- Uydurma metric, title, tarih, teknoloji veya ownership eklenmemeli.
- Job post varsa tailoring gorunur olmali; yoksa domain'e uygun genel baseline korunmali.
- Kullanicinin profilinin builder, designer, engineer veya project-led oldugu durumlarda bunu generic corporate summary'ye ezme.
- One-page mode tekrarli maddeleri budamali, gercek guc eksenlerini onde tutmali ve ATS okunurlugunu korumali.
- Export-review mode placeholder adres / telefon, unsupported degree, merged satirlar ve sahte guclendirme izlerini kirmizi bayrak saymali.
- Weak Spots / Missing Inputs bolumu gercek eksikleri acikca gostermeli.
- ATS optimizasyonu readability'yi bozacak keyword spam'e donusmemeli.

## Failure Patterns To Avoid

- Placeholder adres, telefon veya dummy contact bilgilerini finalde birakmak
- Belirsiz egitim sinyalini dogrulanmis degree olarak yazmak
- Takim etiketi, showcase veya fotograf gorunurlugunu unsupported resmi title / employment claim'e sisirmek
- Teknik veya oyun odakli profili generic corporate summary'ye indirmek
- Stacked-role progression'i kaybetmek veya rolleri tek satirda ezmek
- Canva / PDF export kaynakli merged copy veya layout artifact'larini fark etmemek

## References

- Kisa oturum ornegi icin `examples/session-example.md` dosyasina bak.

## Portability Notes

- Bu skill'in cekirdek davranisi provider-agnostiktir.
- Runtime'a ozel document export, formatting veya editor otomasyonu `adapters/` katmaninda belgelenmelidir.
- Varsayilan gorev plain text / markdown English resume taslagi uretmektir; tasarim araci entegrasyonu cekirdek davranisin parcasi degildir.
