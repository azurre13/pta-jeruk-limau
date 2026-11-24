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

## 2. Daftar Komponen & Estimasi Harga (Untuk 1 Zona = 4 Pohon Sampel)

*(Catatan: Angka di bawah adalah perkiraan awal harga pasar komponen di Indonesia; harga pasti disesuaikan saat pembelian dan pengukuran kedalaman sumur).*

### A. Bagian Air, Pompa, & Pipa
| No | Komponen | Jumlah | Estimasi Satuan | Subtotal (Rp) | Fungsi Singkat |
|---:|---|:---:|:---:|:---:|---|
| 1 | Pompa Air DC 12V (*Self-Priming* / Celup) | 1 unit | 240.000 | 240.000 | Menyedot air dari sumur baru *(disesuaikan kedalaman sumur)* |
| 2 | Saringan Hisap (*Foot Valve* + Keranjang) | 1 unit | 45.000 | 45.000 | Menahan kotoran kasar/pasir di ujung pipa dalam sumur |
| 3 | *Disc Filter* 120 Mesh (3/4" atau 1") + Keran Bilas | 1 unit | 145.000 | 145.000 | Menyaring lumpur/pasir halus agar *dripper* tidak mampet |
| 4 | Katup Listrik (*Motorized Ball Valve* 12V DC) | 1 unit | 165.000 | 165.000 | Keran otomatis yang dibuka-tutup oleh ESP32 |
| 5 | Pipa/Selang PE 16 mm | 40 m | 4.000 | 160.000 | Jalur utama dari sumur (`~16 m`), keliling zona (`~11 m`), + cadangan |
| 6 | *PC Dripper* 8 L/jam (tipe *Anti-Drip/CNL*) | 8 buah | 5.000 | 40.000 | Meneteskan air dengan debit sama rata (2 buah per pohon) |
| 7 | Selang Mikro 4/7 mm + Nepel/Tusuk + Penyangga | 1 set | 60.000 | 60.000 | Menghubungkan pipa PE 16 mm ke posisi akar di bawah tepi daun |
| 8 | Sambungan *Tee*, *Elbow*, Klem, & Keran *End-Flush* | 1 set | 80.000 | 80.000 | Pembagi aliran simetris di zona & keran kuras endapan ujung pipa |
| | **Subtotal Bagian A** | | | **935.000** | |

### B. Bagian Listrik PLN Aman (SELV) & Pelindung
| No | Komponen | Jumlah | Estimasi Satuan | Subtotal (Rp) | Fungsi Singkat |
|---:|---|:---:|:---:|:---:|---|
| 9 | Adaptor / PSU 220V AC ke 12V DC (10A–15A) | 1 unit | 135.000 | 135.000 | Mengubah listrik PLN menjadi tegangan rendah 12V DC yang aman |
| 10 | Boks Panel Kedap Air (IP65) + *Cable Gland* | 1 unit | 165.000 | 165.000 | Melindungi PSU, ESP32, dan kabel dari hujan, lumpur, & serangga |
| 11 | Sekring (*Fuse*), Sakelar Fisik, & 3 Lampu LED | 1 set | 55.000 | 55.000 | Pengaman arus pendek, tombol manual 1 sentuhan, & indikator status |
| 12 | Kabel Listrik NYAF/NYY (jalur PLN ke boks & pompa) | 25 m | 7.000 | 175.000 | Menghubungkan daya secara aman ke boks kontrol & pompa |
| | **Subtotal Bagian B** | | | **530.000** | |

### C. Bagian Kendali & Sensor
| No | Komponen | Jumlah | Estimasi Satuan | Subtotal (Rp) | Fungsi Singkat |
|---:|---|:---:|:---:|:---:|---|
| 13 | Mikrokontroler ESP32 | 1 unit | 75.000 | 75.000 | Otak pengatur jadwal, pembaca sensor, dan penggerak pompa/katup |
| 14 | Modul Jam RTC DS3231 | 1 unit | 35.000 | 35.000 | Penjaga waktu/jadwal siram agar tetap akurat meski listrik mati |
| 15 | *Flow Meter* Air (YF-S201 atau sejenis) | 1 unit | 45.000 | 45.000 | Menghitung jumlah liter air yang keluar di pipa utama |
| 16 | Sensor Tekanan Air (0–5 bar) | 1 unit | 135.000 | 135.000 | Mendeteksi air sumur habis (*dry-run*), pipa bocor, & filter mampet |
| 17 | Sensor Kelembapan Tanah (*Capacitive v1.2* + mod RC/MOSFET) | 4 unit | 35.000 | 140.000 | Membaca kelembapan tanah di masing-masing 4 pohon sampel |
| 18 | Modul Driver / *Relay* 12V + Step-Down 12V ke 5V/3,3V | 1 set | 65.000 | 65.000 | Sakelar elektronik penggerak pompa/katup & penurun tegangan ESP32 |
| | **Subtotal Bagian C** | | | **495.000** | |

---

## 3. Rekap Total Estimasi Biaya Purwarupa
- **Total Komponen Utama (A + B + C):** **Rp1.960.000**
- **Cadangan Bahan Habis Pakai & Ongkir (~12%):** **Rp240.000** *(isolasi tahan air, lem/sealant, tiang ajir, PCB/jumper)*
- **TOTAL ESTIMASI PURWARUPA:** **Rp2.200.000** *(~Rp735.000 per mahasiswa untuk tim 3 orang; jauh di bawah batas plafon CD-2 `≤ Rp5.000.000`)*

