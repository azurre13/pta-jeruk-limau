# PTA Kebun Jeruk Limau

**Tanggal Pembaruan:** 23 November 2026  
Repositori dokumentasi proyek capstone S1 Teknik Komputer Universitas Telkom untuk kebun jeruk limau di Ciberes, Kabupaten Subang, Jawa Barat. Fokus awal proyek pada **`Kebun Besar`** (`CD-1` & `CD-2`) kemudian disesuaikan pasca-survei menjadi fokus prototipe pada **`Kebun Kecil` (`1 Zona = 4 Pohon Sampel`)** sambil mempertahankan seluruh arsip data `Kebun Besar` sebagai jejak perubahan.

**Pemilik repositori:** azurre13  
**Status Saat Ini (`23 Nov 2026`):** **`CD-1` (26 halaman) & `CD-2` (26 halaman) Final ACC** sudah dikumpulkan di [`dokumen/cd1/`](dokumen/cd1/) dan [`dokumen/cd2/`](dokumen/cd2/) serta **dibiarkan utuh dulu**. Pembimbing 1, Dosen Pengampu, dan Mitra telah **ACC pindah ke `Kebun Kecil` (`1 Zona = 4 Pohon Sampel`)** dengan sumber air **sumur baru** (toren `75×75 cm` tidak dipakai, masih memakai **Alkon bensin** + **`2` pekerja × `Rp100.000` setiap `3–4 hari`** jika tak hujan, air `10–15 L/pohon`, listrik PLN ada, serta target memaksimalkan pertumbuhan & buah). Berkas `CD-3` lama yang ada saat ini (`dokumen/cd3/`, `dokumen/draf/cd3/`, `cd3_daffa/` lama) berstatus **draf lama tidak terpakai**; **`CD-3` baru belum dibuat dulu** — kelak dibuat **dari awal** menuju tenggat **`10 Des 2026`** disertai [README Transisi `Kebun Besar` → `Kebun Kecil`](catatan/README_TRANSISI_KEBUN_BESAR_KE_KEBUN_KECIL_CD2_CD3.md) agar menyambung ke `CD-1/CD-2`, lalu **digabung & dirombak total menjadi `CD1–3 Final` untuk SemPro PTA** (`7 Jan 2027`).

## Membuka di Antigravity atau AI lain

Buka folder clone `C:/Users/daffa/Documents/pta-jeruk-limau`. `AGENTS.md` menyimpan aturan dan konteks awal; `GEMINI.md` menjadi pintu masuk untuk Gemini/Antigravity. Setelah membaca konteks repo, cukup berikan kabar hasil bimbingan atau tugas berikutnya. Lihat [panduan chat baru dan peta folder](konteks-ai/MULAI_CHAT_BARU.md).

## Berkas utama

- [CD-1 Final ACC (PDF, 26 halaman)](dokumen/cd1/CD%201%20-%20ANALISIS%20PERMASALAHAN%20PENYIRAMAN%20MANUAL%20PADA%20KEBUN%20JERUK%20LIMAU%20DI%20CIBERES%20SUBANG.pdf)
- [CD-2 Final ACC (PDF, 26 halaman)](dokumen/cd2/CD%202%20-%20ANALISIS%20PERMASALAHAN%20PENYIRAMAN%20MANUAL%20PADA%20KEBUN%20JERUK%20LIMAU%20DI%20CIBERES%20SUBANG.pdf)
- [README Transisi & Perbandingan Kebun Besar vs Kebun Kecil (Jembatan CD-2 ke CD-3)](catatan/README_TRANSISI_KEBUN_BESAR_KE_KEBUN_KECIL_CD2_CD3.md)
- [Data Kebun Kecil & Zona Uji 1 (4 Pohon Sampel) + Kalibrasi Drone (23 Nov 2026)](catatan/DATA_KEBUN_KECIL_DAN_ZONA_4_POHON.md)
- [Sketsa Denah 2D Berskala Kebun Kecil & Zona Uji 1 (PNG)](catatan/denah_kebun_kecil_2d.png)
- [Hasil Survei Ciberes 15 Nov 2026 & Pembaruan ACC Lokasi](catatan/HASIL_SURVEI_CIBERES_15_NOV_2026.md)
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
  cd3/                       Draf lama CD-3 rekan (era Kebun Besar — tidak terpakai)
  draf/                      Arsip kerja CD-1, CD-2, & draf lama CD-3 (cd3/ & cd3_daffa/ non-aktif; CD-3 baru dibuat dari awal nanti)
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
