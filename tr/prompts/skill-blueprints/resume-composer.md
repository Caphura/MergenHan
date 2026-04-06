---
id: mh-blueprint-resume-composer
title: Resume Composer
type: blueprint
status: stable
version: 1.1.0
summary: Mevcut resume / CV, ham kariyer notlari ve inspectable kanitlari okuyup; gerekirse tek kisa netlestirme turu acarak ATS-friendly, evidence-only, role-aware ve gerektiginde one-page veya export-review odakli Ingilizce resume ciktilari ureten stabilize edilmis taslak.
tags:
  - positioning
  - guidance
  - workflow
  - readability
  - evidence
  - validation
depends_on:
  - mh-module-context-audit
  - mh-module-collaborative-guidance
  - mh-module-action-summary
last_reviewed: 2026-04-04
portability: universal
adapter_support:
  claude-code: supported
  chatgpt: supported
  codex: supported
  generic-llm: supported
runtime_dependencies: []
tool_dependencies: []
input_contract: Kullanici mevcut resume / CV metni, ham kariyer notlari, ekran goruntuleri, public kaynaklar, local artifact'lar veya bunlara ek bir job post vererek guclu, ATS-friendly ve evidence-only bir resume taslagi, one-page surum veya export review ister.
output_contract: Gerekirse tek kisa netlestirme turu, Candidate Summary, job post varsa Target Role Fit, ATS-friendly Resume Draft, Weak Spots / Missing Inputs ve gerekiyorsa Optional Tailoring Notes. Review modunda findings-first audit de desteklenir.
notes: Varsayilan dil EN-firsttir. Job post varsa tailoring aktif olur; yoksa domain'e uygun baseline uretilir. Uydurma metric, title, tarih, ownership, degree veya teknoloji eklenmez; inspectable evidence sorudan once kullanilir ve export artifact'lari ayrica denetlenir.
---

# Responsibility

Mevcut resume / CV, daginik kariyer notlari veya inspectable evidence paketlerini; ATS-friendly ama insan okunur, evidence-only ve role-aware bir resume ciktiya donusturmek.

# Trigger Signals

- "CV'mi / resume'mi duzelt."
- "Bu role gore resume'mi tailor et."
- "Ham kariyer notlarimdan guclu bir resume cikart."
- "Bullet'larimi daha etkili hale getir ama uydurma bilgi ekleme."
- "ATS icin daha iyi bir resume istiyorum."
- "Bu PDF / ekran goruntulerinden resume'i toparla."
- "Bunu tek sayfalik final CV'ye sikistir."
- "Export olmus CV'yi kontrol et; kotu calisan yerleri bul."

# Workflow

1. Gelen girdiyi triage et: mevcut resume mi, ham kariyer notlari mi, inspectable evidence pack mi, yoksa bunlarin karisimi mi oldugunu belirle. Ayrica kullanicinin draft, section rewrite, one-page final, tailoring veya export review isteyip istemedigini ayristir.
2. Kullanici inspectable materyal verdiyse once onu tara: ekran goruntuleri, PDF exportlar, repo readme'leri, local dokumanlar, public profil / haber linkleri, onceki draftlar. Kanit zaten gorulebilir durumdaysa gereksiz netlestirme sorma.
3. Evidence tiering uygula: `user-asserted`, `screenshot-or-document-verified`, `local-artifact-verified`, `public-source-verified`, `inferred`. Final copy'yi sertlestirirken bu farki koru; kesin olmayan seyi verified gibi yazma.
4. Hedef sonucu etkileyen kritik eksikleri ayikla: target role, seniority, title progression, somut basarilar, metric'ler, tarih araliklari, ownership, teknik stack, domain positioning ve egitim kesinligi.
5. Girdi hala kritik derecede eksikse varsayilan olarak en fazla 1 kisa tur ac ve 2-4 yuksek etkili soru sor. Uzun anket acma; inspectable kanittan zaten cikabilecek seyi tekrar isteme.
6. Sonraki adimda evidence-only bullet rewrite yap: action, ownership ve outcome mantigini koru; net olmayan bilgileri guclendir ama uydurma metrik, degree, title, teknoloji veya ownership ekleme.
7. Domain'e uygun positioning sec: game / technical / product / operations / research gibi baglama gore ozel baseline kullan. Kullaniciyi otomatik olarak generic white-collar profile'a zorlama.
8. ATS-friendly section drafting yap: Candidate Summary, core strengths / skills, experience bullets ve varsa education / certification iskeletini taranabilir kur.
9. Job post varsa tailoring uygula: yalnizca desteklenen keyword ve sorumluluklara yaslan, keyword spam yapma ve eksik esitlikleri zorla uydurma.
10. Talep one-page final ise en guclu sinyalleri onde tut, tekrarli maddeleri buda, stacked-role progression'i koru ve gercekten tek sayfaya uygun bir copy uret.
11. Talep export review ise placeholder contact bilgileri, unsupported degree claims, generic filler, merged satirlar, ATS'i bozacak layout copy sorunlari ve evidence drift icin findings-first audit yap.
12. Sonucu su yapida ver: Candidate Summary, job post varsa Target Role Fit, Resume Draft, Weak Spots / Missing Inputs ve gerekiyorsa Optional Tailoring Notes. Review modunda once findings'i ver, sonra gerekiyorsa duzeltme yonu belirt.
13. Varsayilan cikti Ingilizce olsun; kullanici acikca baska dil istemedikce final drafti English yaz. Gerekirse netlestirme sorulari kullanicinin diline uyumlu olabilir.
14. Kullanicinin "beni guclu goster" baskisina ragmen uydurma basari, degree, title veya metric yazma; missing / unclear alanlari acikca belirt.

# Output Expectations

- Resume Draft varsayilan olarak concise ATS-friendly professional resume tonunda olmali.
- Final bullet'lar sonuc, etki ve ownership odakli olmali; gorev listesi gibi dagilmamali.
- Job post varsa tailoring gorunur olmali; yoksa domain'e uygun baseline korunmali.
- Candidate Summary kisa, pozisyonlama odakli ve gereksiz sloganlardan uzak olmali.
- Target Role Fit bolumu yalnizca job post veya net target role verildiginde cikmali.
- Weak Spots / Missing Inputs bolumu gercekten eksik veri, zayif metric, net olmayan ownership veya dusuk guvenli claim alanlarini gostermeli.
- Keyword optimizasyonu readability'yi bozacak keyword spam'e donusmemeli.
- Kullanici sadece belirli bir bolumu istiyorsa scope'u gereksiz yere genisletme; ama varsayilan tam draft mantigini koru.
- Teknik, oyun, builder veya project-led profillerde en guclu ispat eksenlerini generic corporate filler ile seyreltme.
- One-page mode tekrarli maddeleri ve ikincil detaylari budamali; final copy taranabilir ve gercekten kisa olmali.
- Export-review mode placeholder adres / telefon, unsupported degree, merged satirlar ve drift eden claim'leri kirmizi bayrak saymali.

# Failure Patterns To Avoid

- Placeholder adres, telefon veya dummy contact bilgilerini finalde birakmak
- Belirsiz egitim sinyalini dogrulanmis degree olarak yazmak
- Takim etiketi, showcase veya fotograf gorunurlugunu unsupported resmi title / employment claim'e sisirmek
- Teknik veya oyun odakli profili generic corporate summary'ye indirmek
- Stacked-role progression'i kaybetmek veya rolleri tek satirda ezmek
- Canva / PDF export kaynakli merged copy veya layout artifact'larini fark etmemek

# Promotion Criteria

- Mevcut resume + job post, ham not + no job post ve eksik veri gibi farkli senaryolarda tutarli sonuc veriyor olmali.
- En fazla 1 kisa netlestirme turuyle anlamli ilerleme sagliyor olmali.
- Uydurma veri eklememe guardrail'i farkli runtime'larda da guvenilir kalmali.
- Job-post-guided tailoring ile general baseline modu birbirinden net ayrisiyor olmali.
- Ekran goruntusu + public source + local artifact gibi karisik kanitlardan resume reconstruct edebilmeli.
- One-page compression modunda guclu sinyalleri korurken copy'yi kisa tutabilmeli.
- Export review modunda placeholder, unsupported claim ve merged copy sorunlarini yakalayabilmeli.
- Skill paketi ve adapter ornekleri uzerinden baska runtime'lara tasinmasi kolay olmali.

