# ChatGPT / Custom GPT

Gak ada mekanisme "skill file" kayak Claude Code. Dua cara pasang:

## Cara 1: Custom GPT
1. Buka GPT Builder → Configure → Instructions
2. Paste isi [`../_core-snippet.md`](../_core-snippet.md) ke kolom Instructions (gabung sama instruksi lain yang udah ada)

## Cara 2: Custom Instructions (akun biasa)
1. Settings → Personalization → Custom Instructions
2. Paste ke kolom "How would you like ChatGPT to respond?"

## Cara 3: Project/system prompt via API
Masukin isi `_core-snippet.md` sebagai bagian dari `system` message.

Batasan: ChatGPT gak punya cara verifikasi otomatis kalo protokol ini diikutin (beda sama skill yang bisa nge-load file referensi lain). Recommended tetep paste versi ringkas (`_core-snippet.md`), bukan `PROTOCOL.md` penuh, biar gak makan context budget custom instructions yang terbatas.
