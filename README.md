# unslop

Protokol biar output AI (chat, dokumen, laporan) kerasa kayak manusia beneran, bukan robot template atau tulisan yang keliatan jelas dari AI.

Cocok buat Claude.ai, Claude Code, ChatGPT, Gemini, Cursor, Copilot, OpenCode, Command Code, OpenClaw.

Lahir dari pelatihan bertahap sebuah bot produksi: asisten WhatsApp harian, ratusan interaksi asli, Bahasa Indonesia informal. Bukan teori di atas kertas.

---

## Sebelum vs Sesudah

**Tanpa protokol ini** (bot ditanya soal kesalahan sebelumnya):
> "Baik, saya akan memperbarui data tersebut. Terima kasih atas informasinya. Perubahan telah dilakukan."

**Dengan protokol ini** (respons asli, anonim):
> "Jun, aku paham. [Nama] udah resign dari [organisasi] per 31 Agustus, tapi di instruksi aku dia masih masuk di daftar tim. Aku yang harusnya update itu waktu dia resign dan gak aku lakuin. Maaf. Aku langsung bersihin sekarang."

Lebih banyak contoh (satu per pilar) ada di [`examples/`](./examples).

---

## Mulai Cepat

**Claude.ai (Web), paling gampang:**
1. Download [`dist/unslop.skill`](./dist/unslop.skill)
2. Settings → Capabilities → Skills → Upload
3. Pilih file itu. Selesai, mulai chat baru langsung kepake.

**Claude Code:**
```bash
git clone https://github.com/shafry00/unslop ~/.claude/skills/unslop
```
Otomatis kedeteksi.

**Mau bikin bot/AI lain (bukan Claude) jadi manusiawi?**
Copy isi [`REWRITE-PROMPT.md`](./REWRITE-PROMPT.md), paste ke AI kamu bareng file instruksi bot kamu sekarang (`AGENTS.md`, system prompt, custom instructions, apapun namanya). AI bakal rewrite instruksi kamu otomatis.

**Platform lain** (ChatGPT, Gemini, Cursor, Copilot, OpenCode, Command Code, OpenClaw, Hermes Agent)?
Lihat [`adapters/`](./adapters), instruksi per platform.

Itu aja buat mulai. Sisa file di bawah ini opsional, buat yang mau paham lebih dalam.

---

## Kalo Mau Paham Lebih Dalam

| File | Isinya |
|---|---|
| [`PROTOCOL.md`](./PROTOCOL.md) | 5 pilar lengkap dan alasannya |
| [`examples/`](./examples) | Transkrip asli (anonim), satu per pilar |
| [`DOCUMENT-MODE.md`](./DOCUMENT-MODE.md) | Versi buat nulis dokumen/artikel, bukan chat |
| [`WRITING-STYLE.md`](./WRITING-STYLE.md) + [`references/`](./references) | Level kalimat: kosakata, struktur, cara kerja detektor AI |
| [`SKILL-lite.md`](./SKILL-lite.md) | Versi ringkas buat platform limit karakter |
| [`tools/strip-em-dash.py`](./tools/strip-em-dash.py) | Post-processing pasti buat jamin zero em-dash |
| [`CHECKLIST.md`](./CHECKLIST.md) | 5 poin self-check |

## Kenapa Ini Beda

Bukan kumpulan tips prompting generik. Tiap contoh di `examples/` punya sisi ✅ yang diambil asli dari bot produksi yang dipake tiap hari (nama dan data disamarkan). Sisi ❌-nya rekonstruksi buat kontras, dan itu ditandain jelas, jadi gak ada klaim palsu soal asal-usulnya.

## Lisensi

MIT. Pake, modif, sebarin bebas.
