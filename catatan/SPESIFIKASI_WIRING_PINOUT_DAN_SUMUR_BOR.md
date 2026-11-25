# Spesifikasi Wiring Pin-to-Pin, Layout Panel IP65, & Cabang 2 Jalur Sumur Bor (`CD-3 Kebun Kecil`)

**Tanggal Penyusunan:** 26 November 2026  
**Acuan Diagram & Berkas Sumber Siap Edit:**
- **Skematik KiCad (`v7/8/9`):** [panel_irigasi_kebun_kecil.kicad_sch](editable_cad/panel_irigasi_kebun_kecil.kicad_sch)
- **Berkas Mentah Draw.io (Edit Langsung Tanpa VS Code — Buka di Browser / `draw.io Desktop`):**
  1. [1_diagram_blok_sistem_kebun_kecil.drawio](editable_drawio/1_diagram_blok_sistem_kebun_kecil.drawio)
  2. [2_flowchart_sistem_kebun_kecil.drawio](editable_drawio/2_flowchart_sistem_kebun_kecil.drawio)
  3. [3_skema_pipa_2_jalur_sumur_bor.drawio](editable_drawio/3_skema_pipa_2_jalur_sumur_bor.drawio)
  4. [4_skematik_wiring_dan_layout_panel_ip65.drawio](editable_drawio/4_skematik_wiring_dan_layout_panel_ip65.drawio) *(2 tab: Wiring + Layout Panel/PCB)*
- **Pratinjau PNG/SVG Siap Masuk `CD-3`:** [skematik_wiring_panel_ip65.png](skematik_wiring_panel_ip65.png) · [layout_panel_ip65_dan_pcb.png](layout_panel_ip65_dan_pcb.png) · [skema_pipa_zona_4_pohon_teknis.png](skema_pipa_zona_4_pohon_teknis.png)

---

## 1. Tabel Netlist Pin-to-Pin `ESP32 DevKit V1 (38-Pin)`

Seluruh penetapan pin di bawah menghindari pin `ADC2` (`GPIO 0, 2, 4, 12–15, 25–27`) untuk pembacaan analog karena bentrok saat `Wi-Fi` aktif, serta menjaga tegangan masuk seluruh pin `ESP32` pada batas aman **`<= 3,3 V`**.

| Net / Fungsi | Pin `ESP32` | Perangkat / Terminal Tujuan | Level Tegangan | Pengaman / Komponen Pendukung | Spesifikasi Kabel |
|---|---|---|---|---|---|
| **`+5V_IN` & `GND`** | `VIN (5V)`, `GND` | Output `Buck Converter 12V→5V` | `5 V DC` | `C 470 µF` + `100 nF` *decoupling*, Sekring `5 A` | `AWG 18` / `0,75 mm²` |
| **`I2C_SDA`, `I2C_SCL`** | `GPIO 21`, `GPIO 22` | `ADS1115 (0x48)` · `RTC DS3231 (0x68)` · `Header PCF8574` | `3,3 V DC` | Pull-up internal modul `I2C` | *Jumper/PCB trace* `0,3 mm` |
| **`SOIL_S1..S4`** | *(via `ADS1115 A0–A3`)* | `4× Sensor Lengas Kapasitif v1.2` (`S1–S4`) | `0–3,0 V DC` *(VCC `3,3V`)* | `4× Resistor Pull-Down 1 MΩ` (`Z-11`) | `4× 3×0,5 mm²` (`<= 3,5 m`) |
| **`DS18B20_1W`** | `GPIO 4` | `4× Sensor Suhu DS18B20 Waterproof` (paralel `1-Wire`) | `3,3 V DC` | `1× Resistor Pull-Up 4,7 kΩ` ke `3,3 V` | Kabel bawaan `DS18B20` (`2–3 m`) |
| **`FLOW_PULSE`** | `GPIO 27` *(Interrupt)* | `1× Flow Sensor YF-B1 / YF-S201` (VCC `5 V`) | `5 V → 3,3 V` | **Pembagi Tegangan `R1=10 kΩ / R2=20 kΩ`** | `3×0,5 mm²` (`< 1 m` di pintu Zona 1) |
| **`PRESS_ADC`** | `GPIO 36 (VP / ADC1_CH0)` | `1× Sensor Tekanan 0–5 bar` (VCC `5 V`, out `0,5–4,5 V`) | `0,5–4,5 V → 0,33–3,0 V` | **Pembagi Tegangan `R1=10 kΩ / R2=20 kΩ`** | `3×0,5 mm²` (`< 1 m` di pintu Zona 1) |
| **`BTN_S13_STOP`** | `GPIO 16` | `1× Push Button IP65 S-13 / STOP` (pintu panel) | `3,3 V` (*Active-Low*) | `INPUT_PULLUP` + `C 100 nF` (*debounce*) | `2×0,5 mm²` internal pintu |
| **`LED_RUN`, `LED_ALM`** | `GPIO 17`, `GPIO 2` | `LED Hijau (RUN/Wi-Fi)` & `LED Merah (ALARM)` | `3,3 V DC` | `2× Resistor 220 Ω` seri | `3×0,5 mm²` internal pintu |
| **`SPI_SD`** | `18 (SCK), 19 (MISO), 23 (MOSI), 5 (CS)` | `Modul MicroSD Adapter + Kartu 16 GB` (`VCC 5 V`) | `5 V / 3,3 V` | Regulator `3,3V` bawaan modul `MicroSD` | *PCB socket / trace* `0,3 mm` |
| **`CMD_SSR_PUMP`** | `GPIO 26` | **`SSR-25DA Zero-Crossing`** → `Pompa AC 220V (125W)` | `3,3V` → **`AC 220V`** | Terisolasi optik di `SSR-25DA` + `MCB 6A` + `ELCB 16A` | `NYYHY 2×1,5 mm²` + `Conduit 20 mm` |
| **`CMD_RLY_V1..V4`** | `GPIO 13, 14, 25, 32` | `Relay Ch-1..4` → `Katup Cabang V1–V4` (`12V DC`) | `12 V DC SELV` | `4× Flyback Diode 1N4007` antiparalel di terminal | `4× 2×0,75 mm²` (`<= 3,5 m`) |
| **`CMD_RLY_VF`** | `GPIO 33` | `Relay Ch-5` → `Katup Bilas Auto End-Flush VF` (`12V DC`) | `12 V DC SELV` | `1× Flyback Diode 1N4007` antiparalel di terminal | `2×0,75 mm²` (`<= 5 m`) |
| **`WIFI_4G`** | *(Internal Wi-Fi `2,4 GHz`)* | `Router / MiFi 4G` di dalam panel (`daya 5V`) | Nirkabel | Koneksi lokal `Wi-Fi` + *non-blocking reconnect* | Tanpa kabel ke `ESP32` |

---

## 2. Arsitektur Cabang 2 Jalur Sumur Bor (Sesuai Foto Lapangan)

Mengacu pada dokumentasi lapangan [pipa sumur baru bangun.jpg](../sumber/dokumentasi/kebon%20kecil/pipa%20sumur%20baru%20bangun.jpg), sumber air di `Kebun Kecil` berupa **pipa sumur bor PVC tunggal (`~2"`)** yang keluar dari tanah *(spesifikasi kedalaman muka air dan jenis pompa akhir masih menunggu pengukuran langsung dan dapat disesuaikan kemudian)*.

Agar sistem otomatis kita berjalan tanpa mengganggu kebiasaan pekerja kebun yang masih memakai **pompa bensin Alkon** untuk menyiram `~68–69` pohon lainnya, dipasang cabang **`Tee PVC 2"`** tepat di kepala pipa sumur bor:

1. **Jalur 1 (Cabang Alkon Mitra — Manual Eksisting):**
   - Pipa `2"` → **`Stop Kran Manual SK-A (2")` → Sambungan Cepat Selang Alkon**.
   - Ketika pekerja menyiram kebun luar zona uji memakai Alkon, **`SK-A` dibuka** dan **`SK-B` ditutup**.
2. **Jalur 2 (Cabang Sistem Irigasi Presisi — Otomatis Kita):**
   - Pipa `2"` → `Reducer 2"→1"` → **`Stop Kran Isolasi SK-B (1")` → `Check Valve CV (1")` → Pompa Listrik AC `220V (125 W)`**.
   - Ketika sistem otomatis kita beroperasi, **`SK-B` dibuka** dan **`SK-A` harus tertutup rapat** (sehingga Alkon tidak menghisap udara dari cabang sebelah). **`Check Valve CV`** menjaga air pancingan pompa listrik tidak turun kembali ke sumur bor dan mencegah aliran balik saat *bypass* bekerja.
   - **Pipa *Recirculation Bypass* (`BP`):** Karena sumur bor bersifat tertutup, pipa *bypass* berkeran manual `BP` menghubungkan sisi tekan (keluaran pompa) kembali ke sisi hisap **di hilir `CV`**. Bukaan `BP` diset satu kali saat komisioning agar saat `1` pohon menyala debit tetap terbaca nyaman **`1,5–2,0 L/menit`** oleh `YF-B1` dan saat bilas `VF` tetap **`>= 6,0 L/menit`**.

---

## 3. Cara Membuka & Mengedit Sendiri File Diagram (Draw.io & KiCad — Tanpa VS Code)

1. **Edit Seluruh Diagram (Blok, Flowchart, Skema Pipa, Wiring, & Layout Panel) di Draw.io — Tanpa VS Code:**
   - **Cara Paling Cepat (Lewat Browser):** Buka [https://app.diagrams.net](https://app.diagrams.net) → pilih `Device` → klik **`Open Existing Diagram`** → pilih salah satu file `.drawio` di folder `catatan/editable_drawio/`. Semua kotak, teks, simbol, dan garis panah langsung bisa kamu geser, ubah, atau ekspor ulang ke `PNG/SVG/PDF`.
   - **Cara Offline (Saat Bimbingan / Sidang):** Pasang aplikasi gratis **`draw.io Desktop`** di Windows (`drawio.com`), lalu klik dua kali langsung file `.drawio` mana saja.
2. **Edit Skematik Elektronika & PCB di KiCad (`panel_irigasi_kebun_kecil.kicad_sch`):**
   - Buka aplikasi **KiCad (`v7 / v8 / v9`)**, klik `File → Open Schematic...` lalu pilih [panel_irigasi_kebun_kecil.kicad_sch](editable_cad/panel_irigasi_kebun_kecil.kicad_sch).
   - Seluruh blok utama (`ESP32`, `ADS1115`, `RTC DS3231`, `MicroSD`, `SSR-25DA`, `Relay 6-Ch`, `PSU SELV`), komponen pengkondisi sinyal (`4× R 1 MΩ`, `2× pembagi tegangan 10k/20k Ω`, `R 4,7 kΩ`, `5× Flyback 1N4007`, `2× LED + 220 Ω`, `C 470 µF / 100 nF`, `Tombol S-13/STOP`), konektor terminal, jalur kawat hijau, dan *global net labels* sudah tersusun rapi di atas lembar `A3` sesuai grid `2,54 mm`.
   - Tinggal geser atau teruskan ke assignment *footprint* & *PCB Editor* saat siap mencetak PCB `100 × 80 mm`.
