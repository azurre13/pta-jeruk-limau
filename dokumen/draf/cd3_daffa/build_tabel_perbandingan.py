# -*- coding: utf-8 -*-
"""
Membuat dokumen Tabel_Perbandingan_Alternatif_Solusi.docx terpisah di folder
dokumen/draf/cd3_daffa/ berbasis hasil membaca penuh 37 pustaka CD-3 (21 zonasi +
7 pembanding awal + 9 pustaka tambahan kajian robotika & adopsi surya), CD-1, CD-2,
dan keluaran numerik simulation_results.json.
"""

import os
import re
import json
import docx
from docx.shared import Inches, Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.enum.section import WD_ORIENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls
from bom_and_data import calc_bom_totals, calc_full_scale

def fmt_rp(val):
    return "Rp" + f"{val:,}".replace(",", ".")

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SIM_JSON = os.path.join(SCRIPT_DIR, "simulation_results.json")
OUT_DOCX = os.path.join(SCRIPT_DIR, "Tabel_Perbandingan_Alternatif_Solusi.docx")


def set_cell_bg(cell, hex_color):
    tcPr = cell._tc.get_or_add_tcPr()
    tcPr.append(parse_xml(f'<w:shd {nsdecls("w")} w:fill="{hex_color}"/>'))


def set_cell_margins(cell, top=75, bottom=75, left=105, right=105):
    tcPr = cell._tc.get_or_add_tcPr()
    tcPr.append(parse_xml(
        f'<w:tcMar {nsdecls("w")}>'
        f'<w:top w:w="{top}" w:type="dxa"/>'
        f'<w:bottom w:w="{bottom}" w:type="dxa"/>'
        f'<w:left w:w="{left}" w:type="dxa"/>'
        f'<w:right w:w="{right}" w:type="dxa"/>'
        f'</w:tcMar>'
    ))


def set_table_grid(table, color="94A3B8", sz="4"):
    tblPr = table._tbl.tblPr
    tblPr.append(parse_xml(
        f'<w:tblBorders {nsdecls("w")}>'
        f'<w:top w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:bottom w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:left w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:right w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:insideH w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'<w:insideV w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
        f'</w:tblBorders>'
    ))


def make_cant_split(row):
    row._tr.get_or_add_trPr().append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))


def make_header_row(row):
    row._tr.get_or_add_trPr().append(parse_xml(f'<w:tblHeader {nsdecls("w")}/>'))


def add_formatted_runs(p, text, font_size=9.5, bold=False, color=None):
    tokens = re.split(r"(\*\*[^*]+\*\*|\*[^*]+\*)", text)
    for tok in tokens:
        if not tok:
            continue
        is_b = bold
        is_i = False
        content = tok
        if tok.startswith("**") and tok.endswith("**"):
            is_b = True
            content = tok[2:-2]
        elif tok.startswith("*") and tok.endswith("*"):
            is_i = True
            content = tok[1:-1]
        r = p.add_run(content)
        r.font.name = "Times New Roman"
        r.font.size = Pt(font_size)
        r.font.bold = is_b
        r.font.italic = is_i
        if color:
            r.font.color.rgb = color


def add_title_block(doc):
    p1 = doc.add_paragraph()
    p1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p1.paragraph_format.space_before = Pt(0)
    p1.paragraph_format.space_after = Pt(2)
    r = p1.add_run("MATRIKS PERBANDINGAN KOMPREHENSIF ALTERNATIF SOLUSI & SIMULASI AWAL CD-3")
    r.font.name = "Times New Roman"
    r.font.size = Pt(14)
    r.font.bold = True
    r.font.color.rgb = RGBColor(15, 23, 42)

    p2 = doc.add_paragraph()
    p2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p2.paragraph_format.space_after = Pt(4)
    add_formatted_runs(
        p2,
        "Capstone Design S1 Teknik Komputer Universitas Telkom — Kasus Kebun Jeruk Limau Desa Ciberes, Subang",
        font_size=11,
        bold=True,
        color=RGBColor(30, 58, 138),
    )

    p3 = doc.add_paragraph()
    p3.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p3.paragraph_format.space_after = Pt(8)
    p3.paragraph_format.line_spacing = 1.15
    add_formatted_runs(
        p3,
        "Dokumen pendamping ini menyintesis hasil pembacaan penuh terhadap 37 pustaka utama (*full-text*) "
        "yang terbagi menjadi 21 rujukan rekayasa mikro-irigasi surya [Z-01 s.d. Z-21], 7 rujukan awal "
        "sistem pembanding [P-01 s.d. P-07], serta 9 pustaka tambahan kajian robotika kebun buah dan "
        "adopsi irigasi surya [G-02 s.d. G-10] dari folder referensi robotika tim (dengan [G-01] sepadan [P-02]), "
        "disandingkan dengan batasan desain CD-2 (*hard constraints* C-01 s.d. C-05 dan spesifikasi "
        "S-01 s.d. S-14: pagu purwarupa <= Rp5.000.000, proyeksi skala penuh <= Rp18.000.000). Skenario "
        "tata letak petak uji *20 m x 3 baris* (Baris 1 - Parit 1 - Baris 2 - Parit 2 - Baris 3 - Parit 3 "
        "beserta parit penghubung melintang) digunakan sebagai basis estimasi awal sebelum validasi "
        "pengukuran lapangan langsung pada survei kebun Ciberes.",
        font_size=10,
    )


def build_styled_table(doc, headers, rows, col_widths_in, col_aligns=None, highlight_col=None):
    table = doc.add_table(rows=len(rows) + 1, cols=len(headers))
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    set_table_grid(table)

    # Header
    hdr_row = table.rows[0]
    make_header_row(hdr_row)
    make_cant_split(hdr_row)
    for c_idx, title in enumerate(headers):
        cell = hdr_row.cells[c_idx]
        cell.width = Inches(col_widths_in[c_idx])
        cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        set_cell_bg(cell, "1E3A8A" if c_idx != highlight_col else "065F46")
        set_cell_margins(cell, 60, 60, 85, 85)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.05
        add_formatted_runs(p, title, font_size=9.2, bold=True, color=RGBColor(255, 255, 255))

    # Body
    for r_idx, row_data in enumerate(rows):
        row = table.rows[r_idx + 1]
        make_cant_split(row)
        base_bg = "F8FAFC" if r_idx % 2 == 1 else "FFFFFF"
        is_total = row_data[0].startswith("TOTAL") or row_data[0].startswith("PERINGKAT")
        for c_idx, text in enumerate(row_data):
            cell = row.cells[c_idx]
            cell.width = Inches(col_widths_in[c_idx])
            cell.vertical_alignment = WD_ALIGN_VERTICAL.TOP
            if is_total:
                set_cell_bg(cell, "DBEAFE" if c_idx != highlight_col else "D1FAE5")
            elif c_idx == highlight_col:
                set_cell_bg(cell, "ECFDF5" if r_idx % 2 == 0 else "D1FAE5")
            elif c_idx == 0:
                set_cell_bg(cell, "EFF6FF" if r_idx % 2 == 0 else "E2E8F0")
            else:
                set_cell_bg(cell, base_bg)
            set_cell_margins(cell, 45, 45, 80, 80)
            p = cell.paragraphs[0]
            align = WD_ALIGN_PARAGRAPH.LEFT
            if col_aligns and c_idx < len(col_aligns):
                align = col_aligns[c_idx]
            p.alignment = align
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.08
            is_b = (c_idx == 0) or is_total
            add_formatted_runs(p, text, font_size=8.4, bold=is_b, color=RGBColor(15, 23, 42))
    return table


def add_section_heading(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(7)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.keep_with_next = True
    add_formatted_runs(p, text, font_size=11, bold=True, color=RGBColor(30, 58, 138))
    return p


def main():
    with open(SIM_JSON, "r", encoding="utf-8") as f:
        sim = json.load(f)
    hyd = sim["hydraulics"]
    ene = sim["energy"]
    _, bom_proto_tot = calc_bom_totals()
    _, bom_full_tot = calc_full_scale()
    bom_proto_str = fmt_rp(bom_proto_tot)
    bom_full_str = fmt_rp(bom_full_tot)

    doc = docx.Document()
    sec = doc.sections[0]
    sec.orientation = WD_ORIENT.LANDSCAPE
    sec.page_width = Cm(29.7)
    sec.page_height = Cm(21.0)
    sec.top_margin = Cm(1.5)
    sec.bottom_margin = Cm(1.5)
    sec.left_margin = Cm(1.6)
    sec.right_margin = Cm(1.6)
    # Total lebar efektif = 29.7 - 3.2 = 26.5 cm (~10.43 in) -> pakai max ~10.2 in

    add_title_block(doc)

    # ==========================================================================
    # TABEL 1: PERBANDINGAN KOMPREHENSIF 4 ALTERNATIF
    # ==========================================================================
    add_section_heading(doc, "Tabel 1. Perbandingan Rekayasa Detail Empat Alternatif Solusi Irigasi Kebun Jeruk Limau")
    t1_headers = [
        "Aspek & Parameter Evaluasi",
        "Alt 1 (Terpilih): Mikro-Irigasi Tetes Terzonasi Mandiri Surya",
        "Alt 2: Wahana Robot Otonom Kebun (UGV AI/LiDAR & Straddle Ditch-Rover)",
        "Alt 3: Robot Penarik Selang 100 m, Pengangkang Kanal & Tambatan Fluida",
        "Alt 4: Tangki Elevasi Gravitasi / Pompa PV Semi-Manual",
    ]
    t1_rows = [
        [
            "Prinsip Kerja & Konfigurasi Utama",
            "Jaringan pipa tetap (PE 1 inci + lateral PE 16 mm) dengan 2x *PC Dripper* 8 L/jam per pohon, pompa DC 12 V surya, *disc filter*, katup bola bermotor (*MBV*) per baris/zona, dan kendali ESP32.",
            "Mencakup: (a) UGV AI beroda/*crawler* membawa tangki, LiDAR 360°/RTK-GPS/RGB-D + Jetson (*OrcBOT* 2x1,1x0,85 m), dan (b) konsep penjelajah pematang (*Straddle Ditch-Rover*) berpipa hisap parit apung + lengan 2-DOF/3-DOF (atau *pilot rover* ultrasonik/encoder) ke radius akar 0,5-0,8 m.",
            "Mesin penggulung penarik selang 120 m + pompa bensin 7 HP 23 m3/jam (*Elkaoud 2025*), robot heksapoda aktuator otot McKibben bertekanan fluida via selang (*Fairfield 2020*), atau pengangkang kanal diesel 30 kW + *gun* 10 kW (*CN115804333A*).",
            "Pompa PV mengangkat air sungai ke menara tandon 2-4 m lalu gravitasi tetes, atau pompa gerobak PV 50 Wp-20 Ah menyiram selang manual oleh operator (Nurwidiana 2022).",
        ],
        [
            "Basis Pustaka Ilmiah Full-Text",
            "Z-01..Z-21 (Dominguez-Nino 2019; Garcia 2020; Meriç 2025; Dafonte 2024; Lavanholi 2018; Hartung FAO 2018; Alex-Tronix OSTI; Lajara 2010).",
            "P-01 Xia 2023; P-03 Li 2025; P-04 Jia 2023; P-05 Gu 2026; P-06 Zhang 2026; G-03 Wu 2025; G-04 Gerdan Koc 2025 (*OrcBOT*); G-05 Gravalos 2019; G-06 Zhang 2019; G-07 Xue 2023; G-08 Wang 2025; G-09 Hassan 2021; G-10 Durga 2024.",
            "P-02 / G-01 Elkaoud 2025 (*Eng*); P-07 Paten CN115804333A; G-02 Fairfield 2020 (Tesis Heksapoda Selang); G-03 Wu 2025 (uji lumpur 35%).",
            "Z-02 FAO-Hartung 2018 (gravitasional & tandon); Z-03 Nurwidiana 2022 (gerobak PV 50 Wp bawang).",
        ],
        [
            "Sumber Daya, Emisi & Keselamatan (S-06, S-10, S-12)",
            "PLTS *off-grid* SELV 12,8 V DC (PV 100 Wp + LiFePO4 30 Ah); 0 g CO2/kWh; aman sentuh (IEC 60364-4-41); kotak IP65.",
            "Paket 48-60 V (*OrcBOT* 60 V langgar SELV <= 48 V) + beban 368,9 W kontinu butuh baterai **3.689 Wh** (DoD 80%) untuk otonomi 8 jam S-06; varian murah 12 V 12,8 Ah hanya cukup 2x10 mnt uji lab.",
            "Mesin bensin 7 HP (*Elkaoud*) / diesel 30 kW (*CN115804333A*) melanggar mutlak S-12 nol emisi; beban tarik selang di tanah basah menggandakan beban baterai listrik.",
            "PV 50-150 Wp tanpa BBM (S-12 terpenuhi); namun varian tandon menara tinggi berisiko roboh di tanah sawah labil & varian gerobak butuh angkat beban.",
        ],
        [
            "Kesesuaian Medan 3 Parit + Penghubung Melintang (+)",
            "Sangat tinggi: *mainline* & lateral PE mudah melintasi parit melintang (+) via jembatan pipa sederhana tanpa menghentikan penyiraman.",
            "Buruk: pada tanah basah 35% (*Wu 2025*), roda selip **10%** (0,38 m/s) & terbenam; *crawler* (selip **3%**) berisiko melongsorkan bibir parit tanah sawah gembur (25-35 kg) & celah parit (+) 0,5-0,6 m; drift belok ~1 m (*OrcBOT*) / UWB RMSE 0,93-1,12 m.",
            "Buruk: model Darcy-Weisbach selang 120 m (35 L/mnt, mu=0,65) memicu gaya seret datar **316-502 N** (selang 3/4-1 inci, massa 49,5-78,7 kg) atau rugi **20,38 bar** (1/2 inci); *CN115804333A* rawan jatuh (*die luo feng xian*) di parit (+).",
            "Sedang: gerobak pompa sulit melewati parit penghubung (+); selang manual tetap harus ditarik melompati 3 parit seperti kondisi eksisting.",
        ],
        [
            "Presisi Dosis (15 L/pohon, S-01) & Keseragaman CU (S-02, S-03)",
            "Sangat tinggi: *2x PC Dripper 8 L/jam* bertekanan >= 78,45 kPa menjaga *CU >= 88-92%*; umpan balik *flow meter* YF-S201 menakar tepat 15 L/pohon (56,25 menit).",
            "Defisit debit/durasi S-03: target 600 pohon @ 15 L dalam <= 4 jam butuh **46,9-53,6 L/mnt**; pompa mikro 5,11 L/mnt perlu **176 dtk/pohon (~30,2 jam)**; tangki ~50 kg habis tiap 2-3 pohon; *OrcBOT* menyemprot kabut daun 150-170 um, bukan 15 L akar.",
            "Buruk: *gun* menyebar radius 47,5-57 m (*Wdac*) s.d. 75 m sehingga air mengguyur tajuk (risiko *Phytophthora*) & parit; heksapoda *Fairfield 2020* belum memiliki uji lapangan maupun data CU.",
            "Rendah: tekanan tandon gravitasi turun seiring penurunan level air (*CU* jatuh di baris ujung), sementara gerobak manual bergantung ketelitian buruh.",
        ],
        [
            "Penanganan Lumpur Sungai Ciberes & Biofouling (S-13)",
            "Optimal: saringan hisap pra-pompa non-korosif + *disc filter* 120-150 mesh (bilas pada dP >= 70 kPa) + keran *end-flush* ujung lateral berkecepatan >= 0,6 m/s (Z-12, Z-15).",
            "Rentan & celah literatur: belum ada jurnal Q1/Q2 (2018-2026) yang menguji *open-ditch suction* berlumpur; air parit cepat surut merembes & pasir halus menyumbat pompa mikro/nosel tanpa pra-filter 120 mesh.",
            "Cukup pada *nozzle* besar *gun*, namun efisiensi air < 50%; gangguan gulungan selang (*hose-reel* macet) kerap memutus siklus; otot fluida *Fairfield* rentan partikel sedimen.",
            "Sedang: saringan dasar tandon mudah mengendapkan lumpur jika tidak dikuras, dan endapan halus tetap berpotensi menyumbat emiter bertekanan rendah (<0,3 bar).",
        ],
        [
            "Instrumentasi Kontrol, Katup & Sensor Tanah",
            "*Motorized Ball Valve* 0 W statis (hemat 99,9% energi katup vs selenoid NC); transduser P 0-5 bar (anti-dry-run & cek filter); sensor tanah *Capacitive v1.2* mod RC 1 MOhm + MOSFET.",
            "Varian AI butuh dual MCU STM32 + Jetson Xavier NX (95,62% mIoU, 32,69 FPS; *Xue 2023*) & sensor saja **$210-1.680** (*Wang 2025*); varian murah ESP32/HC-05 (*Hassan 2021*) & gantry (*Gravalos 2019*) belum teruji di kebun terbuka.",
            "Kendali RF/tombol lokal mesin atau hidraulik pasif; tidak terintegrasi sensor kelengasan tanah perakaran maupun umpan balik *flow meter* dosis 15 L.",
            "Umumnya hanya sakelar manual on/off pompa atau pelampung mekanis; belum memenuhi sistem kendali cerdas terotomatisasi.",
        ],
        [
            "Kemudahan Operasi Buruh (C-05) & Pemeliharaan",
            "Tinggi: otomatis via RTC DS3231 + tombol 1-sentuhan & 3 LED status; perawatan berkala cukup membilas *disc filter* dan membuka keran *end-flush*.",
            "Sangat rendah (gagal C-05): butuh pelatihan navigasi/ROS, pelat titian manual di tiap parit silang (+), pengamanan komponen sasis di lumpur, serta terhambat kapasitas teknis petani kecil (*Durga 2024*).",
            "Rendah: buruh harus menarik/menggulung selang 100-120 m antar-batang & parit, ditambah perawatan rutin mesin bensin/diesel (mengulang keluhan pompa Alkon eksisting).",
            "Sedang-Tinggi: sederhana bagi petani (Nurwidiana 2022), tetapi tidak meringankan tenaga penggulungan/pemindahan selang.",
        ],
        [
            "Biaya Purwarupa (S-08 <= Rp5 Jt) & Proyeksi Kebun Penuh (<= Rp18 Jt)",
            f"Memenuhi: purwarupa petak *20 m x 3 baris* (24 pohon) terhitung **{bom_proto_str}** (<= Rp5 juta); proyeksi 10 zona 600 pohon **{bom_full_str}** (<= Rp18 juta).",
            "Melampaui pagu: purwarupa *straddle/crawler* + lengan 2-DOF/3-DOF tim memakan **Rp7,5-8,5 juta** (kebun penuh Rp26-32 jt); UGV AI/LiDAR + baterai 3,69 kWh menelan **> Rp25-60+ juta**; belum ada BOM Q1/Q2 robot kebun <= Rp5-6 juta.",
            "Melampaui pagu: sistem rel/roda pengangkang & genset atau mesin penarik 7 HP + selang 120 m berkisar > Rp15-40 juta plus BBM operasional.",
            "Varian gerobak PV murah (~Rp2,7-4 juta) tetapi tetap manual; varian tandon 8-10 m3 + menara pondasi cor di tanah sawah membutuhkan > Rp12-22 juta.",
        ],
        [
            "Ringkasan Kesesuaian & Risiko Kegagalan Dominan",
            "**SANGAT LAYAK (TERPILIH)**: risiko penyumbatan *dripper* & penyimpangan ADC sensor tanah dapat dimitigasi sejak desain; siap diuji pasca-survei Ciberes.",
            "**TIDAK LAYAK**: walau lengan akar menarik secara konsep, gagal di selip tanah basah 35% & longsor parit (+), *open-ditch suction* cepat surut, durasi >10-30 jam, baterai 3,69 kWh, & biaya over-budget S-08.",
            "**TIDAK LAYAK**: gaya seret selang 316-502 N / rugi 20,38 bar, gagal di parit silang (+), emisi BBM melanggar S-12, serta membasahi tajuk jeruk.",
            "**KURANG OPTIMAL**: tandon mahal & tekanan tidak konstan; gerobak PV tidak menyelesaikan otomatisasi maupun target dosis S-01.",
        ],
    ]
    t1_widths = [1.55, 2.35, 2.15, 2.15, 2.00]  # total 10.20 in
    build_styled_table(doc, t1_headers, t1_rows, t1_widths, highlight_col=1)

    doc.add_page_break()

    # ==========================================================================
    # TABEL 2: PUGH WEIGHTED DECISION MATRIX
    # ==========================================================================
    add_section_heading(doc, "Tabel 2. Matriks Keputusan Tertimbang (Weighted Decision Matrix) Berbasis CD-2")
    # Hitung eksak dalam Python:
    weights = [0.25, 0.20, 0.25, 0.15, 0.10, 0.05]
    # Alt 1, Alt 2, Alt 3, Alt 4 scores (skala 1-5)
    scores = [
        ("K1. Presisi Dosis (S-01: 15 L) & Keseragaman CU >= 85% (S-02)", 25, [5, 2, 1, 3],
         "Alt 1 pakai 2x PC Dripper + flow meter; Alt 2 defisit debit/waktu S-03 (>10-30 jam); Alt 3 gun menyebar ke tajuk."),
        ("K2. Kesesuaian Catu Off-Grid (S-06) & Topografi Parit '+' Kebun", 20, [5, 2, 2, 3],
         "Alt 1 lintasi parit (+) & MBV 0 W; Alt 2 selip 10% di lumpur 35%/butuh 3,69 kWh; Alt 3 seret selang 316-502 N."),
        [
            "K3. Kepatuhan Pagu Biaya (S-08: <=Rp5 Jt & <=Rp18 Jt) + Skalabilitas",
            25,
            [5, 1, 2, 3],
            f"Alt 1 masuk pagu {bom_proto_str} & {bom_full_str}; Alt 2 straddle/crawler Rp7,5-8,5 jt s.d. AI >Rp25-60 jt.",
        ],
        ("K4. Ketahanan Air Sungai Berlumpur (S-13) & Keandalan Mekanis", 15, [4, 2, 3, 3],
         "Alt 1 pra-filter+disc 120 mesh+flush; Alt 2 hisap parit cepat surut & tanpa bukti Q1/Q2 tahan lumpur."),
        ("K5. Kemudahan Operasi & Rawat oleh Buruh Kebun (C-05, S-11)", 10, [4, 1, 2, 4],
         "Alt 1 tombol 1-sentuhan + LED; Alt 2/3 bebani buruh navigasi, titian parit (+), gulung selang/servis BBM."),
        ("K6. Dampak Lingkungan (S-12: 0 g/kWh) & Keamanan SELV (S-10)", 5, [5, 3, 1, 4],
         "Alt 1 full PLTS 12 V SELV IP65; Alt 2 48-60 V berisiko di basah; Alt 3 pakai bensin 7 HP / diesel 30 kW."),
    ]
    t2_rows = []
    totals = [0.0, 0.0, 0.0, 0.0]
    for label, w_pct, sc, note in scores:
        w = w_pct / 100.0
        cells = [label, f"{w_pct}%"]
        for i in range(4):
            contrib = w * sc[i]
            totals[i] += contrib
            cells.append(f"{sc[i]} ({contrib:.2f})")
        cells.append(note)
        t2_rows.append(cells)

    t2_rows.append([
        "TOTAL SKOR TERTIMBANG (Skala Maks 5,00)", "100%",
        f"{totals[0]:.2f}", f"{totals[1]:.2f}", f"{totals[2]:.2f}", f"{totals[3]:.2f}",
        "Alt 1 unggul signifikan (+1,60 poin di atas peringkat 2).",
    ])
    t2_rows.append([
        "PERINGKAT KELAYAKAN IMPLEMENTASI", "-",
        "Peringkat 1 (DIPILIH)", "Peringkat 4 (Ditolak)", "Peringkat 3 (Ditolak)", "Peringkat 2 (Cadangan)",
        "Konsisten memenuhi seluruh hard constraints C-01 s.d. C-05.",
    ])
    t2_headers = [
        "Kriteria Evaluasi (Skala 1 = Sangat Buruk s.d. 5 = Sangat Baik)",
        "Bobot",
        "Alt 1\n(Tetes Surya)",
        "Alt 2\n(Robot/UGV)",
        "Alt 3\n(Selang/Gun)",
        "Alt 4\n(Tandon/PV)",
        "Justifikasi Kuantitatif Penilaian",
    ]
    t2_widths = [2.45, 0.65, 1.05, 1.05, 1.05, 1.05, 2.90]
    t2_aligns = [WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER,
                 WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT]
    build_styled_table(doc, t2_headers, t2_rows, t2_widths, col_aligns=t2_aligns, highlight_col=2)

    # ==========================================================================
    # TABEL 3: HASIL SIMULASI AWAL HIDROLIKA & ENERGI (CLO3 LEVEL 4)
    # ==========================================================================
    add_section_heading(doc, "Tabel 3. Ringkasan Keluaran Simulasi Awal Hidrolika (Darcy-Weisbach) & Neraca Energi PV-LiFePO4")
    t3_headers = [
        "Skenario Operasi Petak Uji (Basis Estimasi Pra-Survei 20 m x 3 Baris)",
        "Debit Total\n(L/jam | L/mnt)",
        "Kecepatan\nMain | Lat (m/s)",
        "Tekanan Pompa\nBersih | Bilas (bar)",
        "Energi Siklus\n(Wh)",
        "Keterangan Teknis & Kepatuhan Ambang Literatur",
    ]
    t3_rows = []
    for c in hyd["configs"]:
        e_txt = "-"
        if c["trees"] == 8:
            e_txt = f"{round(ene['e_cycle_3zone_mbv_wh']/3.0, 1)} Wh/zona"
        elif c["trees"] == 24:
            e_txt = f"{ene['e_cycle_simul_mbv_wh']} Wh (serentak)\nvs {ene['e_cycle_3zone_mbv_wh']} Wh (3 zona)"
        ket = (
            f"Memenuhi batas scouring endapan v >= 0,60 m/s ({c['passes_scour_06ms']}). "
            if c["trees"] == 0 else
            f"Tekanan emitter terjaga >= 0,785 bar (78,45 kPa); butuh flush berkala (v = {c['v_lat_inlet_ms']:.2f} < 0,60 m/s)."
            if not c["passes_scour_06ms"] else
            f"Menjangkau C-03 (20 pohon/1 lajur 25 m); kecepatan masuk {c['v_lat_inlet_ms']:.2f} >= 0,60 m/s."
        )
        t3_rows.append([
            c["name"],
            f"{c['Q_L_h']:.1f} | {c['Q_L_min']:.2f}",
            f"{c['v_main_ms']:.3f} | {c['v_lat_inlet_ms']:.3f}",
            f"{c['P_pump_clean_bar']:.2f} | {c['P_pump_dirty_filter_bar']:.2f}",
            e_txt,
            ket,
        ])
    t3_rows.append([
        "Efisiensi Katup MBV (0 W Statis) vs Selenoid NC (12 W)",
        "-", "-", "-",
        f"0,033 vs {ene['e_valve_nc_wh']} Wh",
        f"Penghematan energi katup {ene['valve_saving_pct']:.1f}% + baterai LiFePO4 30Ah bertahan {ene['days_autonomy_3d_interval_simul']} hari ({ene['cycles_autonomy_simul_mbv']} siklus serentak).",
    ])
    t3_widths = [2.45, 1.15, 1.25, 1.35, 1.30, 2.70]
    t3_aligns = [WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER,
                 WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT]
    build_styled_table(doc, t3_headers, t3_rows, t3_widths, col_aligns=t3_aligns, highlight_col=None)

    # ==========================================================================
    # TABEL 4: PERBAIKAN ARSITEKTUR USULAN REVISI VS DRAF AWAL TIM
    # ==========================================================================
    doc.add_page_break()
    add_section_heading(doc, "Tabel 4. Rekonsiliasi Teknis Desain Usulan Berbasis Pustaka Penuh vs Draf Awal Sebelumnya")
    t4_headers = [
        "No",
        "Komponen / Parameter Teknis",
        "Kondisi pada Draf Sebelumnya",
        "Perbaikan Spesifik pada Usulan CD-3 Ini",
        "Bukti Ilmiah & Dasar Batasan CD-2",
    ]
    t4_rows = [
        ["1", "Katup Kontrol Zona", "Selenoid Valve NC 12 V 12 W koil ditahan terus (~33,75 Wh/siklus 3 zona) dan berisiko panas/karat.", "*Motorized Ball Valve* 12 V PTFE + H-Bridge; hanya ditarik pulsa 5 detik saat ganti posisi -> **0 W statis** (hemat 99,9% energi katup).", "Z-04 (Alex-Tronix US DOE OSTI), Z-16 (Meriç SciRep 2025), Z-17 (Lajara dkk. 2010)."],
        ["2", "Pemantauan Tekanan & Sumbatan Filter", "Mengandalkan sensor arus pompa INA219 untuk mendeteksi anomali hidrolika secara tidak langsung.", "Transduser tekanan analog 0-5 bar di jalur *mainline*/hilir filter: deteksi langsung *dry-run*, pipa pecah, dan ambang bilas dP >= 70 kPa.", "Z-09 (PLoS ONE 2019), Z-16 (SciRep 2025), CD-2 S-13."],
        ["3", "Material Pompa & Pra-Filtrasi Sungai", "Hanya memasang saringan cakram 120 mesh di hilir pompa tanpa prasyarat material rumah pompa.", "Menetapkan pompa DC non-besi cor (polimer/baja tahan karat) + keranjang saringan hisap pra-pompa di sisi sungai Ciberes.", "Z-12 (Lavanholi 2018), Z-14 (SciRep 2025)."],
        ["4", "Pencegahan Endapan di Ujung Lateral", "Pipa lateral PE 16 mm ditutup mati (*end cap*) tanpa mekanisme penggelontoran sedimen halus.", "Penambahan 3 keran *end-flush* di ujung lateral untuk penggelontoran berkala mencapai kecepatan bilas v >= 0,60 m/s (418,4 L/jam pd v=0,80 m/s).", "Z-12 (Lavanholi 2018): ambang pengendapan 0,6 m/s."],
        ["5", "Keandalan Sensor Tanah Capacitive v1.2", "Dipakai langsung tanpa pengkondisian hardware sehingga rentan korosi, *drift* LDO ESP32, & pengisian parasitik.", "Modifikasi RC (+1 MOhm + 0,1 uF), *power-gating* MOSFET (hanya aktif saat ukur), catu LDO 3,3 V terpisah, & kalibrasi lokal tanah liat Ciberes.", "Z-01 (Dafonte 2024), Z-08 (Dominguez-Nino 2019), Z-21 (Sensors 2026)."],
        ["6", "Kepatuhan Pagu Biaya Purwarupa (S-08)", "Daftar belanja RAB mencantumkan angka melebihi batas (Rp5.960.000) dan tabel menyatu tidak konsisten.", f"Rancangan komponen terkendali sebesar **{bom_proto_str}** (<= Rp5.000.000 sesuai S-08 CD-2) untuk petak uji *20 m x 3 baris* dengan 3 zona MBV.", "CD-2 hard constraint C-02 & spesifikasi S-08."],
        ["7", "Tata Letak Uji & Referensi Pustaka", "Belum memodelkan 3 baris pohon sejajar 3 parit + parit melintang (+) serta memuat sitasi yang belum diunduh/bercampur abstrak.", "Memetakan konfigurasi awal *20 m x 3 baris* + lintasan penyeberangan parit (+); seluruh **37 pustaka** (termasuk 10 pustaka kajian robotika tim) telah dibaca *full-text*.", "Keterangan mitra pra-survei & 37 berkas penuh pustaka CD-3."],
        ["8", "Pendalaman Evaluasi Alternatif Robotik", "Penolakan robot pada draf awal baru bersifat kualitatif umum (UGV tangki & *straddle* Rp7,5-8,5 jt) tanpa bukti teramekanika basah/gaya seret selang.", "Integrasi bukti penuh: uji selip tanah basah 35% (10% roda vs 3% *crawler*), model seret selang 316-502 N, defisit debit 46,9-53,6 L/mnt vs 5,11 L/mnt, baterai 3,69 kWh, & celah *open-ditch suction*.", "G-02 s.d. G-10 (Wu 2025, Gerdan Koc 2025, Fairfield 2020, Wang 2025, Durga 2024) & Kajian Robotika tim."],
    ]
    t4_widths = [0.40, 1.85, 2.50, 3.25, 2.20]
    t4_aligns = [WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT,
                 WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT]
    build_styled_table(doc, t4_headers, t4_rows, t4_widths, col_aligns=t4_aligns, highlight_col=3)

    # Catatan kaki referensi ringkas
    p_ref = doc.add_paragraph()
    p_ref.paragraph_format.space_before = Pt(8)
    p_ref.paragraph_format.space_after = Pt(2)
    p_ref.paragraph_format.line_spacing = 1.1
    add_formatted_runs(
        p_ref,
        "Catatan Rujukan Terverifikasi: Kode [Z-01..Z-21] merujuk pada berkas teks penuh pada "
        "sumber/referensi jurnal/pustaka_cd3/solusi_terpilih_zonasi/, [P-01..P-07] merujuk pada "
        "sumber/referensi jurnal/pustaka_cd3/solusi_pembanding/, sedangkan [G-01..G-10] merujuk pada "
        "kajian & berkas penuh pada sumber/referensi jurnal/referensi_garnie_solusiRobot/ (dengan G-01 sepadan P-02 Elkaoud 2025). "
        "Rincian lengkap 41 sitasi IEEE tercantum pada Daftar Pustaka dalam CD3_Jeruk_Limau_Usulan.docx.",
        font_size=8.5,
        color=RGBColor(71, 85, 105),
    )

    doc.save(OUT_DOCX)
    print(f"Saved {OUT_DOCX}")


if __name__ == "__main__":
    main()
