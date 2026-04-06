---
id: mh-module-action-summary
title: Action Summary
type: module
status: active
version: 1.0.0
summary: Sonucun taranabilir, decision odakli ve uygulanabilir bir short ozetle bitmesini provides.
tags:
  - output-format
  - summary
  - readability
depends_on: []
last_reviewed: 2026-04-03
input_contract: Analiz veya uygulama tamamlandiginda sonucu sunma ihtiyaci.
output_contract: Kullanicinin immediately anlayabilecegi ozet, degisiklik ve sonraki step.
notes: Buyuk yapi degisikliklerinde bile outputyi gereksiz ayrintiya bogmadan toparlar.
---

# Purpose

Uzun veya daginik analizlerin sonunda the user's what oldugunu hizla anlamasini saglamak.

# Usage Rules

- Ilk paragrafta genel sonucu ver.
- Gerekirse short degisiklik listesi kullan.
- Sonraki adimi explicitly isimlendir.

# Module Text

Sonucu short bir ozetle toparla. Ilk bakista neyin degistigini, neden onemli oldugunu ve the user's bundan sonra nereye bakmasi gerektigini anlasilir bicimde ver. Ayrinti gerekiyorsa ozetin altina ekle; ozetin kendisini kalabaliklastirma.
