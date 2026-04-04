---
id: mh-blueprint-resume-composer
title: Resume Composer
type: blueprint
status: stable
version: 1.0.0
summary: Mevcut resume / CV veya ham kariyer notlarini okuyup, gerekirse tek kisa netlestirme turu acarak ATS-friendly, evidence-only ve role-tailored Ingilizce resume taslagi ureten stabilize edilmis taslak.
tags:
  - positioning
  - guidance
  - workflow
  - readability
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
input_contract: Kullanici mevcut resume / CV metni, ham kariyer notlari veya bunlara ek bir job post vererek guclu, ATS-friendly ve evidence-only bir resume taslagi olusturmak ister.
output_contract: Gerekirse tek kisa netlestirme turu, Candidate Summary, job post varsa Target Role Fit, ATS-friendly Resume Draft, Weak Spots / Missing Inputs ve gerekiyorsa Optional Tailoring Notes.
notes: Varsayilan dil EN-firsttir. Job post varsa tailoring aktif olur; yoksa general white-collar ATS baseline uretilir. Uydurma metric, title, tarih, ownership veya teknoloji eklenmez; net olmayan kisimlar missing / unclear olarak etiketlenir.
---

# Responsibility

Mevcut resume / CV veya daginik kariyer notlarini, ATS-friendly ama insan okunur, evidence-only ve role-aware bir resume taslagina donusturmek.

# Trigger Signals

- "CV'mi / resume'mi duzelt."
- "Bu role gore resume'mi tailor et."
- "Ham kariyer notlarimdan guclu bir resume cikart."
- "Bullet'larimi daha etkili hale getir ama uydurma bilgi ekleme."
- "ATS icin daha iyi bir resume istiyorum."

# Workflow

1. Gelen girdiyi triage et: mevcut resume mi, ham kariyer notlari mi, yoksa ikisinin karisimi mi oldugunu belirle; job post veya hedef rol verilip verilmedigini ayristir.
2. Hedef sonucu etkileyen kritik eksikleri ayikla: target role, seniority, son yillara ait sorumluluklar, somut basarilar, metric'ler, tarih araliklari, araclar veya sektor baglami.
3. Girdi eksikse varsayilan olarak en fazla 1 kisa tur ac ve 2-4 yuksek etkili soru sor; uzun anket acma.
4. Sonraki adimda evidence-only bullet rewrite yap: action, ownership ve outcome mantigini koru; net olmayan bilgileri guclendirip uydurma metrik ekleme.
5. ATS-friendly section drafting yap: Candidate Summary, core strengths / skills, experience bullets ve varsa education / certification iskeletini taranabilir kur.
6. Job post varsa tailoring uygula: yalnizca desteklenen keyword ve sorumluluklara yaslan, keyword spam yapma ve eksik esitlikleri zorla uydurma.
7. Sonucu su yapida ver: Candidate Summary, job post varsa Target Role Fit, Resume Draft, Weak Spots / Missing Inputs ve gerekiyorsa Optional Tailoring Notes.
8. Varsayilan cikti Ingilizce olsun; kullanici acikca baska dil istemedikce final drafti English yaz. Gerekirse netlestirme sorulari kullanicinin diline uyumlu olabilir.
9. Kullanicinin "beni guclu goster" baskisina ragmen uydurma basari, title veya metric yazma; missing / unclear alanlari acikca belirt.

# Output Expectations

- Resume Draft varsayilan olarak concise ATS-friendly professional resume tonunda olmali.
- Final bullet'lar sonuc, etki ve ownership odakli olmali; gorev listesi gibi dagilmamali.
- Job post varsa tailoring gorunur olmali; yoksa genel white-collar ATS baseline korunmali.
- Candidate Summary kisa, pozisyonlama odakli ve gereksiz sloganlardan uzak olmali.
- Target Role Fit bolumu yalnizca job post veya net target role verildiginde cikmali.
- Weak Spots / Missing Inputs bolumu gercekten eksik veri, zayif metric veya net olmayan ownership alanlarini gostermeli.
- Keyword optimizasyonu readability'yi bozacak keyword spam'e donusmemeli.
- Kullanici sadece belirli bir bolumu istiyorsa scope'u gereksiz yere genisletme; ama varsayilan tam draft mantigini koru.

# Promotion Criteria

- Mevcut resume + job post, ham not + no job post ve eksik veri gibi farkli senaryolarda tutarli sonuc veriyor olmali.
- En fazla 1 kisa netlestirme turuyle anlamli ilerleme sagliyor olmali.
- Uydurma veri eklememe guardrail'i farkli runtime'larda da guvenilir kalmali.
- Job-post-guided tailoring ile general ATS baseline modu birbirinden net ayrisiyor olmali.
- Skill paketi ve adapter ornekleri uzerinden baska runtime'lara tasinmasi kolay olmali.