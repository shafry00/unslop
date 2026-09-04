# unslop

Protokol buat bikin output AI (chat, dokumen, laporan, apapun) kerasa kayak manusia beneran, bukan robot yang sopan-sopan template atau tulisan yang keliatan jelas dari AI.

## Mulai dari Sini

Pilih satu sesuai kondisi kamu:

**Cuma mau pake di Claude.ai web?**
Download [`dist/unslop.skill`](./dist/unslop.skill), buka Settings → Capabilities → Skills → Upload, pilih file itu. Selesai, gak ada langkah lain.

**Pake Claude Code CLI?**
```bash
git clone https://github.com/shafry00/unslop ~/.claude/skills/unslop
```
Otomatis kedeteksi. Selesai.

**Mau bikin bot/AI lain (bukan Claude) jadi manusiawi?**
Copy isi [`REWRITE-PROMPT.md`](./REWRITE-PROMPT.md), paste ke AI kamu bareng file instruksi bot kamu sekarang (`AGENTS.md`, system prompt, custom instructions, apapun namanya). AI bakal rewrite instruksi kamu otomatis.

**Platform spesifik** (ChatGPT, Gemini, Cursor, Copilot, dll)?
Lihat [`adapters/`](./adapters), ada instruksi per platform.

Itu aja. Sisa file di bawah ini opsional, buat yang mau paham lebih dalam atau butuh referensi tambahan, bukan syarat buat mulai pakai.

## Kalo Mau Paham Lebih Dalam

- [`PROTOCOL.md`](./PROTOCOL.md): isi lengkap 5 pilar dan alasannya
- [`examples/`](./examples): transkrip asli (anonim) tiap pilar
- [`DOCUMENT-MODE.md`](./DOCUMENT-MODE.md): versi buat nulis dokumen/artikel (bukan chat)
- [`WRITING-STYLE.md`](./WRITING-STYLE.md) + [`references/`](./references): level kalimat (kosakata, struktur, cara kerja detektor AI)
- [`SKILL-lite.md`](./SKILL-lite.md): versi ringkas buat platform limit karakter
- [`tools/strip-em-dash.py`](./tools/strip-em-dash.py): post-processing pasti buat jamin zero em-dash, dipake kalo instruksi teks gak cukup reliable
- [`CHECKLIST.md`](./CHECKLIST.md): 5 poin self-check

Lahir dari pelatihan bertahap sebuah bot produksi: asisten WhatsApp harian, ratusan interaksi asli, Bahasa Indonesia informal. Bukan teori di atas kertas.

## Kenapa Ini Beda

Bukan kumpulan tips prompting generik. Tiap contoh di `examples/` punya sisi ✅ yang diambil asli dari bot produksi yang dipake tiap hari (nama dan data disamarkan). Sisi ❌-nya rekonstruksi buat kontras, dan itu ditandain jelas, jadi gak ada klaim palsu soal asal-usulnya.

## Lisensi

MIT. Pake, modif, sebarin bebas.
