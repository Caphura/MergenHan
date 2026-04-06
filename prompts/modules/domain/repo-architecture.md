---
id: mh-module-repo-architecture
title: Repo Architecture
type: module
status: active
version: 1.0.0
summary: Prompt ve skill varliklarini ayrik ama birbirine bagli bir depo mimarisi icinde konumlandirir.
tags:
  - documentation
  - repo-architecture
  - workflow
depends_on: []
last_reviewed: 2026-04-03
input_contract: Prompt librarysi, klasorleme veya bilgi mimarisi kurulumu.
output_contract: Okunur, promotion logic belirgin ve uzun omurlu bir repo iskeleti.
notes: Yapi kurulumlarinda modules, master promptlar, blueprints ve skill paketleri arasindaki ayrimi net tutar.
---

# Purpose

Promptlari "tek klasorde notlar" anlayisindan cikarip maintenancei kolay bir sistem halinde konumlandirmak.

# Usage Rules

- `prompts/` ile `skills/` ayrimini koru.
- Tekrar kullanlisting content modullestir.
- Olgunlasan davranislari blueprint'ten skill'e tasimadan once katalogu currentle.

# Module Text

Repo yapisini, yazim alanlari ile paketlenmis varliklari ayiran bir bilgi mimarisi olarak kur. `prompts/` aktif yazim ve iterasyon alanidir; `skills/` ise olgunlasmis, tekrar kullanilabilir paketleri barindirir. Klasor structure bir bakista anlasilir olmali, yeni gelen biri katalog ve README ile hizla yon bulabilmelidir.
