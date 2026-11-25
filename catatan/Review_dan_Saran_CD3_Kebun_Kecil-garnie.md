# Review Teknis & Saran Penyempurnaan Draf `CD-3` (`Kebun Kecil` — Solusi 1: *Precision Surface Drip*)

**Tanggal:** 25 November 2026  
**Disusun oleh:** Muhammad Al Qarnie (`-garnie`) — *Catatan untuk Rekan Tim & Asisten AI*  
**Objek Review:**
1. [`../dokumen/draf/cd3_kebun_kecil/CD3_Draft_Kebun_Kecil.docx`](../dokumen/draf/cd3_kebun_kecil/CD3_Draft_Kebun_Kecil.docx) (`27 halaman`)
2. Solusi 1 (*Precision Surface Drip / FDI*) pada [`README_ALTERNATIF_SOLUSI_DAN_SCORING_CD3.md`](README_ALTERNATIF_SOLUSI_DAN_SCORING_CD3.md)

**Catatan Penting:**
- File ini sengaja diletakkan di `catatan/` dengan akhiran `-garnie.md` agar **tidak menimpa atau mengacak-acak** berkas kerja rekan tim di `dokumen/draf/cd3_kebun_kecil/`.
- Slot kosong Alternatif 3 pada [`README_ALTERNATIF_SOLUSI_DAN_SCORING_CD3.md`](README_ALTERNATIF_SOLUSI_DAN_SCORING_CD3.md) **dibiarkan apa adanya** sebagai ruang terbuka apabila ada rekan tim yang ingin menambahkan alternatif solusi lain sebelum finalisasi.

---

## 1. Ringkasan Evaluasi Umum

Secara struktur, kedalaman rekayasa Teknik Komputer, simulasi awal (*Hazen-Williams* + *Logika Fuzzy*), dan pembagian tugas 3 anggota, draf [`CD3_Draft_Kebun_Kecil.docx`](../dokumen/draf/cd3_kebun_kecil/CD3_Draft_Kebun_Kecil.docx) sudah sangat solid dan mengarah ke **Level-4 Rubrik `PTA 2627` (`CLO3` & `CLO4`)**. Pilihan **Solusi 1 (*Precision Surface Drip / FDI*)** juga merupakan keputusan paling aman secara agronomi, paling realistis dirawat petani, dan paling efisien dari sisi anggaran mahasiswa.

Namun, terdapat **sejumlah celah teknis, ketidakkonsistenan angka internal, serta kelengkapan template** yang perlu diperbaiki agar naskah siap dikumpulkan pada tenggat `CLO3` (**Kamis, 10 Desember 2026**) dan `CD1–3 Gabungan` (**Kamis, 7 Januari 2027**).

---

## 2. Daftar Perbaikan Wajib terhadap Template `FTE-CD-3` & Rubrik `PTA 2627`

| No | Bagian / Tabel | Kondisi Saat Ini di Draf | Tindakan Perbaikan yang Disarankan |
|---|---|---|---|
| 1 | **Lembar Pengesahan (`Table 1`, baris `R9`)** | Nama **Pembimbing 2 masih kosong**. | Isi dengan identitas resmi Pembimbing 2: **Fussy Mentari Dirgantara, S.T., M.T.** (`NIDN: 0415039501`, Kode: `FUY`). |
| 2 | **Syarat Wajib `CLO3` (`Rubrik PTA`)** | `Tanggal Pengesahan` (`Table 0`) & tanda tangan masih kosong. | Pastikan **tanda tangan basah Pembimbing 1** sudah diperoleh sebelum pengumpulan `10 Des 2026` (rubrik menetapkan nilai = `0` jika tidak ada tanda tangan basah PBB 1 atau terlambat). |
| 3 | **Daftar Revisi (`Table 2`, baris `R2`)** | Ada baris duplikat sisa template `1, 25 Nov 2026` dengan kolom revisi/perbaikan/halaman kosong. | Hapus baris kosong duplikat tersebut agar tabel revisi bersih. |
| 4 | **Visual Perangkat Lunak Non-OOP (`Subbab 1.3.4`)** | Sudah benar memakai pendekatan **non-OOP** (FSM, Flowchart, Pseudocode, Skema Tabel DB) sesuai kesepakatan tim di [`Pembagian_Jobdesk_Tim_CD3_Kebun_Kecil.pdf`](Pembagian_Jobdesk_Tim_CD3_Kebun_Kecil.pdf), tetapi **belum ada gambar DFD dan UI**. | Template `FTE-CD-3` mensyaratkan dokumentasi software memuat **DFD** dan **Desain Antarmuka**. Tambahkan:<br>1. **Gambar DFD (*Context Diagram* & *DFD Level 1*)** untuk alur data sensor → ESP32 → MicroSD/MQTT → Database → Dashboard.<br>2. **Gambar *Wireframe / Mockup* Antarmuka Dashboard Web/HP** (pantau VWC/suhu, tombol siram jarak jauh, notifikasi *fault*, dan *remote tuning*). |
| 5 | **Visual Perangkat Keras (`Subbab 1.3.2`)** | Sudah ada Diagram Blok, Skema Pemipaan, dan Tabel Pin GPIO, tetapi **belum ada gambar desain PCB**. | Template `FTE-CD-3` mensyaratkan dokumentasi hardware memuat **desain PCB**. Tambahkan **gambar Skematik Rangkaian / Layout PCB** (atau minimal *wiring diagram* + tata letak komponen di dalam boks panel IP65 `300×200×150 mm`). |

---

## 3. Daftar Perbaikan Teknis Solusi 1 & Kesesuaian Kondisi Nyata Kebun

### 3.1. Pembatasan Dosis Air Pohon Kerdil `P1 (46 cm)` — Hindari *Waterlogging* & *Phytophthora*
- **Masalah di Draf (`Tabel 1.7`):** Pohon `P1` (`46 cm`, kondisi kerdil/cacat, tidak berbuah) disimulasikan mendapat **`9,25 L`** dalam satu siklus (`k_tajuk = 0,65`), sedangkan `P2 (100 cm)` mendapat **`12,75 L`**.
- **Fakta Agronomi (*Deep Research* #2):** Pohon kerdil `46 cm` di tanah liat merah urugan eks-empang dengan `6` parit dangkal hanya `6 cm` **sangat rentan mengalami genangan mikro (*waterlogging*) dan busuk akar *Phytophthora*** jika disiram `9,25 L` sekaligus.
- **Saran Perbaikan:**
  - Sesuaikan faktor skala tajuk (`k_tajuk`) dan batas atas di aturan Logika Fuzzy sehingga dosis harian pada hari tanpa hujan menjadi:
    - **`P1 (46 cm)`:** dibatasi **`1,5–2,0 L/hari`** (atau **`~3–4 L`** per siklus kering 2–3 hari).
    - **`P2 (100 cm)`:** **`5–6 L/hari`** (atau **`~8–10 L`** per siklus kering).
    - **`P3 (250 cm)` & `P4 (210 cm)`:** **`10–12 L/hari`** (maksimal **`15 L`** saat puncak kemarau).
  - Tambahkan catatan eksplisit di naskah bahwa sistem irigasi tetes mencegah stres kekeringan dan *waterlogging* akibat penyiraman, namun **tidak dapat memulihkan cacat genetik bibit, pemadatan puing urugan, atau genangan hujan dari parit `6 cm`** tanpa intervensi budidaya mitra.

### 3.2. Model Kalibrasi Non-Linear & Pelapisan Anti-Karat Sensor Kapasitif `v1.2`
- **Masalah di Draf & `README` Solusi:** Model kalibrasi masih ditulis linear `θ_v = m·ADC + c` (`Pers. 1` & Pilar 1), padahal karakteristik tanah liat merah tropis bersifat non-linear.
- **Saran Perbaikan:**
  - Gunakan atau bandingkan dengan model regresi non-linear/invers untuk tanah liat merah tropis (*Duarte et al., 2021*):
    $$y = \frac{1}{a + b x} \quad (R^2 = 0{,}96,\; \text{RMSE} = 0{,}019\text{ m}^3/\text{m}^3)$$
  - Wajib tegaskan bahwa keempat sensor kapasitif `v1.2` harus diberi **pelapisan kedap air (*resin epoksi* atau *rubber coating*)** selain *heat-shrink* di kepala modul untuk mencegah korosi berat dalam ~6 bulan pemakaian di tanah lembap, serta ditanam pada **kedalaman `15–20 cm`** (inti zona akar serabut aktif `0–30 cm`) berjarak `15–40 cm` dari batang dan `10–15 cm` dari titik penetes.

### 3.3. Inkonsistensi Jumlah Penetes (`2 penetes/pohon` vs `16 L/jam`)
- **Masalah di Draf:** Di teks (`Subbab 1.1.3`, `Subbab 1.3.3`) dan `Tabel 1.18`, tertulis **`2 penetes/pohon`** (atau opsi *4-way drip stake*). Namun, seluruh perhitungan hidrolika `Tabel 1.5` (`hf_drip @ 16 L/jam`) dan durasi siklus `Tabel 1.7` (`9,25 L` dalam `34,7 menit` = `16 L/jam`) memakai asumsi **`4 penetes × 4 L/jam = 16 L/jam`**.
- **Dampak:** Jika benar-benar hanya memakai `2` penetes (`8 L/jam`), maka waktu siram melonjak 2× lipat dan total durasi siklus menjadi `> 6 jam` — **melanggar spesifikasi `S-03 <= 4,0 jam`**.
- **Saran Perbaikan:** Kunci secara konsisten di seluruh naskah, skema pipa, dan jobdesk bahwa tiap pohon memakai **`4` penetes PC `4 L/jam` (*4-way drip stake* / cincin `4` titik = `16 L/jam/pohon`)**.

### 3.4. Penguncian Topologi Internet (`ESP32 Wi-Fi → Router/MiFi 4G`)
- **Masalah di Draf:** `Tabel 1.10` (Pemetaan Pin ESP32) tidak menyediakan pin UART untuk modul seluler (seperti SIM7670G/SIM7600E), sementara teks/jobdesk menyebut **Wi-Fi**, dan RAB menyebut *"Modem/MiFi 4G atau Modul 4G"*.
- **Saran Perbaikan:** Agar konsisten dan tidak memicu pertanyaan penguji (*"di kebun tidak ada Wi-Fi, kok pakai Wi-Fi?"*), kunci satu arsitektur di seluruh dokumen: **ESP32 berkomunikasi via Wi-Fi lokal menuju sebuah `Router / MiFi 4G LTE` yang diletakkan di dalam/dekat panel IP65**.

### 3.5. Pemilihan Katup Cabang (`Paket A` vs `Paket B`) & Verifikasi Lapangan Bulan 1
- **Katup Cabang:** Jika air sumur baru ternyata berpasir/berlumpur halus, `Solenoid Valve` (Paket A) berisiko macet pada membran diafragmanya; prioritaskan **Paket B (`Motorized Ball Valve Full-Bore 12V`)** selama masih masuk pagu `<= Rp5.000.000`.
- **Verifikasi Wajib Bulan 1 (Des 2026):**
  1. Ukur langsung **kedalaman sumur & tinggi muka air (`Δz` riil)** sebelum membeli pompa (saat ini `Δz = 4,00 m` masih asumsi).
  2. Lakukan **uji kuat sinyal 4G (RSSI/RSRP)** berbagai operator seluler langsung di `Kebun Kecil` sebelum memilih kartu perdana IoT.
  3. Tambahkan 1–2 kalimat justifikasi di `Subbab 1.1` atau `1.3` mengenai **alasan tidak memasang sensor pH/NPK murah** (karena dosen sempat menyinggung pH di rekaman survei `22 Nov`): probe pH/NPK murah tanpa kalibrasi laboratorium memiliki deviasi tinggi, sehingga tim memfokuskan instrumentasi pada lengas tanah, suhu akar, debit, dan tekanan (*anti-clogging*).

---

## 4. Kekurangan & Penambahan Daftar Pustaka Wajib

Saat ini `CD3_Draft_Kebun_Kecil.docx` baru mencantumkan **14 pustaka (`[1]`–`[14]`)** — masih di bawah ambang **Level-4 Rubrik `PTA 2627` (`> 15` pustaka)**. Beberapa referensi penting baik yang **sudah tersedia *full-text* di repositori** ([`CATALOG_REFERENSI_SOLUSI_CD3.md`](../sumber/referensi%20jurnal/draf/pustaka_cd3/CATALOG_REFERENSI_SOLUSI_CD3.md)) maupun hasil riset lanjutan **belum dimasukkan** ke dalam draf.

Berikut daftar referensi yang perlu ditambahkan ke Daftar Pustaka `CD-3`:

1. **Pustaka *Full-Text* di Repositori (`CATALOG_REFERENSI_SOLUSI_CD3.md`) yang Belum Disitasi:**
   - **Dafonte et al. (2024)** [`Z-01`, *Sensors*, DOI: `10.3390/s24248104`] — rujukan teknis filter ADC `0,1 µF`, rata-rata `10×`, *power-gating* sensor, dan peringatan *drift* jam ESP32.
   - **García et al. (2020)** [`Z-05`, *Sensors*, DOI: `10.3390/s20041042`] — tinjauan 178 studi IoT irigasi, pemetaan sensor aliran, serta peringatan korosi probe konduktif.
   - **Abbas et al. (2024)** [`Z-13`, *HardwareX*, DOI: `10.1016/j.ohx.2024.e00523`] — desain kontroler terbuka & ambang irigasi *Citrus* (`61–80 kPa`).
   - **Bawa et al. (2023)** [`Z-19`, *iRASD JEE*, DOI: `10.52131/jee.2023.0402.0040`] — dasar ambang tekanan masuk lateral `> 78,45 kPa` (`~0,78 bar`) untuk mencapai keseragaman `EU > 85%`.
   - **Hartung & Pluschke (2018)** [`Z-21`, FAO & GIZ, ISBN: `978-92-5-130479-2`] — prinsip wajib kontrol irigasi berbasis meter volume (bukan *timer*), bahaya *air trap* hisap, serta *foot valve* macet.
2. **Referensi Agronomi *Citrus amblycarpa*, Tanah Tropis, & Uji Sumbatan yang Belum Masuk:**
   - **Agronomi Spesifik *Citrus amblycarpa*:** Data morfologi perdu, poliembrioni biji (`27,85%`, studi UNDIP), dan produktivitas usahatani jeruk limau (`7,84 ton/ha`, Majalengka), serta acuan umum *Citrus* (Balitjestro/BSIP Kementan & pencegahan busuk akar *Phytophthora*).
   - **Kalibrasi Sensor Kapasitif Tanah Merah Tropis:** **Duarte et al. (2021)** (DOI: `10.3390/s21186193`) untuk model regresi non-linear $y = 1/(a+bx)$ ($R^2 = 0{,}96$, $\text{RMSE} = 0{,}019$).
   - **Uji Sumbatan Emiter PC `16 mm` & Arsitektur IoT ESP32:** **Frontiers in Water (2026)** (DOI: `10.3389/frwa.2026.1973897`) untuk uji sumbatan emiter *pressure-compensating* pipa `16 mm`, serta **Pereira, Chaari, & Daroge (2023)** (*MDPI IoT*, DOI: `10.3390/iot4030012`) untuk arsitektur ESP32 irigasi tetes `12 V DC → 5 V` + *flow sensor*.
3. **Standar Keselamatan Kelistrikan Pertanian & Perapian Pustaka `[13]`:**
   - Tambahkan standar internasional **IEC 60364-7-705:2006** (*Electrical installations of buildings — Agricultural and horticultural premises*).
   - Rapikan pustaka **`[13]`** pada draf dengan memisahkan serta mencantumkan nomor & tahun resmi **PUIL 2011 (`SNI 0225:2011`)** dan **IEC 60529** (derajat proteksi `IP65`).

---

## 5. Panduan Singkat untuk Rekan Tim / Asisten AI Saat Merevisi

Apabila rekan tim atau AI lain membaca catatan ini untuk memperbarui naskah `CD-3`:
1. **Jangan hapus** data historis `Kebun Besar` (`CD-1` & `CD-2`) ataupun tabel perbandingan 2 kebun pada `Subbab 1.1.1`.
2. **Prioritaskan revisi** pada: (a) pengisian nama Pembimbing 2 & perapian tabel pengesahan/revisi, (b) pembuatan 3 gambar yang belum ada (**DFD Context & Level 1**, **UI Wireframe Dashboard**, dan **Skematik/Layout PCB + Panel IP65**), (c) koreksi dosis Fuzzy `P1 (46 cm)` + kunci `4` penetes `16 L/jam` + kunci topologi `ESP32 Wi-Fi → MiFi 4G`, dan (d) penambahan pustaka agronomi *C. amblycarpa* & `IEC 60364-7-705`.
3. Jika hendak membuat versi naskah terpisah dari `dokumen/draf/cd3_kebun_kecil/` milik tim, gunakan folder khusus terpisah (misalnya `dokumen/draf/cd3_garnie/`) agar tidak terjadi konflik file saat *push* ke GitHub.
