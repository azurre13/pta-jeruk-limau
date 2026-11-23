# Konteks Lengkap Proyek PTA Kebun Jeruk Limau

**Diperbarui: 22 November 2026.** Baca file ini, [STATUS_DAN_TINDAK_LANJUT.md](STATUS_DAN_TINDAK_LANJUT.md), [`README_TRANSISI_KEBUN_BESAR_KE_KEBUN_KECIL_CD2_CD3.md`](../catatan/README_TRANSISI_KEBUN_BESAR_KE_KEBUN_KECIL_CD2_CD3.md), [`DATA_KEBUN_KECIL_DAN_ZONA_4_POHON.md`](../catatan/DATA_KEBUN_KECIL_DAN_ZONA_4_POHON.md), [`HASIL_SURVEI_CIBERES_15_NOV_2026.md`](../catatan/HASIL_SURVEI_CIBERES_15_NOV_2026.md), dan [`RINGKUMAN_QNA_SCOPE_DAN_ZONASI_PRA_SURVEI.md`](../catatan/RINGKUMAN_QNA_SCOPE_DAN_ZONASI_PRA_SURVEI.md) di awal chat baru. Kronik revisi lama Oktober–awal November dipindahkan ke [`catatan/arsip/README.md`](../catatan/arsip/README.md).

---

## 1. Tujuan, Identitas, dan Jadwal Akademik

- **Tujuan Mitra:** Awalnya menggantikan penyiraman manual agar biaya turun dan air lebih terjamin (`10–15 L/pohon`). Setelah ACC pindah ke **`Kebun Kecil`**, mitra menginginkan kebun ini menjadi **kebun acuan/percontohan** yang bukan hanya menuntaskan irigasi (`Alkon` + `2 pekerja × Rp100 rb / 3–4 hari`), melainkan juga **memaksimalkan pertumbuhan pohon dan produktivitas buah** (judul proyek berpeluang diperbarui pada tahap `CD1–3 Final`).
- **Tahap Aktif (`22 November 2026`):** `CD-1` (`26 hlm`) dan `CD-2` (`26 hlm`) sudah dikumpulkan dan **dibiarkan utuh dulu**. Pembimbing 1 (**Dr. Agung Nugroho Jati, S.T., M.T.**), Dosen Pengampu Kelas, dan Mitra sudah **ACC memindahkan target ke `Kebun Kecil` (`1 Zona = 4 Pohon Sampel`)**. Roadmap resmi berikutnya: menyusun **`CD-3` (`tenggat 10 Des 2026`)** disertai **catatan transisi `Kebun Besar` → `Kebun Kecil`** agar nyambung ke `CD-2`, lalu setelah `CD-1/2/3` terkumpul semua akan **digabung dan dirombak total menjadi `CD1–3 Final` untuk SemPro PTA (`7 Jan 2027`)**.

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

## 5. Kesepakatan Rekayasa, Alasan Pindah, & Data Baru (`15 & 22 November 2026`)

Rincian lengkap tersedia pada [`README_TRANSISI_KEBUN_BESAR_KE_KEBUN_KECIL_CD2_CD3.md`](../catatan/README_TRANSISI_KEBUN_BESAR_KE_KEBUN_KECIL_CD2_CD3.md), [`DATA_KEBUN_KECIL_DAN_ZONA_4_POHON.md`](../catatan/DATA_KEBUN_KECIL_DAN_ZONA_4_POHON.md), [`denah_kebun_kecil_2d.png`](../catatan/denah_kebun_kecil_2d.png), [`transkrip_survey_limau.md`](../sumber/dokumentasi/kebon%20kecil/Record%20survey%2022%20Nov/transkrip_survey_limau.md), dan [`HASIL_SURVEI_CIBERES_15_NOV_2026.md`](../catatan/HASIL_SURVEI_CIBERES_15_NOV_2026.md):
1. **Alasan Resmi Pindah dari `Kebun Besar` (Data Lama Tetap Disimpan Utuh):**
   - `Kebun Besar 1` (`160` pohon sensus riil `4` baris) memiliki jarak irigasi `10 m` dengan **tebing curam `Δz = 4–5 m`**, arus saluran irigasi bisa **sangat deras saat hujan**, **saluran irigasi bukan tanah milik mitra** (sulit izin instalasi), **tanpa pagar & jauh dari permukiman** (rawan maling), dan **tanpa PLN** sehingga pompa daya tinggi + PLTS + baterai membuat draf `BOM_PROTOTYPE` lama (`dokumen/draf/cd3_daffa/bom_and_data.py` — **draf lama tidak terpakai**: `Rp4,85 jt` / `+ RAB Rp6,435 jt`) melebihi budget mahasiswa hanya untuk `1` petak uji.
2. **Keputusan ACC `Kebun Kecil` (`1 Zona = 4 Pohon Sampel`) & Kondisi Operasional Berjalan:**
   - PBB 1, Dosen Pengampu, dan Mitra **ACC pindah ke `Kebun Kecil`** (`72–73` pohon, `~471 m²`, berpagar aman di permukiman, **listrik PLN tersedia & dapat dipakai bila perlu**).
   - **Air, pompa, & biaya eksisting:** toren `75×75 cm` **tidak akan dipakai** (kapasitas liter tak diketahui); suplai air langsung dari **sumur baru** (`ban kiri atas`) yang saat ini masih disedot **pompa Alkon bensin** dengan biaya **`2 pekerja × Rp100.000 = Rp200.000 / kegiatan`** tiap **`3–4 hari sekali` jika tidak ada hujan** (`~Rp18,2–24,3 jt/thn` `[Hasil Perhitungan skenario tanpa hujan]`), dosis air tetap **`10–15 L/pohon`**.
   - **Visi mitra:** `Kebun Kecil` diharapkan menjadi **acuan/percontohan** bukan hanya untuk irigasi hemat biaya, tetapi juga **memaksimalkan pertumbuhan pohon dan produktivitas buah**.
3. **Data Terukur Zona Uji 1 (`4 Pohon`, Umur Serentak `16 Bulan`) & Skala Drone:**
   - **Tinggi & buah:** `Sampel 1 = 46 cm` *(cacat/kerdil, tidak berbuah)*, `Sampel 2 = 100 cm` *(banyak buah — bagus walau masih kecil; acuan baju merah)*, `Sampel 3 = 250 cm` *(berbuah lebat — sudah dipanen/diambil; **`5,43×`** Sampel 1)*, `Sampel 4 = 210 cm` *(berbuah — sudah dipanen/diambil)*.
   - **Jarak antar-pohon:** `P1–P2 = 300 cm`, `P2–P3 = 210 cm`, `P3–P4 = 290 cm`, `P4–P1 = 230 cm` (`keliling = 10,30 m`; diagonal `P2–P4 ≈ 4,05 m`, `P1–P3 ≈ 3,27 m`). Target panen dewasa `> 2,5 tahun`: `10–15 kg/pohon` berbuah.
   - **Jarak acuan `P2 / Baju Merah` ke sumur:** lurus atas `11,2 m` + kiri `5,0 m` → **jarak lurus miring Pythagoras = `12,27 m`** (`jalur siku = 16,20 m`).
   - **Kalibrasi 3 foto nadir DJI Mini 4 Pro (`~65,87 px/m ±5–7%`):** sisi atas `~18,7 m`, bawah `~19,9 m`, kiri `~24,8 m`, kanan `~24,4 m`, perkiraan luas terpagar **`~471 m²`** ([denah_kebun_kecil_2d.png](../catatan/denah_kebun_kecil_2d.png)).

---

## 6. Koreksi Terdahulu & Aturan Kerja Lintas Tahap

1. Data `Kebun Besar` (`4` pekerja × `Rp100.000` / `~3` hari) tetap disimpan sebagai histori `CD-1/CD-2` — **jangan dihapus** dan **jangan dicampur** dengan data operasional `Kebun Kecil` (**sumur pakai `Alkon bensin` + `2` pekerja × `Rp100.000` / `3–4` hari tanpa hujan**).
2. Di `Kebun Kecil`, **toren `75×75 cm` tidak akan dipakai**; desain suplai air langsung dari **sumur baru**, sedangkan **listrik PLN tersedia** jika dibutuhkan.
3. Jangan menyamakan `12 zona / center-feed` sketsa lama atau kondisi kebun sayuran (`terong/kembang kol`) ke `Kebun Kecil`.
4. `10–15 L/pohon` & `10–15 kg/pohon (> 2,5 thn)` adalah patokan mitra; skenario biaya tahunan `~Rp18,2–24,3 jt/tahun` (`Kebun Kecil`) maupun `~Rp48,7 jt/tahun` (`Kebun Besar`) adalah hasil hitungan tanpa hari hujan, bukan pengeluaran tercatat.
5. **Alur dokumen resmi:** `CD-1` & `CD-2` tidak direvisi saat ini; seluruh berkas `CD-3` yang sudah ada (`dokumen/cd3/`, `dokumen/draf/cd3/`, maupun draf lama di `dokumen/draf/cd3_daffa/`) berstatus **draf lama tidak terpakai** (jangan dilanjutkan). **`CD-3` (`10 Des 2026`) belum dibuat sekarang** — kelak dibuat **baru dari awal** dengan menyisipkan catatan transisi agar nyambung ke `CD-1/CD-2`; lalu **`CD1–3 Final`** digabung & dirombak total untuk **SemPro PTA (`7 Jan 2027`)** setelah `CD-3` beres. Jangan membuat/mengedit berkas `CD-3` maupun `dokumen/` sebelum pengguna memberi arahan mulai.
