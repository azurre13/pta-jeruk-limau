# Direktori Dokumen Capstone Design (CD-1, CD-2, & Draf CD-3)

**Tanggal Pembaruan:** 14 November 2026  
Repositori dokumen proyek Capstone Design S1 Teknik Komputer, Telkom University:  
**"Analisis Permasalahan Penyiraman Manual pada Kebun Jeruk Limau di Ciberes Subang"**

Struktur subfolder dokumen diorganisasi berdasarkan tahapan Capstone Design dan status draf vs berkas final:

```text
dokumen/
├── cd1/                        Dokumentasi Tahap CD-1 (Final ACC, PDF 26 halaman)
├── cd2/                        Dokumentasi Tahap CD-2 (Final ACC, PDF 26 halaman)
├── cd3/                        Berkas CD-3 draf/kolaborasi tim (Qarnie / Garnie, PDF 34 halaman)
└── draf/                       Arsip Naskah Kerja, Draf Revisi, & Skrip Pembangun
    ├── cd1/                    Draf naskah Word CD-1, PDF awal–revisi 3 (21–25 hlm), & logbook
    ├── cd2/                    Draf naskah Word CD-2, skrip build_full_cd2.py, template, & MD draf
    ├── cd3/                    Skrip & draf CD-3 rekan tim + tabel perbandingan (34 hlm / 6 hlm)
    └── cd3_daffa/              Workspace terpisah usulan CD-3 & tabel (23 hlm / 4 hlm — menunggu hasil survei Minggu)
```

## Ringkasan Tahapan

### 1. CD-1 (Problem Definition & Existing Solutions)
- **Fokus:** Analisis permasalahan penyiraman manual, topografi 3 lajur parit tanah sepanjang ±100 m (garis citra koridor `117,52 m`, jarak ke saluran air `20,54 m`), ketiadaan listrik PLN, ketergantungan **pompa mesin bensin Pertalite Alkon 2 inci** (disertai catatan sejarah uji coba modifikasi LPG 3 kg yang dihentikan karena mesin mengalami *overheating*), pemborosan upah buruh (`Rp400.000/siklus` atau skenario `Rp48,7 juta/tahun`), serta analisis komparasi solusi eksisting.
- **Status Akademik:** Dokumen CD-1 telah di-ACC penuh oleh Dosen Pembimbing (Dr. Agung Nugroho Jati, S.T., M.T.) dalam berkas PDF **26 halaman** di `dokumen/cd1/`.

### 2. CD-2 (Engineering Constraints, Specifications, and Verification Protocols)
- **Fokus:** Menetapkan 5 batasan rekayasa (*hard constraints* `C-01` s.d. `C-05`), 14 butir spesifikasi kuantitatif (*engineering specifications* `S-01` s.d. `S-14`), pemisahan anggaran prototipe uji mahasiswa (`S-08 <= Rp5.000.000` untuk `C-03` min. 1 lajur `15–20 pohon` pada bentang operasional `>= 25 m`) vs. proyeksi skala penuh kebun (`<= Rp18.000.000`, `OPEX <= Rp50.000/siklus`, *Payback Period* `12–18 bulan`), serta matriks rencana verifikasi/pengujian.
- **Catatan Koreksi Angka Draf:** Catatan awal sebelum finalisasi sempat menyebut pagu Rp6 juta dan Rp12–15 juta; acuan resmi yang berlaku adalah angka dalam PDF final `CD 2` di `dokumen/cd2/` (**26 halaman**).

### 3. CD-3 (Status Draf Pra-Survei)
- **Status Saat Ini:** Tersedia draf rekan (`dokumen/cd3/` & `dokumen/draf/cd3/`) serta workspace terpisah [`dokumen/draf/cd3_daffa/`](draf/cd3_daffa/). Penyelarasan akhir `CD-3` (arsitektur pompa irigasi vs tampungan, kalibrasi dimensi petak uji `C-03 >= 25 m`, rekonsiliasi jumlah zona skala penuh agar patuh `S-03 <= 4,0 jam` dibanding asumsi draf `10 zona / 960 L/jam`, keputusan `0–2` sensor tanah di samping *Flow Meter*, konsumsi Pertalite nyata, serta koreksi sisa teks LPG pada `build_cd3_daffa.py` baris `554`) **sengaja ditahan** hingga survei lapangan hari Minggu dan pembaruan [Kajian Sumber Air & Pompa](../catatan/KAJIAN_SUMBER_AIR_IRIGASI_DAN_POMPA.md) serta [Rangkuman Q&A Scope & Zonasi](../catatan/RINGKUMAN_QNA_SCOPE_DAN_ZONASI_PRA_SURVEI.md) selesai.
