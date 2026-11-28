# README Alternatif Solusi & *Design Matrix Scoring* `CD-3` (`Kebun Kecil` — `1 Zona = 4 Pohon`)

**Tanggal Penyusunan:** 28 November 2026 *(Diperbarui: Integrasi Audit Hidrolika, Agronomi Jeruk Limau, Kalibrasi Non-Linear, & Paket Software)*  
**Status Dokumen:** Sumber Kebenaran Tunggal (*Single Source of Truth*) — **Basis `CD-3` (`tenggat CLO3 CD3-1: Kamis, 10 Desember 2026`)**. Seluruh parameter hidrolika (`2` penetes permukaan `1,5–2,0 L/mnt` + `Bypass BP` + `Sumur Bor 2 Jalur`), kelistrikan (`SSR-25DA`, `PSU SELV 12V`, `Divider 3,3V`, `IEC 60364-7-705`), agronomi *Citrus × amblycarpa*, serta desain *software* (`DFD 0/1`, `ERD 3NF`, `Wireframe UI`) telah diselaraskan lintas tim (`Daffa, Ariq, Qarnie`). *(Identitas resmi Pembimbing 2 untuk Lembar Pengesahan `CD-3`: **Fussy Mentari Dirgantara, S.T., M.T.**, `NIDN: 0415039501`, Kode: `FUY`.)*

> [!IMPORTANT]
> **Status Naskah Akademik:** Berkas `dokumen/cd1/`, `dokumen/cd2/`, `dokumen/cd3/`, dan `dokumen/draf/` **tidak diubah** pada tahap ini. Seluruh draf `CD-3` lama berstatus tidak terpakai; dokumen ini menjadi acuan inti sebelum merakit naskah final `CD-3` berbasis lokasi ACC `Kebun Kecil` (`22 November 2026`).

**Tautan Acuan Resmi & Konteks Terkait:**
- Panduan & Template Resmi `CD-3`: [Buku Panduan Capstone 2024](../sumber/panduan/bukupanduancapstone_2024signed.pdf) *(hlm. 19–21)* · [Template FTE-CD-3](../sumber/template/FTE-CD-3%20-edited_PBD.pdf) · [Jadwal & Rubrik PTA 2627](../sumber/rubrik-jadwal/Jadwal_PTA%20--%20Rubrik%20PTA%20--%202627%20%281%29.pdf)
- Dokumen Transisi, Data Lapangan, & Spesifikasi Hardware/Software: [README Transisi](README_TRANSISI_KEBUN_BESAR_KE_KEBUN_KECIL_CD2_CD3.md) · [Data Kebun Kecil & Zona 4 Pohon](DATA_KEBUN_KECIL_DAN_ZONA_4_POHON.md) · [Skema Pemipaan 2 Jalur Sumur Bor](skema_pipa_zona_4_pohon_teknis.png) · [Diagram Blok](diagram_blok_sistem_kebun_kecil.png) · [Flowchart](flowchart_sistem_kebun_kecil.png) · [Wiring & Layout Panel/PCB + KiCad](SPESIFIKASI_WIRING_PINOUT_DAN_SUMUR_BOR.md) · [DFD 0/1, ERD, & Wireframe UI](SPESIFIKASI_SOFTWARE_DFD_ERD_UI_CD3.md) · [Daftar Alat & RAB 2 Fase](DAFTAR_ALAT_DAN_RAB_CD3_KEBUN_KECIL.md)
- Kompilasi Riset & Review Tim (`-garnie`): [Kumpulan Referensi Terverifikasi](../sumber/referensi%20jurnal/draf/referensi_garnie_cd3/Kumpulan_Referensi_Terverifikasi_CD3_Kebun_Kecil-garnie.md) · [Deep Research Agronomi *C. amblycarpa*](../sumber/referensi%20jurnal/draf/referensi_garnie_cd3/Hasil_Deep_Research_Agronomi_Jeruk_Limau_CD3-garnie.md) · [Review & Saran Draf `CD-3`](Review_dan_Saran_CD3_Kebun_Kecil-garnie.md)
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

## 2. Arsitektur Inti Bersama (*Core Computer Engineering*, Hidrolik Tervalidasi, & 5 Lapis Anti-Mampet)

Agar seluruh alternatif yang dibandingkan **tetap murni S1 Teknik Komputer** (bukan alat `if kering -> pompa ON` sederhana, dan bukan riset agronomi murni), seluruh alternatif pada `Kebun Kecil` (`1 Zona = 4 Pohon Sampel` + `4` pohon kontrol manual sebagai data uji banding TA) berbagi pondasi sistem tertanam, hidrolika aman, catu daya, dan proteksi anti-mampet berikut:

1. **Kontrol Adaptif Tertutup (*Closed-Loop Fuzzy + Pulse Drip* tanpa Sensor Hujan):**
   - Keputusan mulai menyiram pada jadwal cek RTC (diprioritaskan **pagi/sore hari**) didasarkan **murni pada pembacaan `VWC < Ambang`**, tanpa sensor hujan terpisah (jika hujan turun, kadar air tanah otomatis naik melampaui ambang batas sehingga penyiraman dilewati).
   - Sensor lengas kapasitif (`4` titik, wajib dilapisi **epoksi/karet kedap air + `R_pd 1 MΩ`**, ditanam kedalaman **`15–20 cm`** berjarak `10–15 cm` dari penetes) & suhu tanah (`DS18B20` 1-Wire) dikalibrasi menggunakan **sampel tanah merah asli `Kebun Kecil`**. Mengadopsi temuan kalibrasi tanah liat merah tropis (*Red Oxisol*, `Duarte et al., 2021`), kurva regresi ditingkatkan dari linear menjadi **model hiperbolik non-linear $y = \frac{1}{a + b x}$** ($R^2 = 0{,}96$, $\text{RMSE} = 0{,}019\text{ m}^3/\text{m}^3$) dengan *moving average* `10×` sampel melalui **`ADS1115` 16-bit (`I2C`)** agar bebas galat kurva pabrik (`Z-02`, `Z-11`).
   - Algoritma **Logika Fuzzy** di **ESP32** menghitung **target volume adaptif** sesuai ukuran dan kesehatan tiap pohon agar tidak memicu *waterlogging* maupun busuk akar *Phytophthora*: **`P1 (46 cm, kerdil)` dibatasi `1,5–2,0 L/hari` (`~3–4 L/siklus kering`)**, **`P2 (100 cm)` `5–6 L/hari` (`~8–10 L/siklus`)**, dan **`P3/P4 (210–250 cm)` `10–12 L/hari` (`maks 15 L/siklus`)**. Penyiraman dijalankan bergantian (`1` *flow sensor* `YF-B1` + `4` katup cabang `V1–V4`) memakai ***Pulse Drip* (`maks 5 L/putaran`)**; jeda serap aktif `15 menit` hanya dieksekusi bila sisa pohon di antrean tinggal `1` pohon.
   - **Kesesuaian Debit Opsi 1 (`1,5–2,0 L/menit` per pohon) & *Recirculation Bypass* Sumur Bor:** Sensor `YF-B1 / YF-S201` memiliki batas baca minimum `1,0 L/menit`. Oleh karena itu, `2` penetes *adjustable / micro-bubbler* per pohon diset pada **`1,5–2,0 L/menit`** (selalu terbaca akurat oleh `YF-B1`, total durasi 4 pohon `< 1 jam`, jauh di bawah batas `S-03 <= 4,0 jam`, dan 100% sinkron dengan jobdesk `2` penetes/pohon), dilengkapi **cabang 2 jalur sumur bor (`SK-A` Alkon + `SK-B/CV` pompa listrik kita)** serta **pipa *recirculation bypass* (`BP`) di hilir `CV`**.
2. **Catu Daya Aman Hibrida (`Pompa AC 220V` + `Zona SELV 12V/5V DC`) & Konektivitas `Wi-Fi → Router 4G`:**
   - **Pemisahan Tegangan Pompa vs Zona Tanaman:** Untuk menghindari *voltage drop* berat (`~2–3 V`) pada kabel `16–20 m`, pompa sumur dikunci memakai **Pompa Air `AC 220V` (`125 W`, non-cast iron / *engineering polymer* / *stainless steel*, arus rendah `~0,6 A`)** yang dialiri dari relai panel melalui kabel ber-*conduit* `20 mm` dengan proteksi **MCB + ELCB**. Sebaliknya, seluruh area basah zona pohon (`4` katup `V1–V4`, katup bilas `VF`, `4` sensor tanah, flow, tekanan, dan boks kontrol `ESP32`) **100% menggunakan tegangan aman `SELV 12V / 5V DC` (`S-07`)**.
   - **Konektivitas & Keamanan Lokal:** Di dalam panel IP65 dipasang **`Router / MiFi 4G`**; **`ESP32` terhubung via `Wi-Fi` lokal ke `Router 4G`** tersebut untuk bertukar data dan *remote parameter tuning* melalui protokol **MQTT** (Bojongsoang ↔ Subang). Sistem dilengkapi **`RTC DS3231` + `microSD`** (*store-and-forward* agar nol data hilang saat sinyal seluler turun) serta **`1` tombol fisik lokal (`S-13`)** yang juga berfungsi sebagai tombol **`STOP` darurat** apabila ditekan saat penyiraman sedang berlangsung (Tahap 2).
3. **5 Lapis Rekayasa Anti-Mampet (*Anti-Clogging Engineering* — Nilai Tambah Utama):**
   - **Lapis 1 (Filtrasi & Material Pompa):** *Disc Filter* `120–150 mesh` (`100–130 µm`, celah $1/7\text{–}1/10$ labirin emiter) + **pompa rumah polimer teknik / *stainless steel*** (dilarang memakai besi cor/*cast iron* agar serpihan karat tidak menyumbat hilir filter, `Z-16`).
   - **Lapis 2 (Emiter & Posisi Katup):** Penetes *adjustable* / *micro-bubbler* berbukaan lega (`1,5–2,0 L/mnt` per pohon) atau emiter `PC` *self-flushing* + penempatan katup cabang (`Solenoid NC 12V` atau `Motorized Ball Valve Full-Bore 12V`) di **hilir filter**.
   - **Lapis 3 (Deteksi Dini Mampet & *Dry-Run* Berbasis `1×` Sensor Tekanan Hilir + *Flow Sensor*):** Karena hanya terpasang **`1` sensor tekanan** di hilir filter, deteksi gangguan membandingkan tekanan kerja aktual `P` terhadap rentang normal kalibrasi **`[P_min, P_max]`** serta pulsa `YF-B1/YF-S201` (`Z-04`, `Z-09`):
     - ***Dry-Run* / Filter Hulu Mampet Berat / Sumur Kering (`Flow = 0 > 10 dtk` dan/atau `P < P_min`):** Matikan pompa dulu lalu tutup katup aktif (cegah *water hammer*), kirim alarm darurat ke HP + simpan log `microSD`, dan **hentikan seluruh siklus** kembali ke mode siaga (`L`) agar pompa tidak terbakar.
     - **Mampet Cabang / Katup Macet pada Pohon $i$ (`P > P_max` dan/atau debit anjlok di bawah batas kalibrasi):** Matikan pompa dulu lalu tutup katup `Vi`, tandai `Pohon i = Error/Skip` + kirim alarm cabang spesifik ke HP + simpan log `microSD`, lalu **lanjutkan antrean ke pohon berikutnya (`i + 1`)** *(tidak buntu/hang)*.
   - **Lapis 4 (Pembilasan Pipa Otomatis / *Auto End-Flush*):** Karena kecepatan alir di cabang kadang rendah dan berpotensi mengendapkan lanau halus (`< 0,6 m/s`, `Z-16`), dipasang **`1` katup buang ujung (`VF`)** yang dibuka otomatis oleh ESP32 selama **`30–45 detik`** (`Z-09`) secara berkala (`v >= 0,6 m/s`, kurva optimal `Q = 6,0 L/mnt`) untuk menyapu endapan keluar ujung pipa.
   - **Lapis 5 (Proteksi Khusus Jalur Tanam — Khusus Alternatif 2 `SDI`):** Pemasangan ***air-vacuum relief valve*** untuk mencegah hisapan balik lumpur (*soil suction*) saat pompa berhenti, serta emiter berpelindung akar (*root-barrier*).

---

## 3. Profil Detail Alternatif Solusi (Format Subbab `1.1 FTE-CD-3`)

Seluruh **3 alternatif solusi** di bawah ini disusun setara untuk mencapai target `10–15 L/pohon` yang merata di `Zona Uji 1` (`4` pohon sampel `16 bulan`) dengan kontrol cerdas Teknik Komputer (`ESP32`, Fuzzy + *Pulse Drip*, proteksi mampet, dan IoT).

### Alternatif 1 — Irigasi Tetes Permukaan Presisi Independen Per-Pohon (*Precision Surface Drip / FDI*) + Fuzzy + *Auto End-Flush* + IoT 4G
- **Dasar Pemilihan Alternatif:** Hasil survei `22 Nov 2026` memperlihatkan `4` pohon sampel (`16 bulan`) tumbuh timpang (`46–250 cm`) di tanah merah urugan bekas empang/sampah, daun tidak boleh basah karena rentan **jamur daun** (`transkrip L254–258`), dan perawatan di kebun harus mudah dikerjakan mitra. Studi kebun jeruk tanah liat (`Farag et al., 2025`, `Z-15`) dan sistem tetes ESP32 (`Sensors 2025`, `Z-06`; `Zakaria et al., 2026`, `Z-11`) membuktikan tetes permukaan menghemat air `28,8%` dan menaikkan hasil `12–15%`. Agar sesuai kurva baca minimal `1,0 L/menit` *flow sensor* induk `YF-B1/YF-S201` sekaligus mencegah pompa sumur tercekik, tiap pohon menggunakan `2` penetes *adjustable / micro-bubbler* di atas permukaan tanah (`total 1,5–2,0 L/mnt` per pohon) plus pipa cabang *bypass* balik ke sumur.
- **Fitur Utama:**
  - Cincin pipa PE `16 mm` diletakkan **di atas permukaan tanah** melingkari pangkal akar tiap pohon (`2` penetes *adjustable / micro-bubbler* per pohon, debit setara `1,5–2,0 L/mnt` per pohon agar `YF-B1/YF-S201` akurat), lengkap dengan **pipa *bypass* balik ke sumur** pada kepala pompa `AC 220V` (`125 W` ber-MCB/ELCB).
  - Kendali independen `4` katup cabang (`V1–V4` `12V DC`) + `1` *flow sensor* `YF-B1/YF-S201` + `1` sensor tekanan hilir (`[P_min, P_max]`) + `4` node sensor lengas kapasitif & suhu tanah terkalibrasi + algoritma **Fuzzy + *Pulse Drip*** (`3 × 5 L`).
  - Sistem anti-mampet 4 lapis (`Disc Filter 120–150 mesh`, *fault detection* `P_min/P_max` + *dry-run/mampet cabang*, dan **`Auto End-Flush` $\ge 0{,}6\text{ m/s}$** `30–45 detik`).
- **Fitur Tambahan:** *Edge buffering* (`RTC DS3231 + microSD`), konektivitas `ESP32 Wi-Fi → Router 4G` (MQTT + *remote parameter tuning* Bojongsoang ↔ Subang), serta `1` tombol fisik lokal (`S-13`) yang juga berfungsi sebagai *emergency STOP*.
- **Data Referensi / Pengujian Awal:**
  - `Sensors (2025)` (`PMC11902337`, `Z-06`): ESP32 + `4× SEN0193` di kebun jeruk hemat air **`28,8%`** & hasil naik **`12–15%`**.
  - `Zakaria et al. (2026)` (`PMC13364378`, `Z-11`): kalibrasi lokal `Capacitive v1.2` + `1 MΩ` *pull-down* + LDO `AP2112` mencapai $R^2 = 0{,}92\text{–}0{,}94$ (RMSE `0,40–0,52%`).
  - `Meriç (2025)` (`PMC12019383`, `Z-04`): uji kebun `82` pohon memakai *water meter* + sensor tekanan untuk deteksi anomali.
  - `INTENSIF (2024)` (`DOI 10.29407/intensif.v8i1.21351`): *Smart Drip* ESP32 + Fuzzy mencatat akurasi respons inferensi **`92–94%`**.
- **Prosedur Pengoperasian:** Sistem berjalan otomatis (cek RTC → baca `4` sensor tanah → bila `VWC < Ambang`, hitung target liter Fuzzy → buka katup `Vi` sebelum nyalakan pompa → siram bertahap `1,5–2,0 L/mnt` metode *Pulse Drip* hingga `V_target` → matikan pompa sebelum tutup katup → jalankan *Auto End-Flush* terjadwal); mitra memantau/memicu via dashboard atau tombol fisik `S-13`; pembersihan filter dan `2` penetes permukaan dilakukan secara visual tanpa menggali tanah.

---

### Alternatif 2 — Irigasi Tetes Bawah Permukaan Presisi Independen Per-Pohon (*Precision Subsurface Drip / SDI*) + Fuzzy + *Air-Relief* + IoT 4G
- **Dasar Pemilihan Alternatif:** Pada iklim dataran rendah Subang yang terik (`32–36 °C`), tetes permukaan masih mengalami kehilangan penguapan dan kenaikan salinitas lapisan atas (`ECe`). Dua penelitian lapangan 2025 pada **jeruk di tanah liat** (`Farag et al., 2025`, *Sci. Rep.* `PMC12479814`; `Meshram et al., 2025`, *Front. Hortic.* `10.3389/fhort.2025.1552283`) menunjukkan penanaman jalur tetes di bawah permukaan (**`SDI`**) secara konsisten melampaui *surface drip* pada *Water Use Efficiency* (`WUE`), serapan `N-P-K`, dan hasil buah.
- **Fitur Utama:**
  - Cincin lateral tetes berdinding tebal dengan emiter *root-barrier* (`2` titik alir/pohon terkalibrasi di atas ambang flow `>= 1,0 L/mnt`, atau dikombinasikan dengan manifold zona) **ditanam di kedalaman `15–20 cm`** langsung di zona akar serabut `4` pohon sampel.
  - Arsitektur pompa AC ber-*bypass*, `4` katup cabang, kalibrasi sensor, Fuzzy + *Pulse Drip*, *flow/pressure fault detection* (`[P_min, P_max]`), `Auto End-Flush`, tombol `S-13`, dan `Wi-Fi → Router 4G` **setara dengan Alternatif 1**.
  - Tambahan wajib hidrolika bawah tanah: ***air-vacuum relief valve*** pada titik tertinggi manifold untuk mencegah hisapan balik lumpur (*soil suction clogging*) saat pompa mati.
- **Fitur Tambahan:** Permukaan tanah tetap kering sehingga menekan gulma sekitar batang, melindungi selang dari radiasi UV/cangkul pekerja, serta memperlambat akumulasi garam permukaan (`ECe`).
- **Data Referensi / Pengujian Awal:**
  - `Farag et al. (2025)` (`PMC12479814`, `Z-15`, uji 3 musim jeruk tanah liat): `Full SDI` mengungguli `Surface Drip` & banjir dengan **hemat air `31,58%`**, kenaikan **`WUE` `+58,87%` (hingga `2,96 kg/m³`)**, kenaikan serapan `N-P-K` (`+2,44% / +10,52% / +5,69%`), **hasil buah `+8,70%` (`25,0 t/ha`)**, dan kenaikan `ECe` lapisan atas 3 musim lebih rendah (`34,42%` vs `56,46%` pada *surface drip*).
  - `Meshram et al. (2025)` (`10.3389/fhort.2025.1552283`, jeruk keprok di tanah liat berat *Vertisol*): `SDI` menghasilkan produktivitas air **`7,96–10,73 kg/m³`** (vs *surface drip* `2,79–3,04 kg/m³`) dan kenaikan hasil buah **`15,86%–56,23%`**.
- **Prosedur Pengoperasian:** Operasi kontroler, deteksi gangguan, dan aplikasi IoT identik dengan Alternatif 1; namun pemasangan awal menuntut penggalian parit cincin `15–20 cm` di sekitar akar pohon `16 bulan` (di tanah bekas empang/sampah), dan pemeliharaan mampet/intrusi akar sangat bergantung pada pembacaan anomali `P_max`/flow serta pembongkaran tanah apabila terjadi sumbatan permanen.

---

### Alternatif 3 — Irigasi *Under-Canopy Micro-Jet* Bawah Tajuk Berbasis Zona Pohon + Fuzzy + Flow + IoT 4G
- **Dasar Pemilihan Alternatif:** Untuk kondisi air sumur lapangan yang berpotensi membawa lumpur halus dan puing organik tanah eks-empang, lubang nosel *micro-jet* (`0,8–1,5 mm`) menurut pedoman mikroirigasi jeruk `Smajstrla` (`UF/IFAS AE094`, tersedia di `pustaka_cd1/`) memiliki toleransi partikel paling baik dan langsung terpantau visual, sekaligus berpotensi menurunkan suhu iklim mikro di bawah tajuk pohon besar (`210–250 cm`).
- **Fitur Utama:**
  - Memasang **`2` pasak *micro-jet / micro-sprinkler* sudut semprot rendah (`tinggi 15–25 cm`)** di bawah tajuk tiap pohon (bukan *sprinkler* atas daun), menghasilkan pola pancar mendatar berdiameter sempit (`~0,8–1,2 m`) dengan debit total **`~1,8–2,4 L/menit` per pohon** (alami melampaui ambang `1,0 L/mnt` `YF-B1/YF-S201`).
  - Memakai arsitektur pompa AC ber-*bypass*, `Disc Filter 120–150 mesh`, `4` katup cabang `V1–V4` (`12V DC`), `1` sensor tekanan hilir, `4` node sensor lengas & suhu tanah terkalibrasi, algoritma **Fuzzy + *Pulse***, `Auto End-Flush`, tombol `S-13`, dan `Wi-Fi → Router 4G` setara Alternatif 1.
- **Fitur Tambahan:** Pendinginan mikro di bawah kanopi saat terik siang (`32–36 °C`), pemeriksaan nosel tersumbat seketika dengan mata telanjang, dan kompatibilitas tinggi terhadap debit alami pompa sumur tanpa *head* tekan berlebih.
- **Data Referensi / Pengujian Awal:**
  - `Smajstrla, A. G. (UF/IFAS AE094)`: *Under-canopy microirrigation* pada kebun sitrus mencapai keseragaman aplikasi `EU >= 85–90%` dengan kebutuhan filtrasi lebih ringan (`100–120 mesh` cukup untuk nosel `>= 1,0 mm`), tetapi mengalami kehilangan evaporasi/angin **`10–18%` lebih tinggi** daripada tetes tertutup.
  - `Lavanholi et al. (2018)` (`Z-16`): diameter jalur alir `>= 0,8–1,0 mm` memangkas probabilitas *bridging* partikel tersuspensi secara signifikan dibanding labirin emiter sempit.
- **Prosedur Pengoperasian:** Siklus pembacaan RTC, kalibrasi `VWC`, perhitungan dosis Fuzzy, pembukaan katup bergantian `V1–V4`, serta kontrol dashboard 4G berjalan identik dengan Alternatif 1; pengecekan lapangan difokuskan pada penyetelan arah/sudut *micro-jet* agar semprotan tetap di bawah kanopi dan tidak memerciki daun bawah pohon kerdil `P1` (`46 cm`).

---

## 4. Tabel Perbandingan Teknis Detail (Berbasis Data Jurnal Nyata & Audit Hidrolika)

| Dimensi Perbandingan | Alternatif 1: *Precision Surface Drip* (`FDI`) | Alternatif 2: *Precision Subsurface Drip* (`SDI`) | Alternatif 3: *Under-Canopy Micro-Jet* | Sumber Referensi Terverifikasi |
|---|---|---|---|---|
| **Posisi & Cara Penyaluran Air** | Cincin PE `16 mm` di **atas permukaan tanah** (`2` penetes *adjustable* / *micro-bubbler* per pohon, set `1,5–2,0 L/mnt`), menetes terarah ke akar. | Cincin lateral anti-akar **dikubur `15–20 cm`** di zona akar (`>= 1,0 L/mnt`) + *air-vacuum relief valve*. | `2` pasak *micro-jet* rendah `15–25 cm` bawah tajuk (`1,8–2,4 L/mnt`), pancar halus mendatar. | `Farag et al. (2025)` [`Z-15`]; `Smajstrla` (`UF/IFAS AE094`). |
| **Otak Kendali, Sensor, Daya, & IoT** | `ESP32` (`Wi-Fi → Router 4G` MQTT) + `4` sensor lengas/suhu tanah lokal + Fuzzy + *Pulse Drip* (`3 × 5 L`) + `1× YF-B1/YF-S201` + `1×` sensor tekanan (`[P_min, P_max]`) + `Auto End-Flush` + pompa `AC 220V` (*bypass* sumur) + zona `12V SELV` + tombol `S-13`. | Identik dengan Alt. 1 + pengecekan anomali tekanan balik jalur tanam. | Identik dengan Alt. 1 (durasi Fuzzy disesuaikan faktor penguapan & *drift*). | `Zakaria et al. (2026)` [`Z-11`]; `Meriç (2025)` [`Z-04`]; `INTENSIF (2024)`. |
| **Efisiensi Air (`WUE`) & Penghematan** | Hemat air **`28,8%`** (tetes sensor jeruk); penguapan permukaan terkendali dengan *Pulse Drip*. | **Unggul:** hemat **`31,58%`**, `WUE` **`+58,87%`** (`2,96 kg/m³`), *Vertisol* **`7,96–10,73 kg/m³`**. | Sedang (`10–18%` evaporasi/*drift* lebih tinggi daripada sistem tetes tertutup). | `Sensors (2025)` [`Z-06`]; `Farag et al. (2025)` [`Z-15`]; `Meshram et al. (2025)`; `AE094`. |
| **Dampak ke Pertumbuhan & Hasil Buah** | Hasil naik **`12–15%`** dibanding jadwal konvensional. | **Unggul:** hasil **`+8,70%`** (`25,0 t/ha`) vs `FDI`/banjir & serapan `N-P-K` lebih tinggi. | Baik untuk pohon besar (`210–250 cm`); perlu pembatasan radius untuk pohon kerdil `46 cm`. | `Sensors (2025)` [`Z-06`]; `Farag et al. (2025)` [`Z-15`]; `Meshram et al. (2025)`. |
| **Risiko Mampet & Kemudahan Rawat (`S-14`)** | **Unggul di tetes:** bebas intrusi akar; bukaan `1,5–2,0 L/mnt` lebih lega, mampet tampak visual & cepat dibersihkan (`Disc Filter` + `Auto End-Flush`). | **Rawan:** risiko *root intrusion* & *soil suction*; tidak tampak mata, perbaikan harus gali tanah. | **Sangat tahan mampet** (nosel `0,8–1,5 mm`) & paling mudah dicek visual; rawan semut/serangga di nosel. | `Lavanholi et al. (2018)` [`Z-16`]; `Zong et al. (2019)` [`Z-09`]; `AE094`. |
| **Keamanan Jamur Daun, Gulma, & Pipa** | Aman jamur daun; area basah terbatas di cincin akar (`ECe` 3 musim `+56,5%`); pipa terbuka di atas tanah. | **Unggul:** permukaan kering (minim gulma & bebas jamur leher batang), pipa terlindung, `ECe` terendah (`+34,4%`). | **Risiko tinggi:** percikan semprotan berpotensi membasahi daun bawah pohon kerdil `46 cm` (jamur daun) & gulma paling luas. | `Farag et al. (2025)` [`Z-15`]; `transkrip_survey_limau.md` (`L254–258`). |
| **Instalasi di Tanah Eks-Empang (`16 Bln`)** | **Sangat mudah:** tanpa gali, tidak mengganggu akar `16 bulan` & puing urugan eks-empang. | **Lebih sulit:** butuh galian melingkar `15–20 cm` di tanah urugan sampah dekat akar aktif. | Mudah (tancap pasak), perlu penyetelan sudut/penghalang percikan per pohon. | `DATA_KEBUN_KECIL_DAN_ZONA_4_POHON.md`. |
| **Estimasi CAPEX Purwarupa (`4` Pohon)** | **`Rp2,63–4,03 jt`** *(Paket A)* / **`Rp3,44–5,00 jt`** *(Paket B)* — **Lolos `S-08 <= Rp5 jt`** | **`~Rp3,3–4,8 juta`** *(pipa *root-guard* + *air-vacuum valve* + jasa/alat galian)* | **`~Rp2,7–4,1 juta`** *(nosel *micro-jet* + pelindung percikan, tetap `<= Rp5 jt`)* | Diselaraskan dengan [DAFTAR_ALAT_DAN_RAB_CD3_KEBUN_KECIL.md](DAFTAR_ALAT_DAN_RAB_CD3_KEBUN_KECIL.md). |

---

## 5. Metodologi *Design Matrix Scoring* (Aturan Panduan & Dasar Anti-Sembarangan)

Sesuai **[Buku Panduan Capstone 2024](../sumber/panduan/bukupanduancapstone_2024signed.pdf)** (`hlm. 20`) dan **[Template FTE-CD-3](../sumber/template/FTE-CD-3%20-edited_PBD.pdf)** (`hlm. 4`), pemberian bobot dan skor **tidak boleh bersifat subjektif/asal-asalan**. Berikut aturan formal yang mengikat seluruh angka pada matriks pemilihan kita:

### 5.1 Pemetaan 6 Kriteria & Dasar Penetapan Bobot (`Total = 100%`)

Setiap kriteria diturunkan langsung dari **5 parameter baku Buku Panduan Capstone (`hlm. 20`)** (*tingkat kesesuaian, kehandalan, sumber daya manusia/alat/bahan, waktu, dan biaya*) serta dipetakan langsung ke spesifikasi **`CD-2` (`S-01..S-14`)**:

| Kode | Kriteria Penilaian | Keterkaitan Spesifikasi `CD-2` | Parameter Resmi Panduan (`hlm. 20`) | Bobot | Alasan Ilmiah & Lapangan Penetapan Bobot |
|---|---|---|---:|---:|---|
| **K1** | **Efisiensi Air (`WUE`), Akurasi Dosis (`10–15 L`), & Dukungan Pertumbuhan/Buah** | `S-01, S-02, S-03` | *Tingkat Kesesuaian (Kebutuhan Mitra & Agronomi)* | **20%** | Bobot tertinggi bersama K2 karena tujuan utama mitra (`CD-1` + survei `22 Nov`) adalah menghemat air/biaya penyiraman sekaligus mendukung pertumbuhan merata pada `4` pohon timpang (`46–250 cm`). |
| **K2** | **Ketahanan Anti-Mampet (*Anti-Clogging*) & Kemudahan Perawatan Petani** | `S-05, S-14` | *Kehandalan (Reliability & Maintainability)* | **20%** | Bobot tertinggi bersama K1 karena literatur (`Z-16`, `ASCE`) membuktikan **penyumbatan (*clogging*) adalah penyebab kegagalan operasional nomor 1** pada sistem irigasi mikro; sistem yang sulit dirawat akan ditinggalkan petani. |
| **K3** | **Kelayakan Instalasi pada Lahan Urugan & Jadwal Realisasi TA (`<= 6 Bulan`)** | `S-04, S-09` | *Sumber Daya (Alat/Bahan/Tapak) & Waktu* | **15%** | Tapak `Kebun Kecil` adalah lahan bekas empang/sampah dengan pohon `16 bulan` yang sudah berakar aktif; metode pasang yang merusak akar atau terlalu lama menggali mengancam jadwal TA. |
| **K4** | **Keamanan Jamur Daun/Akar, Penekanan Gulma, Salinitas (`ECe`), & Proteksi Pipa** | `S-07, S-11` | *Tingkat Kesesuaian Lingkungan & Kehandalan Fisik* | **15%** | Mitra menegaskan jamur daun sebagai hama utama (`transkrip L254–258`), cuaca Subang panas terik (UV & penguapan tinggi), dan tanah liat rawan penumpukan garam permukaan (`Z-15`). |
| **K5** | **Kedalaman Rekayasa Teknik Komputer & Pembagian Tim `3` Orang** | `S-06, S-10, S-12, S-13` | *Tingkat Kesesuaian Akademik & Sumber Daya Manusia* | **15%** | Menjamin solusi memenuhi kriteria *Complex Engineering Problem* S1 Teknik Komputer (`kalibrasi, Fuzzy + Pulse Drip, fault detection, IoT Wi-Fi→4G remote tuning`) dan terbagi adil untuk `3` anggota tim (`CLO4`). |
| **K6** | **Efisiensi Biaya Purwarupa (`<= Rp5 jt`) & Potensi Replikasi (`72–73` Pohon)** | `S-08` | *Biaya (CAPEX & OPEX)* | **15%** | Menjamin purwarupa tetap terjangkau anggaran mahasiswa tanpa PLTS mahal dan kelak ekonomis saat mitra mengekspansi ke seluruh `72–73` pohon untuk menggantikan `Alkon` + `2` pekerja (`Rp200 rb / 3–4 hari`). |

---

### 5.2 Rubrik Definisi Skala Skor `1–5` (Standar Objektif Anti-Tebak)

Setiap skor yang diberikan ke suatu alternatif **harus dicocokkan dengan definisi baku berikut** sebelum dimasukkan ke matriks:

| Skor | Arti Umum | Standar Pembuktian yang Wajib Dipenuhi |
|:---:|---|---|
| **5** | **Sangat Baik / Optimal** | Terbukti unggul langsung oleh data jurnal/uji lapangan **tanpa** risiko besar atau kompromi operasional di `Kebun Kecil`. |
| **4** | **Baik** | Memenuhi penuh kebutuhan dan target `CD-2`/`Kebun Kecil`, namun kalah tipis dibanding alternatif terbaik atau memiliki 1 keterbatasan minor yang mudah dimitigasi. |
| **3** | **Cukup (Dengan Mitigasi Berat)** | Dapat berjalan, tetapi memiliki risiko teknis/operasional nyata di `Kebun Kecil` (mis. rawan mampet tersembunyi, butuh galian dekat akar, atau evaporasi angin lebih tinggi). |
| **2** | **Kurang** | Memerlukan modifikasi/perawatan ekstra dan menyisakan risiko biologis/operasional nyata di lahan (`mis. percikan memicu jamur daun` atau hanya memenuhi sebagian target utama). |
| **1** | **Sangat Buruk / Gagal Batasan** | Melanggar batasan lapangan atau spesifikasi kritis (mis. menyemprot tajuk penuh, tidak cocok kontur, atau melampaui pagu `Rp5 jt`). |

---

### 5.3 Tabel *Design Matrix Scoring* (3 Alternatif Lengkap — Tanpa Skor "Rata Kanan")

Rumus skor terbobot: $\text{Skor Total} = \sum_{k=1}^{6} (W_k \times S_k)$, dengan nilai maksimum `5,00` (`100%`).

| Kode | Kriteria | Bobot ($W_k$) | Alt. 1: *Surface Drip* (`FDI`) | Alt. 2: *Subsurface Drip* (`SDI`) | Alt. 3: *Under-Canopy Micro-Jet* |
|---|---|---:|:---:|:---:|:---:|
| **K1** | Efisiensi Air (`WUE`), Dosis `10–15 L`, & Dukungan Buah | `20%` | `4` (`0,80`) | **`5` (`1,00`)** | `3` (`0,60`) |
| **K2** | Ketahanan Anti-Mampet & Kemudahan Rawat Petani (`S-14`) | `20%` | **`5` (`1,00`)** | `3` (`0,60`) | **`5` (`1,00`)** |
| **K3** | Kelayakan Instalasi Tanah Urugan & Jadwal TA | `15%` | **`5` (`0,75`)** | `3` (`0,45`) | `4` (`0,60`) |
| **K4** | Aman Jamur Daun, Minim Gulma, Salinitas, & Proteksi Pipa | `15%` | `4` (`0,60`) | **`5` (`0,75`)** | `2` (`0,30`) |
| **K5** | Kedalaman Rekayasa CE & Pembagian Tim `3` Orang | `15%` | **`5` (`0,75`)** | **`5` (`0,75`)** | `4` (`0,60`) |
| **K6** | Efisiensi Biaya Purwarupa (`<= Rp5 jt`) & Replikasi | `15%` | **`5` (`0,75`)** | `4` (`0,60`) | `4` (`0,60`) |
| | **TOTAL SKOR TERBOBOT (Maks `5,00`)** | **`100%`** | **`4,65` (`93,0%`)** | **`4,15` (`83,0%`)** | **`3,70` (`74,0%`)** |

---

### 5.4 Audit Justifikasi Setiap Skor (Alasan Transparan per Baris untuk Ketiga Alternatif)

| Kode | Perbandingan Skor (`Alt. 1` vs `Alt. 2` vs `Alt. 3`) | Justifikasi Objektif Berdasarkan Data Lapangan & Jurnal |
|---|---|---|
| **K1** | `FDI = 4` vs **`SDI = 5`** vs `Micro-Jet = 3` | **`SDI` diberi `5`** karena data 3 musim jeruk tanah liat (`Farag et al., 2025`, `Z-15`) dan *Vertisol* (`Meshram et al., 2025`) membuktikan `SDI` mencatat `WUE`, serapan `N-P-K`, dan hasil buah tertinggi (`+8,70%` hingga `+56,23%`) akibat penguapan permukaan nyaris nol. **`FDI` diberi `4`** karena tetap sangat efisien (`hemat 28,8%`, hasil `+12–15%`, `Z-06`) dan *Pulse Drip* menjaga air di zona akar, hanya kalah tipis oleh penguapan permukaan. **`Micro-Jet` diberi `3`** karena menurut `AE094 Smajstrla`, pancaran udara mengalami kehilangan evaporasi/angin `10–18%` lebih tinggi dibanding tetes tertutup. |
| **K2** | **`FDI = 5`** vs `SDI = 3` vs **`Micro-Jet = 5`** | **`FDI` dan `Micro-Jet` diberi `5`**: `Micro-Jet` memiliki nosel lebar `0,8–1,5 mm` yang sangat tahan partikel (`Z-16`) dan tampak mata seketika; `FDI` memakai `2` penetes *adjustable* `1,5–2,0 L/mnt` di atas tanah + `Disc Filter 120–150 mesh` + deteksi `[P_min, P_max]`/flow (`Z-04`, `Z-09`) + `Auto End-Flush` $\ge 0{,}6\text{ m/s}$ sehingga cepat dicek dan dibersihkan petani (`S-14`) tanpa intrusi akar. **`SDI` diberi `3`** karena risiko *root intrusion* & *soil suction* tidak tampak visual dan bila mampet permanen menuntut galian tanah. |
| **K3** | **`FDI = 5`** vs `SDI = 3` vs `Micro-Jet = 4` | **`FDI` diberi `5`** karena pemasangan di permukaan cepat, tanpa gali, tidak mengganggu akar `16 bulan` maupun puing urugan eks-empang. **`Micro-Jet` diberi `4`** karena mudah dipasang (tancap pasak), namun butuh penyetelan sudut/penghalang semprotan khusus per pohon yang tingginya berbeda (`46–250 cm`). **`SDI` diberi `3`** karena penggalian melingkar `15–20 cm` di tanah urugan berpuing dekat akar aktif lebih berisiko dan memakan waktu konstruksi TA lebih lama. |
| **K4** | `FDI = 4` vs **`SDI = 5`** vs `Micro-Jet = 2` | **`SDI` diberi `5`** karena permukaan tanah tetap kering (minim gulma & bebas jamur batang), 100% bebas percikan daun, pipa terlindung UV/cangkul, dan kenaikan `ECe` paling rendah (`34,42%` vs `56,46%`, `Z-15`). **`FDI` diberi `4`** karena 100% aman dari jamur daun (tetes rapat di tanah), hanya permukaan basah terbatas memicu gulma ringan & pipa terbuka di atas tanah. **`Micro-Jet` diberi `2`** karena percikan pancaran pada jarak tanam terbuka dan pohon kerdil `P1` (`46 cm`) berisiko membasahi daun bawah sehingga memicu **jamur daun** yang dikeluhkan mitra (`transkrip L254–258`) serta menumbuhkan gulma paling luas. |
| **K5** | **`FDI = 5`** vs **`SDI = 5`** vs `Micro-Jet = 4` | **`FDI` dan `SDI` diberi `5`** karena memaksimalkan seluruh arsitektur Teknik Komputer (`ESP32`, kalibrasi tanah merah lokal `Z-02`/`Z-11`, Fuzzy + *Pulse Drip*, deteksi mampet `[P_min, P_max]` & *dry-run*, *Auto End-Flush*, `Wi-Fi → Router 4G` + `microSD` + *remote tuning*) dengan pembagian adil `3` anggota (`Ariq`, `Daffa`, `Qarnie`). **`Micro-Jet` diberi `4`** karena kontroler elektroniknya sama, tetapi kalibrasi presisi serapan titik akar kurang sensitif akibat pola semprot menyebar yang mudah terdorong angin. |
| **K6** | **`FDI = 5`** vs `SDI = 4` vs `Micro-Jet = 4` | **`FDI` diberi `5`** karena biaya paling efisien (`Rp2,68–4,08 jt` Paket A / `Rp3,46–4,97 jt` Paket B, lolos `S-08 <= Rp5 jt`) memakai pipa PE `16 mm` standar dan mudah direplikasi ke `72–73` pohon. **`SDI` diberi `4`** (`~Rp3,3–4,8 jt`, perlu *dripline root-guard*, *air-vacuum valve*, dan galian). **`Micro-Jet` diberi `4`** (`~Rp2,7–4,1 jt`, tetap `<= Rp5 jt`, namun butuh tambahan pelindung percikan/penyetel tekanan pancar per pohon). |

---

### 5.5 Justifikasi Ilmiah Pemilihan `FDI` (Atas Tanah) vs. `SDI` (Dalam Tanah) untuk Jeruk Limau `16 Bulan`

Meskipun studi lapangan menunjukkan *Subsurface Drip Irrigation* (`SDI`) mencatat efisiensi air (`WUE`) tertinggi (`Farag et al., 2025`, `Z-15`; `Meshram et al., 2025`), penerapan `SDI` bukanlah pilihan optimal bagi kondisi nyata **jeruk limau berumur `16 bulan` di tanah urugan `Kebun Kecil`** karena empat alasan berbasis literatur ilmiah berikut:

1. **Akar Serabut Dangkal Jeruk Limau & Risiko Pemotongan Akar pada Pohon `16 Bulan`:**  
   Menurut pedoman *UF/IFAS Extension* (*Florida Citrus Production Guide*, Morgan, Kadyampakeni, & Zekri), hingga **`~80%` akar serabut penyerap air dan hara (*fibrous feeder roots*) tanaman sitrus terkonsentrasi di lapisan tanah dangkal `0–25/30 cm` (*top 10 inches*)** di bawah zona pembasahan kanopi. Berbeda dengan kebun baru yang ditanam dari nol, keempat pohon sampel di `Kebun Kecil` (`P1–P4`) sudah berumur `16 bulan` dan sebagian telah berbuah lebat. Menggali parit cincin sedalam `15–20 cm` di dekat pangkal batang untuk menanam jalur `SDI` berisiko langsung **memutus jaringan akar serabut aktif** (*root pruning shock*) yang memicu stres dan rontok bunga/buah, sehingga merusak kevalidan uji pertumbuhan TA.
2. **Kompleksitas & Biaya Mitigasi `SDI` di Tanah Merah Urugan Eks-Empang:**  
   *Lamm & Camp (2007)* (*Microirrigation for Crop Production*, Vol. 13, hlm. 473–551) menegaskan bahwa keberhasilan `SDI` pada tanaman keras menuntut proteksi berlapis: pipa *subsurface* khusus berpenghalang akar (*root-barrier* berlapis *copper-oxide* atau injeksi *trifluralin*), katup pelepas vakum/udara (*air-vacuum relief valve*) agar tanah merah liat tidak tersedot balik ke lubang tetes saat pompa mati (*soil suction clogging*), serta pembilasan kimia/asam berkala. Paket mitigasi industri ini tidak ekonomis untuk skala purwarupa `4` pohon di atas tanah urugan eks-empang/sampah yang masih mengandung puing keras, sekaligus melanggar target `S-14` karena penyumbatan di bawah tanah **tidak tampak mata** dan memaksa petani membongkar tanah.
3. **Pencegahan Busuk Akar *Phytophthora* & Kebutuhan Dosis Adaptif pada Pohon Timpang:**  
   Mengacu pada *Dewdney (UF/IFAS `PP-156/CG009`)*, lapisan akar dangkal sitrus sangat rentan mengalami busuk akar dan leher batang (*Phytophthora foot rot, crown rot, and root rot*) apabila zona akar mengalami kejenuhan/genangan air berkepanjangan. Penyaluran `FDI` di permukaan tanah dengan teknik ***Pulse Drip*** bertahap (`5 L/putaran`) memberi jeda oksigenasi tanah merah urugan, sekaligus memudahkan penerapan **skala dosis adaptif Fuzzy** antara pohon kerdil `P1` (`46 cm`, `~5–10 L`) dan pohon besar `P3` (`250 cm`, `10–15 L`) secara terpantau.
4. **Strategi Mengejar Keunggulan `SDI` Secara Murah di Sistem `FDI`:**  
   Kelemahan utama `FDI` dibanding `SDI` hanyalah kehilangan penguapan di permukaan tanah saat siang terik (`32–36 °C` Subang). Kelemahan ini jauh lebih murah dan aman diatasi di sistem `FDI` dengan **menjadwalkan pemeriksaan `RTC` pada pagi/sore hari** (menghindari puncak radiasi siang), menerapkan ***Pulse Drip*** agar air langsung terserap ke zona akar `0–25 cm` tanpa menggenang, serta menjaga daun 100% kering. Oleh karena itu, **`SDI` direkomendasikan hanya apabila mitra kelak membuka petak tanam baru dari nol** (jalur tetes dipasang sebelum bibit ditanam).

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
10. **[Pustaka `CD-1` di Repo]** Smajstrla, A. G. *Microirrigation Design & Uniformity (`UF/IFAS AE094`)* — [17_UF_IFAS_AE094_Smajstrla.html](../sumber/referensi%20jurnal/pustaka_cd1/17_UF_IFAS_AE094_Smajstrla.html).
11. **[Eksternal Terverifikasi]** Lamm, F. R., & Camp, C. R. (2007). *Subsurface drip irrigation*. Dalam F. R. Lamm, J. E. Ayars, & F. S. Nakayama (Eds.), *Microirrigation for Crop Production — Design, Operation, and Management* (*Developments in Agricultural Engineering*, Vol. 13, hlm. 473–551). Elsevier. ISBN `978-0-444-50607-8`.
12. **[Eksternal Terverifikasi]** Morgan, K. T., Kadyampakeni, D. M., & Zekri, M. *Irrigation Management of Citrus Trees & Citrus Fibrous Root Distribution* (*Florida Citrus Production Guide*, UF/IFAS Extension EDIS, University of Florida).
13. **[Pustaka `CD-1` *Full-Text* di Repo]** Dewdney, M. M. *Florida Citrus Production Guide: Phytophthora Foot Rot, Crown Rot, and Root Rot* (`UF/IFAS PP-156/CG009`) — [26_UF_IFAS_PP31_SL127_Graham_Timmer.html](../sumber/referensi%20jurnal/pustaka_cd1/26_UF_IFAS_PP31_SL127_Graham_Timmer.html).
14. **[Referensi Baru Terverifikasi — Tanah Merah]** Duarte, R. N., Araújo Silva, E. M., Bonfim-Silva, E. M., & Koetz, M. (2021). *Using Arduino sensors to monitor vacuum gauge and soil water moisture*. DYNA, 88(219):190–196, DOI: `10.15446/dyna.v88n219.94121`.
15. **[Referensi Baru Terverifikasi — *C. amblycarpa*]** Budiarto, R., Poerwanto, R., Santosa, E., & Efendi, D. (2017). *The Potentials of Limau (Citrus amblycarpa Hassk. Ochse) as A Functional Food and Ornamental Mini Tree*. Journal of Tropical Crop Science, 4(2):49–57, DOI: `10.29244/jtcs.4.2.49-57`; serta **Buih & Susandarini (2023)** (*Al-Kauniyah*, DOI: `10.15408/kauniyah.v16i2.22920`) dan **Kepmentan RI No. `150/Kpts/SR.120/D.2.7/10/2015`**.
16. **[Standar Kelistrikan Kebun]** **IEC 60364-7-705:2006** (*Agricultural and horticultural premises — RCD <= 300 mA & SELV*), **PUIL 2011 (`SNI 0225:2011`)**, dan **IEC 60529 (`IP65`)**. *(Daftar lengkap `> 20` pustaka terverifikasi Crossref/OpenAlex/NCBI dikumpulkan di [Kumpulan_Referensi_Terverifikasi_CD3_Kebun_Kecil-garnie.md](../sumber/referensi%20jurnal/draf/referensi_garnie_cd3/Kumpulan_Referensi_Terverifikasi_CD3_Kebun_Kecil-garnie.md)).*

---

## 7. Daftar Pendalaman & Tindak Lanjut Berurutan (`Pasca-Audit 28 Nov 2026`)

- [x] **Finalisasi Alternatif ke-3, Skor 3 Alternatif, & Agronomi *C. amblycarpa*:** `Alt. 1 (FDI: 4,65)`, `Alt. 2 (SDI: 4,15)`, dan `Alt. 3 (Under-Canopy Micro-Jet: 3,70)`, dasar `FDI vs SDI` (`Subbab 5.5`), model kalibrasi non-linear (`Duarte 2021`), serta dosis adaptif `P1` (`3–4 L`) hingga `P3/P4` (`12–15 L`).
- [x] **Paket *Hardware* Lengkap (Hitam-Putih + `.kicad_sch` + `.drawio`):** [skematik_wiring_panel_ip65.png](skematik_wiring_panel_ip65.png), [layout_panel_ip65_dan_pcb.png](layout_panel_ip65_dan_pcb.png), [skema_pipa_zona_4_pohon_teknis.png](skema_pipa_zona_4_pohon_teknis.png) (Sumur Bor 2 Jalur), [panel_irigasi_kebun_kecil.kicad_sch](editable_cad/panel_irigasi_kebun_kecil.kicad_sch), dan RAB teraudit (`Paket A Rp2,84–4,24 jt`, `Paket B Rp3,50–4,98 jt`).
- [x] **Paket *Software* Lengkap (Hitam-Putih + `.drawio`):** [DFD Level 0](dfd_level0_sistem_kebun_kecil.png) & [DFD Level 1](dfd_level1_sistem_kebun_kecil.png) (perbaikan alur `5.0/D3 → 3.0 → 1.0/2.0`), [ERD 6 Tabel 3NF](erd_database_kebun_kecil.png), [Wireframe UI Web & HP](wireframe_ui_dashboard_kebun_kecil.png), beserta spesifikasi field DB lengkap di [SPESIFIKASI_SOFTWARE_DFD_ERD_UI_CD3.md](SPESIFIKASI_SOFTWARE_DFD_ERD_UI_CD3.md).
- [ ] **Simulasi Komparatif 3 Alternatif (`Kunci Level-4 CLO3`):** Jalankan simulasi numerik *head-to-head* (`FDI` vs `SDI` vs `Micro-Jet`) memakai dosis adaptif terbaru & kalibrasi non-linear untuk membuktikan skor matriks `4,65` vs `4,15` vs `3,70`.
- [ ] **Perakitan `CD-3` Final, Verifikasi Sumur Bor, & Tanda Tangan Basah PBB 1:** Susun ulang naskah `CD-3` sesuai alur dosen (*Arsitektur Global → 3 Subsistem Anggota*), isi nama Pembimbing 2 (**Fussy Mentari Dirgantara, S.T., M.T.**), masukkan `> 20` pustaka + lampiran logbook bimbingan, ukur kedalaman sumur bor di lapangan, dan urus tanda tangan basah PBB 1 sebelum tenggat `10 Des 2026`.
