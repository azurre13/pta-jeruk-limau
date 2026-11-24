# Data Kebun Kecil & Zona Uji 1 (`4 Pohon Sampel`) — Pasca-ACC Lokasi

**Tanggal Penyusunan:** 22 November 2026 *(Pembaruan lengkap hasil survei drone, status buah Sampel 1–4, sumur vs toren, biaya Alkon + 2 pekerja, listrik, & roadmap CD-3 → SemPro)*  
**Status Keputusan:** **ACC** oleh Pembimbing 1 (**Dr. Agung Nugroho Jati, S.T., M.T.**), Dosen Pengampu Kelas, dan Mitra untuk memindahkan lokasi target ke **`Kebun Kecil`** dengan cakupan prototipe **`1 Zona = 4 Pohon Sampel`**.  
**Status Naskah Akademik (`22 November 2026`):** Data lama `CD-1` (`26 hlm`) dan `CD-2` (`26 hlm`) **belum direvisi** pada tahap ini. Penyelarasan awal akan dituliskan sebagai catatan transisi pada **`CD-3` (tenggat `10 Desember 2026`)**, lalu seluruh naskah **`CD1–3 Final`** digabung & dirombak total untuk **SemPro PTA** (`CD3-2` `7 Januari 2027`).

**Lampiran Visual & Sumber Terkait:**
- README Transisi & Perbandingan 2 Kebun (`CD-2` → `CD-3`): [README_TRANSISI_KEBUN_BESAR_KE_KEBUN_KECIL_CD2_CD3.md](README_TRANSISI_KEBUN_BESAR_KE_KEBUN_KECIL_CD2_CD3.md)
- Peta Denah 2D Berskala (PNG): [denah_kebun_kecil_2d.png](denah_kebun_kecil_2d.png)
- Sumber Vektor SVG Denah: [denah_kebun_kecil_2d.svg](denah_kebun_kecil_2d.svg)
- Skema Pemipaan, 4 Katup Cabang, & Jalur Ekspansi: [skema_pipa_zona_4_pohon.png](skema_pipa_zona_4_pohon.png) ([SVG](skema_pipa_zona_4_pohon.svg))
- Diagram Blok Sistem (Hitam-Putih): [diagram_blok_sistem_kebun_kecil.png](diagram_blok_sistem_kebun_kecil.png) ([SVG](diagram_blok_sistem_kebun_kecil.svg))
- Flowchart Cara Kerja Sistem (Hitam-Putih): [flowchart_sistem_kebun_kecil.png](flowchart_sistem_kebun_kecil.png) ([SVG](flowchart_sistem_kebun_kecil.svg))
- Daftar Alat, Bahan, & RAB 2 Fase (`Kebun Kecil`): [DAFTAR_ALAT_DAN_RAB_CD3_KEBUN_KECIL.md](DAFTAR_ALAT_DAN_RAB_CD3_KEBUN_KECIL.md)
- Transkrip Rekaman Survei Kebun Kecil (`22 Nov 2026`): [transkrip_survey_limau.md](../sumber/dokumentasi/kebon%20kecil/Record%20survey%2022%20Nov/transkrip_survey_limau.md)
- Catatan Survei Sebelumnya (`15 Nov 2026`): [HASIL_SURVEI_CIBERES_15_NOV_2026.md](HASIL_SURVEI_CIBERES_15_NOV_2026.md)
- Isian Lapangan: [CHECKLIST_SURVEI_MITRA_CIBERES.md](CHECKLIST_SURVEI_MITRA_CIBERES.md)
- Folder Media Kebun Kecil: `../sumber/dokumentasi/kebon kecil/` *(foto darat `15 Nov 2026`: `IMG_20261115_132905..133216.jpg`, `pipa sumur baru bangun.jpg`, `tampk depan`, `toren`, `dari depn.mp4`, `dari ujung blkng.mp4`; serta foto & video drone `22 Nov 2026`: `Drone viem 4 sampel pohon test.JPG`, `drone view semua kebun kecil.JPG`, `drone view semua kebun dari tengah harusny.JPG`, dan folder `Foto dan video dari drone/`)*

> [!IMPORTANT]
> **Pemisahan Jenis Fakta:**  
> Dokumen ini memisahkan secara tegas `[Ukur]` (pengukuran meteran tim di lapangan), `[Keterangan Mitra/Tim]` (penjelasan lisan mitra atau catatan tim), `[Observasi Visual]` (tampak langsung pada foto/video), `[Hasil Perhitungan]` (turunan matematis), dan `[Skala Drone]` (estimasi dimensi dari kalibrasi foto drone nadir dengan toleransi ±5–7%).

---

## 1. Latar Belakang ACC & Justifikasi Fokus `1 Zona = 4 Pohon`

1. **Pemindahan Lokasi dari `Kebun Besar` ke `Kebun Kecil`:**  
   Hasil survei `15 November 2026` memperlihatkan kendala lapangan berat di `Kebun Besar 1` (jarak irigasi `10 m` dengan tebing curam `Δz = 4–5 m`, tanpa pagar, rawan pencurian, dan perkiraan biaya surya + baterai tinggi untuk hanya 1 petak uji sementara pompa Alkon tetap terpakai di blok lain). Dengan persetujuan PBB 1, Dosen Pengampu, dan Mitra, target prototipe resmi dipindahkan ke **`Kebun Kecil`** (`Kebun Belakang Rumah`, Ciberes, Subang) yang berpagar, aman, dekat jaringan listrik rumah warga, dan memiliki sumber air sumur/toren di dalam plot.
2. **Alasan Penyempitan Cakupan ke `1 Zona = 4 Pohon Sampel`:**
   - **Efisiensi Biaya Mahasiswa:** Fokus instrumentasi, aktuasi, dan pemipaan terkonsentrasi pada `4` pohon berdekatan (keliling `10,30 m`) sehingga anggaran prototipe jauh lebih terukur dibandingkan mencakup seluruh `72–73` pohon sekaligus.
   - **Basis Riset Jangka Panjang (*Longitudinal Testbed*):** Keempat pohon sampel ditanam **serentak pada umur yang sama (`16 bulan`)** di lahan bekas empang dan timbunan sampah urugan yang telah ditutup tanah merah, namun tumbuh sangat timpang (`46 cm` hingga `250 cm`). Variasi kontras dalam satu petak kecil ini menjadikannya sampel ideal untuk pemantauan tanah/lengas dan pengujian dosis penyiraman presisi jangka panjang sebelum sistem direplikasi ke pohon lainnya.

---

## 2. Data Populasi & Infrastruktur Umum `Kebun Kecil`

| Parameter | Nilai / Kondisi | Klasifikasi Sumber | Catatan |
|---|---|---|---|
| **Jumlah Pohon Jeruk Limau** | `72` pohon *(catatan lapangan)* / `~73` pohon *(penyebutan tim)* | `[Keterangan Mitra/Tim]` | Selain jeruk limau, tampak beberapa pohon pisang dan `1` pohon kelapa di dekat pagar timur/kiri pada citra drone. |
| **Jumlah & Ukuran Parit** | `6` parit dangkal (`dalam 6 cm`); parit utama lebar `40 cm`, parit kecil lebar `25 cm`, pipa ke parit `170 cm` | `[Ukur]` | Data catatan survei `15 Nov 2026`; alur pemberian air sebelumnya masih manual. |
| **Jarak Tanam Contoh (Baris 5 Pohon)** | `290 cm`, `290 cm`, `290 cm`, `290 cm`; jarak antar-batang terdekat `120 cm` & `100 cm` (`2` pasang) | `[Ukur]` | Tercatat pada lembar `CHECKLIST_SURVEI_MITRA_CIBERES.md`. |
| **Toren & Sumber Air Sumur** | Terdapat toren `75 × 75 cm` *(volume liter tidak diketahui dan **tidak akan dipakai**)*; sumber air langsung dari **sumur baru** (`ban kiri atas`) yang saat ini masih disedot pakai **pompa Alkon bensin** | `[Ukur]`, `[Observasi Visual]`, & `[Keterangan Mitra/Tim]` | Tampak pada `toren`, `pipa sumur baru bangun.jpg`, dan `drone view semua kebun kecil.JPG`. |
| **Biaya & Pola Penyiraman Eksisting** | **`2 pekerja × Rp100.000 = Rp200.000 / kegiatan`** setiap **`3–4 hari sekali` jika tidak ada hujan** (`~Rp18,2–24,3 jt/thn` `[Hasil Perhitungan skenario tanpa hujan]`); dosis air tetap **`10–15 L / pohon`** | `[Keterangan Mitra/Tim]` & `[Hasil Perhitungan]` | Masalah *cost* & tenaga kerja tetap ada walau pindah dari `Kebun Besar`. |
| **Riwayat Lahan** | Bekas empang / timbunan sampah yang sudah diuruk tanah merah | `[Keterangan Mitra/Tim]` | Terlihat sisa lahan abu/urugan dan makam di luar pagar sisi barat (`kanan` pada foto drone). |
| **Keamanan & Akses Energi** | Berpagar bambu + tembok rumah warga, dekat jalan cor desa; **listrik PLN tersedia dan dapat digunakan jika dibutuhkan** | `[Observasi Visual]` & `[Keterangan Mitra/Tim]` | Jauh lebih aman dari pencurian dibanding `Kebun Besar` yang tanpa listrik, jauh dari permukiman, & tidak berpagar. |

---

## 3. Data Terukur Zona Uji 1 (`4 Pohon Sampel`, Umur `16 Bulan`)

Keempat pohon sampel ditanam serentak (**umur `16 bulan`**) di atas tanah urugan merah eks-empang/sampah. Foto tampak samping memperlihatkan posisi **`Sampel 2`** di kiri depan, **`Sampel 1`** di kanan depan, **`Sampel 3`** di belakang `Sampel 2`, dan **`Sampel 4`** di belakang `Sampel 1`.

### 3.1 Tinggi Tanaman & Status Berbuah

| Identitas | Tinggi (`16 Bulan`) | Kondisi Buah | Posisi Relatif pada Foto Drone Nadir | Sumber |
|---|---|---|---|---|
| **Sampel 1** | **`46 cm`** | **Cacat / kerdil, tidak berbuah** | Sisi kanan dari `Sampel 2` (di samping pengamat pada foto samping) | `[Ukur]`, `[Keterangan Mitra/Tim]`, & `[Observasi Visual]` |
| **Sampel 2** | **`100 cm`** | **Banyak buah — bagus walaupun masih kecil** | Titik acuan posisi pengamat berbaju merah (`depan kiri` pada foto samping) | `[Ukur]`, `[Keterangan Mitra/Tim]`, & `[Observasi Visual]` |
| **Sampel 3** | **`250 cm`** | **Berbuah lebat *(buah sudah dipanen/diambil)*** | Di depan `Sampel 2` *(ke arah atas foto drone)*; **`5,43×`** tinggi `Sampel 1` | `[Ukur]`, `[Keterangan Mitra/Tim]`, & `[Observasi Visual]` |
| **Sampel 4** | **`210 cm`** | **Sudah berbuah *(buah sudah dipanen/diambil)*** | Kanan depan dari `Sampel 2` *(belakang kanan pada foto samping)*; bertajuk besar | `[Ukur]`, `[Keterangan Mitra/Tim]`, & `[Observasi Visual]` |

### 3.2 Jarak Antar-Pohon & Geometri Segi Empat Zona Uji

| Ruas / Parameter | Nilai | Metode / Sumber |
|---|---|---|
| `Pohon 1` ke `Pohon 2` | **`300 cm`** (`3,00 m`) | `[Ukur]` |
| `Pohon 2` ke `Pohon 3` | **`210 cm`** (`2,10 m`) | `[Ukur]` |
| `Pohon 3` ke `Pohon 4` | **`290 cm`** (`2,90 m`) | `[Ukur]` |
| `Pohon 4` ke `Pohon 1` | **`230 cm`** (`2,30 m`) | `[Ukur]` |
| **Keliling Segi Empat Zona Uji** | **`10,30 m`** (`1030 cm`) | `[Hasil Perhitungan]` |
| **Diagonal `Pohon 2 – Pohon 4`** | `≈ 4,05 m` *(irisan segitiga/lingkaran)* vs `~4,02 m` *(foto drone detail)* | `[Hasil Perhitungan]` & `[Skala Drone]` |
| **Diagonal `Pohon 1 – Pohon 3`** | `≈ 3,27 m` *(irisan segitiga/lingkaran)* vs `~3,26 m` *(foto drone detail)* | `[Hasil Perhitungan]` & `[Skala Drone]` |

### 3.3 Patokan Hasil Panen Mitra

- **Patokan Panen Mitra:** **`10–15 kg / pohon`** untuk tanaman yang sudah berbuah pada umur **`> 2,5 tahun`** (`[Keterangan Mitra/Tim]`).
- *Catatan batas klaim:* Angka `10–15 kg/pohon` merupakan keterangan target/patokan mitra untuk pohon dewasa `> 2,5 tahun`, bukan hasil timbang aktual keempat pohon sampel yang saat ini masih berumur `16 bulan`.

---

## 4. Jarak Sumber Air (`Sumur Baru`) ke Zona Uji 1 (Pythagoras)

Titik acuan pengamat (**baju merah**) berada di sisi `Pohon 2` (pada foto drone keseluruhan, pusat objek baju merah terukur `~1,0 m` di sebelah kiri batang `Pohon 2`), sedangkan sumur baru berada pada titik **ban kiri atas** (`drone view semua kebun kecil.JPG`):

| Komponen Jalur | Nilai | Dasar Penentuan |
|---|---|---|
| **Garis Lurus Vertikal Foto** *(Baju Merah / `P2` → garis sejajar sumur)* | **`11,2 m`** | `[Ukur]` |
| **Garis Horizontal Foto** *(ke kiri menuju sumur / ban kiri atas)* | **`5,0 m`** | `[Ukur]` |
| **Total Panjang Jalur Siku (`L-path`)** | **`16,20 m`** (`11,2 + 5,0`) | `[Hasil Perhitungan]` |
| **Jarak Lurus Miring (Pythagoras)** | **`12,27 m`** ($\sqrt{11{,}2^2 + 5{,}0^2} = \sqrt{150{,}44} \approx 12{,}265\text{ m}$) | `[Hasil Perhitungan]` |

*Implikasi pemipaan awal:* Jarak lurus `12,27 m` menjadi dasar perhitungan *head loss* garis terpendek, sedangkan rute pipa lapangan kemungkinan mengikuti kontur/tepi parit berbentuk siku (`~16,2 m`) ditambah margin belokan (`elbow`) dan pencabangan ke `4` pohon sampel.

---

## 5. Kalibrasi Skala Foto Drone Nadir & Dimensi Kebun Kecil

Kalibrasi dilakukan menggunakan metadata EXIF/XMP dari `3` foto nadir (`GimbalPitch = -90°`) kamera drone **DJI Mini 4 Pro (`FC8482`, resolusi `4032 × 2268 px`)**:

1. **`Drone viem 4 sampel pohon test.JPG`** — `RelativeAltitude = +16,80 m`, `DigitalZoom = 1,38×`, `GimbalYaw = +177,1°`, koordinat `(-6.381836°, 107.568375°)` → skala detail Zona Uji **`~322,9 px/m`** (`0,310 cm/px`), memvalidasi proporsi geometri `4` pohon sampel (`P2–P4 ~4,02 m`, `P1–P3 ~3,26 m`, selisih `< 0,8%` terhadap hasil perhitungan irisan jarak meteran).
2. **`drone view semua kebun kecil.JPG`** — `RelativeAltitude = +58,20 m`, `DigitalZoom = 1,17×`, `GimbalYaw = +173,7°`, koordinat `(-6.381862°, 107.568361°)` → skala kalibrasi kebun penuh **`~65,87 px/m` (`1,518 cm/px`)** sebagai nilai tengah antara skala keliling `4` pohon (`67,82 px/m`) dan jarak miring ke sumur (`63,92 px/m`).
3. **`drone view semua kebun dari tengah harusny.JPG`** — `RelativeAltitude = +48,60 m`, `DigitalZoom = 1,00×`, `GimbalYaw = +176,2°`, koordinat `(-6.381842°, 107.568374°)` → mengonfirmasi orientasi penuh batas pagar, jalan cor desa, bangunan rumah, dan lahan luar sebelah kanan.

- **Orientasi Kompas Citra Drone (`GimbalYaw ≈ +174° s.d. +177°`):**  
  Bagian **ATAS foto = Selatan (`S`)**, **BAWAH foto = Utara (`U`)**, **KIRI foto = Timur (`T`)**, dan **KANAN foto = Barat (`B`)**.
- **Perkiraan Ukuran Lahan Terpagar `Kebun Kecil` (`[Skala Drone ±5–7%]`):**
  - Lebar sisi atas *(sisi selatan / dekat gang & deretan rumah)*: **`~18,7 m`** *(rentang `18,2–19,3 m`)*
  - Lebar sisi bawah *(sisi utara / jalan cor desa)*: **`~19,9 m`** *(rentang `19,3–20,5 m`)*
  - Panjang sisi kiri *(sisi timur / jalan cor desa melengkung)*: **`~24,8 m`** *(rentang `24,1–25,5 m`)*
  - Panjang sisi kanan *(sisi barat / pagar bambu batas lahan urugan & makam)*: **`~24,4 m`** *(rentang `23,7–25,2 m`)*
  - **Perkiraan Luas Lahan Terpagar:** **`~471 m²`** *(rentang kalibrasi penuh `~448–504 m²`, rata-rata lebar × panjang `~19,3 m × 24,6 m`)*.

Sketsa lengkap skala penuh kebun, orientasi kompas, posisi sumur, segitiga Pythagoras, detail 4 pohon sampel, dan ringkasan masalah disajikan pada **[denah_kebun_kecil_2d.png](denah_kebun_kecil_2d.png)** (sumber vektor: **[denah_kebun_kecil_2d.svg](denah_kebun_kecil_2d.svg)**).

---

## 6. Masalah Baru yang Muncul & Fokus Rekayasa Selanjutnya

1. **Disparitas Pertumbuhan Ekstrem (`5,43×`) pada Lahan Urugan Homogen Semu:**  
   Meskipun seluruh tanaman berumur `16 bulan` dan lahan eks-empang/sampah sudah diuruk tanah merah, `Sampel 1` cacat (`46 cm`, tidak berbuah), `Sampel 2` (`100 cm`) berbuah banyak meski ukuran buah masih kecil, sedangkan `Sampel 3` (`250 cm`) dan `Sampel 4` (`210 cm`) sudah berbuah hingga dipanen. Hal ini mengindikasikan **heterogenitas kondisi sub-permukaan tanah** (pemadatan urugan, kapasitas simpan lengas, pH/unsur hara, atau drainase mikro).
2. **Visi Baru Mitra: Bukan Hanya Irigasi, Melainkan Memaksimalkan Pertumbuhan Pohon & Buah:**  
   Mitra lebih memilih `Kebun Kecil` diselesaikan terlebih dahulu agar menjadi **kebun acuan**. Jika zona uji `4` pohon ini berhasil, sistem tidak sekadar menyiram `10–15 L/pohon` untuk menekan upah `Rp200.000 / 3–4 hari` dan pemakaian `Alkon bensin`, tetapi juga mendukung pemantauan faktor tumbuh guna **memaksimalkan pertumbuhan pohon dan produktivitas buah** (termasuk kemungkinan penyesuaian judul proyek saat gabung-rombak total **`CD1–3 Final`**).

---

## 7. Roadmap Dokumentasi & Data Teknis Terbuka Menuju `CD-3` (`10 Des 2026`)

1. **Strategi Dokumen Akademik (Disepakati `22 Nov 2026`):** `CD-1` dan `CD-2` dibiarkan tetap seperti versi yang sudah dikumpulkan; pada **`CD-3` (`tenggat 10 Des 2026`)** disertakan **catatan transisi** ([README_TRANSISI_KEBUN_BESAR_KE_KEBUN_KECIL_CD2_CD3.md](README_TRANSISI_KEBUN_BESAR_KE_KEBUN_KECIL_CD2_CD3.md)) agar nyambung ke `CD-2`; setelah `CD-1`, `CD-2`, dan `CD-3` terkumpul semua, ketiganya akan **digabung dan dirombak total menjadi `CD1–3 Final`** untuk **SemPro PTA** (`7 Jan 2027`).
2. **Keputusan Arsitektur Daya & Hidrolika Sumur Sebelum Implementasi `CD-3`:** karena listrik PLN tersedia dan toren `75×75 cm` **tidak dipakai**, desain `CD-3` perlu memutuskan spesifikasi pompa air sumur (menggantikan atau melengkapi `Alkon` pada sumur baru), pemilihan adaptor/PSU DC berproteksi dari listrik PLN vs PLTS mini, serta paket sensor tanah untuk `4` pohon sampel.
