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
input_contract: Prompt kutuphanesi, klasorleme veya bilgi mimarisi kurulumu.
output_contract: Okunur, terfi mantigi belirgin ve uzun omurlu bir repo iskeleti.
notes: Yapi kurulumlarinda moduller, master promptlar, blueprints ve skill paketleri arasindaki ayrimi net tutar.
---

# Purpose

Promptlari "tek klasorde notlar" anlayisindan cikarip bakimi kolay bir sistem halinde konumlandirmak.

# Usage Rules

- `prompts/` ile `skills/` ayrimini koru.
- Tekrar kullanilan icerigi modullestir.
- Olgunlasan davranislari blueprint'ten skill'e tasimadan once katalogu guncelle.

# Module Text

Repo yapisini, yazim alanlari ile paketlenmis varliklari ayiran bir bilgi mimarisi olarak kur. `prompts/` aktif yazim ve iterasyon alanidir; `skills/` ise olgunlasmis, tekrar kullanilabilir paketleri barindirir. Klasor yapisi bir bakista anlasilir olmali, yeni gelen biri katalog ve README ile hizla yon bulabilmelidir.
