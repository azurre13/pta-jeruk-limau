# Melanjutkan Proyek Ini di Chat Baru / AI Lain

**Diperbarui: 16 November 2026.** Cukup buka folder repo `C:/Users/daffa/Documents/pta-jeruk-limau` lalu beri kabar hasil bimbingan atau tugas baru — AI tidak perlu diberi penjelasan ulang dari awal.

---

## Urutan Baca Wajib (Cepat & Hemat Konteks)

AI cukup membaca **5 file inti** berikut untuk memahami 100% status terakhir (`16 November 2026`):
1. [`AGENTS.md`](../AGENTS.md) *(aturan kerja & konteks awal — otomatis dimuat Antigravity bersama [`GEMINI.md`](../GEMINI.md))*
2. [`konteks-ai/KONTEKS_PROYEK.md`](KONTEKS_PROYEK.md) *(ringkasan fakta, batas `CD-1/CD-2`, & perubahan pasca-survei `15 Nov`)*
3. [`konteks-ai/STATUS_DAN_TINDAK_LANJUT.md`](STATUS_DAN_TINDAK_LANJUT.md) *(antrean keputusan bimbingan PBB 1 & status dokumen)*
4. [`catatan/HASIL_SURVEI_CIBERES_15_NOV_2026.md`](../catatan/HASIL_SURVEI_CIBERES_15_NOV_2026.md) *(fakta terukur `Kebun Besar 1`, `Kebun Besar 2`, & `Kebun Kecil` + alasan usulan pindah ke `Kebun Kecil` & sensor tanah)*
5. [`catatan/RINGKUMAN_QNA_SCOPE_DAN_ZONASI_PRA_SURVEI.md`](../catatan/RINGKUMAN_QNA_SCOPE_DAN_ZONASI_PRA_SURVEI.md) *(hasil Q&A desain, *Pure 15 L*, standar perangkat keras, & analisis zonasi)*

*Baca file pendamping di bawah ini hanya bila relevan dengan perintah pengguna:*
- Jika membahas sumber air irigasi / pompa: [`catatan/KAJIAN_SUMBER_AIR_IRIGASI_DAN_POMPA.md`](../catatan/KAJIAN_SUMBER_AIR_IRIGASI_DAN_POMPA.md) & [`catatan/CHECKLIST_SURVEI_MITRA_CIBERES.md`](../catatan/CHECKLIST_SURVEI_MITRA_CIBERES.md).
- Jika butuh kutipan mentah transkrip Audio 1/2/sayuran: [`catatan/DATA_MITRA_LENGKAP.md`](../catatan/DATA_MITRA_LENGKAP.md).
- Jika akan merevisi naskah `CD-1`/`CD-2`/`CD-3`: baca [`CD-2 Final ACC`](../dokumen/cd2/CD%202%20-%20ANALISIS%20PERMASALAHAN%20PENYIRAMAN%20MANUAL%20PADA%20KEBUN%20JERUK%20LIMAU%20DI%20CIBERES%20SUBANG.pdf), [Buku Panduan Capstone 2024](../sumber/panduan/bukupanduancapstone_2024signed.pdf), template di `sumber/template/`, serta [`Jadwal_PTA`](../sumber/rubrik-jadwal/Jadwal_PTA%20--%20Rubrik%20PTA%20--%202627%20%281%29.pdf).

---

## Contoh Prompt Singkat Chat Baru (Pasca-Bimbingan PBB 1)

> Lanjutkan PTA Jeruk Limau sesuai konteks `16 Nov 2026`. Hasil bimbingan dengan Pak Agung (PBB 1): [tulis keputusan beliau soal Kebun Kecil vs Kebun Besar, aturan revisi CD-1/CD-2, dan catu daya]. Tolong susun rencana eksekusi `CD-3` (dan revisi bila perlu).

Jika sebelum/sesudah itu ingin merapikan folder media survei `15 Nov` di `sumber/dokumentasi/`:
> Rapikan file foto & video survei `15 Nov` di `sumber/dokumentasi/` (hapus duplikat identik, pisahkan `Kebun Besar 1`, `Kebun Besar 2`, & `Kebun Kecil`, dan lengkapi ekstensi file yang hilang).

---

## Peta Folder Aktif

| Lokasi dari Root Repo | Fungsi |
|---|---|
| [`dokumen/cd1/`](../dokumen/cd1/) & [`dokumen/cd2/`](../dokumen/cd2/) | **Berkas Final ACC** (`CD-1` 26 hlm & `CD-2` 26 hlm — terkunci; revisi hanya jika diizinkan PBB 1 & Dosen Kelas). |
| [`dokumen/draf/cd3_daffa/`](../dokumen/draf/cd3_daffa/) | Workspace usulan `CD-3` & simulasi (terpisah dari draf rekan `dokumen/cd3/`, ditahan sampai keputusan PBB 1). |
| [`catatan/HASIL_SURVEI_CIBERES_15_NOV_2026.md`](../catatan/HASIL_SURVEI_CIBERES_15_NOV_2026.md) | **Induk temuan survei `15 Nov 2026`** (`Kebun Besar 1`, `Kebun Besar 2`, `Kebun Kecil`) & bahan diskusi PBB 1. |
| [`catatan/RINGKUMAN_QNA_SCOPE_DAN_ZONASI_PRA_SURVEI.md`](../catatan/RINGKUMAN_QNA_SCOPE_DAN_ZONASI_PRA_SURVEI.md) | Induk keputusan desain, *scope Pure 15 L*, hardware wajib, & analisis zona aman. |
| [`catatan/KAJIAN_SUMBER_AIR_IRIGASI_DAN_POMPA.md`](../catatan/KAJIAN_SUMBER_AIR_IRIGASI_DAN_POMPA.md) | Kajian saluran irigasi vs parit, elevasi `Δz`, kabel `12 V`, & isian hasil ukur survei. |
| [`catatan/CHECKLIST_SURVEI_MITRA_CIBERES.md`](../catatan/CHECKLIST_SURVEI_MITRA_CIBERES.md) | Checklist lapangan yang sebagian diisi pada survei `15 Nov 2026`. |
| [`catatan/PAPARAN_SOLUSI_UNTUK_MITRA.md`](../catatan/PAPARAN_SOLUSI_UNTUK_MITRA.md) | Ringkasan non-teknis solusi & kesepakatan diskusi dengan mitra. |
| [`catatan/DATA_MITRA_LENGKAP.md`](../catatan/DATA_MITRA_LENGKAP.md) | Induk data mitra & reproduksi penuh transkrip Audio 1/2 + sayuran *(kamus referensi)*. |
| [`catatan/arsip/`](../catatan/arsip/README.md) | Arsip catatan historis pra-Q&A yang sudah selesai. |
| `sumber/` & `work/` | Bahan sumber asli + foto/video survei (`hanya-baca` kecuali diminta merapikan duplikat) & folder sementara (`diabaikan Git`). |

---

## Jika Chat Hanya Menerima Lampiran File
Lampirkan **`AGENTS.md`**, **`konteks-ai/KONTEKS_PROYEK.md`**, **`konteks-ai/STATUS_DAN_TINDAK_LANJUT.md`**, dan **`catatan/HASIL_SURVEI_CIBERES_15_NOV_2026.md`**.
