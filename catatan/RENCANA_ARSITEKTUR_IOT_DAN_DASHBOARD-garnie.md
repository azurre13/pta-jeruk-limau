# Rencana Arsitektur IoT, Sistem Basis Data, dan Web Dashboard (`CD-3 Kebun Kecil`)

**Disusun oleh:** Muhammad Al Qarnie (`Anggota 3` — Software, Jaringan IoT, Basis Data, & Dashboard UI)  
**Tanggal:** 28 November 2026  
**Lokasi Penyimpanan Berkas:** `CD (Capstone Design)/catatan/RENCANA_ARSITEKTUR_IOT_DAN_DASHBOARD-garnie.md` *(memakai akhiran `-garnie` agar tidak menimpa atau menghambat berkas kerja rekan tim pada `CD-3`)*  
**Status:** Dokumen acuan teknis subsistem perangkat lunak & IoT menuju penyusunan **ERD + Spesifikasi Field Database (`Prioritas #2a`)**, **Wireframe UI Dashboard (`Prioritas #2b`)**, dan **Subbab `1.3.4` naskah final `CD-3`**.

**Dokumen Internal Terkait:**
- Sumber Kebenaran Solusi & Matriks: [`README_ALTERNATIF_SOLUSI_DAN_SCORING_CD3.md`](README_ALTERNATIF_SOLUSI_DAN_SCORING_CD3.md)
- Netlist Pinout ESP32 & Sumur Bor: [`SPESIFIKASI_WIRING_PINOUT_DAN_SUMUR_BOR.md`](SPESIFIKASI_WIRING_PINOUT_DAN_SUMUR_BOR.md)
- DFD Sistem (Non-OOP): [`dfd_level0_kebun_kecil-garnie.svg`](dfd_level0_kebun_kecil-garnie.svg) · [`dfd_level1_kebun_kecil-garnie.svg`](dfd_level1_kebun_kecil-garnie.svg)
- Diagram Blok & Flowchart: [`diagram_blok_sistem_kebun_kecil.svg`](diagram_blok_sistem_kebun_kecil.svg) · [`flowchart_sistem_kebun_kecil.svg`](flowchart_sistem_kebun_kecil.svg)
- Pembagian Peran Tim: [`Pembagian_Jobdesk_Tim_CD3_Kebun_Kecil.pdf`](Pembagian_Jobdesk_Tim_CD3_Kebun_Kecil.pdf)
- Pustaka Terverifikasi: [`Kumpulan_Referensi_Terverifikasi_CD3_Kebun_Kecil-garnie.md`](../sumber/referensi%20jurnal/draf/referensi_garnie_cd3/Kumpulan_Referensi_Terverifikasi_CD3_Kebun_Kecil-garnie.md)

---

## 1. Keputusan Arsitektur Utama & Justifikasi Teknis

Tim menetapkan **Alternatif 1 (*Precision Surface Drip / FDI*)** pada `Zona Uji 1` (`4` pohon sampel `P1–P4` + `4` pohon kontrol pembanding `K1–K4`). Untuk subsistem IoT dan antarmuka pengguna, arsitektur dikunci sebagai:

> **Web Dashboard Responsif (*Mobile-First* / PWA) berbasis Komunikasi MQTT (`ESP32 Wi-Fi → Router 4G`) + *Edge Buffering* `microSD` (*Store-and-Forward*) + Basis Data Terpusat.**

### 1.1 Pemetaan ke Arsitektur 4 Lapis IoT Pertanian (`García et al., 2020`, `R-05`)

| Lapisan | Komponen & Protokol Sistem | Peran Teknis di `Kebun Kecil` |
|---|---|---|
| **1. *Perception & Actuation Layer*** | `ESP32 DevKit V1 (38-Pin)`, `4× Capacitive Soil v1.2` (`ADS1115 0x48` + *pull-down* `1 MΩ`), `4× DS18B20` (`GPIO 4`), `YF-B1` (`GPIO 27`), sensor tekanan `0–5 bar` (`GPIO 36`), `RTC DS3231` (`0x68`), `MicroSD` (`SPI GPIO 5, 18, 19, 23`), tombol `S-13/STOP` (`GPIO 16`), `SSR-25DA` pompa AC (`GPIO 26`), `5× Relay SELV 12V` katup `V1–V4/VF` (`GPIO 13, 14, 25, 32, 33`), `LED_RUN/LED_ALM` (`GPIO 17, 2`). | Mengakuisisi data tanah/air dengan kalibrasi lokal, menghitung dosis `Fuzzy + Pulse Drip`, menjalankan katup sekuensial, menegakkan proteksi *dry-run* & mampet cabang secara **otonom di sisi *edge*** tanpa bergantung pada sinyal internet. |
| **2. *Network & Edge Buffer Layer*** | `Wi-Fi 2,4 GHz` lokal dari `ESP32` menuju `Router / MiFi 4G` di dalam panel `IP65`, protokol **MQTT (`QoS 1`)**, dan penyimpanan cadangan **`D1: MicroSD Buffer`**. | Menjembatani jarak pemantauan Subang ↔ Bandung; menampung antrean log ber-timestamp `RTC DS3231` ketika koneksi seluler 4G terganggu (*store-and-forward*). |
| **3. *Middleware & Persistence Layer*** | **MQTT Broker**, layanan *backend ingestion worker* (*MQTT subscriber* & *REST/WebSocket API*), serta **Basis Data Terpusat** (`D2: Operasional`, `D3: Konfigurasi`, `D4: Pertumbuhan`). | Memvalidasi payload, mencegah duplikasi data *backfill*, menyimpan histori telemetri, kejadian siram, alarm gangguan, konfigurasi Fuzzy/kalibrasi, serta data pertumbuhan uji banding. |
| **4. *Application Layer*** | **Web Dashboard Responsif (*Mobile-First*)** dengan pemisahan tampilan untuk **`E3. Mitra & Pekerja`** (HP) dan **`E4. Tim Pengamat` / Penguji** (Laptop/Desktop). | Memungkinkan pemantauan *real-time*, kontrol siram/STOP darurat, notifikasi alarm, *remote tuning* parameter Fuzzy & kalibrasi, serta analisis grafik perbandingan `P1–P4` vs pohon kontrol. |

### 1.2 Matriks Justifikasi Pemilihan vs Alternatif Platform IoT Lain

| Opsi Platform IoT / UI | Kelebihan Singkat | Alasan Tidak Dipilih sebagai Arsitektur Utama | Referensi Pembanding |
|---|---|---|---|
| **Terpilih: Web Dashboard Responsif (*Mobile-First*) + MQTT + DB Sendiri** | • Satu aplikasi melayani HP mitra (`E3`) dan laptop pengamat/penguji (`E4`).<br>• Kontrol penuh atas skema DB `5+` tabel (`sensor_logs`, `irrigation_events`, `fault_alerts`, `growth_records`, `system_config`, `trees`).<br>• Mendukung *backfill* timestamp asli `RTC DS3231` dari `microSD`.<br>• Menembus CGNAT 4G via koneksi *outbound* MQTT & memenuhi bobot kedalaman CE (`K5 = 15%`). | Membutuhkan perancangan skema API, topik MQTT, dan ERD secara mandiri oleh Anggota 3 *(tetap sangat layak diselesaikan dalam jadwal TA `<= 6 bulan`)*. | `García et al. (2020)` (`R-05`), `Bajenaru et al. (2025)` (`N-02`), `Borankulova et al. (2025)` (`N-04`), `Sharma et al. (2026)` (`N-03`), `Ghanghas et al. (2026)` (`N-05`). |
| *Cloud No-Code/Widget* (mis. Blynk, Arduino Cloud / ThingsBoard tier gratis) | Cepat dibuat untuk prototipe tombol & grafik dasar. | • Paket gratis membatasi jumlah *widget/pin* dan masa retensi histori *(padahal uji TA berjalan berbulan-bulan)*.<br>• Tidak fleksibel untuk input tabel agronomi pohon kontrol (`E4`), *backfill* timestamp `RTC` dari `microSD`, dan analisis komparasi `P1–P4`.<br>• Terlalu dangkal dari sisi rekayasa perangkat lunak S1 Teknik Komputer. | `Pereira, Chaari, & Daroge (2023)` (`N-01`, memakai Blynk + Wi-Fi tanpa 4G/MicroSD/DB uji tumbuh). |
| Aplikasi *Mobile Native* (Android APK / Flutter terpisah) | Akses fitur native ponsel dan ikon aplikasi langsung. | Menggandakan pekerjaan jika tetap butuh panel web laptop untuk `E4. Tim Pengamat` & penguji, menyulitkan pengguna iOS, serta mengharuskan instal ulang APK tiap pembaruan UI. | — |
| *Web Server* Lokal di ESP32 (hanya Wi-Fi AP/LAN kebun) | Tanpa server eksternal. | **Gagal memenuhi syarat pemantauan & *remote parameter tuning* jarak jauh (Bojongsoang ↔ Subang)** karena jaringan seluler 4G berada di balik CGNAT dan tidak memiliki IP publik statis. | — |
| Bot *Chat* (Telegram / WhatsApp) Saja | Ringan untuk notifikasi alarm teks. | Tidak memadai untuk grafik tren `4` pohon serentak, rekap debit air harian, form *remote tuning* Fuzzy & kalibrasi, serta tabel pertumbuhan pohon kontrol. *(Dapat dijadikan kanal notifikasi tambahan dari backend jika diperlukan.)* | — |

---

## 2. Alur Kerja Sistem & Sinkronisasi DFD ↔ FSM ESP32

Arsitektur perangkat lunak ini terikat langsung pada **5 Proses** dan **4 Data Store** di [`dfd_level1_kebun_kecil-garnie.svg`](dfd_level1_kebun_kecil-garnie.svg) serta **State FSM `S0–S9`** pada rancangan *firmware* ESP32:

1. **Akuisisi & Kalibrasi Sensor (`Proses 1.0` ↔ `State S2: READ_CALIB`):**
   - Pada jadwal `RTC DS3231` (atau pemicu manual), ESP32 membaca `4` sensor lengas via `ADS1115` (`N = 10` *moving average*, `Dafonte et al., 2024` `R-01`) dan `4` sensor `DS18B20`.
   - Nilai `ADC` mentah dikonversi ke `% VWC` menggunakan parameter kalibrasi tanah merah Ciberes yang disimpan di memori lokal ESP32 dan dapat diperbarui lewat **`D3: DB Konfigurasi`** (`m, c` atau model hiperbolik $y = 1/(a+bx)$, `Duarte et al., 2021` `A-13`, `Kumar et al., 2025` `A-12`, `Zakaria et al., 2026` `R-03`).
2. **Kendali Fuzzy, *Pulse Drip*, & Proteksi Mampet (`Proses 2.0` ↔ `State S3–S8`):**
   - Keputusan menyiram didasarkan murni pada **`VWC < Ambang`** (tanpa sensor hujan).
   - Fuzzy menghitung target volume `V_target(i)` (mengakomodasi dosis aman pohon kerdil `P1` `46 cm` dibanding `P2–P4`).
   - Eksekusi sekuensial `V1 → V4` (`1,5–2,0 L/mnt`, kuota per putaran `5 L`, jeda serap `15 menit` hanya jika antrean tersisa `1` pohon) + `Auto End-Flush` melalui `VF` (`30–45 dtk`, $v \ge 0{,}6\text{ m/s}$, `Lavanholi et al., 2018` `R-09`).
   - **Keselamatan *Edge-First* (Otonom di ESP32):** Pengawasan `Flow = 0 > 10 dtk` / `P < P_min` (*dry-run* → hentikan siklus) serta `P > P_max` (*branch clog* → tutup katup `Vi`, catat *fault*, lanjutkan antrean pohon `i+1`, `Meriç 2025` `R-04`) dan interupsi tombol **`S-13/STOP`** dieksekusi langsung di ESP32 **tanpa menunggu balasan server/cloud**.
3. **Mekanisme *Store-and-Forward* `MicroSD` & MQTT (`Proses 3.0` ↔ `State S9: LOG_SYNC`):**
   - Setiap rekaman sensor, kejadian irigasi, dan alarm **selalu ditulis lebih dulu ke `D1: MicroSD Buffer`** sebagai baris antrean offline (`pending_sync.csv` / `.jsonl`) disertai `seq_id` unik dan `rtc_timestamp` dari `RTC DS3231`.
   - Jika koneksi `Wi-Fi → Router 4G → MQTT Broker` tersambung, ESP32 mempublikasikan pesan tertunda secara bertahap (*FIFO batching* agar tidak membanjiri RAM ESP32) dan menandai `sync_flag = 1` setelah menerima *PUBACK* (`QoS 1`).
   - Jika terputus, FSM tetap kembali ke `S1: IDLE` / menjalankan jadwal berikutnya sambil terus mengakumulasi log di `microSD` (*non-blocking reconnect*).
4. **Backend *Ingestion* & Basis Data Terpusat (`D2`, `D3`, `D4`):**
   - *Backend worker* berlangganan (*subscribe*) ke topik MQTT, melakukan validasi skema JSON, melakukan **deduplikasi idempoten** berbasis `(device_id, seq_id, ts)` bila ada paket kirim ulang, lalu menyisipkan ke tabel **`D2: DB Operasional`**.
   - Saat **`E4. Tim Pengamat`** menginput data pertumbuhan tinggi/buah atau koefisien kalibrasi baru via Web Dashboard, backend menyimpannya ke **`D4: DB Pertumbuhan`** atau **`D3: DB Konfigurasi`**. Pembaruan konfigurasi di `D3` dipublikasikan ke topik konfigurasi MQTT (`retained = true`) agar ESP32 langsung menerapkannya.
5. **Penyajian Dashboard & Kontrol Jarak Jauh (`Proses 5.0` ↔ `E3` & `E4`):**
   - Dashboard membaca histori dan status terbaru dari `D2`, `D3`, dan `D4` lewat REST API, serta menerima pembaruan *real-time* (status pompa, katup aktif, pembacaan terakhir, atau alarm darurat) melalui WebSocket / MQTT *bridge*.

---

## 3. Desain Kontrak Komunikasi MQTT

Seluruh komunikasi memakai prefiks topik terstruktur untuk memudahkan ekspansi jika kelak `Kebun Kecil` bertambah dari `Zona 1` (`z1`) ke `Zona 2..N` (`72–73` pohon).

| Topik MQTT | Arah | QoS / Retain | Isi *Payload* JSON Ringkas | Tujuan Store / Aksi |
|---|---|---|---|---|
| `limau/z1/telemetry/sensors` | `ESP32 → Broker` | `QoS 1`, `retain=false` | `{"seq":1042,"ts":"2026-12-15T06:00:05+07:00","backfill":false,"readings":[{"tree":"P1","adc":2310,"vwc":24.8,"temp_c":26.4}, ...]}` | `D2` (`sensor_logs`) |
| `limau/z1/telemetry/irrigation` | `ESP32 → Broker` | `QoS 1`, `retain=false` | `{"seq":1043,"tree":"P3","mode":"AUTO_FUZZY","start_ts":"...","end_ts":"...","target_l":12.0,"actual_l":11.8,"pulses":3,"status":"DONE"}` | `D2` (`irrigation_events`) |
| `limau/z1/alerts/fault` | `ESP32 → Broker` | `QoS 1`, `retain=false` | `{"seq":1044,"ts":"...","code":"BRANCH_CLOG","branch":"V2","flow_lpm":0.18,"pressure_bar":2.45,"action":"SKIP_CONTINUE"}` | `D2` (`fault_alerts`) + Notifikasi Web |
| `limau/z1/status/heartbeat` | `ESP32 → Broker` | `QoS 1`, `retain=true` *(+ LWT `offline`)* | `{"ts":"...","online":true,"fsm":"S1_IDLE","pump":false,"valve":"NONE","rssi_wifi":-58,"sd_pending":0}` | Status *online/offline* panel di Header UI |
| `limau/z1/cmd/control` | `Backend → ESP32` | `QoS 1`, `retain=false` | `{"cmd_id":"c-99","action":"MANUAL_WATER" \| "RUN_FLUSH" \| "EMERGENCY_STOP","tree":"P2","limit_l":5.0}` | Trigger `Proses 2.0` (`S4` / `S8`) |
| `limau/z1/cmd/config` | `Backend → ESP32` | `QoS 1`, `retain=true` | `{"ver":4,"vwc_min":22.0,"vwc_max":35.0,"pulse_max_l":5.0,"flush_sec":40,"p_min_bar":0.6,"p_max_bar":2.2,"calib":{"P1":{"a":...,"b":...},"k_tajuk":...}}` | Sinkron `D3` → memori NVS/EEPROM ESP32 |

> **Peran *Last Will and Testament (LWT)*:** Broker MQTT disetel agar otomatis menerbitkan `{"online":false}` pada topik `heartbeat` apabila `ESP32` putus koneksi mendadak melewati batas *keep-alive*, sehingga mitra dan tim langsung mengetahui di dashboard apabila listrik kebun padam atau modem 4G mati *(dan log kebun sedang dialihkan ke `microSD`)*.

---

## 4. Rancangan Tampilan & Modul Web Dashboard (`Prioritas #2b`)

Antarmuka dibagi berdasarkan peran pengguna pada DFD (`E3` vs `E4`) dalam satu aplikasi web responsif:

### A. Tampilan Mitra & Pekerja (`E3` — Fokus *Mobile-First* di HP)
1. **Bar Status Panel & Koneksi (`Top Bar`):** Indikator *Online / Offline (LWT)*, status daya/siram saat ini (`Siaga`, `Menyiram P3`, `Auto End-Flush`, atau `ALARM`), serta jumlah log tertahan di `microSD`.
2. **Kartu Ringkas 4 Pohon Sampel (`P1–P4`):** Menampilkan nama/tinggi pohon, nilai `% VWC` dengan label warna/status teks (*Kering / Optimal / Lembap*), suhu tanah (`°C`), total air hari ini (`L`), dan status katup (`Buka/Tutup`).
3. **Panel Kontrol & Keamanan Cepat:**
   - Tombol darurat **`STOP SEMUA (DARURAT)`** yang mudah dijangkau satu ketukan dan sinkron dengan tombol fisik `S-13`.
   - Tombol aksi manual: *Siram Manual per Pohon (`V1–V4`)* dengan batas volume aman, serta *Jalankan Bilas Pipa (`VF`)*.
4. **Pusat Notifikasi Gangguan (`Fault Banner`):** Pesan berbahasa sederhana untuk pekerja kebun, membedakan **Gangguan Sumber Air (`Dry-Run`: cek sumur/filter)** vs **Gangguan Cabang Spesifik (`Cabang Pi dilewati`: cek penetes/katup `Vi`)** lengkap dengan tombol tandai *"Sudah Diperiksa"*.

### B. Tampilan Tim Pengamat & Penguji (`E4` — Fokus *Analytical Desktop/Tablet*)
1. **Grafik Seri Waktu (*Time-Series*):** Grafik tren `% VWC` & suhu tanah `P1–P4` (rentang 24 jam, 7 hari, 30 hari, 6 bulan) yang dapat di-*overlay* dengan momen penyiraman (`irrigation_events`).
2. **Halaman Uji Banding Pertumbuhan (`P1–P4` vs Kontrol `K1–K4`):** Form input berkala untuk Anggota 1 / Pengamat (tanggal ukur, pohon `P1–P4` atau `K1–K4`, tinggi `cm`, lingkar/tajuk, jumlah/status buah, catatan) + grafik perbandingan laju tumbuh untuk pembuktian TA.
3. **Halaman *Remote Tuning* & Kalibrasi (`D3: system_config`):** Form ubah ambang `VWC`, batas kuota *pulse*, durasi *Auto End-Flush*, batas tekanan `[P_min, P_max]`, `k_tajuk`, dan koefisien kalibrasi tanah merah per sensor, disertai riwayat versi konfigurasi.
4. **Ekspor Data & Laporan Uji:** Unduh dataset mentah/bersih ke format `.csv` untuk analisis `Python` dan pelaporan evaluasi ke pembimbing.

---

## 5. Jembatan ke Desain Basis Data (`Prioritas #2a: ERD`)

Menyelaraskan `Tabel 1.14` di draf `CD-3` dengan DFD Level 1 (`D2`, `D3`, `D4`) serta kebutuhan uji banding `4` pohon sampel + `4` pohon kontrol, struktur tabel logis di basis data terpusat ditingkatkan menjadi **6 tabel terhubung (3NF)**:

1. **`trees` (Master Pohon — pengikat relasi `1:N`):** Menyimpan identitas `P1–P4` (*grup `SAMPLE`*, memiliki katup `V1–V4` & sensor `S1–S4`) dan `K1–K4` (*grup `CONTROL`*, penyiraman manual pembanding), tinggi awal, dan faktor skala tajuk `k_tajuk`.
2. **`sensor_logs` (`D2`):** Rekaman waktu asli `RTC` (`logged_at`), `seq_id`, `raw_adc`, `vwc_pct`, `temp_c`, `pressure_bar`, serta `synced_from_sd` / `received_at`.
3. **`irrigation_events` (`D2`):** Rekaman siklus `start_ts`, `end_ts`, `mode` (`AUTO_FUZZY`, `MANUAL_WEB`, `MANUAL_S13`, `END_FLUSH`), `target_l`, `actual_l`, `pulses`, dan `status`.
4. **`fault_alerts` (`D2`):** Rekaman anomali `fault_code` (`DRY_RUN`, `BRANCH_CLOG`, `FILTER_DELTA_P`, `EMERGENCY_STOP`), `branch_code`, `flow_lpm`, `pressure_bar`, `resolved`, `resolved_at`, dan catatan tindakan.
5. **`growth_records` (`D4`):** Rekaman pertumbuhan berkala oleh `E4` untuk **baik `P1–P4` maupun `K1–K4`** (`measured_date`, `height_cm`, `fruit_status`, `fruit_count`, `notes`, `observer_name`).
6. **`system_config` (`D3`):** Menyimpan parameter global Fuzzy, kuota *pulse*, durasi bilas, batas `[P_min, P_max]`, serta konfigurasi/koefisien kalibrasi sensor per pohon (`config_version`, `updated_by`, `updated_at`).

---

## 6. Parameter Terbuka yang Wajib Diuji di Kebun (Bulan 1–2)

Dokumen arsitektur ini sudah siap menjadi blueprint implementasi, sementara angka operasional aktual berikut akan diisikan saat pengujian lapangan Bulan 1–2 (tanpa perlu mengubah struktur DFD, ERD, maupun UI):

1. Uji kuat sinyal seluler **`RSSI / RSRP / SINR`** berbagai operator 4G tepat di posisi panel IP65 `Kebun Kecil` dan pengukuran total *bandwidth* payload JSON harian.
2. Uji ketahanan sinkronisasi *store-and-forward* **`microSD`** (simulasi putus sinyal 24–72 jam lalu *backfill* otomatis ke database tanpa kehilangan atau duplikasi baris).
3. Penentuan koefisien kalibrasi aktual **`Capacitive v1.2`** pada tanah merah urugan Ciberes (uji gravimetrik Anggota 1) dan batas tekanan **`[P_min, P_max]`** aktual saat *commissioning* pompa + *bypass*.

---

## 7. Daftar Referensi Terverifikasi Pendukung Arsitektur IoT

1. **García, L. et al. (2020).** *Sensors*, `PMC7070544`, DOI: `10.3390/s20041042` (`R-05` / `Z-05` — tinjauan arsitektur 4 lapis IoT irigasi & evaluasi sensor aliran).
2. **Pereira, G. P., Chaari, M. Z., & Daroge, F. (2023).** *IoT-Enabled Smart Drip Irrigation System Using ESP32*. MDPI *IoT*, 4(3):221–243. DOI: `10.3390/iot4030012` (`N-01`).
3. **Bajenaru, V.-D., Istriteanu, S.-E., & Stanciu, D.-I. (2025).** *IoT Monitoring System for Soil Aridification Stage Validated Through Data Analysis and Correlation*. *AgriEngineering*, 7(11):358. DOI: `10.3390/agriengineering7110358` (`N-02`).
4. **Sharma, S., Mishra, D., Yadav, A., Gami, B., & Madhan, E. S. (2026).** *A Low-Cost Intelligent Water Quality Monitoring System with On-Device Machine Learning and Cloud Integration*. *Scientific Reports* (`PMC13043767`). DOI: `10.1038/s41598-026-37287-3` (`N-03` — pencatatan lokal `microSD` SPI & integrasi *cloud*).
5. **Borankulova, G., Altybayev, G., Tungatarova, A., Yeraliyeva, B., Dulatbayeva, S., Murzakhmetov, A., & Bekbolatov, S. (2025).** *Development of Real-Time Water-Level Monitoring System for Agriculture*. *Sensors*, 25(17):5564. DOI: `10.3390/s25175564` (`N-04` — arsitektur Wi-Fi + Router 4G + SD card).
6. **Ghanghas, S., Sihag, N., & Dhanger, P. (2026).** *Smart water management in agriculture: convergence of sensors, imaging, AI, precision irrigation, and robotics systems*. *Frontiers in Water*, 8:1973897. DOI: `10.3389/frwa.2026.1973897` (`N-05` — kendali katup MQTT).
7. **Dafonte, J. et al. (2024).** *Sensors*, `PMC11679594`. DOI: `10.3390/s24248104` (`R-01` / `Z-01` — rata-rata `10×` ADC & *drift* jam ESP32).
8. **Domínguez-Niño, J. M. et al. (2019).** *Sensors*, `PMC6679572`. DOI: `10.3390/s19143101` (`R-02` / `Z-02` — kalibrasi lokal vs kurva pabrik).
9. **Zakaria, Y. S. et al. (2026).** *Sensors*, `PMC13364378`. DOI: `10.3390/s26133979` (`R-03` / `Z-11` — *pull-down* `1 MΩ`, LDO `3,3 V`, & kalibrasi lokal).
10. **Meriç, M. K. (2025).** *Scientific Reports*, `PMC12019383`. DOI: `10.1038/s41598-025-97303-w` (`R-04` / `Z-04` — pemantauan meter pulsa air & sensor tekanan).
11. **Duarte, T. F., Araújo da Silva, T. J., Bonfim-Silva, E. M., & Koetz, M. (2021).** *Using Arduino sensors to monitor vacuum gauge and soil water moisture*. *DYNA*, 88(219):190–196. DOI: `10.15446/dyna.v88n219.94121` (`A-13` — kalibrasi `Capacitive v1.2` tanah liat merah *Red Oxisol* model hiperbolik $y = 1/(a+bx)$).
12. **Kumar, M., Sarangi, A., Singh, M., & Khanna, M. (2025).** *Assessing capacitance soil moisture sensors for precision irrigation scheduling...* *CABI Agriculture and Bioscience*. DOI: `10.1079/ab.2025.0025` (`A-12` — kalibrasi non-linear sensor kapasitif).
