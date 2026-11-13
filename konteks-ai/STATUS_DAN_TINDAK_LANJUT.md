# Status Terkini dan Tindak Lanjut (`14 November 2026`)

**Diperbarui: 14 November 2026.** Ringkasan status dokumen resmi, draf tertahan, dan daftar antrean data survei Minggu sebelum merevisi `CD-3`. *(Catatan historis revisi CD-1/CD-2 bulan Oktober–awal November disimpan di [`catatan/arsip/README.md`](../catatan/arsip/README.md).)*

---

## 1. Status Berkas Akademik

| Dokumen / Folder | Status Sekarang | Aturan Kerja |
|---|---|---|
| [`dokumen/cd1/`](../dokumen/cd1/CD%201%20-%20ANALISIS%20PERMASALAHAN%20PENYIRAMAN%20MANUAL%20PADA%20KEBUN%20JERUK%20LIMAU%20DI%20CIBERES%20SUBANG.pdf) | **Final ACC (`26 halaman`, ttd Pembimbing 1)** | **Terkunci / Jangan Diubah.** |
| [`dokumen/cd2/`](../dokumen/cd2/CD%202%20-%20ANALISIS%20PERMASALAHAN%20PENYIRAMAN%20MANUAL%20PADA%20KEBUN%20JERUK%20LIMAU%20DI%20CIBERES%20SUBANG.pdf) | **Final ACC (`26 halaman`, ttd `4/11/2026`, `C-01..C-05`, `S-01..S-14`)** | **Terkunci / Acuan Mengikat `CD-3`.** |
| `dokumen/cd3/` & `dokumen/draf/cd3/` | Draf kolaborasi rekan tim (`34 halaman` / tabel `6 halaman`) | Jangan ditimpa. |
| [`dokumen/draf/cd3_daffa/`](../dokumen/draf/cd3_daffa/) | Workspace draf terpisah (`23 hlm` + tabel `4 hlm`, simulasi, BOM purwarupa `Rp4,85 jt` / penuh `Rp17,79 jt`) | **Ditahan dulu** hingga data survei Minggu terkumpul. |

---

## 2. Daftar Antrean Data Survei Minggu & Revisi `CD-3`

Panduan lapangan lengkap ada pada [`CHECKLIST_SURVEI_MITRA_CIBERES.md`](../catatan/CHECKLIST_SURVEI_MITRA_CIBERES.md) (`Pos A–G`) dan lembar ukur sumber air pada [`KAJIAN_SUMBER_AIR_IRIGASI_DAN_POMPA.md`](../catatan/KAJIAN_SUMBER_AIR_IRIGASI_DAN_POMPA.md).

| No | Item Terbuka | Status Pra-Survei (`14 Nov 2026`) | Tindakan Pasca-Survei (`CD-3`) |
|---:|---|---|---|
| 1 | **Sumber air irigasi, `Δz`, posisi pompa & kabel** | Opsi `Skenario B` (1 pompa pipa tertutup) vs `C1/C2`; aturan `Δz <= 2 m` kebun atas vs `> 2 m` boks bantaran + kabel `2×4–6 mm²`. | Ukur `Δz1/Δz2`, jarak lintasan nyata, status kemarau/gilir air, & kunci `B / C1 / C2`. |
| 2 | **Geometri `P × L`, jumlah baris, & populasi riil** | Anomali hitungan antara klaim `500–600` pohon, `3` parit `~100 m`, dan lebar (`~6 m` vs `25–30 m`); draf `cd3_daffa` masih memodelkan petak uji `20 m × 3 baris`. | Sensus pohon per baris, ukur jarak tanam & patok petak uji presisi agar `CD-3` patuh `C-03 >= 25 m`. |
| 3 | **Jumlah zona skala penuh (`S-03 <= 4,0 jam`)** | `bom_and_data.py` masih mencantumkan `10 zona @ 960 L/jam` (`9,38 jam > 4,0 jam`). Rekomendasi aman: **`4 zona`** (`3 jam 45 mnt`, `33,3–40 L/mnt`). | Selaraskan jumlah zona, kapasitas pompa DC, & BOM penuh di `bom_and_data.py` + `build_cd3_daffa.py` sesuai populasi riil. |
| 4 | **Sensor tanah vs *Pure 15 L* (`S-01`, `S-04`, `S-13`)** | Audit `CD-2 Tabel 4` menunjukkan `S-01` diverifikasi `Flow meter` + wadah tera; arah minimalis memakai `Flow Meter + tombol tunggal` dengan `0–2` sensor lengas *interlock* hujan. | Kunci keputusan final jumlah sensor tanah (`0` vs `1–2` titik *Capacitive v1.2*) bersama tim/pembimbing. |
| 5 | **Audit BBM Pertalite Alkon & sisa teks LPG di skrip** | MD & dokumen aktif sudah diluruskan; `dokumen/draf/cd3_daffa/build_cd3_daffa.py:554` masih menyebut `"dimodifikasi ke LPG"`. | Ukur konsumsi Pertalite (L/siklus) & biaya servis Alkon untuk *Payback Period*; perbaiki baris `554` saat revisi `CD-3`. |
| 6 | **Identitas mitra, kebutuhan pekerja (`Kriteria 6`), sampel tanah & air** | Identitas usaha/pengelola belum tercantum; wawancara pekerja siram belum terdokumentasi; sampel tanah `1–2 kg` & air belum diambil. | Catat izin pencantuman nama & peran alih tugas pekerja (`Pos A`); bawa sampel tanah/air ke lab Bandung. |

---

## 3. Disiplin Kerja & Target Terdekat

- Edit berkas DOCX/skrip `CD-3` hanya di `dokumen/draf/cd3_daffa/` setelah data Minggu diverifikasi; setelah edit DOCX selalu ekspor ulang PDF dan cek render visual.
- Jangan mengedit `sumber/`, `dokumen/cd1/`, `dokumen/cd2/`, atau `dokumen/cd3/`.
- Beri tanggal pembaruan di setiap `.md` yang diubah dan cek `git status` sebelum menyatakan kondisi sinkronisasi (commit/push hanya saat diminta pengguna).
- **Target jadwal PTA:** `CD3-1` **10 Desember 2026** · `CD3-2` Gabungan **7 Januari 2027** · `SemPro` **11–16 Januari 2027**.
