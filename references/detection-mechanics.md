# Gimana Detektor AI Kerja (dan Kenapa Gak Bisa Diandelin 100%)

Referensi buat `WRITING-STYLE.md`. Ringkasan cara kerja metrik deteksi AI, biar ngerti KENAPA pola-pola di `structural-patterns.md` dan `vocabulary-tells.md` itu relevan, bukan sekadar daftar aturan tanpa dasar.

## Tiga Metrik Utama

**Perplexity**: ngukur seberapa "gampang ditebak" tiap kata dalam kalimat. Kalo prompt-nya "Halo, aku AI ___", kata "asisten" itu perplexity rendah (gampang ditebak model), sementara kata yang gak biasa punya perplexity tinggi. Teks AI cenderung perplexity rendah karena model milih kata yang paling mungkin secara statistik. Teks manusia lebih "gak terduga" pilihan katanya.

**Burstiness**: ngukur variasi panjang dan kompleksitas kalimat dalam satu tulisan. Dihitung dari standar deviasi skor perplexity per kalimat. Tulisan manusia biasanya "bursty": kalimat pendek diselingi kalimat panjang secara gak teratur. Tulisan AI cenderung rata, kalimat-kalimatnya seragam.

**Stilometri**: analisis pola statistik yang lebih luas, frekuensi kata fungsi (kayak "yang", "dan", "di"), keragaman kosakata, pola tanda baca, kedalaman struktur kalimat. Ini "sidik jari" gaya nulis yang bisa beda antar penulis (atau antar model AI).

## Kenapa Ini Gak Bisa Jadi Satu-Satunya Andalan

Penting buat jujur soal batasan metrik-metrik ini:

- GPTZero, salah satu detektor pertama yang mempopulerkan perplexity/burstiness, per akhir 2023 udah pindah ke arsitektur deep-learning dan gak lagi murni ngandelin dua metrik itu. Artinya detektor komersial modern lebih kompleks dari sekadar ngitung dua angka ini.
- Riset akademis (termasuk yang dipublikasi di arXiv soal AI Detectability Index) nunjukin deteksi AI itu "gak semudah yang dikira". Model yang lebih baru makin bagus niru pola manusia, termasuk sengaja bikin burstiness palsu.
- Manusia juga bisa nulis dengan perplexity rendah dan burstiness rendah kalo topiknya teknis/formal. Sebaliknya, AI yang di-prompt dengan baik bisa niru burstiness tinggi.

## Implikasi Buat Cara Kita Pake Aturan Ini

Karena metrik-metrik ini gak sempurna, `unslop` gak nyoba "ngalahin detektor" secara teknis. Tujuannya nulis natural karena itu emang lebih enak dibaca, bukan buat lolos tes tertentu. Aturan-aturan di `vocabulary-tells.md` dan `structural-patterns.md` itu proxy yang membantu, bukan jaminan mutlak. Kalo nurutin semua aturan tapi tulisannya jadi kaku dan gak natural, itu tandanya aturan itu diterapin salah, bukan tandanya kurang ketat.
