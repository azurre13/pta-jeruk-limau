# Melanjutkan Proyek Ini di Chat Baru / AI Lain

**Diperbarui: 14 November 2026.** Cukup buka folder repo `C:/Users/daffa/Documents/pta-jeruk-limau` lalu beri perintah singkat — tidak perlu menempel ulang riwayat diskusi.

---

## Urutan Baca Wajib (Cepat & Hemat Konteks)

AI cukup membaca **4 file inti** berikut untuk memahami 100% proyek saat ini (~500 baris total):
1. [`AGENTS.md`](../AGENTS.md) *(aturan kerja & fakta inti — otomatis dimuat Antigravity bersama [`GEMINI.md`](../GEMINI.md))*
2. [`konteks-ai/KONTEKS_PROYEK.md`](KONTEKS_PROYEK.md) *(fakta, batas data, syarat mengikat `CD-1/CD-2` Final ACC, & larangan kekeliruan lama)*
3. [`konteks-ai/STATUS_DAN_TINDAK_LANJUT.md`](STATUS_DAN_TINDAK_LANJUT.md) *(antrean survei Minggu & daftar revisi `CD-3`)*
4. [`catatan/RINGKUMAN_QNA_SCOPE_DAN_ZONASI_PRA_SURVEI.md`](../catatan/RINGKUMAN_QNA_SCOPE_DAN_ZONASI_PRA_SURVEI.md) *(hasil Q&A `14 Nov`: sampel tanah, 5 *scope*, *Pure 15 L* + `0–2` sensor, hardware wajib, & `4 zona` aman `100 m+`)*

*Hanya baca file pendamping di bawah ini sesuai tugas spesifiknya:*
- Jika membahas survei Minggu / sumber air / pompa: [`catatan/KAJIAN_SUMBER_AIR_IRIGASI_DAN_POMPA.md`](../catatan/KAJIAN_SUMBER_AIR_IRIGASI_DAN_POMPA.md) & [`catatan/CHECKLIST_SURVEI_MITRA_CIBERES.md`](../catatan/CHECKLIST_SURVEI_MITRA_CIBERES.md).
- Jika butuh kutipan mentah transkrip Audio 1/2/sayuran: [`catatan/DATA_MITRA_LENGKAP.md`](../catatan/DATA_MITRA_LENGKAP.md) *(tidak perlu dibaca penuh setiap awal chat)*.
- Jika akan merevisi naskah `CD-3`: baca [`CD-2 Final ACC`](../dokumen/cd2/CD%202%20-%20ANALISIS%20PERMASALAHAN%20PENYIRAMAN%20MANUAL%20PADA%20KEBUN%20JERUK%20LIMAU%20DI%20CIBERES%20SUBANG.pdf), template resmi di `sumber/template/`, serta [`Jadwal_PTA`](../sumber/rubrik-jadwal/Jadwal_PTA%20--%20Rubrik%20PTA%20--%202627%20%281%29.pdf).

---

## Contoh Prompt Singkat Chat Baru

> Lanjutkan proyek PTA Jeruk Limau sesuai konteks terbaru (`14 Nov 2026`). Ini hasil survei Minggu di Ciberes: [tempel data], bantu analisis keputusan desain & pembaruan CD-3.

Jika di chat baru masih ingin lanjut tanya-jawab pra-survei:
> Lanjutkan diskusi PTA Jeruk Limau sesuai ringkasan terbaru repo. Pertanyaan saya: [tulis pertanyaan].

---

## Peta Folder Aktif

| Lokasi dari Root Repo | Fungsi |
|---|---|
| [`dokumen/cd1/`](../dokumen/cd1/) & [`dokumen/cd2/`](../dokumen/cd2/) | **Berkas Final ACC** (`CD-1` 26 hlm & `CD-2` 26 hlm — **terkunci**). |
| [`dokumen/draf/cd3_daffa/`](../dokumen/draf/cd3_daffa/) | Workspace usulan `CD-3` & simulasi (terpisah dari draf rekan `dokumen/cd3/`, ditahan sampai survei Minggu). |
| [`catatan/RINGKUMAN_QNA_SCOPE_DAN_ZONASI_PRA_SURVEI.md`](../catatan/RINGKUMAN_QNA_SCOPE_DAN_ZONASI_PRA_SURVEI.md) | Induk keputusan desain, *scope Pure 15 L*, hardware, & analisis zona aman `100 m+`. |
| [`catatan/KAJIAN_SUMBER_AIR_IRIGASI_DAN_POMPA.md`](../catatan/KAJIAN_SUMBER_AIR_IRIGASI_DAN_POMPA.md) | Kajian saluran irigasi vs parit, elevasi hisap `Δz`, kabel `12 V`, & form ukur air. |
| [`catatan/CHECKLIST_SURVEI_MITRA_CIBERES.md`](../catatan/CHECKLIST_SURVEI_MITRA_CIBERES.md) | Checklist survei lapangan Minggu (`Pos A–G`). |
| [`catatan/PAPARAN_SOLUSI_UNTUK_MITRA.md`](../catatan/PAPARAN_SOLUSI_UNTUK_MITRA.md) | Ringkasan non-teknis solusi & 6 kesepakatan diskusi dengan mitra. |
| [`catatan/DATA_MITRA_LENGKAP.md`](../catatan/DATA_MITRA_LENGKAP.md) | Induk data mitra & reproduksi penuh transkrip Audio 1/2 + sayuran *(kamus referensi)*. |
| [`catatan/arsip/`](../catatan/arsip/README.md) | Arsip catatan historis tahap `CD-1` & `CD-2` yang sudah selesai (disimpan rapi agar tidak membebani chat baru). |
| `sumber/` & `work/` | Bahan sumber asli (**hanya-baca**) & folder sementara QA (`work/` diabaikan Git). |

---

## Jika Chat Hanya Menerima Lampiran File
Lampirkan **`AGENTS.md`**, **`konteks-ai/KONTEKS_PROYEK.md`**, **`konteks-ai/STATUS_DAN_TINDAK_LANJUT.md`**, dan **`catatan/RINGKUMAN_QNA_SCOPE_DAN_ZONASI_PRA_SURVEI.md`** (plus `KAJIAN_SUMBER_AIR_IRIGASI_DAN_POMPA.md` jika membahas pompa/irigasi).
