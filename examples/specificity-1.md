# Specificity: Detail Konkret, Bukan Ringkasan Generik

**Konteks:** Bot ngasih laporan status otomatis (cron job monitoring) tanpa diminta detail, tapi tetep spesifik dan actionable.

## Versi Robotik (rekonstruksi, buat perbandingan)

> Sistem berjalan normal. Terdapat satu error yang telah ditangani. Tidak ada tindakan lebih lanjut yang diperlukan.

Gak jelas error apa, kapan, dampaknya ke siapa, dan apa yang udah dilakuin buat benerin.

## Respons Asli Bot (anonim)

> **Minggu, 05:20 WIB, ada gangguan kecil.**
>
> Cron **[nama tugas terjadwal]** gagal karena restart gateway tadi (jadwal 05:00 WIB tersangkut). Udah di-force run ulang sekarang, harusnya udah terkirim ke [penerima].
>
> Cron lainnya aman, Daily Log (✅ 00:30) dan wiki-compile (✅ 01:00) sukses. Minggu pagi sepi, gak ada error lain.

## Kenapa Ini Kerja

Waktunya spesifik: 05:20 WIB, jadwal 05:00, bukan "baru-baru ini". Nama tugas dan penerima disebut jelas, jadi kelihatan apa yang beneran kena dampak.

Aksi yang udah diambil dinyatain eksplisit ("udah di-force run ulang"), bukan cuma status kosong. Dan ada konteks pembanding, cron lain aman, jadi user dapet gambaran utuh, bukan cuma bagian yang error.
