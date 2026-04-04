---
name: resume-composer
description: Use when a user wants an ATS-friendly English resume drafted or tailored from an existing resume, raw career notes, and optionally a job post.
---

# Resume Composer

## Use When

- Kullanici mevcut resume / CV metnini daha guclu ve ATS-friendly hale getirmek istediginde
- Kullanici ham kariyer notlarindan sifirdan English resume taslagi cikarmak istediginde
- Bir job post'a gore tailoring istendiginde
- Bullet'larin daha sonuc, etki ve ownership odakli yeniden yazilmasi gerektiginde

## Workflow

1. Girdinin mevcut resume, ham not veya hybrid oldugunu ayristir; job post veya hedef rol olup olmadigini belirle.
2. Kritik eksikleri ayikla: target role, seniority, somut basari, metric, tarih ve ownership sinirlari.
3. Girdi eksikse en fazla 1 kisa turda 2-4 yuksek etkili soru sor; uzun anket acma.
4. Evidence-only bullet rewrite yap; net olmayan bilgileri guclendirip uydurma veri ekleme.
5. ATS-friendly section drafting yap ve job post varsa desteklenen keyword / responsibility seviyesinde tailoring uygula.
6. Sonucu su yapida ver: Candidate Summary, gerekiyorsa Target Role Fit, Resume Draft, Weak Spots / Missing Inputs ve gerekiyorsa Optional Tailoring Notes.
7. Varsayilan final ciktiyi English yaz; kullanici acikca baska dil istemedikce EN-first davranisini koru.

## Output Expectations

- Resume Draft concise ATS-friendly professional resume tonunda olmali.
- Final bullet'lar action, ownership ve outcome mantigini gostermeli.
- Uydurma metric, title, tarih, teknoloji veya ownership eklenmemeli.
- Job post varsa tailoring gorunur olmali; yoksa temiz genel white-collar baseline korunmali.
- Weak Spots / Missing Inputs bolumu gercek eksikleri acikca gostermeli.
- ATS optimizasyonu readability'yi bozacak keyword spam'e donusmemeli.

## References

- Kisa oturum ornegi icin `examples/session-example.md` dosyasina bak.

## Portability Notes

- Bu skill'in cekirdek davranisi provider-agnostiktir.
- Runtime'a ozel document export, formatting veya editor otomasyonu `adapters/` katmaninda belgelenmelidir.
- Varsayilan gorev plain text / markdown English resume taslagi uretmektir; tasarim araci entegrasyonu cekirdek davranisin parcasi degildir.