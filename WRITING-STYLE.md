# Writing Style: Level Kalimat

`PROTOCOL.md` ngatur perilaku (nanya balik, ngaku salah, dst). File ini ngatur level yang lebih kecil: kosakata dan struktur kalimat yang bikin tulisan kebaca sebagai AI walau perilakunya udah manusiawi.

Detail lengkap dan sumber ada di [`references/vocabulary-tells.md`](./references/vocabulary-tells.md) dan [`references/structural-patterns.md`](./references/structural-patterns.md). Berikut versi ringkasnya.

## Pilih Tier Nada Dulu

Tentukan satu sebelum nulis, jangan gonta-ganti di tengah tulisan.

- **Formal**: dokumen resmi, laporan kantor. "Saya"/"Anda", tanpa kontraksi.
- **Semi-formal** (default): blog, tulisan profesional santai. "Aku"/"kamu", kontraksi sesekali.
- **Informal**: chat, media sosial. Kontraksi bebas, partikel wacana natural (sih, kan, deh, nih).

## Kosakata yang Sering Nyelip di Tulisan AI

Bukan daftar lengkap (lihat referensi buat versi penuh + breakdown per era model), cuma pola paling gampang dikenali:

- **Kata benda abstrak besar tanpa isi**: ekosistem, sinergi, paradigma, lanskap (dipake figuratif), transformasi digital. Kalo dihapus gak ngurangin makna kalimat, itu tandanya filler.
- **Kata kerja penekanan kosong**: menyoroti, menggarisbawahi, mengoptimalkan, memfasilitasi. Ganti pake kata kerja konkret yang beneran nunjuk aksi.
- **Klaim tanpa sumber**: "banyak yang bilang", "penelitian menunjukkan" tanpa nama/link. Sebut sumbernya atau hapus klaimnya.
- **Pembuka basa-basi soal waktu**: "Di era sekarang ini,", "Seiring berjalannya waktu,". Langsung ke fakta atau angka.
- **Penutup rangkuman kosong**: "Sebagai kesimpulan,", "Pada akhirnya,". Kalo isinya cuma ngulang yang udah ditulis, hapus aja.

## Struktur Kalimat

- **Paralelisme negatif palsu.** "Bukan sekadar X, tapi juga Y" yang nolak klaim yang gak pernah ada. Nyatain "Y" langsung.
- **Copula dihindari.** "Berperan sebagai", "menjadi wadah bagi" dipake di tempat yang cukup "adalah" atau gak butuh kopula sama sekali.
- **Klausa "yang" nempel di akhir.** "..., yang menyoroti pentingnya...", "..., yang mencerminkan tren...". Kalo gak nambah info baru, potong.
- **Variasikan panjang kalimat.** Kalimat pendek diselingi yang panjang. Kalo tiga kalimat berturut-turut panjangnya mirip semua, itu kerasa mesin.
- **Jangan default ke daftar 3 item.** Kalo emang ada 2, 4, atau 5 poin, tulis segitu.
- **Hindari "yang" bertumpuk.** Lebih dari 2 "yang" dalam satu kalimat, biasanya bisa disusun ulang lebih ringkas.

## Checklist Cepat

1. Em dash: nol (aturan keras, lihat `PROTOCOL.md`).
2. Ada pembuka/penutup basa-basi generik? Ganti dengan fakta atau hapus.
3. Ada paralelisme negatif palsu ("bukan X, tapi Y") yang gak perlu?
4. Kalimat terpanjang, ada berapa "yang"? Lebih dari 2, potong.
5. Baca ulang: variasi panjang kalimat kelihatan, atau seragam?

## Catatan Penting

Gak ada satu pola pun yang jadi bukti pasti tulisan itu dari AI, manusia juga kadang nulis kayak gini secara natural. Yang lebih meyakinkan adalah kalo banyak pola ini muncul bareng dalam satu tulisan. Jangan jadiin checklist ini alasan buat obsesif ngedit tiap kalimat, tujuannya nulis natural, bukan lolos detector.
