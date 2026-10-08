# Melanjutkan proyek ini di AI lain

**Diperbarui 9 Oktober 2026.** Buka root repo, lalu berikan tugas singkat. Konteks proyek disimpan dalam berkas sehingga tidak perlu menempelkan seluruh riwayat percakapan.

## Membuka di Antigravity

1. Buka folder `C:/Users/daffa/Documents/pta-jeruk-limau` sebagai workspace/project. Folder ini merupakan clone GitHub yang berisi dokumen aktif dan sumber.
2. Repo menyediakan `AGENTS.md` untuk aturan/konteks awal dan `GEMINI.md` untuk pintu masuk Gemini/Antigravity. `GEMINI.md` memasukkan aturan dari `AGENTS.md`; instruksi rinci tetap memiliki satu sumber agar tidak berbeda antaragen.
3. Mulai dengan tugas singkat, misalnya:

> Baca konteks repo ini, lalu bantu saya menyiapkan data lapangan untuk CD-2.

Contoh lain:

> Lanjutkan proyek ini. Revisi CD-1 berdasarkan catatan dosen berikut: [catatan dosen].

Dokumentasi resmi Antigravity menyebut `AGENTS.md`/`GEMINI.md` sebagai aturan workspace dan mendukung include `@[label](path)`. Konfigurasi repo mengikuti bentuk tersebut; pemuatan langsung pada aplikasi pengguna belum diuji dalam sesi ini. Jika konteks tidak terbaca pada versi aplikasi yang digunakan, cukup tulis:

> Baca AGENTS.md dan dua file konteks yang dirujuk sebelum mengerjakan tugas saya.

Sumber konfigurasi: [Google Antigravity — Rules](https://antigravity.google/docs/rules), diperiksa 9 Oktober 2026.

## Urutan baca AI

1. `AGENTS.md`: tujuan repo, fakta inti, batas data, dan aturan mengedit.
2. `konteks-ai/KONTEKS_PROYEK.md`: riwayat koreksi, seluruh fakta, sumber, batasan, dan keputusan yang masih terbuka.
3. `konteks-ai/STATUS_DAN_TINDAK_LANJUT.md`: hasil yang sudah selesai, pengesahan yang belum tersedia, serta pengukuran berikutnya.
4. Berkas aktif dan sumber yang relevan dengan tugas. Untuk revisi laporan, baca DOCX aktif, template asli, buku panduan, dan rubrik; ekstraksi teks saja belum memeriksa layout.

## Peta folder dan fungsi berkas

| Lokasi dari root repo | Fungsi |
|---|---|
| `dokumen/cd1/CD1_Jeruk_Limau.docx` | Satu laporan Word aktif yang diedit pada nama yang sama. |
| `dokumen/cd1/CD1_Jeruk_Limau.pdf` | PDF pendamping dari DOCX yang sama; snapshot 25 halaman. |
| `catatan/Bahan_Bimbingan_CD1_Jeruk_Limau.md` | Bacaan mahasiswa, penjelasan singkat, data, dan jawaban bimbingan. |
| `catatan/REFERENSI_CD1.md` | Daftar 36 referensi dari DOCX aktif; nomor mengikuti sitasi. |
| `konteks-ai/` | Konteks, status, dan panduan memulai chat baru. |
| `sumber/template/` | Template akademik asli CD-1. |
| `sumber/panduan/` | Buku panduan capstone. |
| `sumber/rubrik-jadwal/` | Jadwal dan rubrik PTA semester 2026/2027. |
| `sumber/riset/` | Laporan riset terdahulu, sebagai referensi yang perlu diperiksa sebelum dikutip. |
| `sumber/dokumentasi/` | Foto, citra, video, transkrip Audio 1/2; lokasi lain dipisahkan. |
| `work/` | Berkas sementara/QA; diabaikan Git dan biasanya tidak ikut clone. |

Seluruh `sumber/` hanya-baca. Folder awal `C:/Users/daffa/Documents/PTA jeruk limau` dan mirror ChatGPT bukan clone aktif ini. Pada komputer lain, gunakan lokasi clone sendiri dan jalur relatif di atas.

## Yang harus langsung dipahami

Tahap proyek adalah CD-1: analisis masalah, kompleksitas, dan perbandingan pendekatan yang tersedia. Air sungai dipompa ke tiga parit tanah yang terhubung melintang, lalu pekerja mengguyurkan air ke sekitar 500–600 pohon. Fokusnya pekerjaan tahap akhir dan volume yang belum terukur. Upah Rp400.000/kegiatan, interval sekitar tiga hari, serta acuan mitra minimal 15 L/pohon merupakan data awal; Rp48,7 juta/tahun dan 7,5–9 m³/kegiatan adalah skenario.

Kebun tanpa PLN. Pompa dilaporkan memakai LPG hasil modifikasi mesin bensin. Tanah jeruk belum diuji; pemupukan dua kali setahun diketahui tetapi jenis/dosis belum tersedia. Hujan, tajuk, fase buah, dan air daerah akar perlu dinilai. Robot dari arahan bimbingan masih kandidat, sama seperti pendekatan lain. Jumlah pompa, kontroler, zona, dosis final, serta desain perangkat belum dipilih.

## Jika chat hanya menerima lampiran

Lampirkan `KONTEKS_PROYEK.md`, `STATUS_DAN_TINDAK_LANJUT.md`, serta DOCX/PDF aktif. Sertakan template/panduan/rubrik bila meminta revisi akademik dan sumber khusus yang diperlukan. Tautan GitHub private saja tidak memberi AI akses otomatis.

Transkrip sayuran tambahan yang dibahas pada konteks berada di lampiran percakapan di luar repo. Konteks menyimpan batas informasi yang telah digunakan; jangan mengaku membaca transkrip lengkap jika lampirannya tidak tersedia. Foto/video/transkrip serta paper juga harus benar-benar dibaca sebelum digunakan sebagai bukti baru.

## Menjaga kesinambungan setelah pekerjaan

Edit file aktif pada nama yang sama. Setelah DOCX berubah, perbarui PDF, jumlah halaman, dan periksa hasil render. Selaraskan ringkasan bimbingan, referensi, konteks, dan status. Cek `git status` serta branch/remote sebelum sinkronisasi; commit dan push mengikuti permintaan pengguna. Pekerjaan lapangan, bimbingan, tanda tangan, dan hasil pengujian hanya dicatat jika benar-benar dikonfirmasi.
