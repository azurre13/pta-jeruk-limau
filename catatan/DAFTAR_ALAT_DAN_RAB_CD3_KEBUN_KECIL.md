# Daftar Alat, Bahan, & Rancangan Anggaran Biaya (RAB) `CD-3` (`Kebun Kecil` — `1 Zona = 4 Pohon Sampel`)

**Tanggal Penyusunan:** 26 November 2026 *(Diperbarui: Cabang 2 Jalur Sumur Bor + Isolasi `SSR-25DA` & Proteksi Sinyal)*  
**Status Dokumen:** Dokumen Kerja Hidup (*Living Working Note*) — **Basis Subbab `1.3` (Alat & Bahan) & Subbab `1.4` (RAB 2 Fase) pada `CD-3` (`tenggat 10 Des 2026`)**. Seluruh komponen diselaraskan 100% dengan arsitektur terbaru pada [skema_pipa_zona_4_pohon_teknis.png](skema_pipa_zona_4_pohon_teknis.png), [skematik_wiring_panel_ip65.png](skematik_wiring_panel_ip65.png), [layout_panel_ip65_dan_pcb.png](layout_panel_ip65_dan_pcb.png), dan [README_ALTERNATIF_SOLUSI_DAN_SCORING_CD3.md](README_ALTERNATIF_SOLUSI_DAN_SCORING_CD3.md).

> [!NOTE]
> **Keterbukaan Sumber Harga & Status Pengadaan:**  
> Seluruh harga satuan pada dokumen ini merupakan **`[Estimasi Harga Pasar Daring Indonesia]`** (rentang wajar e-commerce/toko elektronik-pertanian per 2026, sudah memperhitungkan selisih varian mutu & ongkos kirim) — **bukan nota pembelian riil**. Sebelum belanja dan sebelum dikunci di `CD-3` / `RAB SemPro`, tim wajib memverifikasi spesifikasi **sumur bor baru** (kedalaman muka air, diameter paralon) dan melakukan survei harga/tautan toko aktual.

**Dokumen Terkait:**
- Skema Pemipaan Teknis & 2 Jalur Sumur Bor: [skema_pipa_zona_4_pohon_teknis.png](skema_pipa_zona_4_pohon_teknis.png) ([SVG](skema_pipa_zona_4_pohon_teknis.svg))
- Skematik Wiring Panel IP65 & Layout Panel/PCB: [skematik_wiring_panel_ip65.png](skematik_wiring_panel_ip65.png) · [layout_panel_ip65_dan_pcb.png](layout_panel_ip65_dan_pcb.png) · [SPESIFIKASI_WIRING_PINOUT_DAN_SUMUR_BOR.md](SPESIFIKASI_WIRING_PINOUT_DAN_SUMUR_BOR.md)
- Diagram Blok & Flowchart Cara Kerja: [diagram_blok_sistem_kebun_kecil.png](diagram_blok_sistem_kebun_kecil.png) · [flowchart_sistem_kebun_kecil.png](flowchart_sistem_kebun_kecil.png)
- Alternatif Solusi, Anti-Mampet, & *Design Matrix Scoring*: [README_ALTERNATIF_SOLUSI_DAN_SCORING_CD3.md](README_ALTERNATIF_SOLUSI_DAN_SCORING_CD3.md)
- Data Lapangan `Kebun Kecil` & `4` Pohon Sampel: [DATA_KEBUN_KECIL_DAN_ZONA_4_POHON.md](DATA_KEBUN_KECIL_DAN_ZONA_4_POHON.md)
- Transisi `Kebun Besar` → `Kebun Kecil`: [README_TRANSISI_KEBUN_BESAR_KE_KEBUN_KECIL_CD2_CD3.md](README_TRANSISI_KEBUN_BESAR_KE_KEBUN_KECIL_CD2_CD3.md)

---

## 1. Ringkasan Pilihan Paket Budget (`Fase 1 — Pengembangan Purwarupa`)

Mengacu pada batasan `S-08` (`CAPEX purwarupa <= Rp5.000.000`), disediakan **2 konfigurasi paket** untuk **Alternatif 1 (*Precision Surface Drip / FDI*)** agar tim bebas memilih sesuai keseimbangan dana mahasiswa dan keawetan katup anti-mampet:

| Paket | Fokus Pilihan Komponen Kunci | Total Exact Blok 1–4 (+ Cadangan `5%`) | Posisi terhadap Pagu `S-08 (<= Rp5 jt)` |
|---|---|---:|---|
| **Paket A — Ekonomis Terukur** | `Cabang 2 Jalur Sumur Bor (SK-A/B + CV + BP)` + `Pompa AC 220V 125W` + `SSR-25DA` + `MCB/ELCB` + `4× Solenoid 12V DC` (`+1 VF`) + `Router/MiFi 4G` + `8× Penetes Adjustable (2/pohon)` | **`Rp2.836.050 – Rp4.244.100`** *(tanpa cadangan: `Rp2.701.000 – Rp4.042.000`)* | **Lolos aman** (`57%–85%` dari pagu) |
| **Paket B — Tahan Mampet Unggul** | `Cabang 2 Jalur Sumur Bor` + `Pompa AC 220V Non-Cast Iron` + `SSR-25DA` + **`5× Motorized Ball Valve Full-Bore 12V`** *(anti-macet partikel)* + `ADS1115 16-bit` + `Router/MiFi 4G` + `8× Penetes Adjustable (2/pohon)` | **`Rp3.502.800 – Rp4.984.350`** *(tanpa cadangan: `Rp3.336.000 – Rp4.747.000`)* | **Masih di bawah pagu** (`70%–99,7%` dari pagu; disarankan pilih rentang tengah `~Rp4,1–4,3 jt`) |

*(Catatan: Paket A cocok jika target belanja riil tim dijaga hemat di kisaran **`~Rp3,3–3,6 juta`**; Paket B memakai `5× Motorized Ball Valve Full-Bore` yang paling tahan partikel lumpur dengan selisih biaya katup `~Rp450–500 rb`.)*

---

## 2. Rincian Daftar Alat & Bahan — **RAB Fase 1: Pengembangan & Implementasi Purwarupa**

Seluruh item di bawah mengikuti arsitektur teraudit pada [skema_pipa_zona_4_pohon_teknis.png](skema_pipa_zona_4_pohon_teknis.png) dan [skematik_wiring_panel_ip65.png](skematik_wiring_panel_ip65.png) (`Sumur Bor 2 Jalur (Alkon + Pompa AC) · SSR-25DA Terpisah · Zona 100% SELV 12V/5V DC · Pembagi Tegangan Aman 3,3V · 1 Flow Sensor 1,5–2,0 L/mnt/pohon · 2 Penetes/Pohon di Atas Tanah`).

### Blok 1 — Area Sumur Bor Baru (`2` Jalur: Alkon + Pompa AC `220V`, *Bypass*, & Pipa Induk `~16,2 m`)

| No | Nama Komponen & Spesifikasi Teknis | Fungsi di Sistem | Jml | Satuan | Est. Harga Satuan (Rp) | Est. Subtotal (Rp) |
|---:|---|---|---:|---|---:|---:|
| 1.1 | **Pompa Air Listrik PLN `AC 220V` (`125 W`, `Non-Cast Iron` — bodi *engineering polymer / stainless steel*)** *(Catatan: spesifikasi akhir menyesuaikan pengukuran kedalaman muka air sumur bor baru)* | Mendorong air sumur pada **Jalur 2** tanpa *voltage drop* kabel `20 m` & anti-serpihan karat (`Z-16`) | `1` | unit | `350.000 – 500.000` *(Paket A)*<br>`500.000 – 650.000` *(Paket B)* | `350.000 – 650.000` |
| 1.2 | **Set Cabang `2` Jalur Sumur Bor** (`Tee PVC 2"`, `1× Stop Kran PVC 2" SK-A` untuk **Jalur 1 Alkon**, `Reducer 2"→1"`, `1× Stop Kran PVC 1" SK-B` + `1× Check Valve Kuningan/PVC 1" CV` untuk **Jalur 2 Pompa Kita**) | Memungkinkan pompa bensin Alkon mitra tetap bekerja di Jalur 1 sementara sistem otomatis kita memakai Jalur 2 tanpa hisap angin/balik | `1` | set | `130.000 – 195.000` | `130.000 – 195.000` |
| 1.3 | **Pipa Induk Utama (`PE HDPE 20 mm / PVC AW 1/2"` — panjang kebutuhan `~18–20 m`)** *(acuan ukur jalur siku sumur `16,20 m` + margin sambungan)* | Mengalirkan air bertekanan dari pompa Jalur 2 ke pintu `Zona Uji 1` (`1` jalur tunggal) | `20` | m | `5.000 – 7.500` | `100.000 – 150.000` |
| 1.4 | **Kabel Daya Pompa AC (`NYYHY / NYMHY 2×1,5 mm²`)** + **Pipa Pelindung (*Conduit*) `20 mm`** (`20 m` ikut jalur pipa induk) | Menyalurkan kendali daya AC pompa dari `SSR-25DA` panel ke sumur *(nol kabel sensor ke sumur)* | `1` | paket | `140.000 – 210.000` | `140.000 – 210.000` |
| 1.5 | **Aksesoris Sambungan Sumur–Hulu & Jalur *Recirculation Bypass* (`BP`)** (*Tee hulu, keran manual `BP` di hilir `CV` menuju hisap pompa, Socket drat, Elbow 90°, Watermur, Seal Tape, Lem PVC*) | Mengatur debit agar tetap `>= 1,0 L/mnt` per cabang (cegah pompa *overpressure*) & memudahkan servis lepas-pasang | `1` | set | `85.000 – 125.000` | `85.000 – 125.000` |
| | **Subtotal Blok 1** | | | | | **`805.000 – 1.330.000`** *(A max `1.180.000`)* |

---

### Blok 2 — Pintu Zona 1 (`Pos ESP32`, Filtrasi, Sensor Hulu, Catu Daya Hibrida, `SSR-25DA`, & `Wi-Fi → Router 4G`)

Semua komponen mahal, sensor debit/tekanan, dan panel kontrol berkumpul di pinggir `Zona Uji 1` agar seluruh kabel zona pohon (`SELV 12V/5V DC`) hanya **`~1,5–3,5 m`**.

| No | Nama Komponen & Spesifikasi Teknis | Fungsi di Sistem | Jml | Satuan | Est. Harga Satuan (Rp) | Est. Subtotal (Rp) |
|---:|---|---|---:|---|---:|---:|
| 2.1 | ***Disc Filter* `120–150 Mesh` (`3/4"` / `1"` inline)** *(Lapis 1 Anti-Mampet)* | Menyaring partikel lumpur/pasir `100–130 µm` sebelum masuk sensor, katup, & emiter | `1` | unit | `95.000 – 150.000` | `95.000 – 150.000` |
| 2.2 | **`1×` *Flow Sensor* (`YF-B1` / `YF-S201` bodi kuningan `1/2"`, min. `1,0 L/mnt`)** | Menakar volume liter nyata per pohon (`1,5–2,0 L/mnt` bergantian) & mendeteksi *dry-run* (`Flow=0 > 10 dtk`) | `1` | unit | `75.000 – 120.000` | `75.000 – 120.000` |
| 2.3 | **`1×` Sensor Tekanan Air Elektronik (`0–0,5 MPa / 0–5 bar`, drat `G1/4"`, output `0,5–4,5 V`)** + `Tee` kuningan `1/2" → 1/4"` *(Lapis 3 Anti-Mampet)* | Memantau tekanan hilir filter terhadap rentang normal `[P_min, P_max]` untuk pisahkan *dry-run* vs cabang mampet | `1` | unit | `135.000 – 195.000` | `135.000 – 195.000` |
| 2.4 | **Mikrokontroler `ESP32 DevKit` (`38-pin`) + PCB `100×80 mm` + Komponen Pasif Proteksi** (*2× Pembagi Tegangan `10k/20k Ω` (`5V/4,5V→3,3V/3,0V`), `5× Diode 1N4007`, `4× R 1MΩ`, `R 4,7kΩ`, `2× R 220Ω`, `C 470µF/100nF`*) | Otak sistem + pengkondisi sinyal aman `<= 3,3 V` & redam lonjakan balik induktif katup | `1` | set | `80.000 – 120.000` | `80.000 – 120.000` |
| 2.5 | **Modul `ADC 16-bit I2C ADS1115` (`4-Channel`)** *(Sangat disarankan di Paket B)* | Mengatasi keterbatasan/ketidaklinieran ADC internal ESP32 (`ADC2` bentrok jika Wi-Fi aktif) untuk `4` sensor lengas | `1` | bh | `0` *(opsional Paket A)*<br>`35.000 – 55.000` *(Paket B)* | `0 – 55.000` |
| 2.6 | **Modul `RTC DS3231` (dengan baterai CR2032) + Modul `MicroSD Adapter` + `MicroSD 16 GB`** | Penjaga waktu akurat & *store-and-forward edge buffering* saat sinyal 4G kebun turun | `1` | set | `75.000 – 110.000` | `75.000 – 110.000` |
| 2.7 | **`Router / MiFi 4G` (`Wi-Fi Lokal ↔ Seluler 4G`) + Antena/Charger** | Menghubungkan `ESP32` (via Wi-Fi lokal panel) ke broker MQTT & dashboard HP mitra (`monitoring, STOP, tuning`) | `1` | unit | `250.000 – 350.000` | `250.000 – 350.000` |
| 2.8 | **Catu Daya & Proteksi PLN (`MCB 6A + ELCB 16A` jalur pompa AC + `Adaptor SELV 12V DC 5A` + `Buck 12V→5V` + Sekring + Sekat Isolator)** | Memproteksi jalur pompa AC (`MCB/ELCB`) & menurunkan listrik ke `SELV <= 48 V DC` (`S-07`) untuk katup, ESP32, & sensor | `1` | set | `195.000 – 285.000` | `195.000 – 285.000` |
| 2.9 | **Driver Terpisah: `1× SSR-25DA Zero-Crossing` (+ Heatsink) untuk Pompa AC + `1× Modul Relay 6-Ch` Optocoupler untuk `5` Katup `12V`** | Memisahkan total saklar pompa AC `220V` (`SSR-25DA`, cegah ESP32 reset) dari switching `5` katup `12V SELV` (`V1–V4`, `VF`) | `1` | set | `90.000 – 135.000` | `90.000 – 135.000` |
| 2.10 | **Boks Panel Outdoor `IP65` (`~300×200×150 mm`) + `Cable Gland` (`10` bh) + `1` Tombol Fisik (`S-13` / `Emergency STOP`) + `2` LED Indikator** | Melindungi seluruh elektronik dari hujan/panas (`S-07`) & menyediakan tombol siram manual sekaligus `STOP` darurat (`S-13`) | `1` | set | `165.000 – 245.000` | `165.000 – 245.000` |
| 2.11 | **Tiang Dudukan Panel (`pipa galvanis/PVC cor ~1,5–1,8 m`) + Braket/Klem** | Mendirikan Boks ESP32 setinggi `~1,2 m` di pinggir `Zona Uji 1` | `1` | set | `55.000 – 85.000` | `55.000 – 85.000` |
| | **Subtotal Blok 2** | | | | | **`1.215.000 – 1.850.000`** *(A max `1.795.000`)* |

---

### Blok 3 — Zona Uji 1 (`4` Pohon Sampel: `1` Katup + `2` Penetes Permukaan + `1` Sensor Tanah/Pohon)

| No | Nama Komponen & Spesifikasi Teknis | Fungsi di Sistem | Jml | Satuan | Est. Harga Satuan (Rp) | Est. Subtotal (Rp) |
|---:|---|---|---:|---|---:|---:|
| 3.1 | **Katup Elektrik Cabang `V1–V4` (`12 V DC`, `1/2"`):**<br>• *Paket A:* `Solenoid Valve 12V DC NC` (plastik/kuningan)<br>• *Paket B:* **`Motorized Ball Valve 12V DC Full-Bore` (`CR02`)** | Membuka/menutup suplai air tiap pohon secara bergantian (`1 pohon = 1 katup`) *(Paket B bebas risiko macet partikel)* | `4` | unit | `45.000 – 65.000` *(Paket A)*<br>`135.000 – 165.000` *(Paket B)* | `180.000 – 660.000` |
| 3.2 | **Pipa PE `16 mm` (`~20 m` jalur Zona 1 + cabang pendek) + Aksesoris (`6× Tee 16 mm`, `4× Drat Luar/Socket ke katup 1/2"`, `Elbow`, `End-Cap`, `Clamp`)** | Menyalurkan air dari `Flow Sensor` melewati tengah petak (`V1–V4`) hingga ujung bilas | `1` | paket | `95.000 – 145.000` | `95.000 – 145.000` |
| 3.3 | **`4×` Set `2` Penetes *Adjustable / Micro-Bubbler* Permukaan per Pohon (`total 8 penetes`, set `1,5–2,0 L/mnt/pohon`) + `Tee 16 mm` + Selang Mikro `3/5 mm`** | Menyalurkan `1,5–2,0 L/mnt` tepat di permukaan tanah akar tiap pohon (`2` penetes/pohon, daun tetap kering, mudah terbaca `YF-B1`) | `4` | set pohon | `15.000 – 25.000` | `60.000 – 100.000` |
| 3.4 | **`4×` Sensor Lengas Tanah Kapasitif (`v1.2 / SEN0193`, versi tahan korosi + lapisan *waterproof conformal/epoxy* pada PCB atas & *heat-shrink*)** | Mengukur kadar lengas tiap pohon (`S1–S4`) secara mandiri di tanah urugan yang timpang | `4` | unit | `25.000 – 45.000` | `100.000 – 180.000` |
| 3.5 | **`4×` Sensor Suhu Tanah `DS18B20 Waterproof` (`kabel 2–3 m` + `R pull-up 4,7 kΩ` + `R pull-down 1 MΩ` sensor lengas)** | Memantau suhu zona akar (`15–20 cm`) untuk deteksi cekaman panas & input Fuzzy | `4` | unit | `18.000 – 28.000` | `72.000 – 112.000` |
| 3.6 | **Kabel Sinyal & Aktuator Zona (`~20 m` kabel serabut isi 4 `4×0,5 mm²` + `heat-shrink` + isolasi anti-lembap + patok penahan selang)** | Menghubungkan `V1–V4` & `S1–S4` (`SELV 12V/5V`) ke panel ESP32 di sebelah Zona 1 (`jarak per titik ~1,5–3,5 m`) | `1` | paket | `75.000 – 115.000` | `75.000 – 115.000` |
| | **Subtotal Blok 3** | | | | | **`582.000 – 1.312.000`** *(A max `912.000`)* |

---

### Blok 4 — Bilas Ujung (`Auto End-Flush VF`) & Jalur Ekspansi Modular (`72–73` Pohon)

| No | Nama Komponen & Spesifikasi Teknis | Fungsi di Sistem | Jml | Satuan | Est. Harga Satuan (Rp) | Est. Subtotal (Rp) |
|---:|---|---|---:|---|---:|---:|
| 4.1 | **`1×` Katup Bilas Ujung `VF` (`12 V DC`, `1/2"`):**<br>• *Paket A:* `Solenoid Valve 12V DC`<br>• *Paket B:* `Motorized Ball Valve 12V DC Full-Bore` | **Lapis 4 Anti-Mampet (`Auto End-Flush`):** buka `30–45 dtk` berkala (`>= 0,6 m/s`) membuang endapan lumpur dari ujung pipa | `1` | unit | `45.000 – 65.000` *(Paket A)*<br>`135.000 – 165.000` *(Paket B)* | `45.000 – 165.000` |
| 4.2 | **Stop Kran Manual `SK` (`1/2"` / `16 mm`, `2` unit) + `Tee` Port Ekspansi (`2` unit)** *(di jalur hulu & di ujung Zona 1)* | **Siap Ekspansi Modular:** tinggal buka `SK` untuk menyambung `Zona Baris Barat` dan `Zona 2..N` hingga `72–73` pohon | `2` | set | `18.000 – 30.000` | `36.000 – 60.000` |
| 4.3 | **Slot Ekspansi Elektronik di PCB Panel (`Header I2C + Modul Expander PCF8574` cadangan)** | Menyiapkan pin tambahan bagi katup/sensor `Zona 2..N` tanpa mengganti ESP32 | `1` | bh | `18.000 – 30.000` | `18.000 – 30.000` |
| | **Subtotal Blok 4** | | | | | **`99.000 – 255.000`** *(A max `155.000`)* |

---

### Rekapitulasi Total Exact RAB Fase 1 (Pengembangan Purwarupa `1 Zona = 4 Pohon`)

Seluruh angka di bawah adalah penjumlahan **exact** dari rincian Blok 1–4 pada Bagian 2:

| Kelompok Blok | Paket A (Ekonomis) | Paket B (Anti-Mampet Unggul) |
|---|---:|---:|
| Blok 1 — Sumur Bor `2` Jalur (`SK-A/B + CV + BP`) & Pipa `~16,2 m` | `Rp805.000 – Rp1.180.000` | `Rp955.000 – Rp1.330.000` |
| Blok 2 — Pintu Zona 1 (Filter, Flow, Tekanan, ESP32+PCB, Router 4G, SSR+Relay, MCB/ELCB) | `Rp1.215.000 – Rp1.795.000` | `Rp1.250.000 – Rp1.850.000` |
| Blok 3 — Zona Uji 1 (`4` Pohon: `4` Katup, `8` Penetes `2/Pohon`, `4` Sensor) | `Rp582.000 – Rp912.000` | `Rp942.000 – Rp1.312.000` |
| Blok 4 — `Auto End-Flush (VF)` & Port Ekspansi Modular | `Rp99.000 – Rp155.000` | `Rp189.000 – Rp255.000` |
| **Subtotal Komponen Blok 1–4** | **`Rp2.701.000 – Rp4.042.000`** | **`Rp3.336.000 – Rp4.747.000`** |
| *Cadangan Teknis `5%` (fitting/kabel/ongkir tak terduga)* | `Rp135.050 – Rp202.100` | `Rp166.800 – Rp237.350` |
| **TOTAL CAPEX ALAT PURWARUPA (`FASE 1`)** | **`Rp2.836.050 – Rp4.244.100`** | **`Rp3.502.800 – Rp4.984.350`** |
| **Batas Pagu Spesifikasi `S-08` (`CD-2`)** | **`<= Rp5.000.000` (AMAN)** | **`<= Rp5.000.000` (AMAN)** |

*(Catatan praktik pengadaan: jika seluruh komponen Paket A dibeli pada rentang harga tengah/menengah tanpa memilih opsi termahal di setiap baris, realisasi CAPEX purwarupa berada di kisaran **`~Rp3,54 juta`**; untuk Paket B di kisaran **`~Rp4,24 juta`**.)*

---

## 3. Rincian RAB Fase 2 — Pengujian, Kalibrasi, & Operasional Uji Lapangan

Sesuai format **Template `FTE-CD-3` (`Subbab 1.4`)**, anggaran fase pengujian dipisah dari CAPEX perangkat keras agar transparan untuk mahasiswa dan pembimbing:

| No | Item Pengujian & Kalibrasi | Tujuan Pengujian / Standar `CD-2` & `CD-3` | Jml | Est. Biaya (Rp) |
|---:|---|---|---:|---:|
| T1 | **Paket Data / Kuota Kartu Perdana IoT 4G (`3–4 bulan` uji)** | Pengujian kestabilan MQTT, *remote tuning* Bojongsoang ↔ Subang, & QoS jaringan (`S-13` / KPI Anggota 3) | `3–4` bln | `120.000 – 200.000` |
| T2 | **Kompensasi Token Listrik PLN Mitra Selama Uji (`~3–4 bulan`)** | Beban daya sangat kecil (`ESP32 + 4G + pompa ~125 W hanya nyala ~15–20 mnt/siklus`), alokasi ganti listrik ke pemilik lahan | `1` paket | `50.000 – 100.000` |
| T3 | **Gelas Ukur `1000 mL / 2000 mL` & Ember/Wadah Tera `15 L`** | Verifikasi akurasi *flow sensor* (`10–15 L ± 5%`, `S-01`) & uji keseragaman `2` penetes per pohon (`CU >= 85%`, `S-02`) | `1` set | `45.000 – 85.000` |
| T4 | **Alat Kalibrasi Gravimetri Tanah Merah (`Timbangan Digital 0,1 g` + cawan aluminium/ziplock sampel)** | Membuat kurva kalibrasi lokal `VWC = m·ADC + c` (`Z-02`, `Z-11`) untuk tanah merah eks-empang `Kebun Kecil` | `1` set | `65.000 – 110.000` |
| T5 | **Bahan Habis Pakai Uji & Pemasangan (`Seal tape`, *cable ties* tahan UV `2` pak, lem, silikon seal, timah solder)** | Kerapian proteksi luar ruang & antisipasi kebocoran sambungan saat uji lapangan | `1` paket | `60.000 – 100.000` |
| T6 | **Peralatan Kerja Bengkel** (*Multimeter digital, solder, tang potong pipa PE/PVC, obeng set*) | *Pinjam Lab Teknik Komputer / milik pribadi tim (jika sudah ada = `Rp0`)* | `0–1` set | `0` *(pinjam)* / `~150.000` |
| T7 | **Logistik & Transportasi Survei/Uji Tim (`Bandung ↔ Ciberes, Subang` — operasional mahasiswa)** | Pemasangan alat, pengambilan sampel tanah, & pengambilan data uji banding `4` pohon vs `4` kontrol | `3–4` trip | *(Dicatat terpisah di logbook perjalanan tim sesuai kesepakatan kelompok)* |
| | **SUBTOTAL BIAYA PENGUJIAN & KALIBRASI (`FASE 2` Alat/Bahan)** | | | **`Rp340.000 – Rp595.000`** *(tanpa transport)* |

---

## 4. Proyeksi Biaya Ekspansi ke Seluruh `Kebun Kecil` (`72–73` Pohon) & Hitungan Ekonomi

Bagian ini menjawab pertanyaan dosen/mitra: **"Kalau uji 4 pohon sukses dan mau pasang ke seluruh 72–73 pohon di Kebun Kecil, apakah biayanya kali 18?"**

**Jawabannya: TIDAK!** Karena **unit hulu tidak perlu dibeli ulang** (`Pompa AC 220V + Bypass`, `Disc Filter`, `1× Flow Sensor`, `1× Sensor Tekanan`, `ESP32`, `MCB/ELCB + PSU SELV`, dan `Router 4G` tetap memakai unit yang sama!).

- **Konsep Ekspansi Blok Seragam:** `~68–69` pohon sisanya dibagi menjadi **`5–6` zona blok** (`~10–14` pohon seukuran per zona). Setiap zona baru **hanya butuh `1` katup zona + `1` sensor perwakilan + pipa lateral PE `16 mm` + `2` penetes per pohon** *(sekitar `Rp650.000–Rp950.000` per zona blok)*.
- **Estimasi Tambahan Ekspansi Penuh (`6` Blok Tambahan untuk `~72–73` Pohon):** `~Rp4.000.000 – Rp5.700.000` + `1` modul `PCF8574 I2C` (`~Rp20.000`).
- **Estimasi Total Biaya Sistem Penuh `72–73` Pohon (`Purwarupa Zona 1 + Ekspansi 6 Blok`):** **`±Rp6,2 juta – Rp9,5 juta`** — masih sangat jauh di bawah pagu skala penuh `S-08 <= Rp18.000.000`.
- **Perbandingan dengan Biaya Eksisting `Kebun Kecil` (`[Keterangan Mitra/Tim]` + `[Hasil Perhitungan]`):**
  - Biaya penyiraman manual berjalan saat ini: **`2 pekerja × Rp100.000 = Rp200.000 / kegiatan`** tiap **`3–4 hari`** jika tidak hujan *(atau skenario hitungan tanpa hujan `~Rp18,2–24,3 juta/tahun`, belum termasuk bensin Pertalite & servis pompa `Alkon`)*.
  - Artinya, bahkan jika mitra langsung menerapkan versi penuh `72–73` pohon (`~Rp6,2–9,5 juta`), sistem berpotensi **balik modal dalam waktu sekitar `4–6 bulan` pada musim kemarau / `~5–8 bulan` rata-rata tahunan** *(angka balik modal riil akan disesuaikan dengan jumlah hari hujan setempat di Subang pada perhitungan `CD-3`)*.
