# Cara Install

## Claude Code (CLI)

Taro `SKILL.md` di:
- `~/.claude/skills/unslop/SKILL.md` (global, semua project)
- `.claude/skills/unslop/SKILL.md` (per-project)

Otomatis kedeteksi, invoke manual pake `/unslop` atau otomatis kalo Claude Code ngerasa task-nya relevan.

## Claude.ai Web (fitur Skills)

Beda mekanisme dari Claude Code. Claude web butuh skill di-package dengan struktur spesifik, bukan sekadar zip folder sembarangan:

1. Pake file siap-pakai: [`dist/unslop.skill`](../../dist/unslop.skill) di root repo
2. Settings → Capabilities → Skills → Upload
3. Upload file `.skill` itu langsung

**Kalo mau bikin ulang manual** (misal abis edit SKILL.md sendiri):

```bash
mkdir -p /tmp/unslop-package/unslop
cp SKILL.md /tmp/unslop-package/unslop/SKILL.md
cd /tmp/unslop-package
zip -r -X unslop.skill unslop
```

Struktur yang bener: file `.skill` adalah ZIP biasa (cuma ekstensinya diganti), isinya SATU folder bernama sama kayak skill (`unslop/`), dan `SKILL.md` ada DI DALEM folder itu, bukan di root zip. Kalo di-zip langsung dari `SKILL.md` tanpa folder pembungkus, Claude web gak bisa baca strukturnya dengan benar, itu penyebab paling umum skill gak jalan.

**Troubleshooting lain kalo masih gak jalan setelah upload benar:**
- Cek `description` di frontmatter, itu yang dipake Claude buat mutusin kapan skill ini di-trigger otomatis. Kalo terlalu generik, Claude bisa gak manggil skill ini walau relevan. Coba trigger manual dulu: minta eksplisit "pake skill unslop buat ini" di chat.
- Skill di web kadang butuh restart sesi/chat baru buat kedetect ulang setelah upload.
- Pastiin gak ada dependency ke file lain di luar skill (referensi ke `../PROTOCOL.md` dsb gak akan resolve). `SKILL.md` di folder ini udah didesain self-contained, gak butuh file lain.
