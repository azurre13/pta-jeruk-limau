# DOKUMEN CD-2: SPESIFIKASI DAN BATASAN PERANCANGAN SISTEM IRIGASI KEBUN JERUK LIMAU DI CIBERES SUBANG

**Program Studi S1 Teknik Komputer**  
**Fakultas Teknik Elektro, Universitas Telkom, Bandung**  
**Tahun Akademik 2026/2027**

---

### Data Dokumen dan Lembar Pengesahan (Tabel 0 & Tabel 1)

| Parameter | Nilai / Keterangan |
|---|---|
| **Judul Capstone Design** | Analisis Permasalahan Penyiraman Manual pada Kebun Jeruk Limau di Ciberes Subang |
| **Jenis Dokumen** | Spesifikasi |
| **Nomor Dokumen** | FTE-CD-2 |
| **Nomor Revisi** | 00 |
| **Tanggal Pengesahan** | 29 Oktober 2026 |
| **Fakultas** | Fakultas Teknik Elektro |
| **Program Studi** | S1 Teknik Komputer |
| **Jumlah Halaman** | 25 halaman |

**Tim Penulis (Mahasiswa):**
1. Muhammad Al Qarnie / NIM: 101032330043
2. Maheswara Ariq Athallah / NIM: 101032300050
3. Daffa Hermansyah / NIM: 101032330090

**Disetujui Oleh:**  
Dr. Agung Nugroho Jati, S.T., M.T. (Jabatan: Pembimbing 1)

---

### Timeline Revisi Dokumen (Tabel 2)

| Versi, Tanggal | Revisi | Perbaikan yang Dilakukan | Halaman Revisi |
|---|---|---|---|
| 00, 28 Oktober 2026 | Draf Final CD-2 | Penyelarasan komprehensif dasar penentuan spesifikasi berbasis multi-pilar (wawancara mitra mendalam Audio 1 & Audio 2 Ciberes, regulasi PP No. 20/2006 & Permentan 49/2014, standar ASABE/IEC/ISO/SNI, literatur fisiologi jeruk & sedimen FAO-56/FAO-29), penetapan demarkasi batasan skala purwarupa fungsional (*pilot testbed* 15–20 pohon) dengan skalabilitas penuh 600 pohon, penyempurnaan matriks batasan rekayasa dan spesifikasi kuantitatif terukur (S-01 s.d. S-14) dengan rasionalisasi pagu belanja purwarupa mahasiswa ($\le \text{Rp5.000.000}$) serta proyeksi investasi skala penuh mitra ($\le \text{Rp18.000.000}$), perumusan protokol verifikasi pengujian, perapian rumus matematis berbasis standar Equation Word OMML / LaTeX, serta pembersihan istilah dwibahasa dan pemutakhiran daftar pustaka tervalidasi DOI. | Seluruh Dokumen |
| | | *(Disediakan untuk catatan revisi dosen pembimbing)* | |
| | | *(Disediakan untuk catatan revisi dosen pembimbing)* | |

---

# BAB 1: SPESIFIKASI DAN BATASAN DESAIN SISTEM IRIGASI

Dokumen CD-2 ini merupakan kelanjutan langsung dan berkesinambungan dari dokumen CD-1 (*Analisis Permasalahan Penyiraman Manual pada Kebun Jeruk Limau di Ciberes Subang*) yang telah disahkan oleh dosen pembimbing. Jika CD-1 berfokus pada identifikasi akar permasalahan operasional, pemetaan tapak lahan eksisting, kendala ketiadaan listrik jala-jala, inefisiensi tenaga kerja manual, serta analisis kelemahan solusi terdahulu, maka dokumen CD-2 ini secara formal menetapkan landasan batasan rekayasa mutlak dan spesifikasi kuantitatif terukur yang wajib dipenuhi oleh solusi rekayasa pada tahap perancangan CD-3.

Perumusan batasan dan spesifikasi ini dirancang secara terukur, realistis terhadap kondisi fisik tapak, memiliki landasan ilmiah dan regulasi yang kokoh, serta berprinsip netral terhadap pilihan alternatif solusi (*solution-agnostic*). Selaras dengan ketentuan Buku Panduan Capstone Design FTE Telkom University (2024), ruang lingkup luaran fisik tugas akhir difokuskan pada perancangan dan pembuktian kinerja purwarupa fungsional (*functional working prototype*) pada petak uji representatif (*pilot testbed*) kebun mitra, dengan rancang bangun modular yang secara terstruktur dapat diperluas (*scalable*) untuk mencakup populasi penuh kebun. Pendekatan ini memastikan bahwa ruang eksplorasi desain pada tahap CD-3 tetap terbuka luas untuk membandingkan sekurang-kurangnya tiga konsep alternatif solusi—seperti jaringan mikroirigasi perpipaan terotomasi, wahana mekanis gerak semi-otonom berselang, maupun arsitektur hibrida—tanpa penguncian dini pada satu opsi perangkat keras tertentu.

---

## 1.1 Dasar Penentuan Spesifikasi

Penetapan batasan rekayasa dan spesifikasi kuantitatif dalam dokumen ini tidak didasarkan pada perkiraan subjektif, melainkan merupakan hasil sintesis multi-pilar yang mengintegrasikan empat fondasi rujukan: (1) kebutuhan riil pengguna dan data faktual lapangan hasil wawancara mitra, (2) kerangka regulasi pemerintah dan standar teknis konsensus industri, (3) literatur ilmiah fisiologi tanaman jeruk limau dan pemodelan neraca air, serta (4) karakteristik tapak lahan eksisting dan keterbatasan sumber daya lingkungan.

### 1.1.1 Kebutuhan Pengguna dan Hasil Wawancara Lapangan Mitra Ciberes

Kebutuhan pengguna diperoleh secara primer melalui observasi lapangan mendalam dan rekaman wawancara langsung bersama mitra pengelola kebun jeruk limau di Desa Ciberes, Kecamatan Patokbeusi, Kabupaten Subang, Jawa Barat (terdokumentasi dalam Transkrip Wawancara Audio 1 dan Audio 2, terlampir). Dari penuturan mitra dan verifikasi tim, teridentifikasi fakta-fakta kunci dan kebutuhan esensial sebagai berikut:

1. **Beban Biaya Tenaga Kerja Manual dan Struktur Pengeluaran Mitra**  
   Populasi tanaman kebun berjumlah sekitar 500 hingga 600 pohon jeruk limau yang tertata pada lahan memanjang seluas ~3.000 m² (panjang lintasan ~100 m hingga 117,52 m). Untuk menyiram seluruh pohon tersebut, pengelola kebun mempekerjakan 4 orang buruh harian lepas dengan upah masing-masing Rp100.000 per kegiatan (total pengeluaran Rp400.000 per satu kali siram). Pada musim kemarau dan fase pembungaan/pembuahan, penyiraman wajib dilakukan rutin rata-rata 3 hari sekali (~10 hingga 12 kali per bulan). Skenario perhitungan tahunan menunjukkan estimasi akumulasi upah tenaga kerja mencapai Rp48.700.000 per tahun. Mengingat total biaya modal pembukaan lahan mitra telah menyentuh sekitar Rp90.000.000, beban upah manual ini sangat memberatkan arus kas usaha tani. Pengelola secara tegas menginginkan adanya mekanisasi atau otomasi yang mampu menggantikan pekerjaan fisik menimba dan mengguyur air agar biaya tenaga kerja dapat dipangkas secara drastis [31].

2. **Ketidakpastian Dosis Air dan Keterbatasan Tenaga Fisik**  
   Pekerjaan penyiraman eksisting dilakukan dengan menyedot air sungai ke dalam parit, kemudian 4 pekerja berjalan menyusuri barisan parit untuk menimba air menggunakan wadah ember kecil (kapasitas sekitar 5 Liter) dan mengguyurkannya manual ke pangkal tanaman sebanyak 2 hingga 3 kali guyuran. Estimasi empiris petani adalah sekitar 10 hingga 15 Liter per pohon, namun volume riil per pohon tidak pernah diukur secara presisi. Ketidakseragaman takaran sangat rentan terjadi akibat kelelahan fisik pekerja di tengah terik matahari Subang, di mana pohon-pohon di barisan awal parit kerap menerima air berlebih, sementara pohon di baris tengah hingga ujung parit rawan kekurangan pasokan air.

3. **Kendala Operasional Pompa Bensin Eksisting dan Kegagalan Modifikasi LPG**  
   Suplai air kebun mengandalkan pompa mesin pembakaran internal bensin (merk Alkon diameter pipa 2 inci, berbahan bakar Pertalite) untuk menyedot air dari sungai/saluran irigasi yang berjarak 20,54 meter dari tepi kebun menuju parit tanah. Mitra sempat melakukan modifikasi mekanis dengan mengganti bahan bakar bensin menggunakan tabung gas LPG 3 kg untuk menekan biaya operasional. Namun, eksperimen tersebut terpaksa dihentikan permanen karena blok mesin pompa mengalami kenaikan suhu ekstrem (*overheating*), tarikan mesin tidak stabil, serta menimbulkan kekhawatiran bahaya kebakaran di area basah. Oleh karena itu, mitra membutuhkan sistem penggerak atau pompa baru yang andal, aman, bersuara tenang, dan tidak menimbulkan komplikasi perawatan mekanik.

4. **Kebutuhan Proteksi Hara Pemupukan Jeruk**  
   Pohon jeruk limau di kebun Ciberes dipupuk secara periodik sebanyak dua kali dalam setahun menggunakan kombinasi pupuk NPK dan pupuk organik/kandang yang dibenamkan melingkar di sekeliling tajuk perakaran. Mitra menyampaikan bahwa metode guyuran manual ember bervolume besar kerap menimbulkan aliran limpasan permukaan yang mengikis tanah gembur dan menghanyutkan butiran pupuk ke dasar parit galian sebelum sempat diserap oleh akar serabut. Hal ini menegaskan perlunya sistem penyiraman yang mampu mendistribusikan air secara perlahan dan terarah ke zona perakaran tanpa memicu erosi hara.

5. **Ekspektasi Kinerja Solusi Rekayasa Baru**  
   Mitra mengharapkan sistem irigasi baru memiliki target keandalan yang konkret: (a) mampu menjamin kepastian pasokan air 10–15 Liter per pohon secara merata, (b) memiliki biaya operasional per siklus yang sangat rendah sehingga modal investasi dapat lekas kembali dalam 1–2 musim panen, (c) mudah dioperasikan oleh pekerja lokal melalui pengoperasian tombol tunggal (*single-touch*) tanpa prosedur perangkat lunak yang rumit, serta (d) komponen sistem tahan terhadap paparan cuaca luar ruangan dan lumpur tanah sawah [31].

### 1.1.2 Regulasi Pemerintah dan Standar Teknis Industri

Sistem rekayasa pertanian modern wajib mematuhi kerangka hukum tata kelola air nasional serta standar teknik konsensus industri internasional:

1. **Standar Evaluasi dan Desain Keseragaman Irigasi Mikro (ANSI/ASAE S398.1 & ASAE EP405.1)**  
   American Society of Agricultural and Biological Engineers (ASABE) menetapkan standar baku pengukuran kinerja hidraulik sistem irigasi mikro melalui ANSI/ASAE S398.1 (*Procedure for Sprinkler Testing and Performance Reporting*) dan ASAE EP405.1 (*Design and Installation of Microirrigation Systems*). Untuk budidaya tanaman hortikultura bernilai tinggi, standar menetapkan bahwa Koefisien Keseragaman Christiansen (CU) minimum adalah $\ge 80\%$, dengan target rancangan rekayasa ideal mencapai $CU \ge 85\%$. Nilai keseragaman ini menjamin distribusi kelembapan tanah yang homogen di seluruh blok lahan tanpa disparitas hidraulik antara titik terdekat dan terjauh dari sumber suplai [2], [3], [23].

2. **Regulasi Pemerintah tentang Pengelolaan Air Irigasi (PP No. 20 Tahun 2006 & Permentan No. 49/2014)**  
   Peraturan Pemerintah Republik Indonesia Nomor 20 Tahun 2006 tentang Irigasi juncto Peraturan Menteri Pertanian No. 49/Permentan/OT.140/4/2014 menegaskan amanat konservasi sumber daya air pertanian: pengelolaan air di tingkat usaha tani wajib mengutamakan efisiensi pemanfaatan air secara tertib dan berkesinambungan (target efisiensi aplikasi air $\eta_a \ge 75\text{--}80\%$), mencegah pemborosan air akibat perkolasi dalam dan kebocoran saluran tanah bebas, serta mendorong penerapan teknologi irigasi hemat air berdaya guna tinggi [6], [7].

3. **Standar Komponen dan Emiter Irigasi Mikro (ISO 9261:2004)**  
   Standar internasional ISO 9261:2004 (*Agricultural irrigation equipment — Emitters and emitting pipe — Specification and test methods*) mengatur toleransi mekanis, ketahanan hidraulis terhadap tekanan kerja, serta batas variasi laju alir (*coefficient of manufacturing variation*, $C_v \le 0{,}05$). Standar ini menjadi acuan mutlak agar emiter tetes, lubang mikro, atau nozzle tidak mengalami deformasi fisik dan lonjakan debit saat dioperasikan di bawah tekanan fluida pertanian [8].

4. **Standar Proteksi Selungkup Lingkungan Luar Ruangan (IEC 60529 / SNI IEC 60529:2014)**  
   Peralatan instrumentasi, kontroler elektronika mikrokontroler, akuisisi data, dan sistem konversi daya yang diletakkan di tapak kebun terbuka tanpa naungan permanen wajib memenuhi derajat perlindungan selungkup minimal IP65 berdasarkan standar IEC 60529 dan adopsi identik SNI IEC 60529:2014. Rating ini memastikan selungkup kedap partikel debu tanah secara total serta tahan terhadap semprotan air bertekanan rendah dari berbagai sudut tanpa kebocoran ke papan sirkuit cetak (PCB) [4], [5].

5. **Standar Keselamatan Kelistrikan Area Pertanian Basah (IEC 60364-4-41 & IEEE 1451)**  
   Lingkungan pertanian terbuka dengan saluran air parit basah memiliki konduktivitas tinggi yang meningkatkan risiko bahaya sengatan listrik. Standar IEC 60364-4-41 klausul 414 menetapkan batas tegangan ekstra rendah aman (*Safety Extra-Low Voltage* / SELV) maksimal 48 V DC untuk seluruh aktuator, pompa elektrik mikro, dan instrumentasi lapangan. Sementara itu, standar IEEE Std 1451.4-2004 digunakan sebagai acuan arsitektur instrumentasi sensor terkalibrasi berdaya rendah [10], [11].

6. **Standar Pembangkit Listrik Surya Fotovoltaik Mandiri (IEC 62124 & FAO Guidelines)**  
   Standar *Photovoltaic Stand-Alone Systems: Design Verification* (IEC 62124:2004) dan panduan teknis FAO mengenai *Solar-Powered Irrigation Systems* (Hartung & Pluschke, 2018) mensyaratkan bahwa sistem PLTS off-grid pertanian wajib memperhitungkan faktor cadangan energi mandiri minimal 1,5 hingga 2 hari operasi kontinu tanpa sinar matahari langsung guna mengantisipasi cuaca mendung atau anomali musim hujan di wilayah tropis [9], [26], [27].

### 1.1.3 Karakteristik Fisiologi Tanaman Jeruk Limau dan Literatur Agronomi

Karakteristik biologis tanaman jeruk limau (*Citrus amblycarpa Hassk. Ochse*) menjadi fondasi penentuan dosis volume, frekuensi, dan zona pembasahan:

1. **Morfologi Perakaran Dangkal Jeruk Limau**  
   Berdasarkan kajian morfologi dan metabolomik jeruk limau oleh Budiarto dkk. (2017) serta pedoman nutrisi pohon jeruk University of Florida IFAS Extension (Obreza dkk., 2020), sistem perakaran tanaman jeruk didominasi oleh akar serabut aktif yang terkonsentrasi pada lapisan tanah dangkal dengan kedalaman efektif 20–40 cm dan radius sebaran horizontal 0,5–0,8 m di bawah proyeksi kanopi tajuk pohon. Pemberian air di luar radius proyeksi tajuk tidak dapat diserap optimal oleh akar dan hanya memicu pertumbuhan gulma liar yang menyerap unsur hara tanah [20], [24].

2. **Pemodelan Neraca Air Evapotranspirasi FAO-56 Penman-Monteith**  
   Estimasi kebutuhan air tanaman jeruk limau dihitung mengacu pada metodologi standar FAO Irrigation and Drainage Paper 56 (Allen dkk., 1998), panduan irigasi jeruk Florida (Kadyampakeni dkk., 2023), serta korelasi sistem penjadwalan irigasi Pereira (1996). Kebutuhan evapotranspirasi aktual tanaman dihitung melalui **Persamaan 1**:

$$ET_c = K_c \times ET_0 \quad \text{(Persamaan 1)}$$

Di mana:
- $ET_c$: laju evapotranspirasi aktual tanaman (mm/hari).
- $K_c$: koefisien tanaman jeruk kanopi sedang pada fase pertumbuhan aktif ($K_c = 0{,}70\text{--}0{,}80$).
- $ET_0$: laju evapotranspirasi acuan lingkungan Subang pada musim kemarau ($ET_0 = 4{,}5\text{--}5{,}0\text{ mm/hari}$).

Selanjutnya, volume air per pohon dalam satu siklus penyiraman dihitung melalui persamaan neraca air (**Persamaan 2**):

$$V_{pohon} = ET_c \times A_{tajuk} \times I_{siram} \quad \text{(Persamaan 2)}$$

Di mana:
- $V_{pohon}$: volume air per pohon (Liter/pohon/siklus).
- $A_{tajuk}$: luas proyeksi kanopi tajuk basah perakaran ($\sim 1{,}0\text{ m}^2$ untuk pohon setinggi $\sim 1\text{ m}$).
- $I_{siram}$: interval frekuensi penyiraman ($2\text{--}3\text{ hari per siklus}$).

Substitusi nilai parameter lapangan menghasilkan kebutuhan air teoritis berkisar 9,8 hingga 15,2 Liter per pohon per siklus penyiraman. Perhitungan ilmiah ini secara eksak memvalidasi batas empiris petani mitra di kebun Ciberes (10–15 Liter per pohon) [1], [19], [21].

3. **Pencegahan Risiko Pembusukan Akar (*Phytophthora nicotianae*)**  
   Literatur patologi tanaman oleh Graham & Timmer (2020) dan pedoman keseragaman Smajstrla dkk. (1997) mengingatkan bahwa kejenuhan air tanah yang berkepanjangan (*waterlogging* > 24–48 jam) akibat penggenangan parit tanah galian merupakan pemicu utama serangan jamur tanah *Phytophthora nicotianae* dan *Phytophthora palmivora* yang mengakibatkan pembusukan akar serabut serta penyakit blendok atau kanker pangkal batang. Oleh karena itu, spesifikasi pemberian air harus menjamin aerasi tanah tetap terjaga dan tidak menimbulkan genangan air terpusat lebih dari 30 menit pasca-siram [22], [23].

### 1.1.4 Karakteristik Tapak Lahan Eksisting dan Keterbatasan Sumber Daya

Spesifikasi sistem rekayasa diselaraskan secara ketat dengan kendala fisik tapak kebun di Ciberes:

1. **Ketiadaan Akses Jaringan Listrik PLN**  
   Kebun jeruk limau mitra terletak di bentang hamparan lahan persawahan pedesaan yang belum terjangkau tiang jaringan tegangan rendah PLN. Segala bentuk rancangan solusi rekayasa wajib bersifat mandiri energi (*off-grid*), mengandalkan pembangkit listrik tenaga surya (PLTS fotovoltaik) yang dipadukan dengan baterai penyimpan daya berdensitas tinggi atau penggerak mekanis hemat energi [9], [26], [28].

2. **Kekeruhan Air Sungai dan Sedimentasi Partikulat**  
   Sumber air diambil dari aliran sungai/saluran irigasi primer berjarak 20,54 meter dari batas kebun. Air permukaan alami membawa beban padatan tersuspensi tinggi berupa pasir halus, lumpur liat sedimen, dan serpihan ganggang organik, terutama saat debit sungai menurun di musim kemarau. Mengacu pada studi kualitas air FAO-29 (Ayers & Westcot, 1985), pedoman penyaringan Virginia Tech (Shortridge & Benham, 2023), serta penelitian penyumbatan emiter oleh Bounoua dkk. (2016), Shen dkk. (2022), dan Lavanholi dkk. (2018), sistem wajib dilengkapi penyaring fisik berkerapatan minimal 120 mesh (mampu menahan partikel $\ge 130\ \mu\text{m}$) guna menjamin lubang emiter atau pipa penyalur tidak mengalami penyumbatan fisik emiter [13], [14], [15], [16], [17].

3. **Geometri Jaringan Parit dan Inefisiensi Saluran Tanah Konvensional**  
   Kebun memiliki 3 lajur parit tanah longitudinal memanjang $\sim 100\text{ meter}$ dengan parit melintang penghubung pada bentang lahan selebar 25–30 meter. Analisis irigasi permukaan Walker (1989) menunjukkan bahwa saluran tanah terbuka mengalami kehilangan air hingga 40–50% akibat rembesan lateral dan evaporasi bebas. Parit galian yang semula dibuat untuk memudahkan penimbaan air kini terbukti tidak efisien. Di sisi lain, riset terkini mengenai robotika dan otomasi penyiraman hortikultura (Elkaoud dkk., 2025; Li dkk., 2012) membuktikan bahwa lintasan kebun memanjang sangat berpotensi dilayani oleh jaringan perpipaan mikro maupun wahana penyiram bergerak otonom [18], [25], [28].

---

## 1.2 Batasan dan Spesifikasi Solusi

Berdasarkan sintesis seluruh dasar pertimbangan multi-pilar di atas, bagian ini menetapkan batasan rekayasa dan matriks spesifikasi kuantitatif yang memandu perancangan sistem irigasi kebun jeruk limau.

### 1.2.1 Batasan Rekayasa Solusi

Batasan rekayasa merupakan kondisi batas mutlak yang tidak dapat dilanggar oleh arsitektur solusi mana pun yang akan dirancang:

- **C-01. Kemandirian Pasokan Energi**: Sistem harus beroperasi 100% mandiri tanpa ketergantungan pada jaringan jala-jala listrik PLN (*off-grid*), memanfaatkan pasokan energi terbarukan lokal (seperti fotovoltaik surya) yang terintegrasi dengan modul penyimpan daya baterai.
- **C-02. Kompatibilitas Sumber Air Permukaan Berpartikulat**: Sistem harus mampu menyedot dan memproses air baku dari sungai/saluran irigasi terbuka berkekeruhan alami tanpa mengalami kegagalan pompa dan penyumbatan mekanis pada komponen distribusi fluida.
- **C-03. Kompatibilitas Geometri, Batasan Skala Purwarupa, dan Skalabilitas Sistem**: Sistem purwarupa fungsional Capstone diwajibkan beroperasi dan membuktikan kinerja penyiraman secara empiris pada petak uji representatif (*pilot testbed*) kebun jeruk limau mitra di Ciberes, yaitu sekurang-kurangnya 1 lajur barisan pohon percontohan (15–20 pohon pada bentang operasional $\ge 25\text{ meter}$) dengan kontur tanah parit pertanian terbuka. Di samping itu, rancang bangun arsitektur mekanikal, elektrikal, dan perpipaan/aktuator purwarupa wajib bersifat modular sehingga terbukti secara teknis dapat diskalakan (*scalable*) untuk mencakup populasi penuh 500–600 pohon pada lahan memanjang 100–117,52 meter seluas ~3.000 m² tanpa merusak batang tanaman, tajuk buah, maupun zona perakaran dangkal.
- **C-04. Keselamatan Kelistrikan Area Terbuka Basah**: Seluruh perangkat elektrikal, instrumentasi sensor, pengontrol, dan kabel transmisi yang dipasang di lingkungan kebun terbuka wajib beroperasi pada batas tegangan ekstra rendah aman (*Safety Extra-Low Voltage* / SELV $\le 48\text{ V DC}$) sesuai standar IEC 60364-4-41.
- **C-05. Netralitas Solusi Rekayasa**: Perumusan batasan dan spesifikasi dirancang secara fungsional tanpa mengunci rancangan pada satu opsi arsitektur atau merek komponen tertentu (*solution-agnostic*), memberikan fleksibilitas penuh untuk mengevaluasi alternatif jaringan perpipaan mikro, wahana bergerak mandiri, maupun sistem modular pada tahap CD-3.

### 1.2.2 Spesifikasi Kuantitatif Solusi

Spesifikasi kuantitatif dirumuskan ke dalam empat kategori aspek menyeluruh: teknis, ekonomi, lingkungan, dan operasional/kemitraan. Matriks lengkap spesifikasi kuantitatif disajikan pada Tabel 3:

#### Tabel 3. Matriks Batasan dan Spesifikasi Kuantitatif Solusi

| ID | Parameter Spesifikasi | Nilai Target & Toleransi | Satuan | Kategori Aspek | Rujukan Penentuan |
|---|---|---|---|---|---|
| **S-01** | Akurasi Dosis Volume Air per Pohon | 10 – 15 $\pm$ 5% | Liter/pohon | Aspek Teknis | Wawancara Mitra [31], FAO-56 [1], Florida [21], Pereira [19] |
| **S-02** | Koefisien Keseragaman Distribusi (CU) | $\ge 85$ | % | Aspek Teknis | Standar ANSI/ASAE S398.1, EP405.1 [2], [3], Smajstrla [23] |
| **S-03** | Durasi Total Siklus Penyiraman Kebun | $\le 4{,}0$ (Skala penuh) | Jam/siklus | Aspek Teknis | Batas Waktu Operasi Harian Mitra, Elkaoud [25] |
| **S-04** | Radius dan Kedalaman Pembasahan | $r = 0{,}5\text{--}0{,}8$; $d = 20\text{--}40$ | cm | Aspek Teknis | Morfologi Perakaran Jeruk Limau Budiarto [20], Obreza [24] |
| **S-05** | Derajat Filtrasi Fisik Partikulat | $\ge 120$ (saring $\le 130$) | mesh ($\mu\text{m}$) | Aspek Teknis | Kualitas Air FAO-29 [13], Shortridge [14], Bounoua [15], Lavanholi [17] |
| **S-06** | Ketahanan Cadangan Energi Mandiri | $\ge 8{,}0$ (min. 2 siklus penuh) | Jam operasi | Aspek Teknis | Standar IEC 62124 [9], Hartung & Pluschke [27], Nurwidiana [26] |
| **S-07** | Ketahanan Lingkungan Selungkup | IP65 (Suhu: 20 – 55) | Rating ($^\circ\text{C}$) | Aspek Teknis | Standar IEC 60529 / SNI IEC 60529 [4], [5] |
| **S-08** | Plafon Biaya Modal Purwarupa & Skala Penuh | Purwarupa $\le 5.000.000$; Penuh $\le 18.000.000$ | Rupiah (Rp) | Aspek Ekonomi | Pagu Anggaran Riset Mahasiswa & Analisis Modal Tani [30] |
| **S-09** | Biaya Operasional Siklus (OPEX) | $\le 50.000$ (Hemat $\ge 87{,}5\%$) | Rupiah (Rp) | Aspek Ekonomi | Biaya Upah Manual Eksisting (Rp400.000/siklus), Mitra [31] |
| **S-10** | Periode Pengembalian Modal | $\le 12\text{--}18$ | Bulan | Aspek Ekonomi | Skenario Penghematan Rp48,7 Juta/Tahun, Durga [30] |
| **S-11** | Efisiensi Aplikasi Air Irigasi | $\ge 80$ | % | Aspek Lingkungan | PP No. 20/2006 [6], Permentan 49/2014 [7], ISO 9261 [8], Walker [18] |
| **S-12** | Emisi Gas Buang di Zona Tajuk | 0 (Bebas emisi hidrokarbon) | g/kWh | Aspek Lingkungan | Proteksi Tanah Perakaran dari Residu Pertalite & Overheat Pompa |
| **S-13** | Kemudahan Pengoperasian Mitra | Tombol Tunggal (Ajar $\le 30$) | Menit | Aspek Operasional | Profil Tenaga Kerja Lokal Kebun Ciberes, Usability Testing |
| **S-14** | Durasi Pemeliharaan Rutin Saringan | $\le 20$ (Perkakas lokal) | Menit/bulan | Aspek Operasional | Keterbatasan Bengkel Khusus Pedesaan, Prosedur Shortridge [14] |

#### Penjelasan Rinci Parameter Spesifikasi S-01 sampai S-14:

- **S-01. Akurasi Dosis Volume Air per Pohon**: Sistem harus mampu menyalurkan volume air terukur antara 10 hingga 15 Liter untuk tiap tanaman jeruk limau dengan batas simpangan toleransi kesalahan tidak lebih dari $\pm 5\%$. Nilai kuantitatif ini menjamin tanaman terhidrasi sesuai laju evapotranspirasi lingkungan tanpa risiko pemberian air berlebih yang memboroskan sumber daya air.
- **S-02. Koefisien Keseragaman Distribusi Air (CU)**: Mengacu pada standar ANSI/ASAE S398.1 dan ASAE EP405.1, keseragaman volume air yang diterima oleh pohon di awal, tengah, dan ujung barisan parit harus mencapai minimal 85%. Evaluasi keseragaman distribusi air dihitung menggunakan formula Koefisien Keseragaman Christiansen (CU) (**Persamaan 3**) [2], [3]:

$$CU = 100\% \times \left[ 1 - \frac{\sum_{i=1}^{n} |X_i - \bar{X}|}{n \times \bar{X}} \right] \quad \text{(Persamaan 3)}$$

Di mana:
  - $CU$: Christiansen's Uniformity Coefficient (%).
  - $n$: jumlah pohon sampel uji ($n = 15\text{ bejana}$).
  - $X_i$: volume air tertampung pada bejana sampel ke-$i$ (Liter).
  - $\bar{X}$: rata-rata volume air dari seluruh bejana sampel.
  Nilai keseragaman $CU \ge 85\%$ menjamin pertumbuhan seluruh pohon jeruk limau tetap homogen tanpa adanya pohon yang mengalami kekeringan ekstrem atau pembusukan akar.
- **S-03. Durasi Total Siklus Penyiraman Kebun**: Seluruh proses penyiraman untuk 500–600 pohon pada skala penuh harus dapat dituntaskan dalam waktu kurang dari atau sama dengan 4 jam per siklus kegiatan (ekuivalen laju siram rata-rata $\le 24\text{--}28\text{ detik per pohon}$, atau durasi $\le 8\text{--}10\text{ menit}$ untuk 15–20 pohon percontohan pada purwarupa uji). Hal ini memberikan efisiensi waktu yang masif dibandingkan metode manual 4 orang buruh yang menyita waktu seharian penuh, serta memanfaatkan waktu siram ideal (pagi hari sebelum pukul 10.00 WIB atau sore hari setelah pukul 15.00 WIB) guna meminimalkan kehilangan air akibat evaporasi radiasi matahari langsung [25].
- **S-04. Radius dan Kedalaman Pembasahan Efektif**: Air irigasi diarahkan meresap pada area proyeksi kanopi tanaman dengan radius 0,5–0,8 m dari pangkal batang hingga mencapai kedalaman profil tanah 20–40 cm. Distribusi air yang terkonsentrasi pada zona perakaran aktif serabut menghindarkan pembasahan batang utama yang rentan jamur batang serta tidak membasahi area jalan antar-baris secara sia-sia [20], [24].
- **S-05. Derajat Filtrasi Fisik Partikulat**: Untuk mengatasi kekeruhan air sungai Ciberes, sistem wajib dilengkapi dengan saringan partikulat dengan kerapatan minimal 120 mesh (mampu menyaring partikel berdiameter $\ge 130\ \mu\text{m}$). Hal ini merupakan syarat wajib untuk mencegah terjadinya penyumbatan mekanis pada emiter, lubang nozzle, katup pengontrol, dan impeller pompa air mikro [13], [14], [15], [17].
- **S-06. Ketahanan Cadangan Energi Mandiri**: Subsistem daya mandiri (*off-grid*) harus mampu menyuplai kebutuhan daya operasional beban penuh selama minimal 8 jam kerja kontinu tanpa kehadiran cahaya matahari langsung (setara dengan cadangan daya untuk minimal 2 siklus penyiraman lengkap). Mengacu pada standar IEC 62124 (*Photovoltaic stand-alone systems*) dan pedoman PLTS FAO (Hartung & Pluschke, 2018), konsumsi energi operasional per siklus penyiraman ($E_{siklus}$) dan kapasitas minimum modul penyimpan daya ($C_{baterai}$) dihitung melalui **Persamaan 4** dan **Persamaan 5** [9], [27]:

$$E_{siklus} = P_{beban} \times t_{operasi} \quad \text{(Persamaan 4)}$$

$$C_{baterai} = \frac{E_{siklus} \times N_{autonomy}}{V_{sistem} \times DoD} \quad \text{(Persamaan 5)}$$

Di mana:
  - $E_{siklus}$: energi operasional satu siklus (Wh).
  - $P_{beban}$: total daya pompa dan kontroler (Watt).
  - $t_{operasi}$: durasi kerja satu siklus ($\le 4\text{ jam}$).
  - $N_{autonomy}$: faktor otonomi cadangan ($\ge 2\text{ siklus} = 8\text{ jam}$).
  - $V_{sistem}$: tegangan kerja ekstra rendah aman (12 V DC atau 24 V DC).
  - $DoD$: *Depth of Discharge* aman baterai ($DoD = 80\%$ untuk LiFePO4).
- **S-07. Ketahanan Lingkungan Selungkup**: Seluruh kotak pelindung kontroler, konektor kelistrikan, papan modul sensor, dan unit catu daya wajib bersertifikasi minimal IP65 serta mampu bekerja normal pada rentang suhu ambien $20^\circ\text{C}$ hingga $55^\circ\text{C}$. Selungkup harus tahan terhadap terpaan panas matahari tropis Subang, percikan lumpur tanah, dan semprotan air saat pembersihan kebun [4], [5].
- **S-08. Plafon Biaya Investasi Awal Purwarupa dan Proyeksi Skala Penuh (CAPEX)**: Spesifikasi biaya investasi awal dibedakan secara tegas ke dalam dua tingkatan akuntabilitas rekayasa:
  - *(a) Plafon Biaya Modal Purwarupa Mahasiswa (Prototyping CAPEX)*: Realisasi pengadaan modul elektronika, pompa mikro, instrumentasi sensor, baterai, panel surya uji, dan fabrikasi struktural purwarupa fungsional untuk petak uji percontohan (15–20 pohon) dibatasi maksimal Rp5.000.000. Plafon ini sangat realistis dan terjangkau bagi pembiayaan mandiri maupun hibah tugas akhir mahasiswa tanpa mengurangi validitas pengujian fungsional di lapangan.
  - *(b) Proyeksi Biaya Implementasi Skala Penuh Kebun (Full-Scale Commercial CAPEX)*: Berdasarkan estimasi perbanyakan modular untuk melayani seluruh 500–600 pohon di lahan ~3.000 m², batas atas biaya pengadaan perangkat dan instalasi komersial ditetapkan maksimal Rp18.000.000. Angka batas atas komersial ini dihitung berdasarkan alokasi modal usaha tani kebun mitra agar memenuhi kriteria pengembalian modal investasi yang rasional (S-10) [30], [31].
- **S-09. Biaya Operasional per Siklus Penyiraman (OPEX)**: Biaya operasional yang mencakup konsumsi energi (pengisian daya/bahan bakar cadangan) dan alokasi jasa pemantauan operator ditekan hingga maksimal Rp50.000 per siklus penyiraman. Hal ini menghasilkan penghematan biaya langsung sebesar 87,5% per kegiatan dibandingkan pengeluaran rutin upah guyur manual eksisting (Rp400.000 per kegiatan) [31].
- **S-10. Periode Pengembalian Modal**: Kelayakan ekonomi sistem dinilai berdasarkan kecepatan pengembalian modal investasi awal (*payback period* / PP). Periode pengembalian modal dihitung dengan formula rasio investasi awal (CAPEX) terhadap selisih penghematan biaya operasional tahunan (**Persamaan 6**):

$$PP = \frac{CAPEX}{\Delta OPEX_{tahunan}} \quad \text{(Persamaan 6)}$$

Di mana:
  - $PP$: Payback Period (dalam tahun atau bulan).
  - $CAPEX$: modal investasi implementasi skala penuh sistem rekayasa ($\le \text{Rp18.000.000}$).
  - $\Delta OPEX_{tahunan}$: selisih penghematan biaya operasional tahunan antara metode manual eksisting ($\text{Rp400.000/kegiatan} \times \sim 120\text{ siklus/tahun} = \sim \text{Rp48.000.000/tahun}$) dengan biaya operasional sistem baru ($\le \text{Rp50.000/siklus} \times \sim 120\text{ siklus/tahun} = \le \text{Rp6.000.000/tahun}$). Dengan selisih penghematan bersih mencapai lebih dari Rp42.000.000 per tahun, target titik impas modal investasi penuh dipastikan tercapai dalam kurun waktu 12 hingga 18 bulan operasi [30]. Sementara itu, untuk purwarupa fungsional Capstone mahasiswa dengan pagu belanja $\le \text{Rp5.000.000}$, kelayakan biaya terbukti sangat efisien sebagai prototipe pembuktian konsep sebelum investasi penuh digelontorkan oleh mitra.
- **S-11. Efisiensi Aplikasi Air Irigasi**: Mengacu pada prinsip konservasi air PP No. 20 Tahun 2006, Permentan No. 49/2014, dan panduan FAO, efisiensi aplikasi air ($\eta_a$) dihitung dari rasio volume air yang tersimpan di zona perakaran aktif serabut terhadap volume total air yang dialirkan dari sumber melalui **Persamaan 7** [1], [6], [7], [18]:

$$\eta_a = \left( \frac{V_{akar}}{V_{sumber}} \right) \times 100\% \quad \text{(Persamaan 7)}$$

Di mana:
  - $\eta_a$: efisiensi aplikasi air irigasi (%).
  - $V_{akar}$: volume air yang meresap dan tertahan pada zona perakaran aktif pohon jeruk (kedalaman 20–40 cm dan radius 0,5–0,8 m).
  - $V_{sumber}$: volume total air yang disedot dari sungai melalui pipa masukan utama. Sistem baru ditargetkan mencapai $\eta_a \ge 80\%$, melompat jauh melampaui efisiensi penyiraman parit tanah konvensional eksisting yang kerap di bawah 40–50% akibat rembesan horizontal tanah galian dan evaporasi terbuka di sepanjang parit 100 meter.
- **S-12. Emisi Gas Buang di Zona Tajuk Perakaran**: Sistem operasi penyiraman di sekitar barisan tanaman tidak menghasilkan emisi gas buang jelaga karbon monoksida maupun tetesan residu pelumas oli di atas tanah perakaran. Hal ini memperbaiki kelemahan pompa pembakaran internal berbahan bakar bensin/Pertalite eksisting yang mencemari lingkungan perakaran dan berisiko meracuni mikroorganisme tanah penyubur jeruk.
- **S-13. Kemudahan Pengoperasian oleh Operator Mitra**: Antarmuka pengguna dirancang dengan logika operasional tombol tunggal (*single-touch start*). Pekerja kebun lokal dengan latar belakang pendidikan dasar dapat mengoperasikan dan memantau status penyiraman dengan waktu pelatihan singkat tidak lebih dari 30 menit.
- **S-14. Durasi Pemeliharaan Rutin Saringan dan Mekanik**: Desain mekanis sistem dirancang modular sehingga proses pembongkaran, pembersihan saringan kotoran, dan perakitan kembali dapat dituntaskan oleh satu orang pekerja dalam waktu kurang dari 20 menit per bulan menggunakan perkakas bengkel pertanian umum (seperti obeng dan kunci pas standar tanpa memerlukan alat kalibrasi khusus) [14].

---

## 1.3 Pengukuran dan Verifikasi Spesifikasi

Untuk membuktikan secara ilmiah dan kuantitatif bahwa solusi rekayasa yang dikembangkan pada tahap selanjutnya benar-benar memenuhi spesifikasi yang dijanjikan, bagian ini menyusun rencana pengukuran dan prosedur verifikasi pengujian. Setiap spesifikasi dilengkapi dengan metode standar pengujian, peralatan ukur terkalibrasi, mekanisme langkah pengujian, serta kriteria keberhasilan verifikasi yang disajikan pada Tabel 4.

#### Tabel 4. Matriks Rencana Pengukuran dan Verifikasi Spesifikasi

| ID | Parameter yang Diuji | Target Nilai | Metode / Standar Uji | Alat Ukur / Verifikasi | Kriteria Kelulusan |
|---|---|---|---|---|---|
| **S-01** | Volume Air per Pohon | 10 – 15 L $\pm$ 5% | Metode Volumetrik Langsung | Wadah tera, Gelas ukur 1.000 mL, Flow meter | Volume tertampung 9,5 – 15,75 L. |
| **S-02** | Keseragaman Distribusi | CU $\ge$ 85% | Standar ANSI/ASAE S398.1 | 15 unit bejana ukur, Silinder ukur | Perhitungan matematis CU $\ge$ 85,0%. |
| **S-03** | Durasi Siklus Total | $\le 4{,}0$ Jam (Skala penuh) | Pencatatan Waktu Siklus / Laju per Pohon | Stopwatch terkalibrasi, Data logger sistem | Laju siram $\le 28$ dtk/pohon; siram 1 lajur $\le 10$ mnt. |
| **S-04** | Radius & Kedalaman | $r \ge 0{,}5$ m; $d \ge 20$ cm | Pengukuran Penetrasi Tanah Basah | Meteran baja, Bor tanah mini, Sensor lengas | Profil basah $r \ge 50$ cm dan $d \ge 20$ cm. |
| **S-05** | Derajat Filtrasi Fisik | $\ge 120$ mesh | Uji Hambatan & Partikel Lolos | Saringan kawat 120 mesh, Manometer DP | Nol partikel $\ge 130\ \mu\text{m}$ lolos ke pipa. |
| **S-06** | Cadangan Daya Mandiri | $\ge 8{,}0$ Jam | Uji Beban Penuh Kontinu Off-Grid | DC Power Meter, Clamp meter, Data logger | Operasi beban penuh $\ge 8$ jam tanpa cutoff. |
| **S-07** | Ketahanan Selungkup | IP65 & 20 – 55 $^\circ$C | Metode Uji Standar IEC 60529 | Nozzle 6,3 mm debit 12,5 L/m, Termometer IR | Nol rembesan air ke PCB; stabil 55 $^\circ$C. |
| **S-08** | Biaya Modal (CAPEX) | Purwarupa $\le$ Rp 5 Jt; Penuh $\le$ Rp 18 Jt | Audit Nota BOM Purwarupa & Analisis Finansial | Rekapitulasi nota belanja riil & simulasi biaya skala penuh | Belanja purwarupa $\le$ Rp 5.000.000; Proyeksi skala penuh $\le$ Rp 18.000.000. |
| **S-09** | Biaya Operasional (OPEX) | $\le$ Rp 50.000/siklus | Pencatatan Konsumsi Energi & Jasa | Log pengeluaran operasional per kegiatan | Biaya energi + jasa $\le$ Rp 50.000/siklus. |
| **S-10** | Periode Pengembalian Modal (PP) | $\le 12\text{--}18$ Bulan | Analisis Finansial Usaha Tani | Formula PP = CAPEX / $\Delta$OPEX Tahunan | Nilai PP terhitung $\le 1{,}5$ tahun. |
| **S-11** | Efisiensi Aplikasi Air | $\ge 80\%$ | Neraca Air Masuk vs Terserap Akar | Flow meter pipa utama, Volumetrik perakaran | Rasio volume air terserap $\ge 0{,}80$. |
| **S-12** | Emisi Gas di Kebun | 0 g/kWh Emisi Lokal | Inspeksi Penggerak & Deteksi Gas | Gas detector portabel (CO, HC), Visual pelumas | Nol emisi gas racun & nol ceceran oli. |
| **S-13** | Kemudahan Operasi | Waktu ajar $\le 30$ Menit | Uji Keterpakaian Lapangan | Lembar tugas operator mitra, Stopwatch tugas | Operator mandiri operasikan dalam $\le 30$ mnt. |
| **S-14** | Waktu Pemeliharaan | $\le 20$ Menit/bulan | Uji Waktu Bongkar-Pasang Saringan | Stopwatch, Perkakas kunci pas & obeng umum | Flushing & bersih saringan $\le 20$ menit. |

### Prosedur Verifikasi Terinci

#### 1.3.1 Prosedur Verifikasi Dosis dan Keseragaman Distribusi Air (S-01, S-02, S-04)
1. **Protokol Uji Keseragaman Christiansen (ANSI/ASAE S398.1)**: Sebanyak 15 titik pohon sampel ditetapkan pada lajur petak uji percontohan (*pilot testbed*) mewakili tiga zona hidrolik: 5 pohon di zona pangkal (dekat titik suplai air), 5 pohon di zona tengah (bentang ~12–15 m), dan 5 pohon di zona ujung lajur uji (bentang ~25 m). Pada setiap pohon sampel diletakkan bejana penampung ukur (*catch cans*) yang mengelilingi radius perakaran tanaman.
2. **Pengukuran Volumetrik dan Analisis Matematis CU**: Setelah satu siklus penyiraman selesai dijalankan, volume air tertampung pada masing-masing bejana ($X_i$) diukur menggunakan silinder ukur bertingkat presisi $\pm 5\text{ mL}$. Koefisien Keseragaman Christiansen (CU) dihitung menggunakan rumus matematis Persamaan 3 dengan $n = 15$. Spesifikasi dinyatakan lulus jika $CU \ge 85\%$ dan deviasi volume tiap titik terhadap target 10–15 L tidak melampaui $\pm 5\%$.
3. **Verifikasi Penetrasi dan Infiltrasi Tanah**: Tiga puluh menit pasca-siram, profil kedalaman pembasahan tanah diuji menggunakan bor tanah mini sedalam 40 cm pada radius 60 cm dari batang untuk memastikan air terinfiltrasi pada zona perakaran aktif tanpa menimbulkan genangan permukaan > 30 menit.

#### 1.3.2 Prosedur Verifikasi Durasi Siklus dan Filtrasi Fisik (S-03, S-05)
1. **Pengukuran Durasi Operasi Kebun**: Durasi siklus penyiraman diukur menggunakan stopwatch digital terkalibrasi yang diaktifkan tepat saat pompa/sistem utama mulai beroperasi dari titik awal kebun dan dihentikan saat pohon terakhir selesai terairi. Data waktu diverifikasi melalui pencatatan timestamp pada sistem mikrokontroler. Kriteria kelulusan terpenuhi jika durasi total $\le 240\text{ menit}$ (4 jam).
2. **Pengujian Kinerja Filtrasi Sedimen**: Verifikasi kemampuan saringan dilakukan dengan memasang manometer diferensial pada sisi masuk dan keluar tabung saringan 120 mesh. Air sampel sungai Ciberes dialirkan pada debit kerja nominal selama 2 jam kontinu. Sampel air keluaran ditampung dan diuji menggunakan membran kertas saring laboratorium untuk memverifikasi bahwa tidak ada partikel sedimen berukuran $\ge 130\ \mu\text{m}$ yang lolos menuju subsistem distribusi.

#### 1.3.3 Prosedur Verifikasi Kemandirian Daya dan Proteksi Lingkungan (S-06, S-07)
1. **Uji Ketahanan Pasokan Daya Mandiri**: Uji ketahanan daya mandiri dilakukan dengan kondisi modul baterai terisi penuh (100% SoC) tanpa sambungan pengisian panel surya untuk mensimulasikan kondisi cuaca mendung ekstrem. Seluruh beban operasional diaktifkan pada siklus kerja penuh. Digital clamp meter DC dan alat perekam data (*data logger*) digunakan untuk merekam kurva penurunan tegangan baterai (V), arus beban (I), dan konsumsi daya total (P) setiap 10 menit. Sistem dinyatakan lulus apabila mampu beroperasi stabil selama minimal 8 jam kontinu tanpa menyentuh batas cut-off tegangan rendah.
2. **Uji Proteksi Selungkup Terhadap Debu dan Air (IP65)**: Uji ketahanan lingkungan selungkup mengacu pada klausul standar IEC 60529 untuk proteksi IP65. Selungkup kontroler disemprot menggunakan nozzle berdiameter 6,3 mm dengan debit air 12,5 L/menit dari jarak 2,5–3 meter ke seluruh sambungan dan engsel selama 3 menit. Setelah pengujian semprot, bagian luar dikeringkan dan isi selungkup diperiksa secara visual untuk memastikan tidak ada setetes pun air yang merembes ke papan rangkaian elektronik.

#### 1.3.4 Prosedur Verifikasi Finansial, Efisiensi Biaya, dan Efisiensi Air (S-08, S-09, S-10, S-11)
1. **Audit Biaya Modal Purwarupa dan Simulasi Finansial (CAPEX)**: Biaya investasi awal diverifikasi melalui dua tahapan: (a) audit dokumen rincian anggaran komponen riil (*bill of materials* / BOM) purwarupa fungsional mahasiswa berdasarkan total rekapitulasi nota belanja komponen dan ongkos perakitan mekanis yang wajib terbukti $\le \text{Rp5.000.000}$, serta (b) validasi matematis pemodelan biaya ekspansi skala penuh kebun ($\le \text{Rp18.000.000}$) menggunakan data harga satuan komponen percontohan.
2. **Pengujian Biaya Operasional per Siklus (OPEX)**: Biaya operasional per siklus (OPEX) dihitung dari konsumsi energi habis pakai ditambah alokasi jasa pemantauan operator, dengan batas kelulusan $\le \text{Rp50.000}$ per kegiatan.
3. **Perhitungan Periode Pengembalian Modal**: Periode pengembalian modal dihitung dengan formula $PP = \text{CAPEX riil} / \Delta OPEX_{\text{Tahunan}}$ terhadap biaya manual eksisting (Rp48,7 juta/tahun), dengan syarat $PP \le 1{,}5\text{ tahun}$ (18 bulan).
4. **Pengukuran Efisiensi Aplikasi Air**: Efisiensi aplikasi air diuji dengan memasang alat ukur aliran (*flow meter*) pada pipa masukan utama untuk mengukur volume total air disedot ($V_{sumber}$) dan membandingkannya dengan volume air efektif yang tersimpan pada zona perakaran seluruh pohon ($V_{akar}$), dengan syarat $\eta_a = (V_{akar} / V_{sumber}) \times 100\% \ge 80\%$.

#### 1.3.5 Prosedur Verifikasi Keterpakaian dan Pemeliharaan (S-13, S-14)
1. **Uji Keterpakaian oleh Operator Mitra**: Uji keterpakaian dilakukan bersama pekerja kebun mitra Ciberes menggunakan lembar instruksi kerja standar satu halaman bergambar. Setelah sesi pengenalan selama maksimal 30 menit, pekerja diminta menjalankan sistem secara mandiri. Waktu keberhasilan dan kesalahan eksekusi dicatat, dengan syarat kelulusan pekerja mampu mengoperasikan sistem secara mandiri tanpa asistensi teknis.
2. **Uji Waktu Pemeliharaan Rutin Saringan**: Uji pemeliharaan dilakukan melalui simulasi pembongkaran, pembersihan elemen saringan 120 mesh dengan air mengalir, dan pemasangan kembali menggunakan perkakas standar pertanian (obeng dan kunci pas). Seluruh tahapan prosedur pemeliharaan dicatat menggunakan stopwatch dan dinyatakan lulus apabila tuntas dalam waktu $\le 20\text{ menit}$.

---

## 1.4 Kesimpulan

Dokumen CD-2 ini telah menetapkan kerangka batasan rekayasa dan spesifikasi kuantitatif yang terdefinisi secara presisi, terukur, dan memiliki pijakan ilmiah yang kokoh bagi perancangan sistem irigasi kebun jeruk limau mitra di Ciberes, Subang. Rangkuman poin penting dokumen CD-2 meliputi:

1. **Dasar Penentuan Spesifikasi Multi-Pilar**: Perumusan spesifikasi mengintegrasikan kebutuhan riil mitra kebun Ciberes (penurunan upah manual Rp400.000/kegiatan atau Rp48,7 juta/tahun, keandalan pompa, proteksi pemupukan NPK), regulasi pemerintah (PP No. 20 Tahun 2006 tentang Irigasi dan Permentan No. 49/2014), standar teknik industri konsensus internasional (keseragaman air ANSI/ASAE S398.1 $\ge 85\%$, ASAE EP405.1, ISO 9261:2004, proteksi lingkungan IEC 60529 IP65, keselamatan tegangan rendah SELV $\le 48\text{ V DC}$, otonomi surya IEC 62124), karakteristik agronomi fisiologi tanaman jeruk limau (evapotranspirasi 10–15 L/pohon, perakaran serabut aktif 20–40 cm, pencegahan busuk perakaran *Phytophthora*), serta mitigasi sedimen sungai Ciberes (filtrasi $\ge 120\text{ mesh}$).
2. **Perumusan Spesifikasi Kuantitatif Multi-Aspek**: Ditetapkan 5 batasan mutlak dan 14 butir spesifikasi kuantitatif komprehensif yang mencakup aspek teknis (akurasi dosis air 15 L $\pm$ 5%, keseragaman CU $\ge 85\%$, durasi siram $\le 4\text{ jam}$ skala penuh / laju $\le 28\text{ detik/pohon}$, filtrasi 120 mesh, otonomi energi $\ge 8\text{ jam}$, rating IP65), aspek ekonomi (plafon biaya belanja purwarupa mahasiswa $\le \text{Rp5.000.000}$, proyeksi implementasi skala penuh kebun $\le \text{Rp18.000.000}$, OPEX $\le \text{Rp50.000/siklus}$, payback period $\le 12\text{--}18\text{ bulan}$), aspek lingkungan (efisiensi aplikasi air $\ge 80\%$, bebas emisi lokal di area perakaran), serta aspek operasional mitra (waktu ajar operasi $\le 30\text{ menit}$, waktu perawatan $\le 20\text{ menit/bulan}$).
3. **Netralitas Solusi Rekayasa**: Spesifikasi dirumuskan secara fungsional tanpa bias atau penguncian dini pada satu opsi teknologi maupun merek komponen tertentu (*solution-agnostic*), membuka ruang terbuka bagi evaluasi perpipaan mikro, robotik bergerak berselang, maupun solusi hibrida.
4. **Kesiapan Protokol Pengujian Terukur**: Seluruh spesifikasi telah dipetakan ke dalam matriks rencana pengujian verifikasi yang memuat metode uji baku, instrumen alat ukur terkalibrasi, prosedur pengukuran langkah demi langkah, dan kriteria kelulusan numerik yang objektif.
5. **Transisi Menuju Tahap CD-3**: Batasan dan spesifikasi kuantitatif dalam dokumen CD-2 ini secara formal menjadi tolok ukur acuan evaluasi dan kriteria pembobotan keputusan dalam mengusulkan, menganalisis, dan memilih sekurang-kurangnya tiga alternatif konsep desain solusi pada dokumen rancangan solusi CD-3.

---

## Daftar Pustaka

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

[12] P. Panigrahi and A. K. Srivastava, “Water and nutrient management effects on water use and yield of drip irrigated citrus in vertisol under a sub-humid region,” *Journal of Integrative Agriculture*, vol. 16, no. 5, pp. 1184–1194, 2017, doi: 10.1016/S2095-3119(16)61500-9.

[13] R. S. Ayers and D. W. Westcot, *Water Quality for Agriculture*, FAO Irrigation and Drainage Paper 29 Rev. 1. Rome, Italy: Food and Agriculture Organization of the United Nations (FAO), 1985, ISBN: 92-5-102263-1. [Online]. Available: https://www.fao.org/4/t0234e/t0234e00.htm

[14] J. Shortridge and B. Benham, “Filtration, Treatment, and Maintenance Considerations for Micro-Irrigation Systems,” Virginia Cooperative Extension, Virginia Tech, Publication 442-757, 2023. [Online]. Available: https://www.pubs.ext.vt.edu/442/442-757/442-757.html

[15] S. Bounoua, S. Tomas, J. Labille, B. Molle, J. Granier, P. Haldenwang, and S. N. Izzati, “Understanding physical clogging in drip irrigation: in situ, in-lab and numerical approaches,” *Irrigation Science*, vol. 34, no. 4, pp. 327–342, 2016, doi: 10.1007/s00271-016-0506-8.

[16] Y. Shen, J. Puig-Bargués, M. Li, Y. Xiao, Q. Li, and Y. Li, “Physical, chemical and biological emitter clogging behaviors in drip irrigation systems using high-sediment loaded water,” *Agricultural Water Management*, vol. 270, art. 107738, 2022, doi: 10.1016/j.agwat.2022.107738.

[17] R. Lavanholi, B. Molle, R. J. R. Ramos, and A. P. Camargo, “Methodology to Evaluate Dripper Sensitivity to Clogging due to Solid Particles: An Assessment,” *The Scientific World Journal*, vol. 2018, art. 7697458, pp. 1–9, 2018, doi: 10.1155/2018/7697458.

[18] W. R. Walker, *Guidelines for Designing and Evaluating Surface Irrigation Systems*, FAO Irrigation and Drainage Paper 45. Rome, Italy: Food and Agriculture Organization of the United Nations (FAO), 1989, ISBN: 92-5-102879-6. [Online]. Available: https://www.fao.org/4/t0231e/t0231e00.htm

[19] L. S. Pereira, “Inter-relationships between irrigation scheduling methods and on-farm irrigation systems,” in *Irrigation Scheduling: From Theory to Practice*, FAO Water Reports 8. Rome, Italy: FAO, 1996, pp. 91–104. [Online]. Available: https://www.fao.org/4/w4367e/w4367e0c.htm

[20] R. Budiarto, R. Poerwanto, E. Santosa, and D. Efendi, “The Potentials of Limau (Citrus amblycarpa Hassk. Ochse) as A Functional Food and Ornamental Mini Tree Based on Metabolomic and Morphological Approaches,” *Journal of Tropical Crop Science*, vol. 4, no. 2, pp. 49–57, 2017, doi: 10.29244/jtcs.4.2.49-57.

[21] D. M. Kadyampakeni, K. T. Morgan, M. Zekri, A. W. Schumann, S. Guzmán, F. Alferez, M. A. Shahid, and T. A. Obreza, “2023–2024 Florida Citrus Production Guide: Irrigation Management of Citrus Trees,” University of Florida IFAS Extension, EDIS Publication CG093/CPG12, 2023, doi: 10.32473/edis-cg093-2023.

[22] J. H. Graham and L. W. Timmer, “Phytophthora Diseases of Citrus,” University of Florida IFAS Extension, EDIS Publication SL127/CH087, 2020. [Online]. Available: https://edis.ifas.ufl.edu/publication/CH087

[23] A. G. Smajstrla, B. J. Boman, D. Z. Haman, D. J. Pitts, and F. S. Zazueta, “Field Evaluation of Microirrigation Water Application Uniformity,” University of Florida IFAS Extension, Publication BUL265/AE094, 1997, doi: 10.32473/edis-ae094-1997.

[24] T. A. Obreza, M. Zekri, and S. H. Futch, “Nutrition of Florida Citrus Trees, 3rd Edition: Chapter 3. General Soil Fertility and Citrus Tree Nutrition,” University of Florida IFAS Extension, Publication SL457/SS670, 2020, doi: 10.32473/edis-ss670-2020.

[25] N. Elkaoud, S. Ismail, R. Mahmoud, H. Taraby, S. Shang, D. Wang, and M. Rayan, “Efficient and Effective Irrigation Water Management Using Sprinkler Robot,” *Eng*, vol. 6, no. 7, art. 138, pp. 1–18, Jun. 2025, doi: 10.3390/eng6070138.

[26] Nurwidiana, W. Fatmawati, dan A. Rifa'i, “Perancangan Alat Penyiram Lahan Bawang Merah Berbasis Teknologi Solar Fotovoltaik,” *Jurnal PASTI (Penelitian dan Aplikasi Sistem dan Teknik Industri)*, vol. 15, no. 1, hlm. 61–70, 2021.

[27] H. Hartung and L. Pluschke, *The Benefits and Risks of Solar-Powered Irrigation: A Global Overview*. Rome, Italy: Food and Agriculture Organization of the United Nations (FAO), 2018, ISBN: 978-92-5-130479-2. [Online]. Available: https://www.fao.org/4/i9047en/I9047EN.pdf

[28] G. Li, X. Li, and Q. Zeng, “Development of automatic irrigation and soil moisture monitoring system based on solar energy in citrus orchard,” *Transactions of the Chinese Society of Agricultural Engineering*, vol. 28, no. 12, pp. 140–145, 2012, doi: 10.3969/j.issn.1002-6819.2012.12.024.

[29] J. M. Domínguez-Niño, H. R. Bogena, J. A. Huisman, B. Schilling, and J. Casadesús, “On the Accuracy of Factory-Calibrated Low-Cost Soil Water Content Sensors,” *Sensors*, vol. 19, no. 14, art. 3101, 2019, doi: 10.3390/s19143101.

[30] N. Durga, S. L. Postigo, and M. Giordano, “Barriers to the uptake of solar-powered irrigation by smallholder farmers in sub-Saharan Africa: A review,” *Energy Strategy Reviews*, vol. 51, art. 101294, 2024, doi: 10.1016/j.esr.2024.101294.

[31] Mitra dan Tim Proyek, “Transkrip Wawancara Kebun Jeruk Limau Audio 1 dan Audio 2 Ciberes Subang,” dokumentasi primer tidak diterbitkan, dihimpun Oktober 2026.

---

## Lampiran: Ringkasan Transkrip Wawancara Mitra Lapangan (Audio 1 dan Audio 2 Ciberes)

Catatan Bukti Kebutuhan Pengguna: Berdasarkan rekaman Audio 1 dan Audio 2 wawancara langsung bersama pengelola kebun jeruk limau di Desa Ciberes, Kecamatan Patokbeusi, Kabupaten Subang, Jawa Barat:

1. **Populasi dan Karakteristik Tanaman Jeruk Limau**: Lahan ditanami pohon jeruk limau (*Citrus amblycarpa*) dengan estimasi populasi sekitar 500 hingga 600 pohon. Rata-rata tinggi tajuk pohon saat ini berkisar $\pm 1\text{ meter}$ (tanaman muda/fase pertumbuhan produktif awal). Pohon dipupuk secara periodik dua kali dalam setahun menggunakan pupuk NPK dan pupuk kandang organik.
2. **Geometri Lahan dan Saluran Parit Galian**: Lahan memanjang dengan bentang lintasan $\sim 100\text{ m}$ hingga 117,52 m dan lebar $\sim 25\text{--}30\text{ m}$. Memiliki 3 lajur parit tanah memanjang (lebar 0,5–0,6 m, kedalaman 0,4–0,5 m) dengan parit melintang penghubung. Parit dibuat dengan biaya galian hemat untuk mendekatkan air ke barisan pohon, namun air parit cepat surut dan habis setelah pompa dimatikan akibat rembesan lateral tanah bebas.
3. **Sumber Suplai Air dan Riwayat Pompa Mesin**: Air disedot dari aliran sungai/saluran irigasi primer yang berjarak sekitar 20,54 meter dari batas lahan kebun. Pompa yang digunakan adalah pompa mesin bensin Alkon 2 inci (berbahan bakar Pertalite). Mitra sempat mencoba memodifikasi sistem bahan bakar memakai tabung gas LPG 3 kg demi menekan biaya, namun dihentikan permanen karena blok mesin mengalami kenaikan suhu ekstrem (*overheating*).
4. **Ketiadaan Akses Jaringan Listrik PLN**: Lokasi kebun berada di hamparan lahan persawahan terbuka pedesaan yang belum terjangkau instalasi tiang dan jaringan distribusi listrik tegangan rendah PLN (kondisi off-grid murni).
5. **Praktik Penyiraman Eksisting dan Beban Tenaga Kerja**: Air sungai dipompa masuk ke parit galian, kemudian disiramkan ke tanaman secara manual oleh 4 orang pekerja harian lepas menggunakan timba ember kecil bervolume $\sim 5\text{ Liter}$ (masing-masing pohon diguyur 2–3 ember). Proses penyiraman menyita waktu 4 hingga 6 jam per siklus kegiatan.
6. **Struktur Biaya Upah Tenaga Kerja Manual**: Upah pekerja adalah Rp100.000 per orang per hari kerja. Total pengeluaran per satu kali kegiatan penyiraman adalah Rp400.000 (4 orang $\times$ Rp100.000). Penyiraman dilakukan rutin rata-rata 3 hari sekali pada musim kemarau ($\sim 10\text{--}12\text{ kali/bulan}$). Estimasi akumulasi upah mencapai Rp48.700.000 per tahun, memberatkan total modal pembukaan lahan mitra ($\sim\text{Rp90 juta}$).
7. **Dosis Air Berdasarkan Kebiasaan Praktis Petani**: Petani memperkirakan rata-rata satu pohon menerima sekitar 10 hingga 15 Liter air per kali siram, namun volume aktual per pohon tidak pernah ditakar secara presisi sehingga terjadi variasi kelembapan tanah yang mencolok antar-zona.
8. **Ekspektasi dan Kebutuhan Solusi Otomasi**: Pengelola menginginkan adanya alat atau sistem otomatis/mekanis yang mampu menggantikan pekerjaan guyur manual tersebut agar pengeluaran upah tenaga kerja dapat dipangkas drastis (target biaya operasional $\le \text{Rp50.000/siklus}$), pasokan air ke pohon menjadi teratur dan terjamin, modal lekas kembali dalam 1–2 tahun, serta sistem mudah dioperasikan oleh pekerja lokal tanpa kerumitan teknis.
