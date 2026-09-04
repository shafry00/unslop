# Writing Style: Level Kalimat

`PROTOCOL.md` ngatur perilaku (nanya balik, ngaku salah, dst). File ini ngatur level yang lebih kecil: kosakata dan struktur kalimat yang bikin tulisan kebaca sebagai AI walau perilakunya udah manusiawi.

Materinya diadaptasi dan disingkat dari riset [anti-slop-writing](https://github.com/adenaufal/anti-slop-writing) (MIT, Aden Naufal), disesuaikan ke format dan bahasa unslop. Buat daftar lengkap dan riset di baliknya (perplexity, burstiness, stilometri), rujuk repo aslinya.

## Pilih Tier Nada Dulu

Tentukan satu sebelum nulis, jangan gonta-ganti di tengah tulisan (pergeseran register per paragraf itu sendiri ciri AI).

- **Formal**: dokumen resmi, laporan kantor. "Saya"/"Anda", tanpa kontraksi, tanpa partikel wacana.
- **Semi-formal** (default buat kebanyakan konteks): blog, opini, tulisan profesional santai. "Aku"/"kamu", kontraksi sesekali ("nggak", "udah"), partikel wacana jarang.
- **Informal**: chat, media sosial. Kontraksi bebas, partikel wacana natural (sih, kan, kok, deh, nih).

## Kosakata yang Dihindari

**Puffery/berlebihan tanpa data:** krusial, fundamental, komprehensif, holistik, inovatif, dinamis, transformasi digital, ekosistem, paradigma, sinergi, optimalisasi, lanskap, signifikan (tanpa angka pendukung).

**Kata kerja penekanan kosong:** menyoroti, menggarisbawahi, memfasilitasi, mengoptimalkan, mengedepankan, menyelami, berkontribusi pada, mencerminkan.

**Atribusi samar:** "para ahli", "penelitian menunjukkan", "banyak pihak" tanpa nama sumber. Sebut sumber spesifik atau hapus klaimnya.

**Pembuka template:** "Di era modern ini,", "Seiring perkembangan zaman,", "Dalam konteks X yang semakin Y,". Mulai dengan fakta atau angka konkret, bukan generalisasi waktu.

**Penutup template:** "Sebagai kesimpulan,", "Dapat disimpulkan bahwa", "Pada akhirnya,". Kesimpulan harus nambahin sesuatu baru (lihat `DOCUMENT-MODE.md`), bukan basa-basi penutup.

**Pasangan formulaik:** "tantangan dan peluang", "di satu sisi... di sisi lain", "tidak hanya X tetapi juga Y".

## Struktur Kalimat

- **Variasikan panjang secara dramatis.** Campur kalimat pendek (3-5 kata) dengan yang panjang (25+ kata). Tiga kalimat berturut-turut dengan panjang mirip itu ciri AI.
- **Pecah kebiasaan "rule of three".** AI default nulis daftar 3 item. Sengaja bikin 2, 4, atau 5.
- **Kurangi "yang" berlebih.** Lebih dari 2 "yang" dalam satu kalimat, susun ulang.
- **Kurangi "adalah" yang gak perlu.** Bahasa Indonesia sering gak butuh kopula: "Indonesia negara kepulauan" cukup, gak perlu "Indonesia adalah negara kepulauan".
- **Pro-drop kalau subjek udah jelas.** Jangan ulang "dia, dia, dia" tiap kalimat kalau konteksnya udah jelas siapa yang dimaksud.
- **Lebih suka kata kerja daripada nominalisasi.** "Melatih" bukan "pelaksanaan pelatihan".

## Checklist Cepat Sebelum Kirim

1. Em dash: target nol (lihat aturan keras di `PROTOCOL.md`/`SKILL.md`).
2. Ada pembuka "Di era"/"Seiring"/"Dalam konteks"? Tulis ulang pake fakta spesifik.
3. Ada "merupakan" atau "tidak hanya...tetapi juga"? Susun ulang.
4. Kalimat terpanjang ada berapa "yang"? Kalo lebih dari 2, potong.
5. Variasi panjang kalimat kelihatan, atau seragam semua? Kalo seragam, pecah atau gabung beberapa.
6. Tier nada konsisten dari awal sampe akhir?
