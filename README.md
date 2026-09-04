# Human Communication Protocol

Protokol buat bikin AI agent (chatbot, asisten WhatsApp, apapun) jawabnya kayak manusia beneran — bukan robot yang sopan-sopan template.

Lahir dari pelatihan bertahap sebuah bot produksi (asisten WhatsApp harian, ratusan interaksi asli, Bahasa Indonesia informal), bukan teori di atas kertas.

## Cara Pakai (30 detik)

1. Copy isi [`REWRITE-PROMPT.md`](./REWRITE-PROMPT.md)
2. Paste ke AI kamu (Claude, ChatGPT, siapapun) bareng file instruksi agent kamu sekarang (`AGENTS.md`, `SYSTEM_PROMPT.md`, `SOUL.md`, custom instructions — apapun namanya)
3. AI bakal rewrite instruksi kamu supaya agent-nya otomatis ngikutin protokol ini

Gak perlu ngerti isi protokolnya dulu buat mulai pakai. Tapi kalo mau paham kenapa, baca [`PROTOCOL.md`](./PROTOCOL.md).

## Isi Repo

| File | Fungsi |
|---|---|
| [`PROTOCOL.md`](./PROTOCOL.md) | 5 pilar inti + anti-pattern table |
| [`REWRITE-PROMPT.md`](./REWRITE-PROMPT.md) | Meta-prompt siap-copas buat rewrite instruksi agent kamu |
| [`CHECKLIST.md`](./CHECKLIST.md) | Self-check 5 poin — bisa dipake bot buat ngecek jawabannya sendiri |
| [`examples/`](./examples) | Transcript asli (anonim) — robotik vs hasil protokol |
| [`SKILL.md`](./SKILL.md) | Versi Claude Code skill — invoke langsung tanpa copas manual |

## Kenapa Ini Beda

Bukan kumpulan "prompt tips" generik. Semua contoh di `examples/` itu respons asli dari bot produksi yang udah dipake tiap hari — bukan simulasi atau contoh karangan. Anti-pattern table-nya juga hasil observasi nyata, bukan tebakan.

## Lisensi

MIT — pake, modif, sebarin bebas.
