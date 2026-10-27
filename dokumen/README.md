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
    ├── CD2_Jeruk_Limau.docx    (Dokumen Word CD-2 Final dengan Persamaan OMML)
    ├── CD2_Jeruk_Limau.pdf     (Dokumen PDF CD-2 Final 22 Halaman Siap Cetak/Kumpul)
    ├── DRAFT_CD2_Jeruk_Limau.md (Draf Naskah Lengkap Markdown dengan Rumus LaTeX)
    ├── build_full_cd2.py       (Skrip Pembangun Dokumen Otomatis)
    └── export_cd2_pdf.ps1      (Skrip Otomasi Ekspor PDF via Word COM)
```

## Ringkasan Tahapan

### 1. CD-1 (Problem Definition & Existing Solutions)
- **Fokus:** Analisis permasalahan penyiraman manual, topografi 3 lajur parit tanah sepanjang 100 m, ketiadaan listrik PLN, ketergantungan pompa bensin Pertalite, pemborosan upah buruh (Rp400.000/siklus atau Rp48,7 juta/tahun), serta analisis komparasi solusi eksisting.
- **Status Akademik:** Dokumen CD-1 telah di-ACC penuh oleh Dosen Pembimbing (Dr. Agung Nugroho Jati, S.T., M.T.).

### 2. CD-2 (Engineering Constraints, Specifications, and Verification Protocols)
- **Fokus:** Menetapkan 5 batasan rekayasa (*hard constraints* C-01 s.d. C-05), 14 butir spesifikasi kuantitatif (*engineering specifications* S-01 s.d. S-14), dan matriks rencana verifikasi/pengujian (*verification protocol*).
- **Dasar Penentuan:** Integrasi kebutuhan mitra kebun Ciberes, regulasi nasional (PP No. 20 Tahun 2006 tentang Irigasi), standar internasional (ASAE S398.1, ASAE EP405.1, ISO 9261:2004, IEC 60529 / SNI IEC 60529:2014 IP65, IEC 62124 Off-Grid PV, IEEE 1451), serta literatur agronomi FAO-56 & Florida Citrus Extension.
- **Validasi Referensi:** 22 daftar pustaka telah diverifikasi menyeluruh dengan tautan langsung DOI dan repositori resmi.
- **Persamaan Matematis:** Diformat rapi menggunakan Equation Block native (Word OMML dan LaTeX).
