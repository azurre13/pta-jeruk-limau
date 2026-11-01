# Direktori Dokumen Capstone Design (CD-1 & CD-2)

Repositori dokumen proyek Capstone Design S1 Teknik Komputer, Telkom University:  
**"Analisis Permasalahan Penyiraman Manual pada Kebun Jeruk Limau di Ciberes Subang"**

Struktur subfolder dokumen diorganisasi secara sistematis berdasar tahapan Capstone Design:

```text
dokumen/
├── cd1/                        Dokumentasi Tahap CD-1 (Problem Definition)
│   ├── CD 1 - ANALISIS PERMASALAHAN PENYIRAMAN MANUAL PADA KEBUN JERUK LIMAU DI CIBERES SUBANG.pdf  (Dokumen Final Hasil ACC Dosen)
│   ├── CD1_Jeruk_Limau_Revisi3.docx                                                                (Naskah Word Revisi 3)
│   ├── CD1_Jeruk_Limau_Revisi3.pdf                                                                 (Naskah PDF 25 Halaman)
│   ├── LOGBOOK1 Catatan Diskusi Pembimbing.docx                                                    (Logbook Resmi Bimbingan)
│   └── LOGBOOK1 Catatan Diskusi Pembimbing.pdf                                                     (Logbook Resmi Bimbingan PDF)
└── cd2/                        Dokumentasi Tahap CD-2 (Constraints & Specifications)
    ├── CD2_Jeruk_Limau.docx    (Dokumen Word CD-2 Final 25 Halaman dengan Persamaan OMML)
    ├── CD2_Jeruk_Limau.pdf     (Dokumen PDF CD-2 Final 25 Halaman Siap Cetak/Kumpul)
    ├── DRAFT_CD2_Jeruk_Limau.md (Draf Naskah Lengkap Markdown dengan Rumus LaTeX)
    ├── build_full_cd2.py       (Skrip Pembangun Dokumen Otomatis)
    └── export_cd2_pdf.ps1      (Skrip Otomasi Ekspor PDF via Word COM)
```

## Ringkasan Tahapan

### 1. CD-1 (Problem Definition & Existing Solutions)
- **Fokus:** Analisis permasalahan penyiraman manual, topografi 3 lajur parit tanah sepanjang 100–117,52 m, ketiadaan listrik PLN, ketergantungan pompa bensin Pertalite (dan kegagalan modifikasi LPG akibat *overheating*), pemborosan upah buruh (Rp400.000/siklus atau Rp48,7 juta/tahun), serta analisis komparasi solusi eksisting.
- **Status Akademik:** Dokumen CD-1 telah di-ACC penuh oleh Dosen Pembimbing (Dr. Agung Nugroho Jati, S.T., M.T.).

### 2. CD-2 (Engineering Constraints, Specifications, and Verification Protocols)
- **Fokus:** Menetapkan 5 batasan rekayasa (*hard constraints* C-01 s.d. C-05), 14 butir spesifikasi kuantitatif (*engineering specifications* S-01 s.d. S-14), pemisahan anggaran prototipe mahasiswa (CAPEX TA $\le$ Rp6.000.000) vs. investasi kebun mitra (Rp12–15 juta; *Payback Period* 4–6 bulan), dan matriks rencana verifikasi/pengujian (*verification protocol* Tabel 5).
- **Dasar Penentuan:** Integrasi kebutuhan mitra kebun Ciberes, regulasi nasional (PP No. 20 Tahun 2006 tentang Irigasi & Permentan No. 49/2014), standar internasional (ANSI/ASAE S398.1:2021, ASAE EP405.1:2019, ISO 9261:2004, IEC 60529 / SNI IEC 60529:2014 IP65, IEC 62124 Off-Grid PV, IEC 60364-4-41 SELV, IEEE 1451.4), serta literatur agronomi & otomasi irigasi mutakhir (2016–2026).
- **Validasi Referensi:** 22 daftar pustaka berformat IEEE telah diverifikasi 100% asli dengan bukti berkas lokal dan DOI resmi.
- **Persamaan Matematis:** 7 persamaan rekayasa diformat menggunakan Equation Block native (Word OMML dan LaTeX).
