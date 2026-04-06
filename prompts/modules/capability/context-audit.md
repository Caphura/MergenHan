---
id: mh-module-context-audit
title: Context Audit
type: module
status: active
version: 1.0.0
summary: Oneriden once mevcut yapiyi, dosyalari ve contexti okumayi required klisting inceleme module.
tags:
  - analysis
  - discovery
  - workflow
depends_on: []
last_reviewed: 2026-04-03
input_contract: Yaplistingdirma, editing veya iyilestirme talebi gelmesi.
output_contract: Onerilerin yerel gerceklige dayanmasi.
notes: Yeni repo, eski repo veya parca parca gelen iceriklerde ilk aktiflestirilen modul olmalidir.
---

# Purpose

Baglam okunmadan verilen tavsiyeleri azaltmak ve her oneriyi mevcut dosya gercegine dayandirmak.

# Usage Rules

- Once mevcut klasorleri, adlandirmayi ve dokumanlari tara.
- Gormedigini assumption diye isaretle.
- Kolayca kesfedilebilecek bilgileri to the user geri sorma.

# Module Text

Once mevcut durumu incele. Hangi dosyalar var, hangi klasorler bos, hangi adlandirma kaliplari kullaniliyor ve hangi bilgi zaten repoda mevcut, bunlari netlestirmeden architecture onerme. Onerilerin kesfedilen contexta dayansin; required olmayan assumptionlari minimumda tut.
