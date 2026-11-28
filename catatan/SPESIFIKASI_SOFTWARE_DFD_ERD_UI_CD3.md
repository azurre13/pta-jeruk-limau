# Spesifikasi Perancangan *Software*, Basis Data (`3NF`), & Antarmuka UI (`CD-3 Kebun Kecil`)

**Tanggal Penyusunan:** 28 November 2026  
**Pendekatan Pemodelan:** **Terstruktur / Non-OOP** (`DFD Level 0 & Level 1`, Desain Tabel & `ERD`, *Flowchart*, `FSM 10-State`, dan *Wireframe* Hitam-Putih Low-Fidelity) — mematuhi arahan dosen pengampu *Capstone Design 3* agar tidak mencampuradukkan notasi *Object-Oriented* (UML) pada *firmware* prosedural `ESP32`.

**Berkas Diagram & Sumber Siap Edit (`Draw.io`):**
- **DFD Level 0 (Context Diagram):** [dfd_level0_sistem_kebun_kecil.png](dfd_level0_sistem_kebun_kecil.png) ([SVG](dfd_level0_sistem_kebun_kecil.svg))
- **DFD Level 1 (Balanced & Teraudit):** [dfd_level1_sistem_kebun_kecil.png](dfd_level1_sistem_kebun_kecil.png) ([SVG](dfd_level1_sistem_kebun_kecil.svg))
- **File Edit Draw.io (`DFD Level 0 & 1`, 2 Tab):** [5_dfd_level0_dan_level1_kebun_kecil.drawio](editable_drawio/5_dfd_level0_dan_level1_kebun_kecil.drawio)
- **ERD Basis Data (`Crow's Foot 3NF`, `7` Tabel):** [erd_database_kebun_kecil.png](erd_database_kebun_kecil.png) ([SVG](erd_database_kebun_kecil.svg)) · [File Edit Draw.io](editable_drawio/6_erd_database_kebun_kecil.drawio)
- **Sketsa *Wireframe* UI Dashboard Web & HP:** [wireframe_ui_dashboard_kebun_kecil.png](wireframe_ui_dashboard_kebun_kecil.png) ([SVG](wireframe_ui_dashboard_kebun_kecil.svg)) · [File Edit Draw.io](editable_drawio/7_wireframe_ui_dashboard_kebun_kecil.drawio)

---

## 1. Penyelarasan & Audit *Balancing* DFD Level 0 ↔ Level 1

Seluruh `4` entitas eksternal dan `8` aliran data pada **DFD Level 0** dipertahankan utuh di **DFD Level 1**, dengan perbaikan krusial pada jalur kendali jarak jauh agar tidak ada perintah/konfigurasi *server* yang melompati jembatan MQTT:

| Entitas Eksternal | Aliran di Level 0 | Proses Terkait di Level 1 | Aliran Masuk/Keluar Seimbang di Level 1 |
|---|---|---|---|
| **E1. Sensor Lapangan & RTC** | `E1 → 0`: Data Lengas & Suhu Tanah<br>`E1 → 0`: Data Debit YF-B1, Tekanan, & RTC | `1.0 Akuisisi & Kalibrasi Non-Linear`<br>`2.0 Kendali Fuzzy, Pulse, & Proteksi` | `E1 → 1.0`: Data Lengas & Suhu<br>`E1 → 2.0`: Data Debit YF-B1, Tekanan, & RTC |
| **E2. Tombol S-13/STOP & Aktuator** | `E2 → 0`: Sinyal Tombol S-13 / STOP<br>`0 → E2`: Perintah Pompa AC (SSR), V1–V4, VF, LED | `2.0 Kendali Fuzzy, Pulse, & Proteksi` | `E2 → 2.0`: Tombol S-13/STOP<br>`2.0 → E2`: SSR Pompa, V1–V4, VF, LED |
| **E3. Mitra & Pekerja** | `E3 → 0`: Perintah Siram/STOP & Tuning<br>`0 → E3`: Status Kebun, Grafik, & Alarm | `5.0 Dashboard Web/HP & Konfigurasi` | `E3 → 5.0`: Perintah Siram/STOP & Tuning<br>`5.0 → E3`: Status Kebun, Grafik, & Alarm |
| **E4. Tim Pengamat & Kalibrasi** | `E4 → 0`: Data Kalibrasi & Tumbuh P1–P4<br>`0 → E4`: Rekap Uji Air, Lengas, & Evaluasi | `4.0 Olah Data Uji & Evaluasi P1–P4` | `E4 → 4.0`: Data Kalibrasi & Tumbuh P1–P4<br>`4.0 → E4`: Rekap Uji Air & Evaluasi |

**Perbaikan Logika Jalur `5.0 / D3 → 3.0 → 1.0 / 2.0` (Hasil Review Tim):**
- Setiap perintah manual/STOP dan perubahan parameter *remote tuning* dari **`5.0 Dashboard Web/HP`** dan **`D3: DB Konfigurasi`** **wajib melewati `3.0 Buffer MicroSD & Sinkronisasi Bridge MQTT`** sebelum diturunkan menjadi `Koef. a, b` ke `1.0` dan `Perintah STOP & Aturan Fuzzy` ke `2.0`.
- Dengan demikian, `D1` (*MicroSD*) menjadi antrean lokal murni di `ESP32`, sedangkan `D2` (*DB Operasional*), `D3` (*DB Konfigurasi*), dan `D4` (*DB Pertumbuhan*) berada di sisi *server* di balik gerbang `3.0 Bridge MQTT`.

---

## 2. Desain Spesifikasi Tabel & *Entity Relationship Diagram* (ERD)

Memenuhi syarat perancangan basis data perkuliahan *Capstone Design 3* (tabel spesifikasi atribut lengkap sebelum skema relasi ERD), berikut rancangan rinci **`7` tabel ternormalisasi (`3NF`)** yang telah diselaraskan dengan kebutuhan uji banding `4` pohon sampel + `4` pohon kontrol (`README`), kalibrasi individual per sensor (*Cabia et al., 2025*), akun pengguna *dashboard* (`E3` & `E4`), serta proteksi anti-duplikasi saat sinkronisasi ulang *buffer* `MicroSD`. Penggambaran ERD pada [erd_database_kebun_kecil.png](erd_database_kebun_kecil.png) dan [6_erd_database_kebun_kecil.drawio](editable_drawio/6_erd_database_kebun_kecil.drawio) mengikuti kaidah *Crow's Foot* **Coronel & Morris (*Database Systems: Design, Implementation, & Management*)** serta bentuk tabel ER resmi **`draw.io` (`shape=table`)**: **`1` atribut atomik per baris**, **`PK` digarisbawahi**, **`FK` dicetak miring**, dan seluruh relasi memakai **garis putus-putus (*non-identifying relationship*)** karena setiap tabel anak memiliki *surrogate PK* sendiri (`||` jika FK `NOT NULL`, `|o` jika FK `NULL`):

### 2.1 Tabel `trees` (Master Pohon Uji `P1–P4` & Kontrol `K1–K4`)
| Nama Field | Tipe Data | Panjang | Kunci | Null | Keterangan |
|---|---|---:|---|---|---|
| `tree_id` | `INT` | `11` | `PK` | `NOT NULL` | `AUTO_INCREMENT`, ID pohon (`1..4` sampel, `5..8` kontrol) |
| `tree_code` | `VARCHAR` | `10` | `UQ` | `NOT NULL` | Kode pohon (`'P1'..'P4'` sampel sistem, `'K1'..'K4'` kontrol manual) |
| `tree_group` | `ENUM` | `10` | — | `NOT NULL` | Kelompok uji banding TA (`'SAMPLE'`, `'CONTROL'`) |
| `initial_height_cm` | `DECIMAL` | `5,1` | — | `NOT NULL` | Tinggi awal survei (`46.0`, `100.0`, `250.0`, `210.0` cm utk sampel & ukur awal kontrol) |
| `dose_min_l` | `DECIMAL` | `4,2` | — | `NULL` | Batas bawah dosis adaptif (`3.00`/`8.00`/`12.00` L; `NULL` utk `'CONTROL'`) |
| `dose_max_l` | `DECIMAL` | `4,2` | — | `NULL` | Batas atas dosis adaptif (`4.00`/`10.00`/`15.00` L; `NULL` utk `'CONTROL'`) |
| `valve_gpio` | `TINYINT` | `3` | — | `NULL` | Pin GPIO Relay katup cabang (`13, 14, 25, 32`; `NULL` utk `'CONTROL'`) |
| `sensor_channel` | `TINYINT` | `2` | — | `NULL` | Kanal ADC `ADS1115` sensor lengas (`0..3` utk `A0..A3`; `NULL` utk `'CONTROL'`) |
| `calib_a` | `DECIMAL` | `10,6` | — | `NULL` | Konstanta `a` kalibrasi individual sensor ke-`i` pada $y=1/(a+bx)$ (`NULL` utk `'CONTROL'`) |
| `calib_b` | `DECIMAL` | `10,6` | — | `NULL` | Konstanta `b` kalibrasi individual sensor ke-`i` pada $y=1/(a+bx)$ (`NULL` utk `'CONTROL'`) |
| `status_health` | `ENUM` | `20` | — | `NOT NULL` | Kondisi awal tanaman (`'BAIK'`, `'KERDIL'`) |

### 2.2 Tabel `sensor_logs` (Telemetri Periodik Tiap `10 Menit`)
| Nama Field | Tipe Data | Panjang | Kunci | Null | Keterangan |
|---|---|---:|---|---|---|
| `log_id` | `BIGINT` | `20` | `PK` | `NOT NULL` | `AUTO_INCREMENT`, ID unik rekaman telemetri |
| `tree_id` | `INT` | `11` | `FK, UQ1` | `NOT NULL` | Relasi ke `trees.tree_id` *(bagian kunci komposit anti-duplikasi `UQ1`)* |
| `raw_adc` | `SMALLINT` | `6` | — | `NOT NULL` | Nilai mentah ADC 16-bit `ADS1115` (*moving average* `10×`) |
| `vwc_pct` | `DECIMAL` | `5,2` | — | `NOT NULL` | Kadar air tanah hasil kalibrasi non-linear sensor ke-`i` (`%`) |
| `soil_temp_c` | `DECIMAL` | `4,2` | — | `NOT NULL` | Suhu tanah kedalaman `15–20 cm` dari `DS18B20` (`°C`) |
| `flow_lpm` | `DECIMAL` | `5,2` | — | `NULL` | Debit manifold induk `YF-B1` sesaat saat sampel dibaca (`L/mnt`; `0`/`NULL` saat pompa *idle*) |
| `pressure_bar` | `DECIMAL` | `4,2` | — | `NULL` | Tekanan manifold hilir filter sesaat (`bar`; `0`/`NULL` saat pompa *idle*) |
| `is_offline_sync` | `BOOLEAN` | `1` | — | `NOT NULL` | Penanda `1` jika berasal dari unggah ulang *buffer* `MicroSD` |
| `recorded_at` | `DATETIME` | — | `UQ1` | `NOT NULL` | Stempel waktu akurat `RTC DS3231` (`UQ1(tree_id, recorded_at)` cegah duplikasi *backfill*) |

### 2.3 Tabel `irrigation_events` (Riwayat Siklus Penyiraman & Bilas)
| Nama Field | Tipe Data | Panjang | Kunci | Null | Keterangan |
|---|---|---:|---|---|---|
| `event_id` | `BIGINT` | `20` | `PK` | `NOT NULL` | `AUTO_INCREMENT`, ID unik peristiwa penyiraman |
| `tree_id` | `INT` | `11` | `FK, UQ1` | `NOT NULL` | Relasi ke `trees.tree_id` *(kelompok `'SAMPLE'` `P1–P4`)* |
| `config_id` | `INT` | `11` | `FK` | `NOT NULL` | Relasi ke `system_config.config_id` (versi parameter sistem yang berlaku saat siram) |
| `triggered_by` | `INT` | `11` | `FK` | `NULL` | Relasi ke `users.user_id` (`NULL` utk `AUTO_RTC`/`BTN_S13`; terisi bila `MQTT_APP`) |
| `trigger_mode` | `ENUM` | `15` | — | `NOT NULL` | Pemicu siklus (`'AUTO_RTC'`, `'BTN_S13'`, `'MQTT_APP'`) |
| `target_vol_l` | `DECIMAL` | `5,2` | — | `NOT NULL` | Volume target hasil inferensi Fuzzy / manual (`L`) |
| `delivered_vol_l` | `DECIMAL` | `5,2` | — | `NOT NULL` | Volume aktual terukur oleh `YF-B1` (`L`) |
| `pulse_count` | `TINYINT` | `3` | — | `NOT NULL` | Jumlah putaran *Pulse Drip* (`maks 5 L/putaran`) |
| `duration_s` | `INT` | `11` | — | `NOT NULL` | Total durasi katup aktif (detik) |
| `flush_executed` | `BOOLEAN` | `1` | — | `NOT NULL` | Status apakah *Auto End-Flush `VF`* dijalankan pasca-siklus (`0/1`) |
| `started_at` | `DATETIME` | — | `UQ1` | `NOT NULL` | Waktu `RTC` katup `Vi` mulai dibuka (`UQ1(tree_id, started_at)` anti-duplikasi) |
| `ended_at` | `DATETIME` | — | — | `NULL` | Waktu pompa dimatikan & katup `Vi` ditutup |

### 2.4 Tabel `fault_alerts` (Log Anomali Hidrolika & *Emergency STOP*)
| Nama Field | Tipe Data | Panjang | Kunci | Null | Keterangan |
|---|---|---:|---|---|---|
| `alert_id` | `BIGINT` | `20` | `PK` | `NOT NULL` | `AUTO_INCREMENT`, ID unik alarm gangguan |
| `tree_id` | `INT` | `11` | `FK` | `NULL` | Relasi ke `trees.tree_id` (`NULL` utk gangguan umum hulu `DRY_RUN`/`P_LOW`/`ESTOP`) |
| `event_id` | `BIGINT` | `20` | `FK` | `NULL` | Relasi ke `irrigation_events.event_id` (`NULL` bila gangguan di luar sesi pohon) |
| `resolved_by` | `INT` | `11` | `FK` | `NULL` | Relasi ke `users.user_id` (`NULL` hingga gangguan diverifikasi mitra/tim) |
| `fault_code` | `ENUM` | `20` | `UQ1` | `NOT NULL` | `'DRY_RUN'`, `'BRANCH_CLOG'`, `'P_LOW'`, `'P_HIGH'`, `'ESTOP'` |
| `pressure_bar` | `DECIMAL` | `4,2` | — | `NOT NULL` | Tekanan sesaat saat gangguan terdeteksi (`bar`) |
| `flow_lpm` | `DECIMAL` | `5,2` | — | `NOT NULL` | Debit sesaat saat gangguan terdeteksi (`L/mnt`) |
| `action_taken` | `VARCHAR` | `64` | — | `NOT NULL` | Aksi *failsafe* (`'STOP_ALL_CYCLE'`, `'SKIP_TREE'`, `'MANUAL_STOP'`) |
| `resolved` | `BOOLEAN` | `1` | — | `NOT NULL` | Status verifikasi/penanganan mitra (`0/1`) |
| `created_at` | `DATETIME` | — | `UQ1` | `NOT NULL` | Stempel waktu `RTC` kejadian (`UQ1(fault_code, created_at)` anti-duplikasi *backfill*) |

### 2.5 Tabel `growth_records` (Log Pengamatan Agronomi `P1–P4` & Kontrol `K1–K4`)
| Nama Field | Tipe Data | Panjang | Kunci | Null | Keterangan |
|---|---|---:|---|---|---|
| `growth_id` | `INT` | `11` | `PK` | `NOT NULL` | `AUTO_INCREMENT`, ID rekaman pengamatan lapangan |
| `tree_id` | `INT` | `11` | `FK` | `NOT NULL` | Relasi ke `trees.tree_id` (`'P1..P4'` sampel & `'K1..K4'` kontrol pembanding) |
| `observer_id` | `INT` | `11` | `FK` | `NOT NULL` | Relasi ke `users.user_id` (petugas pencatat lapangan, mis. Ariq/Tim) |
| `height_cm` | `DECIMAL` | `5,1` | — | `NOT NULL` | Tinggi pohon terukur meteran (`cm`) |
| `fruit_count` | `SMALLINT` | `5` | — | `NOT NULL` | Jumlah buah terhitung per kunjungan |
| `fruit_grade` | `ENUM` | `15` | — | `NOT NULL` | Fase buah (`'NIHIL'`, `'KECIL'`, `'BESAR'`, `'PANEN'`) |
| `stem_diam_mm` | `DECIMAL` | `5,1` | — | `NULL` | Diameter batang bawah (`mm`, opsional pengamatan) |
| `measured_at` | `DATE` | — | — | `NOT NULL` | Tanggal pengukuran lapangan |

### 2.6 Tabel `system_config` (Parameter Global *Remote Tuning* & Jadwal Operasi)
| Nama Field | Tipe Data | Panjang | Kunci | Null | Keterangan |
|---|---|---:|---|---|---|
| `config_id` | `INT` | `11` | `PK` | `NOT NULL` | `AUTO_INCREMENT`, ID versi konfigurasi (`dirujuk oleh irrigation_events.config_id`) |
| `updated_by` | `INT` | `11` | `FK` | `NOT NULL` | Relasi ke `users.user_id` (pengguna pengubah konfigurasi terakhir) |
| `vwc_dry_pct` | `DECIMAL` | `4,1` | — | `NOT NULL` | Ambang batas kering pemicu siram (`% VWC`) |
| `vwc_fc_pct` | `DECIMAL` | `4,1` | — | `NOT NULL` | Batas atas *Field Capacity* / henti siram (`% VWC`) |
| `default_calib_a` | `DECIMAL` | `10,6` | — | `NOT NULL` | Konstanta default `a` model hiperbolik $y = 1/(a+bx)$ (*fallback*) |
| `default_calib_b` | `DECIMAL` | `10,6` | — | `NOT NULL` | Konstanta default `b` model hiperbolik $y = 1/(a+bx)$ (*fallback*) |
| `pulse_max_l` | `DECIMAL` | `4,2` | — | `NOT NULL` | Kuota maksimum air per putaran *Pulse Drip* (`5.00` L) |
| `p_min_bar` | `DECIMAL` | `4,2` | — | `NOT NULL` | Ambang tekanan bawah deteksi *dry-run* / filter kotor (`bar`) |
| `p_max_bar` | `DECIMAL` | `4,2` | — | `NOT NULL` | Ambang tekanan atas deteksi cabang mampet (`bar`) |
| `rtc_pagi` | `TIME` | — | — | `NOT NULL` | Jadwal cek pagi (hindari penguapan siang, mis. `06:30:00`) |
| `rtc_sore` | `TIME` | — | — | `NOT NULL` | Jadwal cek sore (`16:30:00`) |
| `flush_interval_cycles` | `TINYINT` | `3` | — | `NOT NULL` | Frekuensi otomatis katup bilas `VF` (`mis. tiap 3 siklus`) |
| `flush_duration_s` | `TINYINT` | `3` | — | `NOT NULL` | Durasi bukaan katup bilas *Auto End-Flush* `VF` (`30–45` dtk, default `35`) |
| `updated_at` | `DATETIME` | — | — | `NOT NULL` | Waktu sinkronisasi terakhir via MQTT |

### 2.7 Tabel `users` (Akun Pengguna *Dashboard Web/HP*: `E3` & `E4`)
| Nama Field | Tipe Data | Panjang | Kunci | Null | Keterangan |
|---|---|---:|---|---|---|
| `user_id` | `INT` | `11` | `PK` | `NOT NULL` | `AUTO_INCREMENT`, ID unik akun pengguna dashboard |
| `username` | `VARCHAR` | `32` | `UQ` | `NOT NULL` | Nama akun login unik (`mitra_ciberes`, `qarnie`, `ariq`, `daffa`) |
| `full_name` | `VARCHAR` | `64` | — | `NOT NULL` | Nama lengkap pengguna atau petugas kebun |
| `password_hash` | `VARCHAR` | `255` | — | `NOT NULL` | Hash kata sandi login terenkripsi (*bcrypt / Argon2*) |
| `role` | `ENUM` | `16` | — | `NOT NULL` | Peran akses sesuai DFD (`'MITRA'`, `'PENGAMAT'`, `'ADMIN'`) |
| `is_active` | `BOOLEAN` | `1` | — | `NOT NULL` | Status aktif akun (`1` aktif, `0` nonaktif) |
| `created_at` | `DATETIME` | — | — | `NOT NULL` | Stempel waktu pembuatan akun |

---

## 3. Ringkasan Komponen *Wireframe* UI (`Web Desktop` & `Mobile HP`)

Sketsa pada [wireframe_ui_dashboard_kebun_kecil.png](wireframe_ui_dashboard_kebun_kecil.png) sengaja dibuat dalam mode *low-fidelity* hitam-putih polos (sesuai ketentuan desain UI tahap `CD-3`) dengan 4 area utama:
1. **Bilah Status & Keamanan Hulu:** Indikator kondisi jaringan `4G/MQTT`, jam `RTC`, status pompa `SSR`, dan jumlah antrean log *offline* di `MicroSD`.
2. **Kartu Pemantauan Per Pohon (`P1–P4`):** Menampilkan `% VWC`, suhu tanah `DS18B20`, target dosis adaptif (`3–4 L`, `8–10 L`, `12–15 L`), status katup `V1–V4`, serta pemicu siram manual per pohon.
3. **Panel Kontrol Kritis & Hidrolika:** Tombol `[SIRAM OTOMATIS]`, tombol hitam **`[EMERGENCY STOP]`** yang memutus `SSR` pompa + menutup katup, pemicu bilas manual `Auto End-Flush VF`, serta pembacaan debit `YF-B1` (`1,5–2,0 L/mnt`) dan tekanan `[P_min..P_max]`.
4. **Grafik Tren & *Remote Tuning* (`Web`) + Tampilan Ringkas (`HP Mitra`):** Grafik garis `% VWC`/volume air, grafik batang pertumbuhan `P1–P4`, form *remote tuning* ambang Fuzzy/kalibrasi non-linear `a, b`/jadwal RTC pagi-sore, ekspor `CSV`, serta versi *mobile* untuk pengoperasian cepat oleh pekerja/mitra langsung dari kebun.
