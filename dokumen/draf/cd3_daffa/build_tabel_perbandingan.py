# -*- coding: utf-8 -*-
"""
Membuat dokumen Tabel_Perbandingan_Alternatif_Solusi.docx terpisah di folder
dokumen/draf/cd3_daffa/ berbasis hasil membaca penuh 28 pustaka CD-3, CD-1, CD-2,
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
        "Dokumen pendamping ini menyintesis hasil pembacaan penuh terhadap 28 pustaka utama (*full-text*) "
        "yang terbagi menjadi 21 rujukan rekayasa mikro-irigasi surya [Z-01 s.d. Z-21] dan 7 rujukan "
        "sistem pembanding [P-01 s.d. P-07], disandingkan dengan batasan desain CD-2 (*hard constraints* C-01 "
        "s.d. C-05 dan spesifikasi S-01 s.d. S-14: pagu purwarupa <= Rp5.000.000, proyeksi skala penuh "
        "<= Rp18.000.000). Skenario tata letak petak uji *20 m x 3 baris* (Baris 1 - Parit 1 - Baris 2 - Parit 2 "
        "- Baris 3 - Parit 3 beserta parit penghubung melintang) digunakan sebagai basis estimasi awal sebelum "
        "validasi pengukuran lapangan langsung pada survei kebun Ciberes.",
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
        "Alt 2: Wahana Robot Otonom Kebun (UGV Beroda / Crawler)",
        "Alt 3: Robot Penarik Selang / Pengangkang Kanal + Gun Bensin/Diesel",
        "Alt 4: Tangki Elevasi Gravitasi / Pompa PV Semi-Manual",
    ]
    t1_rows = [
        [
            "Prinsip Kerja & Konfigurasi Utama",
            "Jaringan pipa tetap (PE 1 inci + lateral PE 16 mm) dengan 2x *PC Dripper* 8 L/jam per pohon, pompa DC 12 V surya, *disc filter*, katup bola bermotor (*MBV*) per baris/zona, dan kendali ESP32.",
            "Robot darat tak berawak (*Scout 2.0* / *crawler* 48 V) membawa tangki 30-50 L, pompa semprot, LiDAR/UWB untuk berpindah pohon demi pohon di sela bedengan.",
            "Mesin penggulung penarik selang 1,5 inci sepanjang 200 m + pompa 7 HP *gun* (Elkaoud 2025) atau sasis 4-roda pengangkang saluran + genset 30 kW + *gun* 10 kW (CN115804333A).",
            "Pompa PV mengangkat air sungai ke menara tandon 2-4 m lalu gravitasi tetes, atau pompa gerobak PV 50 Wp-20 Ah menyiram selang manual oleh operator (Nurwidiana 2022).",
        ],
        [
            "Basis Pustaka Ilmiah Full-Text",
            "Z-01..Z-21 (Dominguez-Nino 2019; Garcia 2020; Meriç 2025; Dafonte 2024; Lavanholi 2018; Hartung FAO 2018; Alex-Tronix OSTI; Lajara 2010).",
            "P-01 Xia 2023; P-03 Li 2025; P-04 Chen 2023 [Jia 2023] (*crawler* UWB); P-05 Gu 2026; P-06 Zhang 2026.",
            "P-02 Elkaoud 2025 (*Eng*); P-07 Paten CN115804333A (Henan Yungeng 2023).",
            "Z-02 FAO-Hartung 2018 (gravitasional & tandon); Z-03 Nurwidiana 2022 (gerobak PV 50 Wp bawang).",
        ],
        [
            "Sumber Daya, Emisi & Keselamatan (S-06, S-10, S-12)",
            "PLTS *off-grid* SELV 12,8 V DC (PV 100 Wp + LiFePO4 30 Ah); 0 g CO2/kWh; aman sentuh (IEC 60364-4-41); kotak IP65.",
            "Baterai 24-48 V + komputer AI (Jetson Orin); konsumsi propulsi 1.500 W (P-04) boros pada tanah liat lengket; risiko terbalik masuk parit.",
            "Bahan bakar bensin 7 HP / genset diesel 30 kW (melanggar S-12 nol emisi); kebisingan tinggi & komponen bertegangan/putar berisiko tinggi.",
            "PV 50-150 Wp tanpa BBM (S-12 terpenuhi); namun varian tandon menara tinggi berisiko roboh di tanah sawah labil & varian gerobak butuh angkat beban.",
        ],
        [
            "Kesesuaian Medan 3 Parit + Penghubung Melintang (+)",
            "Sangat tinggi: *mainline* & lateral PE mudah melintasi parit melintang (+) via jembatan pipa sederhana tanpa menghentikan penyiraman.",
            "Buruk: sasis dengan *ground clearance* 135 mm (P-01) & lebar ~0,7-1,0 m terhadang parit galian serta cabang rendah (~1 m); rentan selip UWB/NLOS (RMSE 0,93-1,12 m, P-04).",
            "Buruk-Sedang: Elkaoud butuh lintasan lurus bebas parit silang; CN115804333A hanya mengangkang kanal beton seragam dan berisiko jatuh (*die luo feng xian*) di persimpangan parit (+).",
            "Sedang: gerobak pompa sulit melewati parit penghubung (+); selang manual tetap harus ditarik melompati 3 parit seperti kondisi eksisting.",
        ],
        [
            "Presisi Dosis (15 L/pohon, S-01) & Keseragaman CU (S-02)",
            "Sangat tinggi: *2x PC Dripper 8 L/jam* bertekanan >= 78,45 kPa menjaga *CU >= 88-92%*; umpan balik *flow meter* YF-S201 menakar tepat 15 L/pohon (56,25 menit).",
            "Rendah-Sedang: tangki robot hanya cukup 2-3 pohon/isi ulang (45-50 kg); pengisian ulang bolak-balik membuat total waktu jauh melebihi S-03 (<= 2 jam).",
            "Buruk: *gun* menyebar radius 47-57 m (*Wdac*) sehingga air terbuang ke parit & daun jeruk, memicu patogen daun & tidak dapat menakar 15 L/pohon.",
            "Rendah: tekanan tandon gravitasi turun seiring penurunan level air (*CU* jatuh di baris ujung), sementara gerobak manual bergantung ketelitian buruh.",
        ],
        [
            "Penanganan Lumpur Sungai Ciberes & Biofouling (S-13)",
            "Optimal: saringan hisap pra-pompa non-korosif + *disc filter* 120-150 mesh (bilas pada dP >= 70 kPa) + keran *end-flush* ujung lateral berkecepatan >= 0,6 m/s (Z-12, Z-15).",
            "Rentan: pompa semprot tekanan tinggi cepat aus/tersumbat bila air parit berlumpur tanpa stasiun pra-filtrasi bertingkat di sisi sungai.",
            "Cukup pada *nozzle* besar *gun*, namun efisiensi air sangat rendah (< 50%) akibat evaporasi & limpasan ke parit.",
            "Sedang: saringan dasar tandon mudah mengendapkan lumpur jika tidak dikuras, dan endapan halus tetap berpotensi menyumbat emiter bertekanan rendah (< 0,3 bar).",
        ],
        [
            "Instrumentasi Kontrol, Katup & Sensor Tanah",
            "*Motorized Ball Valve* 0 W statis (hemat 99,9% energi katup vs selenoid NC); transduser P 0-5 bar (anti-dry-run & cek filter); sensor tanah *Capacitive v1.2* mod RC 1 MOhm + MOSFET.",
            "Kompleksitas terlalu tinggi (LiDAR, RTK-GNSS, kamera RGB-D, kontroler gerak) dengan suku cadang mahal & sulit dirawat buruh desa.",
            "Kendali berbasis *wireless* RF industri atau tombol lokal mesin; tidak terintegrasi sensor kelembapan akar maupun dosis volumetrik.",
            "Umumnya hanya sakelar manual on/off pompa atau pelampung mekanis; belum memenuhi sistem kendali cerdas terotomatisasi.",
        ],
        [
            "Kemudahan Operasi Buruh (C-05) & Pemeliharaan",
            "Tinggi: otomatis via RTC DS3231 + tombol 1-sentuhan & 3 LED status; perawatan berkala cukup membilas *disc filter* dan membuka keran *end-flush*.",
            "Sangat rendah (gagal C-05): operator kebun membutuhkan pelatihan navigasi ROS/telemetri & perbaikan baterai lithium tegangan tinggi.",
            "Rendah: perawatan mesin bensin/diesel rutin (oli, karburator, busi) tidak menyelesaikan masalah kerusakan pompa Alkon eksisting.",
            "Sedang-Tinggi: sederhana bagi petani (Nurwidiana 2022), tetapi tidak meringankan tenaga penggulungan/pemindahan selang.",
        ],
        [
            "Biaya Purwarupa (S-08 <= Rp5 Jt) & Proyeksi Kebun Penuh (<= Rp18 Jt)",
            f"Memenuhi: purwarupa petak *20 m x 3 baris* (24 pohon) terhitung **{bom_proto_str}** (<= Rp5 juta); proyeksi 10 zona 600 pohon **{bom_full_str}** (<= Rp18 juta).",
            "Jauh melampaui pagu: komponen sasis UGV + LiDAR/RTK + motor torsi menelan > Rp25-60 juta bahkan untuk 1 unit purwarupa (gagal C-02/S-08).",
            "Melampaui pagu: sistem rel/roda pengangkang & genset atau mesin penarik 7 HP + selang 200 m berkisar > Rp15-40 juta.",
            "Varian gerobak PV murah (~Rp2,7-4 juta) tetapi tetap manual; varian tandon 8-10 m3 + menara pondasi cor di tanah sawah membutuhkan > Rp12-22 juta.",
        ],
        [
            "Ringkasan Kesesuaian & Risiko Kegagalan Dominan",
            "**SANGAT LAYAK (TERPILIH)**: risiko penyumbatan *dripper* & penyimpangan ADC sensor tanah dapat dimitigasi sejak desain; siap diuji pasca-survei Ciberes.",
            "**TIDAK LAYAK**: selip roda di tanah basah, tersangkut parit melintang (+) dan ranting 1 m, serta biaya >5x pagu C-02.",
            "**TIDAK LAYAK**: emisi & bising BBM melanggar S-12, menyiram tajuk memicu jamur, gagal lewati persimpangan parit (+).",
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
         "Alt 1 gunakan 2x PC Dripper + flow meter; Alt 3 gun menyebar air ke daun/parit."),
        ("K2. Kesesuaian Catu Off-Grid (S-06) & Topografi Parit '+' Kebun", 20, [5, 2, 2, 3],
         "Alt 1 lintasi parit melintang & hemat energi katup MBV 0 W; UGV & pengangkang terhambat parit."),
        [
            "K3. Kepatuhan Pagu Biaya (S-08: <=Rp5 Jt & <=Rp18 Jt) + Skalabilitas",
            25,
            [5, 1, 2, 3],
            f"Alt 1 masuk pagu {bom_proto_str} (purwarupa) & skalabel 10 zona ({bom_full_str}); Alt 2/3 over-budget.",
        ],
        ("K4. Ketahanan Air Sungai Berlumpur (S-13) & Keandalan Mekanis", 15, [4, 2, 3, 3],
         "Alt 1 padukan saringan hisap, disc filter 120 mesh (dP alarm), dan end-flush >= 0,6 m/s."),
        ("K5. Kemudahan Operasi & Rawat oleh Buruh Kebun (C-05, S-11)", 10, [4, 1, 2, 4],
         "Alt 1 pakai tombol 1-sentuhan + LED status; Alt 4 mudah tetapi tetap kerja fisik angkut/gulung."),
        ("K6. Dampak Lingkungan (S-12: 0 g/kWh) & Keamanan SELV (S-10)", 5, [5, 3, 1, 4],
         "Alt 1 full PLTS 12 V DC aman sentuh IP65; Alt 3 pakai mesin bensin/diesel beremisi."),
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
        "Alt 2\n(UGV Robot)",
        "Alt 3\n(Gun BBM)",
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
        ["7", "Tata Letak Uji & Referensi Pustaka", "Belum memodelkan 3 baris pohon sejajar 3 parit + parit melintang (+) serta memuat sitasi yang belum diunduh.", "Memetakan konfigurasi awal *20 m x 3 baris* + lintasan penyeberangan parit (+), dan seluruh 100% pustaka telah diunduh serta dibaca *full-text*.", "Keterangan mitra pra-survei & 28 berkas penuh pustaka CD-3."],
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
        "sumber/referensi jurnal/pustaka_cd3/solusi_terpilih_zonasi/, sedangkan [P-01..P-07] merujuk pada "
        "sumber/referensi jurnal/pustaka_cd3/solusi_pembanding/. Rincian lengkap sitasi IEEE tercantum "
        "pada Daftar Pustaka di dalam dokumen utama CD3_Jeruk_Limau_Usulan.docx.",
        font_size=8.5,
        color=RGBColor(71, 85, 105),
    )

    doc.save(OUT_DOCX)
    print(f"Saved {OUT_DOCX}")


if __name__ == "__main__":
    main()
