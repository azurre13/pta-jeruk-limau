# Direktori Dokumen Capstone Design (CD-1, CD-2, & Draf CD-3)

**Tanggal Pembaruan:** 22 November 2026  
Repositori dokumen proyek Capstone Design S1 Teknik Komputer, Telkom University:  
**"Analisis Permasalahan Penyiraman Manual pada Kebun Jeruk Limau di Ciberes Subang"** *(judul resmi awal `CD-1`/`CD-2`; berpotensi disesuaikan pada tahap gabung-rombak total `CD1–3 Final` setelah perluasan visi optimalisasi pertumbuhan pohon & buah di `Kebun Kecil`)*

Struktur subfolder dokumen diorganisasi berdasarkan tahapan Capstone Design dan status draf vs berkas final:

```text
dokumen/
├── cd1/                        Dokumentasi Tahap CD-1 (Final ACC, PDF 26 halaman — dikumpulkan, jangan ubah dulu)
├── cd2/                        Dokumentasi Tahap CD-2 (Final ACC, PDF 26 halaman — dikumpulkan, jangan ubah dulu)
├── cd3/                        Draf lama CD-3 rekan tim (pra-Kebun Kecil — TIDAK TERPAKAI, jangan dilanjutkan)
└── draf/                       Arsip Naskah Kerja, Draf Revisi, & Skrip Pembangun
    ├── cd1/                    Draf naskah Word CD-1, PDF awal–revisi 3 (21–25 hlm), & logbook
    ├── cd2/                    Draf naskah Word CD-2, skrip build_full_cd2.py, template, & MD draf
    ├── cd3/                    Draf lama CD-3 rekan tim & tabel (TIDAK TERPAKAI — era Kebun Besar)
    └── cd3_daffa/              Berisi draf lama pra-Kebun Kecil (TIDAK TERPAKAI); CD-3 baru akan dibuat dari awal nanti (belum dibuat sekarang)
```

## Ringkasan Tahapan

### 1. CD-1 (Problem Definition & Existing Solutions)
- **Fokus:** Analisis permasalahan penyiraman manual, topografi 3 lajur parit tanah sepanjang ±100 m (garis citra koridor `117,52 m`, jarak ke saluran air `20,54 m`), ketiadaan listrik PLN, ketergantungan **pompa mesin bensin Pertalite Alkon 2 inci** (disertai catatan sejarah uji coba modifikasi LPG 3 kg yang dihentikan karena mesin mengalami *overheating*), pemborosan upah buruh (`Rp400.000/siklus` atau skenario `Rp48,7 juta/tahun`), serta analisis komparasi solusi eksisting.
- **Status Akademik:** Dokumen CD-1 telah di-ACC penuh oleh Dosen Pembimbing (Dr. Agung Nugroho Jati, S.T., M.T.) dalam berkas PDF **26 halaman** di `dokumen/cd1/`.

### 2. CD-2 (Engineering Constraints, Specifications, and Verification Protocols)
- **Fokus:** Menetapkan 5 batasan rekayasa (*hard constraints* `C-01` s.d. `C-05`), 14 butir spesifikasi kuantitatif (*engineering specifications* `S-01` s.d. `S-14`), pemisahan anggaran prototipe uji mahasiswa (`S-08 <= Rp5.000.000` untuk `C-03` min. 1 lajur `15–20 pohon` pada bentang operasional `>= 25 m`) vs. proyeksi skala penuh kebun (`<= Rp18.000.000`, `OPEX <= Rp50.000/siklus`, *Payback Period* `12–18 bulan`), serta matriks rencana verifikasi/pengujian.
- **Catatan Koreksi Angka Draf:** Catatan awal sebelum finalisasi sempat menyebut pagu Rp6 juta dan Rp12–15 juta; acuan resmi yang berlaku adalah angka dalam PDF final `CD 2` di `dokumen/cd2/` (**26 halaman**).

### 3. CD-3 & Roadmap Penyelarasan ke `CD1–3 Final` (SemPro PTA)
- **Status Saat Ini (`22 November 2026`):** Seluruh berkas `CD-3` yang saat ini berada di `dokumen/cd3/`, `dokumen/draf/cd3/`, dan isi lama `dokumen/draf/cd3_daffa/` adalah **draf lama era `Kebun Besar` yang tidak terpakai lagi** (*non-aktif*, dibiarkan sebagai arsip saja dan tidak dilanjutkan). **`CD-3` yang baru belum dibuat sekarang dan akan dibuat dari awal** berbasis `Kebun Kecil` (`1 Zona = 4 Pohon Sampel`) saat pengguna memberi arahan mulai. Sementara itu, data historis `Kebun Besar` pada `CD-1` (`26 hlm`) dan `CD-2` (`26 hlm`) tetap dipertahankan utuh (tidak direvisi sekarang) karena sudah dikumpulkan terlebih dahulu.
- **Aturan Penulisan `CD-3` (`CLO3 - CD3-1`, Tenggat `Kamis, 10 Desember 2026`):** Saat menyusun `CD-3`, wajib menyertakan **catatan transisi perubahan lapangan & perbandingan 2 kebun** mengacu pada [README Transisi `Kebun Besar` → `Kebun Kecil`](../catatan/README_TRANSISI_KEBUN_BESAR_KE_KEBUN_KECIL_CD2_CD3.md) serta [Data Kebun Kecil & Zona 4 Pohon](../catatan/DATA_KEBUN_KECIL_DAN_ZONA_4_POHON.md) (mencakup kendala biaya/PLTS `Kebun Besar`, tebing `4–5 m` & jarak `10 m`, arus irigasi deras saat hujan, saluran irigasi bukan tanah mitra, rawan pencurian, serta kondisi `Kebun Kecil`: sumur baru tanpa toren masih disedot **Alkon bensin** + **`2` pekerja × `Rp100.000` tiap `3–4 hari`** tanpa hujan, air `10–15 L/pohon`, listrik tersedia, serta tujuan memaksimalkan pertumbuhan & buah).
- **Tahap Gabung & Rombak Total (`CLO4 - CD3-2 Gabungan`, Tenggat `Kamis, 7 Januari 2027` · `SemPro: 11–16 Januari 2027`):** Setelah `CD-1`, `CD-2`, dan `CD-3` terkumpul seluruhnya, ketiga dokumen akan **digabung dan dirombak total** (termasuk revisi `CD-1`/`CD-2` dan penyesuaian judul proyek) agar naskah akhir SemPro konsisten sepenuhnya dari Bab 1 sampai Bab 3.
