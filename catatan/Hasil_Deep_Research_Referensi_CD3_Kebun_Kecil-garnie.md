# Hasil Deep Research Literatur Terbuka & Standar Teknis untuk CD-3 (`Kebun Kecil` — Listrik PLN & IoT 4G)

**Tanggal Disimpan:** 24 November 2026  
**Sumber:** Laporan *Deep Research* Gemini (berdasarkan prompt 4 klaster CD-3 `Kebun Kecil` + `Listrik PLN SELV` + `IoT 4G/MicroSD`)

---

## Ringkasan Eksekutif & Celah Bukti Lapangan
1. Penelusuran mencakup literatur *open-access* 2021–2026 dan standar kelistrikan resmi `IEC 60364-7-705:2006` & `HD 60364-7-705:2007`.
2. **Empat celah bukti kuantitatif yang wajib ditutup lewat uji mandiri purwarupa di kebun Ciberes:**
   - Belum ada studi Q1/Q2 terbuka yang menggabungkan `ESP32 + 4G LTE + MicroSD offline buffer + listrik PLN non-PLTS` sekaligus melaporkan data empiris `RSSI/RSRP` kebun & ukuran payload JSON.
   - Belum ada uji lapangan jeruk muda (`~16 bulan`) di tanah urugan merah heterogen yang membandingkan `CU%` & pertumbuhan tajuk antara irigasi tetes sensor vs manual.
   - Belum tersedia kurva kalibrasi + `RMSE` sensor *capacitive v1.2* khusus tanah liat merah tropis.
   - Belum ada makalah tunggal yang membandingkan keempat opsi matriks *scoring* (`tetes otomatis`, `robot`, `tandon gravitasi`, `selang semi-manual ber-flow-meter`) secara serentak.

---

## Tabel 1. Rekapitulasi Status Verifikasi Sumber & Cakupan Data

| Klaster | Identitas Sumber & Tautan Open-Access | Status Verifikasi DOI & Bibliografi | Ringkasan Relevansi Teknis | Kesenjangan Bukti di Sumber |
|---|---|---|---|---|
| **Klaster 1** | MDPI *IoT* 4(3):221–243 (`10.3390/iot4030012`) | **TERVERIFIKASI CROSSREF:** **Pereira, Chaari, & Daroge (2023)**, *IoT-Enabled Smart Drip Irrigation System Using ESP32* *(Catatan: nama "Del Aguila & Oliveira" di teks Gemini keliru; JSON-nya juga sudah ada di `_metadata_non_open_access/02_Pereira_2023`)* | Irigasi tetes ESP32, adaptor `12 V DC` + *step-down* `5 V`, *flow sensor* `FS300A` | Memakai Wi-Fi + Blynk dan sensor ion/resistif; tanpa 4G LTE, MicroSD, atau `%` hemat air |
| **Klaster 1** | MDPI *AgriEngineering* 7(11):358 (`10.3390/agriengineering7110358`) | **TERVERIFIKASI OPENALEX:** *IoT Monitoring System for Soil Aridification Stage Validated Through Data Analysis and Correlation...* (*AgriEngineering*, **2025**) | Stasiun telemetri `ESP32-S3R2` + `SIM7670G 4G LTE` (UART 115.200 bps, `TXB0108`) + MQTT | Bukan kontrol katup irigasi; memakai surya-baterai; tanpa MicroSD & RSSI |
| **Klaster 1** | *Sci. Rep.* (`PMC13043767`, `10.1038/s41598-026-37287-3`) & MDPI *Sensors* (`10.3390/s25175564`) | **TERVERIFIKASI NCBI & CROSSREF:** **Sharma, Mishra, & Yadav (2026)**, *Sci. Rep.* (`PMC13043767`); **Borankulova et al. (2025)**, *Sensors* (`10.3390/s25175564`) | Bukti parsial `microSD` via SPI 24 jam (`PMC13043767`) & `ESP8266` + router 4G + SD card (`s25175564`) | Perlu unduh XML/PDF penuhnya sebelum mengutip detail uji |
| **Klaster 2** | MDPI *Horticulturae* 11(12):1472 (`10.3390/horticulturae11121472`) | **TERVERIFIKASI CROSSREF:** **Rivera-Hernández, Garruña, & Andrade (2025)**, *Seasonal Changes in Physiological Responses and Yield of Citrus latifolia...* (*Horticulturae*) | Irigasi *Citrus latifolia* berbasis ambang tegangan lengas tanah (`−0,010` s.d. `−0,085 MPa`; 4 pohon/perlakuan) | Tidak melaporkan `%` hemat air, nilai `CU%`, atau bobot panen di teks |
| **Klaster 2** | Artikel MDPI (`10.3390/s25051568`) | **Sudah ada full-text di repo (`Z-06`, *Sensors* 2025, `10.3390/s25051568`)** | Validasi sensor kapasitif (kedalaman `15 cm` dari zona akar `30 cm`); ulas hemat air `15–20%` | Angka `15–20%` berasal dari literatur semangka (`[29]`), bukan uji primer jeruk |
| **Klaster 2** | *Frontiers in Water* (`10.3389/frwa.2026.1973897`) | **TERVERIFIKASI CROSSREF:** **Ghanghas, Sihag, & Dhanger (2026)**, *Smart water management in agriculture: convergence of sensors, imaging, AI, precision irrigation, and robotics systems* | Benchmark kontrol katup MQTT (zaitun `98,1%` akurasi) & hemat air (tomat/cabai `32%`; padi `16,5–37%`) | Tabel tinjauan lintas komoditas; bukan uji lapangan jeruk di tanah liat |
| **Klaster 3** | MDPI *Sensors* (`10.3390/s25020343`) & *Electronics* (`10.3390/electronics15204831`) | **TERVERIFIKASI CROSSREF:** **Abdelmoneim et al. (2025)**, *Sensors* (`10.3390/s25020343`); **Salah et al. (2026)**, *Electronics* (`10.3390/electronics15204831`) | Respons sensor kapasitif (`R² = 0,967`) & konstruksi PCB tahan korosi pada ESP32 | Nilai `RMSE` spesifik tanah liat merah & persamaan regresi perlu cek dari naskah penuh |
| **Klaster 3** | MDPI *Water* (`10.3390/w18121462`, `w18020244`, `w11071346`, `w15122251`) & `2673-4591/160/1/60` | **TERVERIFIKASI CROSSREF:** **Ghodgaonkar et al. (2026)** `w18121462`; **Ghonimy et al. (2026)** `w18020244`; **Solé-Torres et al. (2019)** `w11071346`; **Wei et al. (2023)** `w15122251` *(kode `2673-4591/160/1/60` belum tercocok DOI-nya)* | Uji sumbatan *PC dripper* `16 mm` (`15 psi`), eksponen `0 ≤ x ≤ 0,1`, mesh filter, sensor pra/pasca filter | Tanpa angka ambang batas numerik *dry-run* pompa atau batas `ΔP` alarm filter |
| **Klaster 3** | `IEC 60364-7-705:2006` & `HD 60364-7-705:2007` + PDF *IJEEE* 2025 | Standar resmi IEC/HD terverifikasi penuh; PDF *IJEEE* tanpa DOI di teks | Wajib **`RCD ≤ 300 mA`** pada lokasi pertanian/rumah terhubung; skema TN/TT/IT `IEC 60364-4-41` | Bukan eksperimen langsung adaptor `220 V AC → 12 V DC SELV` dalam boks `IP65` |
| **Klaster 4** | arXiv (`arxiv.org/abs/2508.08607`) | Terverifikasi penuh: Justin London (2025), DOI `10.48550/arXiv.2508.08607` | Robot penyiram otonom (Jetson Nano, RPLiDAR `12 m`, lengan 6-DOF, tangki `36 L`) | *Preprint* desain kinematika; tanpa angka uji `CU%`, hemat air, atau total biaya |
| **Klaster 4** | Artikel MDPI (`mdpi.com/2673-4117/6/7/138`) | **Sudah ada di repo (`P-06`, Elkaoud et al. 2025, `Eng`, `10.3390/eng6070138`)** | Robot *sprinkler* bergerak (`4× 350 W`, efisiensi aplikasi air `81,1–82,5%`) | Tanpa rincian biaya investasi, waktu operasi, maupun komparasi dengan tetes/manual |
| **Klaster 4** | *IJFET* (`francis-press.com/papers/10255`) | Terverifikasi: Jiahui Li et al. (2023), DOI `10.25236/IJFET.2023.050408` | Robot penyiram *line-tracking* + visi berbasis STM32 untuk tanaman pot/rumah kaca | Non-Q1/Q2; hanya abstrak tanpa angka uji kuantitatif |

---

## Ringkasan Celah & Parameter Wajib Uji Mandiri di Kebun Ciberes (Bab IV / CD-4)

| Bagian di Dokumen CD-3 | Parameter/Fakta Terverifikasi untuk Disitasi | Parameter Kosong yang Wajib Diuji Mandiri di Kebun Ciberes |
|---|---|---|
| **Bab I & II:** Justifikasi irigasi presisi & zona uji | Pertahankan SMT `−35 kPa` (`−0,035 MPa`); cekaman `−85 kPa` turunkan fisiologi & buah; hujan 6 hari tak memulihkan; 4 pohon/perlakuan; potensi hemat air `15–20%` (semangka) & `32%` (RF tomat/cabai); akurasi katup MQTT `98,1%` (zaitun) | Pemantauan tinggi/batang, jumlah buah, & konsumsi air nyata pada `4` pohon uji (`46`, `100`, `210`, `250 cm`) |
| **Bab III:** Catu daya PLN & keselamatan listrik | Wajib `RCD ≤ 300 mA` pada sirkuit lokasi pertanian/rumah terhubung (`IEC 60364-7-705`); konsep `SELV 12 V DC` (`IEC 60364-4-41`) & selungkup `IP65` (`IEC 60529`); *step-down* `12 V → 5 V` ESP32 | Pengukuran arus *inrush* & beban tunak pompa DC 12 V + modem 4G, kenaikan suhu boks `IP65`, & uji trip RCD rumah |
| **Bab III:** Sensor kelembapan *capacitive v1.2* | Penempatan kedalaman `15 cm` (zona akar `≤ 30 cm`); kalibrasi lokal naikkan akurasi `42–45%`; linearitas sensor `R² = 0,967`; antisipasi *sensor drift* | Kalibrasi gravimetrik tanah merah urugan Ciberes untuk membangun kurva `ADC → % VWC` dengan `RMSE` & `R²` aktual |
| **Bab III:** Hidraulika PE `16 mm`, *PC dripper*, & filter | Eksponen `0 ≤ x ≤ 0,1`; tekanan uji acuan `15 psi`; ukuran *mesh* filter lebih halus dari partikel pemicu *clogging*; penempatan sensor tekanan pra & pasca filter | Pengukuran `CU%` aktual `8` titik *dripper*, karakterisasi batas tekanan/aliran *dry-run*, & uji `ΔP` saat filter `120 mesh` tersumbat |
| **Bab III:** Komunikasi `4G LTE`, `MicroSD`, & payload | UART `115.200 bps` + *level shifter* `3,3 V ↔ 1,8/2,8 V` (`TXB0108`) untuk `SIM7670G`; MQTT ke DB terpusat; pola *store-and-forward* CSV di `microSD` | Pengukuran `RSRP/RSSI/SINR` operator di kebun Ciberes, uji sinkronisasi `MicroSD` saat putus sinyal, & total byte payload JSON/hari |
| **Bab III:** Matriks *Scoring* Alternatif (`1–5`) | Robot tangki `36 L` (`~2–3 pohon/isi ulang`); robot *sprinkler* `4×350 W`; emiter PC butuh tekanan uji acuan `15 psi` (`~10,5 m` *head*) | Penilaian analitis/kalkulatif lokal bagi tandon gravitasi (`~10,5 m` vs *head* tekanan) dan selang semi-manual + *flow meter* (`menit kerja/hari` untuk `72–73` pohon) |
