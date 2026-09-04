# unslop

Protokol buat bikin output AI (chat, dokumen, laporan, apapun) kerasa kayak manusia beneran, bukan robot yang sopan-sopan template atau tulisan yang keliatan jelas dari AI.

Ada dua mode: [`PROTOCOL.md`](./PROTOCOL.md) buat percakapan interaktif (chatbot, asisten), dan [`DOCUMENT-MODE.md`](./DOCUMENT-MODE.md) buat task nulis sekali-jalan (dokumen, artikel, laporan).

Lahir dari pelatihan bertahap sebuah bot produksi: asisten WhatsApp harian, ratusan interaksi asli, Bahasa Indonesia informal. Bukan teori di atas kertas.

## Cara Pakai (30 detik)

1. Copy isi [`REWRITE-PROMPT.md`](./REWRITE-PROMPT.md)
2. Paste ke AI kamu (Claude, ChatGPT, siapapun) bareng file instruksi agent kamu sekarang. `AGENTS.md`, `SYSTEM_PROMPT.md`, `SOUL.md`, custom instructions, apapun namanya.
3. AI bakal rewrite instruksi kamu supaya agent-nya otomatis ngikutin protokol ini.

Gak perlu ngerti isi protokolnya dulu buat mulai pakai. Kalo mau paham kenapa, baca [`PROTOCOL.md`](./PROTOCOL.md).

## Isi Repo

| File | Fungsi |
|---|---|
| [`PROTOCOL.md`](./PROTOCOL.md) | 5 pilar inti dan anti-pattern table |
| [`REWRITE-PROMPT.md`](./REWRITE-PROMPT.md) | Meta-prompt siap-copas buat rewrite instruksi agent kamu |
| [`CHECKLIST.md`](./CHECKLIST.md) | Self-check 5 poin, bisa dipake bot buat ngecek jawabannya sendiri |
| [`examples/`](./examples) | Transkrip asli (anonim), satu per pilar |
| [`SKILL.md`](./SKILL.md) | Versi Claude Code skill, invoke langsung tanpa copas manual |
| [`DOCUMENT-MODE.md`](./DOCUMENT-MODE.md) | Mapping 5 pilar ke task nulis dokumen (laporan, artikel, proposal), plus anti-pattern AI slop |
| [`WRITING-STYLE.md`](./WRITING-STYLE.md) | Level kalimat: kosakata dan struktur yang bikin tulisan kebaca AI. Pelengkap PROTOCOL.md yang ngatur perilaku |
| [`references/`](./references) | Breakdown lengkap kosakata per era model dan pola struktur, sumber [Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) |
| [`SKILL-lite.md`](./SKILL-lite.md) | Versi ringkas buat platform limit karakter (ChatGPT Custom Instructions, dsb) |
| [`adapters/`](./adapters) | Cara pasang di Claude Code, ChatGPT, Gemini, Cursor, Copilot, OpenCode, Command Code, OpenClaw, dan Hermes Agent |
| [`tools/strip-em-dash.py`](./tools/strip-em-dash.py) | Script find-replace buat jamin zero em-dash di output final. Instruksi ke AI gak pernah 100% reliable, ini post-processing yang pasti, tanpa panggil AI lagi (nol token) |
| [`dist/unslop.skill`](./dist/unslop.skill) | Package siap-upload buat fitur Skills di Claude.ai web |

## Platform yang Didukung

Tiap platform punya konvensi config beda (skill file, system instruction, `AGENTS.md`, dsb). Lihat folder [`adapters/`](./adapters) untuk instruksi spesifik tiap platform:

- [Claude Code](./adapters/claude-code)
- [ChatGPT / Custom GPT](./adapters/chatgpt)
- [Gemini](./adapters/gemini)
- [Cursor](./adapters/cursor)
- [GitHub Copilot](./adapters/copilot)
- [OpenCode](./adapters/opencode)
- [Command Code](./adapters/commandcode)
- [OpenClaw](./adapters/openclaw)
- [Hermes Agent](./adapters/hermes-agent)

Semua adapter narik dari [`adapters/_core-snippet.md`](./adapters/_core-snippet.md), versi ringkas protokol yang siap ditempel langsung.

## Kenapa Ini Beda

Bukan kumpulan tips prompting generik. Tiap contoh di `examples/` punya sisi ✅ yang diambil asli dari bot produksi yang dipake tiap hari (nama dan data disamarkan). Sisi ❌-nya rekonstruksi buat kontras, dan itu ditandain jelas, jadi gak ada klaim palsu soal asal-usulnya. Anti-pattern table juga hasil observasi nyata, bukan tebakan.

## Lisensi

MIT. Pake, modif, sebarin bebas.
