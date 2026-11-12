# Panduan Ekstensi IDE dan Alur Kerja Git Capstone Design

Dokumen ini mencatat daftar ekstensi yang digunakan di Antigravity / VS Code untuk pengerjaan Capstone Design **PTA Jeruk Limau (Kebun Ciberes, Subang)** serta penjelasan ringkas alur kerja Git (Commit vs. Push).

---

## 1. Daftar Ekstensi & Alat Bantu yang Direkomendasikan

| Nama Ekstensi | Identifier | Fungsi Utama untuk Proyek Capstone |
|---|---|---|
| **Markdown Preview Enhanced** | `shd101wyy.markdown-preview-enhanced` | Menampilkan preview dokumen `.md` dengan rumus matematika $\text{KaTeX/LaTeX}$, tabel rapi, dan diagram Mermaid secara instan. |
| **Markdown All in One** | `yzhang.markdown-all-in-one` | Otomasi navigasi *Table of Contents* (TOC), penomoran bab, dan pemformatan teks naskah proposal. |
| **Draw.io Integration** | `hediet.vscode-drawio` | Membuat dan menyunting diagram blok sistem (ESP32, pompa, sensor), diagram alir, serta skema perpipaan hidrolika di dalam editor. |
| **VSCode PDF Viewer** | `tomoki1207.pdf` | Membaca dokumen PDF hasil ekspor (CD-1, CD-2, CD-3) dan jurnal acuan IEEE/paten tanpa harus keluar dari Antigravity IDE. |
| **Python** | `ms-python.python` | Menjalankan skrip generator naskah resmi (`build_full_cd3.py`) yang mengompilasi dokumen Word dengan formula native OMML. |
| **Code Spell Checker - Indonesian** | `streetsidesoftware.code-spell-checker-indonesian` | Mendeteksi salah ketik (*typo*) pada penulisan karya tulis ilmiah berbahasa Indonesia formal. |
| **PlatformIO IDE** | `platformio.platformio-ide` | Lingkungan pemrograman mikrokontroler ESP32, kalibrasi sensor kelembapan tanah, dan pengujian relay katup solenoid (tahap purwarupa). |

---

## 2. Perbedaan Mendasar: Commit vs. Push

Banyak pemula bingung membedakan antara *Commit* dan *Push*. Berikut analogi sederhananya:

```text
[ Komputer Lokal Anda ]                                  [ Server GitHub Online ]
  File Diedit ──> git add ──> git commit ───────────────> git push
  (Kerja di laptop) (Masuk Amplop) (Disimpan di Laptop)     (Terkirim ke GitHub)
```

1. **Commit (`git commit`)**:
   * **Menyimpan perubahan di laptop lokal Anda.**
   * Ibarat membuat *checkpoint* / *savepoint* game di komputer Anda sendiri.
   * Berkas **belum terkirim ke internet**. Rekan tim dan dosen belum bisa melihat perubahan ini sebelum Anda melakukan *Push*.

2. **Push (`git push`)**:
   * **Mengirim dan menyinkronkan *commit* dari laptop ke server GitHub.**
   * Setelah berhasil di-push, seluruh perubahan akan muncul di website `https://github.com/azurre13/pta-jeruk-limau`.
   * Rekan tim (Al Qarnie, Daffa) dapat melihat dan mengunduh (*pull*) berkas baru tersebut ke laptop mereka masing-masing.

---

## 3. Langkah Standar Alur Kerja Git Tim

Setiap kali Anda selesai mengedit atau menambahkan berkas baru:

1. **Simpan lokal (Commit):**
   ```powershell
   git add .
   git commit -m "docs: tambah panduan ekstensi dan alur kerja git"
   ```
2. **Kirim ke GitHub (Push):**
   ```powershell
   git push origin main
   ```
3. **Mengambil pembaruan terbaru dari teman tim (Pull):**
   ```powershell
   git pull origin main
   ```
