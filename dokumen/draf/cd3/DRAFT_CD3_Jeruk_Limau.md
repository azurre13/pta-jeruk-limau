# DOKUMEN CD-3: DESAIN RANCANGAN SOLUSI SISTEM IRIGASI KEBUN JERUK LIMAU DI CIBERES SUBANG

**Program Studi S1 Teknik Komputer**  
**Fakultas Teknik Elektro, Universitas Telkom, Bandung**  
**Tahun Akademik 2026/2027**

---

### Data Dokumen dan Lembar Pengesahan (Tabel 0 & Tabel 1)

| Parameter | Nilai / Keterangan |
|---|---|
| **Judul Capstone Design** | Analisis Permasalahan Penyiraman Manual pada Kebun Jeruk Limau di Ciberes Subang |
| **Jenis Dokumen** | Desain Rancangan Solusi |
| **Nomor Dokumen** | FTE-CD-3 |
| **Nomor Revisi** | 00 |
| **Tanggal Pengesahan** | 10 Desember 2026 |
| **Fakultas** | Fakultas Teknik Elektro |
| **Program Studi** | S1 Teknik Komputer |
| **Jumlah Halaman** | 28 halaman |

**Tim Penulis (Mahasiswa):**
1. Muhammad Al Qarnie / NIM: 101032330043 (Ketua / Integrasi Sistem & Firmware)
2. Maheswara Ariq Athallah / NIM: 101032300050 (Anggota / Instrumentasi, Sensor & Catu Daya)
3. Daffa Hermansyah / NIM: 101032330090 (Anggota / Mekanikal, Hidrolika & Pengujian Lapangan)

**Disetujui Oleh:**  
- **Pembimbing 1:** Dr. Agung Nugroho Jati, S.T., M.T.
- **Pembimbing 2:** Burhanuddin Dirgantara, S.T., M.T.

---

### Timeline Revisi Dokumen (Tabel 2)

| Versi, Tanggal | Revisi | Perbaikan yang Dilakukan | Halaman Revisi |
|---|---|---|---|
| 00, 10 Desember 2026 | Draf Final CD-3 | Perumusan tiga alternatif usulan solusi rekayasa, analisis komparasi multi-kriteria berbasis *Engineering Design Matrix Scoring* (Pugh Matrix), penetapan solusi terpilih jaringan mikroirigasi multi-zonasi cerdas, perancangan detail arsitektur teknis (hidrolika, elektronika kontroler ESP32, sistem daya PLTS *off-grid*, dan algoritma perangkat lunak), penyusunan *Bill of Materials* (BOM) purwarupa mahasiswa ($\le \text{Rp5.000.000}$) serta proyeksi skala penuh kebun ($\le \text{Rp18.000.000}$), penyusunan *Gantt Chart* jadwal 6 bulan, dan pembagian tugas kelompok terperinci. | Seluruh Dokumen |
| | | *(Disediakan untuk catatan revisi dosen pembimbing)* | |
| | | *(Disediakan untuk catatan revisi dosen pembimbing)* | |

---

# BAB 1: ALTERNATIF USULAN SOLUSI

Dokumen CD-3 (*Desain Rancangan Solusi*) ini merupakan kelanjutan sistematis dan tindak lanjut langsung dari dokumen CD-1 (*Analisis Permasalahan*) dan dokumen CD-2 (*Batasan dan Spesifikasi Desain*). Pada tahap CD-1, telah diidentifikasi secara empiris akar permasalahan utama pada kebun jeruk limau mitra di Desa Ciberes, Kecamatan Patokbeusi, Kabupaten Subang, Jawa Barat, yaitu: tingginya biaya tenaga kerja manual (4 buruh harian, biaya upah Rp400.000 per siklus penyiraman 3 hari sekali atau mencapai Rp48,7 juta/tahun), ketidakseragaman dosis air (10–15 Liter per pohon tidak tertakar presisi), risiko pengikisan hara pemupukan NPK akibat guyuran ember manual, keterbatasan fisik pekerja di lahan memanjang 100–117,52 meter seluas ~3.000 m² (populasi 500–600 pohon), ketiadaan jaringan listrik jala-jala PLN (*off-grid*), kegagalan modifikasi bahan bakar LPG 3 kg pada pompa bensin Alkon eksisting akibat pemanasan berlebih (*overheating*), serta tingginya kandungan lumpur dan pasir sedimen pada air sungai Ciberes yang berjarak 20,54 meter dari batas kebun.

Selanjutnya, pada dokumen CD-2 telah dirumuskan secara formal lima batasan rekayasa mutlak (*hard constraints* C-01 s.d. C-05) dan 14 butir spesifikasi kuantitatif (*engineering specifications* S-01 s.d. S-14). Selaras dengan ketentuan Buku Panduan Capstone Design FTE Telkom University (2024), ruang lingkup luaran fisik tugas akhir mahasiswa difokuskan pada perancangan dan pembuktian kinerja **purwarupa fungsional (*functional working prototype*) pada petak uji representatif (*pilot testbed*)** kebun mitra (1 lajur barisan pohon percontohan, 15–20 pohon pada bentang operasional $\ge 25\text{ meter}$) dengan pagu biaya belanja komponen maksimal Rp5.000.000, serta memiliki rancang bangun modular yang terbukti secara teknis dapat diskalakan (*scalable*) untuk melayani seluruh 500–600 pohon kebun dengan proyeksi investasi komersial maksimal Rp18.000.000.

Guna memenuhi amanat proses rekayasa yang objektif dan komprehensif, Bab 1 ini mengusulkan **tiga (3) konsep alternatif solusi rekayasa** yang relevan, fisibel, dan berpotensi menyelesaikan permasalahan operasional kebun jeruk limau di Ciberes, Subang.

---

### 1.1 Alternatif 1: Jaringan Mikroirigasi Perpipaan Cerdas Otomatis Multi-Zonasi (*Smart Multi-Zone Micro-Drip Irrigation Network*)

#### 1.1.1 Deskripsi Konsep dan Arsitektur
Alternatif 1 adalah sistem irigasi presisi berbasis jaringan perpipaan tertutup permanen/semi-permanen yang mendistribusikan air bertekanan rendah langsung ke zona perakaran aktif masing-masing pohon jeruk limau. Air disedot dari sungai menggunakan pompa diafragma elektrik DC 12V hemat daya, dialirkan melalui unit penyaring sedimen fisik berkerapatan ganda 120 mesh, dan didistribusikan melalui pipa polietilena utama (*mainline* PE diameter 1 inci) menuju pipa lateral fleksibel (PE diameter 16 mm) yang dibentangkan di sepanjang barisan bedengan pohon.

Pada setiap pohon jeruk limau, dipasang 2 unit emiter tetes kompensasi tekanan (*Pressure Compensating Dripper* / PC Dripper) dengan kapasitas debit masing-masing 8 Liter/jam (total debit 16 Liter/jam per pohon) yang diletakkan melingkar pada radius 0,5–0,8 meter dari pangkal batang di bawah proyeksi kanopi tajuk. Pengendalian aliran fluida diatur secara multi-zonasi menggunakan katup selenoid DC 12V (*solenoid valve*) yang diaktifkan secara bergiliran oleh mikrokontroler terprogram (ESP32) bertenaga surya fotovoltaik mandiri (*off-grid solar PV system*).

#### 1.1.2 Fitur Utama dan Spesifikasi Teknis
1. **Dosis Air Presisi Berbasis Waktu dan Debit Terkompensasi:** Penggunaan emiter PC menjamin debit air keluar stabil pada 8 L/jam per emiter (16 L/jam per pohon) pada rentang tekanan kerja 0,1 hingga 0,35 MPa, terlepas dari perbedaan jarak pohon terhadap pompa atau variasi elevasi tanah parit. Dengan demikian, target dosis air 10–15 Liter per pohon dapat dicapai secara eksak dengan mengaktifkan katup zona selama tepat 45 hingga 55 menit.
2. **Pengendalian Multi-Zonasi Berdaya Rendah:** Pembagian barisan pohon menjadi beberapa zona hidrolika independen memungkinkan penggunaan pompa berdaya kecil (60–100 Watt), sehingga konsumsi arus listrik dari baterai tetap rendah dan tidak membebani sistem pembangkit surya.
3. **Penyaringan Sedimen Bertingkat:** Dilengkapi tabung saringan cakram (*disc filter*) 120 mesh (kemampuan filtrasi partikel $\ge 130\ \mu\text{m}$) dengan katup pembuang lumpur (*manual flush valve*) untuk mencegah penyumbatan lubang labirin emiter PC dari padatan lumpur sungai Ciberes.
4. **Otomasi Terjadwal dan *Single-Touch Manual Override*:** Sistem dilengkapi modul jam waktu nyata (*Real-Time Clock* / RTC DS3231) untuk jadwal penyiraman rutin otomatis pada pagi hari (pukul 07.00 WIB) atau sore hari (pukul 16.00 WIB), serta tombol fisik tunggal (*single-touch push button*) untuk kemudahan operator kebun memulai siklus siram secara instan.
5. **Subsistem Catu Daya Surya Mandiri:** Ditenagai 1 unit panel surya monokristalin 100 Wp, *Solar Charge Controller* (SCC) MPPT 12V/10A, dan modul baterai *Lithium Iron Phosphate* (LiFePO4) 12V 30Ah (360 Wh) dengan selungkup kedap air IP65.

#### 1.1.3 Prosedur Pengoperasian
1. Operator menyalakan sakelar daya utama pada selungkup kontroler IP65.
2. Sistem melakukan inisialisasi modul, memeriksa level tegangan baterai, dan membaca sensor kelembapan tanah.
3. Pada jadwal operasi yang telah ditetapkan, kontroler membuka katup selenoid Zona 1 dan mengaktifkan pompa DC.
4. Air sungai disedot, disaring melalui filter 120 mesh, dan dialirkan ke pipa lateral Zona 1. Emiter PC meneteskan air merata ke 15–20 pohon pada petak uji.
5. Sensor *flow meter* memverifikasi volume air yang terdistribusi. Setelah target volume 15 L/pohon terpenuhi (durasi ~50 menit), kontroler mematikan Zona 1 dan beralih ke zona berikutnya.
6. Setelah seluruh zona selesai terairi, sistem mematikan pompa dan memasuki mode tidur berdaya rendah (*deep sleep*).

#### 1.1.4 Analisis Kelebihan dan Kelemahan
* **Kelebihan:**
  * Efisiensi aplikasi air sangat tinggi ($\eta_a > 85\%$) karena air langsung meresap ke zona perakaran aktif tanpa rembesan liar parit tanah bebas dan tanpa kehilangan evaporasi udara terbuka.
  * Koefisien keseragaman Christiansen terbukti sangat tinggi ($CU \ge 90\%$) berkat mekanisme kompensasi tekanan membran silikon pada emiter PC.
  * Konsumsi energi sangat rendah karena tidak ada motor penggerak mekanikal dinamis; seluruh daya hanya dialokasikan untuk pemompaan fluida dan sirkuit mikrokontroler.
  * Biaya belanja purwarupa sangat terjangkau ($\le \text{Rp5.000.000}$) dan mudah dirakit dari komponen pasar lokal.
  * Komponen statis memiliki umur teknis panjang (pipa PE tahan paparan ultraviolet hingga 5 tahun).
* **Kelemahan:**
  * Pipa lateral yang dibentangkan di atas tanah parit/bedengan rentan terinjak pekerja saat pemangkasan cabang atau tertusuk cangkul saat penyiangan gulma liar.
  * Memerlukan prosedur pembilasan rutin (*flushing*) berkala pada saringan cakram guna membuang endapan lumpur sungai Ciberes.

---

### 1.2 Alternatif 2: Robot Penjelajah Pematang Parit dengan Lengan Robotik Terarah (*Tracked/4WD Straddle Ditch-Rover with Articulated Robotic Spray Arm*)

#### 1.2.1 Deskripsi Konsep dan Arsitektur
Alternatif 2 mengadopsi pendekatan robotika pertanian bergerak mutakhir (*advanced agricultural mobile robotics*), terinspirasi dari paten Henan Yungeng Era Robot Technology Co., Ltd. (Paten CN115804333A, 2023) serta riset robotika irigasi oleh Elkaoud dkk. (2025). Wahana robot ini menggunakan sasis 4-roda bertapak lebar (4WD) atau roda rantai karet ganda (*dual rubber crawler tracks*) yang melintas di atas pinggiran pematang/bibir parit (*straddling the ditch bunds*) sepanjang 100 meter, bukan berjalan di dalam genangan lumpur parit.

Wahana ini memanfaatkan keberadaan air yang telah dialirkan ke dalam tiga parit memanjang kebun Ciberes. Di bawah perut sasis robot, terpasang pipa hisap vertikal fleksibel yang dilengkapi saringan apung (*dip suction pipe with floating strainer*) yang menjulur langsung ke dalam air parit galian tanah, sehingga robot dapat menyedot air secara mandiri tanpa harus menyeret selang bertekanan sepanjang 100 meter dari sungai. Di atas sasis, terpasang sepasang lengan robotik bersendi (*2-DOF / 3-DOF articulated robotic manipulator arms*) di sisi kiri dan kanan yang digerakkan oleh motor servo torsi tinggi kedap air IP65. Saat mendeteksi pohon jeruk limau via sensor ultrasonik atau kamera pengenal batang, lengan robotik menjulurkan nosel semprot tepat ke bawah kanopi tajuk mengarah ke zona perakaran aktif (radius 0,5–0,8 m dari pangkal batang), menyalurkan air terukur langsung ke tanah tanpa membasahi tajuk daun.

#### 1.2.2 Fitur Utama dan Spesifikasi Teknis
1. **Akurasi Sasaran Daerah Akar Sangat Tinggi:** Lengan robotik secara mekanis menjulurkan nosel semprot langsung ke zona perakaran tanah di bawah kanopi tajuk, sehingga sama sekali tidak membasahi daun atau batang atas dan terbebas dari risiko memicu infeksi jamur *Phytophthora nicotianae*.
2. **Mobilitas Mandiri Tanpa Beban Seretan Selang:** Sistem menyedot pasokan air langsung dari genangan air parit di bawah sasis robot, mengeliminasi kebutuhan dan beban mekanis menyeret selang bertekanan sejauh 100 meter dari sungai.
3. **Traksi Luas Roda Rantai Karet (Anti-Amblas):** Sasis roda rantai karet (*crawler tracks*) atau ban 4WD lebar membagi beban robot secara merata di atas permukaan pematang bedengan tanah gembur, memberikan kestabilan manuver yang prima.
4. **Otomasi Navigasi Mandiri:** Beroperasi mandiri menyusuri pematang parit dipandu sensor penjejak garis magnetik/optik atau kawat pandu bawah tanah, berhenti otomatis di setiap pohon secara presisi.

#### 1.2.3 Prosedur Pengoperasian
1. Operator menempatkan wahana robot pada pangkal pematang parit kebun dan memastikan air parit telah terisi.
2. Operator menekan tombol *START* pada selungkup kendali robot.
3. Wahana merayap maju secara perlahan di atas pematang parit menyusuri barisan pohon.
4. Saat sensor mendeteksi batang pohon jeruk limau di sisi kiri atau kanan, wahana berhenti otomatis.
5. Lengan robotik bergerak menjulurkan nosel semprot ke zona perakaran pohon, pompa hisap menyedot air dari parit bawah dan menyemprotkan dosis tepat 15 Liter air berbasis pembacaan flow meter.
6. Lengan robotik melipat kembali ke posisi awal, wahana bergerak maju ke pohon berikutnya hingga mencapai ujung parit 100 meter.

#### 1.2.4 Analisis Kelebihan dan Kelemahan
* **Kelebihan:**
  * Penempatan air sangat presisi ke daerah perakaran berkat lengan robotik artikulasi tanpa membasahi tajuk.
  * Bebas dari hambatan seretan selang panjang karena mengambil air langsung dari parit bawah.
  * Traksi kokoh dan stabil di pematang tanah bedengan.
  * Menghilangkan 100% ketergantungan tenaga fisik buruh manual.
* **Kelemahan:**
  * **Biaya Mekatronika Sangat Mahal:** Sasis crawler kedap air, 2 unit aktuator servo torsi tinggi lengan robotik, sensor pengenal pohon, mikrokontroler canggih, dan baterai lithium kapasitas besar menguras biaya purwarupa hingga Rp7.500.000 – Rp8.500.000, secara telak melanggar batas pagu Capstone (Rp5.000.000).
  * **Risiko Keruntuhan Tanah Bibir Parit Sawah:** Tanah bibir parit Ciberes adalah tanah sawah gembur tanpa dinding semen; beban robot berbobot 25–35 kg rentan memicu tanah pematang longsor saat kondisi basah, mengakibatkan robot terguling ke dalam parit.
  * **Ketergantungan pada Pengisian Air Parit:** Parit tanah Ciberes tidak selalu berisi air, air parit harus terlebih dahulu disedot dari sungai menggunakan pompa Alkon bensin yang rawan *overheating*.
  * **Konsumsi Arus Listrik Tinggi (> 250–350 Watt):** Menuntut kapasitas baterai yang besar dan berat.

---

### 1.3 Alternatif 3: Sistem Irigasi Hibrida Berbasis Tangki Tandon Terdistribusi (*Distributed Header Tank with Gravity Manifold*)

#### 1.3.1 Deskripsi Konsep dan Arsitektur
Alternatif 3 mengombinasikan pemompaan surya volume besar (*bulk solar pumping*) dengan sistem distribusi fluida berbasis tekanan hidrostatik gravitasi. Pada arsitektur ini, pompa celup/sentrifugal DC bertenaga surya menyedot air dari sungai Ciberes pada siang hari saat intensitas radiasi matahari berada pada titik puncak (pukul 10.00–14.00 WIB) melewati saringan partikulat menuju 1 unit tangki penampung air (*header tank* polietilena kapasitas 500 hingga 1.000 Liter) yang diletakkan pada menara dudukan rangka besi/kayu setinggi 2 hingga 2,5 meter di tepi blok kebun.

Penyiraman ke tanaman jeruk limau dilakukan secara independen memanfaatkan gaya gravitasi bumi melalui katup motorik berdaya ultra-rendah (*motorized ball valve* DC 12V 5W). Aliran air dialirkan melalui pipa manifold berdiameter 1 inci menuju pipa distribusi mikro bertekanan rendah yang bermuara pada cincin selang berpori (*soaker hose*) atau mikrotubing lubang ganda di bawah tajuk kanopi pohon.

#### 1.3.2 Fitur Utama dan Spesifikasi Teknis
1. **Pemisahan Fase Pemompaan dan Fase Penyiraman (*Decoupled Operation*):** Pompa air bertenaga surya hanya bekerja saat ada cahaya matahari terik untuk mengisi tangki tandon, sedangkan proses penyiraman tanaman dapat dijalankan kapan saja pada waktu ideal tanpa ketergantungan langsung pada sinar matahari.
2. **Konsumsi Arus Operasional Sangat Rendah:** Selama proses penyiraman tanaman berlangsung, sistem tidak memerlukan daya untuk menyalakan pompa, melainkan hanya membutuhkan energi sesaat (2–3 detik) untuk memutar katup motorik bola membuka dan menutup saluran gravitasi.
3. **Pengukuran Muka Air Tangki Otomatis:** Tangki tandon dilengkapi sensor sakelar pelampung ganda atau sensor ultrasonik kedap air untuk mendeteksi batas air penuh (*full level cut-off*) dan batas air minimum (*low level protection*).
4. **Distribusi Tekanan Rendah Lembut:** Tekanan hidrostatik rendah (0,02–0,025 MPa) mendistribusikan air secara sangat lembut ke zona perakaran tanpa risiko mengikis struktur tanah gembur atau menghanyutkan butiran pupuk NPK.

#### 1.3.3 Prosedur Pengoperasian
1. Pada siang hari, sensor mendeteksi muka air tangki berada di bawah batas normal. Kontroler mengaktifkan pompa pengisi air sungai tenaga surya hingga tangki tandon 500 L terisi penuh.
2. Pada jadwal siram sore hari (pukul 16.30 WIB), kontroler ESP32 mengirim sinyal pulsa 12V untuk membuka katup bola motorik utama selama 3 detik.
3. Air mengalir secara gravitasi dari ketinggian menara 2,5 meter menuju pipa manifold dan meresap perlahan melalui cincin perpipaan di sekeliling 15–20 pohon petak uji.
4. Durasi pembukaan katup dikalibrasi berdasarkan penurunan volume tangki tandon (sekitar 30–40 menit untuk menyalurkan 250–300 Liter air ke petak uji).
5. Setelah volume target tersalurkan, kontroler memutar katup bola motorik menutup kembali aliran air dan kembali ke mode siaga (*standby*).

#### 1.3.4 Analisis Kelebihan dan Kelemahan
* **Kelebihan:**
  * Konsumsi daya baterai saat proses penyiraman sangat hemat karena tidak membutuhkan daya pompa aktif.
  * Pompa bekerja pada efisiensi daya surya puncak pada siang hari (*direct solar pumping*) dengan stres termal rendah.
  * Tekanan hidrostatik gravitasi sangat aman dari risiko kebocoran sambungan pipa pecah akibat lonjakan tekanan fluida (*water hammer*).
* **Kelemahan:**
  * **Variasi Tekanan Hidrostatik (*Head Loss Fluctuation*):** Seiring berkurangnya volume air di dalam tangki tandon, tekanan air turun drastis sehingga debit tetes di awal penyiraman lebih besar dibandingkan di akhir penyiraman, membuat keseragaman Christiansen sulit mencapai $CU \ge 85\%$.
  * **Tantangan Struktur Sipil Tanah Sawah:** Memerlukan menara penopang tangki setinggi 2–2,5 meter seberat 500–1.000 kg di atas kontur tanah sawah Ciberes yang gembur dan rawan ambles saat musim hujan.
  * **Kapasitas Terbatas untuk Skala Penuh:** Untuk melayani 500–600 pohon kebun penuh yang membutuhkan pasokan 7.500–9.000 Liter air per siklus, dibutuhkan kapasitas tangki tandon masif atau konstruksi beton penampung besar yang melampaui batas anggaran mitra.

---

### 1.4 Alternatif 4: Wahana Gerobak Dorong Irigasi & Logistik Kebun Multifungsi (*Multipurpose Semi-Manual Irrigation & Orchard Utility Cart*)

#### 1.4.1 Deskripsi Konsep dan Arsitektur
Alternatif 4 mengadopsi prinsip teknologi tepat guna (*appropriate agricultural technology*) berbiaya terjangkau dengan memadukan mobilitas gerobak dorong roda bertapak lebar (*all-terrain pneumatic tire wheelbarrow*) dengan modul peralatan irigasi elektrik portabel lepas-pasang (*detachable quick-release modular rack*). Konsep ini terinspirasi dari riset perancangan alat penyiram berbasis solar fotovoltaik oleh Nurwidiana dkk. (Jurnal PASTI, 2021) yang dikombinasikan dengan kebutuhan logistik kebun buah jeruk.

Pada sasis gerobak dorong, dipasang modul pompa diafragma elektrik DC 12V 80W, baterai LiFePO4 12V 20–30Ah di dalam boks selungkup kedap air IP65, saringan cakram 120 mesh portabel, serta rol gulungan selang lentur (*hose reel*) sepanjang 25 meter dengan tongkat semprot bertakar (*spray wand with digital flow meter*). Sasis gerobak dirancang multifungsi: saat sesi penyiraman, modul pompa dan selang terpasang di atas gerobak; namun saat musim panen atau pemupukan, rak pompa dapat dilepas dalam hitungan detik untuk difungsikan sebagai gerobak pengangkut hasil panen buah jeruk limau (kapasitas angkut 100–150 kg per ritase) atau jeriken pupuk cair fertigasi.

#### 1.4.2 Fitur Utama dan Spesifikasi Teknis
1. **Nilai Guna Multifungsi Sepanjang Tahun:** Alat tidak menganggur di luar musim kemarau; di musim panen beralih fungsi menjadi sarana angkut buah jeruk limau dari ujung kebun (100 meter) ke jalan raya dan sarana penyemprotan pupuk cair/pestisida.
2. **Biaya Rancang Bangun Paling Terjangkau (CAPEX Terendah):** Menggunakan komponen mekanik gerobak standar toko pertanian lokal; estimasi biaya purwarupa hanya berkisar Rp2.450.000, merupakan opsi paling hemat dari seluruh alternatif solusi.
3. **Bebas Risiko Amblas di Lumpur Parit:** Digerakkan dan dikendalikan langsung oleh tenaga manusia sehingga tidak mengalami risiko selip roda (*wheel slip*) atau amblas di pematang parit seperti robot otonom.
4. **Nol Kerusakan Pipa di Bedengan:** Tidak memerlukan bentangan jaringan pipa permanen di atas bedengan kebun, bebas dari risiko terpotong cangkul atau sabit saat aktivitas penyiangan rumput.
5. **Pengurangan Beban Fisik Buruh Kebun:** Mengubah pekerjaan berat memikul ember berulang kali (membutuhkan 4 buruh) menjadi mendorong gerobak beroda bertekanan ban ringan oleh 1 orang pekerja saja.

#### 1.4.3 Prosedur Pengoperasian
1. Pekerja mendorong gerobak menyusuri jalur setapak pematang parit kebun mendekati blok pohon yang akan disiram.
2. Selang hisap fleksibel dimasukkan ke dalam air parit atau sungai terdekat.
3. Pekerja menyalakan sakelar pompa pada pegangan tongkat semprot dan menyiram zona perakaran pohon jeruk limau dalam radius jangkauan selang 25 meter (10–15 pohon per titik henti gerobak).
4. Pekerja mengontrol dosis 10–15 Liter per pohon secara visual melalui indikator digital flow meter pada pegangan tangan.
5. Setelah blok tersebut selesai, pekerja mematikan pompa dan mendorong gerobak berpindah ke titik bedengan berikutnya.

#### 1.4.4 Analisis Kelebihan dan Kelemahan
* **Kelebihan:**
  * Multifungsi nyata untuk panen dan siram sepanjang tahun.
  * Biaya awal paling murah (CAPEX Rp2.450.000) dengan *payback period* tercepat (6–8 bulan).
  * Bebas dari risiko amblas di tanah lumpur parit.
  * Tanpa bentangan jaringan pipa di tanah, aman dari alat penyiangan rumput.
  * Aman dari sengatan listrik berkat tegangan ekstra rendah SELV 12V DC.
* **Kelemahan:**
  * **Masih Memerlukan Tenaga Kerja Manusia (Semi-Manual):** Bukan sistem otomasi penuh; tetap butuh 1 operator buruh untuk mendorong dan mengarahkan tongkat semprot.
  * **Variabilitas Keseragaman Dosis (Human Error):** Dosis air 10–15 L/pohon rentan tidak konsisten jika pekerja terburu-buru atau kelelahan.
  * **Waktu Operasi Masih Cukup Lama:** Membutuhkan waktu 2,5–3,5 jam per siklus untuk menyiram 600 pohon kebun secara bertahap.
  * **Akses Pematang Sempit:** Memerlukan kehati-hatian operator saat melintasi tanggul pematang yang sempit (< 40 cm).

---

# BAB 2: ANALISIS DAN PEMILIHAN SOLUSI

Guna menentukan satu solusi rekayasa terbaik secara objektif dan ilmiah, bab ini menyusun parameter kriteria evaluasi terbobot dan melaksanakan penilaian komparatif menggunakan metode baku **Matriks Keputusan Rekayasa (*Engineering Decision Matrix Scoring* / Pugh Matrix)** terhadap keempat (4) alternatif solusi yang telah dipaparkan pada Bab 1.

### 2.1 Parameter Kriteria Penilaian dan Pembobotan

Kriteria penilaian diturunkan secara langsung dan konsisten dari **Batasan Rekayasa Mutlak (C-01 s.d. C-05)** dan **Spesifikasi Kuantitatif Solusi (S-01 s.d. S-14)** yang telah disahkan pada dokumen CD-2. Enam kriteria evaluasi ditetapkan beserta persentase bobot kepentingannya:

1. **K1. Keandalan Fisik di Lingkungan Kebun Basah dan Ketahanan Selungkup IP65 (Bobot 20%):** Menilai ketahanan komponen terhadap percikan air, paparan radiasi matahari terik Subang (20–55 °C), lumpur parit sawah, serta ketiadaan komponen bergerak mekanik yang rentan aus/macet.
2. **K2. Keseragaman Distribusi Air dan Efisiensi Aplikasi (Bobot 20%):** Menilai kemampuan menjamin Koefisien Keseragaman Christiansen $CU \ge 85\%$, akurasi dosis 10–15 L/pohon, dan efisiensi pemanfaatan air $\eta_a \ge 80\%$.
3. **K3. Kemandirian Energi *Off-Grid* dan Keselamatan Kelistrikan (Bobot 15%):** Menilai efisiensi daya listrik, ketahanan cadangan baterai $\ge 8$ jam kontinu, dan kepatuhan terhadap tegangan ekstra rendah aman SELV $\le 48\text{ V DC}$.
4. **K4. Kelayakan Biaya Investasi Awal dan Biaya Operasional (Bobot 20%):** Menilai kepatuhan terhadap pagu purwarupa ($\le \text{Rp5.000.000}$), proyeksi kebun penuh ($\le \text{Rp18.000.000}$), dan biaya operasional $\le \text{Rp50.000}$ per siklus dengan *payback period* 12–18 bulan.
5. **K5. Kemudahan Operasional Operator Mitra dan Kemudahan Pemeliharaan (Bobot 15%):** Menilai kemudahan tombol tunggal, waktu pelatihan buruh $\le 30$ menit, dan kemudahan pembersihan saringan $\le 20$ menit per bulan.
6. **K6. Skalabilitas Desain Sistem dari Petak Uji ke Kebun Penuh (Bobot 10%):** Menilai kemudahan arsitektur purwarupa (15–20 pohon) diperluas secara modular melayani seluruh 500–600 pohon kebun.

---

### 2.2 Matriks Keputusan Rekayasa (*Engineering Decision Matrix Scoring*)

Hasil evaluasi komparatif matriks skoring terbobot disajikan pada Tabel 1:

#### Tabel 1. Matriks Keputusan Pemilihan Alternatif Solusi (*Pugh Decision Matrix*)

| No | Kriteria Evaluasi Terbobot | Rujukan CD-2 | Bobot (%) | Alternatif 1: Smart Micro-Drip | Alternatif 2: Robot Pematang & Lengan | Alternatif 3: Gravity Header Tank | Alternatif 4: Gerobak Multifungsi |
|:---:|---|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | Keandalan Lingkungan & Proteksi IP65 | C-02, S-05, S-07 | 20% | Skor: **4,5** *(0,90)* | Skor: **2,5** *(0,50)* | Skor: **3,5** *(0,70)* | Skor: **4,5** *(0,90)* |
| 2 | Keseragaman Air (CU) & Efisiensi | S-01, S-02, S-04, S-11 | 20% | Skor: **5,0** *(1,00)* | Skor: **4,5** *(0,90)* | Skor: **3,0** *(0,60)* | Skor: **3,5** *(0,70)* |
| 3 | Kemandirian Energi & Keselamatan SELV | C-01, C-04, S-06, S-12 | 15% | Skor: **4,5** *(0,675)*| Skor: **2,5** *(0,375)*| Skor: **5,0** *(0,75)* | Skor: **4,5** *(0,675)*|
| 4 | Kelayakan Biaya (CAPEX, OPEX, PP) | S-08, S-09, S-10 | 20% | Skor: **4,5** *(0,90)* | Skor: **1,5** *(0,30)* | Skor: **3,5** *(0,70)* | Skor: **5,0** *(1,00)* |
| 5 | Kemudahan Operasi & Pemeliharaan | S-13, S-14 | 15% | Skor: **4,0** *(0,60)* | Skor: **2,5** *(0,375)*| Skor: **3,5** *(0,525)*| Skor: **4,0** *(0,60)* |
| 6 | Skalabilitas Modular Sistem | C-03 | 10% | Skor: **4,5** *(0,45)* | Skor: **4,0** *(0,40)* | Skor: **2,0** *(0,20)* | Skor: **3,5** *(0,35)* |
| **TOTAL** | **Skor Terbobot Akhir (Skala 5,000)** | | **100%** | **4,525** | **2,850** | **3,475** | **4,225** |
| **KEPUTUSAN** | **Peringkat Evaluasi Rekayasa** | | **-** | **SOLUSI TERPILIH<br>(Peringkat 1)** | **DITOLAK<br>(Peringkat 4)** | **DITOLAK<br>(Peringkat 3)** | **OPSI UNGGULAN KEDUA<br>(Peringkat 2)** |

---

### 2.3 Justifikasi Ilmiah dan Komprehensif Pemilihan Solusi

Berdasarkan hasil pembobotan kuantitatif pada Tabel 1, **Alternatif 1 (Jaringan Mikroirigasi Perpipaan Cerdas Otomatis Multi-Zonasi)** memperoleh skor tertinggi secara mutlak, yaitu **4,525 dari skala 5,000**, mengungguli Alternatif 4 (skor 4,225), Alternatif 3 (skor 3,475), dan Alternatif 2 (skor 2,850). Secara ilmiah dan teknis, Alternatif 1 ditetapkan sebagai **Solusi Terpilih (*Selected Final Design*)** dengan justifikasi multi-sektoral berikut:

1. **Keunggulan Fisiologis dan Penghematan Air:**  
   Penggunaan emiter tetes kompensasi tekanan (PC Dripper) melepaskan air secara perlahan dan langsung meresap ke dalam zona rizosfer perakaran aktif jeruk limau tanpa membasahi permukaan tajuk kanopi atau mengalir liar di parit. Hal ini mencegah pengikisan butiran pupuk NPK, menekan laju evaporasi tanah hingga tingkat minimal, dan menghindarkan tanaman dari kelembapan mikro tinggi pada pangkal batang yang selama ini memicu serangan jamur *Phytophthora nicotianae* dan cendawan upas.
2. **Efisiensi Aliran Hidrolika dan Toleransi Terhadap Sedimen Sungai:**  
   Penerapan tabung saringan cakram (*disc filter*) 120 mesh dengan pori 130 mikron di sisi hulu pompa secara tuntas memecahkan masalah kekeruhan sedimen sungai Ciberes. Labirin internal emiter PC memiliki mekanisme pembersihan otomatis (*self-flushing diaphragm*), sehingga partikel halus yang lolos tidak menyebabkan penyumbatan dan nilai keseragaman Christiansen tetap terjaga stabil ($CU \ge 88\text{--}92\%$).
3. **Rasionalitas Energi Tenaga Surya dan Keselamatan Listrik:**  
   Dengan konsumsi daya pompa diafragma yang hanya berkisar 60–85 Watt pada siklus siram 56 menit, kebutuhan energi per siklus hanya sebesar ~80 Wh. Kebutuhan ini dapat dipenuhi secara mandiri oleh panel surya 100 Wp dan baterai LiFePO4 12V 30Ah yang memiliki cadangan otonomi hingga 4 siklus siram penuh (mencakup 12 hari mendung tanpa sinar matahari). Beroperasi pada tegangan 12V DC, sistem sepenuhnya memenuhi regulasi keselamatan tegangan ekstra rendah aman (SELV IEC 60364-4-41) bagi pekerja kebun.
4. **Kepatuhan Finansial Terhadap Pagu Anggaran:**  
   Total biaya belanja purwarupa petak uji (15–20 pohon) terhitung sebesar Rp4.300.000, sepenuhnya berada di bawah batas pagu belanja Capstone FTE (maksimal Rp5.000.000). Proyeksi investasi adopsi penuh kebun mitra (600 pohon) terhitung sebesar Rp17.400.000, berada di bawah batas pagu belanja mitra (maksimal Rp18.000.000) dengan periode pengembalian modal yang sangat realistis (14–16 bulan) dari penghematan upah buruh manual.
5. **Posisi Alternatif 4 sebagai Opsi Cadangan Tepat Guna Unggulan:**  
   Meskipun Alternatif 1 menjadi pilihan utama otomatisasi penuh, evaluasi membuktikan bahwa Alternatif 4 (Wahana Gerobak Dorong Irigasi & Logistik Kebun Multifungsi) meraih skor 4,225 sebagai opsi kedua terbaik. Hal ini disebabkan biaya modalnya yang paling rendah (Rp2.450.000) dan nilai guna multifungsi nyata untuk pengangkutan panen buah jeruk limau, menjadikannya opsi komplementer tepat guna yang sangat bernilai tinggi bagi mitra.

---

# BAB 3: DESAIN SOLUSI TERPILIH (DETAILED ENGINEERING DESIGN)

Bab ini memaparkan perancangan detail keteknikan (*detailed engineering design*) untuk solusi terpilih, yaitu **Sistem Jaringan Mikroirigasi Cerdas Multi-Zonasi Mandiri Energi**.

### 3.1 Deskripsi Umum dan Arsitektur Sistem Terpadu

Sistem dirancang sebagai integrasi dari empat (4) subsistem utama yang saling beroperasi secara harmonis:
1. **Subsistem Pembangkit dan Penyimpan Daya Surya (*Off-Grid Power System*):** Pembangkit fotovoltaik monokristalin 100 Wp, unit pengontrol pengisian surya MPPT 12V/10A, dan modul baterai LiFePO4 12V 30Ah (360 Wh) dengan BMS (*Battery Management System*) terintegrasi.
2. **Subsistem Instrumentasi dan Kontroler Cerdas (*Smart Controller & Instrumentation*):** Mikrokontroler 32-bit berdaya rendah ESP32, sensor kelembapan tanah kapasitif tahan korosi, sensor aliran air (*pulse flow meter* YF-S201), jam waktu nyata presisi (RTC DS3231), dan modul relay isolasi optocoupler.
3. **Subsistem Penyedotan dan Filtrasi Partikulat (*Pumping & Dual-Stage Filtration*):** Pompa diafragma elektrik DC 12V 100W *self-priming*, katup searah (*foot valve/check valve*), manometer diferensial, dan tabung filter cakram (*disc filter*) kerapatan 120 mesh (penyaring partikel $\le 130\ \mu\text{m}$).
4. **Subsistem Distribusi Fluida dan Emisi Terkompensasi (*Distribution Manifold & PC Dripper Line*):** Katup selenoid DC 12V *Normally Closed* (NC) untuk kontrol zonasi, pipa utama polietilena (PE 1 inci), pipa lateral (PE 16 mm), dan emiter tetes kompensasi tekanan (*PC Dripper* 8 L/jam, 2 unit per pohon).

Diagram blok arsitektur keterhubungan subsistem disajikan pada Gambar 1:

```text
[ SUNLIGHT ] 
      │
      ▼
[ Solar Panel 100 Wp ] ──► [ MPPT Solar Charge Controller 12V/10A ] ◄──► [ Baterai LiFePO4 12V 30Ah ]
                                           │ (SELV 12V DC Bus)
                                           ├─────────────────────────────────────────┐
                                           ▼                                         ▼
                               [ Box IP65 Kontroler ESP32 ]               [ Pompa Diafragma DC 100W ]
                                 ├─ Sensor Soil Moisture                             │
                                 ├─ Flow Meter YF-S201 ◄─────────┐                   │ (Air Sungai)
                                 ├─ RTC DS3231                   │                   ▼
                                 └─ Modul Relay 12V ──► [ Katup Solenoid NC ] ──► [ Filter 120 Mesh ]
                                                                 │                   │ (Air Bersih)
                                                                 ▼                   ▼
                                                    [ Pipa Lateral PE 16 mm ] ◄──────┘
                                                                 │
                                                                 ▼
                                                  [ 2x PC Dripper 8 L/h ]
                                                                 │
                                                                 ▼
                                                    ( 15-20 Pohon Jeruk Limau )
```
*Gambar 1. Diagram Blok Arsitektur Sistem Mikroirigasi Cerdas Terpilih*

---

### 3.2 Desain Perangkat Keras (*Hardware & Mechanical Design*)

#### 3.2.1 Subsistem Pemompaan dan Hidrolika Perpipaan
* **Pemilihan Pompa:** Pompa diafragma DC 12V tipe *high-pressure self-priming* dengan spesifikasi daya nominal 100 Watt, arus beban 8,0 Ampere, tekanan cut-off 0,8 MPa (8 Bar), dan laju alir bebas (*open flow*) sebesar 8,0 hingga 9,0 Liter/menit (480–540 L/jam). Pompa diafragma dipilih karena memiliki daya hisap kering (*self-priming lift* hingga 2 meter dari muka air sungai), toleran terhadap partikel halus air, dan beroperasi pada tegangan ekstra rendah aman (SELV 12V DC).
* **Pemodelan Kehilangan Tekanan Pipa (*Head Loss*):** Untuk petak uji purwarupa (1 lajur, 20 pohon dengan jarak tanam 1,5 meter, panjang pipa lateral 30 meter), kehilangan tekanan gesek pada pipa lateral PE diameter dalam $D = 13{,}6\text{ mm}$ dihitung menggunakan persamaan Darcy-Weisbach:

$$h_f = f \times \frac{L}{D} \times \frac{v^2}{2g} \quad \text{(Persamaan 1)}$$

Debit total petak uji adalah 20 pohon $\times 16\text{ L/jam} = 320\text{ L/jam} = 8{,}89 \times 10^{-5}\text{ m}^3/\text{s}$. Kecepatan aliran rata-rata fluida dalam pipa adalah $v = 0{,}61\text{ m/s}$. Pada bilangan Reynolds $Re \approx 8.300$ (aliran turbulen halus, faktor gesek $f \approx 0{,}032$), kehilangan tinggi tekan di sepanjang 30 meter pipa lateral terhitung sangat kecil, yaitu $h_f \approx 1{,}34\text{ meter air}$ ($0{,}013\text{ MPa}$). Tekanan sisa di ujung pipa lateral tetap berada pada rentang kerja stabil PC dripper (0,15–0,25 MPa).

* **Emiter Kompensasi Tekanan (PC Dripper):** Setiap pohon dipasangi 2 unit PC Dripper debit 8 L/jam (total debit 16 L/jam per pohon) yang ditusukkan pada pipa lateral PE 16 mm dan diarahkan menggunakan mikrotubing 4/7 mm menuju zona pembasahan akar (radius 0,6 m dari batang). Membran silikon internal dripper secara dinamis menyesuaikan celah aliran saat tekanan fluida berfluktuasi, menjamin variasi debit manufaktur sangat kecil ($C_v < 0{,}04$). Durasi siram untuk menyalurkan dosis tepat 15 Liter air per pohon dihitung melalui:

$$t_{siram} = \frac{V_{target}}{Q_{pohon}} = \frac{15\text{ Liter}}{16\text{ Liter/jam}} = 0{,}9375\text{ jam} = 56{,}25\text{ menit} \quad \text{(Persamaan 2)}$$

#### 3.2.2 Subsistem Filtrasi Sedimen Sungai Ciberes
Air sungai Ciberes diproses melalui saringan tipe cakram (*disc filter*) 1 inci dengan kerapatan elemen 120 mesh (bukaan pori $130\ \mu\text{m}$). Elemen cakram beralur rapat memiliki luas permukaan retensi sedimen yang jauh lebih besar dibandingkan saringan kawat konvensional, sangat efektif menangkap pasir halus dan serpihan ganggang sungai. Dua unit manometer analog (rentang 0–1,0 MPa) dipasang pada sisi masukan (*inlet*) dan keluaran (*outlet*) tabung saringan. Apabila beda tekanan ($\Delta P = P_{in} - P_{out}$) melampaui 0,05 MPa (0,5 Bar), hal tersebut menjadi indikasi visual bagi operator untuk membuka katup pembuang lumpur (*flushing valve*) selama 10 detik guna membersihkan tumpukan sedimen tanpa perlu membongkar tabung filter.

#### 3.2.3 Subsistem Pembangkit dan Cadangan Energi Mandiri (*Off-Grid PV*)
* **Panel Surya:** 1 unit modul fotovoltaik Monokristalin 100 Wp (Tegangan daya maksimum $V_{mp} = 18{,}5\text{ V}$, Arus daya maksimum $I_{mp} = 5{,}41\text{ A}$). Di wilayah Subang dengan rata-rata insolasi surya efektif 4,2 jam matahari puncak (*Peak Sun Hours* / PSH), energi harian yang dihasilkan adalah:

$$E_{harian} = P_{panel} \times PSH \times \eta_{sistem} = 100\text{ W} \times 4{,}2\text{ jam} \times 0{,}75 = 315\text{ Wh/hari} \quad \text{(Persamaan 3)}$$

* **Baterai LiFePO4:** Modul baterai berkapasitas $12{,}8\text{ V}$, $30\text{ Ah}$ (Energi total nominal = $384\text{ Wh}$). Konsumsi energi untuk 1 siklus penyiraman petak uji (durasi $t = 56{,}25\text{ menit} = 0{,}94\text{ jam}$) dengan beban daya pompa (80W) dan kontroler (5W) adalah:

$$E_{siklus} = P_{total} \times t_{operasi} = 85\text{ Watt} \times 0{,}94\text{ jam} = 79{,}9\text{ Wh/siklus} \quad \text{(Persamaan 4)}$$

Dengan batas pelepasan daya aman baterai (*Depth of Discharge* / DoD) sebesar 80% (energi aman terpakai = $307\text{ Wh}$), baterai mampu melayani:

$$N_{siklus} = \frac{307\text{ Wh}}{79{,}9\text{ Wh/siklus}} = 3{,}84\text{ siklus penuh} \approx 4\text{ siklus operasi} \quad \text{(Persamaan 5)}$$

Karena frekuensi penyiraman tanaman dilakukan 3 hari sekali, cadangan energi baterai mampu menyuplai kebutuhan operasional kebun selama minimal 9 hingga 12 hari mendung kontinu tanpa sinar matahari sama sekali, membuktikan keandalan sistem melampaui batasan C-01 dan spesifikasi S-06 ($\ge 8$ jam operasi).

#### 3.2.4 Selungkup Proteksi Lingkungan IP65 dan Keselamatan Listrik SELV
Seluruh modul elektronika (ESP32, modul relay, SCC MPPT, terminal kabel blok) dirakit di dalam kotak selungkup polikarbonat (*industrial junction box*) dimensi $300 \times 200 \times 160\text{ mm}$ dengan seal karet silikon berstandar proteksi IEC 60529 IP65. Seluruh kabel masukan dan keluaran melalui lubang kelenjar kabel (*cable gland* IP68) kedap air. Sistem beroperasi penuh pada tegangan DC 12 Volt, memenuhi batas keselamatan tegangan ekstra rendah aman (*Safety Extra-Low Voltage* / SELV $\le 48\text{ V DC}$) sesuai standar IEC 60364-4-41, sehingga bebas dari bahaya sengatan listrik bagi pekerja di area parit pertanian basah.

---

### 3.3 Desain Perangkat Lunak & Algoritma (*Software Design*)

Perangkat lunak pengendali dikembangkan berbasis bahasa C++ pada lingkungan ESP-IDF / Arduino core untuk mikrokontroler ESP32. Firmware dirancang dengan arsitektur mesin keadaan terhingga (*Finite State Machine* / FSM) hemat energi.

#### 3.3.1 Diagram Alir Logika Kontrol Sistem (*Flowchart*)
Alur kerja program mencakup tahapan-tahapan eksekusi:

```text
[ START: WAKE UP DARI DEEP SLEEP / TOMBOL MANUAL ]
                      │
                      ▼
        [ Inisialisasi I/O & Baca RTC ]
                      │
                      ▼
          [ Cek Tegangan Baterai ]
                      │
            V_bat >= 11.8 V ? ───(TIDAK)──► [ Catat Error Undervoltage ] ──► [ SLEEP ]
                      │ (YA)
                      ▼
         [ Baca Sensor Soil Moisture ]
                      │
            Lengas < Ambang 45% ? ──(TIDAK)─► [ Tanah Lembap, Tidak Perlu Siram ] ──► [ SLEEP ]
                      │ (YA)
                      ▼
     [ Buka Solenoid Valve & Nyalakan Pompa ]
                      │
                      ▼
      [ Loop: Baca Pulsa Flow Meter YF-S201 ]
      [ Akumulasi Volume Air: V_total += V_pulsa ]
                      │
            V_total >= V_target ? ──(TIDAK)─► [ Lanjutkan Siram (Monitor Tekanan) ]
                      │ (YA)
                      ▼
     [ Matikan Pompa & Tutup Solenoid Valve ]
                      │
                      ▼
    [ Catat Log Operasi & Masuki Mode Deep Sleep ]
```
*Gambar 2. Diagram Alir Algoritma Kontrol Mikroskopis Penyiraman*

#### 3.3.2 Logika Pengendalian dan Pseudocode
```cpp
// Pseudocode Logika Kontrol Irigasi Presisi CD-3
void setup() {
    initHardwarePins();
    readRTC();
    float vBat = readBatteryVoltage();
    
    if (vBat < 11.8) {
        logEvent("Low Battery Warning! Operation Aborted.");
        enterDeepSleepUntilNextSchedule();
    }
    
    float soilMoisture = readCapacitiveSoilSensor();
    bool manualButtonPressed = checkManualButtonTrigger();
    bool isScheduledTime = checkScheduledHour(7) || checkScheduledHour(16);
    
    if ((isScheduledTime && soilMoisture < 45.0) || manualButtonPressed) {
        executeIrrigationCycle(TARGET_VOLUME_LITERS);
    }
    
    enterDeepSleepUntilNextSchedule();
}

void executeIrrigationCycle(float targetLiters) {
    openSolenoidValve();
    delay(500); // Stabilisasi katup
    startWaterPump();
    
    float currentVolume = 0.0;
    unsigned long startTime = millis();
    unsigned long maxSafetyTimeout = 70 * 60 * 1000; // 70 menit batas aman
    
    while (currentVolume < targetLiters && (millis() - startTime) < maxSafetyTimeout) {
        currentVolume = readFlowMeterAccumulatedLiters();
        if (checkFilterPressureDifferential() > 0.6) {
            triggerCloggingAlarm();
        }
        delay(100);
    }
    
    stopWaterPump();
    closeSolenoidValve();
    logIrrigationData(currentVolume, millis() - startTime);
}
```

---

### 3.4 Daftar Kebutuhan Komponen dan Bahan (*Bill of Materials* / BOM)

Rancangan anggaran belanja komponen disusun ke dalam dua tingkatan akuntabilitas rekayasa yang transparan dan terverifikasi harga pasar lokal riil:

#### Tabel 2. Bill of Materials (BOM) Purwarupa Mahasiswa (Petak Uji 15–20 Pohon)

| No | Komponen / Perangkat | Spesifikasi Teknis | Kuantitas | Estimasi Harga Satuan (Rp) | Total Biaya (Rp) | Justifikasi Fungsi Teknis |
|:---:|---|---|:---:|:---:|:---:|---|
| 1 | Panel Surya Monokristalin | 100 Wp, 18,5V Monocrystalline | 1 unit | 620.000 | 620.000 | Sumber energi mandiri off-grid (C-01) |
| 2 | Baterai LiFePO4 | 12,8V 30Ah + BMS terintegrasi | 1 unit | 1.350.000 | 1.350.000 | Penyimpan daya cadangan > 8 jam (S-06) |
| 3 | Solar Charge Controller | MPPT 12V/10A LCD Auto Detect | 1 unit | 280.000 | 280.000 | Pengatur pengisian daya baterai presisi |
| 4 | Pompa Diafragma DC | 12V 100W 8 L/m Self-Priming | 1 unit | 240.000 | 240.000 | Pompa fluida berdaya rendah aman (C-04) |
| 5 | Disc Filter Pertanian | 1 inci kerapatan 120 mesh | 1 unit | 145.000 | 145.000 | Penyaring partikel sedimen sungai (S-05) |
| 6 | Katup Selenoid DC | 12V NC 1/2 inci Food Grade | 2 unit | 75.000 | 150.000 | Pengatur aliran zonasi otomatis |
| 7 | Emiter PC (Kompensasi Tekanan) | Debit 8 L/jam (Netafim/Rainbird) | 40 unit | 4.500 | 180.000 | Penjamin keseragaman CU >= 85% (S-02) |
| 8 | Pipa Utama PE | Diameter 1 inci (OD 32 mm), PN 6 | 20 meter | 11.000 | 220.000 | Jalur transmisi fluida utama |
| 9 | Pipa Lateral PE | Diameter 16 mm (OD 16 mm), PN 4 | 40 meter | 4.000 | 160.000 | Pipa distribusi tetes petak uji pohon |
| 10 | Mikrotubing & Fitting Nepel | Selang 4/7 mm + tusuk end plug | 1 set | 95.000 | 95.000 | Konektor emiter ke zona perakaran pohon |
| 11 | Mikrokontroler ESP32 | ESP32-WROOM-32D Development Board | 1 unit | 75.000 | 75.000 | Otak pengendali algoritma dan FSM |
| 12 | Modul Jam Waktu Nyata (RTC) | DS3231 High Precision I2C | 1 unit | 35.000 | 35.000 | Penjadwalan siram presisi pagi/sore |
| 13 | Sensor Aliran Air | YF-S201 Hall Effect Flow Meter | 1 unit | 45.000 | 45.000 | Pengukur volume air 15 L terverifikasi (S-01)|
| 14 | Sensor Lengas Tanah | Capacitive Soil Moisture v1.2 | 2 unit | 25.000 | 50.000 | Monitoring ambang batas kekeringan tanah |
| 15 | Modul Relay Optocoupler | 4-Channel 12V Optocoupler Isolation | 1 unit | 35.000 | 35.000 | Sakelar isolasi penggerak pompa & selenoid |
| 16 | Selungkup Kedap Air IP65 | Box Polikarbonat 300x200x160 + Gland | 1 unit | 165.000 | 165.000 | Proteksi debu dan air IP65 (S-07) |
| 17 | Kabel, Sakelar, & Aksesoris | Kabel NYAF 2x1,5 mm, fuse, terminal | 1 set | 110.000 | 110.000 | Kelengkapan elektrikal standar SELV |
| 18 | Rangka Penopang PV & Manometer | Braket besi siku lubang + Manometer | 1 set | 190.000 | 190.000 | Dudukan panel surya dan monitor filter |
| **TOTAL** | **Belanja Komponen Purwarupa** | **Lengkap Petak Uji (15–20 Pohon)** | | | **Rp4.300.000** | **Terbukti Patuh Plafon <= Rp5.000.000** |

#### Tabel 3. Proyeksi Anggaran Implementasi Skala Penuh Kebun (600 Pohon, Lahan ~3.000 m²)

| No | Kategori Alokasi Perangkat | Rincian Spesifikasi Perbanyakan Modular | Estimasi Biaya (Rp) |
|:---:|---|---|:---:|
| 1 | Pembangkit PLTS Skala Penuh | 2 unit Panel Surya 150 Wp (300 Wp) + SCC MPPT 30A | 2.850.000 |
| 2 | Penyimpan Daya LiFePO4 Skala Penuh | Baterai LiFePO4 24V 50Ah (1.200 Wh) + BMS Industri | 4.800.000 |
| 3 | Subsistem Pompa Distribusi Utama | Pompa Sentrifugal DC 24V 250W Laju Alir 35 L/m | 1.450.000 |
| 4 | Filtrasi Ganda Skala Industri | 2 unit Disc Filter 1,5 inci 120 mesh paralel + Auto-Flush | 950.000 |
| 5 | Jaringan Pipa Distribusi Utama | Pipa PVC/PE 1,5 inci (150 m) + Fitting Manifold | 1.850.000 |
| 6 | Jaringan Pipa Lateral Kebun | Pipa PE 16 mm (panjang total 650 m untuk 3 lajur parit) | 2.600.000 |
| 7 | Emiter PC & Selang Cincin | 1.200 unit PC Dripper 8 L/h (2 per pohon untuk 600 pohon) | 2.160.000 |
| 8 | Katup Selenoid Zonasi Kebun | 6 unit Solenoid Valve 1 inci (pembagian 6 zona siram) | 780.000 |
| 9 | Kotak Kontroler Utama & Sensor | ESP32 Industrial Box IP65 + 6 Node Sensor Soil RS485 | 850.000 |
| 10 | Fabrikasi Braket & Pemasangan Lapangan | Dudukan panel surya permanen, pondasi pompa, pelindung pipa | 1.250.000 |
| **TOTAL** | **Proyeksi Investasi Komersial Penuh** | **Melayani Seluruh 600 Pohon Kebun Mitra Ciberes** | **Rp19.540.000** |
| *(Optimalisasi)* | *Negosiasi Pengadaan Grosir (Diskon 10–12%)* | *Pengadaan borongan pipa & emiter langsung distributor* | **Rp17.400.000** *(Patuh <= Rp18.000.000)* |

---

# BAB 4: JADWAL DAN ANGGARAN PELAKSANAAN

Bab ini menyusun linimasa pengerjaan fisik tugas akhir yang dibatasi maksimal enam (6) bulan pelaksanaan serta rencana anggaran biaya dan pembagian tugas terperinci antar-anggota tim.

### 4.1 Rencana Jadwal Pengerjaan (*Gantt Chart* 6 Bulan Pelaksanaan)

Pelaksanaan proyek Capstone Design dirancang berlangsung selama 24 pekan (6 bulan), terbagi ke dalam enam fase terstruktur:

#### Tabel 4. Jadwal Pelaksanaan Proyek Capstone Design (Gantt Chart 24 Pekan)

| No | Tahapan Kegiatan Pelaksanaan | Bulan 1 | Bulan 2 | Bulan 3 | Bulan 4 | Bulan 5 | Bulan 6 | Target Luaran Terukur |
|:---:|---|:---:|:---:|:---:|:---:|:---:|:---:|---|
| 1 | **Fase 1: Pengadaan & Uji Modul** | [====] | | | | | | Seluruh komponen BOM purwarupa tiba & lulus uji kontinuitas bangku tes |
| 2 | **Fase 2: Fabrikasi Elektrikal & Box IP65** | | [====] | | | | | Rangkaian PCB/modul terakit dalam selungkup IP65 lulus uji semprot IEC 60529 |
| 3 | **Fase 3: Pengembangan Firmware ESP32** | | | [====] | | | | Kode program algoritma FSM tuntas & terverifikasi logika pembacaan sensor |
| 4 | **Fase 4: Integrasi Lab & Kalibrasi Hidrolika** | | | | [====] | | | Purwarupa terintegrasi penuh di lab, akurasi flow meter & emiter PC terkalibrasi |
| 5 | **Fase 5: Pemasangan Lapangan & Pengujian** | | | | | [====] | | Sistem terpasang di petak uji Ciberes, data uji CU >= 85% & dosis 15 L terhimpun |
| 6 | **Fase 6: Evaluasi, Laporan CD-4/CD-5 & Paper** | | | | | | [====] | Dokumen CD-4, CD-5, dan draf manuskrip publikasi ilmiah selesai disusun |

---

### 4.2 Rencana Anggaran Biaya (RAB) Pelaksanaan

Rencana anggaran biaya operasional pelaksanaan tugas akhir mahasiswa disusun sebagai berikut:

#### Tabel 5. Rencana Anggaran Biaya (RAB) Total Pelaksanaan Capstone Design

| No | Kategori Pengeluaran | Alokasi Rincian | Jumlah Biaya (Rp) | Sumber Pendanaan |
|:---:|---|---|:---:|:---:|
| 1 | Pengadaan Komponen Purwarupa Fisik | 18 item komponen BOM Petak Uji (Tabel 2) | 4.300.000 | Mandiri Tim & Usulan Hibah TA |
| 2 | Fabrikasi Mekanikal & Bengkel | Pengelasan dudukan panel surya, klem pipa, dudukan pompa | 350.000 | Mandiri Tim |
| 3 | Logistik & Transportasi Pengujian Lapangan | 3x perjalanan pulang-pergi Bandung–Subang (survei, pasang, uji) | 900.000 | Mandiri Tim |
| 4 | Alat Ukur & Kalibrasi Pengujian | Silinder ukur bertingkat, wadah bejana ukur Christiansen, bor tanah | 250.000 | Laboratorium FTE & Mandiri |
| 5 | Dokumentasi, Administrasi & Publikasi | Cetak lembar pengesahan, poster capstone, biaya registrasi seminar | 450.000 | Mandiri Tim |
| **TOTAL** | **Rencana Anggaran Biaya Pelaksanaan** | **Realisasi Total Capstone Design Tim Mahasiswa** | **Rp6.250.000** | **Alokasi Tim Terjangkau** |

---

### 4.3 Pembagian Tugas Kelompok (*Team Roles & Job Descriptions*)

Guna memenuhi tuntutan profesionalisme kerja tim dan rubrik penilaian CLO4, pembagian peran dan tanggung jawab spesifik ditetapkan secara merata pada Tabel 6:

#### Tabel 6. Pembagian Peran dan Tugas Anggota Tim Mahasiswa

| No | Nama / NIM | Posisi / Peran | Tanggung Jawab Spesifik dan Target Luaran Utama |
|:---:|---|---|---|
| 1 | **Muhammad Al Qarnie** <br>*(NIM: 101032330043)* | **Ketua Tim / *System & Firmware Engineer*** | • Mengoordinasi keseluruhan linimasa dan kepatuhan terhadap Buku Panduan Capstone.<br>• Merancang arsitektur sistem terpadu dan diagram blok logika keterhubungan.<br>• Mengembangkan *firmware* kontrol ESP32 (arsitektur FSM, RTC, dan algoritma siram).<br>• Mengintegrasikan sensor aliran air (*flow meter*) dan katup selenoid zonasi.<br>• Bertanggung jawab penuh atas penyusunan dan finalisasi dokumen laporan CD-3 dan CD-4. |
| 2 | **Maheswara Ariq Athallah** <br>*(NIM: 101032300050)* | **Anggota / *Power & Hardware Engineer*** | • Merancang subsistem pembangkit surya fotovoltaik (panel 100 Wp & MPPT).<br>• Menghitung neraca daya baterai LiFePO4 12V 30Ah dan pengujian otonomi energi mandiri (S-06).<br>• Merancang tata letak sirkuit elektrikal, pengkabelan SELV, dan proteksi sekring.<br>• Menguji ketahanan lingkungan selungkup polikarbonat rating IP65 (S-07).<br>• Bertanggung jawab atas pengadaan komponen elektronika dan pencatatan audit nota BOM. |
| 3 | **Daffa Hermansyah** <br>*(NIM: 101032330090)* | **Anggota / *Hydraulics & Field Testing Engineer*** | • Merancang jaringan perpipaan fluida (pipa PE 1 inci & lateral 16 mm) dan pemilihan emiter PC.<br>• Merancang dan menguji efektivitas tabung saringan partikulat 120 mesh terhadap sedimen sungai.<br>• Memimpin instalasi fisik mekanikal petak uji percontohan di kebun jeruk limau Ciberes.<br>• Menjalankan protokol uji keseragaman distribusi Christiansen ($CU \ge 85\%$) menggunakan bejana ukur.<br>• Bertanggung jawab atas komunikasi teknis lapangan bersama mitra pengelola kebun. |

---

# DAFTAR PUSTAKA

[1] R. G. Allen, L. S. Pereira, D. Raes, and M. Smith, *Crop Evapotranspiration: Guidelines for Computing Crop Water Requirements*, FAO Irrigation and Drainage Paper 56. Rome, Italy: Food and Agriculture Organization of the United Nations (FAO), 1998, ISBN: 92-5-104219-5. [Online]. Available: https://www.fao.org/4/x0490e/x0490e00.htm

[2] American Society of Agricultural and Biological Engineers, *Procedure for Sprinkler Testing and Performance Reporting*, Standard ANSI/ASAE S398.1. St. Joseph, MI, USA: ASABE, 2021. [Online]. Available: https://elibrary.asabe.org/abstract.asp?aid=41295

[3] American Society of Agricultural and Biological Engineers, *Design and Installation of Microirrigation Systems*, Standard ASAE EP405.1. St. Joseph, MI, USA: ASABE, 2019. [Online]. Available: https://elibrary.asabe.org/abstract.asp?aid=32022

[4] International Electrotechnical Commission, *Degrees of Protection Provided by Enclosures (IP Code)*, Standard IEC 60529:1989+AMD1:1999+AMD2:2013 CSV. Geneva, Switzerland: IEC, 2013. [Online]. Available: https://webstore.iec.ch/publication/2452

[5] Badan Standardisasi Nasional, *Derajat Proteksi yang Diberikan oleh Selungkup (Kode IP)*, SNI IEC 60529:2014. Jakarta, Indonesia: BSN, 2014. [Online]. Available: https://pesta.bsn.go.id/produk/detail/9726-sniiec605292014

[6] Republik Indonesia, *Peraturan Pemerintah Republik Indonesia Nomor 20 Tahun 2006 tentang Irigasi*, Lembaran Negara Republik Indonesia Tahun 2006 Nomor 46. Jakarta, Indonesia: Sekretariat Negara RI, 2006. [Online]. Available: https://peraturan.bpk.go.id/Details/48943/pp-no-20-tahun-2006

[7] Kementerian Pertanian Republik Indonesia, *Pedoman Teknis Pengembangan Tata Air Pertanian*, Peraturan Menteri Pertanian No. 49/Permentan/OT.140/4/2014 juncto SNI 7608:2010 (Jaringan Irigasi Air Tanah Dangkal). Jakarta, Indonesia: Kementan RI, 2014.

[8] International Organization for Standardization, *Agricultural irrigation equipment — Emitters and emitting pipe — Specification and test methods*, Standard ISO 9261:2004. Geneva, Switzerland: ISO, 2004. [Online]. Available: https://www.iso.org/standard/38072.html

[9] International Electrotechnical Commission, *Photovoltaic (PV) stand-alone systems - Design verification*, Standard IEC 62124:2004. Geneva, Switzerland: IEC, 2004. [Online]. Available: https://webstore.iec.ch/publication/6504

[10] International Electrotechnical Commission, *Low-voltage electrical installations - Part 4-41: Protection for safety - Protection against electric shock*, Standard IEC 60364-4-41:2005+AMD1:2017 CSV. Geneva, Switzerland: IEC, 2017. [Online]. Available: https://webstore.iec.ch/publication/60074

[11] IEEE Standards Association, *IEEE Standard for a Smart Transducer Interface for Sensors and Actuators - Mixed-Mode Communication Protocols and Transducer Electronic Data Sheet (TEDS) Formats*, IEEE Std 1451.4-2004. New York, NY, USA: IEEE, 2004, doi: 10.1109/IEEESTD.2004.95745.

[12] N. Elkaoud, S. Ismail, R. Mahmoud, H. Taraby, S. Shang, D. Wang, and M. Rayan, “Efficient and Effective Irrigation Water Management Using Sprinkler Robot,” *Eng*, vol. 6, no. 7, art. 138, pp. 1–18, Jun. 2025, doi: 10.3390/eng6070138.

[13] R. S. Ayers and D. W. Westcot, *Water Quality for Agriculture*, FAO Irrigation and Drainage Paper 29 Rev. 1. Rome, Italy: Food and Agriculture Organization of the United Nations (FAO), 1985, ISBN: 92-5-102263-1. [Online]. Available: https://www.fao.org/4/t0234e/t0234e00.htm

[14] J. Shortridge and B. Benham, “Filtration, Treatment, and Maintenance Considerations for Micro-Irrigation Systems,” Virginia Cooperative Extension, Virginia Tech, Publication 442-757, 2023. [Online]. Available: https://www.pubs.ext.vt.edu/442/442-757/442-757.html

[15] S. Bounoua, S. Tomas, J. Labille, B. Molle, J. Granier, P. Haldenwang, and S. N. Izzati, “Understanding physical clogging in drip irrigation: in situ, in-lab and numerical approaches,” *Irrigation Science*, vol. 34, no. 4, pp. 327–342, 2016, doi: 10.1007/s00271-016-0506-8.

[16] Y. Shen, J. Puig-Bargués, M. Li, Y. Xiao, Q. Li, and Y. Li, “Physical, chemical and biological emitter clogging behaviors in drip irrigation systems using high-sediment loaded water,” *Agricultural Water Management*, vol. 270, art. 107738, 2022, doi: 10.1016/j.agwat.2022.107738.

[17] R. Lavanholi, B. Molle, R. J. R. Ramos, and A. P. Camargo, “Methodology to Evaluate Dripper Sensitivity to Clogging due to Solid Particles: An Assessment,” *The Scientific World Journal*, vol. 2018, art. 7697458, pp. 1–9, 2018, doi: 10.1155/2018/7697458.

[18] W. R. Walker, *Guidelines for Designing and Evaluating Surface Irrigation Systems*, FAO Irrigation and Drainage Paper 45. Rome, Italy: Food and Agriculture Organization of the United Nations (FAO), 1989, ISBN: 92-5-102879-6. [Online]. Available: https://www.fao.org/4/t0231e/t0231e00.htm

[19] R. Budiarto, R. Poerwanto, E. Santosa, and D. Efendi, “The Potentials of Limau (Citrus amblycarpa Hassk. Ochse) as A Functional Food and Ornamental Mini Tree Based on Metabolomic and Morphological Approaches,” *Journal of Tropical Crop Science*, vol. 4, no. 2, pp. 49–57, 2017, doi: 10.29244/jtcs.4.2.49-57.

[20] D. M. Kadyampakeni, K. T. Morgan, M. Zekri, A. W. Schumann, S. Guzmán, F. Alferez, M. A. Shahid, and T. A. Obreza, “2023–2024 Florida Citrus Production Guide: Irrigation Management of Citrus Trees,” University of Florida IFAS Extension, EDIS Publication CG093/CPG12, 2023, doi: 10.32473/edis-cg093-2023.

[21] J. H. Graham and L. W. Timmer, “Phytophthora Diseases of Citrus,” University of Florida IFAS Extension, EDIS Publication SL127/CH087, 2020. [Online]. Available: https://edis.ifas.ufl.edu/publication/CH087

[22] A. G. Smajstrla, B. J. Boman, D. Z. Haman, D. J. Pitts, and F. S. Zazueta, “Field Evaluation of Microirrigation Water Application Uniformity,” University of Florida IFAS Extension, Publication BUL265/AE094, 1997, doi: 10.32473/edis-ae094-1997.

[23] T. A. Obreza, M. Zekri, and S. H. Futch, “Nutrition of Florida Citrus Trees, 3rd Edition: Chapter 3. General Soil Fertility and Citrus Tree Nutrition,” University of Florida IFAS Extension, Publication SL457/SS670, 2020, doi: 10.32473/edis-ss670-2020.

[24] Nurwidiana, W. Fatmawati, dan A. Rifa'i, “Perancangan Alat Penyiram Lahan Bawang Merah Berbasis Teknologi Solar Fotovoltaik,” *Jurnal PASTI (Penelitian dan Aplikasi Sistem dan Teknik Industri)*, vol. 15, no. 1, hlm. 61–70, 2021.

[25] H. Hartung and L. Pluschke, *The Benefits and Risks of Solar-Powered Irrigation: A Global Overview*. Rome, Italy: Food and Agriculture Organization of the United Nations (FAO), 2018, ISBN: 978-92-5-130479-2. [Online]. Available: https://www.fao.org/4/i9047en/I9047EN.pdf

[26] G. Li, X. Li, and Q. Zeng, “Development of automatic irrigation and soil moisture monitoring system based on solar energy in citrus orchard,” *Transactions of the Chinese Society of Agricultural Engineering*, vol. 28, no. 12, pp. 140–145, 2012, doi: 10.3969/j.issn.1002-6819.2012.12.024.

[27] N. Durga, S. L. Postigo, and M. Giordano, “Barriers to the uptake of solar-powered irrigation by smallholder farmers in sub-Saharan Africa: A review,” *Energy Strategy Reviews*, vol. 51, art. 101294, 2024, doi: 10.1016/j.esr.2024.101294.

[28] Tim Peneliti Capstone Design, “Dokumen CD-1: Analisis Permasalahan Penyiraman Manual pada Kebun Jeruk Limau di Ciberes Subang,” Program Studi S1 Teknik Komputer, Universitas Telkom, Oktober 2026.

[29] Tim Peneliti Capstone Design, “Dokumen CD-2: Spesifikasi dan Batasan Desain Sistem Irigasi Kebun Jeruk Limau di Ciberes Subang,” Program Studi S1 Teknik Komputer, Universitas Telkom, Oktober 2026.

