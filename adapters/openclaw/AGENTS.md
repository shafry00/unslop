# OpenClaw

OpenClaw baca `AGENTS.md` dan `SOUL.md` (kalo ada) di workspace sebagai bootstrap instruksi agent tiap sesi.

## Cara Pasang

1. Copy isi [`../_core-snippet.md`](../_core-snippet.md)
2. Append sebagai section baru di `AGENTS.md` workspace kamu (`~/.openclaw/workspace/AGENTS.md`)

## Catatan

Protokol ini sebenernya lahir dari observasi bot OpenClaw produksi. Kalo `SOUL.md` kamu udah kena limit karakter bootstrap (perhatikan log `workspace bootstrap file SOUL.md is X chars; truncating`), taro protokol ini di `AGENTS.md` (yang dibaca terpisah dari SOUL.md), bukan numpuk di SOUL.md yang gampang kepotong.
