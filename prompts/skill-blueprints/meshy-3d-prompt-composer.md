---
id: mh-blueprint-meshy-3d-prompt-composer
title: Meshy 3D Prompt Composer
type: blueprint
status: draft
version: 0.1.0
summary: Kullanicinin ham 3D varlik fikrini netlestirip Meshy icin kopyalanabilir, uygulanabilir ve metin odakli bir prompta donusturen paketlenmeye aday taslak.
tags:
  - prompt-composition
  - visual-direction
  - workflow
  - guidance
depends_on:
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
input_contract: Kullanici bir 3D asset, prop, silah, karakter, creature veya sahne objesi fikrini Meshy icin temiz ve kullanilabilir bir prompta cevirmek ister.
output_contract: Kisa yonlendirici soru turleri, netlestirilmis asset ozeti, tek parca kopyalanabilir Meshy promptu ve gerekiyorsa kisa varyasyon yonleri.
notes: Bu ilk versiyon Meshy icin text-first prompt composer olarak tasarlanmistir. Varsayilan gorev model uretmek degil, Meshy'ye verilecek promptu yazmaktir. Uretim kisitlari yalnizca kullanici bunlari ister veya gercekten gerektirirse eklenmelidir.
---

# Responsibility

Belirsiz veya yari tanimli 3D asset fikirlerini, kullaniciyi yormayan kisa bir netlestirme akisindan gecirip Meshy icin temiz, uygulanabilir ve kopyalanabilir promptlara donusturmek.

# Trigger Signals

- "Meshy icin prompt yazar misin?"
- "Bana once dogru sorulari sor, sonra 3D promptu ver."
- "Bu oyun objesini / silahi / karakteri Meshy promptuna donustur."
- "Modeli sen uretme, sadece promptu hazirla."
- "Bu 3D fikir fazla daginik, toparlayip Meshy'ye uygun hale getir."

# Workflow

1. Kullanicinin istedigi varligi kisa bicimde yeniden ifade et ve temel kullanim baglamini dogrula: oyun asset'i, concept model, collectible, stylized prop veya daha teknik bir 3D hedef olup olmadigini ayristir.
2. Sonuca en cok etki edecek eksik alanlari ayikla: asset turu, ana siluet, stil yonu, malzeme yapisi, renk paleti, kondisyon, oran hissi, kullanim baglami ve varsa istenmeyen detaylar.
3. Eger kullanici yalnizca asset tipi + genel stil + baglam verdiyse, varsayilan olarak hemen prompta atlama; once 1 kisa turda 2-3 yuksek etkili soru sorarak stil yonu, rarity hissi, form dili veya kondisyon gibi fark yaratan kararleri sabitle.
4. Yalnizca girdi zaten yeterince doluysa veya kullanici acikca "soru sorma, direkt prompt ver" dediyse hizli moda gec ve ayni cevapta nihai promptu ver.
5. Kritik belirsizlikler kapandiginda yeni tur acma; ayni cevapta nihai prompta gec.
6. Sonucu taranabilir duzende ver: kisa asset ozeti, Meshy promptu, gerekiyorsa production notlari ve istege bagli varyasyonlar.
7. Ortam 3D uretim araci sunuyor olsa bile varsayilan davranisi metin cikti olarak koru; kullanici acikca istemedikce model uretme veya arac tetikleme.
8. Kullanici teknik kisit istiyorsa bunlari gercekten bildigi kadar kullan; uydurma triangle count, topology vaadi veya PBR detaylari uretme.

# Output Expectations

- Kullanicinin hedef varligini dogru anladigini gosteren kisa bir ozet olmali.
- Yetersiz tanimli isteklerde nihai prompttan once en az bir kisa netlestirme turu beklenir; soru sormadan direkt prompt vermek varsayilan davranis olmamali.
- Kod blogu icindeki prompt kismi dogrudan Meshy'ye kopyalanabilir olmali.
- Prompt; ana ozne, siluet, stil, malzeme, renk, kondisyon ve kullanim hissini tek akista birlestirmeli.
- Belirsiz kalite sloganlari, anlamsiz superlatifler veya image-model kaliplariyla sisirilmemeli.
- Game-ready veya production-ready gibi iddialar ancak kullanici acikca o yone gittiyse ve gerekli baglam verildiyse eklenmeli.
- Teknik notlar kisa, gercekci ve kullanicinin ihtiyacina bagli olmali.
- Kullanici yalnizca prompt istiyorsa ek analiz uzatilmamali; ama bu, eksik girdilerde tek tur netlestirmeyi atlamak anlamina gelmemeli.

# Promotion Criteria

- Farkli Meshy senaryolarinda tutarli calisiyor olmali: prop, silah, karakter, creature, environment parcasi ve stylized collectible gibi.
- Soru secimi tekrar tekrar dengeli sonuc veriyor olmali; kullaniciyi gereksiz yormadan anlamli netlik saglamali.
- "Metin promptu ver, modeli uretme" guardrail'i farkli runtime'larda da guvenilir kalmali.
- Nihai cikti tek bir runtime'in syntax'ina asiri baglanmadan adapterlerde temsil edilebilmeli.
- Gercek kullanim ornekleri biriktiginde `skills/` altinda paketlenmeye ve gerekiyorsa `examples/` klasoru ile desteklenmeye hazir sayilabilir.