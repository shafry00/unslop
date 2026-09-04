# Gemini (CLI / API system instruction)

Gemini CLI baca file `GEMINI.md` di root project sebagai context otomatis, mirip `AGENTS.md` di tool lain.

## Cara Pasang

1. Copy isi [`../_core-snippet.md`](../_core-snippet.md)
2. Taro sebagai section di `GEMINI.md` project kamu (atau bikin baru kalo belum ada)
3. Kalo pake Gemini API langsung (bukan CLI), masukin sebagai bagian dari `system_instruction`

## Catatan

Gemini CLI otomatis include `GEMINI.md` di context tiap sesi tanpa perlu di-invoke manual, jadi taro protokol ini di bagian atas file biar keprioritasin.
