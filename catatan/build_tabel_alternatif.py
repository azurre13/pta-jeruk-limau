# -*- coding: utf-8 -*-
"""
Script to build 'Tabel_Perbandingan_Alternatif_Solusi.docx' and export to PDF.
A clean, elegant, professional landscape document summarizing all 4 engineering
solution alternatives for CD-3, detailing their descriptions, working mechanisms,
technical pros (kelebihan), cons (kekurangan), cost estimations, and final decision status.
Includes:
- Alternatif 1: Smart Multi-Zone Micro-Drip Irrigation Network (Otomatis Penuh)
- Alternatif 2: Tracked/4WD Straddle Ditch-Rover with Articulated Robotic Spray Arm (Robot Penjelajah Pematang Parit & Lengan Robotik)
- Alternatif 3: Distributed Header Tank with Gravity Manifold (Gravitasi Tandon)
- Alternatif 4: Multipurpose Semi-Manual Irrigation & Orchard Utility Cart (Gerobak Sorong Multifungsi)
"""

import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.enum.section import WD_ORIENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=140, right=140):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def set_table_full_grid(table, color="808080", sz="4"):
    tblPr = table._tbl.tblPr
    borders = parse_xml(f'<w:tblBorders {nsdecls("w")}><w:top w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/><w:bottom w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/><w:insideH w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/><w:insideV w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/><w:left w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/><w:right w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/></w:tblBorders>')
    tblPr.append(borders)

def make_row_cant_split(row):
    trPr = row._tr.get_or_add_trPr()
    trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))

def make_row_header(row):
    trPr = row._tr.get_or_add_trPr()
    trPr.append(parse_xml(f'<w:tblHeader {nsdecls("w")}/>'))

def add_formatted_runs(p, text, font_name="Times New Roman", font_size=10, bold=False, color_rgb=None):
    parts = text.split('*')
    for i, part in enumerate(parts):
        if not part:
            continue
        r = p.add_run(part)
        r.font.name = font_name
        r.font.size = Pt(font_size)
        r.font.bold = bold
        if i % 2 == 1:
            r.font.italic = True
        if color_rgb:
            r.font.color.rgb = color_rgb

def create_document():
    doc = docx.Document()
    
    # 1. Page Setup: Landscape A4
    sec = doc.sections[0]
    sec.orientation = WD_ORIENT.LANDSCAPE
    sec.page_width = Inches(11.69)
    sec.page_height = Inches(8.27)
    sec.top_margin = Inches(0.6)
    sec.bottom_margin = Inches(0.6)
    sec.left_margin = Inches(0.7)
    sec.right_margin = Inches(0.7)
    
    # 2. Header Document Title
    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(0)
    p_title.paragraph_format.space_after = Pt(2)
    add_formatted_runs(p_title, "TABEL PERBANDINGAN DAN ANALISIS 4 ALTERNATIF SOLUSI REKAYASA (CD-3)", font_size=13, bold=True)
    
    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_before = Pt(0)
    p_sub.paragraph_format.space_after = Pt(3)
    add_formatted_runs(p_sub, "Proyek Capstone Design: *Analisis Permasalahan Penyiraman Manual pada Kebun Jeruk Limau di Ciberes Subang*", font_size=11, bold=True)
    
    p_meta = doc.add_paragraph()
    p_meta.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_meta.paragraph_format.space_before = Pt(0)
    p_meta.paragraph_format.space_after = Pt(10)
    add_formatted_runs(p_meta, "Disusun oleh: Muhammad Al Qarnie (101032330043), Maheswara Ariq Athallah (101032300050), Daffa Hermansyah (101032330090)\nProgram Studi S1 Teknik Komputer | Fakultas Teknik Elektro | Universitas Telkom Bandung (2026)", font_size=9, bold=False)

    # 3. Context Box / Short Intro
    p_intro = doc.add_paragraph()
    p_intro.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_intro.paragraph_format.space_before = Pt(0)
    p_intro.paragraph_format.space_after = Pt(8)
    p_intro.paragraph_format.line_spacing = 1.15
    add_formatted_runs(p_intro, "Dokumen ini menyajikan komparasi komprehensif atas empat (4) konsep alternatif solusi rekayasa pada tahap Dokumen CD-3 (*Desain Rancangan Solusi*). Evaluasi ini disusun guna menjawab kendala fisik tapak kebun mitra Ciberes seluas ~3.000 m² (populasi 500–600 pohon, memanjang 100 meter, berparit sawah labil, ketiadaan listrik PLN/*off-grid*, dan kekeruhan sedimen sungai Ciberes) selaras dengan batasan rekayasa mutlak CD-2 (C-01 s.d. C-05) serta spesifikasi kuantitatif (S-01 s.d. S-14). Alternatif yang dievaluasi mencakup pendekatan otomatis penuh jaringan perpipaan tetes (Alternatif 1), robot penjelajah pematang parit berlengan artikulasi (Alternatif 2), tandon pasif gravitasi (Alternatif 3), dan gerobak dorong irigasi-logistik tepat guna multifungsi (Alternatif 4).", font_size=9.5)

    # 4. Main Comparison Table (Table 1)
    p_cap1 = doc.add_paragraph()
    p_cap1.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p_cap1.paragraph_format.space_before = Pt(4)
    p_cap1.paragraph_format.space_after = Pt(4)
    p_cap1.paragraph_format.keep_with_next = True
    add_formatted_runs(p_cap1, "Tabel 1. Perbandingan Menyeluruh Konsep, Mekanisme Kerja, Kelebihan, dan Kekurangan 4 Alternatif Solusi Rekayasa", font_size=10, bold=True)

    t1_headers = [
        "Alternatif Solusi & Arsitektur",
        "Prinsip Kerja & Mekanisme Operasional",
        "Kelebihan (Kekuatan Teknis & Lapangan)",
        "Kekurangan (Kelemahan & Risiko Rekayasa)",
        "Estimasi Anggaran & Status Pemilihan"
    ]

    t1_data = [
        [
            "ALTERNATIF 1:\n\n*Smart Multi-Zone Micro-Drip Irrigation Network*\n\n(Jaringan Mikroirigasi Perpipaan Cerdas Otomatis Multi-Zonasi)",
            "• Air disedot dari Sungai Ciberes via pompa diafragma elektrik DC 12V hemat daya (80 Watt).\n"
            "• Melewati stasiun filtrasi cakram ganda (*disc filter*) 120 mesh (pori 130 μm) dengan katup *manual flush* pembuang lumpur.\n"
            "• Ditransmisikan melalui pipa utama PE 1 inci menuju pipa lateral PE 16 mm di bedengan pohon.\n"
            "• Setiap pohon dipasangi 2 unit *Pressure Compensating (PC) Dripper* (debit tetap 8 L/jam x 2 = 16 L/jam per pohon).\n"
            "• Katup selenoid membuka selama tepat 56 menit untuk memberikan dosis 15 L per pohon secara presisi.\n"
            "• Dikendalikan mikrokontroler ESP32 terprogram FSM bertenaga surya 100 Wp & baterai LiFePO4 12V 30Ah.",
            
            "1. Efisiensi Air Tertinggi (ηa >= 90–95%):\n"
            "Air langsung meresap ke rizosfer perakaran aktif tanpa terbuang ke parit atau menguap di kanopi.\n\n"
            "2. Keseragaman Sangat Presisi (CU >= 88–92%):\n"
            "Membran silikon PC Dripper menjaga debit konstan 16 L/jam meski terdapat variasi tekanan fluida atau elevasi lahan parit.\n\n"
            "3. Penekanan Risiko Penyakit Jamur:\n"
            "Daun dan batang tidak basah, mencegah infeksi jamur upas dan busuk akar *Phytophthora nicotianae*.\n\n"
            "4. Konsumsi Daya Ultra Hemat (80 W):\n"
            "Baterai LiFePO4 bertahan hingga 4 siklus siram penuh (9–12 hari mendung kontinu tanpa sinar matahari).\n\n"
            "5. Eliminasi Beban Fisik Buruh Secara Penuh:\n"
            "Menggantikan 100% kerja fisik buruh angkut ember manual dan menghemat upah operasional hingga Rp48 juta/tahun.\n\n"
            "6. Modularitas Sangat Tinggi:\n"
            "Sangat mudah diperluas (*scalable*) dari petak uji (15–20 pohon) ke kebun penuh (600 pohon) tanpa rombak arsitektur.\n\n"
            "7. Keselamatan Kerja Listrik SELV:\n"
            "Operasi 12V DC aman dari bahaya sengatan listrik di parit sawah basah (standar IEC 60364-4-41).",
            
            "1. Pemeliharaan Saringan Berkala:\n"
            "Tabung saringan cakram 120 mesh perlu dibilas (*flushed*) berkala (1x per 2–4 pekan) untuk membuang akumulasi lumpur sungai Ciberes.\n\n"
            "2. Kerentanan Selang Terhadap Alat Penyiang:\n"
            "Selang lateral PE 16 mm di permukaan tanah berisiko terpotong saat penyiangan rumput/gulma manual dengan cangkul/sabit bila tidak ditata rapi.",
            
            "Biaya Purwarupa (Petak Uji):\n"
            "Rp4.300.000\n"
            "*(Patuh Plafon <= Rp5.000.000)*\n\n"
            "Proyeksi Kebun Penuh (600 Pohon):\n"
            "Rp17.400.000\n"
            "*(Patuh Plafon Mitra <= Rp18.000.000)*\n\n"
            "Periode Balik Modal (PP):\n"
            "14–16 Bulan\n\n"
            "STATUS AKHIR:\n"
            "★ SOLUSI TERPILIH ★\n"
            "(Peringkat 1 / Skor 4,525)\n"
            "Kategori: Otomatis Penuh"
        ],
        [
            "ALTERNATIF 2:\n\n*Tracked/4WD Straddle Ditch-Rover with Articulated Robotic Spray Arm*\n\n(Robot Penjelajah Pematang Parit & Lengan Robotik Terarah)",
            "• Wahana robot bergerak menggunakan sasis 4-roda bertapak lebar (4WD) atau roda rantai karet ganda (*rubber tracks/crawler*) yang melintas di atas pinggiran pematang bibir parit (*straddling the ditch*).\n"
            "• Membawa pompa hisap DC elektrik dengan pipa hisap vertikal fleksibel berfilter apung yang menjulur ke bawah menyedot air parit secara mandiri (tanpa perlu menarik selang dari sungai).\n"
            "• Dilengkapi sepasang lengan robotik bersendi (*2-DOF / 3-DOF articulated robotic arms*) di sisi kiri dan kanan.\n"
            "• Berjalan otonom dipandu sensor penjejak garis atau kawat batas di pematang.\n"
            "• Saat mendeteksi batang pohon via sensor ultrasonik/kamera pengenal, robot berhenti dan menggerakkan lengan robotik menjulurkan nosel semprot tepat ke bawah kanopi tajuk mengarah ke zona perakaran (radius 0,6 m), mengalirkan dosis air presisi.",
            
            "1. Akurasi Sasaran Daerah Akar Sangat Tinggi:\n"
            "Lengan robotik secara mekanis mendekatkan nosel tepat ke tanah perakaran di bawah tajuk kanopi, tidak membasahi daun atau batang atas sehingga mencegah jamur *Phytophthora*.\n\n"
            "2. Mobilitas Mandiri Tanpa Beban Seretan Selang:\n"
            "Menghisap air langsung dari air parit galian tanah di bawahnya, mengeliminasi kerepotan menyeret selang bertekanan sejauh 100 meter dari sungai.\n\n"
            "3. Traksi Luas Roda Rantai (Anti-Amblas):\n"
            "Roda rantai (*crawler tracks*) atau ban 4WD lebar membagi beban secara merata di atas permukaan tanah pematang bedengan.\n\n"
            "4. Otomasi Navigasi Modern:\n"
            "Beroperasi otomatis menyusuri parit memanjang 100 meter tanpa memerlukan pengawalan konstan operator buruh.",
            
            "1. Biaya Mekatronika Sangat Mahal (Melampaui Plafon):\n"
            "Pengadaan sasis crawler tahan air, 2 unit servo torsi tinggi lengan robotik, sensor pengenal pohon, mikrokontroler canggih, dan baterai kapasitas tinggi menguras biaya Rp7,5–8,5 Juta, melanggar batas pagu Capstone (Rp5.000.000).\n\n"
            "2. Risiko Keruntuhan Tanah Bibir Parit Sawah:\n"
            "Tanah bibir parit Ciberes gembur dan tanpa dinding semen; beban robot berbobot 25–35 kg rentan memicu tanah pematang longsor saat kondisi basah, mengakibatkan robot terguling ke dalam parit.\n\n"
            "3. Ketergantungan Pada Pengisian Air Parit:\n"
            "Parit tanah Ciberes tidak selalu berisi air; air parit harus terlebih dahulu disedot dari sungai menggunakan pompa Alkon bensin yang rawan panas berlebih (*overheating*).\n\n"
            "4. Konsumsi Arus Listrik Tinggi (> 250–350 Watt):\n"
            "Motor penggerak traksi crawler, aktuator lengan robotik, dan pompa hisap menuntut kapasitas baterai yang besar dan berat.",
            
            "Biaya Purwarupa (Petak Uji):\n"
            "Rp7.500.000 – Rp8.500.000\n"
            "*(Telak Melampaui Plafon Rp5 Juta)*\n\n"
            "Proyeksi Kebun Penuh (1–2 Unit):\n"
            "Rp26.000.000 – Rp32.000.000\n"
            "*(Melampaui Plafon Mitra Rp18 Juta)*\n\n"
            "Periode Balik Modal (PP):\n"
            "> 24 Bulan\n\n"
            "STATUS AKHIR:\n"
            "✕ DITOLAK ✕\n"
            "(Peringkat 4 / Skor 2,850)\n"
            "Kategori: Robotik Canggih"
        ],
        [
            "ALTERNATIF 3:\n\n*Distributed Header Tank with Gravity Manifold*\n\n(Sistem Irigasi Hibrida Berbasis Tangki Tandon Terdistribusi)",
            "• Pompa air sentrifugal DC bertenaga surya menyedot air dari sungai Ciberes pada siang hari saat matahari terik (10.00–14.00 WIB).\n"
            "• Air ditampung di tangki tandon polietilena (500–1.000 Liter) di atas menara penopang rangka setinggi 2–2,5 meter.\n"
            "• Penyiraman tanaman dilakukan pada waktu terpisah (sore atau pagi hari) memanfaatkan gaya gravitasi bumi murni.\n"
            "• Katup bola motorik (*motorized ball valve* DC 12V 5W) membuka selama 30–40 menit untuk menyalurkan air via selang berpori (*soaker hose*) atau manifold berlubang.",
            
            "1. Konsumsi Arus Sangat Hemat Saat Siram:\n"
            "Proses siram murni memanfaatkan gaya gravitasi bumi tanpa menyalakan pompa, energi baterai hanya terpakai 2–3 detik untuk memutar katup.\n\n"
            "2. Pemisahan Fase Pompa & Siram (*Decoupled*):\n"
            "Pompa bekerja langsung pada efisiensi puncak radiasi surya siang hari (*direct solar pumping*) dengan stres termal rendah.\n\n"
            "3. Tekanan Aliran Lembut & Aman Bocor:\n"
            "Tekanan hidrostatik rendah (0,02–0,025 MPa) mencegah sambungan pipa pecah dan tidak mengikis lapisan tanah perakaran.",
            
            "1. Fluktuasi Tekanan Hidrostatik (*Head Droop*):\n"
            "Seiring penurunan volume air di tandon, tekanan air turun drastis sehingga debit tetes di awal jauh lebih deras daripada di akhir; nilai keseragaman CU sulit mencapai target >= 85%.\n\n"
            "2. Beban Struktur Sipil Berat di Tanah Sawah:\n"
            "Menara penopang tangki seberat 500–1.000 kg rentan miring atau ambles di atas tanah sawah Ciberes yang gembur saat hujan.\n\n"
            "3. Skalabilitas Kebun Penuh Sangat Berat & Mahal:\n"
            "Untuk melayani 600 pohon kebun yang memerlukan pasokan 7.500–9.000 Liter air per siklus, dibutuhkan tandon penampung raksasa atau bak beton mahal yang melampaui anggaran mitra.",
            
            "Biaya Purwarupa (Petak Uji):\n"
            "Rp4.850.000\n"
            "*(Mendekati Plafon Rp5.000.000)*\n\n"
            "Proyeksi Kebun Penuh:\n"
            "Rp24.500.000 – Rp27.000.000\n"
            "*(Melampaui Plafon Mitra)*\n\n"
            "Periode Balik Modal (PP):\n"
            "20–22 Bulan\n\n"
            "STATUS AKHIR:\n"
            "✕ DITOLAK ✕\n"
            "(Peringkat 3 / Skor 3,475)\n"
            "Kategori: Pasif Gravitasi"
        ],
        [
            "ALTERNATIF 4:\n\n*Multipurpose Semi-Manual Irrigation & Orchard Utility Cart*\n\n(Wahana Gerobak Dorong Irigasi & Logistik Kebun Multifungsi)",
            "• Menggunakan rangka gerobak sorong ban tapak lebar (*pneumatic all-terrain tire*) dengan dudukan lepas-pasang (*detachable quick-release*).\n"
            "• Mengusung modul pompa diafragma DC 12V 80W, baterai LiFePO4 12V 20–30Ah dalam boks IP65, saringan cakram 120 mesh portabel, dan gulungan selang lentur (*hose reel*) 25 meter dengan tongkat semprot bertakar (*spray wand with digital flow meter*).\n"
            "• Dioperasikan semi-manual oleh 1 orang buruh: gerobak didorong ke jalur setapak parit, selang hisap dimasukkan ke air sungai/parit terdekat, lalu menyiram 10–15 pohon dalam radius selang dengan takaran presisi.\n"
            "• Bak angkut dapat difungsikan bergantian untuk mengangkut hasil panen buah jeruk limau (kapasitas 100–150 kg per ritase) atau jeriken pupuk cair fertigasi.",
            
            "1. Nilai Guna Multifungsi Sepanjang Tahun:\n"
            "Tidak menganggur saat tidak menyiram; di musim panen beralih fungsi menjadi alat angkut buah jeruk limau dari ujung kebun (100 m) dan sarana pemupukan/pestisida cair.\n\n"
            "2. Biaya Rancang Bangun Paling Terjangkau (CAPEX Terendah):\n"
            "Menggunakan komponen mekanik gerobak standar toko tani lokal; biaya purwarupa hanya berkisar Rp2,4 Juta (paling hemat dari semua opsi).\n\n"
            "3. Bebas Risiko Amblas di Lumpur Parit:\n"
            "Digerakkan dan diarahkan langsung oleh tenaga manusia sehingga tidak mengalami risiko selip roda (*wheel slip*) atau terperosok seperti robot otonom.\n\n"
            "4. Nol Risiko Kerusakan Pipa Akibat Cangkul:\n"
            "Tidak membutuhkan bentangan jaringan pipa permanen di atas bedengan, bebas dari bahaya terpotong alat penyiang gulma/sabit.\n\n"
            "5. Pengurangan Beban Fisik Buruh:\n"
            "Mengubah kerja berat memikul ember berulang kali (4 orang buruh) menjadi mendorong gerobak beroda aerodinamis oleh 1 orang buruh.\n\n"
            "6. Keselamatan Kerja Ekstra Rendah Aman (SELV 12V):\n"
            "Sistem elektrik DC 12V sepenuhnya aman dari risiko sengatan listrik di lingkungan pertanian basah.",
            
            "1. Masih Memerlukan Tenaga Kerja Manusia (Semi-Manual):\n"
            "Bukan sistem otomasi penuh; mitra tetap harus menugaskan 1 orang pekerja untuk mendorong gerobak dan mengarahkan nosel siram pohon demi pohon.\n\n"
            "2. Variabilitas Keseragaman Dosis (Human Error):\n"
            "Meskipun dilengkapi meteran air digital pada tongkat semprot, akurasi pemberian air 10–15 L per pohon tetap bergantung pada ketelitian dan kesabaran operator.\n\n"
            "3. Waktu Penyiraman Tetap Memakan Beberapa Jam:\n"
            "Penyiraman 500–600 pohon secara bertahap blok demi blok membutuhkan waktu 2,5–3,5 jam per siklus siram.\n\n"
            "4. Akses Pematang yang Sangat Sempit:\n"
            "Pada pematang parit sempit (< 40 cm), membutuhkan keahlian dan kehati-hatian operator dalam menjaga keseimbangan muatan gerobak.",
            
            "Biaya Purwarupa (Petak Uji):\n"
            "Rp2.450.000\n"
            "*(Sangat Patuh Plafon <= Rp5.000.000)*\n\n"
            "Proyeksi Kebun Penuh (1–2 Unit Lengkap):\n"
            "Rp4.800.000 – Rp5.500.000\n"
            "*(Sangat Hemat, Plafon Mitra <= Rp18 Juta)*\n\n"
            "Periode Balik Modal (PP):\n"
            "6–8 Bulan\n\n"
            "STATUS AKHIR:\n"
            "★ ALTERNATIF TERBAIK KEDUA ★\n"
            "(Peringkat 2 / Skor 4,225)\n"
            "Kategori: Tepat Guna Semi-Manual"
        ]
    ]

    col_widths = [Inches(1.8), Inches(2.0), Inches(2.5), Inches(2.5), Inches(1.5)]
    
    t1 = doc.add_table(rows=len(t1_data) + 1, cols=5)
    t1.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_full_grid(t1, color="808080", sz="4")
    
    # Header
    hdr = t1.rows[0]
    make_row_cant_split(hdr)
    make_row_header(hdr)
    for c_idx, cell in enumerate(hdr.cells):
        cell.width = col_widths[c_idx]
        cell.text = ""
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.line_spacing = 1.05
        p.paragraph_format.space_before = Pt(4)
        p.paragraph_format.space_after = Pt(4)
        add_formatted_runs(p, t1_headers[c_idx], font_size=9.5, bold=True)
        set_cell_background(cell, "1F497D") # Elegant Dark Blue Header
        for r in p.runs:
            r.font.color.rgb = RGBColor(255, 255, 255)
        set_cell_margins(cell, 100, 100, 100, 100)

    # Rows
    for r_idx, row_data in enumerate(t1_data):
        row = t1.rows[r_idx + 1]
        make_row_cant_split(row)
        is_selected = (r_idx == 0) # Alt 1 is selected
        is_runner_up = (r_idx == 3) # Alt 4 is runner up
        
        for c_idx, cell in enumerate(row.cells):
            cell.width = col_widths[c_idx]
            cell.text = ""
            p = cell.paragraphs[0]
            p.paragraph_format.line_spacing = 1.12
            p.paragraph_format.space_before = Pt(3)
            p.paragraph_format.space_after = Pt(3)
            
            if c_idx in [0, 4]:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            else:
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                
            bold_flag = (c_idx == 0)
            add_formatted_runs(p, row_data[c_idx], font_size=8.5, bold=bold_flag)
            
            # Subtle row tinting
            if is_selected:
                if c_idx == 4:
                    set_cell_background(cell, "D9EAD3") # Light Green for Selected
                else:
                    set_cell_background(cell, "F3F8F2") # Very light greenish tint
            elif is_runner_up:
                if c_idx == 4:
                    set_cell_background(cell, "FFF2CC") # Warm Yellow for Runner Up
                else:
                    set_cell_background(cell, "FFFCF5") # Subtle warm tint
            else:
                if c_idx == 4:
                    set_cell_background(cell, "F4CCCC") # Light Red for Rejected
                else:
                    set_cell_background(cell, "FFFFFF" if r_idx % 2 == 1 else "F9F9F9")
                    
            set_cell_margins(cell, 80, 80, 90, 90)

    # 5. Summary Pugh Matrix Table (Table 2)
    doc.add_paragraph().paragraph_format.space_after = Pt(8)
    
    p_cap2 = doc.add_paragraph()
    p_cap2.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p_cap2.paragraph_format.space_before = Pt(8)
    p_cap2.paragraph_format.space_after = Pt(4)
    p_cap2.paragraph_format.keep_with_next = True
    add_formatted_runs(p_cap2, "Tabel 2. Rangkuman Skor Kuantitatif Matriks Keputusan Rekayasa (Pugh Matrix Scoring 6 Kriteria)", font_size=10, bold=True)

    t2_headers = [
        "No", "Kriteria Evaluasi Terbobot", "Rujukan Dokumen CD-2", "Bobot (%)",
        "Alternatif 1:\nSmart Micro-Drip", "Alternatif 2:\nRobot Pematang & Lengan", "Alternatif 3:\nGravity Header Tank", "Alternatif 4:\nGerobak Multifungsi"
    ]
    t2_data = [
        ["1", "Keandalan Lingkungan Kebun & Proteksi IP65", "Batasan C-02, Spesifikasi S-05, S-07", "20%", "4,5  (0,90)", "2,5  (0,50)", "3,5  (0,70)", "4,5  (0,90)"],
        ["2", "Keseragaman Distribusi Air (CU >= 85%) & Efisiensi", "Spesifikasi S-01, S-02, S-04, S-11", "20%", "5,0  (1,00)", "4,5  (0,90)", "3,0  (0,60)", "3,5  (0,70)"],
        ["3", "Kemandirian Energi Off-Grid & Keamanan Listrik SELV", "Batasan C-01, C-04, Spesifikasi S-06, S-12", "15%", "4,5  (0,675)", "2,5  (0,375)", "5,0  (0,75)", "4,5  (0,675)"],
        ["4", "Kelayakan Finansial (BOM Purwarupa, Proyeksi Penuh, PP)", "Spesifikasi S-08, S-09, S-10", "20%", "4,5  (0,90)", "1,5  (0,30)", "3,5  (0,70)", "5,0  (1,00)"],
        ["5", "Kemudahan Operasional Operator & Pemeliharaan", "Spesifikasi S-13, S-14", "15%", "4,0  (0,60)", "2,5  (0,375)", "3,5  (0,525)", "4,0  (0,60)"],
        ["6", "Skalabilitas Desain Sistem dari Petak Uji ke Seluruh Kebun", "Batasan C-03", "10%", "4,5  (0,45)", "4,0  (0,40)", "2,0  (0,20)", "3,5  (0,35)"],
        ["", "TOTAL SKOR AKHIR TERBOBOT (SKALA 5,000)", "", "100%", "4,525", "2,850", "3,475", "4,225"],
        ["", "KEPUTUSAN EVALUASI & STATUS AKHIR", "", "-", "SOLUSI TERPILIH\n(Peringkat 1)", "DITOLAK\n(Peringkat 4)", "DITOLAK\n(Peringkat 3)", "OPSI UNGGULAN KEDUA\n(Peringkat 2)"]
    ]

    col_w2 = [Inches(0.4), Inches(2.2), Inches(1.8), Inches(0.6), Inches(1.3), Inches(1.2), Inches(1.3), Inches(1.4)]
    t2 = doc.add_table(rows=len(t2_data) + 1, cols=8)
    t2.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_full_grid(t2, color="808080", sz="4")

    hdr2 = t2.rows[0]
    make_row_cant_split(hdr2)
    make_row_header(hdr2)
    for c_idx, cell in enumerate(hdr2.cells):
        cell.width = col_w2[c_idx]
        cell.text = ""
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.line_spacing = 1.05
        p.paragraph_format.space_before = Pt(3)
        p.paragraph_format.space_after = Pt(3)
        add_formatted_runs(p, t2_headers[c_idx], font_size=8.5, bold=True)
        set_cell_background(cell, "366092")
        for r in p.runs:
            r.font.color.rgb = RGBColor(255, 255, 255)
        set_cell_margins(cell, 80, 80, 60, 60)

    for r_idx, row_data in enumerate(t2_data):
        row = t2.rows[r_idx + 1]
        make_row_cant_split(row)
        is_summary = (r_idx >= len(t2_data) - 2)
        for c_idx, cell in enumerate(row.cells):
            cell.width = col_w2[c_idx]
            cell.text = ""
            p = cell.paragraphs[0]
            p.paragraph_format.line_spacing = 1.05
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(2)
            
            if c_idx in [0, 2, 3] or is_summary:
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            else:
                p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                
            bold_flag = is_summary or (c_idx in [4, 7] and not is_summary)
            add_formatted_runs(p, row_data[c_idx], font_size=8.0, bold=bold_flag)
            
            if is_summary:
                if r_idx == len(t2_data) - 1:
                    if c_idx == 4:
                        set_cell_background(cell, "D9EAD3") # Green for Winner
                    elif c_idx == 7:
                        set_cell_background(cell, "FFF2CC") # Yellow for Runner Up
                    elif c_idx in [5, 6]:
                        set_cell_background(cell, "F4CCCC") # Red for Rejected
                    else:
                        set_cell_background(cell, "EAEAEA")
                else:
                    set_cell_background(cell, "EAEAEA")
            elif c_idx == 4:
                set_cell_background(cell, "F2F7FA")
            elif c_idx == 7:
                set_cell_background(cell, "FFFCF5")
            set_cell_margins(cell, 50, 50, 50, 50)

    # 6. Concluding Notes
    p_concl = doc.add_paragraph()
    p_concl.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_concl.paragraph_format.space_before = Pt(8)
    p_concl.paragraph_format.space_after = Pt(0)
    p_concl.paragraph_format.line_spacing = 1.15
    add_formatted_runs(p_concl, "Kesimpulan Analisis Rekayasa: Penataan ulang Alternatif 2 dengan mengadopsi konsep robot penjelajah pematang parit (sasis crawler/4WD) bersenjatakan lengan robotik terarah membuktikan pemodelan robotika pertanian yang jauh lebih realistis dan berdaya guna tinggi dalam menargetkan zona perakaran jeruk limau secara presisi tanpa membasahi daun. Namun demikian, tingginya kompleksitas mekatronika dan biaya purwarupa (Rp7,5–8,5 Juta) yang secara telak melampaui plafon belanja Capstone (Rp5.000.000) serta risiko keruntuhan tanah bibir parit sawah yang gembur menjadi dasar ilmiah kuat penolakan opsi ini. Dengan demikian, Alternatif 1 (Jaringan Mikroirigasi Tetes Otomatis Cerdas) tetap kokoh sebagai Solusi Terpilih Utama (Skor 4,525), diikuti Alternatif 4 (Gerobak Dorong Multifungsi) sebagai Opsi Unggulan Kedua Tepat Guna (Skor 4,225).", font_size=9.5)

    return doc

def main():
    catatan_dir = r"c:\Users\LENOVO\Documents\TA lulus\CD (Capstone Design)\catatan"
    draf_dir = r"c:\Users\LENOVO\Documents\TA lulus\CD (Capstone Design)\dokumen\draf\cd3"
    
    out_docx_catatan = os.path.join(catatan_dir, "Tabel_Perbandingan_Alternatif_Solusi.docx")
    out_docx_draf = os.path.join(draf_dir, "Tabel_Perbandingan_Alternatif_Solusi.docx")
    
    doc = create_document()
    doc.save(out_docx_catatan)
    doc.save(out_docx_draf)
    print(f"Created DOCX at:\n- {out_docx_catatan}\n- {out_docx_draf}")

if __name__ == "__main__":
    main()
