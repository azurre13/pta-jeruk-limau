# Rangkuman Diskusi Final dan Arah Perancangan Dokumen CD-2
**Proyek Capstone S1 Teknik Komputer - Fakultas Teknik Elektro, Universitas Telkom**  
*Topik: Sistem Irigasi Presisi Mandiri Energi pada Kebun Jeruk Limau di Ciberes, Subang*  
*Tanggal Penyusunan: 28 Oktober 2026*

---

## 1. Hakikat dan Posisi Strategis Dokumen CD-2

Dokumen **CD-2 (Spesifikasi dan Batasan Desain)** memiliki fungsi utama sebagai jembatan rekayasa (*engineering bridge*) antara **Analisis Permasalahan (CD-1)** dan **Rancangan Alternatif Solusi (CD-3)**.

* **Bukan Memilih Desain Akhir:** CD-2 **tidak boleh mengunci pilihan teknologi atau merek tertentu** (*solution-agnostic*). Menentukan apakah sistem menggunakan jaringan pipa tetes, robot bergerak, atau kereta semi-otonom baru dilakukan di tahap CD-3.
* **Fungsi Utama CD-2:**
  1. Menetapkan **Batasan (*Constraints*)**: Pagar pembatas yang tidak dapat ditawar akibat kondisi fisik tapak lahan, keterbatasan sumber daya, dan profil pengguna.
  2. Menetapkan **Spesifikasi (*Specifications*)**: Target performa kuantitatif yang wajib dipenuhi oleh solusi apa pun yang akan dipilih nantinya.
  3. Menetapkan **Rencana Verifikasi (*Verification Protocols*)**: Prosedur, alat ukur terkalibrasi, dan kriteria kelulusan pengujian untuk membuktikan setiap spesifikasi tercapai.
* **Kepatuhan Rubrik Capstone FTE (Bobot Penilaian):**
  * Dasar Pemilihan Spesifikasi (20%): Wajib didasarkan pada **lebih dari 2 pilar rujukan** (Kebutuhan Mitra, Standar Industri, Regulasi/Agronomi, dan Literatur Mutakhir).
  * Detail Spesifikasi (40%): Spesifikasi **kuantitatif terukur** dengan penjelasan komprehensif lintas aspek (Teknis, Ekonomi, Lingkungan, Operasional).
  * Pengukuran/Verifikasi (30%): Memuat **parameter, alat ukur spesifik, dan mekanisme pengujian**.
  * Anggaran (10%): Memuat **plafon anggaran, detail per modul, dan justifikasi logis**.

---

## 2. Klarifikasi Anggaran: Desain Mitra vs. Prototipe Mahasiswa

Salah satu kekhawatiran terbesar tim mahasiswa adalah ketakutan menanggung biaya infrastruktur kebun komersial mitra yang tidak didanai. Berdasarkan **Buku Panduan Capstone FTE 2024 (Hal. 7, 11, 21, dan 22)**:

1. **Status Kemitraan (Mitra Sasar):**
   * Sesuai standar akreditasi internasional **IABEE**, mitra berfungsi sebagai penyedia permasalahan riil di masyarakat. Mitra tidak bertindak sebagai investor yang membiayai mahasiswa, dan mahasiswa **bukan kontraktor yang bertugas membelikan instalasi komersial kebun**.
2. **Pemisahan Dua Sudut Pandang Anggaran:**
   * **Target Plafon Biaya Sistem Kebun (CAPEX Mitra: Rp10.000.000 – Rp15.000.000):**
     * Merupakan analisis kelayakan teknis-ekonomis di atas kertas (*engineering feasibility study*).
     * Membuktikan bahwa jika sistem diterapkan penuh untuk 500 pohon, biaya investasi akan tertutup (*payback period*) dalam kurun waktu $\le 4\text{--}6$ bulan berkat penghematan upah manual (yang saat ini mencapai Rp400.000/kegiatan atau skenario Rp48,7 juta/tahun).
   * **Plafon Anggaran Prototipe Tugas Akhir (RAB Mahasiswa: Maksimal Rp6.000.000):**
     * Merupakan biaya riil yang dikeluarkan tim mahasiswa (3 orang) untuk merakit 1 unit purwarupa fungsional (*Proof of Concept / Testbed*).
     * Nilai Rp6.000.000 (setara Rp2.000.000/mahasiswa) adalah *sweet spot* yang sangat rasional, mencakup: catu daya surya/baterai, pompa fluida skala uji, mikrokontroler, selungkup IP65, alat ukur volumetrik, dan dana darurat/kontingensi 15%.
3. **Batas Ruang Lingkup Luaran Fisik (CD-4 & CD-5):**
   * Buku Panduan Capstone (Hal. 22) secara eksplisit menegaskan bahwa jika implementasi fisik skala penuh melibatkan lahan yang sangat luas atau biaya yang besar, pengujian dilakukan pada **prototipe skala representatif (testbed beberapa pohon uji)**.
   * Prototipe tersebut merupakan aset tugas akhir mahasiswa yang dibawa ke kebun mitra hanya untuk pengambilan data pengujian, lalu **dibawa pulang kembali ke kampus** untuk didemokan dalam Sidang Capstone.

---

## 3. Analisis Kondisi Lahan (Foto CD-1) dan Dinamika Pilihan Solusi

Berdasarkan inspeksi foto tapak lahan kebun Ciberes (`sumber/dokumentasi/foto/`), ditemukan sejumlah karakteristik fisik kritis:
* Parit tanah galian terbuka berliku (lebar 40–60 cm, kedalaman 20–30 cm) yang berubah menjadi lumpur becek saat tergenang air.
* Pematang tanah gembur tidak rata di kanan-kiri parit dengan kemiringan menuju saluran.
* Ranting pohon jeruk limau (tinggi 1–1,3 m) rimbun dan menjorok ke koridor jalan.
* Terdapat parit penghubung melintang (pertemuan berbentuk "+") yang memotong kontinuitas lintasan.

### Perbandingan Karakteristik Solusi (Bahan Komparasi CD-3):
1. **Jaringan Perpipaan Tetap (Fixed Piping / Drip / Micro-Sprinkler):**
   * *Tantangan Hidrolika:* Membentang pipa 100 meter untuk menyiram puluhan pohon sekaligus rentan mengalami penurunan tekanan (*head loss*). Tanpa nozzle *Pressure Compensating* (PC), pohon di pangkal pipa akan kelebihan air sedangkan pohon di ujung kekurangan air.
   * *Tantangan Sedimen:* Air sungai Ciberes membawa partikulat lumpur yang rawan menyumbat emiter mikro, sehingga butuh filtrasi fisik bertingkat.
   * *Keunggulan:* Tidak terpengaruh kondisi tanah becek di lapangan dan mengeliminasi 100% kebutuhan pekerja berkeliling.
2. **Wahana / Robot Bergerak (Mobile Irrigation Unit):**
   * *Keunggulan Hidrolika:* Jarak pompa ke nozzle semprot hanya 1–2 meter, sehingga **tekanan air dijamin 100% konstan** di setiap pohon.
   * *Efisiensi Sensor:* Hanya membutuhkan **1 unit sensor aliran (flow meter)** terpusat untuk menakar dosis 10–15 L/pohon secara presisi sebelum berpindah ke pohon berikutnya.
   * *Mekanisme Nozzle Ganda:* Dapat menggunakan 2 nozzle (sisi kanan dan kiri) yang menyiram 2 barisan pohon secara simultan.
   * *Tantangan Fisik:* Memerlukan traksi roda/lintasan yang mampu melintasi tanah becek, atau mengasumsikan penyiapan permukaan lintasan (*site/track preparation*) sebagai bagian dari cetak biru desain.

---

## 4. Solusi Deteksi Posisi Pohon yang Tidak Teratur (*Tree Detection*)

* **Fakta Lapangan:** Jarak tanam dan posisi pohon jeruk limau di kebun Ciberes tidak berada pada garis lurus sempurna pabrikan (*non-uniform alignment*).
* **Efisiensi Komputasi:** Menggunakan komputer visi berdaya tinggi (seperti NVIDIA Jetson) memerlukan biaya perangkat keras yang mahal (Rp4–8 juta) serta konsumsi daya baterai yang besar di lingkungan terbuka.
* **Alternatif Rekayasa:** Penggunaan larik sensor jarak optik/akustik (*Ultrasonic Array* atau *ToF LiDAR*) atau modul mikrokontroler visi hemat daya (seperti ESP32-S3 Cam / Raspberry Pi ringan) mampu mendeteksi profil jarak tajuk/batang pohon dengan biaya sangat rendah (< Rp300 ribu) serta kebal terhadap gangguan silau sinar matahari (*sunlight glare*).
* **Formulasi CD-2:** Spesifikasi dirumuskan secara fungsional: **"Akurasi Deteksi Keberadaan Tanaman $\ge 85\%$ pada rentang jarak deteksi 0,5–1,5 meter"** tanpa mengunci komponen sensor.

---

## 5. Kebijakan Kemutakhiran Pustaka (2016–2026)

Menindaklanjuti arahan pengguna dan kaidah penulisan ilmiah IABEE, daftar pustaka CD-2 **tidak lagi menggunakan referensi usang tahun 1980-an/1990-an**, melainkan memprioritaskan literatur mutakhir 10 tahun terakhir (2016–2026):
1. **Paten Robot Irigasi Parit:** Paten CN115804333A (Maret 2023) – *Farmland Irrigation Robot, Its Control Assembly, and Irrigation Method*.
2. **Jurnal Robot Sprinkler:** Nabil Elkaoud dkk., *Eng* (MDPI, 2025) – *Efficient and Effective Irrigation Water Management Using Sprinkler Robot*.
3. **Jurnal Catu Daya Surya Pertanian:** Nurwidiana, Fatmawati, & Rifa'i, *Jurnal Teknologi Pertanian Andalas* (2022) – *Perancangan Alat Penyiram Lahan Bawang Berbasis Solar Fotovoltaik*.
4. **Navigasi Robot Perkebunan:** A. Jiang & T. Ahamed, *Sensors* (2023) – *Autonomous Navigation for Agricultural Robots*.
5. **Standar Keseragaman Irigasi Mikro:** ASABE S398.1 (Revisi 2021) & ASABE EP405.1 (Revisi 2019).
6. **Standar Proteksi Selungkup Lingkungan:** IEC 60529 / SNI IEC 60529:2014.
7. **Panduan Manajemen Irigasi Jeruk:** D. M. Kadyampakeni dkk., *UF/IFAS Extension Citrus Production Guide* (Edisi 2021/2026).
8. **Morfologi Jeruk Limau:** R. Budiarto dkk., *Journal of Tropical Crop Science* (2017).
9. **Karakteristik Sensor Lengas Tanah:** J. M. Domínguez-Niño dkk., *Sensors* (2019).

---

## 6. Ringkasan Matriks Spesifikasi CD-2

| Kategori Aspek | Kode | Parameter Spesifikasi | Nilai Target & Toleransi | Satuan |
|---|:---:|---|---|:---:|
| **Teknis** | S-01 | Akurasi Dosis Volume Air per Pohon | 10 – 15 ($\pm 10\%$) | Liter/pohon |
| **Teknis** | S-02 | Koefisien Keseragaman Distribusi (CU) | $\ge 80,0$ | % |
| **Teknis** | S-03 | Durasi Total Siklus Penyiraman Kebun | $\le 4,5$ | Jam/siklus |
| **Teknis** | S-04 | Akurasi Deteksi Keberadaan Pohon | $\ge 85,0$ (Jarak: 0,5–1,5) | % (meter) |
| **Teknis** | S-05 | Derajat Proteksi Filtrasi Partikulat | $\ge 120$ (Partikel $\le 130$) | mesh ($\mu\text{m}$) |
| **Teknis** | S-06 | Ketahanan Catu Daya Mandiri (*Autonomy*) | $\ge 6,0$ (Min. 1 siklus penuh) | Jam operasi |
| **Teknis** | S-07 | Tingkat Proteksi Selungkup Luar (*Ingress*) | Standar IP65 (Suhu: 20–50) | Rating ($^\circ\text{C}$) |
| **Ekonomi** | S-08 | Plafon Biaya Prototipe Tim (CAPEX TA) | $\le 6.000.000$ (Realisasi $\approx 4,6$ Jt) | Rupiah |
| **Ekonomi** | S-09 | Estimasi Investasi Sistem Mitra Kebun | $\le 12.000.000\text{--}15.000.000$ | Rupiah |
| **Ekonomi** | S-10 | Pengurangan Biaya Upah Operasional | $\ge 75,0$ (Hemat $\ge \text{Rp300.000/kegiatan}$) | % |
| **Ekonomi** | S-11 | Periode Pengembalian Modal (*Payback Period*) | $\le 4\text{--}6$ | Bulan |
| **Lingkungan**| S-12 | Efisiensi Penggunaan Air Irigasi ($\eta_a$) | $\ge 80,0$ | % |
| **Lingkungan**| S-13 | Emisi Polutan Kimia di Area Tajuk | 0 (Bebas ceceran oli & emisi gas) | g/kWh |
| **Operasional**| S-14 | Kemudahan Pengoperasian bagi Operator | Waktu adaptasi operator $\le 30$ | Menit |
| **Operasional**| S-15 | Waktu Pembersihan Saringan / Pemeliharaan | $\le 15$ (Perkakas tangan umum) | Menit/pekan |

Dokumen ini menjadi acuan final sebelum dilakukan penyusunan dokumen naskah resmi `dokumen/CD2_Jeruk_Limau.docx`.

