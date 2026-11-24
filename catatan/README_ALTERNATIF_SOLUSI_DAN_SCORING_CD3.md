# README Alternatif Solusi & *Design Matrix Scoring* `CD-3` (`Kebun Kecil` — `1 Zona = 4 Pohon`)

**Tanggal Penyusunan:** 25 November 2026  
**Status Dokumen:** Dokumen Kerja Hidup (*Living Working Note*) — **Persiapan Subbab `1.1` & `1.2` `CD-3` (`tenggat CLO3 CD3-1: Kamis, 10 Desember 2026`)**. Dokumen ini sengaja diletakkan di `catatan/` agar seluruh alternatif, detail teknis (termasuk rekayasa anti-mampet), bobot, dan skor dapat **ditambah, diubah, dan diperdalam** bersama tim sebelum dituangkan ke naskah resmi `CD-3` baru dari awal.

> [!IMPORTANT]
> **Status Naskah Akademik:** Berkas `dokumen/cd1/`, `dokumen/cd2/`, `dokumen/cd3/`, dan `dokumen/draf/` **tidak diubah** pada tahap ini. Seluruh draf `CD-3` lama berstatus tidak terpakai; dokumen ini menjadi bahan inti penyusunan `CD-3` baru dari awal berbasis lokasi ACC `Kebun Kecil` (`22 November 2026`).

**Tautan Acuan Resmi & Konteks Terkait:**
- Panduan & Template Resmi `CD-3`: [Buku Panduan Capstone 2024](../sumber/panduan/bukupanduancapstone_2024signed.pdf) *(hlm. 19–21)* · [Template FTE-CD-3](../sumber/template/FTE-CD-3%20-edited_PBD.pdf) · [Jadwal & Rubrik PTA 2627](../sumber/rubrik-jadwal/Jadwal_PTA%20--%20Rubrik%20PTA%20--%202627%20%281%29.pdf)
- Dokumen Transisi & Data Lapangan: [README Transisi `Kebun Besar` → `Kebun Kecil`](README_TRANSISI_KEBUN_BESAR_KE_KEBUN_KECIL_CD2_CD3.md) · [Data Kebun Kecil & Zona 4 Pohon](DATA_KEBUN_KECIL_DAN_ZONA_4_POHON.md) · [Denah 2D Kebun Kecil](denah_kebun_kecil_2d.png) · [Skema Pemipaan, 4 Katup, & Ekspansi](skema_pipa_zona_4_pohon.png) ([SVG](skema_pipa_zona_4_pohon.svg))
- Transkrip Survei `22 Nov 2026`: [transkrip_survey_limau.md](../sumber/dokumentasi/kebon%20kecil/Record%20survey%2022%20Nov/transkrip_survey_limau.md)
- Katalog Pustaka *Full-Text* di Repo: [CATALOG_REFERENSI_SOLUSI_CD3.md](../sumber/referensi%20jurnal/draf/pustaka_cd3/CATALOG_REFERENSI_SOLUSI_CD3.md) · [README Sintesis Solusi Zonasi](../sumber/referensi%20jurnal/draf/pustaka_cd3/solusi_terpilih_zonasi/README_SINTESIS_SOLUSI_ZONASI.md)

---

## 1. Kepatuhan Terhadap Aturan Resmi Panduan, Template `FTE-CD-3`, & Rubrik `CLO3`

Mengacu langsung pada **[Buku Panduan Capstone 2024](../sumber/panduan/bukupanduancapstone_2024signed.pdf)** (`hlm. 19–21`), **[Template FTE-CD-3](../sumber/template/FTE-CD-3%20-edited_PBD.pdf)** (`hlm. 4–5`), dan **[Rubrik PTA 2627](../sumber/rubrik-jadwal/Jadwal_PTA%20--%20Rubrik%20PTA%20--%202627%20%281%29.pdf)**:

1. **Syarat Subbab `1.1 Alternatif Usulan Solusi`:**
   - Mahasiswa **wajib mengusulkan sekurang-kurangnya `3` alternatif solusi** yang semuanya relevan dengan masalah lapangan dan batasan/spesifikasi `CD-2` (disertai penyesuaian transisi `Kebun Kecil`).
   - Setiap alternatif wajib memuat: **(a) dasar pemilihan alternatif** *(studi literatur / desain awal)*, **(b) fitur utama**, **(c) fitur tambahan**, **(d) data pengujian awal / data literatur implementasi nyata**, dan **(e) prosedur pengoperasian**.
   - **Prinsip kualitas tim:** seluruh alternatif harus **sama-sama serius dan setara tujuannya** (tidak boleh ada alternatif "pangkas fitur / asal-asalan" hanya demi mengisi jumlah 3 baris).
2. **Syarat Subbab `1.2 Analisis dan Pemilihan Solusi` (`Bobot 100%` pada `CLO3 CD3-1`, `10 Des 2026`):**
   - Wajib memiliki **(1) daftar parameter seleksi yang jelas beserta dasar pembobotannya** (parameter resmi Panduan hlm. 20: *tingkat kesesuaian, biaya, waktu, kehandalan, serta sumber daya manusia, alat, dan bahan*) dan **(2) mekanisme pemilihan solusi menggunakan *Design Matrix Scoring* (*Engineering Design Matrix*)**.
   - **Target `Level-4` Rubrik Dosen Kelas & Pembimbing/Penguji (`CLO3`):** minimal 2 (template: 3) alternatif solusi dengan *matrix scoring* serta **penjelasan komprehensif berbasis justifikasi metode dan simulasi/pengujian awal** *(catatan rubrik: tanda tangan basah Pembimbing 1 wajib ada sebelum tenggat agar nilai tidak `0`)*.

---

## 2. Arsitektur Inti Bersama (*Core Computer Engineering* & 5 Lapis Anti-Mampet)

Agar seluruh alternatif yang dibandingkan **tetap murni S1 Teknik Komputer** (bukan alat `if kering -> pompa ON` sederhana, dan bukan riset agronomi murni), seluruh alternatif pada `Kebun Kecil` (`1 Zona = 4 Pohon Sampel` + `4` pohon kontrol manual sebagai data uji banding TA) berbagi pondasi sistem tertanam & anti-mampet berikut:

1. **Kontrol Adaptif Tertutup (*Closed-Loop Fuzzy + Pulse Drip*):**
   - Sensor lengas kapasitif (`4` titik) & suhu tanah (`DS18B20` 1-Wire) dikalibrasi terlebih dahulu menggunakan **sampel tanah merah asli `Kebun Kecil`** (`VWC = m·ADC + c`, *moving average* `10×` sampel) untuk mengatasi galat kurva pabrik (`RMSE 5,33%` → `0,40–1,37%`, `Z-02` & `Z-11`).
   - Algoritma **Logika Fuzzy** di **ESP32** menghitung **target volume liter (`V_target`, pagu aman `10–15 L/pohon`)** dari kelembapan tanah, suhu, dan profil ukuran tiap pohon (`46/100/250/210 cm`), lalu menyiram bergantian (`1` *flow sensor* induk + `4` katup cabang independen) secara bertahap (**metode *Pulse Drip* + jeda serap `15 menit`**) agar tanah liat merah tidak meluber/banjir ke parit `6 cm`.
2. **Konektivitas IoT Tanpa Wi-Fi Kebun + *Remote Parameter Tuning*:**
   - Memakai listrik **PLN rumah** (adaptor DC aman berproteksi `SELV <= 48 V DC`) + konektivitas **seluler 4G** (protokol MQTT), dilengkapi **`RTC DS3231` + penyimpanan lokal `microSD`** (*store-and-forward* agar nol data hilang saat sinyal turun) serta **1 tombol fisik manual** (`S-13`).
   - Fitur ***remote parameter tuning*** via MQTT memungkinkan penyesuaian ambang Fuzzy dari Bandung (Bojongsoang) tanpa bolak-balik ke Subang yang beriklim lebih panas.
3. **5 Lapis Rekayasa Anti-Mampet (*Anti-Clogging Engineering* — Nilai Tambah Utama):**
   - **Lapis 1 (Filtrasi & Material Pompa):** *Disc Filter* `120–150 mesh` (`100–130 µm`, celah $1/7\text{–}1/10$ labirin emiter) + **pompa rumah polimer teknik / *stainless steel*** (dilarang memakai besi cor/*cast iron* agar serpihan karat tidak menyumbat hilir filter, `Z-16`).
   - **Lapis 2 (Emiter & Posisi Katup):** Emiter *Pressure-Compensating* (`PC`) *self-flushing* berjalur labirin lebar + penempatan katup cabang (`Motorized Ball Valve` *full-bore* atau solenoid) di **hilir filter**.
   - **Lapis 3 (Deteksi Dini Mampet Otomatis di ESP32):** Pembacaan **sensor tekanan elektronik + *flow sensor*** secara *real-time* (`Z-04`, `Z-09`). Jika beda tekanan menembus ambang bilas ($\Delta p \approx 70\text{ kPa} / 0{,}7\text{ bar}$, `Z-09`) atau debit cabang pohon $i$ anjlok di bawah kalibrasi saat katup buka, ESP32 memicu alarm mampet spesifik per cabang ke HP mitra; jika `flow == 0` saat pompa hidup, pompa dimatikan otomatis (*dry-run / leak protection*).
   - **Lapis 4 (Pembilasan Pipa Otomatis / *Auto End-Flush*):** Karena kecepatan alir mode tetes di pipa `16 mm` berada di bawah kecepatan pengendapan kritis **`0,6 m/s`** (`Z-16`), dipasang **`1` katup buang ujung (*end-flush valve*)** yang dibuka otomatis oleh ESP32 selama **`30–45 detik`** (`Z-09`) secara berkala agar aliran deras ($\ge 0{,}6\text{–}1{,}0\text{ m/s}$) menyapu endapan lumpur halus keluar sebelum masuk ke emiter.
   - **Lapis 5 (Proteksi Khusus Jalur Tanam — Khusus Alternatif 2 `SDI`):** Pemasangan ***air-vacuum relief valve*** untuk mencegah hisapan balik lumpur (*soil suction*) saat pompa berhenti, serta emiter berpelindung akar (*root-barrier*).

---

## 3. Profil Detail Alternatif Solusi (Format Subbab `1.1 FTE-CD-3`)

> *Catatan progres:* Saat ini **Alternatif 1 (`Surface Drip / FDI`)** dan **Alternatif 2 (`Subsurface Drip / SDI`)** sudah dirinci penuh sebagai duel utama berskor ketat. **Alternatif 3** disiapkan sebagai slot pengembangan (`Under-Canopy Micro-Jet` — dapat diubah, diperdalam, atau diganti sesuai diskusi lanjutan tim & PBB 1 agar memenuhi syarat minimal `3` alternatif template `FTE-CD-3`).

### Alternatif 1 — Irigasi Tetes Permukaan Presisi Independen Per-Pohon (*Precision Surface Drip / FDI*) + Fuzzy + *Auto End-Flush* + IoT 4G
- **Dasar Pemilihan Alternatif:** Hasil survei `22 Nov 2026` memperlihatkan `4` pohon sampel (`16 bulan`) tumbuh timpang (`46–250 cm`) di tanah merah urugan bekas empang/sampah, daun tidak boleh basah karena rentan **jamur daun** (`transkrip L254–258`), dan perawatan di kebun harus mudah dikerjakan mitra. Studi kebun jeruk tanah liat (`Farag et al., 2025`, `Z-15`) dan sistem tetes ESP32 (`Sensors 2025`, `Z-06`; `Zakaria et al., 2026`, `Z-11`) membuktikan tetes cincin `16 mm` (`4 × 4 L/jam = 16 L/jam/pohon`) hemat air `28,8%` dan menaikkan hasil `12–15%`.
- **Fitur Utama:**
  - Cincin pipa PE `16 mm` diletakkan **di atas permukaan tanah** melingkari pangkal akar tiap pohon (`radius ~30–50 cm`, `4` emiter PC `4 L/jam` per pohon).
  - Kendali independen `4` katup cabang + `1` *flow sensor* + `1` sensor tekanan + `4` node sensor lengas kapasitif & suhu tanah terkalibrasi + algoritma **Fuzzy + *Pulse Drip***.
  - Sistem anti-mampet 4 lapis (`Disc Filter 120–150 mesh`, *fault detection* tekanan/aliran, dan **`Auto End-Flush` $\ge 0{,}6\text{ m/s}$** `30–45 detik`).
- **Fitur Tambahan:** *Edge buffering* (`RTC DS3231 + microSD`), IoT 4G MQTT + *remote parameter tuning* (Bojongsoang ↔ Subang), serta `1` tombol fisik lokal untuk mitra.
- **Data Referensi / Pengujian Awal:**
  - `Sensors (2025)` (`PMC11902337`, `Z-06`): ESP32 + `4× SEN0193` di kebun jeruk hemat air **`28,8%`** & hasil naik **`12–15%`**.
  - `Zakaria et al. (2026)` (`PMC13364378`, `Z-11`): kalibrasi lokal `Capacitive v1.2` + `1 MΩ` *pull-down* + LDO `AP2112` mencapai $R^2 = 0{,}92\text{–}0{,}94$ (RMSE `0,40–0,52%`).
  - `Meriç (2025)` (`PMC12019383`, `Z-04`): uji kebun `82` pohon memakai *water meter* `1 L/pulsa` + sensor tekanan `6 bar` untuk deteksi anomali.
  - `INTENSIF (2024)` (`DOI 10.29407/intensif.v8i1.21351`): *Smart Drip* ESP32 + Fuzzy mencatat akurasi respons inferensi **`92–94%`**.
- **Prosedur Pengoperasian:** Sistem berjalan otomatis (cek sensor berkala → hitung target liter Fuzzy → buka katup pohon kering bergantian → tetes bertahap *Pulse Drip* hingga target *flow* / *Field Capacity* → jalankan *Auto End-Flush* terjadwal); mitra dapat memantau/memicu dari HP 4G atau menekan tombol fisik lokal; pembersihan filter/emiter dilakukan visual tanpa menggali tanah.

---

### Alternatif 2 — Irigasi Tetes Bawah Permukaan Presisi Independen Per-Pohon (*Precision Subsurface Drip / SDI*) + Fuzzy + *Air-Relief* + IoT 4G
- **Dasar Pemilihan Alternatif:** Pada iklim dataran rendah Subang yang terik (`32–36 °C`), tetes permukaan masih mengalami kehilangan penguapan dan kenaikan salinitas lapisan atas (`ECe`). Dua penelitian lapangan 2025 pada **jeruk di tanah liat** (`Farag et al., 2025`, *Sci. Rep.* `PMC12479814`; `Meshram et al., 2025`, *Front. Hortic.* `10.3389/fhort.2025.1552283`) menunjukkan penanaman jalur tetes di bawah permukaan (**`SDI`**) secara konsisten melampaui *surface drip* pada *Water Use Efficiency* (`WUE`), serapan `N-P-K`, dan hasil buah.
- **Fitur Utama:**
  - Cincin lateral tetes berdinding tebal dengan emiter *root-barrier* **ditanam di kedalaman `15–20 cm`** langsung di zona akar serabut `4` pohon sampel.
  - Arsitektur kontrol elektronik, `4` katup cabang, kalibrasi sensor, Fuzzy + *Pulse Drip*, *flow/pressure fault detection*, `Auto End-Flush`, dan IoT 4G **setara dengan Alternatif 1**.
  - Tambahan wajib hidrolika bawah tanah: ***air-vacuum relief valve*** pada titik tertinggi manifold untuk mencegah hisapan balik lumpur (*soil suction clogging*) saat pompa mati.
- **Fitur Tambahan:** Permukaan tanah tetap kering sehingga menekan gulma sekitar batang, melindungi selang dari radiasi UV/cangkul pekerja, serta memperlambat akumulasi garam permukaan (`ECe`).
- **Data Referensi / Pengujian Awal:**
  - `Farag et al. (2025)` (`PMC12479814`, `Z-15`, uji 3 musim jeruk tanah liat): `Full SDI` mengungguli `Surface Drip` & banjir dengan **hemat air `31,58%`**, kenaikan **`WUE` `+58,87%` (hingga `2,96 kg/m³`)**, kenaikan serapan `N-P-K` (`+2,44% / +10,52% / +5,69%`), **hasil buah `+8,70%` (`25,0 t/ha`)**, dan kenaikan `ECe` lapisan atas 3 musim lebih rendah (`34,42%` vs `56,46%` pada *surface drip*).
  - `Meshram et al. (2025)` (`10.3389/fhort.2025.1552283`, jeruk keprok di tanah liat berat *Vertisol*): `SDI` menghasilkan produktivitas air **`7,96–10,73 kg/m³`** (vs *surface drip* `2,79–3,04 kg/m³`) dan kenaikan hasil buah **`15,86%–56,23%`**.
- **Prosedur Pengoperasian:** Operasi kontroler & aplikasi IoT identik dengan Alternatif 1; namun pemasangan awal menuntut penggalian parit cincin `15–20 cm` di sekitar akar pohon `16 bulan`, dan pemeliharaan mampet/intrusi akar sangat bergantung pada pembacaan anomali *flow/pressure*, jadwal *flushing* lebih ketat, serta pembongkaran tanah apabila terjadi sumbatan permanen.

---

### Alternatif 3 — `[SLOT PENGEMBANGAN / KANDIDAT AWAL: Under-Canopy Micro-Jet Bawah Tajuk + Fuzzy + Flow + IoT 4G]`
> *Status:* Kerangka awal untuk melengkapi syarat minimal `3` alternatif pada template `FTE-CD-3` (dapat didalami, diubah menjadi variasi arsitektur jaringan *multi-node* `ESP-NOW/LoRa`, atau diganti pada diskusi QnA berikutnya).
- **Konsep Singkat:** Mengganti emiter tetes dengan **`1–2` pasak *micro-jet / micro-sprinkler* rendah (`tinggi 20–30 cm`) di bawah tajuk tiap pohon** (bukan *sprinkler* atas daun), tetap memakai `4` katup cabang + *flow/pressure* + sensor lengas + Fuzzy + IoT 4G.
- **Keunggulan Nyata (Referensi *UF/IFAS AE094 Smajstrla* — tersedia di `pustaka_cd1/`):** Lubang nosel lebar (`0,8–1,5 mm`) jauh lebih tahan mampet dibanding *dripper* sempit, kerusakan/macet langsung terlihat mata dalam sekejap, dan area pembasahan luas (`radius 0,5–1,5 m`) ideal untuk akar pohon besar (`210–250 cm`) sekaligus mendinginkan iklim mikro bawah tajuk.
- **Tantangan Nyata:** Kehilangan penguapan & *drift* angin lebih tinggi daripada tetes, memicu gulma lebih luas, dan percikan semprotan rendah berisiko membasahi daun bawah pada pohon kerdil `Sampel 1` (`46 cm`) sehingga berpotensi memicu jamur daun bila sudut semprot tidak dibatasi ketat.

---

## 4. Tabel Perbandingan Teknis Detail (Berbasis Data Jurnal Nyata)

| Dimensi Perbandingan | Alternatif 1: *Precision Surface Drip* (`FDI`) | Alternatif 2: *Precision Subsurface Drip* (`SDI`) | Slot Alternatif 3: *Under-Canopy Micro-Jet* *(Draf Awal)* | Sumber Referensi Terverifikasi |
|---|---|---|---|---|
| **Posisi & Cara Penyaluran Air** | Cincin PE `16 mm` di **atas tanah** (`4×4 L/jam` per pohon), menetes pelan ke akar. | Cincin lateral anti-akar **dikubur `15–20 cm`** di zona akar + *air-vacuum valve*. | Pasak pendek `20–30 cm` bawah tajuk, semprot halus mendatar. | `Farag et al. (2025)` [`Z-15`]; `Smajstrla` (`UF/IFAS AE094`). |
| **Otak Kendali, Sensor, & IoT** | ESP32 + kalibrasi lokal + Fuzzy + *Pulse Drip* + `4` katup + *Flow & Pressure* + `Auto End-Flush` + IoT 4G. | Identik dengan Alt. 1 + pengecekan anomali tekanan balik jalur tanam. | Identik dengan Alt. 1 (durasi Fuzzy disesuaikan faktor penguapan). | `Zakaria et al. (2026)` [`Z-11`]; `Meriç (2025)` [`Z-04`]; `INTENSIF (2024)`. |
| **Efisiensi Air (`WUE`) & Penghematan** | Hemat air **`28,8%`** (tetes sensor jeruk); sedikit penguapan permukaan. | **Unggul:** hemat **`31,58%`**, `WUE` **`+58,87%`** (`2,96 kg/m³`), *Vertisol* **`7,96–10,73 kg/m³`**. | Baik, namun di bawah tetes akibat penguapan & *drift* angin permukaan. | `Sensors (2025)` [`Z-06`]; `Farag et al. (2025)` [`Z-15`]; `Meshram et al. (2025)`. |
| **Dampak ke Pertumbuhan & Hasil Buah** | Hasil naik **`12–15%`** dibanding jadwal konvensional. | **Unggul:** hasil **`+8,70%`** (`25,0 t/ha`) vs `FDI`/banjir & serapan `N-P-K` lebih tinggi. | Baik untuk pohon besar berakar luas; perlu kontrol ketat pada pohon kecil. | `Sensors (2025)` [`Z-06`]; `Farag et al. (2025)` [`Z-15`]; `Meshram et al. (2025)`. |
| **Risiko Mampet & Kemudahan Rawat (`S-14`)** | **Unggul di tetes:** bebas intrusi akar; mampet langsung terlihat & cepat dibersihkan (`Disc Filter` + `Auto End-Flush`). | **Rawan:** risiko *root intrusion* & *soil suction*; tidak tampak mata, perbaikan harus gali tanah. | **Paling tahan mampet** (nosel `0,8–1,5 mm`) & paling mudah dicek visual; rawan semut/serangga di nosel. | `Lavanholi et al. (2018)` [`Z-16`]; `Zong et al. (2019)` [`Z-09`]; tinjauan *ASCE/MDPI*. |
| **Keamanan Jamur Daun, Gulma, & Pipa** | Aman jamur daun; permukaan basah memicu gulma & pipa terpapar UV/cangkul (`ECe` 3 musim `+56,5%`). | **Unggul:** permukaan kering (minim gulma & bebas jamur leher batang), pipa terlindung, `ECe` lebih rendah (`+34,4%`). | Risiko percikan ke daun rendah pohon kerdil `46 cm` (jamur) & area gulma paling luas. | `Farag et al. (2025)` [`Z-15`]; `transkrip_survey_limau.md` (`L254–258`). |
| **Instalasi di Tanah Eks-Empang (`16 Bln`)** | **Sangat mudah:** tanpa gali, tidak mengganggu akar `16 bulan` & puing urugan. | **Lebih sulit:** butuh galian melingkar `15–20 cm` di tanah urugan sampah dekat akar aktif. | Mudah (cukup tancap pasak), perlu penyetelan sudut per pohon. | `DATA_KEBUN_KECIL_DAN_ZONA_4_POHON.md`. |
| **Estimasi CAPEX Purwarupa (`4` Pohon)** | **`~Rp2,2–3,2 juta`** *(hemat, `< Rp5 jt`)* | **`~Rp2,8–3,9 juta`** *(pipa *root-guard* + *air-vacuum valve* + galian, tetap `< Rp5 jt`)* | **`~Rp2,3–3,3 juta`** *(tetap `< Rp5 jt`)* | Estimasi awal skala `4` pohon + PLN *(akan dirinci di RAB `CD-3`)* |

---

## 5. Metodologi *Design Matrix Scoring* (Aturan Panduan & Dasar Anti-Sembarangan)

Sesuai **[Buku Panduan Capstone 2024](../sumber/panduan/bukupanduancapstone_2024signed.pdf)** (`hlm. 20`) dan **[Template FTE-CD-3](../sumber/template/FTE-CD-3%20-edited_PBD.pdf)** (`hlm. 4`), pemberian bobot dan skor **tidak boleh bersifat subjektif/asal-asalan**. Berikut aturan formal yang mengikat seluruh angka pada matriks pemilihan kita:

### 5.1 Pemetaan 6 Kriteria & Dasar Penetapan Bobot (`Total = 100%`)

Setiap kriteria diturunkan langsung dari **5 parameter baku Buku Panduan Capstone (`hlm. 20`)** (*tingkat kesesuaian, kehandalan, sumber daya manusia/alat/bahan, waktu, dan biaya*) serta spesifikasi `CD-2`:

| Kode | Kriteria Penilaian | Parameter Resmi Panduan (`hlm. 20`) | Bobot | Alasan Ilmiah & Lapangan Penetapan Bobot |
|---|---|---|---:|---|
| **K1** | **Efisiensi Air (`WUE`), Akurasi Dosis (`10–15 L`), & Dukungan Pertumbuhan/Buah** | *Tingkat Kesesuaian (Kebutuhan Mitra & Agronomi)* | **20%** | Bobot tertinggi bersama K2 karena tujuan utama mitra (`CD-1` + survei `22 Nov`) adalah menghemat air/biaya penyiraman sekaligus mendukung pertumbuhan merata pada `4` pohon timpang (`46–250 cm`). |
| **K2** | **Ketahanan Anti-Mampet (*Anti-Clogging*) & Kemudahan Perawatan Petani (`S-14`)** | *Kehandalan (Reliability & Maintainability)* | **20%** | Bobot tertinggi bersama K1 karena literatur (`Z-16`, `ASCE`) membuktikan **penyumbatan (*clogging*) adalah penyebab kegagalan operasional nomor 1** pada sistem irigasi mikro; sistem yang sulit dirawat akan ditinggalkan petani. |
| **K3** | **Kelayakan Instalasi pada Lahan Urugan & Jadwal Realisasi TA (`<= 6 Bulan`)** | *Sumber Daya (Alat/Bahan/Tapak) & Waktu* | **15%** | Tapak `Kebun Kecil` adalah lahan bekas empang/sampah dengan pohon `16 bulan` yang sudah berakar aktif; metode pasang yang merusak akar atau terlalu lama menggali mengancam jadwal TA. |
| **K4** | **Keamanan Jamur Daun/Akar, Penekanan Gulma, Salinitas (`ECe`), & Proteksi Fisik Pipa** | *Tingkat Kesesuaian Lingkungan & Kehandalan Fisik* | **15%** | Mitra menegaskan jamur daun sebagai hama utama (`transkrip L254–258`), cuaca Subang panas terik (UV & penguapan tinggi), dan tanah liat rawan penumpukan garam permukaan (`Z-15`). |
| **K5** | **Kedalaman Rekayasa Teknik Komputer & Keselarasan Pembagian Tim `3` Orang** | *Tingkat Kesesuaian Akademik & Sumber Daya Manusia* | **15%** | Menjamin solusi memenuhi kriteria *Complex Engineering Problem* S1 Teknik Komputer (`kalibrasi, Fuzzy + Pulse Drip, fault detection, IoT 4G remote tuning`) dan terbagi adil untuk `3` anggota tim (`CLO4`). |
| **K6** | **Efisiensi Biaya Purwarupa (`S-08 <= Rp5 jt`) & Potensi Replikasi (`72–73` Pohon)** | *Biaya (CAPEX & OPEX)* | **15%** | Menjamin purwarupa tetap terjangkau anggaran mahasiswa tanpa PLTS mahal dan kelak ekonomis saat mitra mengekspansi ke seluruh `72–73` pohon untuk menggantikan `Alkon` + `2` pekerja (`Rp200 rb / 3–4 hari`). |

---

### 5.2 Rubrik Definisi Skala Skor `1–5` (Standar Objektif Anti-Tebak)

Setiap skor yang diberikan ke suatu alternatif **harus dicocokkan dengan definisi baku berikut** sebelum dimasukkan ke matriks:

| Skor | Arti Umum | Standar Pembuktian yang Wajib Dipenuhi |
|:---:|---|---|
| **5** | **Sangat Baik / Optimal** | Terbukti unggul langsung oleh data jurnal/uji lapangan **tanpa** risiko besar atau kompromi operasional di `Kebun Kecil`. |
| **4** | **Baik** | Memenuhi penuh kebutuhan dan target `CD-2`/`Kebun Kecil`, namun kalah tipis dibanding alternatif terbaik atau memiliki 1 keterbatasan minor yang mudah dimitigasi. |
| **3** | **Cukup (Dengan Mitigasi Berat)** | Dapat berjalan, tetapi memiliki risiko teknis/operasional nyata di `Kebun Kecil` (mis. rawan mampet tersembunyi, butuh galian dekat akar, atau butuh komponen/perawatan ekstra). |
| **2** | **Kurang** | Memerlukan biaya, perawatan, atau modifikasi besar yang menyulitkan petani/mahasiswa, atau hanya memenuhi sebagian target utama. |
| **1** | **Sangat Buruk / Gagal Batasan** | Melanggar batasan lapangan atau spesifikasi kritis (mis. membasahi daun memicu jamur berat, tidak cocok kontur, atau melampaui pagu `Rp5 jt`). |

---

### 5.3 Tabel *Design Matrix Scoring* (Status Saat Ini: Duel `Alt. 1` vs `Alt. 2`, Siap Ditambah `Alt. 3`)

Rumus skor terbobot: $\text{Skor Total} = \sum_{k=1}^{6} (W_k \times S_k)$, dengan nilai maksimum `5,00` (`100%`).

| Kode | Kriteria | Bobot ($W_k$) | Alt. 1: *Surface Drip* (`FDI`) | Alt. 2: *Subsurface Drip* (`SDI`) | Alt. 3: `[Slot Pengisian]` |
|---|---|---:|:---:|:---:|:---:|
| **K1** | Efisiensi Air (`WUE`), Dosis `10–15 L`, & Dukungan Buah | `20%` | `4` (`0,80`) | **`5` (`1,00`)** | *Menunggu finalisasi Alt. 3* |
| **K2** | Ketahanan Anti-Mampet & Kemudahan Rawat Petani (`S-14`) | `20%` | **`5` (`1,00`)** | `3` (`0,60`) | *Menunggu finalisasi Alt. 3* |
| **K3** | Kelayakan Instalasi Tanah Urugan & Jadwal TA | `15%` | **`5` (`0,75`)** | `3` (`0,45`) | *Menunggu finalisasi Alt. 3* |
| **K4** | Aman Jamur Daun, Minim Gulma, Salinitas, & Proteksi Pipa | `15%` | `4` (`0,60`) | **`5` (`0,75`)** | *Menunggu finalisasi Alt. 3* |
| **K5** | Kedalaman Rekayasa CE & Pembagian Tim `3` Orang | `15%` | **`5` (`0,75`)** | **`5` (`0,75`)** | *Menunggu finalisasi Alt. 3* |
| **K6** | Efisiensi Biaya Purwarupa (`<= Rp5 jt`) & Replikasi | `15%` | **`5` (`0,75`)** | `4` (`0,60`) | *Menunggu finalisasi Alt. 3* |
| | **TOTAL SKOR TERBOBOT (Maks `5,00`)** | **`100%`** | **`4,65` (`93,0%`)** | **`4,15` (`83,0%`)** | *—* |

---

### 5.4 Audit Justifikasi Setiap Skor (Alasan Transparan per Baris)

| Kode | Perbandingan Skor (`Alt. 1` vs `Alt. 2`) | Justifikasi Objektif Berdasarkan Data Lapangan & Jurnal |
|---|---|---|
| **K1** | `FDI = 4` vs **`SDI = 5`** | **`SDI` diberi `5`** karena data 3 musim jeruk tanah liat (`Farag et al., 2025`, `Z-15`) dan *Vertisol* (`Meshram et al., 2025`) membuktikan `SDI` mencatat `WUE`, serapan `N-P-K`, dan hasil buah tertinggi (`+8,70%` hingga `+56,23%`) akibat penguapan permukaan nyaris nol. **`FDI` diberi `4`** karena tetap sangat efisien (`hemat 28,8%`, hasil `+12–15%`, `Z-06`), tetapi kalah tipis akibat sebagian penguapan permukaan di iklim terik Subang. |
| **K2** | **`FDI = 5`** vs `SDI = 3` | **`FDI` diberi `5`** karena gabungan `Disc Filter 120–150 mesh` + emiter PC + deteksi tekanan/aliran (`Z-04`, `Z-09`) + `Auto End-Flush` $\ge 0{,}6\text{ m/s}$ (`Z-16`) + inspeksi visual langsung membuat pembersihan/penggantian emiter sangat cepat untuk petani (`S-14`) dan bebas intrusi akar. **`SDI` diberi `3`** karena meskipun memakai filter & *flush* yang sama, risiko *root intrusion* & hisapan balik lumpur tetap ada, tidak tampak visual, dan bila mampet berat menuntut galian tanah. |
| **K3** | **`FDI = 5`** vs `SDI = 3` | **`FDI` diberi `5`** karena pemasangan di permukaan cepat, tidak merusak akar pohon `16 bulan` yang sudah berbuah, dan tidak terhambat sisa puing sampah urugan eks-empang. **`SDI` diberi `3`** karena penggalian melingkar `15–20 cm` di tanah urugan berpuing dekat akar aktif lebih berisiko, memakan waktu lebih lama, dan menuntut kehati-hatian ekstra. |
| **K4** | `FDI = 4` vs **`SDI = 5`** | **`SDI` diberi `5`** karena permukaan tanah tetap kering (menekan gulma & jamur leher batang), 100% bebas percikan ke daun, pipa terlindung dari UV/cangkul, serta kenaikan salinitas permukaan `ECe` jauh lebih rendah (`34,42%` vs `56,46%` dalam 3 musim, `Z-15`). **`FDI` diberi `4`** karena tetap 100% aman dari jamur daun (tetes di tanah), tetapi permukaan basah lebih mudah ditumbuhi gulma dan pipa terbuka di atas tanah. |
| **K5** | **`FDI = 5`** vs **`SDI = 5`** | **Keduanya diberi `5`** karena mendukung penuh seluruh arsitektur Teknik Komputer (`ESP32`, kalibrasi tanah lokal `Z-02`/`Z-11`, Logika Fuzzy + *Pulse Drip*, deteksi error aliran/tekanan `Z-04`/`Z-09`, *Auto End-Flush*, IoT 4G + `microSD` + *remote tuning*) dan dapat dibagi rata ke `3` anggota tim (*Hardware/Hidrolika/PCB*, *Embedded Control/Kalibrasi/Fuzzy*, *IoT 4G/Dashboard/Uji Banding*). |
| **K6** | **`FDI = 5`** vs `SDI = 4` | **`FDI` diberi `5`** karena biaya komponen paling efisien (`~Rp2,2–3,2 jt`, jauh di bawah `S-08 <= Rp5 jt`) memakai pipa PE `16 mm` standar dan mudah direplikasi bertahap ke `72–73` pohon. **`SDI` diberi `4`** karena tetap `< Rp5 jt` (`~Rp2,8–3,9 jt`), tetapi butuh komponen khusus tambahan (*dripline root-guard*, *air-vacuum relief valve*, dan biaya/tenaga galian). |

---

## 6. Daftar Pustaka Kunci yang Digunakan

1. **[Z-15 — *Full-Text* di Repo]** Farag, A. A., Abd El-Aziz, M. A., & El-Husseiny, A. M. (2025). *Evaluation of surface and subsurface drip irrigation on citrus tree productivity in clayey soils*. Scientific Reports, `PMC12479814`, DOI: `10.1038/s41598-025-19575-6`.
2. **[Eksternal Terverifikasi]** Meshram, D. T., Srivastava, A. K., Thirugnanavel, A., et al. (2025). *Agronomic response of subsurface versus surface drip irrigation in Nagpur mandarin (Citrus reticulata Blanco) on Indian Vertisol*. Frontiers in Horticulture, DOI: `10.3389/fhort.2025.1552283`.
3. **[Z-06 — *Full-Text* di Repo]** *Sensors* (2025). *Capacitive Soil Moisture Sensor Node for Citrus Drip Irrigation*. `PMC11902337`, DOI: `10.3390/s25051568`.
4. **[Z-11 — *Full-Text* di Repo]** Zakaria, Y. S. et al. (2026). *Solar Capacitive Soil Moisture Node Calibration with ESP32*. Sensors, `PMC13364378`, DOI: `10.3390/s26133979`.
5. **[Z-02 — *Full-Text* di Repo]** Domínguez-Niño, J. M. et al. (2019). *Differential, Field-Scale Calibration of Capacitive Soil Moisture Sensors in Orchards*. Sensors, `PMC6679572`, DOI: `10.3390/s19143101`.
6. **[Z-04 — *Full-Text* di Repo]** Meriç, M. K. (2025). *WSN Drip Irrigation with Latching Valve, Pulse Water Meter, and Pressure Monitoring*. Scientific Reports, `PMC12019383`, DOI: `10.1038/s41598-025-97303-w`.
7. **[Z-09 — *Full-Text* di Repo]** Zong, Q. et al. (2019). *Hydraulics of Self-Cleaning Screen Filters (`124 µm`)*. PLoS ONE, `PMC6922369`, DOI: `10.1371/journal.pone.0226354`.
8. **[Z-16 — *Full-Text* di Repo]** Lavanholi, R. et al. (2018). *Dripper Clogging by Solid Particles and Flushing Velocity*. Scientific World Journal, `PMC6218717`, DOI: `10.1155/2018/7697458`.
9. **[Eksternal Terverifikasi]** *INTENSIF* (2024). *Smart Drip Irrigation System Based on IoT Using Fuzzy Logic (ESP32)*. DOI: `10.29407/intensif.v8i1.21351`.
10. **[Pustaka `CD-1` di Repo]** Smajstrla, A. G. *Microirrigation Design & Uniformity (`UF/IFAS AE094`)* — `sumber/referensi jurnal/pustaka_cd1/17_UF_IFAS_AE094_Smajstrla.html`.

---

## 7. Daftar Pendalaman & Item Terbuka (Bisa Diubah/Ditambah di Sini)

- [ ] **Finalisasi Alternatif ke-3:** Putuskan apakah Slot Alternatif 3 diisi *Under-Canopy Micro-Jet* (referensi UF/IFAS) atau sekaligus membandingkan arsitektur *Multi-Node Nirkabel* (`ESP-NOW/LoRa`), lalu lengkapi baris skor & justifikasinya pada Bagian `5.3` & `5.4`.
- [ ] **Simulasi / Pengujian Awal (`Syarat Level-4 Rubrik CLO3 Pembimbing`):** Siapkan perhitungan/simulasi hidrolika untuk `Kebun Kecil` (`jarak sumur 12,27 m miring / 16,20 m siku`, *head loss* pipa `16 mm`, debit pompa, kecepatan *end-flush* $\ge 0{,}6\text{ m/s}$, serta simulasi permukaan aturan **Logika Fuzzy**).
- [ ] **Spesifikasi Pompa Sumur & Katup Cabang:** Konfirmasi jenis/kedalaman sumur baru di `Kebun Kecil` untuk mengunci pilihan pompa (`DC 12/24 V + PSU PLN` vs `AC kecil + relay`) dan tipe katup (`Motorized Ball Valve` vs `Solenoid NC/Latching` di hilir filter).
- [ ] **Konfirmasi ke Pembimbing 1 (Pak Agung):** Pastikan bobot arsitektur `1 Zona = 4 Pohon` + `4` pohon pembanding manual + `5` lapis anti-mampet + Fuzzy + IoT 4G sudah ACC untuk pembagian `3` mahasiswa TA sebelum naskah `CD-3` ditulis.
