# Konteks Lengkap Proyek PTA Kebun Jeruk Limau

**Diperbarui: 16 November 2026.** Baca file ini, [STATUS_DAN_TINDAK_LANJUT.md](STATUS_DAN_TINDAK_LANJUT.md), [`HASIL_SURVEI_CIBERES_15_NOV_2026.md`](../catatan/HASIL_SURVEI_CIBERES_15_NOV_2026.md), dan [`RINGKUMAN_QNA_SCOPE_DAN_ZONASI_PRA_SURVEI.md`](../catatan/RINGKUMAN_QNA_SCOPE_DAN_ZONASI_PRA_SURVEI.md) di awal chat baru. Kronik revisi lama Oktober–awal November dipindahkan ke [`catatan/arsip/README.md`](../catatan/arsip/README.md).

---

## 1. Tujuan, Identitas, dan Jadwal Akademik

- **Tujuan Mitra:** Menggantikan pekerjaan timba-guyur air manual (`last-mile irrigation`) agar biaya tenaga kerja turun, pemberian air per pohon lebih terjamin terhadap acuan `15 L`, dan biaya total tahun pertama lebih hemat (alat, instalasi, energi, perawatan, dan upah tersisa).
- **Tahap Aktif (`16 November 2026`):** `CD-1` (`26 hlm`) dan `CD-2` (`26 hlm`) berstatus **Final ACC**. Survei lapangan Ciberes sudah dilakukan pada **Minggu, 15 November 2026**, dan **tim sedang menyiapkan diskusi bimbingan Pembimbing 1 (`17 November 2026`) untuk memutuskan arah lokasi implementasi (`Opsi A Pindah Kebun Kecil + revisi CD-1/CD-2` vs `Opsi B Tetap Kebun Besar Portabel`)** sebelum mengedit naskah/skrip `CD-3`.

| Identitas / Jadwal | Data Resmi Terverifikasi |
|---|---|
| Tim Mahasiswa | Muhammad Al Qarnie (`101032330043`), Maheswara Ariq Athallah (`101032300050`), Daffa Hermansyah (`101032330090`) |
| Institusi & Pembimbing 1 | S1 Teknik Komputer, FTE Universitas Telkom · **Dr. Agung Nugroho Jati, S.T., M.T.** *(Pembimbing 2 & ttd CD-3 belum ada)* |
| Lokasi Tapak Proyek | `JH7H+222`, Desa Ciberes, Kec. Patokbeusi, Kab. Subang, Jawa Barat *(nama usaha/pengelola belum tercantum)* |
| Pemilik Repo & Visibilitas | `azurre13/pta-jeruk-limau` (`public` saat dicek 9 Okt 2026; verifikasi ulang via Git sebelum menyatakan status) |
| Tenggat Resmi `CD-3` | `CLO3 - CD3-1`: **Kamis, 10 Desember 2026** · `CLO4 - CD3-2` (`CD1-3 Gabungan`): **Kamis, 7 Januari 2027** · `SemPro`: **11–16 Januari 2027** |

---

## 2. Sistem Eksisting dan Pemisahan Badan Air

```text
Saluran irigasi besar / "sungai" di luar kebun (garis citra 20,54 m; paralel koridor 117,52 m)
          │
          ▼
Pompa mesin bensin Alkon 2 inci — PERTALITE AKTIF
(uji coba modifikasi LPG 3 kg pada masa lalu DIHENTIKAN permanen karena overheating & merusak seher/ring)
          │
          ▼
3 parit galian tanah dalam kebun (±100 m memanjang + penghubung melintang "+")
          │
          ▼
4 pekerja menimba dengan ember hitam kecil -> mengguyur manual tiap pohon
```

- **Beda fungsi air:** Saluran irigasi luar adalah **sumber air eksternal**; 3 parit tanah adalah **penampung dekat pohon** (bukan sumber air mandiri atau sistem otomatis).
- **Tanpa PLN:** Jarak rumah berlistrik pada foto lokasi lain tidak membuktikan kebun jeruk tersambung PLN.

---

## 3. Fakta Mitra, Batas Kepastian, dan Skenario Hitungan

| Informasi | Status & Batas Penggunaan |
|---|---|
| `±500–600 pohon`, tinggi banyak pohon `±1 m` | Keterangan lisan mitra/tim; **belum sensus riil**. *(Catatan anomali: jika hanya 3 baris × 100 m, 500–600 pohon berarti jarak tanam 0,5–0,6 m — wajib sensus Minggu.)* |
| `3 parit ±100 m` + penghubung melintang `+`, lebar kebun (`~6 m` lisan vs `~25–30 m` di CD-2), garis citra `117,52 m` & `20,54 m` | Garis peta hanya jarak horizontal `2D`, **bukan beda tinggi vertikal (`Δz` / head pompa)**, bukan luas lahan terukur, dan bukan lebar jalur bebas robot. |
| Penyiraman `~3 hari sekali`, `4 pekerja × Rp100.000 = Rp400.000/kegiatan` | Skenario upah tetap (`(365/3) × Rp400 rb ≈ Rp48,7 juta/tahun`; `10 kegiatan/30 hr = Rp4 jt`) **bukan pengeluaran tercatat**, belum memperhitungkan hujan, bensin Pertalite, maupun servis Alkon. |
| Acuan minimal `15 L/pohon` (`7,5–9 m³` nominal/kegiatan) | Berasal dari keterangan mitra; **bukan volume ember aktual** (kapasitas ember & tumpahan belum diukur) dan **bukan dosis agronomis tervalidasi**. |
| Air parit cepat habis setelah pompa berhenti | Laporan mitra; besar rembesan vs pengambilan ember vs penguapan belum diukur. |
| Biaya kumulatif `~Rp90 juta` & pemupukan `2×/tahun` (`"1 kuintal lebih"`) + pestisida mingguan | Penuturan mitra sejak buka lahan / umum; rincian cakupan, jenis, dan kesuburan tanah jeruk belum diuji lab. |

**Aturan Sumber Audio & Pemisahan Lokasi (Wajib):**
- **Audio 1** adalah sumber utama tapak jeruk (`00:04–00:15` pekerja panen **jangan** dipakai untuk penyiraman; `05:15–06:08` rujukan kebun lain berlistrik **jangan** dipindahkan ke tapak jeruk).
- **Audio 2** hanya tambahan setelah memisahkan kondisi **kebun belakang rumah** (`00:58–01:43` bekas sampah/empang/urukan; `03:29–04:04` kotak resapan).
- **Wawancara sayuran** (terong/kembang kol `±500 m–1 km` di persawahan: panen `15/17 ton`, urea `3/5 kuintal/ha`, `100–200 bata`, keluhan pH labil) **dilarang keras** dipindahkan sebagai kondisi tanah atau pupuk kebun jeruk.
- Yang dibaca tim AI adalah **transkrip & reproduksi teks** ([DATA_MITRA_LENGKAP.md](../catatan/DATA_MITRA_LENGKAP.md)), bukan audio mentah langsung.

---

## 4. Batasan Mengikat dari `CD-1` & `CD-2` Final ACC

- **CD-1 (`dokumen/cd1/`, `26 hlm`, ACC):** Kompleksitas yang didukung analisis adalah kriteria **1, 2, dan 7**; kriteria **3** diajukan lewat pemodelan hubungan air–waktu–energi–pekerjaan–biaya tahun ke-1; kriteria **6 belum terpenuhi** (butuh wawancara kebutuhan pekerja pada `Pos A.2` survei Minggu).
- **CD-2 (`dokumen/cd2/`, `26 hlm`, ACC ttd Pembimbing 1 `4/11/2026`):** Menetapkan **`C-01..C-05`** dan **`S-01..S-14`**:
  - `C-01` & `S-06`: 100% *off-grid*, cadangan daya mandiri **`>= 8,0 jam`** (`>= 2 siklus penuh`, `LiFePO4 DoD 80%`).
  - `C-02` & `S-05`: air sungai keruh `20,54 m`, saringan **`>= 120 mesh` (`<= 130 µm`)**.
  - `C-03`: purwarupa wajib minimal **`1 lajur 15–20 pohon pada bentang operasional >= 25 m`**, dan modular ke `500–600 pohon` (`100–117,52 m`, `~3.000 m²`).
  - `C-04` & `S-07`: keselamatan **`SELV <= 48 V DC`** dan selungkup **`IP65` (`20–55 °C`)**.
  - `C-05`: *solution-agnostic* sampai evaluasi pembandingan di `CD-3`.
  - `S-01`: dosis **`10–15 L ± 5% / pohon`** (verifikasi `Tabel 4`: **wadah tera, gelas ukur, `Flow meter`** — bukan wajib sensor tanah).
  - `S-02`: `CU >= 85%` | `S-03`: siklus penuh **`<= 4,0 jam`** (`<= 24–28 dtk/pohon`) | `S-04`: radius pembasahan `0,5–0,8 m`, dalam `20–40 cm` (tanpa genangan `> 30 mnt`).
  - `S-08`: CAPEX purwarupa **`<= Rp5.000.000`**, proyeksi penuh **`<= Rp18.000.000`** | `S-09`: `OPEX <= Rp50.000/siklus` | `S-10`: `PP <= 12–18 bulan`.
  - `S-11`: `eta_a >= 80%` | `S-12`: `0 g/kWh` emisi | `S-13`: **Tombol Tunggal (`ajar <= 30 mnt`)** | `S-14`: rawat saringan `<= 20 mnt/bln`.

---

## 5. Kesepakatan Rekayasa & Temuan Survei (`14–16 November 2026`)

Rincian lengkap pra-survei & pasca-survei tersedia pada [`HASIL_SURVEI_CIBERES_15_NOV_2026.md`](../catatan/HASIL_SURVEI_CIBERES_15_NOV_2026.md), [`KAJIAN_SUMBER_AIR_IRIGASI_DAN_POMPA.md`](../catatan/KAJIAN_SUMBER_AIR_IRIGASI_DAN_POMPA.md), dan [`RINGKUMAN_QNA_SCOPE_DAN_ZONASI_PRA_SURVEI.md`](../catatan/RINGKUMAN_QNA_SCOPE_DAN_ZONASI_PRA_SURVEI.md):
1. **Temuan Kritis Survei `15 November 2026` di `Kebun Besar 1`:**
   - Cacah pohon riil `4` baris = **`160` pohon** (`53+37+37+33`, jarak tanam `~2,28 m`), bukan `500–600` dalam satu hamparan tersebut (`500–600` terpecah dengan `Kebun Besar 2` + lahan kosong + `Kebun Kecil`).
   - Jarak saluran ke parit `10 m` dengan **beda tinggi vertikal `Δz = 4–5 m`** (`> batas hisap 2 m`), **tanpa pagar sama sekali** (hanya paranet hitam tipis), **rawan pencurian**, ember pekerja `~7 L` (`2 ember ≈ 13 L`, demo pekerja `~15 L` pakai selang kanvas + ember), dan pekerja di video menyebut jadwal biasa **`1× seminggu` (`seharian`)**.
2. **Alasan Usulan Pindah ke `Kebun Kecil` (Akan Dikonsultasikan ke PBB 1 `17 Nov 2026`):**
   - Draf `BOM_PROTOTYPE` lama ([`bom_and_data.py`](../dokumen/draf/cd3_daffa/bom_and_data.py)) sudah mencapai **`Rp4.850.000`** (`+ Support RAB Rp1.585.000 = Rp6.435.000`) dengan pos surya+baterai **`Rp2.020.000`** hanya untuk `1` petak uji `15–24` pohon (sisa Kebun Besar tetap pakai `Alkon` manual) — dan sangat berisiko dicuri.
   - **`Kebun Kecil`** (`13:27–13:32 WIB`) memiliki **`72` pohon tercatat / `73` disebut tim** (`jarak 290 cm`, `2 pasang` `100–120 cm`), **`6` parit dangkal `6 cm`** (`40 cm` utama / `25 cm` kecil), **`toren 75 × 75 cm`**, **`pipa sumur baru bangun` berjarak `170 cm` ke parit**, berpagar bambu & tembok rumah (**aman dari maling**, dekat jaringan listrik rumah), tanah urugan bekas empang/timbunan sampah (`Audio 2`), serta penyiraman masih manual. Pindah ke `Kebun Kecil` berpotensi **menuntaskan 100% seluruh `72–73` pohon**, **memangkas biaya PLTS bila diizinkan PBB 1 (`PSU 12 V` vs PLTS kecil)**, dan menambah **sensor kondisi tanah multi-zona** (*lengas + suhu + opsi EC/pH, hindari "sensor NPK RS485 murah" tanpa kalibrasi lab*).
3. **Konsekuensi Akademik (Wajib Diputuskan PBB 1 Besok):** Pindah ke `Kebun Kecil` menuntut revisi terkoordinasi atas `CD-1` dan `CD-2` (`C-01 off-grid`, `C-02 sungai`, `C-03 500–600 pohon`, ekonomi) menjelang **`CD1-3 (Gabungan)` `7 Jan 2027`**. Jika PBB 1 melarang mengubah `CD-1`/`CD-2`, cadangannya tetap di `Kebun Besar` dengan desain **kotak unit portabel lepas-pasang bawa-pulang**.

---

## 6. Koreksi Terdahulu yang Dilarang Terulang

1. Tiga parit adalah selokan tanah eksisting (memudahkan timba ember), bukan pipa usulan AI atau furrow teruji, dan saling terhubung melintang `+`.
2. Pompa aktif mitra adalah **Alkon Pertalite**; **LPG 3 kg sudah dihentikan** (bukan sistem berjalan).
3. Jangan menyamakan `12 zona / center-feed` sketsa lama, kebun belakang rumah (`Audio 2`), atau kebun sayuran ke tapak jeruk.
4. `15 L/pohon` belum menjadi volume terukur aktual; `Rp48,7 jt/tahun` hanyalah skenario upah; pagu final `CD-2` adalah `<= Rp5 jt` purwarupa / `<= Rp18 jt` penuh (bukan `Rp6 jt` catatan lama).
5. Jangan memodifikasi berkas `sumber/`, `dokumen/cd1/`, `dokumen/cd2/`, `dokumen/cd3/`, maupun `dokumen/draf/cd3_daffa/` sebelum keputusan bimbingan PBB 1 (`17 Nov 2026`) keluar dan disepakati tim.
