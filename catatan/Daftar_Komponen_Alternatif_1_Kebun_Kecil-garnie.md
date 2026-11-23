# Daftar Komponen & Cara Kerja Solusi Alternatif 1 (Kebun Kecil)

**Target:** Zona Uji 1 (**4 Pohon Sampel**, keliling `10,30 m`, jarak ke sumur baru `12,27–16,20 m`)  
**Sumber Air & Listrik:** Sumur baru dalam lahan + Listrik PLN rumah (dikonversi ke **12V DC aman sentuh / SELV**)

---

## 1. Cara Kerja Singkat
1. **Cek Tanah:** Sensor tanah di masing-masing dari 4 pohon membaca kondisi lembap atau kering. Jika tanah masih basah (misal habis hujan), penyiraman otomatis dilewati.
2. **Pompa & Saring:** Saat jadwal tiba dan tanah kering, mikrokontroler **ESP32** membuka katup dan menyalakan pompa listrik **12V DC** untuk menyedot air dari sumur baru melewati saringan (*disc filter 120 mesh*) agar pasir tidak menyumbat.
3. **Alirkan & Bagi Rata:** Air mengalir lewat pipa/selang PE `16 mm` menuju tengah Zona Uji 1, lalu dibagi rata ke **2 `PC Dripper` per pohon** (total 8 penetes) agar keluarnya seragam di keempat pohon.
4. **Ukur & Berhenti Otomatis:** **`Flow meter`** di pipa utama menghitung total liter air yang keluar. Begitu mencapai target (misal `60 Liter` untuk `4 pohon × 15 L`), ESP32 otomatis mematikan pompa dan menutup katup.
5. **Pengaman:** Sensor tekanan membaca kondisi abnormal—jika air sumur habis (*dry-run*) pompa langsung dimatikan, dan jika saringan kotor lampu indikator menyala untuk mengingatkan bilas filter.

---

## 2. Daftar Komponen (Untuk 1 Zona = 4 Pohon Sampel)

### A. Bagian Air, Pompa, & Pipa
| No | Komponen | Jumlah | Fungsi Singkat |
|---:|---|:---:|---|
| 1 | Pompa Air DC 12V (*Self-Priming* / Celup) | 1 unit | Menyedot air dari sumur baru ke pipa *(jenis disesuaikan kedalaman air sumur)* |
| 2 | Saringan Hisap (*Foot Valve* + Keranjang) | 1 unit | Menahan kotoran kasar/pasir di ujung pipa dalam sumur |
| 3 | *Disc Filter* 120 Mesh (3/4" atau 1") + Keran Bilas | 1 unit | Menyaring lumpur/pasir halus agar *dripper* tidak mampet |
| 4 | Katup Listrik (*Motorized Ball Valve* 12V DC) | 1 unit | Keran otomatis yang dibuka-tutup oleh ESP32 |
| 5 | Pipa/Selang PE 16 mm | ±35–40 m | Jalur utama dari sumur (`~16 m`), keliling zona (`~11 m`), + cadangan belokan |
| 6 | *PC Dripper* 8 L/jam (disarankan tipe *Anti-Drip/CNL*) | 8 buah | Meneteskan air dengan debit sama rata (2 buah per pohon) |
| 7 | Selang Mikro 4/7 mm + Nepel/Tusuk + Penyangga | 1 set | Menghubungkan pipa PE 16 mm ke posisi akar di bawah tepi daun |
| 8 | Sambungan *Tee*, *Elbow*, Klem, & Keran *End-Flush* | 1 set | Pembagi aliran simetris di zona & keran kuras endapan di ujung pipa |

### B. Bagian Listrik PLN Aman (SELV) & Pelindung
| No | Komponen | Jumlah | Fungsi Singkat |
|---:|---|:---:|---|
| 9 | Adaptor / PSU 220V AC ke 12V DC (10A–15A) | 1 unit | Mengubah listrik PLN menjadi tegangan rendah 12V DC yang aman |
| 10 | Boks Panel Kedap Air (IP65) + *Cable Gland* | 1 unit | Melindungi PSU, ESP32, dan kabel dari hujan, lumpur, & serangga |
| 11 | Sekring (*Fuse*), Sakelar Fisik, & 3 Lampu LED | 1 set | Pengaman arus pendek, tombol manual 1 sentuhan, & indikator status |
| 12 | Kabel Listrik NYAF/NYY (jalur PLN ke boks & pompa) | ±20–25 m | Menghubungkan daya secara aman ke boks kontrol & pompa |

### C. Bagian Kendali & Sensor
| No | Komponen | Jumlah | Fungsi Singkat |
|---:|---|:---:|---|
| 13 | Mikrokontroler ESP32 | 1 unit | Otak pengatur jadwal, pembaca sensor, dan penggerak pompa/katup |
| 14 | Modul Jam RTC DS3231 | 1 unit | Penjaga waktu/jadwal siram agar tetap akurat meski listrik mati |
| 15 | *Flow Meter* Air (YF-S201 atau sejenis) | 1 unit | Menghitung jumlah liter air yang keluar di pipa utama |
| 16 | Sensor Tekanan Air (0–5 bar) | 1 unit | Mendeteksi air sumur habis (*dry-run*), pipa bocor, & filter mampet |
| 17 | Sensor Kelembapan Tanah (*Capacitive v1.2* + mod RC/MOSFET) | 4 unit | Membaca kelembapan tanah di masing-masing 4 pohon sampel |
| 18 | Modul Driver / *Relay* 12V + Step-Down 12V ke 5V/3,3V | 1 set | Sakelar elektronik penggerak pompa/katup & penurun tegangan untuk ESP32 |
