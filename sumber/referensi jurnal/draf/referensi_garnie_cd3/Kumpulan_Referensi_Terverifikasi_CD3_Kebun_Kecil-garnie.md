# Kumpulan Referensi Terverifikasi untuk Dokumen CD-3 Baru (`Kebun Kecil` — PLN, IoT 4G, & Agronomi Jeruk Limau)

**Tanggal Kompilasi:** 25 November 2026  
**Sumber Gabungan:**
1. Pustaka lama relevan yang sudah terverifikasi *full-text* di [`sumber/referensi jurnal/`](../sumber/referensi%20jurnal/pustaka_cd3/CATALOG_REFERENSI_SOLUSI_CD3.md) *(selain artikel PLTS murni)*.
2. Hasil Deep Research #1 ([Hasil_Deep_Research_Referensi_CD3_Kebun_Kecil-garnie.md](Hasil_Deep_Research_Referensi_CD3_Kebun_Kecil-garnie.md)) — *IoT 4G, Adaptor 12V, Filtrasi, SELV/RCD IEC 60364, & Pembanding Robot*.
3. Hasil Deep Research #2 ([Hasil_Deep_Research_Agronomi_Jeruk_Limau_CD3-garnie.md](Hasil_Deep_Research_Agronomi_Jeruk_Limau_CD3-garnie.md)) — *Agronomi Citrus amblycarpa, Balitjestro, Perakaran/Phytophthora, & Kalibrasi Sensor v1.2*.

*(Catatan Verifikasi: Seluruh DOI jurnal internasional telah diperiksa ulang melalui **Crossref API / OpenAlex API / NCBI**. Jika sumber pedoman nasional/pratinjau belum mencantumkan DOI, tautan PDF langsungnya disertakan terpisah agar tetap transparan saat menyusun Daftar Pustaka CD-3).*

---

## Klaster A — Pustaka Inti Repositori yang Tetap Dipakai (`pustaka_cd1/` & `pustaka_cd3/`)

| Kode | Penulis, Tahun, & Judul Singkat | DOI / Berkas Lokal | Peran di CD-3 Baru (`Kebun Kecil`) |
|---|---|---|---|
| **R-01** | **Dafonte et al. (2024)**, *Sensors* — Proximal Low-Cost Sensors + ESP32 | `10.3390/s24248104` (`Z-01`) | Filter ADC `0,1 µF`, rata-rata 10×, & *power-gating* MOSFET sensor |
| **R-02** | **Domínguez-Niño et al. (2019)**, *Sensors* — Local Soil Sensor Calibration | `10.3390/s19143101` (`Z-02`) | Bukti kalibrasi pabrik galat tinggi (`RMSE 5,33%`) vs lokal (`RMSE 1,03–1,37%`) |
| **R-03** | **Zakaria et al. (2026)**, *Sensors* — Soil-Specific Calibration Capacitive | `10.3390/s26133979` (`Z-11`) | Modifikasi *pull-down* `1 MΩ`, LDO `3,3 V` terpisah, pelapisan silikon |
| **R-04** | **Meriç (2025)**, *Sci. Rep.* — WSN Drip Irrigation & Latching Valve | `10.1038/s41598-025-97303-w` (`Z-04`) | H-bridge + katup motor/latching, meter air 1 L/pulsa, transduser tekanan |
| **R-05** | **García et al. (2020)**, *Sensors* — IoT-Based Smart Irrigation Review | `10.3390/s20041042` (`Z-05`) | Arsitektur 4 lapis IoT, evaluasi sensor aliran (`YF-S` / Hall), anti-korosi probe |
| **R-06** | **Abdelmoneim et al. (2025)**, *Sensors* — Soil Moisture vs Weather Drip | `10.3390/s25051568` (`Z-06`) | Posisi sensor `15 cm` di zona akar `30 cm`, potensi hemat air `15–20%` |
| **R-07** | **Farag et al. (2025)**, *Sci. Rep.* — Citrus Tree Productivity in Clayey Soils | `10.1038/s41598-025-19575-6` (`Z-15`) | Irigasi tetes jeruk pada tanah liat (`16 mm`, hemat air `31,58%`, WUE `+58,87%`) |
| **R-08** | **Abbas et al. (2024)**, *HardwareX* — ASCD Irrigation Controller | `10.1016/j.ohx.2024.e00523` (`Z-13`) | Ambang hisapan tanah jeruk (`61–80 kPa`), proteksi IP64, bukti erosi probe resistif |
| **R-09** | **Lavanholi et al. (2018)**, *Sci. World J.* — Dripper Clogging Solid Particles | `10.1155/2018/7697458` (`Z-16`) | Batas kecepatan endap `0,6 m/s` (*end-flush*), larangan pompa besi cor |
| **R-10** | **Zong et al. (2019)**, *PLoS ONE* — Self-Cleaning Screen Filters 124 µm | `10.1371/journal.pone.0226354` (`Z-09`) | Acuan saringan `~120 mesh` & pemicu bilas filter pada `ΔP = 70 kPa` |
| **R-11** | **Alex-Tronix (1998)**, *US DOE OSTI* — Irrigation Valve Energy Saver | `DE-FG01-97EE15698` (`Z-17`) | Korosi galvanik koil DC kontinu vs pulsa *latching* / MBV hemat energi |
| **R-12** | **Allen et al. (1998)**, *FAO Paper 56* — Crop Evapotranspiration | `pustaka_cd1/` | Metode standar perhitungan kebutuhan air tanaman ($ET_c$) |

---

## Klaster B — Referensi Baru Solusi Pilihan, IoT 4G LTE, PLN SELV, & Pembanding Robot *(Terverifikasi Crossref/OpenAlex/NCBI)*

| Kode | Penulis, Tahun, & Jurnal | DOI Resmi / Standar | Peran di CD-3 Baru |
|---|---|---|---|
| **N-01** | **Pereira, Chaari, & Daroge (2023)**, *IoT* 4(3):221–243 | `10.3390/iot4030012` | Desain **ESP32 + adaptor `12 V DC` + *step-down* `5 V` + *flow sensor* Hall** |
| **N-02** | *AgriEngineering* (2025), Vol. 7(11), art. 358 | `10.3390/agriengineering7110358` | Antarmuka **ESP32-S3 + modem 4G LTE `SIM7670G`** (UART `115.200 bps`, *level shifter* `TXB0108`) + MQTT ke database |
| **N-03** | **Sharma, Mishra, & Yadav (2026)**, *Sci. Rep.* (`PMC13043767`) | `10.1038/s41598-026-37287-3` | Mekanisme pencatatan lokal `microSD` via SPI + integrasi *cloud* |
| **N-04** | **Borankulova et al. (2025)**, *Sensors* 25(17):5564 | `10.3390/s25175564` | Arsitektur pemantauan air pertanian berbasis 4G LTE + SD card |
| **N-05** | **Ghanghas, Sihag, & Dhanger (2026)**, *Frontiers in Water* | `10.3389/frwa.2026.1973897` | Benchmark akurasi kendali katup MQTT (`98,1%` pada zaitun), hemat air `32%`, & risiko *sensor drift* |
| **N-06** | **Abdelmoneim et al. (2025)**, *Sensors* 25(2):343 | `10.3390/s25020343` | Linearitas respons sensor kapasitif ($R^2 = 0,967$) |
| **N-07** | **Salah et al. (2026)**, *Electronics* 15(20):4831 | `10.3390/electronics15204831` | Konstruksi PCB anti-korosi sensor *Capacitive* pada ESP32 |
| **N-08** | **Ghodgaonkar et al. (2026)**, *Water* 18(12):1462 | `10.3390/w18121462` | Uji sumbatan *PC dripper* berdiafragma di pipa `16 mm` (tekanan acuan `15 psi`) |
| **N-09** | **Ghonimy et al. (2026)**, *Water* 18(2):244 | `10.3390/w18020244` | Kriteria klasifikasi eksponen tekanan-debit *PC dripper* ($0 \le x \le 0,1$) |
| **N-10** | **Solé-Torres et al. (2019)**, *Water* 11(7):1346 | `10.3390/w11071346` | Pemantauan keseragaman distribusi pipa `16 mm` memakai meter air & transduser tekanan |
| **N-11** | **Wei et al. (2023)**, *Water* 15(12):2251 | `10.3390/w15122251` | Bukti tekanan terlalu rendah (`30–40 kPa`) memperburuk sumbatan |
| **N-12** | **IEC 60364-7-705:2006 & HD 60364-7-705:2007** (+ `IEC 60364-4-41`, `IEC 60529`) | Standar Resmi IEC / CENELEC | Wajib **`RCD ≤ 300 mA`** jika listrik rumah terhubung ke lahan kebun (`705.20`, `705.411`) + isolasi **`SELV 12 V DC`** & boks **`IP65`** |
| **N-13** | **Justin London (2025)**, *arXiv* (`arXiv:2508.08607`) | `10.48550/arXiv.2508.08607` | Pembanding **Matriks Scoring Alt 2 (Robot):** tangki `36 L` hanya cukup `~2–3 pohon` jeruk limau sebelum isi ulang (`20–30` rit untuk `72–73` pohon) |
| **N-14** | **Elkaoud et al. (2025)**, *Eng* 6(7):138 *(sudah ada `P-06`)* + **Xia (2023)**, **Li (2025)**, **Jia (2023)**, **Gu (2026)**, **Zhang (2026)**, **Wu (2025)**, **CN115804333A** | `10.3390/eng6070138`, dll. *(ada di `pustaka_cd3/`)* | Pembanding **Matriks Scoring Alt 2/3 (Robot/Sprinkler):** daya motor `4×350 W`, selip tanah basah `10%`, sempit di lahan `471 m²` |

---

## Klaster C — Referensi Agronomi *Citrus × amblycarpa*, Lembaga Resmi (Kew/Kementan/UF-IFAS), & Kalibrasi Sensor v1.2

| Kode | Penulis, Tahun, & Sumber | DOI / Tautan Resmi | Peran di CD-3 Baru |
|---|---|---|---|
| **F-01** | **Royal Botanic Gardens, Kew (POWO) / IPNI / UPOV (`CITRU_AMB`)** | `urn:lsid:ipni.org:names:771842-1` | **Otoritas taksonomi botani dunia:** tata nama sah *Citrus × amblycarpa* (Hassk.) Ochse, asli Jawa, habitus perdu/pohon kecil |
| **F-02** | **Keputusan Menteri Pertanian RI (`SK No. 150/Kpts/SR.120/D.2.7/10/2015`)** — **Balitjestro / BSIP Kementan RI** | Varietas Unggul **Sari Agrihorti** (`kikomunal-indonesia.dgip.go.id`) | **Otoritas hukum & agronomi nasional:** deskripsi resmi buah jeruk limau/sambal (`3,0–3,8 cm`, `18–28,6 g`) & produktivitas resmi (`241–250 buah` / `6,25–7,25 kg/pohon/tahun` umur 3 thn) |
| **F-03** | **Budiarto, Poerwanto, Santosa, & Efendi (2017)** — **IPB University**, *J. Trop. Crop Sci.* 4(2):49–57 *(PDF Terunduh)* | `10.29244/jtcs.4.2.49-57` (`F-05_IPB_JTCS_2017...pdf`) | Morfologi spesifik *C. amblycarpa* Jawa Barat (tajuk ringkas, percabangan jarang, daun unifoliate aromatik) |
| **F-04** | **Kadyampakeni, Morgan, & Strauss (2022)** — **UF/IFAS Extension**, *Florida Citrus Production Guide: Root Health Management* (`CG094`) & *Phytophthora* (`CG009`) | `10.32473/edis-cg094-2022` & `10.32473/edis-cg009-2022` *(+ `pustaka_cd1/`)* | **Otoritas sitrikultur internasional:** zona akar serabut aktif `0–30 cm`, batas genangan, & pencegahan *Phytophthora* |
| **A-01** | **Putri T. J. Buih & R. Susandarini (2023)**, *Al-Kauniyah: Jurnal Biologi* 16(2):255–268 *(PDF Terunduh)* | `10.15408/kauniyah.v16i2.22920` | Karakterisasi morfologi komparatif ***Citrus × amblycarpa*** → dasar radius *dripper* ringkas (`15–50 cm`) |
| **A-02** | **Buletin Anatomi dan Fisiologi UNDIP** (Vol. 9 No. 2, Agu 2024, pp. 111–120) *(PDF Terunduh)* | `ejournal2.undip.ac.id/index.php/baf/article/download/20943/pdf` | Sifat poliembrioni **`27,85%`** (*C. × amblycarpa*) → bukti ilmiah variasi genetik bibit asal biji |
| **A-03** | *Journal of Innovation and Research in Agriculture* 2(1) (2023) *(PDF Terunduh)* | `A-03-ANALISIS_PENDAPATAN...pdf` | Produktivitas usahatani *C. amblycarpa* di Majalengka **`7,84 ton/ha`** (`~5,06–5,13 kg/pohon` proporsional di `471 m²`) |
| **A-04** | **Sutopo et al. / Balitbangtan (2021)**, *Teknologi Produksi Jeruk* (IPB Press) | ISBN `978-623-256-784-9` | Syarat tumbuh resmi Balitbangtan (`0–400 m dpl`, suhu tanah `22–27 °C`, `pH 5,5–6,5`, bahan kasar `< 15%`), larangan bibit akar *coiled* |
| **A-05** | **Agus Sugiyatno et al. / Balitjestro (2021)**, *Teknologi Bujangseta* (`JPFP Unila 2025`, *PDF Terunduh*) | `jurnal.fp.unila.ac.id/index.php/JPFP` | Pemangkasan pucuk/cabang dalam + pemupukan bertahap untuk `Sampel 3 & 4` |
| **A-05b** | **Farida Yulianti**, **Disertasi Doktor Univ. Brawijaya** *(PDF Terunduh)* | `repository.ub.ac.id/192546/` | Riset tingkat doktoral mengenai kompatibilitas batang bawah & mutu buah jeruk |
| **A-05f** | **Devy, N. F. et al. (2013)**, *Jurnal Hortikultura* 23(1):21–27 (**Balitbangtan Kementan RI**, *PDF Terunduh*) | `media.neliti.com` (`A-05f`) | Perbanyakan & sambung batang bawah jeruk resmi Balitbangtan |
| **A-06** | **Rivera-Hernández, Garruña, & Andrade (2025)**, *Horticulturae* 11(12):1472 *(PDF Terunduh)* | `10.3390/horticulturae11121472` | Ambang SMT **`−0,035 MPa`** optimal vs cekaman `−0,085 MPa` (`4` pohon/perlakuan pada jeruk asam) |
| **A-07** | **Meshram et al. (2025)**, *Frontiers in Horticulture* *(PDF Terunduh)* | `10.3389/fhort.2025.1552283` | Dosis tetes jeruk berbuah muda **`6 L` vs `12 L/pohon/hari`**, rumus $IT = ET_{NM}/DC$, & `55–65% FC` |
| **A-08** | **Bagherian & Hajieghrari (2026)**, *Phytopathologia Mediterranea* 65(2):309–317 *(PDF Terunduh)* | `10.36253/phyto-17259` | Bukti pengendalian *waterlogging* menurunkan penyakit akar *Phytophthora* secara signifikan |
| **A-09** | **Sravani, Singh, & Bakshi (2020)**, *J. Pharmacogn. Phytochem.* 9(5):2557–2560 *(PDF Terunduh)* | `10.22271/phyto.2020.v9.i5aj.12726` | Efisiensi irigasi tetes jeruk (`+40,46%` hasil, hemat air `55%` vs genangan) |
| **A-11** | **Cabia et al. (2025)**, *Annals of Tropical Research* 47(2):90–105 *(PDF Terunduh)* | `10.32945/atr4727.2025` | Strategi sampling **`3 dtk`** & log **`10 mnt`** pada **`Capacitive v1.2` (`FA3003-1`)** + kalibrasi per unit sensor |
| **A-12** | **Kumar et al. (2025)**, *CABI Agric. Biosci.* *(PDF Terunduh)* | `10.1079/ab.2025.0025` | Bukti wajib kalibrasi non-linear sensor kapasitif (tanpa kalibrasi `RMSE 9,43–13,44` → setelah kalibrasi `0,60–1,06`) |
| **A-13** | **Duarte et al. (2021)**, *DYNA* 88(219):190–196 *(PDF Terunduh)* | `10.15446/dyna.v88n219.94121` | Kalibrasi `Capacitive v1.2` pada tanah liat merah *Red Oxisol* ($\rho_{bd}=1,2\text{ Mg/m}^3$), model hiperbolik $y=1/(a+bx)$ ($R^2=0,96$, `RMSE 0,019`) |
| **A-14** | **Mahmud et al. (2026)**, *Sensors* 26(9):2692 *(PDF Terunduh)* | `10.3390/s26092692` | Pelapisan pelindung *Capacitive* pada kondisi tanah jenuh & pemantauan multi-sensor |

*(Catatan pembersihan: Sitasi lemah/kurang relevan seperti Bab II tugas akhir mahasiswa `Polsri`, artikel pangan mayones `FoodTech`, ekstrak kulit `Sintesa`, dan jurnal non-Q1/Q2 `IJFET` telah dihapus dari folder `pdf/` agar seluruh daftar pustaka bertumpu pada lembaga resmi & jurnal terakreditasi/bereputasi.)*

---

## Catatan Desain Kritis yang Wajib Diperhatikan Saat Masuk Penulisan CD-3
1. **Diferensiasi Dosis (`1,5–2 L` vs `5–6 L` vs `10–12 L/hari`):** Karena `Sampel 1 (46 cm)` tidak boleh disiram `10–12 L/hari` seperti `Sampel 3 & 4 (210–250 cm)`, sistem di **CD-3** perlu menggunakan **pemisahan kontrol katup sub-zona / *solenoid* kecil per sampel** atau **pemilihan debit *PC Dripper* berbeda** (misal `Sampel 1` memakai `1–2 L/jam` sedangkan `Sampel 3–4` memakai `2× 4–8 L/jam`), bukan hanya 1 katup terbuka durasi sama untuk keempat pohon!
2. **Jangan Campur PDF Tidak Terverifikasi ke Daftar Pustaka:** Pastikan saat menulis Bab Daftar Pustaka nanti, hanya entri yang URL/DOI-nya terverifikasi di atas (dan bila mengutip pedoman seperti `2673-4591/160/1/60` atau `IJFET`, verifikasi halaman aslinya terlebih dahulu atau gunakan sumber terverifikasi dari tabel ini).
