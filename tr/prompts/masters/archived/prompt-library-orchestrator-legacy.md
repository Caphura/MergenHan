---
id: mh-master-prompt-library-orchestrator-legacy
title: Prompt Library Orchestrator Legacy
type: master
status: archived
version: 0.8.0
summary: Prompt library duzenlemek icin onceki ve daha dar kapsamli orkestrasyon surumu.
tags:
  - library
  - legacy
  - repo-hygiene
depends_on:
  - mh-module-context-audit
  - mh-module-action-summary
last_reviewed: 2026-04-03
input_contract: Kucuk olcekli prompt duzenleme talepleri.
output_contract: Ozet seklinde yapi onerisi.
notes: Tarihsel referans icin saklanir; yeni kullanimda aktif surum tercih edilir.
---

# Goal

Kucuk olcekli prompt yiginlarini daha derli toplu hale getirmek.

# Assembly Map

- `mh-module-context-audit`: Mevcut durumu anlamak icin.
- `mh-module-action-summary`: Sonucu kisa ve uygulanabilir vermek icin.

# Prompt Body

Prompt kutuphanesini kisa bir gozden gecirme ile toparla, belirgin yinelemeleri isaretle ve temel klasorleme onerisi ver.

Bu surum eski yaklasimi temsil eder:

- detayli modul taksonomisi zorunlu degildir
- skill-blueprint ile skill ayrimi zayiftir
- yonetisim metadatasi ikinci plandadir

# Maintenance Notes

- Yeni kullanimlarda yerine aktif orchestrator kullanilir.
