---
id: mh-module-no-sensitive-data
title: No Sensitive Data
type: module
status: active
version: 1.0.0
summary: Repoya hangi iceriklerin asla girmemesi gerektigini tanimlayan guvenlik ve governance module.
tags:
  - safety
  - governance
  - privacy
depends_on: []
last_reviewed: 2026-04-03
input_contract: Repo icine yeni prompt, example veya asset ekleme decisioni.
output_contract: Acikca paylasilabilir ve risk tasimayan content secimi.
notes: Ozellikle musteri islerinden tureyen prompt varyantlarinda etkin olmalidir.
---

# Purpose

Paylasilmamasi gereken veri ve prompt varyantlarini erkenden ayiklamak.

# Usage Rules

- API anahtari, gizli token, musteri verisi veya specific strateji notlarini repoya tasima.
- Example veri gerekiyorsa sentetik ve guvenli example kullan.
- Riskli content promptun parcasina degil harici ve korumali alana tasi.

# Module Text

This repository only paylasilabilir ve guvenli content barindirir. Gizli anahtarlar, musteriye specific prompt varyantlari, hassas is akislari veya paylasimi sinirli veri exampleleri prompt librarysine dahil edilmez. Supheli durumlarda disarida birakmak default decisiondir.
