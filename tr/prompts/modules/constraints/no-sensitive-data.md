---
id: mh-module-no-sensitive-data
title: No Sensitive Data
type: module
status: active
version: 1.0.0
summary: Repoya hangi iceriklerin asla girmemesi gerektigini tanimlayan guvenlik ve yonetisim modulu.
tags:
  - safety
  - governance
  - privacy
depends_on: []
last_reviewed: 2026-04-03
input_contract: Repo icine yeni prompt, ornek veya asset ekleme karari.
output_contract: Acikca paylasilabilir ve risk tasimayan icerik secimi.
notes: Ozellikle musteri islerinden tureyen prompt varyantlarinda etkin olmalidir.
---

# Purpose

Paylasilmamasi gereken veri ve prompt varyantlarini erkenden ayiklamak.

# Usage Rules

- API anahtari, gizli token, musteri verisi veya ozel strateji notlarini repoya tasima.
- Ornek veri gerekiyorsa sentetik ve guvenli ornek kullan.
- Riskli icerigi promptun parcasina degil harici ve korumali alana tasi.

# Module Text

Bu repo yalnizca paylasilabilir ve guvenli icerik barindirir. Gizli anahtarlar, musteriye ozel prompt varyantlari, hassas is akislari veya paylasimi sinirli veri ornekleri prompt kutuphanesine dahil edilmez. Supheli durumlarda disarida birakmak varsayilan karardir.
