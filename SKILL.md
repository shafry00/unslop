---
name: human-communication-protocol
description: Rewrite AI agent instructions (AGENTS.md, system prompts, custom instructions) to follow the Human Communication Protocol. Makes bot responses sound human instead of robotic. Use when the user asks to "humanize" a bot's tone, fix robotic-sounding responses, or apply this protocol to an agent config file.
---

# Human Communication Protocol Skill

Baca `PROTOCOL.md` di repo ini buat detail lengkap 5 pilar (Honesty, Curiosity, Vulnerability, Personality, Specificity) dan anti-pattern table.

## Langkah

1. Minta user tunjukin file instruksi agent yang mau direwrite (AGENTS.md, system prompt, dsb). Kalo belum dikasih, tanya dulu. Jangan asumsi.
2. Baca file itu.
3. Identifikasi bagian yang robotik: nada formal berjarak, gak ada mekanisme tanya balik, gak ada cara ngaku salah, jawaban template.
4. Rewrite dengan embed 5 pilar. Preserve struktur dan instruksi teknis yang udah ada. Bahasa ngikutin bahasa asli file.
5. Tambah section baru (misal "Cara Ngobrol") kalo emang belum ada tempat yang pas.
6. Output: file lengkap yang udah direwrite, plus ringkasan perubahan.

## Referensi

- `PROTOCOL.md`: definisi lengkap 5 pilar dan anti-pattern
- `CHECKLIST.md`: 5 poin self-check, bisa ditempel ke instruksi agent biar dia ngecek jawabannya sendiri
- `examples/`: contoh transkrip asli (anonim) buat kalibrasi nada
