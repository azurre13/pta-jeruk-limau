# Melanjutkan Proyek Ini di Chat Baru / AI Lain

**Diperbarui: 22 November 2026.** Cukup buka folder repo `D:/UserData/Documents/pta-jeruk-limau` lalu beri perintah berikutnya — AI tidak perlu diberi penjelasan ulang dari awal.

---

## Urutan Baca Wajib (Cepat & Hemat Konteks)

AI cukup membaca **8 file inti** berikut untuk memahami 100% status terakhir (`22–25 November 2026`):
1. [`AGENTS.md`](../AGENTS.md) *(aturan kerja, snapshot data `22 Nov`, & roadmap dokumen)*
2. [`konteks-ai/KONTEKS_PROYEK.md`](KONTEKS_PROYEK.md) *(ringkasan fakta, batas `CD-1/CD-2`, & pemisahan angka 2 kebun)*
3. [`konteks-ai/STATUS_DAN_TINDAK_LANJUT.md`](STATUS_DAN_TINDAK_LANJUT.md) *(status berkas & tindak lanjut `CD-3` `10 Des` → `CD1–3` `7 Jan`)*
4. [`catatan/README_TRANSISI_KEBUN_BESAR_KE_KEBUN_KECIL_CD2_CD3.md`](../catatan/README_TRANSISI_KEBUN_BESAR_KE_KEBUN_KECIL_CD2_CD3.md) *(alasan lengkap pindah, perbandingan 2 kebun, & matriks jembatan `CD-2 → CD-3`)*
5. [`catatan/README_ALTERNATIF_SOLUSI_DAN_SCORING_CD3.md`](../catatan/README_ALTERNATIF_SOLUSI_DAN_SCORING_CD3.md) *(dokumen hidup alternatif solusi, 5 lapis anti-mampet, & Design Matrix Scoring berbasis Panduan Capstone)*
6. [`catatan/DATA_KEBUN_KECIL_DAN_ZONA_4_POHON.md`](../catatan/DATA_KEBUN_KECIL_DAN_ZONA_4_POHON.md) *(data terukur `4` pohon sampel `16 bln`, sumur/Alkon/listrik, & kalibrasi 3 foto drone `22 Nov`)*
7. [`catatan/HASIL_SURVEI_CIBERES_15_NOV_2026.md`](../catatan/HASIL_SURVEI_CIBERES_15_NOV_2026.md) *(histori survei 1 tanggal `15 Nov 2026`: `Kebun Besar 1`, `Kebun Besar 2`, & awal `Kebun Kecil`)*
8. [`catatan/RINGKUMAN_QNA_SCOPE_DAN_ZONASI_PRA_SURVEI.md`](../catatan/RINGKUMAN_QNA_SCOPE_DAN_ZONASI_PRA_SURVEI.md) *(hasil Q&A desain pra-survei `14 Nov` & standar perangkat keras)*

*Lampiran visual denah:* [`catatan/denah_kebun_kecil_2d.png`](../catatan/denah_kebun_kecil_2d.png) *(sketsa berskala 2D Kebun Kecil & Zona Uji 1).*

*Baca file pendamping di bawah ini hanya bila relevan dengan perintah pengguna:*
- Jika membahas sumber air irigasi / pompa: [`catatan/KAJIAN_SUMBER_AIR_IRIGASI_DAN_POMPA.md`](../catatan/KAJIAN_SUMBER_AIR_IRIGASI_DAN_POMPA.md) & [`catatan/CHECKLIST_SURVEI_MITRA_CIBERES.md`](../catatan/CHECKLIST_SURVEI_MITRA_CIBERES.md).
- Jika butuh kutipan mentah transkrip Audio 1/2/sayuran: [`catatan/DATA_MITRA_LENGKAP.md`](../catatan/DATA_MITRA_LENGKAP.md).
- Jika akan merevisi naskah `CD-1`/`CD-2`/`CD-3`: baca [`CD-2 Final ACC`](../dokumen/cd2/CD%202%20-%20ANALISIS%20PERMASALAHAN%20PENYIRAMAN%20MANUAL%20PADA%20KEBUN%20JERUK%20LIMAU%20DI%20CIBERES%20SUBANG.pdf), [Buku Panduan Capstone 2024](../sumber/panduan/bukupanduancapstone_2024signed.pdf), template di `sumber/template/`, serta [`Jadwal_PTA`](../sumber/rubrik-jadwal/Jadwal_PTA%20--%20Rubrik%20PTA%20--%202627%20%281%29.pdf).

---

## Contoh Prompt Singkat Chat Baru (Siap Menyusun `CD-3` `10 Des 2026`)

> Lanjutkan PTA Jeruk Limau sesuai konteks `22 Nov 2026`. Kita sudah sepakat pindah ke `Kebun Kecil` (`1 Zona = 4 Pohon Sampel`), `CD-1/2` dibiarkan tetap dulu, dan draf `CD-3` lama tidak dipakai. Tolong buat **`CD-3` baru dari awal** (mulai dari arsitektur sistem irigasi sumur + listrik/daya aman + sensor pemantau tanah & optimasi pertumbuhan buah) menuju tenggat `10 Des 2026` dengan menyertakan catatan transisi dari `README_TRANSISI_KEBUN_BESAR_KE_KEBUN_KECIL_CD2_CD3.md`.

---

## Peta Folder Aktif

| Lokasi dari Root Repo | Fungsi |
|---|---|
| [`dokumen/cd1/`](../dokumen/cd1/) & [`dokumen/cd2/`](../dokumen/cd2/) | **Berkas Final ACC Lama** (`CD-1` 26 hlm & `CD-2` 26 hlm — dibiarkan tetap sampai fase gabung-rombak total `CD1–3 Final` `7 Jan 2027`). |
| `dokumen/cd3/`, `dokumen/draf/cd3/`, & `cd3_daffa/` lama | **Draf Lama `CD-3` Tidak Terpakai** (era `Kebun Besar` — jangan dilanjutkan; **`CD-3` baru dibuat dari awal** nanti saat diminta pengguna). |
| [`catatan/README_TRANSISI_KEBUN_BESAR_KE_KEBUN_KECIL_CD2_CD3.md`](../catatan/README_TRANSISI_KEBUN_BESAR_KE_KEBUN_KECIL_CD2_CD3.md) | **Jembatan `CD-2 → CD-3` (`22 Nov 2026`)**: alasan detail pindah, kelebihan/kekurangan 2 kebun, & matriks perubahan. |
| [`catatan/README_ALTERNATIF_SOLUSI_DAN_SCORING_CD3.md`](../catatan/README_ALTERNATIF_SOLUSI_DAN_SCORING_CD3.md) | **Dokumen Hidup Alternatif Solusi & Scoring `CD-3` (`25 Nov 2026`)**: profil `Alt. 1/2` (+ slot `Alt. 3`), 5 lapis anti-mampet, & *Design Matrix Scoring* berbasis Panduan Capstone. |
| [`catatan/DATA_KEBUN_KECIL_DAN_ZONA_4_POHON.md`](../catatan/DATA_KEBUN_KECIL_DAN_ZONA_4_POHON.md) | **Induk data `Kebun Kecil` (`22 Nov 2026`)**: 4 pohon sampel `16 bln`, sumur/Alkon/listrik, Pythagoras `12,27 m`, & skala drone. |
| [`catatan/denah_kebun_kecil_2d.png`](../catatan/denah_kebun_kecil_2d.png) | **Sketsa Denah 2D Berskala** (`Kebun Kecil` penuh ~471 m² + detail Zona Uji 1, vektor di [`denah_kebun_kecil_2d.svg`](../catatan/denah_kebun_kecil_2d.svg)). |
| [`catatan/HASIL_SURVEI_CIBERES_15_NOV_2026.md`](../catatan/HASIL_SURVEI_CIBERES_15_NOV_2026.md) | **Induk temuan survei `15 Nov 2026`** (`Kebun Besar 1`, `Kebun Besar 2`, `Kebun Kecil`). |
| [`catatan/RINGKUMAN_QNA_SCOPE_DAN_ZONASI_PRA_SURVEI.md`](../catatan/RINGKUMAN_QNA_SCOPE_DAN_ZONASI_PRA_SURVEI.md) | Induk diskusi pra-survei mengenai desain, standar perangkat keras, & analisis zona aman. |
| [`catatan/KAJIAN_SUMBER_AIR_IRIGASI_DAN_POMPA.md`](../catatan/KAJIAN_SUMBER_AIR_IRIGASI_DAN_POMPA.md) | Kajian saluran irigasi vs parit, elevasi `Δz`, kabel `12 V`, & isian hasil ukur survei. |
| [`catatan/CHECKLIST_SURVEI_MITRA_CIBERES.md`](../catatan/CHECKLIST_SURVEI_MITRA_CIBERES.md) | Checklist lapangan yang sebagian diisi pada survei `15 Nov 2026`. |
| [`catatan/PAPARAN_SOLUSI_UNTUK_MITRA.md`](../catatan/PAPARAN_SOLUSI_UNTUK_MITRA.md) | Ringkasan non-teknis solusi & kesepakatan diskusi dengan mitra. |
| [`catatan/DATA_MITRA_LENGKAP.md`](../catatan/DATA_MITRA_LENGKAP.md) | Induk data mitra & reproduksi penuh transkrip Audio 1/2 + sayuran *(kamus referensi)*. |
| [`catatan/arsip/`](../catatan/arsip/README.md) | Arsip catatan historis pra-Q&A yang sudah selesai. |
| `sumber/` & `work/` | Bahan sumber asli + foto/video survei & folder sementara (`diabaikan Git`). |

---

## Jika Chat Hanya Menerima Lampiran File
Lampirkan **`AGENTS.md`**, **`konteks-ai/KONTEKS_PROYEK.md`**, **`konteks-ai/STATUS_DAN_TINDAK_LANJUT.md`**, **`catatan/README_TRANSISI_KEBUN_BESAR_KE_KEBUN_KECIL_CD2_CD3.md`**, dan **`catatan/DATA_KEBUN_KECIL_DAN_ZONA_4_POHON.md`**.
