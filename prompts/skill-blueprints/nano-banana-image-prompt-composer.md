---
id: mh-blueprint-nano-banana-image-prompt-composer
title: Nano Banana Image Prompt Composer
type: blueprint
status: stable
version: 1.0.0
summary: Kisa ama etkili soru akisiyla kullanicinin gorsel fikrini netlestirip Nano Banana icin kopyalanabilir nihai prompta donusturen paketlenmeye aday taslak.
tags:
  - image-generation
  - prompt-composition
  - visual-direction
  - nano-banana
  - workflow
depends_on:
  - mh-master-nano-banana-image-prompt-composer
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
input_contract: Kullanici yari tanimli bir gorsel fikir verir ve bunu Nano Banana icin temiz, uygulanabilir ve kopyalanabilir bir image prompta donusturmek ister.
output_contract: Kisa yonlendirici soru turleri, netlestirilmis sahne ozeti, tek parca nihai Nano Banana promptu ve gerekiyorsa ince ayar varyasyonlari.
notes: Gemini ve ChatGPT uzerinde dogrudan kullanimda dogrulanmis, gorsel uretmeden metin promptu veren davranis taslagi. Skill paketine terfi karari icin farkli gorsel kategori orneklerinde ek kullanim faydali olur.
---

# Responsibility

Belirsiz veya eksik tarif edilmis gorsel fikirleri, kullaniciyi yormayan kisa bir netlestirme akisindan gecirip Nano Banana icin yuksek kaliteli nihai prompt haline getirmek.

# Trigger Signals

- "Bana Nano Banana icin prompt yaz."
- "Bu gorsel fikrini netlestir."
- "Bana once dogru sorulari sor, sonra image promptu ver."
- "Bir sahne fikrim var, bunu gorsel prompta donustur."
- "Gorseli sen uretme, sadece promptu yaz."

# Workflow

1. Kullanicinin ilk sahne fikrini kisa bicimde yeniden ifade et ve temel yonu dogrula.
2. Sonuca en cok etki edecek eksik alanlari ayikla: sahne, isik, stil, kadraj, atmosfer, gercekcilik seviyesi ve istenmeyen detaylar.
3. Mumkun oldugunca 2-4 arasi yuksek etkili soru sor; kullaniciyi uzun anketle yorma.
4. Kritik belirsizlikler kapandiginda yeni soru acma; ayni cevapta nihai prompta gec.
5. Sonucu taranabilir duzende ver: sahne ozeti, Nano Banana promptu, ince ayar notlari ve istege bagli varyasyonlar.
6. Ortam gorsel uretebiliyor olsa bile varsayilan davranisi metin cikti olarak koru; kullanici acikca istemedikce gorsel uretme veya arac tetikleme.

# Output Expectations

- Kullanicinin hedefini kisa ve dogru anladigini gosteren bir sahne ozeti olmali.
- Kod blogu icindeki prompt kismi dogrudan kopyalanabilir olmali.
- Prompt; ozne, ortam, isik, kompozisyon, stil ve atmosferi tek akista birlestirmeli.
- Gereksiz uzunluk, anlamsiz kalite sloganlari veya kopya artist listeleriyle sisirilmemeli.
- Varsa negatif yonlendirmeler kisa ve islevsel tutulmali.
- Kullanici sadece prompt istiyorsa ek analiz uzatilmamali.

# Promotion Criteria

- Farkli gorsel kategori orneklerinde de tutarli calisiyor olmali: manzara, portre, urun, fantastik sahne, ic mekan gibi.
- Soru sayisi ve soru secimi tekrar tekrar dengeli sonuc veriyor olmali.
- "Metin promptu ver, gorseli uretme" guardrail'i farkli runtime'larda da guvenilir kalmali.
- Nihai cikti farkli adapterlerde kolayca temsil edilebilmeli ve provider-specific syntax'a asiri baglanmamali.
- Kullanici talep sinyalleri yeterince tekrar ediyorsa `skills/` altinda paketlenmeye hazir sayilabilir.
