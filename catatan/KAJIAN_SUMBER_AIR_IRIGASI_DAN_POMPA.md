# Kajian Teknis Sumber Air Irigasi, Penempatan Pompa, dan Kabel Daya Kebun Jeruk Limau

**Tanggal Penyusunan:** 14 November 2026  
**Status Dokumen:** Dokumen Hidup (*Living Document*) — Pra-Survei Lapangan (siap diperbarui setelah survei Minggu di Ciberes, Subang)  
**Dokumen Terkait:**
- [Rangkuman Q&A Scope, Pure 15 L, & Zonasi 100 m+](RINGKUMAN_QNA_SCOPE_DAN_ZONASI_PRA_SURVEI.md)
- [Checklist Survei Mitra Ciberes](CHECKLIST_SURVEI_MITRA_CIBERES.md)
- [Paparan Solusi untuk Mitra](PAPARAN_SOLUSI_UNTUK_MITRA.md)
- [Data Mitra Lengkap *(Kamus Transkrip)*](DATA_MITRA_LENGKAP.md)

> **Posisi Dokumen:** Catatan ini menghimpun analisis teknik sumber air dan pompa hasil tanya-jawab internal sebelum survei Minggu ke Ciberes. **Dokumen ini belum mengubah naskah resmi `CD-1`, `CD-2`, maupun draf `CD-3`** (`dokumen/cd1/`, `dokumen/cd2/`, `dokumen/draf/cd3_daffa/`). Keputusan akhir arsitektur pompa (Opsi B vs Opsi C1/C2) baru dikunci setelah data elevasi tebing, debit/kontinuitas saluran irigasi, dan biaya bensin Alkon terukur di lapangan.

---

## 1. Pelurusan Istilah Sumber Air (Jangan Sampai Tertukar)

Dalam wawancara dan citra lokasi sering muncul kata **"sungai"**, **"irigasi"**, dan **"parit"**. Agar tim, mitra, dan dosen pembimbing memakai acuan yang sama, batas definisinya adalah sebagai berikut:

| Istilah | Wujud Fisik di Tapak | Bukti Visual / Rekaman | Status & Masalah Teknis |
|---|---|---|---|
| **Saluran Irigasi Besar / "Sungai"** | Badan air terbuka lebar (`±25–30 m` perkiraan visual video) yang sejajar di sisi jalan/tanggul sepanjang koridor kebun | Citra `Jarak_Menuju_Sungai_20_54m.png` (`20,54 m` dari pin kebun ke badan air), `Screenshot 2026-10-05 204359.png` (`117,52 m`), Video `00:02`, dan `Audio 2` `03:05–03:13` (*"air irigasi"*) | Sumber air **eksternal**. Belum dikonfirmasi status resminya (saluran irigasi teknis/sekunder PJT II/PU atau sungai alami), pola buka-tutup pintu air saat kemarau, dan selisih tinggi tebing (`Δz`). |
| **3 Parit Galian Tanah ("Irigasi Buatan dalam Kebun")** | Tiga selokan tanah tanpa beton memanjang `±100 m` dengan penghubung melintang `+` di antara bedengan jeruk | Video `00:05–00:18`, Foto `Screenshot 2026-10-05 211212.png` & `211238.png`, `Audio 1` `00:31–00:39` & `02:36–03:18` | Sarana **eksisting di dalam kebun** untuk mendekatkan air ke pekerja agar mudah ditimba dengan ember. Air di dalamnya **bukan sumber mandiri**, melainkan diisikan dari saluran irigasi besar memakai **pompa bensin Alkon 2 inci (Pertalite)**. |

**Kesimpulan istilah:**
- Parit tanah di kebun **tetap bisa dipertahankan atau dimodifikasi** bila hanya dijadikan cadangan penampung sementara, tetapi parit itu sendiri **tidak menghasilkan air** — airnya tetap berasal dari saluran irigasi besar di luar pagar kebun.
- Yang menyebabkan biaya berulang dan kerusakan pada pompa eksisting bukan semata jarak datarnya, melainkan pemakaian **pompa mesin bensin Pertalite Alkon 2 inci** setiap pengisian parit (mitra sempat mencoba modifikasi **LPG 3 kg**, namun **dihentikan** karena mesin cepat panas/*overheating* dan merusak seher/ring).

---

## 2. Fakta Geometri dari Citra Peta & Video (Jarak Datar vs Beda Elevasi)

Dari penelaahan visual atas [Jarak_Menuju_Sungai_20_54m.png](../sumber/dokumentasi/citra/Jarak_Menuju_Sungai_20_54m.png), [Screenshot 2026-10-05 204359.png](../sumber/dokumentasi/citra/Screenshot%202026-10-05%20204359.png), dan [WhatsApp Video 2026-10-05 at 21.16.41.mp4](../sumber/dokumentasi/video/WhatsApp%20Video%202026-10-05%20at%2021.16.41.mp4) (`00:02`):

1. **Kebun ternyata tepat bersebelahan memanjang dengan saluran irigasi:** Garis ukur `20,54 m` membentang dari kepala/pin petak kebun (`hulu NW`) hampir tegak lurus masuk ke tengah badan air irigasi (jarak horizontal ke bibir air diperkirakan lebih dekat, sekitar `±12–15 m`), sementara koridor kebun `117,52 m` berjalan **paralel** tepat di sepanjang saluran yang sama (berseberangan sisi dengan *Jl. Royek - Bakananyar Road*).
2. **Tantangan utama bukan jarak jauh mendatar, melainkan tangga ketinggian (`Δz`):** Detik `00:02` video memperlihatkan kebun berada di **atas tanggul**, turun ke **bantaran jalan tanah tempat motor diparkir**, lalu turun lagi ke **permukaan air irigasi**.
3. **Batas data saat ini:** Garis Google Maps `20,54 m` hanya mengukur jarak horizontal (`2D`), **belum menunjukkan tinggi vertikal `Δz`** antara muka air terendah saat kemarau, bibir bantaran bawah, dan elevasi bedengan kebun atas. Parameter `Δz` ini wajib diukur dengan meteran/selang *waterpass* pada survei Minggu.

---

## 3. Jawaban Masalah "Apakah Jadi Dobel Pompa?"

Keraguan umum saat merancang pengambilan air dari saluran irigasi adalah: *"Apakah kita butuh 1 pompa di irigasi + 1 pompa booster lagi di Zona 1 kebun agar tekanan dripper aman?"*

Jawabannya bergantung pada **apakah saluran air dibuat tertutup (berpipa penuh) atau dijatuhkan terbuka dulu**:

### Kasus A — Pipa Tertutup Langsung (`1 Pompa Saja`)
Jika 1 unit pompa surya (*pressurized DC*) menarik air dari saluran irigasi dan **langsung mendorongnya masuk ke pipa tertutup** (`Pompa -> Saringan Cakram 120-mesh -> Katup Solenoid / Zona -> Pipa HDPE -> Emiter Dripper PC`):
- Pompa **tidak perlu didobel**, karena tekanan yang sudah dibangun pompa tetap terjaga di dalam pipa tertutup sampai ujung *dripper*.
- Estimasi kasar anggaran tekanan (*head budget*) skenario 1 pompa (masih harus diverifikasi ulang dengan nilai `Δz` hasil survei Minggu):
  - Rugi elevasi naik tebing (`misal Δz = 2–3 m`): $\approx 0,20\text{–}0,30\ \text{bar}$.
  - Rugi gesek pipa HDPE `20 m` intake + `25 m` lateral (`±12 L/menit`): $\approx 0,01\text{–}0,04\ \text{bar}$.
  - Rugi saringan kotor maks (sesuai asumsi desain draf): hingga `0,70 bar`.
  - Tekanan kerja minimum *dripper* kompensasi tekanan (*PC 2 L/h*): `≥ 1,00 bar` (sesuai rentang operasi standar `0,5–3,5 bar`).
  - **Total kebutuhan head pompa:** $\approx 1,91\text{–}2,04\ \text{bar}$ (`~20–21 m head`) — angka ini masih berada dalam kapasitas **1 unit pompa DC bertekanan (`~35–40 m` / `~3,5–4 bar` maks)** tanpa memerlukan pompa kedua di kebun.

### Kasus B — Sistem Terbuka Dua Tahap (`Baru Menjadi 2 Pompa`)
Sistem baru menjadi **dobel pompa** jika air dipompa naik dari saluran irigasi lalu **dibuang terbuka ke parit tanah atau bak/kolam terpal** (tekanan air kembali jatuh ke `0 bar` terhadap atmosfer), sehingga dibutuhkan **pompa kedua** untuk menghisap air dari parit/kolam dan menekannya ke jaringan pipa tetes.

---

## 4. Analisis Penempatan Pompa, Batas Hisap (`Suction Lift`), dan Rugi Tegangan Kabel DC 12 V

Menaruh **panel surya + baterai `LiFePO4` + kotak kendali ESP32** di bantaran bawah dekat saluran irigasi **sangat berisiko** (rawan dicuri, terendam banjir luapan, atau rusak akibat kelembapan/aktivitas lalu-lalang motor di bantaran). Sebaliknya, menaruh **PLTS & kotak kendali aman di kebun atas (Zona 1)** memunculkan pertanyaan kabel ke pompa sejauh `~15–20 m`.

### 4.1 Perhitungan Rugi Tegangan Kabel DC `12 V` (Jarak 1 Arah `20 m`, Panjang Lintasan PP `40 m`)

Menggunakan nilai resistivitas tembaga $\rho = 0,0175\ \Omega\cdot\text{mm}^2/\text{m}$ dengan asumsi arus beban pompa nominal $I = 6\ \text{A}$ (pompa `~72 W` @ `12,8 V` nominal `LiFePO4`):

$$R_{\text{kabel}} = \frac{\rho \times (2 \times L)}{A}, \qquad \Delta V = I \times R_{\text{kabel}}$$

| Luas Penampang Kabel | $R_{\text{PP}}$ (`40 m`) | $\Delta V$ @ `6 A` (`%` dari `12,8 V`) | Perkiraan Tegangan di Terminal Pompa | Kelayakan Teknis |
|---|---:|---:|---:|---|
| **`0,75 mm²`** (kabel audio/kecil) | `0,933 Ω` | **`5,60 V`** (`43,8%`) | `7,20 V` | **GAGAL.** Pompa melemah/berhenti saat beban tekanan naik; kabel cepat panas. |
| **`2,5 mm²`** | `0,280 Ω` | **`1,68 V`** (`13,1%`) | `11,12 V` | **Tidak disarankan** untuk jarak `20 m` (tekanan pompa berkurang nyata saat baterai di `~12 V`). |
| **`4,0 mm²`** (kabel *twin* otomotif/PV) | `0,175 Ω` | **`1,05 V`** (`8,2%`) | `11,75 V` | **Batas wajar darurat**, lebih aman bila jarak aktual bantaran hanya `≤ 15 m` ($\Delta V \approx 0,79\ \text{V}$). |
| **`6,0 mm²`** (kabel PV DC `6 mm²`) | `0,117 Ω` | **`0,70 V`** (`5,5%`) | `12,10 V` | **Layak & Aman** jika pompa terpaksa ditaruh di bibir tebing bawah (`15–20 m` dari panel surya di kebun atas). |

*(Catatan: Jika arus puncak pompa mencapai `8 A` pada saat tekanan saringan kotor, seluruh nilai $\Delta V$ pada tabel di atas ikut naik proporsional `8/6 = 1,33×`.)*

### 4.2 Aturan Penempatan Pompa Berdasarkan Hasil Ukur Tebing (`Δz`)

Keputusan posisi fisik pompa mengikuti hasil ukur beda tinggi air terhadap tepi kebun atas pada survei Minggu:

1. **Pola Ideal — Semua di Kebun Atas (Jika Beda Tinggi Muka Air $\Delta z_{\text{hisap}} \le 1,5\text{–}2,0\ \text{m}$):**
   - Panel surya, baterai, boks ESP32, saringan cakram, **DAN pompa DC** semuanya diletakkan aman di **dalam petak Zona 1 kebun atas**.
   - **Daya hisap:** Hanya ada selang hisap keras (*spiral HDPE* `1–1,25 inci` lengkap *foot valve/check valve* di ujung) yang turun ke saluran irigasi. Tidak ada kabel daya `12 V` jarak jauh ($\Delta V \approx 0\ \text{V}$), tidak ada perangkat berharga di bantaran luar, dan pompa diafragma *self-priming* umumnya masih mampu menghisap vertikal `1,5–2,0 m` dengan catatan pipa hisap **kedap udara** dan jarak ke sumber sependek mungkin.
2. **Pola Tebing Curam — Pompa di Boks Pengaman Bantaran, PLTS di Kebun Atas (Jika $\Delta z_{\text{hisap}} > 2,0\ \text{m}$):**
   - Pompa *self-priming* kecil kesulitan menghisap vertikal terlalu tinggi (risiko kavitasi dan masuk angin/*air-lock*). Oleh karena itu, pompa ditaruh **dekat bibir air / bantaran bawah** di dalam **boks pelindung terkunci** (agar mendorong ke atas, bukan menarik tinggi).
   - **Panel surya + baterai + kontroler tetap di kebun atas**, lalu dialirkan ke pompa bawah melalui **kabel DC `2×4 mm²` atau `2×6 mm²` di dalam pipa pelindung (*conduit* PVC/HDPE) yang ditanam dangkal**, beriringan dengan pipa air `1"` menuju saringan cakram di Zona 1.

---

## 5. Proteksi Ujung Hisap Terhadap Arus Saluran Irigasi, Sampah, dan Luapan Hujan

Menjawab kekhawatiran ujung pipa hisap terbawa arus saat debit saluran naik atau hujan deras:

1. **Jangan sekadar melempar selang bebas:** Selang fleksibel tanpa jangkar akan terseret arus atau tersangkut sampah plastik/ranting.
2. **Rakitan Kurungan Pipa Pelindung (*Stilling Pipe Cage*):**
   - Pancangkan tiang pipa galvanis/besi sudut atau PVC tebal (`2–3 inci`) di tepi dalam tebing yang terlindung dari aliran utama.
   - Masukkan ujung selang hisap + *foot valve* + saringan kasar ke dalam **selongsong PVC `3–4 inci` berlubang banyak** (*perforated stilling pipe*) atau **kurungan kawat ram galvanis tahan karat** yang diikat klem baja ke tiang pancang, dengan ujung hisap menggantung **`30–50 cm` di atas dasar lumpur** agar tidak menyedot endapan dasar.
   - Pasang **sambungan lepas-cepat (*quick-release union / camlock*)** di bibir atas tebing, sehingga bila terjadi peringatan banjir besar, selang/intake dapat diangkat dalam hitungan detik tanpa memotong pipa.
3. **Interaksi Otomasi Saat Hujan:** Pada saat hujan deras (saat arus saluran paling keruh dan deras), sensor kelembapan tanah mendeteksi kecukupan lengas di daerah akar sehingga pompa **secara otomatis tidak menyala** (meminimalkan penyedotan air keruh pasca-hujan).

---

## 6. Matriks Tiga Skenario Keputusan (Diputuskan Pasca-Survei Minggu)

Tim memetakan tiga skenario arsitektur suplai air agar tidak salah pilih sebelum fakta lapangan lengkap terkumpul:

| Skenario | Skema Aliran | Kelebihan Utama | Kelemahan & Risiko terhadap Batasan `CD-2` | Syarat Keputusan Lapangan |
|---|---|---|---|---|
| **B — 1 Pompa Surya Langsung dari Irigasi *(Kandidat Utama)*** | Irigasi *(kurungan intake)* $\rightarrow$ Pompa DC Surya $\rightarrow$ Saringan Cakram $\rightarrow$ Katup Zona $\rightarrow$ *Dripper* | Eliminasi penuh Alkon Pertalite (**`OPEX ~Rp0`** bahan bakar); **`0 g/kWh`** emisi di seluruh kebun (**`S-12`** terpenuhi penuh); hanya **1 pompa** sehingga patuh pagu **`S-08 <= Rp5 jt`**. | Memerlukan izin akses saluran, proteksi arus/pencurian *intake* luar kebun, dan dipastikan saluran tidak kering berminggu-minggu di kemarau puncak. | Dipilih **JIKA** saluran irigasi tetap berair saat kemarau (atau terhenti `<= 3–5 hari`), mitra mengizinkan pipa menyeberang bantaran, dan `Δz` teratasi pola 4.2. |
| **C1 — Kolam Terpal / Parit Sekat + 1 Pompa Surya *(Rencana B)*** | *(Tahap terpisah: Alkon / sumber eksisting isi tampungan tertutup/terpal di dalam kebun)* $\rightarrow$ **1 Pompa DC Surya** $\rightarrow$ Saringan $\rightarrow$ *Dripper* | Seluruh komponen elektronika, pompa, dan PLTS 100% di dalam pagar kebun; tahan periode kering/tutup pintu irigasi selama air tampungan cukup; lumpur kasar dapat mengendap dulu di tampungan. | Jika pengisian tampungan tetap memakai pompa Pertalite Alkon eksisting: masih tersisa biaya bensin/perawatan (`OPEX`) & emisi di tepi saluran, ditambah biaya konstruksi kolam terpal/bak (`C-03`/`S-08`) serta penguapan/lumut bila tidak ditutup. | Dipilih **HANYA JIKA** saluran irigasi terbukti dikeringkan lama saat kemarau (*gilir air*), dilarang menaruh intake permanen oleh pengelola irigasi/desa, atau tebing terlalu curam/longsor. |
| **C2 — 2 Pompa DC *(Transfer Rendah + Booster Pipa)*** | Pompa celup DC surya di saluran $\rightarrow$ Bak tandon kecil di Zona 1 $\rightarrow$ Pompa Booster DC $\rightarrow$ *Dripper* | Tidak perlu *suction lift* tinggi (pompa celup mendorong air dari bawah); jeda tampungan menstabilkan sedimen sebelum masuk *dripper*. | **Dobel pompa, baterai/daya PV lebih besar**, dan biaya tandon berpotensi mendorong purwarupa menembus pagu **`S-08 <= Rp5.000.000`** serta skala penuh **`<= Rp18.000.000`**. | Hanya dipertimbangkan bila `Δz` muka air ekstrem (`> 4–5 m`) dan air sangat perlu pengendapan awal sebelum saringan cakram. |

---

## 7. Lembar Isian Hasil Survei Minggu (Diisi Sepulang dari Ciberes)

Bagian ini disiapkan kosong untuk diisi langsung sesudah survei lapangan menggunakan [CHECKLIST_SURVEI_MITRA_CIBERES.md](CHECKLIST_SURVEI_MITRA_CIBERES.md):

| No | Parameter yang Diukur / Dikonfirmasi | Hasil Ukur / Fakta Lapangan *(Isi Minggu)* | Dampak Langsung ke Desain (`CD-3`) |
|---:|---|---|---|
| 1 | **Status resmi saluran air besar** *(irigasi teknis PU/PJT II atau sungai alami)* & aturan pasang pipa intake | `[BELUM DIUKUR]` | Menentukan legalitas pemasangan intake permanen/semi-permanen (**Skenario B vs C1**). |
| 2 | **Jadwal pengeringan / gilir irigasi kemarau** *(pernah kosong total berapa hari/minggu?)* | `[BELUM DIUKUR]` | Jika pernah kering `> 7 hari`, sistem wajib mempertimbangkan buffer tampungan (**C1**). |
| 3 | **Beda tinggi vertikal muka air saat surut ke bibir bantaran (`Δz1`)** & ke **tanah kebun atas (`Δz2`)** | `Δz1 = ____ m`, `Δz2 = ____ m`, total `Δz = ____ m` | Penentu utama: **`Δz <= 2 m`** -> pompa aman di kebun atas; **`> 2 m`** -> pompa di boks bantaran + kabel `4–6 mm²` atau pompa celup. |
| 4 | **Jarak miring aktual lintasan kabel/pipa** dari titik aman PLTS Zona 1 ke posisi air terendah | `L = ____ m` | Dipakai memfinalkan ukuran penampang kabel DC (`2×4` atau `2×6 mm²`) dan panjang pipa hisap. |
| 5 | **Kecepatan arus & tanda muka banjir tertinggi di tebing** saat hujan | `[BELUM DIUKUR]` | Menentukan konstruksi pancang *stilling pipe cage* & jarak aman kotak pompa. |
| 6 | **Biaya & konsumsi aktual Pertalite pompa Alkon** per siklus pengisian parit | `____ L/siklus = Rp ________/siklus` + servis `Rp ________/thn` | Acuan dasar **OPEX eksisting sebenarnya** yang dibandingkan terhadap target `S-09/S-10`. |
| 7 | **Keputusan Skenario Sumber Air Final Tim & Mitra** | `[ B / C1 / C2 ]` | Setelah dikunci di sini, baru naskah & simulasi `CD-3` diperbarui konsisten. |

---

## Riwayat Pembaruan Dokumen
- **14 November 2026:** Penyusunan awal dokumen hidup kajian sumber air, beda tinggi tebing, analisis 1 pompa vs 2 pompa, tabel jatuh tegangan kabel DC `12 V` jarak `20 m`, proteksi banjir, dan matriks 3 skenario keputusan pra-survei Minggu.
