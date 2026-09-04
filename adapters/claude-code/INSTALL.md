# Cara Install

## Claude Code (CLI)

Taro `SKILL.md` di:
- `~/.claude/skills/unslop/SKILL.md` (global, semua project)
- `.claude/skills/unslop/SKILL.md` (per-project)

Otomatis kedeteksi, invoke manual pake `/unslop` atau otomatis kalo Claude Code ngerasa task-nya relevan.

## Claude.ai Web (fitur Skills)

Beda mekanisme dari Claude Code. Claude web butuh skill di-package, bukan cuma file mentah:

1. Bikin folder isinya `SKILL.md` ini
2. Zip folder itu (bukan file `.md`-nya doang, foldernya)
3. Settings → Capabilities → Skills → Upload
4. Upload zip-nya

**Kalo masih gak jalan setelah di-zip dan upload:**
- Cek `description` di frontmatter, itu yang dipake Claude buat mutusin kapan skill ini di-trigger otomatis. Kalo terlalu generik/gak spesifik, Claude bisa gak manggil skill ini walau relevan. Coba trigger manual dulu: minta eksplisit "pake skill unslop buat ini" di chat.
- Skill di web kadang butuh restart sesi/chat baru buat kedetect ulang setelah upload.
- Pastiin gak ada dependency ke file lain di luar skill (referensi ke `../PROTOCOL.md` dsb gak akan resolve). `SKILL.md` di folder ini udah didesain self-contained, gak butuh file lain.
