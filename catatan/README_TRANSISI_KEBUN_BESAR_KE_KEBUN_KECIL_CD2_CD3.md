# README Transisi Proyek: Perpindahan `Kebun Besar` → `Kebun Kecil` (`1 Zona = 4 Pohon`) & Jembatan `CD-2` ke `CD-3`

**Tanggal Penyusunan:** 23 November 2026  
**Status Keputusan:** **ACC Resmi** oleh Pembimbing 1 (**Dr. Agung Nugroho Jati, S.T., M.T.**), Dosen Pengampu Kelas, dan Mitra.  
**Tujuan Dokumen:** Menjadi catatan jembatan formal sebelum menyusun **`CD-3` (tenggat `10 Desember 2026`)**, mengarsipkan perbandingan lengkap kelebihan & kekurangan dua kebun tanpa menghapus data historis `Kebun Besar`, dan merancang konsolidasi perombakan total **`CD1–3 Final`** untuk **SemPro PTA**.

**Tautan Dokumen Terkait:**
- Data teknis `Kebun Kecil` & `4` pohon sampel: [DATA_KEBUN_KECIL_DAN_ZONA_4_POHON.md](DATA_KEBUN_KECIL_DAN_ZONA_4_POHON.md)
- Sketsa denah berskala 2D Kebun Kecil: [denah_kebun_kecil_2d.png](denah_kebun_kecil_2d.png) · [denah_kebun_kecil_2d.svg](denah_kebun_kecil_2d.svg)
- Rekaman fakta survei `15 Nov 2026` (`Kebun Besar 1`, `Kebun Besar 2`, `Kebun Kecil`): [HASIL_SURVEI_CIBERES_15_NOV_2026.md](HASIL_SURVEI_CIBERES_15_NOV_2026.md)
- Data awal mitra & transkrip penuh: [DATA_MITRA_LENGKAP.md](DATA_MITRA_LENGKAP.md)
- Indeks naskah akademik: [Direktori Dokumen CD-1/CD-2/CD-3](../dokumen/README.md)

> [!IMPORTANT]
> **Aturan Penyimpanan Data Historis (`CD-1` & `CD-2`):**  
> Seluruh data lapangan lama `Kebun Besar` (`CD-1 Final ACC` `26 hlm` & `CD-2 Final ACC` `26 hlm`) **tetap dipertahankan utuh dan tidak dibuang/dihapus**. Alasannya: (1) `CD-1` & `CD-2` sudah dikumpulkan terlebih dahulu, dan (2) kendala terukur `Kebun Besar` justru menjadi dasar ilmiah (*engineering rationale*) mengapa ruang lingkup diturunkan dan dipindahkan ke `Kebun Kecil` pada tahap **`CD-3`**, sebelum seluruh naskah digabung dan dirombak total untuk **`SemPro PTA`**.

---

## 1. Roadmap Penyusunan & Penyelarasan Dokumen Akademik

| Tahap | Tenggat / Jadwal Resmi | Status Sekarang (`23 Nov 2026`) | Perlakuan Dokumen |
|---|---|---|---|
| **1. `CD-1` & `CD-2` Final ACC** | Sudah dikumpulkan (`13 Okt` & `4 Nov 2026`) | **Terkunci Sementara** (`dokumen/cd1/`, `dokumen/cd2/`) | **Tidak direvisi sekarang.** Isi lama (`Kebun Besar`, `C-01..C-05`, `S-01..S-14`) dibiarkan utuh sebagai dokumen yang sudah dikumpulkan. |
| **2. Penyusunan `CD-3` (`CLO3 - CD3-1`)** | **Kamis, 10 Desember 2026** | **Belum Dibuat (Draf Lama Non-Aktif)** | Seluruh file `CD-3` yang ada di `dokumen/cd3/`, `dokumen/draf/cd3/`, dan isi lama `cd3_daffa/` adalah **draf lama tidak terpakai**. Saat mulai nanti (jangan dibuat dulu sebelum diminta), **`CD-3` dibuat baru dari awal** dan wajib menyertakan **catatan transisi perubahan lapangan (`Kebun Besar` → `Kebun Kecil`, `1 Zona = 4 Pohon`)** serta perbandingan 2 kebun ini agar nyambung dengan `CD-1` & `CD-2`. |
| **3. Gabungan `CD1–3 Final` & SemPro (`CLO4 - CD3-2`)** | **Kamis, 7 Januari 2027** *(SemPro: **11–16 Januari 2027**)* | **Rencana Konsolidasi Total** | Setelah `CD-1`, `CD-2`, dan `CD-3` terkumpul, seluruh bab digabung dan **dirombak total** (termasuk revisi `CD-1/CD-2` serta penyesuaian **judul proyek** bila mencakup pengoptimalan pertumbuhan & buah) agar naskah akhir SemPro bersih dan konsisten dari Bab 1–3. |

---

## 2. Alasan Lengkap Perpindahan Lokasi (`Kebun Besar` → `Kebun Kecil`, `1 Zona = 4 Pohon`)

Pemindahan lokasi dilakukan karena gabungan faktor teknis hidrolika, legalitas lahan sumber air, keamanan perangkat mahasiswa, keterbatasan anggaran, serta nilai riset agronomis yang jauh lebih tinggi di `Kebun Kecil`:

1. **Biaya & Cakupan `Kebun Besar` Melampaui Anggaran Mahasiswa (*Cost & Scope*):**  
   Tidak adanya listrik PLN dan jauhnya sumber air memaksa penggunaan panel surya (`PLTS`), baterai berkapasitas besar, dan pompa berdaya tinggi. Draf `BOM_PROTOTYPE` lama untuk `Kebun Besar` saja sudah menyentuh **`Rp4.850.000`** (`+ Support RAB Rp1.585.000 = Rp6.435.000`, dengan pos PLTS + baterai **`Rp2.020.000`**) dan itu pun baru sanggup melayani `1` petak uji (`15–24` pohon), sedangkan sisanya tetap mengandalkan `Alkon`.
2. **Kendala Jarak, Elevasi Curam, & Daya Pompa Tinggi dari Saluran Irigasi:**  
   Pada survei `Kebun Besar 1`, jarak dari saluran irigasi ke parit terdekat mencapai **`10 m`** dengan beda tinggi vertikal **`Δz = 4–5 m`** (`> batas hisap pompa kecil ~2 m`). Menarik air dari dasar saluran irigasi curam membutuhkan pompa bertekanan/daya tinggi yang boros energi dan mahal.
3. **Arus Saluran Irigasi Sewaktu-waktu Sangat Deras Saat Hujan:**  
   Kondisi debit dan arus saluran irigasi umum berfluktuasi ekstrem ketika turun hujan deras, sehingga berisiko menghanyutkan, merusak, atau menyumbat instalasi *intake* pompa mahasiswa.
4. **Saluran Irigasi Bukan Tanah Milik Mitra (Kendala Izin & Akses Pemasangan):**  
   Badan saluran irigasi umum berada di luar lahan milik mitra, sehingga tim maupun mitra sulit memasang dudukan pompa permanen, rumah pelindung, ataupun struktur pipa tetap secara bebas dan aman secara perizinan.
5. **Rawan Pencurian (*Security Risk*):**  
   `Kebun Besar` berada jauh dari permukiman warga dan tidak memiliki pagar permanen (hanya paranet hitam tipis). Menempatkan panel surya, baterai, mikrokontroler, katup, dan pompa tanpa penjagaan 24 jam terlalu berisiko tinggi hilang dicuri.
6. **Masalah Biaya & Tenaga Kerja di `Kebun Kecil` Masih Nyata Terjadi:**  
   Pindah ke `Kebun Kecil` tidak menghilangkan urgensi masalah utama proyek: sumber air sumur di `Kebun Kecil` saat ini masih menggunakan **pompa Alkon bensin** dan mitra tetap harus membayar **`2 pekerja × Rp100.000 = Rp200.000 / kegiatan`** setiap **`3–4 hari sekali` jika tidak ada hujan** (`~Rp18,2–24,3 juta/tahun` sebagai skenario hitungan tanpa hari hujan, belum termasuk BBM/servis Alkon), dengan acuan dosis air **`10–15 L / pohon`** yang masih sama.
7. **Daya Tarik Riset Pertumbuhan Pohon Tidak Merata & Visi Baru Mitra (Irigasi + Optimasi Pertumbuhan & Buah):**  
   Keempat pohon sampel di `Kebun Kecil` ditanam serentak (**umur `16 bulan`** di tanah merah urugan eks-empang/sampah), namun memperlihatkan ketimpangan tinggi hingga **`5,43×`** (`46 cm` cacat tidak berbuah vs `250 cm` berbuah lebat). Mitra justru **lebih menyukai `Kebun Kecil` diselesaikan terlebih dahulu sebagai kebun acuan/percontohan**. Jika berhasil di zona `4` pohon ini, sistem bukan hanya menggantikan pekerjaan penyiraman manual, melainkan juga memantau kondisi lingkungan tanah untuk **memaksimalkan pertumbuhan pohon dan produktivitas buah**. Konsekuensinya, ruang lingkup dan **judul proyek berpeluang diperbarui** saat penyusunan `CD1–3 Final`.

---

## 3. Perbandingan Detail `Kebun Besar` vs `Kebun Kecil`

### 3.1 Matriks Perbandingan Lapangan

| Aspek | Kebun Besar (`Kebun Besar 1` — Plot Lama `CD-1/CD-2`) | Kebun Kecil (`Kebun Belakang Rumah` — Lokasi ACC Baru) |
|---|---|---|
| **Status Saat Ini** | **Histori / Dasar `CD-1` & `CD-2` Lama** *(diarsipkan utuh, tidak untuk prototipe saat ini)* | **Lokasi Resmi ACC (`22 Nov 2026`)**, fokus **`1 Zona = 4 Pohon Sampel`** |
| **Lokasi & Keamanan** | Area persawahan terbuka jauh dari rumah warga; hanya paranet tipis; **rawan pencurian**. | Area permukiman; dikelilingi **pagar bambu + tembok rumah warga** + jalan cor desa; **aman**. |
| **Populasi & Skala Lahan** | Keterangan awal `500–600` pohon (terpecah beberapa plot); sensus riil `Kebun Besar 1` = **`160` pohon** (`4` baris, panjang `~117,5 m`). | `72–73` pohon jeruk limau pada luas terpagar **`~471 m²`** (`[Skala Drone ±5–7%]`), prototipe difokuskan pada **`1 Zona = 4 pohon`**. |
| **Sumber Air Utama** | Saluran irigasi umum di luar kebun (`bukan milik mitra`); jarak **`10 m`**, tebing **`Δz = 4–5 m`**, arus deras saat hujan. | **Sumur baru** di dalam pagar kebun milik mitra (`jarak P2–sumur = 12,27 m miring / 16,20 m siku`). *(Toren `75×75 cm` ada di lahan tetapi **tidak dipakai**.)* |
| **Parit & Kondisi Eksisting** | `3` parit tanah memanjang `±100 m` + penghubung melintang `+`. | `6` parit dangkal **`6 cm`** (utama lebar `40 cm`, kecil `25 cm`). |
| **Akses Listrik & Pompa** | **Tidak ada PLN** (harus PLTS + baterai mahal); pompa aktif `Alkon 2 inci Pertalite` *(LPG 3 kg pernah gagal/overheat)*. | **Listrik PLN tersedia** (dapat dipakai jika butuh) + **sumur saat ini masih disedot pakai `Alkon bensin`**. |
| **Upah & Jadwal Eksisting** | `4 pekerja × Rp100.000 = Rp400.000 / kegiatan` (`~3 hari sekali` skenario mitra → `~Rp48,7 jt/thn`; video pekerja `1×/minggu`). | **`2 pekerja × Rp100.000 = Rp200.000 / kegiatan`** setiap **`3–4 hari sekali` jika tidak ada hujan** (`~Rp18,2–24,3 jt/thn` skenario hitungan tanpa hujan). |
| **Acuan Kebutuhan Air** | `15 L / pohon` *(patokan lisan mitra; demo pekerja `~15 L`, ember `~7 L`)*. | **`10–15 L / pohon`** *(masih sama dengan acuan kebutuhan sebelumnya)*. |
| **Kondisi Tanah & Tanaman** | Lahan sawah terbuka; variasi umur/pertumbuhan antarpohon belum menjadi fokus utama `CD-1`. | Eks-empang & timbunan sampah diuruk tanah merah; **`4` pohon sampel seumur (`16 bln`) sangat timpang (`46–250 cm`)**. |
| **Estimasi Biaya Prototipe** | Berat untuk mahasiswa (`BOM` lama `Rp4,85 jt` / `+ RAB Rp6,435 jt` baru dapat `1` zona; PLTS `Rp2,02 jt`). | Jauh lebih hemat karena `1 zona = 4 pohon`, dekat sumber air sumur (`12,27 m`), dan opsi listrik PLN tersedia. |

### 3.2 Kelebihan & Kekurangan Masing-Masing Kebun

#### Kebun Besar (`Kebun Besar 1`)
- **Kelebihan:**
  1. Dampak ekonomi langsung berskala paling besar bila seluruh blok terotomasi (`4 pekerja × Rp100.000 = Rp400.000/kegiatan`), yang telah menjadi justifikasi ekonomi awal `CD-1` dan `CD-2`.
  2. Tata baris lebih seragam/lurus memanjang sehingga secara teoretis mudah dimodelkan dalam skenario pipa lajur panjang (`100 m`).
- **Kekurangan:**
  1. **Tidak ada listrik** dan **tanpa pagar keamanan** → komponen surya, baterai, sensor, dan kontroler sangat rawan dicuri serta melampaui anggaran mahasiswa.
  2. **Sumber air saluran irigasi sulit secara hidrolika dan legalitas:** tebing curam `4–5 m` (`10 m`), arus deras saat hujan, dan **lahan irigasi bukan milik mitra** sehingga sulit mengurus izin pemasangan instalasi permanen.
  3. **ROI prototipe kurang terasa langsung:** dengan anggaran mahasiswa, alat hanya sanggup melayani `1` zona kecil sementara `Alkon` dan pekerja tetap harus beroperasi untuk blok kebun lainnya.

#### Kebun Kecil (`Kebun Belakang Rumah` — Lokasi Terpilih)
- **Kelebihan:**
  1. **Aman & infrastruktur mendukung:** berpagar bambu + tembok rumah warga, dekat permukiman, **listrik PLN tersedia jika diperlukan**, serta **sumur berada di dalam lahan milik mitra** (tidak terkendala izin irigasi umum).
  2. **Masalah biaya operasional tetap valid:** penyedotan sumur masih memakai **Alkon bensin** dan membayar **`2 pekerja × Rp100.000 = Rp200.000` per `3–4 hari`** saat tidak hujan, dengan kebutuhan air **`10–15 L/pohon`**.
  3. **Kaya nilai riset & disukai mitra:** fokus `1 Zona = 4 Pohon Sampel` memungkinkan pemantauan detail ketimpangan pertumbuhan umur `16 bulan` (`46 cm` vs `250 cm`), bukan hanya mengotomasi air tetapi juga membantu **memaksimalkan pertumbuhan pohon dan buah** sehingga layak dijadikan percontohan (*benchmark*) sebelum direplikasi ke blok lain.
- **Kekurangan:**
  1. Cakupan awal prototipe lebih kecil (`4` pohon sampel dari `72–73` pohon), sehingga perlu narasi akademik yang kuat di `CD-3` dan `CD1–3` agar tetap memenuhi bobot kompleksitas dan justifikasi skalabilitas biaya.
  2. Nilai penghematan upah tahunan di `Kebun Kecil` (`Rp200.000/kegiatan` untuk `2` pekerja) lebih kecil dibanding asumsi `Kebun Besar` (`Rp400.000/kegiatan` untuk `4` pekerja), sehingga perhitungan kelayakan ekonomi dan *Payback Period* di `CD-3`/`CD1–3` wajib disesuaikan ulang secara realistis.
  3. Heterogenitas urugan eks-empang/sampah membuat respons kebutuhan air dan kesuburan tiap pohon tidak seragam, menuntut pembacaan sensor tanah dan analisis pertumbuhan yang lebih cermat.

---

## 4. Matriks Jembatan Perubahan `CD-2` → `CD-3` (Panduan Wajib Naskah `10 Des 2026` & Rombak Total `CD1–3`)

| Elemen | Ketentuan Lama (`CD-2 Final ACC`) | Kondisi Baru (`Kebun Kecil`, `1 Zona = 4 Pohon`) | Yang Harus Dicatat di `CD-3` (`10 Des 2026`) | Yang Dirombak Total Saat `CD1–3 Final` (`7 Jan 2027`) |
|---|---|---|---|---|
| **Judul & Tujuan Proyek** | Penyiraman manual untuk kebun jeruk limau skala `500–600` pohon (`Kebun Besar`). | Fokus awal prototipe pada `Kebun Kecil` (`1 Zona = 4 Pohon`) untuk mengatasi irigasi sekaligus **memaksimalkan pertumbuhan pohon & hasil buah**. | Tetap merujuk konteks transisi dari `CD-1/CD-2` dengan catatan subbab penjelasan perpindahan target ke `Kebun Kecil` & penambahan tujuan pemantauan pertumbuhan/buah. | **Finalisasi judul proyek baru** (bila disepakati pembimbing) serta penulisan ulang Latar Belakang & Rumusan Masalah Bab 1–2 agar selaras penuh. |
| **Lokasi & Sumber Air (`C-02` & `S-05`)** | Saluran irigasi umum `20,54 m`, tebing `4–5 m`, air sungai keruh saringan `>= 120 mesh`. | **Sumur baru** di dalam pagar kebun mitra (`jarak P2–sumur 12,27 m miring / 16,20 m siku`; toren `75×75 cm` tidak dipakai). | Cantumkan alasan penghentian desain *intake* irigasi (bukan tanah mitra, arus deras hujan, `Δz 4–5 m`) dan konversi suplai ke **sumur kebun**. | Sinkronkan seluruh diagram lokasi, topografi `Kebun Kecil` (`~471 m²`), dan peta denah 2D terbaru ke Bab 1 & Bab 2. |
| **Catu Daya (`C-01` & `S-06`)** | 100% *off-grid* (`PLTS` + baterai `LiFePO4`, cadangan `>= 8 jam`). | **Listrik PLN rumah tersedia & boleh digunakan jika dibutuhkan** *(opsi catu daya AC-DC berproteksi atau hibrid/cadangan hemat biaya)*. | Jelaskan opsi pemanfaatan PLN/catu daya aman berbiaya rendah sebagai adaptasi keamanan & efisiensi atas ketidaksiapan PLTS di lahan terbuka `Kebun Besar`. | Perbarui `C-01` dan `S-06` pada Bab 2 `CD-2` hasil gabungan agar konsisten dengan arsitektur daya terpilih. |
| **Cakupan Uji (`C-03`)** | Min. `1 lajur 15–20 pohon`, bentang `>= 25 m`, proyeksi modular `500–600 pohon`. | **`1 Zona = 4 Pohon Sampel`** (`keliling 10,30 m`; umur `16 bln`: `46/100/250/210 cm`), proyeksi modular ke `72–73` pohon `Kebun Kecil` lalu replikasi ke kebun mitra lain. | Tegaskan bahwa penyempitan `4` pohon di `CD-3` adalah unit uji presisi berbiaya efisien untuk studi komparatif pertumbuhan tanaman di lahan homogen semu. | Revisi klausul `C-03` dan kriteria desain pada Bab 2 agar unit uji `4` pohon + modul skalabilitas `72–73` pohon menjadi standar resmi. |
| **Spesifikasi Dosis & Sensor (`S-01..S-04`)** | Dosis `10–15 L ± 5%/pohon`, verifikasi *Flow Meter* & wadah tera (sensor tanah belum wajib). | Dosis acuan tetap **`10–15 L/pohon`**, ditambah kebutuhan **pemantauan parameter tanah & pertumbuhan** guna menjawab disparitas `5,43×` (`46` vs `250 cm`). | Rumuskan solusi arsitektur penyiraman presisi + sensor kondisi tanah di `CD-3` sebagai perluasan nilai tambah sistem (bukan sekadar timer). | Masukkan kebutuhan sensor tanah & indikator pertumbuhan pohon/buah ke matriks spesifikasi `S-01..S-14` pada gabungan `CD1–3`. |
| **Ekonomi & Kelayakan (`S-08..S-10`)** | Basis upah `Rp400 rb/siklus` (`4` orang), `CAPEX <= Rp5 jt` prototipe / `<= Rp18 jt` penuh. | Basis upah `Kebun Kecil` **`Rp200 rb/kegiatan`** (`2` orang setiap `3–4 hari` saat tak hujan) + penghematan BBM Alkon + potensi kenaikan hasil buah `> 2,5 thn` (`10–15 kg/pohon`). | Hitung ulang TCO, penghematan biaya pompa/buruh `Kebun Kecil`, dan nilai ekonomis dari perbaikan keseragaman pertumbuhan & panen pada analisis pemilihan solusi `CD-3`. | Rombak total Bab 1.2 & Bab 2 ekonomi agar angka `Rp200 rb/3–4 hari`, BBM Alkon, dan proyeksi hasil buah seragam dari awal sampai akhir. |

---

## 5. Rekap Fakta Terakhir `Kebun Kecil` (Snapshot Referensi Penulisan `CD-3`)

1. **Kondisi `4` Pohon Sampel (Umur Serentak `16 Bulan` di Tanah Merah Urugan Eks-Empang/Sampah):**
   - **Sampel 1 (`46 cm`):** kondisi tanaman **cacat / kerdil**, **tidak berbuah**; `P1 → P2 = 300 cm`.
   - **Sampel 2 (`100 cm`):** **banyak buah — bagus walaupun masih kecil**; titik acuan pengamat baju merah (`P2 → P3 = 210 cm`).
   - **Sampel 3 (`250 cm`):** **berbuah lebat — buah sudah dipanen/diambil**; tinggi `5,43×` Sampel 1 (`P3 → P4 = 290 cm`).
   - **Sampel 4 (`210 cm`):** **berbuah — buah sudah dipanen/diambil**; tajuk besar (`P4 → P1 = 230 cm`).
   - **Geometri Zona Uji 1:** keliling `10,30 m`; diagonal estimasi `P2–P4 ≈ 4,05 m`, `P1–P3 ≈ 3,27 m`. Target panen dewasa `> 2,5 tahun` menurut mitra: **`10–15 kg / pohon`** berbuah.
2. **Sumber Air, Jarak Sumur, & Energi:**
   - **Toren `75 × 75 cm`:** kapasitas liter tidak diketahui dan **tidak akan dipakai**.
   - **Sumber air aktif:** **sumur baru** (`ban kiri atas`), saat ini masih menggunakan **Alkon bensin**.
   - **Jarak acuan `P2 / Baju Merah` ke sumur (`[Ukur] + [Hasil Perhitungan]`):** lurus atas `11,2 m` + kiri `5,0 m` = **`16,20 m` jalur siku**, atau **`12,27 m` jarak lurus miring (Pythagoras)**.
   - **Listrik PLN:** **tersedia** di lokasi permukiman dan dapat dipakai apabila dibutuhkan oleh desain sistem.
   - **Biaya penyiraman manual berjalan:** **`2 pekerja × Rp100.000 = Rp200.000 / kegiatan`** tiap **`3–4 hari sekali` jika tidak ada hujan** (`~Rp18,2–24,3 juta/tahun` `[Hasil Perhitungan skenario tanpa hujan]`), kebutuhan air tetap **`10–15 L / pohon`**.
