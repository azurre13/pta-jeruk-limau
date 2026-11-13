# PTA Kebun Jeruk Limau

**Tanggal Pembaruan:** 14 November 2026  
Repositori dokumentasi proyek capstone S1 Teknik Komputer Universitas Telkom untuk kebun jeruk limau di Ciberes, Kabupaten Subang, Jawa Barat. Fokus proyek adalah menyelesaikan permasalahan penyiraman tahap akhir (*last-mile irrigation*) tanpa listrik PLN dari jaringan parit tanah dan **pompa mesin bensin Alkon 2 inci (Pertalite)** milik mitra.

**Pemilik repositori:** azurre13  
**Status Saat Ini:** **`CD-1` (26 halaman) & `CD-2` (26 halaman) Final ACC** telah disahkan dan tersedia di [`dokumen/cd1/`](dokumen/cd1/) dan [`dokumen/cd2/`](dokumen/cd2/). Proyek kini berada pada **tahap persiapan survei lapangan & penyelarasan draf `CD-3`** (draf rekan tim di [`dokumen/cd3/`](dokumen/cd3/) & [`dokumen/draf/cd3/`](dokumen/draf/cd3/), serta workspace usulan terpisah di [`dokumen/draf/cd3_daffa/`](dokumen/draf/cd3_daffa/)). Naskah CD tidak diubah sebelum data survei Minggu terkumpul.

## Membuka di Antigravity atau AI lain

Buka folder clone `C:/Users/daffa/Documents/pta-jeruk-limau`. `AGENTS.md` menyimpan aturan dan konteks awal; `GEMINI.md` menjadi pintu masuk untuk Gemini/Antigravity. Setelah membaca konteks repo, cukup berikan tugas berikutnya. Lihat [panduan chat baru dan peta folder](konteks-ai/MULAI_CHAT_BARU.md).

## Berkas utama

- [CD-1 Final ACC (PDF, 26 halaman)](dokumen/cd1/CD%201%20-%20ANALISIS%20PERMASALAHAN%20PENYIRAMAN%20MANUAL%20PADA%20KEBUN%20JERUK%20LIMAU%20DI%20CIBERES%20SUBANG.pdf)
- [CD-2 Final ACC (PDF, 26 halaman)](dokumen/cd2/CD%202%20-%20ANALISIS%20PERMASALAHAN%20PENYIRAMAN%20MANUAL%20PADA%20KEBUN%20JERUK%20LIMAU%20DI%20CIBERES%20SUBANG.pdf)
- [Indeks direktori dokumen & status draf CD-3](dokumen/README.md)
- [Checklist Survei Lapangan Minggu Ciberes](catatan/CHECKLIST_SURVEI_MITRA_CIBERES.md)
- [Kajian Sumber Air Irigasi, Beda Elevasi, Pompa & Kabel 12 V](catatan/KAJIAN_SUMBER_AIR_IRIGASI_DAN_POMPA.md)
- [Rangkuman Q&A Teknis, Penyederhanaan Scope, & Zonasi 100 m+ (Handoff AI)](catatan/RINGKUMAN_QNA_SCOPE_DAN_ZONASI_PRA_SURVEI.md)
- [Paparan Solusi Detail untuk Mitra Ciberes](catatan/PAPARAN_SOLUSI_UNTUK_MITRA.md)
- [Data mitra lengkap, sumber, estimasi, dan transkrip utuh](catatan/DATA_MITRA_LENGKAP.md)
- [Arsip catatan historis CD-1, CD-2, & awal CD-3](catatan/arsip/README.md)
- [Mulai chat baru dengan AI](konteks-ai/MULAI_CHAT_BARU.md)
- [Konteks proyek lengkap untuk AI](konteks-ai/KONTEKS_PROYEK.md)
- [Catatan pekerjaan yang masih terbuka](konteks-ai/STATUS_DAN_TINDAK_LANJUT.md)
- [Indeks sumber asli](sumber/README.md)

## Susunan folder

```text
sumber/
  template/                  Template resmi CD-1, CD-2, & CD-3
  panduan/                   Buku panduan capstone
  rubrik-jadwal/             Jadwal dan rubrik PTA
  riset/                     Laporan riset terdahulu
  referensi jurnal/          Pustaka & sintesis solusi CD-3
  dokumentasi/               Foto, citra peta, lokasi lain, video, transkrip Audio 1/2
  MANIFEST.json              Asal, ukuran, dan SHA-256 berkas sumber/salinan CD-1
dokumen/
  cd1/                       CD-1 Final ACC (PDF 26 hlm)
  cd2/                       CD-2 Final ACC (PDF 26 hlm)
  cd3/                       Draf CD-3 kolaborasi (Qarnie/Garnie, 34 hlm)
  draf/                      Arsip kerja CD-1, CD-2, CD-3, & workspace draf terpisah cd3_daffa/
catatan/                     Rangkuman Q&A pra-survei, kajian pompa, panduan survei, kamus data mitra, & arsip/ CD-1/CD-2
konteks-ai/                  Konteks lengkap, status terkini, dan petunjuk memulai chat baru
AGENTS.md                    Aturan kerja dan konteks awal agen
GEMINI.md                    Pintu masuk Antigravity/Gemini
```

## Fakta yang menjadi dasar

- Sekitar 500–600 pohon; banyak pohon diperkirakan setinggi ±1 m.
- Tiga parit galian tanah memanjang sekitar 100 m, dengan penghubung melintang setiap beberapa pohon menurut tim.
- Parit dibuat untuk memudahkan pekerja mengambil air dekat deretan pohon; penggalian tanah dipilih sebagai cara sederhana dan hemat.
- Penyiraman masih manual memakai ember hitam kecil. Kapasitas ember, jumlah guyuran, dan volume per pohon belum diukur.
- Sekitar tiga hari sekali; upah empat pekerja × Rp100.000 per orang per kegiatan = Rp400.000 per kegiatan.
- Acuan 15 L/pohon berasal dari penuturan mitra. Skenario 7,5–9 m³ bukan volume aktual dan bukan kebutuhan agronomis tervalidasi.
- Kebun belum tersambung PLN karena jauh dari jaringan listrik. Suplai air mengandalkan **pompa bensin Alkon 2 inci berbahan bakar Pertalite**; mitra sempat mencoba modifikasi **LPG 3 kg** untuk menekan ongkos bahan bakar, namun **dihentikan permanen** karena mesin cepat mengalami panas berlebih (*overheating*) dan menggerus komponen (seher/ring).
- Mitra mencari cara menggantikan pekerjaan guyur manual agar biaya tenaga kerja penyiraman turun.

## Tim

| Anggota | NIM | Akun GitHub |
|---|---|---|
| Muhammad Al Qarnie | 101032330043 | [@Garnie104](https://github.com/Garnie104) |
| Maheswara Ariq Athallah | 101032300050 | [@Riq-Z](https://github.com/Riq-Z) |
| Daffa Hermansyah | 101032330090 | [@azurre13](https://github.com/azurre13) |

Pembimbing: **Dr. Agung Nugroho Jati, S.T., M.T.**  
Lokasi mitra: **JH7H+222, Ciberes, Kabupaten Subang, Jawa Barat**. Nama usaha/pengelola belum dicantumkan.

## Melanjutkan pekerjaan

Baca konteks AI terlebih dahulu. Sumber asli dipertahankan apa adanya. Edit dokumen aktif pada nama file yang sama agar versi tidak menumpuk. Setelah mengedit DOCX, ekspor ulang PDF dan periksa halaman yang berubah. Tanda tangan dosen diperoleh dari dosen; kolom pengesahan tidak diisi oleh AI.

**Visibilitas saat diperiksa 9 Oktober 2026: public.** Catatan lama menyebut private, tetapi pemeriksaan GitHub menunjukkan keadaan berbeda. Pembaruan ini menggunakan repositori yang sama. Tidak ada kredensial GitHub, kata sandi, atau token yang disertakan.
