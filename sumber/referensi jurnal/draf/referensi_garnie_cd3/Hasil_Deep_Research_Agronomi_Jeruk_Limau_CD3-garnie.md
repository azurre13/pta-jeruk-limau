# Hasil Deep Research Agronomi *Citrus amblycarpa*, Perakaran, Kebutuhan Air, & Kalibrasi Sensor v1.2 (CD-3 `Kebun Kecil`)

**Tanggal Disimpan:** 25 November 2026  
**Status Verifikasi:** 7 DOI jurnal internasional terverifikasi langsung via **Crossref API** (`10.3389/fhort.2025.1552283`, `10.36253/phyto-17259`, `10.32945/atr4727.2025`, `10.1079/ab.2025.0025`, `10.15446/dyna.v88n219.94121`, `10.22271/phyto.2020.v9.i5aj.12726`, `10.3390/s26092692`), dilengkapi literatur nasional *Citrus amblycarpa* & pedoman Balitjestro/Balitbangtan RI.

---

## Ringkasan Eksekutif & Batasan Ilmiah untuk CD-3

1. **Pemisahan Ketat Bukti Spesifik *C. amblycarpa* vs *Citrus* Umum:**
   - Riset terbuka khusus *Citrus amblycarpa* (jeruk limau/sambal) sejauh ini baru mencakup karakterisasi morfologi perdu, sifat poliembrioni biji sebesar **27,85%**, profil asam sitrat/minyak atsiri buah, dan produktivitas hamparan **7,84 ton/ha** di Majalengka.
   - Data kedalaman akar serabut, koefisien tanaman ($K_c$), takaran air harian (L/pohon/hari), dosis NPK baku, dan ambang lengas kritis khusus *C. amblycarpa* **belum tersedia** di literatur terbuka—sehingga CD-3 mengadopsi acuan ilmiah genus *Citrus* (Balitjestro/BSIP & jurnal internasional) yang disesuaikan dengan habitus perdu *C. amblycarpa* serta sifat tanah merah berliat Subang.
2. **Implikasi Langsung ke Desain Hardware & Kontrol (`4` Pohon Sampel):**
   - **Posisi & kedalaman sensor:** Tanam sensor *Capacitive v1.2* pada kedalaman **15–20 cm** (pusat zona akar serabut aktif `0–30 cm`, terhindar bias penguapan 5 cm teratas), berjarak **10–15 cm** dari titik penetes dan **15–40 cm** dari batang sesuai lebar tajuk.
   - **Ketahanan & kalibrasi sensor:** Wajib dilapisi epoksi/karet kedap air (sensor murah terkorosi berat dalam ~6 bulan) dan dikalibrasi individual per titik tanah merah Ciberes memakai metode gravimetri oven `105 °C` 24 jam + regresi non-linear (mis. model hiperbolik $y = 1/(a+bx)$).
   - **Diferensiasi dosis hari tanpa hujan (batas kendali `55–65% FC` hingga tepat `< FC`):**
     - **Sampel 3 & 4 (`210–250 cm`):** `10–12 L/pohon/hari`
     - **Sampel 2 (`100 cm`):** `5–6 L/pohon/hari`
     - **Sampel 1 (`46 cm`, kerdil):** pembatasan rekayasa `1,5–2,0 L/pohon/hari` hanya saat mendekati ambang kering *(memerlukan pengaturan katup/jadwal terpisah atau debit emiter berbeda dari Sampel 3–4 agar tidak memicu hipoksia/busuk akar)*.
3. **Batasan Klaim Ketimpangan Umur 16 Bulan (`46 cm` vs `250 cm`):**
   - Ketimpangan pada umur tanam serentak berasal dari kombinasi **4 faktor non-irigasi**: (a) heterogenitas bibit / semai zigotik (`27,85%` poliembrioni) atau cacat pangkal akar (*coiled root*), (b) pemadatan tanah urugan & sisa sampah/puing `> 15%`, (c) kegagalan drainase makro akibat parit `6 cm` (memicu hipoksia & *Phytophthora*), dan (d) naungan kanopi di lahan rapat (`~6,45–6,54 m²/pohon`).
   - Sistem irigasi tetes CD-3 mencegah stres kekeringan dan *waterlogging* akibat penyiraman, namun pemulihan total tetap memerlukan pendampingan mitra: **pendalaman parit drainase (`30–50 cm`), dolomit/kompos bila pH masam, pemangkasan cabang dalam/pucuk (*Bujangseta*), dan cek fisik akar Sampel 1**.

---

## Ringkasan Evaluasi 5 Topik Agronomi

| Topik | Fakta Terverifikasi (*C. amblycarpa* / Acuan *Citrus*) | Evaluasi & Implikasi Langsung pada `Kebun Kecil` (`CD-3`) |
|---|---|---|
| **1. Morfologi & Zona Akar** | Habitus perdu berbatang bulat, berbuah sepanjang tahun (*C. amblycarpa*); akar serabut aktif irigasi tetes terpusat pada kedalaman `0–30 cm` dan radius `≤ 60 cm` dari emiter. | Sensor ditanam **`15–20 cm`**; `2× PC Dripper` dipasang berseberangan di bawah *drip line* (`15–20 cm` untuk `P1`, `25–30 cm` untuk `P2`, `40–50 cm` untuk `P3–P4`), dilarang menempel batang. |
| **2. Syarat Tumbuh & Ambang Tanah** | Elevasi `0–400 m dpl`, suhu `20–28 °C` (`25–31 °C` tajuk, `22–27 °C` tanah), `pH 5,5–6,5`, bahan kasar `< 15%`, muka air tanah `≥ 50–75 cm`; cekaman `< 50%` air tersedia, kritis `55–65% FC`, jenuh `> FC` aktifkan *Phytophthora*. | Subang cocok elevasi/suhu, tetapi **parit `6 cm`** gagal mengatuskan zona `0–30 cm` saat hujan, urugan sampah berisiko bahan kasar `> 15%` & masam (`pH < 5`), dan kepadatan `~6,5 m²/pohon` memicu naungan. |
| **3. Perbanyakan & Ketimpangan 16 Bln** | Biji *C. amblycarpa* poliembrioni `27,85%` (mayoritas monoembrio/zigotik berfase juvenil panjang); okulasi/cangkok memintas fase juvenil; bibit berkualitas menentukan `> 50%` hasil; akar *coiled* wajib ditolak. | Menjelaskan ilmiah mengapa `P1` kerdil & `P2` berbuah kecil walau berumur sama `16 bulan`; membatasi klaim irigasi agar tidak menjanjikan sembuhkan cacat genetik/akar. |
| **4. Kebutuhan Air & Produktivitas** | Produktivitas *C. amblycarpa* Majalengka `7,84 ton/ha` (`~5,06–5,13 kg/pohon` proporsional di `471 m²`); $ET_c$ jeruk Indonesia `3,02 mm/hari`; uji jeruk muda `6–12 L/hari` optimal; paket *Bujangseta* (pangkas + pupuk `7–8×/thn`). | Menjadi dasar **diferensiasi dosis** (`10–12 L` vs `5–6 L` vs `1,5–2,0 L/hari`) dan rumus waktu irigasi $IT = ET_{NM} / DC$. |
| **5. Hubungan Air–Tanah & Buah** | Cekaman air saat berbunga–pentil (`< 2,5 cm`) menurunkan hasil `20–41%`; defisit pembesaran buah menurunkan bobot, sari buah, & asam sitrat; fluktuasi picu buah pecah (*cracking*). | Stabilisasi kelengasan `55–65% FC` ditargetkan meningkatkan ukuran buah `Sampel 2` dan menjaga konsistensi `Sampel 3–4`. |

---

## Matriks Implementasi Lapangan CD-3 pada Empat Pohon Sampel

| Sampel Uji (Umur 16 Bulan) | Jarak 2× *PC Dripper* dari Batang | Posisi & Kedalaman Sensor *Capacitive v1.2* | Target Dosis Hari Kering | Logika Kendali & Rekomendasi Non-Irigasi Mitra |
|---|---|---|---|---|
| **Sampel 1** (`46 cm`, kerdil, nihil buah) | `15–20 cm` (2 sisi berlawanan) | `15 cm` dari batang (`10 cm` dari penetes), kedalaman `15 cm` (enkapsulasi penuh) | `1,5–2,0 L/pohon/hari` *(penskalaan rekayasa ~15–20% dewasa)* — hanya saat kering | Hentikan aliran sebelum `FC`; pakai katup/jadwal terpisah atau debit lebih kecil; cek fisik akar *coiled*/puing & pangkas naungan tetangga. |
| **Sampel 2** (`100 cm`, berbuah banyak tapi kecil) | `25–30 cm` (2 sisi, bawah *drip line*) | `25 cm` dari batang (`10–15 cm` dari penetes), kedalaman `15–20 cm` | `5,0–6,0 L/pohon/hari` *(selaras uji `6 L/hari`)* | Pertahankan stabil di `55–65% FC` untuk pembesaran buah & cegah *fruit drop*; rekomendasikan pemupukan NPK berimbang. |
| **Sampel 3** (`250 cm`, berbuah lebat, panen) | `40–50 cm` (2 sisi berlawanan) | `40 cm` dari batang (`10–15 cm` dari penetes), kedalaman `15–20 cm` | `10–12 L/pohon/hari` *(selaras uji `12 L/hari`)* | Jadwal terpisah dari Sampel 1; pangkas pucuk/cabang dalam (*Bujangseta*) & kembalikan hara panen (`~70% sink` buah). |
| **Sampel 4** (`210 cm`, tajuk besar, panen) | `40–50 cm` (2 sisi berlawanan) | `35–40 cm` dari batang (`10–15 cm` dari penetes), kedalaman `15–20 cm` | `10–12 L/pohon/hari` *(via siklus jeda/pulse agar tak meluap)* | Wajibkan pendalaman parit drainase dari `6 cm` menjadi `30–50 cm` agar lapisan akar `0–30 cm` aman dari genangan hujan. |

---

## Inventaris Sumber Terverifikasi dari Deep Research #2

### A. Literatur Spesifik *Citrus amblycarpa*
1. **Putri Tiyara Junjung Buih & Ratna Susandarini (2023)**, *"Karakterisasi Morfologi Citrus jambhiri Lush. dan Hubungan Kekerabatannya dengan Citrus amblycarpa (Hassk.) Ochse"*, *Al-Kauniyah: Jurnal Biologi*, Vol. 16(2), hlm. 255–268. PDF: https://journal.uinjkt.ac.id/index.php/kauniyah/article/download/22920/pdf/107068
2. **Portal Jurnal BAF Universitas Diponegoro** *(metadata penulis/tahun tidak tertampil pada pratinjau)*, *"Studi Poliembrio Biji Jeruk Sambal"*. PDF: https://ejournal2.undip.ac.id/index.php/baf/article/download/20943/pdf *(poliembrioni `27,85%` dari 300 biji)*.
3. **ResearchGate (`372977724`)**, *"Analisis Pendapatan Usaha Tani Jeruk Limau (Citrus amblycarpa) Pola Kemitraan dan Non Mitra di Desa Gunungkuning Kecamatan Sindang Kabupaten Majalengka"*. https://www.researchgate.net/publication/372977724_ANALISIS_PENDAPATAN_USAHA_TANI_JERUK_LIMAU_CITRUS_AMBLYCARPA_POLA_KEMITRAAN_DAN_NON_MITRA_DI_DESA_GUNUNGKUNING_KECAMATAN_SINDANG_KABUPATEN_MAJALENGKA *(produktivitas `7,84 ton/ha`)*.
4. **FoodTech: Jurnal Teknologi Pangan Univ. Tanjungpura** (Vol. 4(1), hlm. 24, Mei 2022), *"Penggunaan Jeruk Sambal (Citrus Amblycarpa) sebagai Bahan Pengasam Alami Terhadap Sifat Fisikokimia dan Sensori Mayones"*. PDF: https://jurnal.untan.ac.id/index.php/jft/article/viewFile/56638/pdf
5. **Pendukung karakterisasi & perbanyakan:** Socfindo Conservation Plant 203 (`socfindoconservation.co.id/plant/203`), Polsri BAB II Dwi Sandi (`eprints.polsri.ac.id/13082/3/3.%20BAB%20II%20DWI%20SANDI.pdf`), Jurnal Sintesa Unhira Bali (`jurnal.undhirabali.ac.id/index.php/sintesa/article/download/1242/1088/4567`).

### B. Pedoman Resmi Balitjestro/Balitbangtan & Agronomi Nasional (*Citrus* Umum)
6. **Sutopo, A. Sugiyatno, Hardiyanto, B. A. Fanshuri, & T. G. Aji (2021)**, *"Bab V Teknologi Produksi Jeruk (hlm. 155–215)"*, dalam *Teknologi Inovatif Jeruk Sehat Nusantara* (Ed. K. Budiarto & A. N. Sugiharto), IPB Press, ISBN `978-623-256-784-9`.
7. **A. Sugiyatno et al. (Nov 2021)**, *"Penerapan Teknologi Bujangseta pada Tanaman Jeruk untuk Mendukung Peningkatan Produktivitas, Kualitas dan Ketersediaan Buah Sepanjang Tahun"* (Balitjestro), beserta JPFP Unila (`jurnal.fp.unila.ac.id/index.php/JPFP/article/download/10788/6205`) & Laporan Tahunan Kementan 2019 (SITARA).
8. **Riset batang bawah & pemupukan acuan Balitjestro:** Farida Yulianti (UB, `repository.ub.ac.id/192546/2/Farida%20Yulianti.pdf`), Prosiding Perhorti 2019 (`repository.lppm.unila.ac.id/18387/1/prosiding_perhorti_2019.pdf`), studi okulasi Neliti (`media.neliti.com/media/publications/84029-none-265b8f87.pdf`), serta artikel pemupukan/agroklimat nasional (`smujo.id/psnmbi/article/download/1313/1270/1190`, `ejournal.unipas.ac.id/index.php/JK/article/download/1837/1109`, `ejournals.umma.ac.id/index.php/agribis/article/download/1265/873`).

### C. Jurnal Internasional & Nasional Irigasi, Perakaran, *Phytophthora*, & Sensor v1.2 *(Terverifikasi Crossref)*
9. **D. T. Meshram, A. K. Srivastava, A. Thirugnanavel, & D. Meshram (2025)**, *"Agronomic response of subsurface versus surface drip irrigation in Nagpur mandarin..."*, *Frontiers in Horticulture*, DOI: **`10.3389/fhort.2025.1552283`**.
10. **S. A. A. Bagherian & B. Hajieghrari (2026)**, *"Integrated management of citrus gummosis (Phytophthora spp.) in semi-arid Iran..."*, *Phytopathologia Mediterranea*, Vol. 65(2), pp. 309–317, DOI: **`10.36253/phyto-17259`**.
11. **A. Sravani, G. Singh, & P. Bakshi (2020)**, *"Performance evaluation of drip irrigation (fertigation) in citrus cultivation: A review"*, *J. Pharmacogn. Phytochem.*, Vol. 9(5), DOI: **`10.22271/phyto.2020.v9.i5aj.12726`**.
12. **C. A. Cabia, Sumaria, de Padua, & Leorna (2025)**, *"Quantifying calibration strategies for capacitive soil-moisture sensors (V1.2 SKU: FA3003-1) in automated drip irrigation for upland, rainfed farms"*, *Annals of Tropical Research*, Vol. 47(2), pp. 90–105, DOI: **`10.32945/atr4727.2025`**.
13. **M. Kumar, A. Sarangi, M. Singh, & M. Khanna (2025)**, *"Assessing capacitance soil moisture sensors for precision irrigation scheduling..."*, *CABI Agriculture and Bioscience*, DOI: **`10.1079/ab.2025.0025`**.
14. **Duarte, Araújo Silva, Bonfim-Silva, & Koetz (2021)**, *"Using Arduino sensors to monitor vacuum gauge and soil water moisture"*, *DYNA*, Vol. 88(219), DOI: **`10.15446/dyna.v88n219.94121`** *(kalibrasi Capacitive v1.2 pada Red Oxisol liat $\rho_{bd}=1,2\text{ Mg/m}^3$, model hiperbolik $y=1/(a+bx)$, $R^2=0,96$, $\text{RMSE}=0,019$)*.
15. **M. Mahmud, Dong, Alam, & Sharmin (2026)**, *"IoT-Based Precision Irrigation System Featuring Multi-Sensor Monitoring and Scheduled..."*, *Sensors*, Vol. 26(9), art. 2692, DOI: **`10.3390/s26092692`**.
16. **Pendukung terbuka lainnya:** Jurnal Irigasi PUPR (*Cropwat 8.0* Jeruk Keprok 55 `3,02 mm/hari`: `sda.pu.go.id/.../156/276/928`), laporan WRC `261-1-96.pdf`, CORE `37374413.pdf`, dan IWA *Water Science* 25(3):424.
