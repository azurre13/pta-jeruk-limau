# Rangkuman Diskusi Final dan Arah Perancangan Dokumen CD-2
**Proyek Capstone S1 Teknik Komputer - Fakultas Teknik Elektro, Universitas Telkom**  
*Topik: Analisis Permasalahan Penyiraman Manual pada Kebun Jeruk Limau di Ciberes Subang*  
*Dosen Pembimbing 1: Dr. Agung Nugroho Jati, S.T., M.T.*  
*Tanggal Penyusunan Final: 28 Oktober 2026*

---

## 1. Hakikat dan Posisi Strategis Dokumen CD-2

Dokumen **CD-2 (Spesifikasi dan Batasan Perancangan)** memiliki fungsi utama sebagai jembatan rekayasa (*engineering bridge*) antara **Analisis Permasalahan (CD-1)** dan **Rancangan Alternatif Solusi (CD-3)**.

* **Prinsip Netralitas Solusi (*Solution-Agnostic*):** CD-2 **tidak mengunci pilihan teknologi atau merek tertentu**. Menentukan apakah sistem menggunakan jaringan pipa mikroirigasi terotomasi, wahana/kereta penyiram bergerak berselang, atau sistem hibrida modular baru dilakukan secara komparatif di tahap CD-3.
* **Fungsi Utama CD-2:**
  1. Menetapkan **5 Batasan Mutlak (`C-01` s.d. `C-05`)**: Pagar pembatas yang tidak dapat ditawar akibat kondisi fisik tapak lahan (air sungai/parit bersedimen, ketiadaan listrik PLN, plafon biaya prototipe mahasiswa vs. mitra, proteksi IP65 & keselamatan SELV, serta ergonomi kerja & netralitas solusi).
  2. Menetapkan **14 Spesifikasi Kuantitatif (`S-01` s.d. `S-14`)**: Target performa kuantitatif lintas aspek (teknis, ekonomi, lingkungan, operasional) yang wajib dipenuhi oleh solusi apa pun yang dipilih pada CD-3.
  3. Menetapkan **Rencana Pengukuran & Prosedur Pengujian Verifikasi (`Tabel 5`)**: Prosedur uji baku, alat ukur terkalibrasi, dan kriteria kelulusan (*pass/fail criteria*) untuk membuktikan setiap spesifikasi tercapai pada CD-4.
* **Kepatuhan Rubrik Capstone FTE (Bobot Penilaian CLO2):**
  * Dasar Pemilihan Spesifikasi (20%): Didasarkan pada **4 pilar rujukan** (Kebutuhan Mitra Ciberes Audio 1 & 2, Standar Industri ASABE/ISO/IEC/IEEE/SNI, Regulasi PP No. 20/2006 & Permentan No. 49/2014 + Agronomi Jeruk Limau, serta Literatur & Paten Mutakhir 2016–2026).
  * Detail Spesifikasi (40%): 14 Spesifikasi kuantitatif terukur (`Tabel 3`) dilengkapi 7 persamaan matematis rekayasa (Persamaan 1 s.d. 7).
  * Pengukuran/Verifikasi (30%): Matriks rencana pengukuran, alat ukur terkalibrasi, dan prosedur uji langkah demi langkah (`Tabel 5`).
  * Anggaran (10%): Rincian plafon anggaran per modul (`Tabel 4`) yang memisahkan secara tegas **CAPEX Prototipe Mahasiswa ($\le$ Rp6.000.000; estimasi BOM $\sim$Rp4,6 juta)** dan **Kelayakan Investasi Kebun Mitra 500 Pohon (Rp12.000.000 – Rp15.000.000; *Payback Period* 3,4–4,3 bulan / target $\le$ 4–6 bulan)**.

---

## 2. Klarifikasi Anggaran: Prototipe Mahasiswa vs. Investasi Kebun Mitra

Berdasarkan **Buku Panduan Capstone FTE 2024 (Hal. 7, 11, 21, dan 22)**:

1. **Status Kemitraan (*Mitra Sasar*):**
   * Sesuai standar akreditasi internasional **IABEE**, mitra berfungsi sebagai penyedia permasalahan riil di masyarakat. Mahasiswa hanya diwajibkan membangun **1 unit prototipe uji (*Proof-of-Concept*)** pada skala representatif (*testbed*), bukan menghibahkan konstruksi kebun komersial 500 pohon secara penuh.
2. **Pemisahan Dua Sudut Pandang Anggaran (`Tabel 4`):**
   * **Plafon Anggaran Prototipe Tugas Akhir (CAPEX TA Mahasiswa: $\le$ Rp6.000.000):**
     * Estimasi riil *Bill of Materials* (BOM) sebesar **Rp4.600.000** ($\sim$Rp1.533.000 per mahasiswa untuk 3 anggota tim) ditambah cadangan kontingensi maksimal Rp1.400.000.
   * **Batas Kelayakan Investasi Sistem Kebun Mitra (Skala Penuh 500 Pohon: Rp12.000.000 – Rp15.000.000):**
     * Terhadap beban upah penyiraman manual eksisting sebesar Rp400.000/siklus (Rp4.000.000/bulan pada musim kemarau atau Rp48.700.000/tahun) dan target biaya operasional baru $\le$ Rp50.000/siklus (penghematan bersih $\Delta OPEX_{bulanan} = \text{Rp3.500.000/bulan}$ atau $\sim\text{Rp42.600.000/tahun}$), titik impas (*Payback Period*) tercapai dalam **3,43 hingga 4,29 bulan** (target spesifikasi $\le$ **4–6 bulan**).

---

## 3. Ringkasan Matriks 5 Batasan (C-01 s.d. C-05) & 14 Spesifikasi (S-01 s.d. S-14)

### A. 5 Batasan Rekayasa Mutlak (*Hard Constraints*)
- **C-01**: Kompatibilitas Sumber Air Permukaan (Sungai 20,54 m) dan Parit Tanah Bersedimen.
- **C-02**: Kemandirian Pasokan Energi (*Off-Grid*) Tanpa Listrik PLN & Bebas *Overheating*.
- **C-03**: Plafon Biaya Prototipe Mahasiswa ($\le$ Rp6.000.000) & Kelayakan Investasi Mitra (Rp12–15 Juta).
- **C-04**: Ketahanan Lingkungan Terbuka Tropis (Minimal IP65) & Keselamatan Tegangan Rendah ($\text{SELV} \le 48\text{ V DC}$).
- **C-05**: Ergonomi Kerja (Mitigasi Skor REBA 10), Kemudahan Operasi 1 Tombol, & Netralitas Solusi (*Solution-Agnostic*).

### B. 14 Spesifikasi Kuantitatif Solusi (`Tabel 3`)

| Kategori Aspek | Kode | Parameter Spesifikasi | Nilai Target & Toleransi | Satuan |
|---|:---:|---|---|:---:|
| **Teknis** | S-01 | Akurasi Dosis Volume Air per Pohon | $10\text{--}15\ (\pm 5\%)$ | Liter/pohon |
| **Teknis** | S-02 | Koefisien Keseragaman Distribusi ($CU$) | $\ge 85{,}0$ | % |
| **Teknis** | S-03 | Durasi Total Siklus Penyiraman Kebun | $\le 4{,}0\ (\le 240\text{ menit})$ | Jam/siklus |
| **Teknis** | S-04 | Zona Basah Akar & Ketepatan Sasaran Pohon | $r = 0{,}5\text{--}0{,}8\text{ m}$; $d = 20\text{--}40\text{ cm}$; Sasaran $\ge 85\%$ | m; cm; % |
| **Teknis** | S-05 | Derajat Filtrasi Fisik Partikulat Air | $\ge 120$ (Menahan partikel $\ge 130$) | mesh ($\mu\text{m}$) |
| **Teknis** | S-06 | Ketahanan Cadangan Energi Mandiri (*Autonomy*) | $\ge 8{,}0$ (Min. 2 siklus penuh) | Jam operasi |
| **Teknis** | S-07 | Derajat Proteksi Selungkup & Tegangan | IP65 (Suhu $20\text{--}55\ ^\circ\text{C}$; SELV $\le 48\text{ V DC}$) | Rating ($^\circ\text{C}$; V) |
| **Ekonomi** | S-08 | Plafon Biaya Prototipe Mahasiswa vs. Investasi Mitra | Prototipe TA $\le 6.000.000$ (BOM $\sim 4{,}6\text{ Jt}$); Mitra $\le 12\text{--}15\text{ Jt}$ | Rupiah (Rp) |
| **Ekonomi** | S-09 | Biaya Operasional per Siklus (OPEX) | $\le 50.000$ (Penghematan $\ge 87{,}5\%$) | Rp/siklus |
| **Ekonomi** | S-10 | Periode Pengembalian Modal Mitra ($PP$) | $\le 4\text{--}6$ (Eksak: 3,43–4,29 bulan) | Bulan |
| **Lingkungan**| S-11 | Efisiensi Aplikasi Air Irigasi ($\eta_a$) | $\ge 80{,}0$ | % |
| **Lingkungan**| S-12 | Emisi Gas Buang & Residu Oli di Zona Tajuk | $0$ (Bebas emisi CO/HC & ceceran oli) | g/kWh |
| **Operasional**| S-13 | Kemudahan Pengoperasian Operator Lokal | Kendali 1 Tombol (Waktu ajar $\le 30$) | Menit |
| **Operasional**| S-14 | Durasi Pemeliharaan Rutin Saringan | $\le 15\text{--}20$ (Perkakas tangan umum) | Menit/pekan |
