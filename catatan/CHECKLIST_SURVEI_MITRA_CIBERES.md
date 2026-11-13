# Checklist Survei Lapangan & Verifikasi Data Kurang — Kebun Jeruk Limau Mitra Ciberes

**Tanggal Pembaruan:** 14 November 2026  
**Dokumen Kajian Terkait:** [Kajian Sumber Air Irigasi & Pompa](KAJIAN_SUMBER_AIR_IRIGASI_DAN_POMPA.md) · [Paparan Solusi untuk Mitra](PAPARAN_SOLUSI_UNTUK_MITRA.md)  
**Tujuan Dokumen:** Menjadi panduan langkah demi langkah tim Capstone saat turun ke kebun jeruk limau mitra di **Ciberes, Subang** (kunjungan Minggu) agar **tidak ada satu pun data fisik, agronomi, hidrolika, ekonomi, maupun kebutuhan pekerja yang terlewat** sebelum penguncian arsitektur pompa & ukuran pipa di **CD-3** dan persiapan fabrikasi/uji **CD-4**.

> [!IMPORTANT]
> **Aturan Keras Pencatatan di Lapangan (Wajib Ditaati Tim):**
> 1. **Pisahkan Lokasi Secara Ketat:** Seluruh angka pada formulir ini khusus untuk **kebun jeruk limau di tepi sungai/irigasi (`JH7H+222`)**. **JANGAN** mencampurkan kondisi kebun belakang rumah (bekas empang/urukan/kotak resapan) ataupun kebun sayuran **terong/kembang kol** (jarak ±500 m–1 km, uraian Urea/luas bata) ke lembar catatan kebun jeruk.
> 2. **Bedakan Perkiraan Lisan vs Hasil Ukur:** Tandai dengan jelas angka yang masih berupa ucapan mitra (`[Ucap]`) vs hasil pengukuran alat langsung di lokasi (`[Ukur]`). Angka acuan `15 L/pohon` belum dianggap volume aktual sampai ember ditera dan guyuran dihitung.
> 3. **Rekonsiliasi Batasan Purwarupa `C-03` CD-2:** Draf [CD3_Jeruk_Limau_Usulan.pdf](../dokumen/draf/cd3_daffa/CD3_Jeruk_Limau_Usulan.pdf) sementara memodelkan petak uji `20 m × 3 baris` (~24 pohon contoh), sedangkan syarat [CD 2 final](../dokumen/cd2/CD%202%20-%20ANALISIS%20PERMASALAHAN%20PENYIRAMAN%20MANUAL%20PADA%20KEBUN%20JERUK%20LIMAU%20DI%20CIBERES%20SUBANG.pdf) `C-03` mensyaratkan minimal **1 lajur 15–20 pohon pada bentang operasional >= 25 m**. Oleh karena itu, **jarak tanam nyata dan panjang baris petak uji wajib diukur presisi pada kunjungan ini** sebelum memotong/membeli pipa.

---

## 0. Informasi Kunjungan (Isi di Lokasi)

- **Tanggal & Jam Survei:** `____ / ____ / 2026` (`____:____` – `____:____` WIB)
- **Tim Mahasiswa yang Turun:** `[ ]` Muhammad Al Qarnie  `[ ]` Maheswara Ariq Athallah  `[ ]` Daffa Hermansyah
- **Cuaca Saat Tiba & Riwayat Hujan 3 Hari Terakhir:** `___________________________` *(kering / habis hujan kemarin / gerimis)*
- **Koordinat GPS Titik Tengah Kebun / Sungai:** `___________________________`

---

## 1. Persiapan Alat Bawaan dari Bandung (Cek Sebelum Berangkat)

- [ ] **Meteran gulung panjang (>= 30 m atau 50 m)** + **meteran tukang/baja 5 m** *(ukur panjang baris 100 m, jarak sungai, lebar kebun, jarak tanam, dan dimensi parit)*.
- [ ] **Tali rafia / patok bambu & lakban warna (min. 6 patok)** *(menandai batas fisik calon petak uji `20–30 m × 3 baris` agar difoto dan disepakati langsung dengan pemilik)*.
- [ ] **Selang air bening / waterpass sederhana (`10–15 m`) + penggaris/tongkat ukur** *(mengukur beda tinggi/`Δz` permukaan air sungai ke permukaan bedengan kebun)*.
- [ ] **Wadah tera / gelas ukur `1.000 mL` (1 L) + ember ukur diketahui volumenya (`>= 10–20 L`)** *(kalibrasi kapasitas ember hitam pekerja + uji infiltrasi `15 L` di piringan akar + uji taksir debit pompa Alkon)*.
- [ ] **Stopwatch HP / digital & kalkulator** *(mengukur lama isi ember, lama guyur per pohon, waktu pompa Alkon, dan laju surutnya air parit)*.
- [ ] **Sekop kecil / cetok / bor tanah mini** *(menggali lubang cek kedalaman akar 20–40 cm + mengambil sampel tanah)*.
- [ ] **4× Kantong plastik ziplock + spidol permanen** *(membawa pulang `~1–2 kg` sampel tanah liat zona perakaran kedalaman 15–30 cm untuk uji lab & kalibrasi sensor `Capacitive v1.2`)*.
- [ ] **2× Botol air bening bersih `600 mL` / `1.000 mL`** *(sampel air Sungai Ciberes & air Parit untuk uji kekeruhan/filtrasi `120 mesh` + cek TDS/EC di lab)*.
- [ ] **Multimeter + Aplikasi Kompas/Matahari di HP** *(cek orientasi Utara-Selatan kebun dan potensi bayangan naungan panel surya pukul 08.00–16.00)*.
- [ ] **Berkas cetak**: dokumen ini + [PAPARAN_SOLUSI_UNTUK_MITRA.md](PAPARAN_SOLUSI_UNTUK_MITRA.md) + gambar `fig1_arsitektur_sistem.png` & `fig2_denah_petak_uji_20m.png` + lembar persetujuan/MoM mitra.

---

## 2. Pos A — Identitas Mitra, Izin Lahan & Kebutuhan Pekerja (Tutup Gap Kriteria 6 CD-1)

*Mengisi kekosongan data identitas usaha pada `CD-1/CD-2/CD-3` dan memvalidasi apakah Kriteria 6 (dampak sosial/peran pekerja) serta `S-13` (kemudahan operasi buruh) dapat dipenuhi secara objektif.*

### A.1 Identitas Resmi & Riwayat Kunjungan Sebelumnya
- [ ] Nama lengkap pemilik / pengelola kebun yang berwenang: `___________________________`
- [ ] Nama usaha / kelompok tani (bila ada; jika kebun keluarga perorangan, catat apa adanya): `___________________________`
- [ ] Nomor HP/WA koordinator lapangan yang bisa dihubungi tim: `___________________________`
- [ ] **Izin pencantuman nama mitra** di laporan akademik & lembar persetujuan Capstone (CD-1 s.d. CD-4): `[ ] Diizinkan dicantumkan penuh`  `[ ] Hanya inisial/jabatan`
- [ ] Konfirmasi tanggal pengambilan foto awal `P1/P2` & rekaman Audio 1/2 terdahulu (bila masih tersimpan di WA): `___________________________`

### A.2 Wawancara Pekerja Kebun (`4 Pekerja Penyiraman` — Jangan Dicampur Pekerja Panen/Kebun Sayuran!)
- [ ] Status ke-4 pekerja penyiraman: `[ ] Pekerja harian lepas khusus siram`  `[ ] Pekerja kebun tetap yang merangkap (panen, penyiangan, pupuk, semprot)`
- [ ] Pembagian peran aktual saat menyiram:
  - Siapa yang menyalakan/menunggu pompa bensin Alkon (Pertalite) di tepi sungai/saluran irigasi? `___________________________`
  - Siapa saja yang menimba & mengguyur (apakah dibagi per parit/baris)? `___________________________`
- [ ] Jam kerja nyata untuk 1 siklus penuh `500–600 pohon`: mulai pukul `______` s.d. `______` WIB (istirahat `____` mnt) -> total durasi efektif `____` jam.
- [ ] Bagaimana jadwal menyiram berubah saat musim hujan vs kemarau? (Misal: kemarau benar-benar tiap `3 hari sekali`, musim hujan jeda `____ hari` atau hanya jika kering `____ hari`?) `___________________________`
- [ ] Tingkat literasi / kenyamanan pekerja terhadap antarmuka alat:
  - Bisa membaca petunjuk bergambar sederhana & membedakan warna lampu LED (Hijau / Merah / Kuning)? `[ ] Ya`  `[ ] Perlu pendampingan`
  - Bila guyur manual digantikan irigasi otomatis 1 tombol, **ke mana peran pekerja diarahkan** agar mitra tetap terbantu dan tidak timbul penolakan sosial? (misal: fokus pemangkasan, pemupukan, panen, babat rumput, plus tugas kontrol 1 tombol & bilas filter `< 20 mnt/bln`) `___________________________`
- [ ] Kesan pekerja mengenai **beban terberat** kerja saat ini (angkat ember saat parit dangkal, bungkuk, licin di tebing parit, gangguan pompa mati, dll.): `___________________________`

---

## 3. Pos B — Sumber Air Saluran Irigasi/Sungai, Elevasi (`Head`), Arus, & Kualitas Air (`C-02`, `S-05`)

*Data ini menentukan keputusan arsitektur sumber air ([Kajian Sumber Air & Pompa](KAJIAN_SUMBER_AIR_IRIGASI_DAN_POMPA.md)), posisi fisik pompa (kebun atas vs bantaran), ukuran kabel DC `12 V`, proteksi arus saat hujan, dan ketahanan `Disc Filter 120 mesh`.*

### B.1 Identitas Saluran, Jarak & Beda Ketinggian (`Head Statis`)
- [ ] Jenis & status pengelola badan air besar di tepi kebun: `[ ] Sungai alami`  `[ ] Saluran irigasi teknis/sekunder (PU / PJT II)`  `[ ] Kali/saluran irigasi tersier`
- [ ] **Izin penempatan *intake*:** Apakah pemasangan selang hisap dalam kurungan pipa penahan arus (*stilling pipe cage*) di tebing diperbolehkan pengelola saluran/desa/mitra, atau harus portabel bongkar-pasang? `___________________________`
- [ ] **Jarak lintasan pipa/kabel nyata** *(bukan garis lurus Google Maps `20,54 m`!)* mengikuti kontur tebing & bantaran motor:
  - Dari **titik hisap dalam air** ke **bibir bantaran bawah (tempat motor/kotak pompa darurat)**: `________ m`
  - Dari **bibir bantaran bawah** naik ke **titik aman panel surya & kotak kontrol di Zona 1 kebun atas**: `________ m`
  - **Total panjang jalur *mainline* air -> *header***: `________ m` *(dibandingkan dengan `31 m` di draf BOM purwarupa)*
- [ ] **Ukur beda tinggi vertikal (`Δz` / *static head* dengan selang *waterpass*):**
  - Tinggi permukaan air saat surut sekarang ke **bibir bantaran bawah** (`Δz1`): **`________ m`**
  - Tinggi **bibir bantaran bawah** ke **permukaan bedengan kebun atas** (`Δz2`): **`________ m`**
  - **Total tinggi hisap jika pompa ditaruh aman di kebun atas (`Δz1 + Δz2`)**: **`________ m`** *(kunci keputusan: bila `<= 1,5–2,0 m`, pompa DC aman ikut di kebun atas; bila `> 2,0 m`, pompa perlu ditaruh di boks aman bantaran bawah dengan kabel DC `2×4–6 mm²`!)*
  - Cek tanda batas **muka air banjir tertinggi** & kekuatan arus tebing saat hujan deras (`± ________ cm` dari muka air sekarang / sejajar bantaran motor?): `___________________________`

### B.2 Ketersediaan Air Kemarau, Arus, & Mutu Air
- [ ] Apakah aliran saluran irigasi/sungai pernah **dikeringkan / digilir (tutup pintu irigasi) / surut ekstrem** di puncak kemarau? Kapan bulannya, berapa hari/minggu paling lama keringnya, dan apakah parit kebun juga ikut kering? `___________________________`
- [ ] **Kelayakan Opsi Cadangan Tampungan (bila irigasi digilir kering atau dilarang pasang intake):** Apakah di ujung petak atas tersedia ruang aman untuk kolam terpal kecil / sekat parit berlapis terpal? `___________________________`
- [ ] Kondisi fisik air langsung di titik hisap:
  - Warna/kekeruhan: `[ ] Jernih`  `[ ] Keruh cokelat muda`  `[ ] Keruh pekat berlumpur`
  - Sampah/kotoran & kecepatan arus perkiraan: `[ ] Banyak daun/ranting`  `[ ] Plastik/lumut`  `[ ] Pasir dasar kasar` | Arus normal/hujan: `___________________________`
  - Jarak vertikal dari dasar saluran yang aman menggantung *foot valve* di dalam kurungan pancang (`target 30–50 cm` di atas lumpur dasar): `________ cm` dari dasar.
- [ ] **Ambil 2 botol sampel air** (`1 L` sungai + `600 mL` parit setelah dipompa) berlabel tanggal & titik -> bawa ke laboratorium Telkom!
- [ ] Konfirmasi teknis PLN terakhir (`C-01`): berapakah jarak tiang PLN terdekat yang terlihat (misal ke rumah di gambar `L`) dari titik pompa sungai? **`________ m`** *(hanya sebagai catatan argumen biaya tarikan tiang PLN mahal vs PLTS 100 Wp)*.

---

## 4. Pos C — Pemetaan Geometri Kebun, Parit 1–2–3 + Melintang (`+`), & Sensus Pohon (`C-03`)

*Mengakhiri ketidakpastian angka `117,52 m`, lebar `6 m` vs `25–30 m`, panjang parit `~100 m`, dan jumlah populasi `500–600 pohon`, sekaligus menguji kelayakan jalur alternatif robot.*

### C.1 Tata Letak Makro & Arah Orientasi
- [ ] Gambar sketsa denah kebun pada selembar kertas kotak-kotak (foto hasilnya!), wajib beri panah **Utara** dan posisi **Sungai/Saluran Irigasi** terhadap `Baris 1`, `Baris 2`, `Baris 3`.
- [ ] Hitung jumlah **keseluruhan baris pohon memanjang** yang ada di kebun jeruk ini *(apakah betul tepat 3 baris pohon sejajar 3 parit seperti skema `Baris 1 – Parit 1 – Baris 2 – Parit 2 – Baris 3 – Parit 3`, atau ada baris ke-4 dst.?)*:
  - Jumlah baris pohon total: `________` baris
  - **Sensus jumlah pohon per baris (hitung nyata satu per satu / tanda kapur):**
    - Baris 1: `____` pohon *(pohon kosong/mati `____` titik)*
    - Baris 2: `____` pohon *(pohon kosong/mati `____` titik)*
    - Baris 3: `____` pohon *(pohon kosong/mati `____` titik)*
    - Baris lainnya (bila ada): `__________________________________`
    - **TOTAL POPULASI RIIL TERHITUNG:** **`________` pohon hidup** + **`________` titik kosong** *(bandingkan dengan perkiraan `500–600`)*
- [ ] **Ukur panjang ujung ke ujung bidang kebun:**
  - Panjang Baris 1: `______ m` | Baris 2: `______ m` | Baris 3: `______ m` *(bandingkan dengan `~100 m` & garis `117,52 m`)*
  - **Ukur jarak tanam antar pohon dalam satu baris** *(ambil 5–10 selang acak: pangkal, tengah, ujung)*:
    - Sampel jarak tanam: `____, ____, ____, ____, ____ m` -> **Rata-rata `________ m`**
  - **Ukur lebar melintang kebun (kunci dimensi *header/manifold*!):**
    - Posisi lateral Baris 1 terhadap Parit 1 (`cm`): `______` | Lebar atas Parit 1 (`cm`): `______`
    - Jarak antar sumbu pohon Baris 1 ke Baris 2: **`________ m`**
    - Jarak antar sumbu pohon Baris 2 ke Baris 3: **`________ m`**
    - **Total lebar kebun terukur (tepi kiri hingga tepi kanan):** **`________ m`** *(rekonsiliasi antara keterangan `~6 m` vs dugaan `25–30 m` di CD-2!)*
- [ ] Kemiringan tanah sepanjang baris 100 m (datar atau landai miring ke arah mana?): `___________________________`

### C.2 Geometri Parit Galian Tanah & Penghubung Melintang (`+`)
- [ ] Panjang aktual: Parit 1 = `____ m`, Parit 2 = `____ m`, Parit 3 = `____ m`.
- [ ] **Penampang parit** (ukur di titik pangkal, tengah, dan ujung):
  - Lebar bibir atas parit: `____ – ____ cm`
  - Lebar dasar parit: `____ – ____ cm`
  - Kedalaman parit dari muka tanah bedengan: `____ – ____ cm`
- [ ] **Penghubung melintang (`+`):**
  - Total jumlah parit penghubung melintang: `______` buah.
  - Jarak antar parit `+`: setiap **`____` pohon** atau setiap **`________ m`**.
  - Lebar & kedalaman parit penghubung `+`: `____ cm` × `____ cm`.
- [ ] **Kecepatan air parit surut/habis (Neraca Air Parit):**
  - Tinggi air parit tepat setelah pompa Alkon berhenti mengisi: `______ cm`.
  - Setelah pompa mati (tanpa ditimba 10–15 menit), turun menjadi: `______ cm` setelah `____` menit!
  - Di mana air masuk dari pompa (inlet parit mana?) dan ke mana arah alirannya? Adakah kebocoran/ujung parit terbuka langsung ke pembuangan/sawah sebelah? `___________________________`

### C.3 Verifikasi Lapangan Data Medan untuk Pembanding Robot (`Alt 2 & Alt 3` CD-3)
- [ ] **Lebar jalur bebas bersih (*clear path width*)** di antara batang/cabang pohon 1 m & bibir parit yang tidak terhalang dahan keras: `________ cm` *(periksa di titik tersempit!)*.
- [ ] **Ketahanan bibir parit tanah liat basah:** bila diinjak tepat di bibir `15–20 cm` dari tepi parit saat basah, apakah mudah amblas/longsor? `[ ] Mudah longsor` `[ ] Cukup keras`.
- [ ] **Ruang ujung baris (*headland*):** lebar ruang putar kosong sebelum pagar/parit/sawah tetangga: `________ m`.

### C.4 Penentuan Koordinat Pasti Petak Uji Purwarupa (Rekonsiliasi `20 m × 3 baris` vs `C-03`)
- [ ] Pilih segmen **pangkal/awal/tengah** 3 baris berdekatan bersama pemilik kebun agar tidak mengganggu panen/kerja rutin.
- [ ] Pasang patok pada bentang **`20 m`** vs **`25 m`** sepanjang 3 baris tersebut lalu hitung:
  - Dalam **1 baris × 20 m** ada berapa pohon? `______ pohon` -> 3 baris × 20 m = **`______ pohon`**.
  - Jika ditarik **1 baris × 25 m** (mengikuti teks minimal `1 lajur >= 25 m` di `C-03`), ada berapa pohon di 1 baris? `______ pohon` -> 3 baris × 25 m = **`______ pohon`**.
- [ ] Tandai posisi **parit melintang (`+`)** yang berada di dalam petak uji: ada `____` parit silang yang perlu **jembatan penyangga pipa sederhana** agar pipa tidak terinjak/terendam!

---

## 5. Pos D — Observasi Penyiraman Eksisting, Kalibrasi Ember & Audit Pompa Bensin Alkon (Pertalite)

*Menutup ketidakpastian volume aktual `< 15 L` serta memverifikasi konsumsi nyata BBM Pertalite, biaya servis pompa, dan riwayat uji coba LPG terdahulu sebagai pembanding adil `Payback Period`.*

### D.1 Kalibrasi Ember & Pengukuran Guyuran Nyata
- [ ] Foto & ukur dimensi **ember hitam kecil** pekerja: diameter atas `____ cm`, diameter bawah `____ cm`, tinggi `____ cm`.
- [ ] **Kalibrasi volume dengan gelas ukur `1 L` / literan:**
  - Volume isi penuh sampai bibir ember: **`________ Liter`**
  - Volume isi kebiasaan pekerja saat menimba di parit dangkal (`tingkat isi normal`): **`________ Liter`**
- [ ] **Amati pekerja mengguyur minimal 3–5 pohon berbeda** (misal di parit penuh vs parit dangkal / baris ujung):
  - Jumlah ember/guyuran rata-rata per pohon: `____` ember -> dikali volume isi = **`________ Liter/pohon`** *(bandingkan langsung dengan acuan mitra `15 L/pohon`!)*.
  - Perkiraan tumpahan yang langsung meluncur kembali ke parit / di luar radius akar: `[ ] Hampir nol` `[ ] ~10–25%` `[ ] > 25%`
  - Waktu menyiram per pohon (menimba + jalan + mengguyur): `________ detik/pohon`.
- [ ] Kesan kondisi air saat parit mulai dangkal: apakah pekerja menimba lebih sedikit per pohon di parit ujung/saat dangkal? `[ ] Ya` `[ ] Tidak`.

### D.2 Audit Teknis Pompa Mesin Eksisting (`Alkon` Bensin Pertalite + Catatan Riwayat Uji LPG)
- [ ] Foto pelat nama (*nameplate*) pompa & mesin penggerak, kondisi dudukan pompa di tepi saluran, serta ukuran selang hisap/buang eksisting.
- [ ] Catat spesifikasi tertera: Merek/Tipe `______________`, Daya `____ HP / ____ cc`, Ukuran Hisap/Buang `____ inci`, Debit/Head maksimal di pelat `__________`.
- [ ] Taksir debit aktual pompa di kebun (tampung ujung selang/keluaran ke wadah 20 L + *stopwatch*, ulangi 3×):
  - Ulang 1: `____ dtk` | Ulang 2: `____ dtk` | Ulang 3: `____ dtk` -> **Debit aktual: `________ L/menit`**.
  - Total waktu pompa menyala per 1 hari penyiraman (mengisi parit `500–600` pohon): `________ jam/menit`.
- [ ] **Audit Biaya Bahan Bakar Nyata (Pertalite Aktif) & Riwayat Pengalaman Uji LPG:**
  - Konsumsi **bensin Pertalite aktif sekarang**: butuh berapa liter per siklus penyiraman (`____ liter/siklus`) dengan harga eceran/SPBU di Ciberes (`Rp ________/liter`) -> **Biaya Pertalite per siklus: Rp `________`**.
  - **Riwayat uji coba LPG 3 kg terdahulu *(sudah dihentikan)*:** kapan dicoba, sempat dipakai berapa lama, gejala panas/*overheating* apa yang terjadi, kerusakan komponen apa yang timbul (seher/ring/klep), dan kapan resmi kembali memakai Pertalite murni? `___________________________`
  - Riwayat servis rutin pompa 6–12 bulan terakhir: ganti oli tiap berapa jam (`Rp ______`), biaya ganti busi/seher/seal/servis karburator (`Rp ________/tahun`), berapa kali pompa bermasalah sehingga harus sewa/pinjam pompa lain (`Rp ________`)?
- [ ] Klarifikasi angka **`~Rp90 juta`** (Audio 1): pastikan rincian kasarnya (sejak buka lahan tahun `______`: bibit/tanah/pagar/parit vs upah siram berapa tahun) agar tim tidak salah mengutip di laporan.

---

## 6. Pos E — Agronomi Jeruk Limau, Uji Tanah/Akar, Pemupukan & Hujan (`S-01`, `S-04`)

*Mengunci parameter agronomi asli tapak jeruk tanpa meminjam data sayuran atau Florida/India, serta mengambil sampel wajib untuk kalibrasi sensor.*

### E.1 Data Bibit, Ukuran Pohon & Fase Pertumbuhan
- [ ] Konfirmasi jenis jeruk ke pemilik/penjual bibit: `[ ] Jeruk Limau (*C. amblycarpa*)` `[ ] Jeruk Nipis` `[ ] Campur / Lainnya: _______`. Asal bibit: `[ ] Cangkok` `[ ] Okulasi/Stek` `[ ] Biji`.
- [ ] Tahun tanam pertama kebun: tahun `______` (umur sekarang `______` bulan/tahun); apakah ada tanaman baru sulaman berumur beda (`____` pohon)?
- [ ] Ukur **5 pohon contoh** (mewakili pohon pendek `~1 m`, sedang, dan paling rimbun):
  - Pohon 1: Tinggi `____ cm` | Lebar tajuk `____ cm` | Tinggi dahan terendah dr tanah `____ cm` | Fase `__________`
  - Pohon 2: Tinggi `____ cm` | Lebar tajuk `____ cm` | Tinggi dahan terendah dr tanah `____ cm` | Fase `__________`
  - Pohon 3: Tinggi `____ cm` | Lebar tajuk `____ cm` | Tinggi dahan terendah dr tanah `____ cm` | Fase `__________`
  - Pohon 4: Tinggi `____ cm` | Lebar tajuk `____ cm` | Tinggi dahan terendah dr tanah `____ cm` | Fase `__________`
  - Pohon 5: Tinggi `____ cm` | Lebar tajuk `____ cm` | Tinggi dahan terendah dr tanah `____ cm` | Fase `__________`
  *(Penting: lebar tajuk menetapkan di mana `PC dripper` dipasang pada radius `0,5–0,8 m`!)*
- [ ] Perkirakan persentase kondisi kebun saat ini: `% Vegetatif/Tunas: ___%`, `% Berbunga: ___%`, `% Berbuah kecil: ___%`, `% Siap panen: ___%`.
- [ ] Dari mana mitra memperoleh acuan **"minimal 15 L/pohon"** (pengalaman pribadi, penyuluh pertanian, atau artikel/YouTube)? `___________________________`
- [ ] Hasil panen jeruk limau saat ini (berapa kg/minggu atau kg/tahun, harga jual, dan apakah mitra pernah mencatat buah kecil/gugur saat telat siram): `___________________________`

### E.2 Pengamatan Zona Akar, Uji Infiltrasi `15 L`, & Pengambilan Sampel Tanah
- [ ] Gali cek kecil hati-hati pada 1–2 pohon di jarak `50 cm` dari pangkal batang hingga `25–35 cm` bawah tanah:
  - Kedalaman dominan akar serabut aktif: `____ – ____ cm`.
  - Warna & tekstur tanah di tangan (dipilin saat lembap): `[ ] Lempung liat lengket bisa dipilin tipis` `[ ] Lempung berpasir` `[ ] Liat retak saat kering`.
  - Kondisi tanah saat ini sebelum disiram: `[ ] Kering retak` `[ ] Lembap gembur` `[ ] Becek tergenang`.
- [ ] **Uji Infiltrasi Mini `15 L` di 1 Pohon Contoh (Verifikasi `S-04`):**
  - Siram pelan `15 Liter` di piringan akar diameter `1,0–1,2 m`.
  - Waktu habis meresap hingga tak ada genangan: `________ menit` *(lulus syarat `<= 30 menit`? `[ ] Ya [ ] Masih menggenang >30 mnt`)*.
  - 30 menit setelah siram, gali/tusuk cek di jarak `50 cm` & `80 cm` dari batang: kedalaman tembus basah = **`________ cm`** *(target `S-04`: `20–40 cm`!)*.
- [ ] **Ambil `1–2 kg` sampel tanah jeruk** (kedalaman `15–30 cm`, gabung dari 3 titik bedengan, masuk plastik klip berlabel *"Tanah Jeruk Ciberes"*) -> **WAJIB dibawa pulang** untuk uji pH/EC lab & **pembuatan kurva kalibrasi sensor `Capacitive v1.2`**!

### E.3 Pemupukan, Pestisida & Pola Hujan
- [ ] Klarifikasi **"pupuk 1 kuintal lebih, dua kali setahun"**:
  - Jenis & merek pupuk yang dipakai (NPK / Urea / KCl / Dolomit / Pupuk kandang): `___________________________`
  - Berat **1 kuintal lebih (`>100 kg`)** itu dipakai untuk **berapa pohon** dalam **satu kali pemupukan**? `________ kg` untuk `________ pohon` (= `~______ gram/pohon/aplikasi`).
  - Tanggal aplikasi terakhir (`______`) & metode sebar (tabur / tugal / kocor)? `___________________________`
- [ ] Klarifikasi **pestisida mingguan**: produk/bahan aktif `______________`, perkiraan dosis/tangki `________`, hama/penyakit yang sering muncul di jeruk (kutu kebul, kutu loncat, blendok/busuk batang, lalat buah?): `___________________________`
- [ ] Aturan tunda siram saat hujan menurut pengalaman mitra: jika hujan turun deras hari ini, berapa hari berikutnya baru disiram lagi? `________ hari`

---

## 7. Pos F — Lokasi Panel Surya, Box Kontrol IP65, Jalur Jembatan Parit, & Keamanan Lahan

*Menentukan lokasi fisik penempatan peralatan saat instalasi CD-4 dan mencegah gagal operasi akibat naungan, banjir, tikus, maupun pencurian.*

- [ ] **Pilih calon titik tiang Panel Surya `100 Wp` + Kotak Panel `IP65` *(tetap aman di kebun atas, jangan taruh di bantaran irigasi!)*:**
  - Jarak lintasan kabel/pipa dari kotak panel kebun atas ke titik pompa *(jika tebing `> 2 m` dan pompa harus ditaruh di boks aman bantaran bawah)*: `________ m` *(penting untuk memilih ukuran kabel DC `2×4 mm²` vs `2×6 mm²` agar rugi tegangan tetap rendah!)*.
  - Konfirmasi lokasi aman menempatkan pompa DC itu sendiri: `[ ] Bisa di kebun atas bersama kotak panel (bila Δz <= 1,5–2 m)`  `[ ] Perlu boks terkunci di bantaran + konduit kabel turun`  `[ ] Pakai kolam/parit terpal cadangan dalam kebun`.
  - Jarak dari kotak panel ke *header* 3 katup MBV petak uji: `________ m` *(ukuran kabel kontrol H-Bridge `2×0,75/1,5 mm²` + kabel sensor)*.
  - Cek arah hadap matahari & **hambatan naungan** (ada pohon besar/bambu/gubuk di sisi Timur–Utara–Barat pukul 08.00–16.00?): `[ ] Terbuka bebas bayangan` `[ ] Ada bayangan pada jam: _______`.
  - Elevasi titik tiang di atas batas banjir sungai: `+ ________ cm`.
- [ ] **Keamanan Fisik Perangkat & Proteksi Hama/Maling (`Risiko Nyata Kebun Terbuka`):**
  - Apakah di area kebun jeruk ada penjaga tetap, saung pekerja, atau pagar keliling? `___________________________`
  - Apakah di kebun pernah terjadi pencurian buah/pompa/aki, sehingga panel surya, baterai LiFePO4, dan kotak panel harus dibuat **mudah dilepas-bawa (*portable* setelah uji?) atau dikunci gembok pelat baja/rantai** di tiang cor? `___________________________`
  - Risiko gangguan **tikus sawah/anjing/cangkul/mesin babat rumput** terhadap pipa PE 16 mm & kabel sensor:
    - Diskusikan dengan pemilik apakah pipa PE 16 mm di setiap baris lebih aman diletakkan: `[ ] Rapat tanah di bawah pangkal pohon dalam piringan` atau `[ ] Diikat menggantung di ajir/patok pendek ±15–20 cm di atas tanah` (aman dari cangkul/babat rumput & mempermudah pengecekan tetesan dripper!).
- [ ] Di tiap perlintasan **parit penghubung melintang (`+`)** pada petak uji: catat apakah jembatan pipa penopang kayu/bambu/PVC setinggi berapa cm yang aman dilangkahi pekerja saat bekerja!

---

## 8. Pos G — Checklist Foto Wajib & Penutupan Kunjungan (MoM)

Sebelum pulang dari Ciberes, pastikan seluruh bukti visual & kesepakatan berikut sudah tersimpan:

- [ ] **Foto 1:** Tampak lebar seluruh petak uji yang disepakati (dengan patok penanda `20 m`/`25 m` terlihat jelas).
- [ ] **Foto 2:** Sumber air Sungai Ciberes + titik rencana pemasangan *foot valve* pompa (dengan meteran/tongkat pembanding ketinggian tebing!).
- [ ] **Foto 3:** Penampang parit memanjang + pertemuan parit melintang `+` **dengan meteran terbuka di dalam bingkai foto**.
- [ ] **Foto 4:** Ember hitam pekerja berdampingan dengan botol ukur `1 L` / penggaris.
- [ ] **Foto 5:** Pompa Alkon bensin (Pertalite) eksisting + area sambungan selang hisap/buang + foto *close-up* pelat spesifikasi/label mesin.
- [ ] **Foto 6:** 3–5 foto kondisi pohon jeruk (keseluruhan tajuk, piringan akar radius 0,5–0,8 m, buah/bunga jika ada, dan lubang tes akar/infiltrasi `15 L`).
- [ ] **Foto 7:** Calon titik tiang panel surya 100 Wp (arah menghadap ke langit terbuka untuk memverifikasi bebas naungan).
- [ ] **Kesepakatan Mitra / Berita Acara Kunjungan (MoM singkat):** Catat poin persetujuan pemasangan petak uji percontohan (luasan, perkiraan jadwal instalasi & uji coba), izin bawa sampel air/tanah, lalu mintalah tanda tangan / paraf pemilik kebun + foto bersama sebagai bukti kemitraan Capstone CD-3/CD-4!
