# Rangkuman Diskusi, Sinkronisasi CD-1/CD-2, dan Arah Desain Teknis CD-3
**Proyek Capstone S1 Teknik Komputer — Fakultas Teknik Elektro, Universitas Telkom**  
*Topik: Sistem Otomasi Irigasi Tetes Terzonasi Bertenaga Surya untuk Kebun Jeruk Limau, Ciberes, Subang*  
*Tanggal Penyusunan: 13 November 2026 · Diperbarui: 14 November 2026*

> [!NOTE]
> **Status Sinkronisasi Pra-Survei (14 November 2026):**  
> - **Acuan Operasional Pompa Mitra:** Kebun Ciberes aktif menggunakan **pompa bensin Pertalite (Alkon 2 inci)**; modifikasi LPG 3 kg adalah uji coba terdahulu yang dihentikan karena *overheating*.  
> - **Rencana Finalisasi Setelah Survei Minggu:** Keputusan arsitektur pengambilan air saluran irigasi vs kolam/parit tampungan, ukuran kabel `12 V`, panjang petak uji terhadap `C-03 >= 25 m`, dan angka final BOM draf `dokumen/draf/cd3_daffa/` (yang saat ini di skrip `bom_and_data.py` bernilai **Rp4.850.000** perangkat keras purwarupa / **Rp6.435.000** dengan dukungan / **Rp17.790.000** skala penuh) baru akan dikunci bersama setelah data survei Minggu terkumpul di [Kajian Sumber Air & Pompa](../KAJIAN_SUMBER_AIR_IRIGASI_DAN_POMPA.md) dan [Checklist Survei](../CHECKLIST_SURVEI_MITRA_CIBERES.md).

---

## 1. Pengikatan Mutlak terhadap CD-1 & CD-2 (Hasil Verifikasi Berkas Final)

Seluruh rancangan CD-3 wajib tunduk pada fakta CD-1 ([CD-1 Final ACC](../../dokumen/cd1/CD%201%20-%20ANALISIS%20PERMASALAHAN%20PENYIRAMAN%20MANUAL%20PADA%20KEBUN%20JERUK%20LIMAU%20DI%20CIBERES%20SUBANG.pdf), 26 hlm) dan batasan/spesifikasi CD-2 final ([CD-2 Final ACC](../../dokumen/cd2/CD%202%20-%20ANALISIS%20PERMASALAHAN%20PENYIRAMAN%20MANUAL%20PADA%20KEBUN%20JERUK%20LIMAU%20DI%20CIBERES%20SUBANG.pdf), 26 hlm):

| Kode CD-2 | Ketentuan Mengikat | Implikasi Langsung pada Desain CD-3 |
|---|---|---|
| **`C-01` & `S-06`** | 100% *off-grid* (PV + baterai), cadangan $\ge 8{,}0\text{ jam}$ ($\ge 2$ siklus penuh, LiFePO4 `DoD = 80%`). | Tidak boleh ada catu PLN (`220 VAC`); jendela puncak Indonesia 5 jam/hari dengan efisiensi sistem 60% (*Nurwidiana 2022*) & derating termal PV siang 14,22% (*Bawa 2023*). |
| **`C-02` & `S-05`** | Kompatibel air sungai keruh berjarak **20,54 m**, saringan **$\ge 120\text{ mesh}$ ($\le 130\text{ }\mu\text{m}$)**. | Wajib saringan hisap kasar pra-pompa (tanpa besi cor/*cast iron*) + *Disc Filter* 120–150 mesh + katup bilas (`Δp = 70 kPa` optimal pada 124 µm) + keran *end-flush* di tiap ujung baris ($\ge 0{,}6\text{ m/s}$ cegah flokulasi liat). |
| **`C-03`** | Purwarupa petak uji minimal **15–20 pohon pada bentang operasional $\ge 25\text{ meter}$**, modular ke 500–600 pohon (~3.000 m²; bentang 100–117,52 m). | **Penyelarasan usulan koridor 20 m × 3 baris** (lihat Bagian 2): memasang 3 baris lateral × 20 m (total **60 m lateral**, ~24–30 pohon) + pipa transmisi sungai 20,54 m memenuhi koridor hemat 20 m sekaligus melampaui syarat $\ge 15\text{–}20\text{ pohon}$ & bentang $\ge 25\text{ m}$. |
| **`C-04` & `S-07`** | Keselamatan kelistrikan **SELV $\le 48\text{ V DC}$** (`IEC 60364-4-41`) & selungkup **IP65** (`20–55 °C`). | Sistem 12 V / 24 V DC aman sentuh di lahan basah; kotak kendali polikarbonat IP65 + *cable gland* + konektor tahan air (seperti SP13 IP68 atau *conduit* antihama FAO). |
| **`S-01`, `S-02`, `S-04`, `S-11`** | Dosis **10–15 L $\pm$ 5% / pohon**, **$CU \ge 85\%$**, pembasahan radius **0,5–0,8 m**, kedalaman **20–40 cm** (tanpa genangan $>30\text{ menit}$), efisiensi aplikasi **$\eta_a \ge 80\%$**. | Dosis diukur dengan **meter air pulsa / *flow sensor* terkalibrasi** (bukan *timer* buta); tekanan masuk lateral dijaga **$> 78{,}45\text{ kPa}$ ($\sim 0{,}8\text{–}1{,}0\text{ bar}$)** agar *PC Dripper* seragam ($CU \ge 85\%$). |
| **`S-08`, `S-09`, `S-10`** | **CAPEX Purwarupa $\le \text{Rp5.000.000}$**; Proyeksi Skala Penuh $\le \text{Rp18.000.000}$; OPEX $\le \text{Rp50.000/siklus}$; PP 12–18 bulan. | *Catatan koreksi:* Draf catatan lama keliru menulis Rp6 juta; pagu resmi CD-2 adalah **maksimal Rp5.000.000**. |
| **`S-12`, `S-13`, `S-14`** | Emisi 0 g/kWh di tajuk; tombol tunggal (`<= 30 menit` latih); pembersihan filter `< 20 menit/bulan`. | Menggugurkan robot bermesin bensin 7 HP (*Elkaoud 2025*) & genset 30 kW (`CN115804333A`); antarmuka 1 tombol fisik + OLED lokal tanpa ketergantungan internet. |

---

## 2. Rekonsiliasi Tata Letak Lapangan: `20 m × 3 Baris Parit (+)`

Berdasarkan keterangan lapangan pengguna (`Baris pohon 1 – Parit 1 – Baris pohon 2 – Parit 2 – Baris pohon 3 – Parit 3`, terdapat parit penghubung melintang `+` tiap beberapa pohon), jika panjang petak uji per lajur dibatasi **20 meter**:
1. **Mengapa jangan hanya 1 baris × 20 m:** Bila jarak tanam $\sim 2\text{–}2{,}5\text{ m}$, 1 baris 20 m hanya memuat 8–10 pohon ($< 15\text{–}20\text{ pohon}$) dan panjang lateralnya $20\text{ m}$ ($< 25\text{ m}$ pada `C-03`).
2. **Konfigurasi Solusi `20 m × 3 Baris` (Memenuhi User + `C-03`):**
   - Pipa utama PE 1" ($\sim 20\text{–}25\text{ m}$) menarik air dari sungai ke *header/manifold* distribusi yang melintasi pangkal 3 baris kebun (menyeberangi Parit 1, Parit 2, Parit 3 dengan jembatan pipa/penyangga sederhana atau *trench* kecil agar tidak mengganggu pekerja).
   - Dari *manifold* bercabang **3 lajur lateral PE 16 mm × 20 m** (total lateral **60 m** — melampaui syarat bentang $\ge 25\text{ m}$ — mencakup **20–30 pohon**, langsung membuktikan penyaluran air melewati parit memanjang & parit melintang `+`).
   - **Pembagian 2 atau 3 sub-zona katup:** Misal Zona 1 (Baris 1, ~10 pohon = 160 L/jam) dan Zona 2 (Baris 2 & 3, ~16–20 pohon, atau masing-masing 1 katup per baris untuk uji rotasi 3 zona!). Dengan pompa diafragma/sentrifugal DC 12V bekerja per ~10 pohon ($2{,}7\text{ L/menit}$ pada 1–1,5 bar), tekanan masuk lateral tetap di atas ambang **0,78–1,0 bar** (`Hadole 2022`), sehingga *PC Dripper* 8 L/jam (2 buah per pohon melingkari radius 0,5–0,8 m) bekerja di daerah kompensasinya.

---

## 3. Rincian Desain Teknis & Peningkatan Wajib atas Draf Rekan Tim (`CD 3 ...(qarnie).pdf`)

Revisi teknis terpenting dari pembacaan 28 naskah penuh atas draf awal rekan tim (`Rp 4.300.000`):

1. **Kelompok Kelistrikan & Aktuator Katup (Mengganti Solenoid NC Kontinu):**
   - **Hindari Solenoid NC biasa** (menyerap arus kontinu & memicu korosi galvanik kawat di kebun lembap, *OSTI / DOE DE-FG01-97EE15698*).
   - **Pakai *Motorized Ball Valve* DC 12 V 2-kabel/3-kabel (CR02/CR05)** atau ***DC Latching Solenoid Valve* + H-Bridge `DRV8800`/L298N**: konsumsi daya statis **0 W**, dan tipe *ball valve* berlubang penuh (*full bore*) lebih tahan terhadap serpihan/pasir sungai dibanding diafragma solenoid biasa.
   - Tambahkan ***low-battery valve shutoff interlock*** (`V_bat < 11,5 V` untuk LiFePO4 4S) + tunda anti-siklus pendek pompa **$> 30\text{ detik}$**.

2. **Kelompok Instrumentasi Sensor & Anti-*Brownout*:**
   - **Perbaikan wajib `Capacitive Soil Moisture v1.2` (*Sensors 2026, PMC13364378* & *Dafonte 2024*):** Pasang resistor *pull-down* **1 MΩ** eksternal (`Signal–GND`), kapasitor **`0,1 µF`** pada pin ADC ESP32 + perataan 10–16 sampel, **regulator 3,3 V eksternal terpisah (`AP2112` / *buck* 3,3 V terdedikasi)** untuk menghindari *brownout* `< 2,5 V`, ***power-gating* MOSFET** agar sensor mati saat tidur, serta segel silikon pada tepi PCB. Kalibrasi wajib pada sampel tanah liat Ciberes kedalaman 20–30 cm (*Domínguez-Niño 2019*).
   - **Sensor Tekanan Nyata (Menghapus "Sensor Hantu" di Firmware):** Draf awal memanggil `checkFilterPressureDifferential()` di kode, tetapi BOM hanya berisi manometer jarum. Tambahkan **1× Transduser Tekanan Elektronik 0–5 bar (0,5–4,5 V dengan *voltage divider* ke 3,3 V ADC)** di hilir filter agar ESP32 betul-betul dapat mendeteksi anomali tekanan rendah (pompa/sumber surut/bocor `< 0,6–0,78 bar`) maupun sumbatan filter/saluran, serta tetap simpan **1× manometer jarum di hulu filter** sebagai rujukan manual operator.
   - **Dosis Volume Presisi (`S-01`):** Kalibrasi gravimetrik **YF-S201** pada debit kerja zona nyata ($3\text{–}6\text{ L/menit}$) di laboratorium sebelum ke kebun (atau gunakan *water meter reed switch* 1 L/pulsa seperti *Meriç 2025*).

3. **Kelompok Hidrolika & Filtrasi Sungai:**
   - Wajib pasang **keranjang saringan hisap kasar + *foot/check valve* pra-pompa** (polimer/kuningan, **hindari besi cor**, *Lavanholi 2018*), lalu pompa DC 12 V, lalu **Disc Filter 1" 120–150 mesh** dengan **keran bilas manual**.
   - Ganti *end plug* mati di ujung 3 baris lateral PE 16 mm menjadi **3× keran *end-flush* 16 mm** agar kecepatan pembilasan melampaui ambang pengendapan **$\ge 0{,}6\text{ m/s}$** (*Lavanholi 2018*).

---

## 4. Proyeksi BOM Petak Uji `20 m × 3 Baris` (Patuh `S-08 <= Rp5.000.000`)

| No | Subsistem & Komponen Rekomendasi | Qty | Est. Satuan (Rp) | Subtotal (Rp) | Keterangan Kepatuhan |
|---:|---|---:|---:|---:|---|
| 1 | Panel Surya Monokristalin 100 Wp (dudukan tinggi bebas naungan) | 1 | 600.000 | 600.000 | `C-01`, *Nurwidiana 2022* |
| 2 | MPPT Solar Charge Controller 12V/10A–20A | 1 | 280.000 | 280.000 | Efisiensi MPPT (*Bawa 2023*) |
| 3 | Baterai LiFePO4 12,8V 24Ah–30Ah + BMS | 1 | 1.350.000 | 1.350.000 | `S-06` ($\ge 8\text{ jam}$, DoD 80%) |
| 4 | Pompa Diafragma/Sentrifugal DC 12V 100W *Self-Priming* (non-besi cor) | 1 | 260.000 | 260.000 | Uji kurva H–Q $\ge 1\text{ bar}$ |
| 5 | Saringan hisap kasar + *check valve* pra-pompa + Disc Filter 1" 120/150 mesh | 1 set | 220.000 | 220.000 | `C-02`, `S-05`, *Lavanholi 2018* |
| 6 | *Motorized Ball Valve* 12V DC 3/4" (atau *Latching Solenoid* + DRV8800/L298N) | 2–3 | 150.000 | 450.000 | 0 W statis, antikarat kabel (*OSTI*) |
| 7 | Pipa transmisi PE 1" (30 m: 20,5 m sungai + *manifold* 3 baris) + fitting | 1 set | 360.000 | 360.000 | Menyeberangi 3 parit |
| 8 | Pipa Lateral PE 16 mm (60 m untuk 3 baris × 20 m) + 3× keran *end-flush* + cincin 4/7 mm | 1 set | 320.000 | 320.000 | `C-03` (>25 m lateral total), *end-flush* $\ge 0{,}6\text{ m/s}$ |
| 9 | PC Dripper 8 L/jam (60 unit untuk 24–30 pohon × 2/pohon) | 60 | 4.000 | 240.000 | `S-02` ($CU \ge 85\%$), `S-04` |
| 10 | ESP32 + LDO 3,3 V eksternal + RTC DS3231 + OLED + tombol fisik 1-sentuhan | 1 set | 175.000 | 175.000 | `S-13`, *Sensors 2026* |
| 11 | Sensor: *Flow Meter* YF-S201 (terkalibrasi) + 1× Transduser Tekanan 0–5 bar + 1× Manometer hulu + 2× Capacitive v1.2 (R 1 MΩ + 0,1 µF + MOSFET + silikon) | 1 set | 290.000 | 290.000 | `S-01` dosis liter, deteksi sumbatan nyata (*Meriç 2025*; *Zong 2019*) |
| 12 | Boks IP65 + *gland* + kabel NYAF + sekring + MOSFET driver pompa + rangka PV | 1 set | 380.000 | 380.000 | `C-04` SELV, `S-07` IP65 |
| — | **TOTAL PROYEKSI PURWARUPA TERVERIFIKASI** | — | — | **Rp4.925.000** | **Patuh ketat `S-08` ($\le \text{Rp5.000.000}$)** |

> **Catatan fleksibilitas anggaran & sinkronisasi dengan skrip draf CD-3 (`14 November 2026`):** Tabel di atas mencatat proyeksi awal 13 November sebesar `Rp4.925.000`. Pada skrip draf terpisah [`dokumen/draf/cd3_daffa/bom_and_data.py`](../../dokumen/draf/cd3_daffa/bom_and_data.py) angka *hardware* purwarupa telah dipadatkan ke **Rp4.850.000** (atau **Rp6.435.000** bila memasukkan pos pendukung riset/uji lab), dengan proyeksi skala penuh 600 pohon **Rp17.790.000**. Jika menggunakan **2 katup zona** (Zona 1 = Baris 1; Zona 2 = Baris 2 & 3, ~12 pohon per zona) dan baterai LiFePO4 12V 24Ah (~Rp1.150.000), total BOM dapat ditekan ke **~Rp4.550.000**, menyisakan cadangan untuk kebutuhan kabel DC `2×4–6 mm²` atau kurungan *intake* pasca-survei Minggu.
