# Rangkuman Q&A Teknis, Penyederhanaan Scope, dan Analisis Zona Pra-Survei (`14 November 2026`)

**Tanggal Penyusunan:** 14 November 2026  
**Status Dokumen:** Dokumen Handoff Hidup (*Living Handoff Note*) untuk AI & Tim sebelum/sesudah survei lapangan Minggu di Ciberes, Subang  
**Dokumen Pendamping Utama:**
- [Kajian Sumber Air Irigasi, Pompa, & Kabel DC](KAJIAN_SUMBER_AIR_IRIGASI_DAN_POMPA.md)
- [Checklist Survei Lapangan Minggu Ciberes](CHECKLIST_SURVEI_MITRA_CIBERES.md)
- [Paparan Solusi untuk Mitra](PAPARAN_SOLUSI_UNTUK_MITRA.md)
- [Data Mitra Lengkap *(Kamus Referensi Transkrip)*](DATA_MITRA_LENGKAP.md)
- [Arsip Diskusi Awal CD-3 *(Historis Pra-Q&A)*](arsip/Bahan_Diskusi_dan_Arah_CD3.md)

> [!IMPORTANT]
> **Panduan Cepat untuk AI di Chat Baru (Jangan Minta Pengguna Menjelaskan Ulang):**
> 1. Seluruh hasil tanya-jawab rekayasa pada **14 November 2026** sudah dirangkum di sini agar chat baru langsung memahami posisi desain, kekhawatiran pengguna soal besaran *scope*, serta hitungan hidrolika/waktu skala penuh tanpa perlu *re-prompt*.
> 2. **`CD-1` (`26 hlm`) & `CD-2` (`26 hlm`, ttd Pembimbing 1 `4/11/2026`) berstatus Final ACC dan TIDAK BOLEH DIUBAH.**
> 3. **Draf `CD-3` (`dokumen/draf/cd3_daffa/` dan `dokumen/cd3/`) sengaja DITAHAN untuk tidak diedit terlebih dahulu** sampai hasil ukur survei lapangan hari Minggu terkumpul.

---

## 1. Status Operasional Pompa & Sumber Air (Sudah Diluruskan `14 November 2026`)

1. **Pompa aktif mitra:** Menggunakan **pompa mesin bensin Alkon 2 inci (Pertalite)** untuk menaikkan air dari saluran irigasi/sungai ke **3 parit galian tanah (`±100 m`, penghubung `+`)** agar pekerja dapat menimba ember.
2. **Riwayat LPG 3 kg:** Modifikasi bahan bakar LPG 3 kg **pernah dicoba** mitra untuk menghemat bensin, namun **sudah dihentikan permanen** karena mesin mengalami panas berlebih (*overheating*) dan merusak seher/ring.
3. **Pemisahan badan air & aturan 1 pompa vs 2 pompa:**
   - **Saluran irigasi besar / sungai** di samping luar pagar kebun (`garis ukur 20,54 m` & `117,52 m`) adalah **sumber air eksternal**; parit galian dalam kebun hanyalah bak tampung dekat pohon, bukan sumber air mandiri.
   - Bila air ditarik dari saluran irigasi **langsung masuk ke jaringan pipa tertutup bertekanan**, cukup **1 pompa DC surya** (tidak dobel pompa), dengan posisi pompa (`kebun atas` vs `boks bantaran + kabel 2×4–6 mm²`) menunggu hasil ukur beda tinggi tebing `Δz` (`<= 1,5–2 m` vs `> 2 m`) di survei Minggu. Rincian lengkap ada di [KAJIAN_SUMBER_AIR_IRIGASI_DAN_POMPA.md](KAJIAN_SUMBER_AIR_IRIGASI_DAN_POMPA.md).

---

## 2. Alasan Mengambil Sampel Tanah & Daya Simpan Sampel

Pertanyaan yang sudah disepakati: *Mengapa tetap mengambil sampel tanah (`1–2 kg`, kedalaman `15–30 cm`) saat survei Minggu, dan apakah aman bila disimpan lama sebelum dipakai di Bandung?*

1. **Tiga fungsi sampel tanah tapak jeruk Ciberes:**
   - **Uji daya serap & perakaran `S-04`:** Memastikan siraman `15 L` meresap habis tanpa genangan `> 30 menit` dan menembus kedalaman akar `20–40 cm` (mencegah risiko busuk akar *Phytophthora* di `CD-2`).
   - **Kalibrasi sensor bila sensor lengas dipasang:** Nilai ADC sensor kelembapan kapasitif (*Capacitive v1.2*) sangat dipengaruhi tekstur lempung/liat setempat sehingga perlu dikalibrasi memakai tanah asli tapak (*Domínguez-Niño 2019*), bukan angka bawaan pabrik atau data kebun sayuran.
   - **Menutup kekosongan data `CD-1 1.2.8`:** Kebun jeruk mitra belum pernah diuji pH/teksturnya (tidak boleh meminjam data kebun terong/kembang kol yang terpisah jarak `±500 m–1 km`).
2. **Keamanan simpan lama:**
   - Sampel tanah yang dimasukkan ke plastik ziplock bersih (terlebih jika dikeringanginkan atau disimpan kering/sejuk) **aman disimpan berminggu-minggu hingga berbulan-bulan** untuk uji tekstur, pH, EC, dan pembuatan kurva kalibrasi lengas (karena prosedur kalibrasi di lab justru dimulai dari tanah yang dikeringkan lalu dibasahi bertahap secara terukur).
   - Yang berubah bila dibiarkan lama hanyalah **kadar air sesaat saat dicangkul di kebun** — karenanya pengamatan kondisi lembap/kering lapangan dicatat langsung pada [Checklist Survei](CHECKLIST_SURVEI_MITRA_CIBERES.md) (`Pos E.2`).

---

## 3. Peta 5 Scope Teknis, Urutan Ketergantungan, dan Tingkat Kesulitan

Untuk memandu implementasi agar tidak salah urut antara hidrolika, daya, dan elektronik:

| Urutan Prioritas | Scope | Tingkat Kesulitan & Risiko | Alasan Teknis / Titik Kritis |
|---:|---|---|---|
| **1 (Fondasi)** | **Sumber Air, Elevasi (`Δz`), Pompa & Perpipaan** | **Tinggi (Paling Menentukan)** | Jika beda tinggi hisap tebing/arus sungai & kurungan *intake* salah ukur, pompa bisa *air-lock*/kavitasi, tersumbat lumpur (`C-02`), atau melanggar batas waktu `S-03`. |
| **2 (Kritis)** | **Catu Daya PLTS Off-Grid & Kabel DC (`C-01`, `C-04`, `S-06`)** | **Menengah–Tinggi** | Harus menjaga `SELV <= 48 V DC`, otonomi `>= 8 jam` (`>= 2 siklus`, `LiFePO4 DoD 80%`), drop tegangan kabel `12 V` jarak `15–20 m` (`>= 2×4–6 mm²`), serta keamanan fisik dari pencurian di kebun terbuka. |
| **3 (Inti Solusi)** | **Dosis Presisi `15 L`, Filtrasi `120 mesh`, & Keseragaman `CU >= 85%`** | **Menengah** | Inti kebutuhan mitra: *Disc Filter* `120–150 mesh`, *flow meter* terkalibrasi (`S-01`), `PC Dripper` (`p >= 0,785–1,0 bar`), keran *end-flush* (`>= 0,6 m/s`), serta **1 tombol fisik (`S-13`)**. |
| **4 (Kendali)** | **Kontroler `ESP32`, Katup Zona (`MBV`), & Proteksi `IP65` (`S-07`)** | **Menengah** | *Motorized Ball Valve* (`0 W` statis), transduser tekanan untuk deteksi pompa kering/filter mampet, LDO `3,3 V` anti-*brownout*, dalam boks `IP65`. |
| **5 (Tambahan)** | **Sensor Kelembapan Tanah & Tunda-Siram Hujan** | **Rawan *Drift* Lapangan** | Paling rentan pembacaan meleset di tanah liat retak dan korosi PCB jika epoksi bocor; fungsinya sebatas penunda saat tanah basah, bukan penentu liter air. |

---

## 4. Kesepakatan Penyederhanaan Scope: `Pure 15 L` (*Flow Meter* + Tombol) vs Sensor Tanah

Menanggapi kekhawatiran pengguna bahwa *scope* proyek terasa lebih besar dibanding topik TA kelompok lain (mis. *air quality* kandang ayam, *LiDAR*, pemilah biji kopi, atau pemantau asma), hasil verifikasi langsung atas dokumen resmi **[CD-2 Final ACC](../dokumen/cd2/CD%202%20-%20ANALISIS%20PERMASALAHAN%20PENYIRAMAN%20MANUAL%20PADA%20KEBUN%20JERUK%20LIMAU%20DI%20CIBERES%20SUBANG.pdf)** (`Tabel 3` & `Tabel 4`, hal. `11–18`) memastikan hal berikut:

1. **`CD-2` TIDAK mewajibkan otomasi penuh berbasis banyak sensor kelembapan tanah.**
   - **`S-01` (Akurasi Dosis `10–15 L ± 5%`):** Di `Tabel 4` diverifikasi memakai **`Wadah tera, Gelas ukur 1.000 mL, Flow meter`**, bukan sensor tanah.
   - **`S-04` (Radius `>= 0,5 m`; Kedalaman `20–40 cm`):** Di `Tabel 4` diverifikasi memakai **`Meteran baja, Bor tanah mini, Sensor lengas`**.
   - **`S-13` (Kemudahan Operator):** Mewajibkan pengoperasian **Tombol Tunggal (`ajar <= 30 menit`)**.
2. **Arah Desain Minimalis & Andal (*Core Pure 15 L*):**
   - **Tulang punggung utama:** `PLTS + Pompa + Disc Filter + Flow Meter terkalibrasi + PC Dripper + 1 Tombol Tunggal`. Ini sudah langsung menjawab keluhan mitra (menggantikan guyur manual, tepat `15 L/pohon`, dan masuk anggaran purwarupa **`S-08 <= Rp5.000.000`**).
   - **Jumlah sensor kelembapan tanah cukup `0–2` unit saja (JANGAN dipasang di setiap pohon/baris):**
     - **`0` sensor di kontrol otomatis (Pure `15 L` + Tombol):** Secara kontrak `CD-2` masih dapat dipertanggungjawabkan bila verifikasi `S-04` memakai `bor tanah mini + meteran baja`, serta paling kecil risiko error di lapangan.
     - **`1–2` titik `Capacitive v1.2` berkalibrasi (Opsi Hibrida Ringan):** Dipakai murni sebagai **pengaman/interlock tunda-siram saat tanah masih basah habis hujan** sekaligus mempermudah bukti telemetry untuk pembimbing tanpa menambah beban perawatan besar. Keputusan `0` vs `1–2` sensor akan disepakati bersama tim/pembimbing setelah survei Minggu.
3. **Batas Realistis Purwarupa terhadap Jadwal TA ([Jadwal PTA 2026/2027](../sumber/rubrik-jadwal/Jadwal_PTA%20--%20Rubrik%20PTA%20--%202627%20%281%29.pdf)):**
   - `CLO3 - CD3-1`: **Kamis, 10 Desember 2026** (Week 12).
   - `CLO4 - CD3-2` (Gabungan): **Kamis, 7 Januari 2027** (Week 16), diikuti `SemPro` **11–16 Januari 2027**.
   - Target perangkat keras fisik TA tetap **purwarupa pada `1` petak uji (`C-03`)**, **bukan** memasang pipa untuk seluruh kebun `500–600 pohon` sebagai syarat lulus TA; skala penuh `<= Rp18 juta` merupakan proyeksi modularitas rekayasa di dokumen.

---

## 5. Anomali Estimasi `P × L` & Kebutuhan Survei Geometri Kebun

1. **Ketidakcocokan angka mentah pra-survei yang wajib diluruskan saat turun Minggu (`Pos C`):**
   - Data lisan/awal menyebut `500–600 pohon`, tinggi `±1 m`, `3` parit memanjang `±100 m` (koridor citra `117,52 m`), dengan lebar sempat disebut `~6 m` di diskusi awal sedangkan `CD-2 Final ACC` (`hal. 7 & 22`) mencatat `lebar ~25–30 m` dan `3 lajur parit`.
   - Secara hitungan tanam: bila benar hanya ada **`3` baris pohon** sepanjang `100–117 m`, maka `500–600 pohon` memaksa jarak antar-pohon hanya **`0,5–0,6 m`** (terlalu berdempetan untuk pohon berkanopi `~1 m`). Kemungkinan besar jumlah baris pohon sebenarnya `> 3 baris` atau jumlah populasi riil `< 500 pohon`.
2. **Rekonsiliasi Petak Uji Purwarupa (`1` Zona `C-03`):**
   - Kontrak mengikat `CD-2 C-03` mensyaratkan minimal **`1` lajur barisan pohon percontohan (`15–20 pohon`) pada bentang operasional `>= 25 meter`**.
   - Draf `dokumen/draf/cd3_daffa/` sementara memodelkan `20 m × 3 baris` (~24 pohon contoh). Setelah jarak tanam nyata diukur hari Minggu, petak uji diselaraskan menjadi misalnya **`1 lajur × 25–30 m` (`15–20 pohon`)** atau **`3 baris × 25 m`** agar patuh terhadap angka tertulis `>= 25 m` dan tetap `<= Rp5.000.000`.

---

## 6. Analisis Jumlah Zona Aman untuk Skala Penuh `100 m+` (`S-03 <= 4,0 Jam`, `S-02 >= 85%`)

### 6.1 Aturan Fisika Volume vs Waktu
Pada skala penuh `500–600 pohon` dengan dosis `15 L/pohon` (`7.500–9.000 L/siklus`), batas durasi `CD-2 S-03 <= 4,0 jam/siklus` memaksa debit rata-rata pompa **minimal**:
- Untuk `600 pohon` (`9.000 L / 4 jam`): **`2.250 L/jam` (`37,5 L/menit`)**.
- Untuk `500 pohon` (`7.500 L / 4 jam`): **`1.875 L/jam` (`31,25 L/menit`)**.

> [!WARNING]
> **Koreksi Wajib Draf `CD-3` Pasca-Survei (`10 Zona / 960 L/jam` vs `S-03 <= 4,0 Jam`):**  
> Draf [`bom_and_data.py`](../dokumen/draf/cd3_daffa/bom_and_data.py#L39-L48) dan [`build_cd3_daffa.py`](../dokumen/draf/cd3_daffa/build_cd3_daffa.py#L771-L821) mencantumkan **`10 zona @ 50–60 pohon/zona`** dengan pompa **`~960 L/jam` (`16 L/menit`)** dan durasi siram **`56,25 menit/zona`** (`2 × 8 L/jam = 16 L/jam/pohon`).  
> Bila dijalankan bergilir 1 zona pada satu waktu, `10 × 56,25 menit` = **`562,5 menit` (`9 jam 22,5 menit`)**, sehingga **melanggar `CD-2 S-03 <= 4,0 jam`**. Angka proyeksi skala penuh di draf `CD-3` harus diperbaiki setelah sensus pohon riil hari Minggu selesai.

### 6.2 Perbandingan Opsi Pembagian Zona Aman untuk Bentang `100–118 m`

| Konfigurasi Zona Skala Penuh | Pohon / Zona | Emiter / Pohon | Total Durasi Siklus | Debit Pompa Aktif (@ `1,5–2 bar`) | Kelayakan Teknik, Biaya (`S-08 <= Rp18 jt`), & Waktu (`S-03`) |
|---|---:|---|---|---|---|
| **`1–2 zona`** | `250–600` | `2 × 8 L/jam` (`16 L/jam`) | `56 – 112,5 menit` | `80 – 160 L/menit` | ❌ **Over-spec**: butuh pompa besar (~0,6–1,5 kW), pipa utama >2 inci, PLTS & baterai membengkak di atas `Rp18 juta`. |
| **`4 zona` *(Rekomendasi Utama)*** | **`125–150`** | **`2 × 8 L/jam` (`16 L/jam`)** | **`4 × 56,25 mnt = 3 jam 45 mnt`** | **`33,3 – 40 L/menit` (`2.000–2.400 L/jam`)** | ✅ **PALING AMAN**: lulus `S-03 <= 4,0 jam` (ada cadangan 15 mnt untuk jeda katup/*flushing*), cukup **4 katup bermotor (`MBV`)**, tiap zona memotong panjang `100–118 m` menjadi cabang `PE 16 mm` sepanjang hanya **`~25–30 m`** sehingga rugi gesek kecil & `CU >= 85%`. |
| **`5 zona`** | `100–120` | `2 × 8 L/jam` (`16 L/jam`) | `5 × 56,25 mnt = 4 jam 41 mnt` | `26,7 – 32 L/menit` | ⚠️ **Melewati `4,0 jam`** pada dosis `15 L`, baru lolos (`3 jam 45 mnt`) jika dosis tervalidasi `12 L/pohon`. |
| **`8 zona` *(emiter 2× lipat)*** | `63–75` | `4 × 8 L/jam` (`32 L/jam`) | `8 × 28,1 mnt = 3 jam 45 mnt` | `33,3 – 40 L/menit` | ⚠️ **Waktu & hidrolis aman**, tetapi jumlah emiter membengkak ke **`2.400 unit`** + **8 katup MBV** sehingga sangat mepet terhadap pagu `Rp18 juta`. |
| **`10 zona` bergilir** *(draf lama)* | `50–60` | `2 × 8 L/jam` (`16 L/jam`) | **`9 jam 22 mnt`** | `16 L/menit` (`960 L/jam`) | ❌ **Melanggar `S-03 <= 4,0 jam`** (kecuali menyala `3` zona serentak per gelombang dengan pompa `~40–48 L/menit`, yang fungsinya sama saja dengan 4 zona tetapi boros katup). |

**Alasan hidrolis `4 zona` untuk `100 m+`:**
- Selang lateral `PE 16 mm` (`ID 13,6 mm`) tidak boleh ditarik menerus `100 m` dari satu ujung karena kehilangan tekanan membuat ujung baris jatuh di bawah tekanan kompensasi dripper (`~0,785–1,0 bar` di `simulate_and_plot_cd3.py`) dan menyulitkan *end-flush* `>= 0,6 m/s`.
- Dengan `HDPE mainline 1,5–2 inci` dan `4 zona`, cabang lateral `PE 16 mm` cukup sepanjang **`~25–30 m`** per zona. Satu segmen `25–30 m` tersebut sekaligus menjadi modul fisik yang langsung diuji pada purwarupa TA (`C-03`).
- Perkiraan beban listrik pompa `~40 L/menit` @ *head* `~20–25 m` adalah sekitar `~250–350 W` selama `3,75 jam` (`~1,0–1,3 kWh/siklus`), yang masih memiliki waktu pengisian PLTS **`2–3 hari`** sesuai interval penyiraman mitra.
- **Catatan pasca-sensus Minggu:** bila jumlah pohon aktif ternyata lebih sedikit (misal `~350–400 pohon`) atau dosis terukur cukup `10–12 L/pohon`, konfigurasi `4 zona` tetap aman dengan kebutuhan debit pompa yang jauh lebih ringan (`~22–32 L/menit`).

---

## 7. Standar Perbaikan Teknis Perangkat Keras atas Draf Awal (Diserap dari Catatan `CD-3`)

Agar tidak perlu membuka catatan arsip terpisah, berikut poin teknis wajib dari hasil telaah draf awal rekan & literatur yang tetap dipertahankan dalam desain `CD-3`:

1. **Aktuator Katup & Proteksi Baterai:** Gunakan ***Motorized Ball Valve (MBV)* `12 V DC`** (atau *latching solenoid* + H-Bridge `DRV8800`/L298N) berkonsumsi **`0 W` statis** agar tidak menguras baterai dan bebas korosi kawat solenoid *Normally Closed*; tambahkan *interlock* pemutus beban saat **`V_bat < 11,5 V`** (`LiFePO4 4S`) dan tunda anti-siklus pendek pompa **`> 30 detik`**.
2. **Instrumentasi & Anti-*Brownout*:**
   - **Dosis Presisi (`S-01`):** Kalibrasi gravimetrik *flow meter* (`YF-S201` atau meter air pulsa *reed switch*) memakai gelas/ember ukur sebelum pemasangan lapangan.
   - **Sensor Tekanan Nyata (Menghapus "Sensor Hantu"):** Pasang `1× Transduser Tekanan Elektronik 0–5 bar` (`0,5–4,5 V` dengan pembagi tegangan ke `3,3 V ADC`) di hilir *disc filter* untuk deteksi sumbatan (`Δp >= 0,7 bar`), pompa kering, atau pipa pecah, didampingi `1× manometer jarum` manual di hulu filter.
   - **Jika memakai `1–2` titik sensor kelembapan tanah (*Capacitive v1.2*):** Wajib tambah resistor *pull-down* **`1 MΩ`**, kapasitor filter **`0,1 µF`** + perataan 10–16 sampel ADC, **regulator `3,3 V` eksternal terpisah (`AP2112` / buck `3,3 V`)** anti-*brownout*, ***power-gating* MOSFET**, segel epoksi/silikon pada tepi PCB, dan kurva kalibrasi tanah liat Ciberes.
3. **Hidrolika & Filtrasi Sungai:** Pra-pompa memakai keranjang hisap + *foot/check valve* polimer/kuningan (**hindari besi cor**), lalu *Disc Filter 1" 120–150 mesh* (`<= 130 µm`, `S-05`) dengan keran bilas, dan tiap ujung baris `PE 16 mm` memakai **keran *end-flush*** agar pembilasan mencapai **`>= 0,6 m/s`**.
4. **Kepatuhan Inti `CD-2 Final ACC` (`C-01..C-05`, `S-01..S-14`):** `100% off-grid` (`C-01`), air sungai berpartikel `20,54 m` (`C-02`, `S-05 >= 120 mesh`), petak uji min. `1` lajur `15–20 pohon >= 25 m` (`C-03`), `SELV <= 48 V DC` & `IP65` (`C-04`, `S-07`), dosis `10–15 L ± 5%` (`S-01`), `CU >= 85%` (`S-02`), durasi penuh `<= 4,0 jam` (`S-03`), otonomi `>= 8,0 jam` (`S-06`), pagu **`<= Rp5.000.000`** purwarupa / **`<= Rp18.000.000`** penuh (`S-08`), `OPEX <= Rp50.000/siklus` (`S-09`), `PP <= 12–18 bulan` (`S-10`), `eta_a >= 80%` (`S-11`), `0 g/kWh` emisi (`S-12`), `1 tombol` ajar `<= 30 mnt` (`S-13`), perawatan `<= 20 mnt/bln` (`S-14`).

---

## 8. Daftar Antrean Edit `CD-3` Pasca-Survei Minggu (Jangan Dikerjakan Sebelum Data Masuk)

Saat pengguna kembali membawa data survei Minggu (mengisi `Pos A–G` di [CHECKLIST_SURVEI_MITRA_CIBERES.md](CHECKLIST_SURVEI_MITRA_CIBERES.md) dan lembar isian di [KAJIAN_SUMBER_AIR_IRIGASI_DAN_POMPA.md](KAJIAN_SUMBER_AIR_IRIGASI_DAN_POMPA.md)), lakukan urutan kerja berikut pada `dokumen/draf/cd3_daffa/`:

1. **Kunci arsitektur suplai air (`Skenario B` vs `C1` vs `C2`)** & posisi fisik pompa (`kebun atas` vs `boks bantaran + kabel 2×4–6 mm²`) berdasarkan `Δz` nyata & status irigasi kemarau.
2. **Perbaiki baris `554` `build_cd3_daffa.py`** agar seragam menyebutkan **Alkon Pertalite aktif** (uji coba LPG 3 kg dihentikan karena *overheating*).
3. **Selaraskan dimensi petak uji purwarupa** (`>= 25 m` per `C-03`) dengan jarak tanam & jumlah baris nyata hasil sensus kebun.
4. **Koreksi proyeksi skala penuh (`bom_and_data.py` & `build_cd3_daffa.py`)** dari `10 zona / 960 L/jam` (`9,38 jam`) menjadi jumlah zona yang patuh `S-03 <= 4,0 jam` (kandidat utama **`4 zona`** sesuai populasi riil hasil sensus).
5. **Kunci keputusan sensor tanah (`0` atau `1–2` titik *interlock* hujan)** di samping **`Flow Meter` + tombol tunggal (`S-01`, `S-13`)**, lalu ekspor ulang DOCX → PDF dan periksa render visual halaman per halaman.

---

## Riwayat Pembaruan Dokumen
- **14 November 2026:** Penyusunan ringkasan menyeluruh hasil tanya-jawab pra-survei (tanah, 5 scope berurutan, opsi penyederhanaan *Pure 15 L* + `0–2` sensor sesuai `CD-2`, anomali `P × L`, dan perhitungan zona aman skala penuh `100 m+` untuk `S-03 <= 4,0 jam`) sebagai panduan langsung bagi chat AI berikutnya.
