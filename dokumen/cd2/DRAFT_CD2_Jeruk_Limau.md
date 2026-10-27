# DOKUMEN CD-2: SPESIFIKASI DAN BATASAN PERANCANGAN SISTEM IRIGASI KEBUN JERUK LIMAU DI CIBERES SUBANG

**Program Studi S1 Teknik Komputer**  
**Fakultas Teknik Elektro, Universitas Telkom, Bandung**  
**Tahun Akademik 2026/2027**

---

### Data Dokumen dan Lembar Pengesahan (Tabel 0 & Tabel 1)

**Judul Capstone Design**

Analisis Permasalahan Penyiraman Manual pada Kebun Jeruk Limau di Ciberes Subang
**Jenis Dokumen**

Spesifikasi
**Nomor Dokumen**

FTE-CD-2
**Nomor Revisi**

00
**Tanggal Pengesahan**

29 Oktober 2026
**Fakultas**

Fakultas Teknik Elektro
**Program Studi**

S1 Teknik Komputer

**Tim Penulis (Mahasiswa):**
1. Muhammad Al Qarnie / NIM: 101032330043
2. Maheswara Ariq Athallah / NIM: 101032300050
3. Daffa Hermansyah / NIM: 101032330090

**Disetujui Oleh:**
**Pembimbing 1**

Dr. Agung Nugroho Jati, S.T., M.T. (Jabatan: Pembimbing 1)

---

### Timeline Revisi Dokumen (Tabel 2)

| Versi, Tanggal | Revisi | Perbaikan yang Dilakukan | Halaman Revisi |
|---|---|---|---|
| 00, 26 Oktober 2026 | Draf Awal CD-2 | Penyusunan dasar pemilihan spesifikasi berbasis multi-rujukan (wawancara mitra, regulasi pemerintah, standar ASABE/IEC/SNI, literatur agronomi), perumusan batasan rekayasa, matriks spesifikasi kuantitatif multi-aspek (teknis, ekonomi, lingkungan, operasional), serta metode pengukuran dan verifikasi terperinci. | Seluruh Dokumen |
| | | *(Disediakan untuk catatan revisi dosen pembimbing)* | |
| | | *(Disediakan untuk catatan revisi dosen pembimbing)* | |

---

# BAB 1: SPESIFIKASI DAN BATASAN DESAIN SISTEM IRIGASI

Dokumen CD-2 ini merupakan kelanjutan langsung dari dokumen CD-1 (*Analisis Permasalahan Penyiraman Manual pada Kebun Jeruk Limau di Ciberes Subang*) yang telah disahkan oleh dosen pembimbing. Jika CD-1 berfokus pada identifikasi akar masalah, kendala empiris, kompleksitas permasalahan rekayasa, serta kajian kelemahan solusi eksisting, maka dokumen CD-2 ini menetapkan landasan batas operasional (*constraints*) dan spesifikasi kuantitatif (*specifications*) yang wajib dipenuhi oleh solusi rekayasa yang akan dirancang pada tahap CD-3. 

Perumusan batasan dan spesifikasi ini dirancang secara terukur (*measurable*), realistis (*feasible*), memiliki dasar ilmiah yang kokoh (*grounded*), serta bersifat abstrak terhadap pilihan solusi atau merek tertentu (*solution-agnostic*). Pendekatan ini memastikan bahwa ruang perancangan pada tahap CD-3 tetap terbuka untuk mengevaluasi berbagai alternatif solusi (seperti jaringan mikroirigasi perpipaan, wahana bergerak semi-otonom, maupun sistem hibrida) tanpa bias awal pada merek atau teknologi perangkat keras tertentu.

---

## 1.1 Dasar Penentuan Spesifikasi

Penentuan batasan dan spesifikasi dalam proses rekayasa sistem (*engineering design process*) tidak boleh didasarkan pada asumsi subjektif yang mengada-ada. Pada perancangan sistem irigasi kebun jeruk limau mitra di Ciberes, Subang, penetapan seluruh parameter kuantitatif didasarkan pada sintesis empat pilar rujukan utama: (1) kebutuhan pengguna dan data empiris mitra lapangan, (2) regulasi pemerintah dan standar teknis industri, (3) literatur ilmiah fisiologi tanaman dan neraca air, serta (4) karakteristik tapak lahan dan keterbatasan infrastruktur eksisting.

### 1.1.1 Kebutuhan Pengguna dan Hasil Wawancara Lapangan (Mitra Ciberes)
Kebutuhan mitra pengelola kebun jeruk limau di Ciberes, Subang digali melalui wawancara mendalam dan observasi langsung di tapak kebun (Transkrip Wawancara Audio 1, terlampir). Dari hasil observasi tersebut, teridentifikasi sejumlah *pain points* operasional dan ekspektasi fungsional mitra:
**1. Beban Biaya Tenaga Kerja Manual**

Untuk menyiram populasi sekitar 500–600 pohon jeruk limau yang membentang di atas lahan sepanjang ~100 m, pengelola kebun mempekerjakan 4 orang pekerja harian lepas dengan upah masing-masing Rp100.000 per kegiatan (total Rp400.000 per kegiatan). Kegiatan penyiraman dilakukan rutin rata-rata setiap 3 hari sekali (terutama pada musim kemarau dan masa transisi buah). Skenario perhitungan tahunan menunjukkan estimasi pengeluaran tenaga kerja penyiraman mencapai Rp48,7 juta/tahun. Pengelola kebun secara eksplisit menyatakan kebutuhan utama untuk menekan atau mengeliminasi pengeluaran upah manual ini melalui penerapan mekanisasi atau otomasi.
**2. Ketidakpastian dan Ketidakmerataan Dosis Air**

Praktik penyiraman eksisting mengandalkan pekerja yang menimba air parit menggunakan ember hitam kecil lalu mengguyurkannya ke tiap pohon. Pekerja tidak mengukur volume air per pohon, sehingga pohon di area dekat titik pompa berisiko menerima air berlebih, sementara pohon di ujung parit berisiko kekurangan air atau bahkan terlewat akibat kelelahan fisik pekerja.
**3. Ketergantungan Pompa Berbahan Bakar Bensin (Pertalite)**

Pasokan air disedot dari sungai berjarak 20,54 m menuju tiga lajur parit tanah menggunakan pompa mesin berbahan bakar Pertalite. Mitra mengeluhkan biaya operasional bahan bakar, kerepotan pemeliharaan mekanik berkala, serta uji coba bahan bakar gas LPG masa lalu yang dihentikan karena mesin mengalami panas berlebih (*overheat*).
**4. Ekspektasi Solusi dari Mitra**

Mitra mengharapkan sistem baru mampu mengalirkan air dalam jumlah yang cukup (mengacu pada estimasi praktis petani minimal 10–15 Liter per pohon per siklus), dapat beroperasi secara terjadwal/teratur, mudah dioperasikan oleh pekerja lokal tanpa kerumitan teknis, serta memiliki biaya investasi awal dan pemeliharaan yang terjangkau agar modal dapat tertutup dari penghematan upah tenaga kerja dalam kurun waktu 1–2 tahun.

### 1.1.2 Regulasi Pemerintah dan Standar Teknis Industri
Perancangan sistem rekayasa wajib mematuhi kerangka hukum, regulasi tata air nasional, dan standar konsensus industri internasional:
**1. Standar Keseragaman Irigasi Mikro (ASABE S398.1 & ASABE EP405.1)**

*American Society of Agricultural and Biological Engineers* (ASABE) menetapkan standar evaluasi keseragaman distribusi air irigasi mikro (*Christiansen's Uniformity Coefficient*, $CU$). Untuk irigasi presisi pada tanaman hortikultura tahunan bernilai ekonomi tinggi, nilai $CU$ minimum yang disyaratkan adalah $\ge 80\%$, dengan target ideal pada perancangan rekayasa baru mencapai $\ge 85\%$. Nilai keseragaman ini menjamin setiap pohon menerima pasokan air seragam terlepas dari jarak pohon terhadap sumber suplai.
2. **Kebijakan dan Standar Teknis Irigasi Pertanian Nasional dan Internasional (PP No. 20/2006 & ISO 9261:2004) [6], [7]:** Peraturan Pemerintah Republik Indonesia No. 20 Tahun 2006 tentang Irigasi menegaskan prinsip konservasi air bahwa penyediaan dan pemanfaatan air irigasi wajib diselenggarakan secara tertib, efisien, adil, dan berkelanjutan, serta memprioritaskan efisiensi pemanfaatan air untuk komoditas hortikultura produktif. Sejalan dengan regulasi nasional tersebut, standar internasional ISO 9261:2004 (*Agricultural irrigation equipment — Emitters and emitting pipe*) menetapkan parameter baku keseragaman laju pancaran air mikroirigasi (variasi debit emitter < 7%) guna mencegah kehilangan air akibat evaporasi parit terbuka, mencegah genangan lokal, serta meniadakan *run-off* yang memicu erosi unsur hara perakaran.
3. **Standar Proteksi Selungkup Lingkungan Terbuka (IEC 60529 / SNI IEC 60529:2014):** Peralatan instrumentasi, kontroler elektronik, akuisisi data, dan sistem daya yang beroperasi di lingkungan pertanian terbuka tanpa naungan permanen wajib memiliki tingkat proteksi selungkup (*Ingress Protection*) minimal **IP65**. Standar ini menjamin selungkup kedap terhadap partikel debu tanah secara total (*dust-tight*) dan terlindung dari semprotan air bertekanan rendah dari segala arah tanpa terjadi kebocoran yang merusak rangkaian sirkuit.
**4. Standar Keamanan Kelistrikan dan Jaringan Sensor (IEEE 1451 & IEC 60364-4-41)**

Seluruh perangkat kelistrikan yang dipasang di area basah pertanian terbuka wajib beroperasi pada batas tegangan ekstra rendah aman (*Safety Extra-Low Voltage* / SELV $\le 48\text{ V DC}$) untuk mencegah bahaya sengatan listrik bagi manusia dan hewan ternak. Standar komunikasi instrumentasi IEEE 1451 dan IEEE 802.15.4 digunakan sebagai acuan arsitektur transmisi data sensor nirkabel berdaya rendah (*low-power wireless sensor network*).
**5. Standar Sistem Pembangkit Listrik Tenaga Surya Mandiri (IEC 62124)**

Standar *Photovoltaic Stand-Alone Systems: Design Verification* (IEC 62124) menetapkan bahwa sistem fotovoltaik *off-grid* pertanian harus dirancang dengan kapasitas cadangan energi (*days of autonomy*) minimal 1,5 hingga 2 hari operasi tanpa radiasi matahari langsung guna mengantisipasi cuaca mendung berkepanjangan pada musim transisi.

### 1.1.3 Karakteristik Fisiologi Tanaman Jeruk Limau dan Literatur Agronomi
Karakteristik biologis tanaman jeruk limau (*Citrus amblycarpa Hassk. Ochse*) menjadi fondasi penentuan dosis volume, frekuensi, dan zona pembasahan:
**1. Morfologi Perakaran Dangkal**

Penelitian Budiarto dkk. (2017) dan pedoman Florida Citrus Extension (Obreza dkk., 2020) menunjukkan bahwa perakaran tanaman jeruk didominasi oleh akar serabut aktif (*feeder roots*) pada lapisan tanah dangkal dengan kedalaman $20 - 40\text{ cm}$ dan radius persebaran horizontal $0,5 - 0,8\text{ m}$ mengikuti proyeksi tajuk tanaman. Pemberian air di luar radius tersebut tidak efektif diserap oleh tanaman dan hanya akan memicu pertumbuhan gulma liar.
**2. Kebutuhan Air Berbasis Model FAO-56**

Mengacu pada pedoman standar FAO Irrigation and Drainage Paper 56 (Allen dkk., 1998) serta panduan manajemen air jeruk dari University of Florida IFAS Extension (Kadyampakeni dkk., 2023), estimasi kebutuhan air tanaman jeruk limau muda dihitung secara presisi menggunakan model evapotranspirasi standar Penman-Monteith (Persamaan 1):

$$
ET_c = K_c \times ET_0 \tag{1}
$$

Di mana:
- $ET_c$ = laju evapotranspirasi aktual tanaman (mm/hari)
- $K_c$ = koefisien tanaman jeruk limau muda kanopi sedang ($K_c = 0,70 - 0,80$)
- $ET_0$ = laju evapotranspirasi acuan lingkungan Ciberes Subang pada musim kemarau ($ET_0 = 4,5 - 5,0\text{ mm/hari}$)

Selanjutnya, volume air terukur yang wajib diberikan per pohon dalam satu siklus penyiraman ($V_{pohon}$) dihitung melalui persamaan volume neraca air (Persamaan 2):

$$
V_{pohon} = ET_c \times A_{tajuk} \times I_{siram} \tag{2}
$$

Di mana:
- $A_{tajuk}$ = luas proyeksi kanopi tajuk basah perakaran ($\sim 1,0\text{ m}^2$)
- $I_{siram}$ = interval frekuensi penyiraman ($2 - 3\text{ hari per siklus}$)

Melalui substitusi nilai parameter lapangan tersebut, diperoleh kebutuhan air berkisar **$10 - 15\text{ Liter per pohon per siklus penyiraman}$**. Hasil perhitungan matematis ini memvalidasi secara ilmiah taksiran kebiasaan empiris petani mitra di kebun Ciberes [1], [16].
3. **Pencegahan Risiko Pembusukan Akar (*Phytophthora nicotianae*):** Literatur patologi jeruk oleh Graham & Timmer (2020) serta pedoman Smajstrla dkk. (2021) memperingatkan bahwa kejenuhan air tanah yang berlangsung lama (*waterlogging* $> 24 - 48\text{ jam}$) akibat penggenangan parit atau drainase yang buruk merupakan pemicu utama serangan patogen jamur tanah *Phytophthora nicotianae* dan *Phytophthora palmivora* yang menyebabkan busuk perakaran dan kanker pangkal batang (*foot rot*). Oleh karena itu, spesifikasi pemberian air harus menjamin aerasi tanah tetap terjaga dan tidak menimbulkan kubangan air tergenang lebih dari 30 menit setelah proses penyiraman selesai.

### 1.1.4 Karakteristik Tapak Lahan Eksisting dan Keterbatasan Sumber Daya
Spesifikasi sistem rekayasa harus selaras dengan kendala fisik tapak kebun di Ciberes:
**1. Ketiadaan Akses Listrik PLN**

Tapak kebun terletak jauh dari jaringan distribusi tegangan rendah PLN. Segala bentuk rancangan sistem tidak boleh bergantung pada sumber listrik jala-jala PLN, melainkan wajib mandiri (*self-sufficient / off-grid*) memanfaatkan energi terbarukan (seperti pembangkit listrik tenaga surya / fotovoltaik) yang dipadukan dengan modul penyimpan daya (baterai) atau sumber mekanik efisien.
**2. Karakteristik Air Sungai dan Kebutuhan Filtrasi**

Sumber air utama kebun berasal dari aliran sungai/saluran irigasi yang berjarak 20,54 m dari tepi lahan kebun. Air permukaan alami memiliki tingkat kekeruhan dinamis dan membawa muatan padatan tersuspensi (*suspended solids*) berupa partikel pasir halus, lumpur sedimen, dan serpihan organik (Ayers & Westcot, 1985; Bounoua dkk., 2016). Kondisi ini mewajibkan adanya subsistem penyaringan fisik (*filtration*) dengan kapasitas penyaringan minimal 120 mesh ($130\ \mu\text{m}$) agar pipa, pompa mikro, katup solenoid, maupun nozzle tidak mengalami penyumbatan fisik (*clogging*).
**3. Geometri Jaringan Kebun**

Populasi 500–600 pohon tertata dalam barisan teratur di antara tiga lajur galian parit tanah sepanjang 100 m dengan lebar blok 20,54 m. Jarak antar pohon berkisar antara 2–3 meter. Spesifikasi sistem harus mampu mendistribusikan air menjangkau seluruh panjang lintasan 100 m tersebut secara merata tanpa kehilangan tekanan hidrolik yang berlebihan.

---

## 1.2 Batasan dan Spesifikasi Solusi

Berdasarkan sintesis dari seluruh dasar pertimbangan di atas, bagian ini menetapkan batasan rekayasa (*engineering constraints*) dan daftar spesifikasi kuantitatif (*engineering specifications*). Sesuai dengan kaidah Buku Panduan Capstone FTE Telkom University, spesifikasi dirumuskan secara **abstrak terhadap pilihan solusi atau merek tertentu (*solution-agnostic*)**, sehingga tidak mengikat perancangan pada satu opsi teknologi saja sebelum dilakukan komparasi alternatif pada dokumen CD-3.

### 1.2.1 Batasan Rekayasa Solusi (*Engineering Constraints*)
Batasan rekayasa merupakan kondisi batas mutlak (*hard constraints*) yang tidak dapat dilanggar oleh arsitektur solusi mana pun yang akan dirancang:
**C-01. Kemandirian Energi / Off-Grid Standalone**

Sistem harus beroperasi secara mandiri tanpa memerlukan sambungan jala-jala listrik PLN kebun, menggunakan pasokan daya lokal berbasis energi terbarukan atau baterai.
**C-02. Kompatibilitas Sumber Air Permukaan Berpartikulat**

Sistem harus mampu memproses air baku dari sungai/saluran irigasi terbuka berkekeruhan alami tanpa mengalami kerusakan pompa dan tanpa mengalami kegagalan fungsi akibat sedimentasi.
**C-03. Kompatibilitas Geometri dan Topografi Kebun**

Sistem harus mampu melayani area kebun seluas 500–600 pohon dengan rentang lintasan memanjang hingga 100 m dan lebar 20,5 m tanpa merusak struktur batang dan perakaran dangkal tanaman.
**C-04. Keselamatan Kelistrikan Area Terbuka / SELV**

Seluruh subsistem elektrikal dan instrumentasi yang terpasang di area basah kebun wajib beroperasi pada rentang tegangan ekstra rendah aman (*Safety Extra-Low Voltage* $\le 48\text{ V DC}$) sesuai IEC 60364-4-41.
**C-05. Netralitas Solusi / Solution-Agnostic**

Perumusan batasan dan spesifikasi tidak mengunci pilihan arsitektur pada satu merek komponen tertentu atau satu jenis solusi mekanis tertentu (memberikan fleksibilitas penuh untuk mengevaluasi opsi jaringan perpipaan mikro, sistem mekanisasi gerak semi-otonom, maupun solusi hibrida pada CD-3).

### 1.2.2 Spesifikasi Kuantitatif Solusi (*Engineering Specifications*)
Spesifikasi rekayasa dijabarkan ke dalam empat aspek menyeluruh: teknis, ekonomi, lingkungan, dan operasional/kemitraan. Ringkasan seluruh spesifikasi kuantitatif disajikan pada **Tabel 3**, yang kemudian diikuti dengan deskripsi penjelasan mendalam pada masing-masing parameternya.

#### Tabel 3: Matriks Batasan dan Spesifikasi Kuantitatif Solusi

| ID | Parameter Spesifikasi | Nilai Target & Toleransi | Satuan | Kategori Aspek | Rujukan Penentuan |
|---|---|---|---|---|---|
| **S-01** | Akurasi Dosis Volume Air per Pohon | $10 - 15 \pm 5\%$ | Liter/pohon | Aspek Teknis | Wawancara Mitra, FAO-56 [1], Florida IFAS [16] |
| **S-02** | Koefisien Keseragaman Distribusi Air ($CU$) | $\ge 85$ | $\%$ | Aspek Teknis | Standar ASABE S398.1, EP405.1 |
| **S-03** | Durasi Total Siklus Penyiraman Kebun | $\le 4,0$ | Jam/siklus | Aspek Teknis | Batas Waktu Operasi Harian Mitra |
| **S-04** | Radius dan Kedalaman Pembasahan Efektif | $r = 0,5 - 0,8$; $d = 20 - 40$ | cm | Aspek Teknis | Morfologi Perakaran Jeruk Limau [15], [22] |
| **S-05** | Derajat Filtrasi Fisik Partikulat | $\ge 120$ (kemampuan saring $\le 130$) | mesh ($\mu\text{m}$) | Aspek Teknis | Standar Kualitas Air FAO-29 [12], Ayers [13] |
| **S-06** | Ketahanan Cadangan Energi Mandiri (*Autonomy*) | $\ge 8,0$ (minimal 2 siklus penuh tanpa surya) | Jam operasi | Aspek Teknis | Standar IEC 62124 (Off-Grid PV) |
| **S-07** | Ketahanan Lingkungan Selungkup (*Ingress Protection*) | IP65 (Suhu operasi: $20 - 55$) | Rating ($^\circ\text{C}$) | Aspek Teknis | Standar IEC 60529 / SNI IEC 60529:2014 |
| **S-08** | Batas Biaya Investasi Awal Sistem (CAPEX) | $\le 18.000.000$ | Rupiah (Rp) | Aspek Ekonomi | Analisis Kelayakan Payback Period |
| **S-09** | Biaya Operasional per Siklus Penyiraman (OPEX) | $\le 50.000$ (Efisiensi $\ge 85\%$ vs manual) | Rupiah (Rp) | Aspek Ekonomi | Biaya Upah Manual Eksisting (Rp400.000) |
| **S-10** | Periode Pengembalian Modal (*Payback Period*) | $\le 12 - 18$ | Bulan | Aspek Ekonomi | Skenario Penghematan Upah Rp48,7 Juta/Tahun |
| **S-11** | Efisiensi Aplikasi Air Irigasi ($\eta_a$) | $\ge 80$ | $\%$ | Aspek Lingkungan | PP No. 20/2006 [6], ISO 9261 [7], FAO-56 [1] |
| **S-12** | Emisi Gas Buang di Zona Tajuk Perakaran | $0$ (Bebas emisi hidrokarbon lokal) | $\text{g/kWh}$ | Aspek Lingkungan | Perlindungan Kualitas Tanah Perakaran |
| **S-13** | Kemudahan Pengoperasian oleh Operator Mitra | *Single-touch* / semi-otonom (Waktu ajar $\le 30$) | Menit | Aspek Operasional | Profil Tenaga Kerja Lokal Kebun Ciberes |
| **S-14** | Durasi Pemeliharaan Rutin Saringan/Mekanik | $\le 20$ (Menggunakan perkakas lokal) | Menit/bulan | Aspek Operasional | Keterbatasan Bengkel Khusus di Pedesaan |

#### Penjelasan Komprehensif Masing-Masing Spesifikasi:

**1. S-01 (Akurasi Dosis Volume Air per Pohon)**

Sistem harus mampu menyalurkan volume air terukur antara 10 hingga 15 Liter untuk tiap tanaman jeruk limau dengan batas simpangan kesalahan (*error tolerance*) tidak lebih dari $\pm 5\%$. Nilai kuantitatif ini menjamin tanaman terhidrasi sesuai laju evapotranspirasi lingkungan tanpa risiko pemberian air berlebih (*over-irrigation*) yang memboroskan sumber daya air.
**2. S-02 (Koefisien Keseragaman Distribusi Air - $CU$)**

Mengacu pada standar ANSI/ASAE S398.1 dan ASAE EP405.1, keseragaman volume air yang diterima oleh pohon di awal, tengah, dan ujung barisan parit harus mencapai minimal 85%. Evaluasi keseragaman distribusi air dihitung menggunakan formula Koefisien Keseragaman Christiansen (*Christiansen's Uniformity Coefficient*, $CU$) sebagaimana ditunjukkan pada Persamaan 3 [2], [3]:

$$
CU = 100\% \times \left[ 1 - \frac{\sum_{i=1}^{n} |X_i - \bar{X}|}{n \times \bar{X}} \right] \tag{3}
$$

Di mana:
- $CU$ = *Christiansen's Uniformity Coefficient* (%)
- $n$ = jumlah pohon sampel uji ($n = 15\text{ bejana}$)
- $X_i$ = volume air tertampung pada bejana sampel ke-$i$ (Liter atau mL)
- $\bar{X}$ = rata-rata volume air dari seluruh bejana sampel ($\bar{X} = \frac{1}{n} \sum_{i=1}^{n} X_i$)

Nilai keseragaman $CU \ge 85\%$ menjamin pertumbuhan seluruh pohon jeruk limau tetap homogen tanpa adanya pohon yang mengalami kekeringan ekstrem atau pembusukan akar.
**3. S-03 (Durasi Total Siklus Penyiraman Kebun)**

Seluruh proses penyiraman untuk 500–600 pohon harus dapat dituntaskan dalam waktu kurang dari atau sama dengan 4 jam per siklus kegiatan. Hal ini memberikan efisiensi waktu yang masif dibandingkan metode manual 4 orang buruh yang menyita waktu seharian penuh, serta memanfaatkan waktu siram ideal (pagi hari sebelum pukul 10.00 WIB atau sore hari setelah pukul 15.00 WIB) guna meminimalkan kehilangan air akibat evaporasi radiasi matahari langsung.
**4. S-04 (Radius dan Kedalaman Pembasahan Efektif)**

Air irigasi diarahkan meresap pada area proyeksi kanopi tanaman dengan radius 0,5–0,8 m dari pangkal batang hingga mencapai kedalaman profil tanah 20–40 cm. Distribusi air yang terkonsentrasi pada zona perakaran aktif serabut menghindarkan pembasahan batang utama yang rentan jamur batang serta tidak membasahi area jalan antar-baris secara sia-sia.
**5. S-05 (Derajat Filtrasi Fisik Partikulat)**

Untuk mengatasi kekeruhan air sungai Ciberes, sistem wajib dilengkapi dengan saringan partikulat dengan kerapatan minimal 120 mesh (mampu menyaring partikel berdiameter $\ge 130\ \mu\text{m}$). Hal ini merupakan syarat wajib untuk mencegah terjadinya penyumbatan mekanis pada emiter, lubang nozzle, katup pengontrol, dan impeller pompa air mikro.
**6. S-06 (Ketahanan Cadangan Energi Mandiri / Autonomy)**

Subsistem daya mandiri (*off-grid*) harus mampu menyuplai kebutuhan daya operasional beban penuh selama minimal 8 jam kerja kontinu tanpa kehadiran cahaya matahari langsung (setara dengan cadangan daya untuk minimal 2 siklus penyiraman lengkap). Mengacu pada standar IEC 62124 (*Photovoltaic stand-alone systems*), konsumsi energi operasional per siklus penyiraman ($E_{siklus}$) dan kapasitas minimum modul penyimpan daya ($C_{baterai}$) dihitung melalui Persamaan 4 dan Persamaan 5 [8]:

$$
E_{siklus} = P_{beban} \times t_{operasi} \tag{4}
$$

$$
C_{baterai} \ge \frac{E_{siklus} \times N_{autonomy}}{V_{sistem} \times DoD} \tag{5}
$$

Di mana:
- $E_{siklus}$ = energi operasional satu siklus (Wh)
- $P_{beban}$ = total daya pompa dan kontroler (Watt)
- $t_{operasi}$ = durasi kerja satu siklus ($\le 4\text{ jam}$)
- $N_{autonomy}$ = faktor otonomi cadangan ($\ge 2\text{ siklus} = 8\text{ jam}$)
- $V_{sistem}$ = tegangan kerja ekstra rendah aman ($12\text{ V DC}$ atau $24\text{ V DC}$)
- $DoD$ = *Depth of Discharge* aman baterai ($DoD = 80\%$ untuk LiFePO4)

Hal ini menjamin keandalan operasi pompa tetap prima saat cuaca berawan berturut-turut.
**7. S-07 (Ketahanan Lingkungan Selungkup / Ingress Protection)**

Seluruh kotak kontrol (*controller enclosure*), konektor kelistrikan, papan modul sensor, dan unit catu daya wajib bersertifikasi minimal IP65 serta mampu bekerja normal pada rentang suhu ambien $20^\circ\text{C}$ hingga $55^\circ\text{C}$. Selungkup harus tahan terhadap terpaan panas matahari tropis Subang, percikan lumpur tanah, dan semprotan air saat pembersihan kebun.
**8. S-08 (Batas Biaya Investasi Awal / CAPEX)**

Total biaya rancang bangun, belanja komponen, fabrikasi struktural, instalasi sistem, dan instrumentasi dibatasi maksimal Rp18.000.000. Angka batas atas ini ditetapkan secara rasional agar investasi terjangkau oleh petani skala menengah dan tidak melebihi alokasi dana kelayakan modal usaha tani.
**9. S-09 (Biaya Operasional per Siklus / OPEX)**

Biaya operasional yang mencakup konsumsi energi (pengisian daya/bahan bakar cadangan) dan alokasi jasa pemantauan operator ditekan hingga maksimal Rp50.000 per siklus penyiraman. Hal ini menghasilkan penghematan biaya langsung sebesar 87,5% per kegiatan dibandingkan pengeluaran rutin upah guyur manual eksisting (Rp400.000 per kegiatan).
**10. S-10 (Periode Pengembalian Modal / Payback Period)**

Kelayakan ekonomi sistem rekayasa dinilai berdasarkan kecepatan pengembalian modal investasi awal (*Payback Period*, $PP$). Periode pengembalian modal dihitung dengan formula rasio investasi awal ($CAPEX$) terhadap selisih penghematan biaya operasional tahunan ($\Delta OPEX_{tahunan}$) pada Persamaan 6:

$$
PP = \frac{CAPEX}{\Delta OPEX_{tahunan}} \tag{6}
$$

Di mana:
- $PP$ = *Payback Period* (dalam tahun atau bulan)
- $CAPEX$ = modal investasi awal sistem rekayasa ($\le \text{Rp}18.000.000$)
- $\Delta OPEX_{tahunan}$ = selisih penghematan biaya operasional tahunan antara metode manual eksisting ($\text{Rp}400.000/\text{kegiatan} \times \approx 120\text{ siklus/tahun} \approx \text{Rp}48.000.000/\text{tahun}$) dengan biaya operasional sistem baru ($\le \text{Rp}50.000/\text{siklus} \times \approx 120\text{ siklus/tahun} \approx \le \text{Rp}6.000.000/\text{tahun}$)

Dengan selisih penghematan bersih mencapai lebih dari Rp42.000.000 per tahun, target titik impas modal dipastikan tercapai dalam kurun waktu 12 hingga 18 bulan operasi.

**11. S-11 (Efisiensi Aplikasi Air Irigasi / $\eta_a$)**

Mengacu pada prinsip konservasi air PP No. 20 Tahun 2006 dan standar FAO-56, efisiensi aplikasi air ($\eta_a$) dihitung dari rasio volume air yang tersimpan di zona perakaran aktif serabut terhadap volume total air yang dialirkan dari sumber melalui Persamaan 7 [1], [6], [7]:

$$
\eta_a = \left( \frac{V_{akar}}{V_{sumber}} \right) \times 100\% \tag{7}
$$

Di mana:
- $\eta_a$ = efisiensi aplikasi air irigasi (%)
- $V_{akar}$ = volume air yang meresap dan tertahan pada zona perakaran aktif pohon jeruk (kedalaman $20 - 40\text{ cm}$ dan radius $0,5 - 0,8\text{ m}$)
- $V_{sumber}$ = volume total air yang disedot dari sungai melalui pipa masukan utama

Sistem baru ditargetkan mencapai $\eta_a \ge 80\%$, melompat jauh melampaui efisiensi penyiraman parit tanah konvensional eksisting yang kerap di bawah 40–50% akibat rembesan horizontal tanah galian dan evaporasi terbuka di sepanjang parit 100 meter.
**12. S-12 (Emisi Gas Buang di Zona Tajuk Perakaran)**

Sistem operasi penyiraman di sekitar barisan tanaman tidak menghasilkan emisi gas buang jelaga karbon monoksida maupun tetesan residu pelumas oli di atas tanah perakaran. Hal ini memperbaiki kelemahan pompa pembakaran internal berbahan bakar bensin/Pertalite eksisting yang mencemari lingkungan perakaran dan berisiko meracuni mikroorganisme tanah penyubur jeruk.
**13. S-13 (Kemudahan Pengoperasian oleh Operator Mitra)**

Antarmuka pengguna (*user interface*) dirancang dengan logika operasional sederhana (*semi-autonomous / single-button start*). Pekerja kebun lokal dengan latar belakang pendidikan dasar dapat mengoperasikan dan memantau status penyiraman dengan waktu pelatihan singkat tidak lebih dari 30 menit.
**14. S-14 (Durasi Pemeliharaan Rutin Saringan dan Mekanik)**

Desain mekanis sistem dirancang modular sehingga proses pembongkaran, pembersihan saringan kotoran, dan perakitan kembali dapat dituntaskan oleh satu orang pekerja dalam waktu kurang dari 20 menit per bulan menggunakan perkakas bengkel pertanian umum (seperti obeng dan kunci pas standar tanpa memerlukan alat kalibrasi khusus).

---

## 1.3 Pengukuran dan Verifikasi Spesifikasi

Untuk membuktikan secara ilmiah dan kuantitatif bahwa solusi rekayasa yang dikembangkan pada tahap selanjutnya benar-benar memenuhi spesifikasi yang dijanjikan, bagian ini menyusun rencana pengukuran dan prosedur verifikasi (*verification protocol*). Setiap spesifikasi dilengkapi dengan metode standar pengujian, peralatan ukur terkalibrasi, mekanisme langkah pengujian, serta kriteria keberhasilan verifikasi yang disajikan pada **Tabel 4**.

#### Tabel 4: Matriks Rencana Pengukuran dan Verifikasi Spesifikasi

| ID Spesifikasi | Parameter yang Diverifikasi | Nilai Target Uji | Metode / Standar Pengujian | Alat Ukur / Verifikasi | Kriteria Kelulusan Verifikasi |
|---|---|---|---|---|---|
| **S-01** | Volume Air per Pohon | $10 - 15 \text{ L} \pm 5\%$ | Metode Volumetrik Langsung | Wadah kalibrasi tera berstandar, Gelas ukur 1.000 mL, Flow meter digital presisi | Volume tertampung pada tiap pohon sampel berada pada rentang $9,5 - 15,75\text{ L}$. |
| **S-02** | Keseragaman Distribusi Air | $CU \ge 85\%$ | Standar ASABE S398.1 (*Catch Cans Method*) | 15 unit bejana ukur (*catch cans*), Silinder ukur mililiter, Formula Christiansen | Perhitungan matematis nilai koefisien keseragaman $CU \ge 85,0\%$. |
| **S-03** | Durasi Total Waktu Siklus | $\le 4,0\text{ Jam}$ | Pencatatan Waktu Operasi Total Siklus Kebun | Stopwatch digital terkalibrasi, Data log sistem | Timer penghentian proses pada pohon terakhir tercatat $\le 240\text{ menit}$. |
| **S-04** | Radius & Kedalaman Pembasahan | $r \ge 0,5\text{ m}$; $d \ge 20\text{ cm}$ | Pengukuran Geometris Penetrasi Tanah Basah | Pita ukur meteran baja, Bor tanah mini (*soil auger sampler*), Sensor kelembapan tanah | Profil basah tanah terdeteksi meluas radius $\ge 50\text{ cm}$ dan tembus kedalaman $\ge 20\text{ cm}$. |
| **S-05** | Derajat Filtrasi Partikulat | $\ge 120\text{ mesh}$ | Uji Hambatan Alir dan Inspeksi Ukuran Partikel | Saringan uji kawat 120 mesh ($130\ \mu\text{m}$), Manometer tekanan diferensial | Tidak ada partikel $\ge 130\ \mu\text{m}$ lolos ke sistem dan beda tekanan filter stabil. |
| **S-06** | Ketahanan Cadangan Energi | $\ge 8,0\text{ Jam}$ | Uji Beban Penuh Kontinu (*Discharge Test*) | Digital DC Power Meter, Clamp meter DC, Data logger tegangan/arus baterai | Baterai mampu memasok daya beban penuh $\ge 8$ jam tanpa jatuh di bawah ambang batas *cut-off*. |
| **S-07** | Ketahanan Selungkup Luar | IP65 & $20 - 55^\circ\text{C}$ | Standar Uji IEC 60529 (Klausul 13.4 & 14.2.5) | Nozzle semprot air diameter 6,3 mm debit 12,5 L/menit, Termometer inframerah | Tidak ada air/debu merembes ke dalam kompartemen sirkuit; operasi stabil pada $55^\circ\text{C}$. |
| **S-08** | Biaya Investasi Awal (CAPEX) | $\le \text{Rp } 18.000.000$ | Audit Finansial *Bill of Materials* (BOM) | Rekapitulasi nota belanja riil, Invoice resmi pengadaan komponen | Akumulasi total biaya pengadaan hardware dan fabrikasi tidak melebihi batas plafon. |
| **S-09** | Biaya Operasional (OPEX) | $\le \text{Rp } 50.000\text{/siklus}$ | Perhitungan Biaya Bahan Bakar/Listrik & Operator | Lembar log pengeluaran operasional per kegiatan penyiraman | Biaya habis pakai energi + upah pengawas per siklus terbukti $\le \text{Rp } 50.000$. |
| **S-10** | Periode Pengembalian Modal | $\le 12 - 18\text{ Bulan}$ | Analisis Payback Period Finansial Pertanian | Formula $PP = \frac{\text{CAPEX}}{\Delta \text{OPEX Tahunan}}$ | Nilai $PP$ terhitung menghasilkan durasi balik modal $\le 1,5\text{ tahun}$. |
| **S-11** | Efisiensi Aplikasi Air ($\eta_a$) | $\ge 80\%$ | Neraca Air Masuk vs Terserap Perakaran | Water meter aliran pipa masukan, Pengukuran volumetrik perakaran | Rasio volume air tersimpan di tanah aktif dibagi volume air tersedot $\ge 0,80$. |
| **S-12** | Emisi Gas Buang di Kebun | $0\text{ g/kWh}$ Emisi Lokal | Inspeksi Sumber Penggerak dan Deteksi Gas | Gas detector portabel (CO, HC), Pemeriksaan visual rembesan oli | Tidak terdeteksi emisi gas buang beracun dan nol tumpahan pelumas di tanah kebun. |
| **S-13** | Kemudahan Pengoperasian | Waktu ajar $\le 30\text{ Menit}$ | Uji Keterpakaian Lapangan (*Usability Testing*) | Lembar kuesioner tugas operator mitra, Stopwatch pencatat waktu tugas | Operator mitra mampu menjalankan prosedur operasional secara mandiri dalam $\le 30$ menit. |
| **S-14** | Durasi Pemeliharaan Rutin | $\le 20\text{ Menit/bulan}$ | Uji Waktu Bongkar-Pasang (*Disassembly Time*) | Stopwatch, Kotak perkakas kunci pas dan obeng standar pertanian | Prosedur *flushing* dan pembersihan saringan selesai tuntas dalam waktu $\le 20\text{ menit}$. |

---

### Prosedur dan Mekanisme Pengukuran Terperinci:

#### 1.3.1 Prosedur Verifikasi Dosis dan Keseragaman Distribusi Air (S-01, S-02, S-04)
**1. Penentuan Titik Sampel**

Pilih 15 pohon sampel yang tersebar secara acak terstratifikasi mewakili kondisi ekstrem lahan: 5 pohon di baris awal (dekat titik suplai air), 5 pohon di baris tengah lintasan (jarak ~50 m), dan 5 pohon di ujung lintasan parit (jarak ~100 m).
2. **Pemasangan Wadah Penangkap (*Catch Cans*):** Letakkan bejana penampung air terkalibrasi di bawah zona tajuk masing-masing pohon sampel dengan orientasi mengelilingi perakaran.
**3. Pelaksanaan Siklus Siram**

Jalankan sistem irigasi untuk melakukan satu siklus penyiraman penuh sesuai konfigurasi standar operasional.
**4. Pencatatan Volumetrik**

Setelah proses penyiraman berhenti, ukur volume air yang tertampung pada bejana masing-masing pohon ($X_i$) menggunakan silinder ukur bertingkat presisi $\pm 5\text{ mL}$.
**5. Perhitungan Matematis Nilai $CU$**

Hitung rata-rata volume air tertampung ($\bar{X}$) dan hitung nilai Koefisien Keseragaman Christiansen menggunakan persamaan matematis:
   $$CU = 100 \times \left(1 - \frac{\sum_{i=1}^{n} |X_i - \bar{X}|}{n \cdot \bar{X}}\right)$$
   di mana $n = 15$ adalah jumlah titik sampel. Kriteria lulus terpenuhi jika $CU \ge 85\%$ dan deviasi tiap titik terhadap target volume 10–15 L tidak melampaui $\pm 5\%$.
**6. Verifikasi Penetrasi Perakaran**

Tiga puluh menit pasca-penyiraman, lakukan pengeboran sampel tanah menggunakan bor tanah mini (*soil core auger*) sedalam 40 cm pada radius 60 cm dari pangkal batang. Amati batas pembasahan vertikal tanah dan pastikan tidak terdapat air yang menggenang di permukaan tanah lebih dari 30 menit.

#### 1.3.2 Prosedur Verifikasi Durasi Siklus dan Filtrasi Fisik (S-03, S-05)
**1. Verifikasi Waktu Operasi**

Stopwatch digital diaktifkan serentak saat tombol mulai (*start*) sistem ditekan pada titik awal kebun. Timer dihentikan tepat ketika pohon ke-500/600 selesai menerima kuota air yang ditentukan. Durasi total dicatat dalam satuan menit. Sistem dinyatakan lulus apabila waktu tempuh $\le 240\text{ menit}$ (4 jam).
**2. Verifikasi Filtrasi Saringan**

Pasang manometer diferensial pada sisi saluran masuk (*inlet*) dan keluaran (*outlet*) tabung saringan 120 mesh. Alirkan air sampel sungai Ciberes pada kapasitas debit puncak selama 2 jam kontinu. Ukur tekanan diferensial ($\Delta P$) dan lakukan pengujian laboratorium sederhana terhadap air keluaran menggunakan kertas saring analitik untuk memastikan tidak ada partikel padatan tersuspensi berdiameter $\ge 130\ \mu\text{m}$ yang lolos.

#### 1.3.3 Prosedur Verifikasi Kemandirian Daya dan Proteksi Lingkungan (S-06, S-07)
**1. Uji Otonomi Energi Beban Penuh**

Pastikan modul baterai terisi penuh (100% *State of Charge* / SoC). Putuskan sambungan panel surya/sumber pengisian eksternal untuk mensimulasikan kondisi cuaca mendung total. Operasikan seluruh beban pompa, katup solenoid, modul mikrokontroler, dan motor penggerak pada siklus kerja penuh.
**2. Pencatatan Karakteristik Listrik**

Hubungkan digital DC clamp meter dan data logger untuk merekam kurva penurunan tegangan baterai ($V$), konsumsi arus listrik ($I$), dan daya serap total ($P = V \times I$) setiap interval 10 menit. Sistem dinyatakan lulus jika sistem dapat terus beroperasi normal tanpa *undervoltage cutoff* selama minimal 8 jam kerja kontinu.
**3. Uji Ketahanan Semprot Air (IP65)**

Selungkup kotak kontrol yang memuat seluruh rangkaian elektronik ditutup rapat sesuai standar pengencangan sekrup pabrikan. Semprotkan air menggunakan nozzle berdiameter 6,3 mm dengan laju alir $12,5\text{ Liter/menit}$ dari jarak 2,5–3 meter ke seluruh sambungan, engsel, dan permukaan selungkup selama minimal 3 menit. Setelah penyemprotan, keringkan bagian luar selungkup, buka penutup, dan lakukan inspeksi visual mikroskopis. Syarat kelulusan: tidak boleh ada setetes pun air yang merembes ke bagian dalam papan sirkuit, dan instrumen tetap menyala normal saat diberi tegangan kerja.

#### 1.3.4 Prosedur Verifikasi Finansial, Efisiensi Biaya, dan Efisiensi Air (S-08, S-09, S-10, S-11)
**1. Audit Biaya Investasi (CAPEX)**

Seluruh kuitansi, faktur belanja komponen elektronik, pipa, aktuator, rangka mekanik, dan ongkos fabrikasi bengkel lokal diakumulasikan ke dalam dokumen *Bill of Materials* (BOM) komprehensif. Total biaya riil harus terbukti $\le \text{Rp } 18.000.000$.
**2. Pengujian Biaya Operasional Siklus (OPEX)**

Pada setiap kali pengujian siklus siram penuh, hitung konsumsi energi listrik/bahan bakar terpakai serta alokasi upah penjaga sistem. Biaya total operasional dibagi frekuensi penyiraman harus bernilai $\le \text{Rp } 50.000$ per kegiatan.
3. **Perhitungan Balik Modal (*Payback Period*):** Hitung selisih efisiensi tahunan terhadap sistem manual eksisting ($\Delta \text{OPEX} = \text{Rp } 48.700.000 - (\text{OPEX baru} \times 120\text{ siklus/tahun})$). Hitung durasi balik modal dengan rumus $PP = \frac{\text{CAPEX riil}}{\Delta \text{OPEX Tahunan}}$. Kriteria kelulusan tercapai apabila $PP \le 1,5\text{ tahun}$ (18 bulan).
**4. Verifikasi Efisiensi Aplikasi Air ($\eta_a$)**

Pasang flow meter air pada pipa masukan utama untuk mengukur volume total air yang disedot ($V_{\text{in}}$). Ukur total volume air yang tertampung di zona perakaran pohon sampel dikalikan total populasi pohon ($V_{\text{akar}}$). Hitung efisiensi aplikasi air dengan persamaan $\eta_a = \frac{V_{\text{akar}}}{V_{\text{in}}} \times 100\%$. Kriteria lulus jika $\eta_a \ge 80\%$.

#### 1.3.5 Prosedur Verifikasi Keterpakaian dan Pemeliharaan (S-13, S-14)
1. **Uji Keterpakaian Mitra (*Usability Test*):** Berikan panduan prosedur operasional standar (*SOP*) satu lembar bergambar kepada pekerja kebun mitra Ciberes. Berikan sesi demonstrasi dan pelatihan selama maksimal 30 menit. Mintalah pekerja menyalakan sistem, memilih mode siram, dan mematikan sistem secara mandiri tanpa bantuan tim pengembang. Catat waktu keberhasilan dan tingkat kekeliruan pekerja. Kriteria lulus: pekerja mampu mengeksekusi perintah dasar dengan sukses dalam waktu belajar $\le 30\text{ menit}$.
2. **Uji Waktu Pemeliharaan (*Maintenance Disassembly Test*):** Siapkan kotak peralatan standar berisi obeng plus-minus dan kunci pas. Lakukan simulasi pembersihan filter kotor: matikan katup, buka rumah filter, keluarkan elemen saringan 120 mesh, bersihkan kotoran dengan air mengalir, pasang kembali, dan nyalakan sistem. Catat durasi waktu menggunakan stopwatch. Kriteria lulus: seluruh tahapan perawatan tuntas dalam waktu $\le 20\text{ menit}$.

---

## 1.4 Kesimpulan

Dokumen CD-2 ini telah menetapkan kerangka batasan rekayasa (*engineering constraints*) dan spesifikasi kuantitatif (*engineering specifications*) yang terdefinisi secara presisi, terukur, dan memiliki pijakan ilmiah yang kokoh bagi perancangan sistem irigasi kebun jeruk limau mitra di Ciberes, Subang.

Rangkuman poin penting dokumen CD-2 meliputi:
**1. Dasar Penentuan Spesifikasi Multi-Pilar**

Perumusan spesifikasi tidak didasarkan pada asumsi subjektif, melainkan mengintegrasikan kebutuhan riil mitra kebun Ciberes (penurunan upah manual Rp400.000/kegiatan, keandalan pompa, suplai air teratur), regulasi pemerintah (Permen Pertanian No. 49/2014, SNI 7608:2010), standar teknik industri konsensus internasional (keseragaman air ASABE S398.1 $\ge 85\%$, proteksi lingkungan IEC 60529 IP65, keselamatan tegangan rendah SELV $\le 48\text{ V DC}$, otonomi surya IEC 62124), serta karakteristik agronomi tanaman jeruk limau (kebutuhan evapotranspirasi 10–15 L/pohon, kedalaman perakaran serabut aktif 20–40 cm, dan pencegahan busuk perakaran *Phytophthora*).
**2. Perumusan Spesifikasi Kuantitatif Multi-Aspek**

Ditetapkan 5 batasan mutlak (*hard constraints*) dan 14 butir spesifikasi kuantitatif komprehensif yang mencakup aspek teknis (akurasi dosis air $15\text{ L} \pm 5\%$, keseragaman $CU \ge 85\%$, durasi siram $\le 4\text{ jam}$, filtrasi 120 mesh, otonomi energi $\ge 8\text{ jam}$, rating IP65), aspek ekonomi (CAPEX $\le \text{Rp } 18.000.000$, OPEX $\le \text{Rp } 50.000$/siklus, payback period $\le 12 - 18\text{ bulan}$), aspek lingkungan (efisiensi aplikasi air $\ge 80\%$, bebas emisi lokal di area perakaran), serta aspek operasional mitra (waktu ajar operasi $\le 30\text{ menit}$, waktu perawatan $\le 20\text{ menit/bulan}$).
3. **Netralitas Solusi (*Solution-Agnostic*):** Spesifikasi dirumuskan secara fungsional tanpa bias atau penguncian dini pada satu opsi teknologi maupun merek komponen tertentu.
**4. Kesiapan Protokol Pengujian**

Seluruh spesifikasi telah dipetakan ke dalam matriks rencana pengujian verifikasi yang memuat metode uji baku, instrumen alat ukur terkalibrasi, prosedur pengukuran langkah demi langkah, dan kriteria kelulusan numerik yang objektif.
**5. Transisi Menuju Tahap CD-3**

Batasan dan spesifikasi kuantitatif dalam dokumen CD-2 ini secara formal menjadi tolok ukur acuan (*benchmarking criteria*) dan kriteria pembobotan (*decision matrix criteria*) dalam mengusulkan, menganalisis, dan memilih sekurang-kurangnya tiga alternatif konsep desain solusi pada dokumen rancangan solusi **CD-3**.

---

## Daftar Pustaka

[1] R. G. Allen, L. S. Pereira, D. Raes, dan M. Smith, *Crop Evapotranspiration: Guidelines for Computing Crop Water Requirements*, FAO Irrigation and Drainage Paper 56. Roma, Italia: Food and Agriculture Organization of the United Nations (FAO), 1998. Tersedia: https://www.fao.org/4/x0490e/x0490e00.htm

[2] ASABE Standards, *ANSI/ASAE S398.1: Procedure for Sprinkler Testing and Performance Reporting*, Standard ANSI/ASAE S398.1. St. Joseph, MI, AS: American Society of Agricultural and Biological Engineers, 2021. Tersedia: https://elibrary.asabe.org/abstract.asp?aid=41295

[3] ASABE Standards, *Design and Installation of Microirrigation Systems*, Standard ANSI/ASAE EP405.1. St. Joseph, MI, AS: American Society of Agricultural and Biological Engineers, 2019. Tersedia: https://elibrary.asabe.org/abstract.asp?aid=32022

[4] International Electrotechnical Commission, *Degrees of Protection Provided by Enclosures (IP Code)*, Standard IEC 60529:1989+AMD1:1999+AMD2:2013 CSV. Jenewa, Swiss: IEC, 2013. Tersedia: https://webstore.iec.ch/publication/2452

[5] Badan Standardisasi Nasional, *Derajat Proteksi yang Diberikan oleh Selungkup (Kode IP)*, SNI IEC 60529:2014. Jakarta, Indonesia: BSN, 2014. Tersedia: https://pesta.bsn.go.id/produk/detail/9726-sniiec605292014

[6] Pemerintah Republik Indonesia, *Peraturan Pemerintah Republik Indonesia Nomor 20 Tahun 2006 tentang Irigasi*, Lembaran Negara Republik Indonesia Tahun 2006 Nomor 46. Jakarta, Indonesia: Sekretariat Negara, 2006. Tersedia: https://peraturan.bpk.go.id/Details/48943/pp-no-20-tahun-2006

[7] International Organization for Standardization, *Agricultural irrigation equipment — Emitters and emitting pipe — Specification and test methods*, Standard ISO 9261:2004. Jenewa, Swiss: ISO, 2004. Tersedia: https://www.iso.org/standard/38072.html

[8] International Electrotechnical Commission, *Photovoltaic Stand-Alone Systems: Design Verification*, Standard IEC 62124:2004. Jenewa, Swiss: IEC, 2004. Tersedia: https://webstore.iec.ch/publication/6504

[9] International Electrotechnical Commission, *Low-voltage electrical installations - Part 4-41: Protection for safety - Protection against electric shock*, Standard IEC 60364-4-41:2005+AMD1:2017 CSV. Jenewa, Swiss: IEC, 2017. Tersedia: https://webstore.iec.ch/publication/60074

[10] IEEE Standards Association, *IEEE Standard for a Smart Transducer Interface for Sensors and Actuators - Mixed-Mode Communication Protocols and Transducer Electronic Data Sheet (TEDS) Formats*, IEEE Std 1451.4-2004, hlm. 1–439, 2004, doi: 10.1109/IEEESTD.2004.95745.

[11] P. Panigrahi dan A. K. Srivastava, “Water and nutrient management effects on water use and yield of drip irrigated citrus in vertisol under a sub-humid region,” *Journal of Integrative Agriculture*, vol. 16, no. 5, hlm. 1184–1194, 2017, doi: 10.1016/S2095-3119(16)61500-9.

[12] R. S. Ayers dan D. W. Westcot, *Water Quality for Agriculture*, FAO Irrigation and Drainage Paper 29 Rev. 1. Roma, Italia: Food and Agriculture Organization of the United Nations (FAO), 1985. Tersedia: https://www.fao.org/4/t0234e/t0234e00.htm

[13] S. Bounoua, B. Molle, H. Boyer, dan F. L. Bentouba, “Understanding physical clogging in drip irrigation: In situ, in-lab and numerical approaches,” *Irrigation Science*, vol. 34, no. 4, hlm. 327–342, 2016, doi: 10.1007/s00271-016-0506-8.

[14] Y. Shen, J. Puig-Bargués, M. Li, Y. Xiao, Q. Li, dan Y. Li, “Physical, chemical and biological emitter clogging behaviors in drip irrigation systems using high-sediment loaded water,” *Agricultural Water Management*, vol. 270, art. 107738, 2022, doi: 10.1016/j.agwat.2022.107738.

[15] R. Budiarto, R. Poerwanto, E. Santosa, dan D. Efendi, “The Potentials of Limau (Citrus amblycarpa Hassk. Ochse) as A Functional Food and Ornamental Mini Tree Based on Metabolomic and Morphological Approaches,” *Journal of Tropical Crop Science*, vol. 4, no. 2, hlm. 49–57, 2017, doi: 10.29244/jtcs.4.2.49-57.

[16] D. M. Kadyampakeni, K. T. Morgan, P. Nkedi-Kizza, dkk., *2023–2024 Florida Citrus Production Guide: Irrigation Management of Citrus Trees*, University of Florida IFAS Extension, Publ. CG093, 2023, doi: 10.32473/edis-cg093-2023.

[17] J. H. Graham dan L. W. Timmer, *Phytophthora Diseases of Citrus*, University of Florida IFAS Extension, Publ. SL127/CH087, 2020. Tersedia: https://edis.ifas.ufl.edu/publication/CH087

[18] A. G. Smajstrla, B. J. Boman, D. Z. Haman, D. J. Pitts, dan F. S. Zazueta, *Field Evaluation of Microirrigation Water Application Uniformity*, University of Florida IFAS Extension, Publ. BUL265/AE094, 1997, doi: 10.32473/edis-ae094-1997.

[19] T. Obreza, M. Zekri, dan S. H. Futch, *Nutrition of Florida Citrus Trees, 3rd Edition: Chapter 3. General Soil Fertility and Citrus Tree Nutrition*, University of Florida IFAS Extension, Publ. SL457/SS670, 2020, doi: 10.32473/edis-ss670-2020.

[20] G. Li, X. Li, dan Q. Zeng, “Development of automatic irrigation and soil moisture monitoring system based on solar energy in citrus orchard,” *Transactions of the Chinese Society of Agricultural Engineering*, vol. 28, no. 12, hlm. 146–152, 2012, doi: 10.3969/j.issn.1002-6819.2012.12.024.

[21] J. M. Domínguez-Niño, H. R. Bogena, J. A. Huisman, B. Schilling, dan J. Casadesús, “On the accuracy of factory-calibrated low-cost soil water content sensors,” *Sensors*, vol. 19, no. 14, art. 3101, 2019, doi: 10.3390/s19143101.

[22] Mitra dan Tim Proyek, “Transkrip Wawancara Kebun Jeruk Limau Audio 1 Ciberes Subang,” dokumentasi primer lapangan tidak diterbitkan, dihimpun Oktober 2026.

---

## Lampiran: Ringkasan Transkrip Wawancara Mitra Lapangan (Audio 1 Ciberes)

*Berdasarkan rekaman Audio 1 wawancara langsung bersama pengelola kebun jeruk limau di Desa Ciberes, Kecamatan Patokbeusi, Kabupaten Subang, Jawa Barat:*

**Populasi Tanaman**

Lahan ditanami pohon jeruk limau dengan estimasi populasi sekitar 500 hingga 600 pohon, dengan rata-rata tinggi tajuk pohon saat ini berkisar ±1 meter.
**Topografi dan Infrastruktur Parit**

Lahan memiliki 3 lajur parit tanah memanjang dengan panjang masing-masing sekitar 100 meter dan terdapat parit melintang penghubung. Parit dibuat dengan biaya hemat untuk mendekatkan air ke barisan pohon.
**Sumber Air dan Pompa**

Air diambil dari aliran sungai/saluran irigasi yang berjarak sekitar 20,54 meter dari batas kebun. Pompa yang digunakan adalah pompa mesin bensin Alkon (Pertalite). Mitra sempat mencoba memodifikasi bahan bakar menggunakan gas LPG 3 kg untuk menghemat biaya, namun dihentikan karena mesin mengalami panas berlebih (*overheat*).
**Ketiadaan Jaringan Listrik PLN**

Lokasi kebun berada di area sawah/kebun terbuka yang belum terjangkau instalasi tiang listrik tegangan rendah PLN.
**Penyiraman Eksisting dan Tenaga Kerja**

Air sungai disedot ke dalam parit, kemudian disiramkan ke tanaman secara manual oleh 4 orang pekerja harian lepas menggunakan timba ember kecil.
**Biaya Tenaga Kerja**

Upah pekerja adalah Rp100.000 per orang per hari kerja. Total pengeluaran per satu kali kegiatan penyiraman adalah Rp400.000 (4 orang × Rp100.000). Penyiraman dilakukan rutin rata-rata 3 hari sekali pada musim kemarau.
**Dosis Air Menurut Kebiasaan Petani**

Petani memperkirakan rata-rata satu pohon menerima sekitar 10 hingga 15 Liter air per kali siram, namun volume aktual per pohon tidak pernah ditakar secara presisi.
**Harapan Mitra**

Pengelola menginginkan adanya alat atau sistem otomatis/mekanis yang mampu menggantikan pekerjaan guyur manual tersebut agar pengeluaran upah tenaga kerja dapat dipangkas drastis, serta pasokan air ke pohon menjadi lebih teratur dan terjamin.
