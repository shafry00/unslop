---
name: unslop
description: Rewrite AI agent instructions or apply the unslop Human Communication Protocol directly to responses and written documents. Use when the user asks to "humanize" a bot's tone, fix robotic-sounding responses, remove AI slop from writing, or apply this protocol to an agent config file.
---

# unslop Skill

Taro folder ini di `~/.claude/skills/unslop/` (global) atau `.claude/skills/unslop/` (per-project). Invoke lewat `/unslop` atau otomatis kalo Claude Code deteksi task yang relevan.

## Langkah

1. Kalo diminta rewrite instruksi agent lain (AGENTS.md, system prompt, dsb): minta filenya dulu kalo belum dikasih, baca, identifikasi bagian robotik, rewrite dengan embed 5 pilar. Preserve struktur dan instruksi teknis yang udah ada.
2. Kalo diminta langsung ngerjain task (chat/dokumen): terapin 5 pilar langsung ke respons/tulisan kamu sendiri di sesi ini.

## 5 Pilar

Lihat [`../_core-snippet.md`](../_core-snippet.md) buat versi ringkas, atau [`../../PROTOCOL.md`](../../PROTOCOL.md) dan [`../../DOCUMENT-MODE.md`](../../DOCUMENT-MODE.md) buat detail lengkap plus contoh.
