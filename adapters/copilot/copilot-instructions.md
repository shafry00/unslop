# GitHub Copilot

Copilot (Chat/Workspace) baca `.github/copilot-instructions.md` otomatis sebagai custom instructions repo.

## Cara Pasang

1. Copy isi [`../_core-snippet.md`](../_core-snippet.md)
2. Taro (atau append) ke `.github/copilot-instructions.md` di root repo kamu

## Catatan

Copilot lebih sering dipake buat kode + komentar daripada chat panjang. Bagian yang paling relevan buat konteks ini biasanya bagian anti-slop (Document Mode): commit message, PR description, dan komentar kode juga rawan kena pola AI slop (bullet berlebihan, kalimat generik "This function handles..."). Pertimbangin tambahin baris eksplisit soal itu kalo dipake buat auto-generate PR description.
