# -*- coding: utf-8 -*-
"""
Script to build 'Tabel_Perbandingan_Alternatif_Solusi.docx' and export to PDF.
A clean, elegant, professional landscape document summarizing all 3 engineering
solution alternatives for CD-3, detailing their descriptions, working mechanisms,
technical pros (kelebihan), cons (kekurangan), cost estimations, and final decision status.
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
    add_formatted_runs(p_title, "TABEL PERBANDINGAN DAN ANALISIS ALTERNATIF SOLUSI REKAYASA (CD-3)", font_size=13, bold=True)
    
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
    add_formatted_runs(p_intro, "Dokumen ringkasan ini memuat komparasi teknis menyeluruh atas tiga (3) konsep alternatif usulan solusi rekayasa pada tahap Dokumen CD-3 (*Desain Rancangan Solusi*). Evaluasi ini disusun guna menjawab kendala fisik tapak kebun mitra Ciberes seluas ~3.000 m² (populasi 500–600 pohon, memanjang 100 meter, berparit sawah labil, ketiadaan listrik PLN/*off-grid*, dan kekeruhan sedimen sungai Ciberes) selaras dengan batasan rekayasa mutlak CD-2 (C-01 s.d. C-05) serta spesifikasi kuantitatif (S-01 s.d. S-14).", font_size=9.5)

    # 4. Main Comparison Table (Table 1)
    p_cap1 = doc.add_paragraph()
    p_cap1.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p_cap1.paragraph_format.space_before = Pt(4)
    p_cap1.paragraph_format.space_after = Pt(4)
    p_cap1.paragraph_format.keep_with_next = True
    add_formatted_runs(p_cap1, "Tabel 1. Perbandingan Menyeluruh Konsep, Mekanisme Kerja, Kelebihan, dan Kekurangan 3 Alternatif Solusi Rekayasa", font_size=10, bold=True)

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
            "5. Eliminasi Beban Kerja Fisik:\n"
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
            "★ TERPILIH ★\n"
            "(Peringkat 1 / Skor 4,525)"
        ],
        [
            "ALTERNATIF 2:\n\n*Automated Guided Sprinkler Cart / Robot*\n\n(Wahana Mekanis Penyiram Semi-Otonom Lajur Parit)",
            "• Menggunakan wahana mekanis/robot beroda tiga atau roda rantai (*crawler cart*) yang berjalan menyusuri lajur parit kebun.\n"
            "• Membawa pipa semprot (*boom spray*) dengan nosel semprot bertekanan ke arah kiri dan kanan bedengan.\n"
            "• Pasokan air disuplai melalui selang fleksibel panjang (*hose reel*) dari pompa sentrifugal stasioner di tepi sungai.\n"
            "• Robot bergerak lambat (0,05–0,1 m/s) dipandu kawat batas bawah tanah atau sensor penjejak.\n"
            "• Berhenti selama 2 menit per pohon saat mendeteksi pohon via sensor ultrasonik/limit switch, lalu bergerak maju kembali.",
            
            "1. Tanpa Jaringan Pipa Permanen Luas:\n"
            "Mengurangi pemasangan ratusan meter jaringan pipa tetap di atas lahan kebun mitra.\n\n"
            "2. Kebal Terhadap Butiran Pasir Kasar:\n"
            "Nosel semprot memiliki orifis lebih lebar (1,5–2 mm) sehingga lebih toleran terhadap butiran pasir sungai Ciberes tanpa risiko mampet total.\n\n"
            "3. Fleksibilitas Penempatan Lajur:\n"
            "Satu unit wahana dapat digunakan bergantian untuk beberapa parit jika dipindahkan manual oleh operator.",
            
            "1. Risiko Mekanikal Parit Sawah Ekstrem:\n"
            "Kontur parit sawah Ciberes gembur, becek, berlumpur tebal, dan tergenang air saat basah; roda robot sangat rentan selip (*wheel slip*) atau terperosok.\n\n"
            "2. Hambatan Beban Seretan Selang (*Hose Drag*):\n"
            "Menyeret selang bertekanan sepanjang 50–100 meter di atas lumpur membutuhkan torsi motor sangat masif dan rawan tersangkut di tunggul/batu.\n\n"
            "3. Konsumsi Listrik Sangat Boros (> 350–400 W):\n"
            "Motor traksi dan pompa bertekanan tinggi menuntut bank baterai dan panel surya yang sangat besar, berat, dan mahal.\n\n"
            "4. Rancang Bangun Prototipe Sangat Mahal:\n"
            "Biaya sasis kedap air IP65, motor torsi tinggi, roda gigi reduksi kedap air, dan kendali navigasi melampaui pagu mahasiswa.\n\n"
            "5. Risiko Jamur & Pemborosan Pupuk:\n"
            "Semprotan nosel membasahi daun dan pangkal batang secara liar, memicu jamur upas dan menghanyutkan butiran pupuk NPK ke parit.",
            
            "Biaya Purwarupa (Petak Uji):\n"
            "Rp5.800.000 – Rp6.500.000\n"
            "*(Melampaui Batas Rp5.000.000)*\n\n"
            "Proyeksi Kebun Penuh:\n"
            "Rp22.000.000 – Rp28.000.000\n"
            "*(Melampaui Batas Mitra)*\n\n"
            "Periode Balik Modal (PP):\n"
            "> 24 Bulan\n\n"
            "STATUS AKHIR:\n"
            "✕ DITOLAK ✕\n"
            "(Peringkat 3 / Skor 2,550)"
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
            "(Peringkat 2 / Skor 3,475)"
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
        "Alternatif 1: Smart Micro-Drip", "Alternatif 2: Sprinkler Cart Robot", "Alternatif 3: Gravity Header Tank"
    ]
    t2_data = [
        ["1", "Keandalan Lingkungan Kebun & Proteksi IP65", "Batasan C-02, Spesifikasi S-05, S-07", "20%", "4,5  (0,90)", "2,0  (0,40)", "3,5  (0,70)"],
        ["2", "Keseragaman Distribusi Air (CU >= 85%) & Efisiensi", "Spesifikasi S-01, S-02, S-04, S-11", "20%", "5,0  (1,00)", "3,5  (0,70)", "3,0  (0,60)"],
        ["3", "Kemandirian Energi Off-Grid & Keamanan Listrik SELV", "Batasan C-01, C-04, Spesifikasi S-06, S-12", "15%", "4,5  (0,675)", "2,5  (0,375)", "5,0  (0,75)"],
        ["4", "Kelayakan Finansial (BOM Purwarupa, Proyeksi Penuh, PP)", "Spesifikasi S-08, S-09, S-10", "20%", "4,5  (0,90)", "2,0  (0,40)", "3,5  (0,70)"],
        ["5", "Kemudahan Operasional Operator & Pemeliharaan", "Spesifikasi S-13, S-14", "15%", "4,0  (0,60)", "2,5  (0,375)", "3,5  (0,525)"],
        ["6", "Skalabilitas Desain Sistem dari Petak Uji ke Seluruh Kebun", "Batasan C-03", "10%", "4,5  (0,45)", "3,0  (0,30)", "2,0  (0,20)"],
        ["", "TOTAL SKOR AKHIR TERBOBOT (SKALA 5,000)", "", "100%", "4,525", "2,550", "3,475"],
        ["", "KEPUTUSAN EVALUASI & STATUS AKHIR", "", "-", "SOLUSI TERPILIH (Peringkat 1)", "DITOLAK (Peringkat 3)", "DITOLAK (Peringkat 2)"]
    ]

    col_w2 = [Inches(0.4), Inches(2.6), Inches(2.3), Inches(0.8), Inches(1.4), Inches(1.4), Inches(1.4)]
    t2 = doc.add_table(rows=len(t2_data) + 1, cols=7)
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
        add_formatted_runs(p, t2_headers[c_idx], font_size=9.0, bold=True)
        set_cell_background(cell, "366092")
        for r in p.runs:
            r.font.color.rgb = RGBColor(255, 255, 255)
        set_cell_margins(cell, 80, 80, 80, 80)

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
                
            bold_flag = is_summary or (c_idx == 4 and not is_summary)
            add_formatted_runs(p, row_data[c_idx], font_size=8.5, bold=bold_flag)
            
            if is_summary:
                if r_idx == len(t2_data) - 1:
                    set_cell_background(cell, "D9EAD3" if c_idx == 4 else ("F4CCCC" if c_idx in [5, 6] else "EAEAEA"))
                else:
                    set_cell_background(cell, "EAEAEA")
            elif c_idx == 4:
                set_cell_background(cell, "F2F7FA")
            set_cell_margins(cell, 50, 50, 60, 60)

    # 6. Concluding Notes
    p_concl = doc.add_paragraph()
    p_concl.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_concl.paragraph_format.space_before = Pt(8)
    p_concl.paragraph_format.space_after = Pt(0)
    p_concl.paragraph_format.line_spacing = 1.15
    add_formatted_runs(p_concl, "Kesimpulan Rekayasa: Alternatif 1 (Jaringan Mikroirigasi Perpipaan Cerdas Otomatis Multi-Zonasi) secara meyakinkan menjadi solusi terpilih dengan nilai 4,525. Solusi ini paling unggul dalam aspek efisiensi pemanfaatan air, stabilitas keseragaman dosis berbasis emiter PC, keandalan catu daya surya off-grid berdaya rendah, eliminasi 100% beban fisik petani manual, serta kepatuhan ketat terhadap anggaran belanja purwarupa (Rp4.300.000 <= Rp5.000.000) dan proyeksi kebun komersial (Rp17.400.000 <= Rp18.000.000). Rincian teknis lengkap, gambar blok diagram, pemodelan matematis Darcy-Weisbach, flowchart firmware FSM, dan Gantt Chart diuraikan pada Dokumen Resmi CD-3.", font_size=9.5)

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
