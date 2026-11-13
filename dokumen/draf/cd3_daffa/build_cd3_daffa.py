# -*- coding: utf-8 -*-
"""
Pembangkit Dokumen Draf CD-3: CD3_Jeruk_Limau_Usulan.docx
Lokasi: dokumen/draf/cd3_daffa/ (terpisah dari draf rekan tim di dokumen/draf/cd3/).

Mengacu ketat pada:
- Template resmi FTE-CD-3 -edited_PBD.docx (1.1, 1.2, 1.3, 1.4, Daftar Pustaka)
- Rubrik CLO3 & CLO4 PTA FTE Telkom University
- Data mitra & batasan desain CD-1 dan CD-2 (C-01..C-05, S-01..S-14)
- 37 pustaka teks penuh (full-text) terverifikasi [Z-01..Z-21, P-01..P-07, G-02..G-10] + 4 standar resmi (total 41 rujukan IEEE)
- Hasil simulasi numerik simulation_results.json dan bom_and_data.py
"""

import os
import re
import sys
import json
import argparse
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

from bom_and_data import (
    calc_bom_totals,
    calc_full_scale,
    RAB_SUPPORT,
)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(SCRIPT_DIR, "..", "..", ".."))
TEMPLATE_PATH = os.path.join(REPO_ROOT, "sumber", "template", "FTE-CD-3 -edited_PBD.docx")
ASSETS_DIR = os.path.join(SCRIPT_DIR, "assets")
SIM_JSON = os.path.join(SCRIPT_DIR, "simulation_results.json")
OUT_DOCX = os.path.join(SCRIPT_DIR, "CD3_Jeruk_Limau_Usulan.docx")


# ==============================================================================
# HELPER PEMFORMATAN WORD & OMML
# ==============================================================================
def set_cell_bg(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    tcPr.append(parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>'))


def set_cell_margins(cell, top=70, bottom=70, left=100, right=100):
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


def add_formatted_runs(p, text, font_name="Times New Roman", font_size=12, bold=False, color=None):
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
        r.font.name = font_name
        r.font.size = Pt(font_size)
        r.font.bold = is_b
        r.font.italic = is_i
        if color:
            r.font.color.rgb = color


def add_h1(doc, text, page_break=False):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(14)
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.line_spacing = 1.15
    p.paragraph_format.keep_with_next = True
    p.paragraph_format.page_break_before = page_break
    p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
    add_formatted_runs(p, text, font_size=13, bold=True, color=RGBColor(15, 23, 42))
    return p


def add_h2(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(11)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.15
    p.paragraph_format.keep_with_next = True
    p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
    add_formatted_runs(p, text, font_size=12, bold=True, color=RGBColor(30, 58, 138))
    return p


def add_h3(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(8)
    p.paragraph_format.space_after = Pt(3)
    p.paragraph_format.line_spacing = 1.15
    p.paragraph_format.keep_with_next = True
    p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
    add_formatted_runs(p, text, font_size=11.5, bold=True, color=RGBColor(15, 23, 42))
    return p


def add_body(doc, text, indent=True):
    p = doc.add_paragraph()
    p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(5)
    p.paragraph_format.line_spacing = 1.35
    if indent:
        p.paragraph_format.first_line_indent = Inches(0.35)
    add_formatted_runs(p, text, font_size=11.5, bold=False)
    return p


def add_bullet(doc, text):
    p = doc.add_paragraph()
    p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.left_indent = Inches(0.35)
    p.paragraph_format.first_line_indent = Inches(-0.18)
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(3.5)
    p.paragraph_format.line_spacing = 1.25
    add_formatted_runs(p, "•  " + text, font_size=11.5, bold=False)
    return p


def add_caption(doc, text, is_table=True):
    p = doc.add_paragraph()
    p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.keep_with_next = is_table
    p.paragraph_format.space_before = Pt(8 if is_table else 3)
    p.paragraph_format.space_after = Pt(3 if is_table else 8)
    p.paragraph_format.line_spacing = 1.15
    add_formatted_runs(p, text, font_size=10.5, bold=True, color=RGBColor(15, 23, 42))
    return p


def add_figure(doc, filename, caption, width_in=5.85):
    path = os.path.join(ASSETS_DIR, filename)
    p_img = doc.add_paragraph()
    p_img.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_img.paragraph_format.space_before = Pt(6)
    p_img.paragraph_format.space_after = Pt(2)
    p_img.paragraph_format.keep_with_next = True
    run = p_img.add_run()
    run.add_picture(path, width=Inches(width_in))
    add_caption(doc, caption, is_table=False)


def add_equation(doc, omml_str, eq_num_label):
    tbl = doc.add_table(rows=1, cols=2)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    r = tbl.rows[0]
    make_cant_split(r)
    c0, c1 = r.cells[0], r.cells[1]
    c0.width = Inches(5.3)
    c1.width = Inches(0.75)
    c0.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
    c1.vertical_alignment = WD_ALIGN_VERTICAL.CENTER

    p0 = c0.paragraphs[0]
    p0.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p0.paragraph_format.space_before = Pt(2)
    p0.paragraph_format.space_after = Pt(2)
    p0._element.append(parse_xml(omml_str))

    p1 = c1.paragraphs[0]
    p1.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p1.paragraph_format.space_before = Pt(2)
    p1.paragraph_format.space_after = Pt(2)
    add_formatted_runs(p1, f"({eq_num_label})", font_size=11)


def add_code_block(doc, code_lines):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    make_cant_split(tbl.rows[0])
    cell = tbl.rows[0].cells[0]
    cell.width = Inches(6.0)
    set_cell_bg(cell, "F8FAFC")
    set_cell_margins(cell, 90, 90, 120, 120)
    set_table_grid(tbl, color="CBD5E1", sz="4")
    p = cell.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.line_spacing = 1.04
    r = p.add_run("\n".join(code_lines))
    r.font.name = "Consolas"
    r.font.size = Pt(8.0)
    r.font.color.rgb = RGBColor(15, 23, 42)
    p_sp = doc.add_paragraph()
    p_sp.paragraph_format.space_after = Pt(4)


def add_table(doc, headers, rows, col_widths_in, col_aligns=None, highlight_col=None, font_size=8.8):
    tbl = doc.add_table(rows=len(rows) + 1, cols=len(headers))
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    set_table_grid(tbl)

    hdr = tbl.rows[0]
    make_header_row(hdr)
    make_cant_split(hdr)
    for ci, h_txt in enumerate(headers):
        cell = hdr.cells[ci]
        cell.width = Inches(col_widths_in[ci])
        cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
        set_cell_bg(cell, "1E3A8A" if ci != highlight_col else "065F46")
        set_cell_margins(cell, 70, 70, 75, 75)
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        p.paragraph_format.line_spacing = 1.05
        add_formatted_runs(p, h_txt, font_size=font_size, bold=True, color=RGBColor(255, 255, 255))

    for ri, row_data in enumerate(rows):
        row = tbl.rows[ri + 1]
        make_cant_split(row)
        is_total = str(row_data[0]).strip().upper().startswith(("TOTAL", "PERINGKAT"))
        for ci, val in enumerate(row_data):
            cell = row.cells[ci]
            cell.width = Inches(col_widths_in[ci])
            cell.vertical_alignment = WD_ALIGN_VERTICAL.TOP
            if is_total:
                set_cell_bg(cell, "DBEAFE" if ci != highlight_col else "D1FAE5")
            elif ci == highlight_col:
                set_cell_bg(cell, "ECFDF5" if ri % 2 == 0 else "D1FAE5")
            elif ci == 0:
                set_cell_bg(cell, "EFF6FF" if ri % 2 == 0 else "E2E8F0")
            else:
                set_cell_bg(cell, "F8FAFC" if ri % 2 == 1 else "FFFFFF")
            set_cell_margins(cell, 60, 60, 70, 70)
            p = cell.paragraphs[0]
            p.alignment = col_aligns[ci] if (col_aligns and ci < len(col_aligns)) else WD_ALIGN_PARAGRAPH.LEFT
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.12
            is_b = (ci == 0) or is_total
            add_formatted_runs(p, str(val), font_size=font_size - 0.3, bold=is_b, color=RGBColor(15, 23, 42))

    p_after = doc.add_paragraph()
    p_after.paragraph_format.space_before = Pt(0)
    p_after.paragraph_format.space_after = Pt(4)
    return tbl


def fmt_rp(val):
    return "Rp" + f"{val:,}".replace(",", ".")


# ==============================================================================
# OMML PERSAMAAN MATEMATIS RESMI
# ==============================================================================
OMML_DARCY = '''<m:oMathPara xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math">
  <m:oMath>
    <m:sSub><m:e><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>h</m:t></m:r></m:e><m:sub><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>f</m:t></m:r></m:sub></m:sSub>
    <m:r><m:t> = </m:t></m:r>
    <m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>f</m:t></m:r>
    <m:r><m:t> · </m:t></m:r>
    <m:f><m:num><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>L</m:t></m:r></m:num><m:den><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>D</m:t></m:r></m:den></m:f>
    <m:r><m:t> · </m:t></m:r>
    <m:f><m:num><m:sSup><m:e><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>v</m:t></m:r></m:e><m:sup><m:r><m:t>2</m:t></m:r></m:sup></m:sSup></m:num><m:den><m:r><m:t>2</m:t></m:r><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>g</m:t></m:r></m:den></m:f>
    <m:r><m:t> · </m:t></m:r>
    <m:sSub><m:e><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>F</m:t></m:r></m:e><m:sub><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>Chr</m:t></m:r></m:sub></m:sSub>
    <m:r><m:t> + </m:t></m:r>
    <m:r><m:t>Σ</m:t></m:r>
    <m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>K</m:t></m:r>
    <m:r><m:t> · </m:t></m:r>
    <m:f><m:num><m:sSup><m:e><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>v</m:t></m:r></m:e><m:sup><m:r><m:t>2</m:t></m:r></m:sup></m:sSup></m:num><m:den><m:r><m:t>2</m:t></m:r><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>g</m:t></m:r></m:den></m:f>
  </m:oMath>
</m:oMathPara>'''

OMML_TDH = '''<m:oMathPara xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math">
  <m:oMath>
    <m:sSub><m:e><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>P</m:t></m:r></m:e><m:sub><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>pompa</m:t></m:r></m:sub></m:sSub>
    <m:r><m:t> = </m:t></m:r>
    <m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>ρg</m:t></m:r>
    <m:d><m:dPr><m:begChr m:val="("/><m:endChr m:val=")"/></m:dPr><m:e>
      <m:r><m:t>Δ</m:t></m:r><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>z</m:t></m:r>
      <m:r><m:t> + </m:t></m:r>
      <m:sSub><m:e><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>h</m:t></m:r></m:e><m:sub><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>f,main</m:t></m:r></m:sub></m:sSub>
      <m:r><m:t> + </m:t></m:r>
      <m:sSub><m:e><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>h</m:t></m:r></m:e><m:sub><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>f,lat</m:t></m:r></m:sub></m:sSub>
    </m:e></m:d>
    <m:r><m:t> + Δ</m:t></m:r>
    <m:sSub><m:e><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>P</m:t></m:r></m:e><m:sub><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>filter</m:t></m:r></m:sub></m:sSub>
    <m:r><m:t> + </m:t></m:r>
    <m:sSub><m:e><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>P</m:t></m:r></m:e><m:sub><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>emitter</m:t></m:r></m:sub></m:sSub>
  </m:oMath>
</m:oMathPara>'''

OMML_TIME = '''<m:oMathPara xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math">
  <m:oMath>
    <m:sSub><m:e><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>t</m:t></m:r></m:e><m:sub><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>siram</m:t></m:r></m:sub></m:sSub>
    <m:r><m:t> = </m:t></m:r>
    <m:f>
      <m:num><m:sSub><m:e><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>V</m:t></m:r></m:e><m:sub><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>target</m:t></m:r></m:sub></m:sSub></m:num>
      <m:den><m:sSub><m:e><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>N</m:t></m:r></m:e><m:sub><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>e</m:t></m:r></m:sub></m:sSub><m:r><m:t> · </m:t></m:r><m:sSub><m:e><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>q</m:t></m:r></m:e><m:sub><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>e</m:t></m:r></m:sub></m:sSub></m:den>
    </m:f>
    <m:r><m:t> × 60 menit</m:t></m:r>
  </m:oMath>
</m:oMathPara>'''

OMML_PV = '''<m:oMathPara xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math">
  <m:oMath>
    <m:sSub><m:e><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>E</m:t></m:r></m:e><m:sub><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>surya</m:t></m:r></m:sub></m:sSub>
    <m:r><m:t> = </m:t></m:r>
    <m:sSub><m:e><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>P</m:t></m:r></m:e><m:sub><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>PV</m:t></m:r></m:sub></m:sSub>
    <m:r><m:t> · </m:t></m:r>
    <m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>PSH</m:t></m:r>
    <m:r><m:t> · </m:t></m:r>
    <m:d><m:dPr><m:begChr m:val="("/><m:endChr m:val=")"/></m:dPr><m:e><m:r><m:t>1 − </m:t></m:r><m:sSub><m:e><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>δ</m:t></m:r></m:e><m:sub><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>termal</m:t></m:r></m:sub></m:sSub></m:e></m:d>
    <m:r><m:t> · </m:t></m:r>
    <m:sSub><m:e><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>η</m:t></m:r></m:e><m:sub><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>MPPT+kabel</m:t></m:r></m:sub></m:sSub>
  </m:oMath>
</m:oMathPara>'''

OMML_ENERGY_CYCLE = '''<m:oMathPara xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math">
  <m:oMath>
    <m:sSub><m:e><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>E</m:t></m:r></m:e><m:sub><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>siklus</m:t></m:r></m:sub></m:sSub>
    <m:r><m:t> = </m:t></m:r>
    <m:sSub><m:e><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>P</m:t></m:r></m:e><m:sub><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>pompa</m:t></m:r></m:sub></m:sSub><m:sSub><m:e><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>t</m:t></m:r></m:e><m:sub><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>op</m:t></m:r></m:sub></m:sSub>
    <m:r><m:t> + 2</m:t></m:r><m:sSub><m:e><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>N</m:t></m:r></m:e><m:sub><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>z</m:t></m:r></m:sub></m:sSub><m:sSub><m:e><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>P</m:t></m:r></m:e><m:sub><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>pulsa</m:t></m:r></m:sub></m:sSub><m:sSub><m:e><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>t</m:t></m:r></m:e><m:sub><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>pulsa</m:t></m:r></m:sub></m:sSub>
    <m:r><m:t> + </m:t></m:r>
    <m:sSub><m:e><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>E</m:t></m:r></m:e><m:sub><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>kontrol+tidur</m:t></m:r></m:sub></m:sSub>
  </m:oMath>
</m:oMathPara>'''

OMML_AUTONOMY = '''<m:oMathPara xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math">
  <m:oMath>
    <m:sSub><m:e><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>N</m:t></m:r></m:e><m:sub><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>otonomi</m:t></m:r></m:sub></m:sSub>
    <m:r><m:t> = </m:t></m:r>
    <m:f>
      <m:num><m:sSub><m:e><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>V</m:t></m:r></m:e><m:sub><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>bat</m:t></m:r></m:sub></m:sSub><m:r><m:t> · </m:t></m:r><m:sSub><m:e><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>C</m:t></m:r></m:e><m:sub><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>bat</m:t></m:r></m:sub></m:sSub><m:r><m:t> · </m:t></m:r><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>DoD</m:t></m:r></m:num>
      <m:den><m:sSub><m:e><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>E</m:t></m:r></m:e><m:sub><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>siklus</m:t></m:r></m:sub></m:sSub></m:den>
    </m:f>
    <m:r><m:t> × </m:t></m:r>
    <m:sSub><m:e><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>I</m:t></m:r></m:e><m:sub><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>hari</m:t></m:r></m:sub></m:sSub>
  </m:oMath>
</m:oMathPara>'''


# ==============================================================================
# DAFTAR PUSTAKA TERVERIFIKASI PENUH (28 FULL-TEXT CD-3 + STANDAR RESMI CD-1/CD-2)
# ==============================================================================
IEEE_REFS = [
    'J. Dafonte, M. Á. González, and E. Comesaña, "Soil Water Status Monitoring System with Proximal Low-Cost Sensors and LoRa Technology for Smart Water Irrigation in Woody Crops," *Sensors*, vol. 24, no. 24, art. 8104, 2024, doi: 10.3390/s24248104.',
    'H. Hartung and L. Pluschke, *The Benefits and Risks of Solar-Powered Irrigation—A Global Overview*, Food and Agriculture Organization of the United Nations (FAO) and GIZ, Rome, Italy, 2018.',
    'N. Nurwidiana, W. Fatmawati, and A. Rifa\'i, "Perancangan Alat Penyiram Lahan Bawang Merah Berbasis Teknologi Solar Fotovoltaik," *Jurnal Teknologi Pertanian Andalas*, vol. 26, no. 1, pp. 61–70, Mar. 2022.',
    'Alex-Tronix, *Irrigation Valve Solenoid Energy Saver: Final Technical Report*, U.S. Department of Energy Grant No. DE-FG01-97EE15698, OSTI Technical Report, 1998.',
    'J. M. Domínguez-Niño, H. R. Bogena, J. A. Huisman, B. Schilling, and J. Casadesús, "On the Accuracy of Factory-Calibrated Low-Cost Soil Water Content Sensors," *Sensors*, vol. 19, no. 14, art. 3101, 2019, doi: 10.3390/s19143101.',
    'M. K. Meriç, "Implementation of a wireless sensor network for irrigation management in drip irrigation systems," *Scientific Reports*, vol. 15, art. 97303, 2025, doi: 10.1038/s41598-025-97303-w.',
    'L. García, L. Parra, J. M. Jimenez, J. Lloret, and P. Lorenz, "IoT-Based Smart Irrigation Systems: An Overview on the Recent Trends on Sensors and IoT Systems for Irrigation in Precision Agriculture," *Sensors*, vol. 20, no. 4, art. 1042, 2020, doi: 10.3390/s20041042.',
    'A. A. Abdelmoneim, C. M. Al Kalaany, G. Dragonetti, et al., "Comparative Analysis of Soil Moisture- and Weather-Based Irrigation Scheduling for Drip-Irrigated Lettuce Using Low-Cost Internet of Things Capacitive Sensors," *Sensors*, vol. 25, no. 5, art. 1568, 2025, doi: 10.3390/s25051568.',
    'R. Lajara, J. Alberola, and J. Pelegrí-Sebastiá, "A Solar Energy Powered Autonomous Wireless Actuator Node for Irrigation Systems," *Sensors*, vol. 11, no. 1, pp. 329–340, Dec. 2010, doi: 10.3390/s110100329.',
    'L. Parra, J. Rocher, L. García, J. Lloret, J. Tomás, et al., "Design of a WSN for Smart Irrigation in Citrus Plots with Fault-Tolerance and Energy-Saving Algorithms," *Network Protocols and Algorithms*, vol. 10, no. 2, pp. 95–115, 2018.',
    'O. K. Ogidan, S. D. Oluwagbayide, and T. O. Ale, "A Microcontroller-Based Irrigation Scheduling Using FAO Penman-Monteith Equation," *Turkish Journal of Agricultural Engineering Research*, vol. 4, no. 1, pp. 15–25, 2023, doi: 10.46592/turkager.1170630.',
    'Q. Zong, Z. Liu, and H. Liu, "Backwashing performance of self-cleaning screen filters in drip irrigation systems," *PLoS ONE*, vol. 14, no. 12, art. e0226354, 2019, doi: 10.1371/journal.pone.0226354.',
    'Z. Jin, L. Chen, Q. Li, et al., "Establishment of predictive models for head loss and filtration efficiency of pontoon mesh rotary filter based on dimension analysis," *Scientific Reports*, vol. 15, art. 87708, 2025, doi: 10.1038/s41598-025-87708-y.',
    'Y. S. Zakaria, S. Chen, T. A. Adongo, et al., "Soil-Specific Calibration and Integration of Low-Cost Capacitive Soil Moisture Sensors into a Solar-Powered Sensor Node," *Sensors*, vol. 26, no. 13, art. 3979, 2026, doi: 10.3390/s26133979.',
    'M. A. Abdelhamid, T. K. Abdelkader, H. A. A. Sayed, et al., "Design and evaluation of a solar powered smart irrigation system for sustainable urban agriculture," *Scientific Reports*, vol. 15, art. 94251, 2025, doi: 10.1038/s41598-025-94251-3.',
    'N. S. Abbas, M. S. Salim, and N. Sabri, "ASCD: Automatic sensing and control device for crop irrigation scheduling," *HardwareX*, vol. 18, art. e00523, 2024, doi: 10.1016/j.ohx.2024.e00523.',
    'S. Abba, J. W. Namkusong, J.-A. Lee, and M. L. Crespo, "Design and Performance Evaluation of a Low-Cost Autonomous Sensor Interface for a Smart IoT-Based Irrigation Monitoring and Control System," *Sensors*, vol. 19, no. 17, art. 3643, 2019, doi: 10.3390/s19173643.',
    'A. A. Farag, M. A. Abd El-Aziz, A. M. El-Husseiny, et al., "Effects of irrigation systems and water management strategies on soil chemical properties and citrus tree productivity in clayey soils," *Scientific Reports*, vol. 15, art. 19575, 2025, doi: 10.1038/s41598-025-19575-6.',
    'R. Lavanholi, F. C. Oliveira, A. P. de Camargo, and J. A. Frizzone, "Methodology to Evaluate Dripper Sensitivity to Clogging due to Solid Particles: An Assessment," *The Scientific World Journal*, vol. 2018, art. 7697458, 2018, doi: 10.1155/2018/7697458.',
    'V. B. Shinde and S. S. Wandre, "Solar photovoltaic water pumping system for irrigation: A review," *African Journal of Agricultural Research*, vol. 10, no. 22, pp. 2267–2273, May 2015, doi: 10.5897/AJAR2015.9879.',
    'A.-R. Bawa, A. K. Sunnu, and E. A. Sarsah, "Recent Advances in Solar-powered Photovoltaic Pumping Systems for Drip Irrigation," *iRASD Journal of Energy & Environment*, vol. 4, no. 2, pp. 112–132, 2023, doi: 10.52131/jee.2023.0402.0040.',
    'Y. Xia, X. Lei, J. Pan, L. Chen, Z. Zhang, and X. Lyu, "Research on orchard navigation method based on fusion of 3D SLAM and point cloud positioning," *Frontiers in Plant Science*, vol. 14, art. 1207742, 2023, doi: 10.3389/fpls.2023.1207742.',
    'N. Elkaoud, S. Ismail, R. Mahmoud, H. Taraby, S. Shang, D. Wang, and M. Rayan, "Efficient and Effective Irrigation Water Management Using Sprinkler Robot," *Eng*, vol. 6, no. 7, art. 138, Jun. 2025, doi: 10.3390/eng6070138.',
    'H. Li, K. Huang, Y. Sun, X. Lei, Q. Yuan, J. Zhang, and X. Lv, "An autonomous navigation method for orchard mobile robots based on octree 3D point cloud optimization," *Frontiers in Plant Science*, vol. 15, art. 1510683, 2025, doi: 10.3389/fpls.2024.1510683.',
    'L. Jia, Y. Wang, L. Ma, et al., "Integrated Positioning System of Kiwifruit Orchard Mobile Robot Based on UWB/LiDAR/ODOM," *Sensors*, vol. 23, no. 17, art. 7570, 2023, doi: 10.3390/s23177570.',
    'R. Gu, S. Luan, Y. Zhao, and S. Zhao, "Heterogeneous agricultural robots: a review of collaborative sensing and control, challenges and opportunities," *Frontiers in Plant Science*, vol. 17, art. 1878431, 2026, doi: 10.3389/fpls.2026.1878431.',
    'H.-W. Zhang, Y.-M. Qin, A.-Q. Wu, and X. Xi, "Ground Mobile Robots for High-Throughput Plant Phenotyping: A Review from the Closed-Loop Perspective of Perception, Decision, and Action," *Plants*, vol. 15, no. 8, art. 1218, 2026, doi: 10.3390/plants15081218.',
    'Z. Bai, C. Zhang, D. Sun, et al., "Agricultural Farmland Irrigation Robot, Control Assembly Thereof, and Irrigation Method Using Same (农田灌溉机器人、其用控制组件及利用其进行的灌溉方法)," China Patent Application CN115804333A (Applicant: Henan Yungeng Era Robot Technology Co., Ltd.), filed Dec. 23, 2022.',
    'R. G. Allen, L. S. Pereira, D. Raes, and M. Smith, *Crop Evapotranspiration: Guidelines for Computing Crop Water Requirements*, FAO Irrigation and Drainage Paper No. 56, Rome, 1998.',
    'International Electrotechnical Commission, *IEC 60364-4-41: Low-voltage electrical installations — Protection for safety — Protection against electric shock*, IEC Standard, Geneva, 2017.',
    'International Electrotechnical Commission, *IEC 60529: Degrees of protection provided by enclosures (IP Code)*, IEC Standard, Geneva, 2013.',
    'International Organization for Standardization, *ISO 9261: Agricultural irrigation equipment — Emitters and emitting pipe — Specification and test methods*, Geneva, 2004.',
    'K. Fairfield, *Design and Application of a Water Powered Irrigation Robot*, M.A.Sc. Thesis, Dept. of Mechanical Engineering, University of Victoria, Victoria, BC, Canada, 2020.',
    'T. Wu, D. Liu, and X. Li, "Designing Hybrid Mobility for Agricultural Robots: Performance Analysis of Wheeled and Tracked Systems in Variable Terrain," *Machines*, vol. 13, no. 7, art. 572, Jul. 2025, doi: 10.3390/machines13070572.',
    'D. Gerdan Koc, C. Koc, and M. Comakli, "AI-powered autonomous spraying robot for precision orchard applications," *Journal of Agricultural Engineering*, art. 1766, 2025, doi: 10.4081/jae.2025.1766.',
    'I. Gravalos, A. Avgousti, T. Gialamas, N. Alfieris, and G. Paschalidis, "A robotic irrigation system for urban gardening and agriculture," *Journal of Agricultural Engineering*, vol. L, art. 966, pp. 198–207, 2019, doi: 10.4081/jae.2019.966.',
    'Q. Zhang, M. Karkee, and A. Tabb, "The use of agricultural robots in orchard management," in *Robotics and Automation for Improving Agriculture*, J. Billingsley, Ed. Cambridge, UK: Burleigh Dodds Science Publishing, 2019, pp. 187–214, doi: 10.19103/AS.2019.0056.14.',
    'X. Xue, Q. Luo, M. Bu, Z. Li, S. Lyu, and S. Song, "Citrus Tree Canopy Segmentation of Orchard Spraying Robot Based on RGB-D Image and the Improved DeepLabv3+," *Agronomy*, vol. 13, no. 8, art. 2059, Aug. 2023, doi: 10.3390/agronomy13082059.',
    'Y. Wang, W. Jia, M. Ou, X. Wang, and X. Dong, "A Review of Orchard Canopy Perception Technologies for Variable-Rate Spraying," *Sensors*, vol. 25, no. 16, art. 4898, Aug. 2025, doi: 10.3390/s25164898.',
    'A. Hassan, R. M. Asif, A. U. Rehman, Z. Nishtar, M. K. A. Kaabar, and K. Afsar, "Design and development of an irrigation mobile robot," *IAES International Journal of Robotics and Automation (IJRA)*, vol. 10, no. 2, pp. 75–90, Jun. 2021, doi: 10.11591/ijra.v10i2.pp75-90.',
    'N. Durga, P. Schmitter, C. Ringler, S. Mishra, M. S. Magombeyi, et al., "Barriers to the uptake of solar-powered irrigation by smallholder farmers in sub-Saharan Africa: A review," *Energy Strategy Reviews*, vol. 51, art. 101294, Jan. 2024, doi: 10.1016/j.esr.2024.101294.',
]


def build_document(page_count_label="..."):
    with open(SIM_JSON, "r", encoding="utf-8") as f:
        sim = json.load(f)
    hyd = sim["hydraulics"]
    ene = sim["energy"]

    bom_rows, bom_proto_tot = calc_bom_totals()
    full_rows, full_tot = calc_full_scale()
    rab_support_tot = sum(x[3] for x in RAB_SUPPORT)
    rab_grand_tot = bom_proto_tot + rab_support_tot

    doc = docx.Document(TEMPLATE_PATH)

    # 1. Cover Template Update
    def set_cov_p(idx, txt, size, bold=False):
        p = doc.paragraphs[idx]
        p.text = txt
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for r in p.runs:
            r.font.name = "Times New Roman"
            r.font.size = Pt(size)
            r.font.bold = bold

    set_cov_p(0, "DOKUMEN CD-3", 16, True)
    set_cov_p(14, "ANALISIS PERMASALAHAN PENYIRAMAN MANUAL PADA KEBUN JERUK LIMAU DI CIBERES SUBANG", 14, True)
    set_cov_p(19, "Oleh :", 12, False)
    set_cov_p(21, "Muhammad Al Qarnie / 101032330043", 12, False)
    set_cov_p(22, "Maheswara Ariq Athallah / 101032300050", 12, False)
    set_cov_p(23, "Daffa Hermansyah / 101032330090", 12, False)
    set_cov_p(32, "PRODI S1 TEKNIK KOMPUTER", 14, True)
    set_cov_p(33, "FAKULTAS TEKNIK ELEKTRO", 14, True)
    set_cov_p(34, "UNIVERSITAS TELKOM", 14, True)
    set_cov_p(35, "BANDUNG", 14, True)
    set_cov_p(36, "2026", 14, True)

    # 2. T0 (Identitas Dokumen) — tanggal & jumlah halaman akurat (tanggal kosong sampai disahkan)
    t0 = doc.tables[0]
    t0.rows[0].cells[2].text = "Analisis Permasalahan Penyiraman Manual pada Kebun Jeruk Limau di Ciberes Subang"
    t0.rows[1].cells[2].text = "Desain Rancangan Solusi"
    t0.rows[2].cells[2].text = "FTE-CD-3"
    t0.rows[3].cells[2].text = "00 (Draf Awal Usulan)"
    t0.rows[4].cells[2].text = "-"
    t0.rows[5].cells[2].text = "Fakultas Teknik Elektro"
    t0.rows[6].cells[2].text = "S1 Teknik Komputer"
    t0.rows[7].cells[2].text = f"{page_count_label} halaman"

    for row in t0.rows:
        make_cant_split(row)
        for cell in row.cells:
            for p in cell.paragraphs:
                p.paragraph_format.line_spacing = 1.15
                p.paragraph_format.space_after = Pt(2)
                for r in p.runs:
                    r.font.name = "Times New Roman"
                    r.font.size = Pt(10)

    # 3. T1 (Data Pemeriksaan dan Persetujuan) — Pembimbing 2 & tanggal & tanda tangan dibiarkan kosong sesuai aturan
    t1 = doc.tables[1]
    t1.rows[1].cells[2].text = ": Muhammad Al Qarnie"
    t1.rows[2].cells[2].text = ": 101032330043"
    t1.rows[3].cells[2].text = ": Maheswara Ariq Athallah"
    t1.rows[4].cells[2].text = ": 101032300050"
    t1.rows[5].cells[2].text = ": Daffa Hermansyah"
    t1.rows[6].cells[2].text = ": 101032330090"
    t1.rows[7].cells[2].text = ": Dr. Agung Nugroho Jati, S.T., M.T."
    t1.rows[8].cells[2].text = ":"
    t1.rows[9].cells[2].text = ":"
    t1.rows[10].cells[2].text = ":"

    for row in t1.rows:
        make_cant_split(row)
        for cell in row.cells:
            for p in cell.paragraphs:
                p.paragraph_format.line_spacing = 1.15
                p.paragraph_format.space_after = Pt(2)
                for r in p.runs:
                    r.font.name = "Times New Roman"
                    r.font.size = Pt(10)

    # 4. T2 (Timeline Revisi Dokumen)
    t2 = doc.tables[2]
    for ri in range(2, len(t2.rows)):
        for ci in range(4):
            t2.rows[ri].cells[ci].text = ""
    t2.rows[1].cells[0].text = "00, Pra-Survei\n(Nov 2026)"
    t2.rows[1].cells[1].text = "Draf Usulan CD-3 Berbasis 37 Pustaka Penuh"
    t2.rows[1].cells[2].text = (
        f"Penyusunan lengkap alternatif solusi (4 kandidat termasuk pembaruan kajian robotika Straddle Ditch-Rover dan UGV/gun), matriks keputusan tertimbang berdasarkan CD-2, "
        f"desain rinci sistem mikro-irigasi tetes terzonasi surya SELV 12 V menggunakan Motorized Ball Valve 0 W statis, "
        f"transduser tekanan 0-5 bar, modifikasi RC+MOSFET sensor tanah Capacitive v1.2, keran end-flush v >= 0,6 m/s, "
        f"simulasi awal Darcy-Weisbach dan neraca energi PV-LiFePO4, tata letak awal petak uji 20 m x 3 baris (menunggu "
        f"verifikasi lapangan), serta BOM purwarupa {fmt_rp(bom_proto_tot)} (<= Rp5 juta) dan proyeksi penuh {fmt_rp(full_tot)}."
    )
    t2.rows[1].cells[3].text = "Seluruh Dokumen"
    for row in t2.rows:
        make_cant_split(row)
        for cell in row.cells:
            for p in cell.paragraphs:
                p.paragraph_format.line_spacing = 1.15
                p.paragraph_format.space_after = Pt(2)
                for r in p.runs:
                    r.font.name = "Times New Roman"
                    r.font.size = Pt(10)

    # 5. Bersihkan placeholder template dari Body[68] ke akhir dan jeda kosong Body[43..52] sebelum page break
    body = doc._element.body
    for idx in range(len(body) - 1, 67, -1):
        body[idx].getparent().remove(body[idx])
    for idx in range(52, 42, -1):
        body[idx].getparent().remove(body[idx])

    # ==========================================================================
    # 1.1 ALTERNATIF USULAN SOLUSI
    # ==========================================================================
    add_h1(doc, "1.1 Alternatif Usulan Solusi")
    add_body(
        doc,
        "Dokumen CD-3 (*Desain Rancangan Solusi*) ini merupakan kelanjutan langsung dari analisis kebutuhan dan akar "
        "permasalahan pada kebun jeruk limau mitra di Desa Ciberes, Subang (CD-1) serta penetapan batasan rekayasa mutlak "
        "(*hard constraints* C-01 s.d. C-05) dan 14 spesifikasi kuantitatif (S-01 s.d. S-14) pada dokumen CD-2. Berdasarkan "
        "fakta awal lapangan yang terdokumentasi di CD-1, kebun mitra seluas sekitar ~3.000 m² berisikan ~500–600 pohon jeruk "
        "limau (banyak di antaranya bertajuk rendah setinggi sekitar 1 m) dengan kontur tiga parit galian tanah memanjang "
        "sepanjang ~100 m beserta parit penghubung melintang (+). Air diambil dari saluran/sungai berjarak ~20,54 m dari tepi "
        "kebun menggunakan pompa berbahan bakar yang dimodifikasi ke LPG dan kerap mengalami gangguan mekanis, kemudian "
        "air ditimba dan diguyur secara manual oleh empat pekerja dengan upah Rp400.000 per siklus tiga hari sekali "
        "(mencapai skenario Rp48,7 juta/tahun) serta acuan dosis awal mitra minimal 15 Liter/pohon."
    )
    add_body(
        doc,
        "Guna memastikan rancangan tetap terukur sebelum pengukuran dimensi detail kebun mitra dilakukan pada survei "
        "lanjutan lapangan, petak uji purwarupa pada draf ini dimodelkan secara modular mengikuti skema awal mitra "
        "**20 m × 3 baris pohon** (pola *Baris 1 – Parit 1 – Baris 2 – Parit 2 – Baris 3 – Parit 3* beserta parit "
        "penghubung melintang, dengan estimasi awal 24 pohon), seraya menjaga kompatibilitas perpanjangan pipa menuju "
        "syarat C-03 CD-2 (15–20 pohon pada bentang operasional >= 25 m) dan batasan pagu belanja purwarupa "
        "maksimal Rp5.000.000 (S-08) serta skalabilitas menuju kebun penuh 500–600 pohon dengan proyeksi investasi "
        "<= Rp18.000.000. Berangkat dari penelaahan penuh (*full-text*) terhadap 37 referensi ilmiah dan paten utama "
        "[1]–[28], [33]–[41] (plus 4 standar teknis [29]–[32]), empat alternatif solusi dirumuskan sebagai ruang keputusan rekayasa."
    )

    add_h2(doc, "1.1.1 Alternatif 1: Sistem Mikro-Irigasi Tetes Terzonasi Mandiri Surya (Usulan Terpilih)")
    add_body(
        doc,
        "Alternatif 1 mengusulkan arsitektur perpipaan tertutup bertekanan rendah yang mendistribusikan air sungai "
        "Ciberes langsung ke zona perakaran aktif setiap pohon jeruk limau secara otomatis dan terukur. Konsep ini "
        "menyintesis praktik terbaik mikro-irigasi surya dan instrumentasi berbiaya hemat dari [1]–[21]: air dialirkan "
        "melalui saringan hisap non-korosif pra-pompa menuju pompa diafragma DC 12 V (material polimer/tahan korosi), "
        "melewati *disc filter* 120–150 mesh berfitur bilas lumpur, lalu diatur alirannya per baris/zona menggunakan "
        "*Motorized Ball Valve* (MBV) 12 V DC berdaya statis 0 W sebelum keluar melalui dua *Pressure Compensating (PC) "
        "Dripper* berdebit 8 L/jam per pohon (total 16 L/jam/pohon) pada radius tajuk 0,5–0,8 m."
    )
    add_body(
        doc,
        "Kelebihan utama Alternatif 1 meliputi: (1) efisiensi aplikasi tinggi serta bebas pembasahan daun sehingga menekan "
        "risiko jamur akar dan pangkal batang [18], (2) jaringan pipa PE fleksibel mudah dirutekan melintasi parit "
        "melintang (+), (3) penggunaan katup bola bermotor menghemat energi pegang katup hingga 99,9% dibandingkan selenoid "
        "*normally-closed* (NC) konvensional [4], [6], [9], dan (4) operasi *single-touch* berbasis RTC DS3231, *flow meter* "
        "YF-S201, transduser tekanan 0–5 bar, dan sensor tanah termodifikasi sangat bersahabat bagi buruh kebun (C-05). "
        "Kelemahan yang harus dimitigasi adalah kebutuhan pembilasan *disc filter* dan pembukaan keran *end-flush* di ujung "
        "lateral agar partikel lumpur halus sungai tidak mengendap di dalam pipa [12], [19]."
    )

    add_h2(doc, "1.1.2 Alternatif 2: Wahana Robot Bergerak Otonom & Straddle Ditch-Rover")
    add_body(
        doc,
        "Alternatif 2 mencakup wahana robot darat tak berawak (*Unmanned Ground Vehicle*/UGV) beroda atau perayap (*crawler*) "
        "komersial/riset [22], [24]–[27], [34]–[40], termasuk varian konseptual tim yaitu *Tracked/4WD Straddle Ditch-Rover* "
        "berlengan ganda 2-DOF/3-DOF (*dual articulated arm*) dengan penyedot parit apung (*floating ditch suction*). "
        "Konsep robot bergerak menyusuri barisan tanaman [22], [24], [35], [37]–[39] atau mengangkangi parit galian untuk "
        "menggantikan aktivitas pekerja mengguyur air langsung ke pangkal tiap pohon secara berurutan tanpa jaringan pipa distribusi."
    )
    add_body(
        doc,
        "Meskipun unggul dalam fleksibilitas navigasi pada lahan rata komersial [22], [24], [35], audit literatur penuh dan "
        "evaluasi rekayasa terukur membuktikan lima hambatan mendasar pada kondisi Ciberes dan spesifikasi CD-2: "
        "(1) **Kapasitas tangki & defisit debit (throughput)**: UGV tangki on-board sekelas *Scout 2.0* (*ground clearance* "
        "~135 mm, muatan ~50 kg) [22], [27] hanya membawa air untuk 2–3 pohon per pengisian ulang; jika memakai konsep "
        "*Straddle Ditch-Rover* berpompa DC 12 V 5,11 L/menit (~Rp7,5–8,5 juta purwarupa), dosis minimal 15 L/pohon memerlukan "
        "176,1 detik/pohon atau **30,19 jam kontinu** untuk 600 pohon (padahal S-03 menuntut debit total 46,9–53,6 L/menit untuk "
        "jendela kerja <= 3 jam/kegiatan), sedangkan prototipe *irrigation rover* berbiaya rendah [40] hanya berkapasitas demo "
        "mikro tanpa sertifikasi lapangan; "
        "(2) **Risiko mekanika tanah & parit silang (+)**: pada tanah lempung datar dengan kadar air 34,7–35,3% saja [34], roda "
        "masih mengalami *slip* 10% (0,38 m/s) dan rantai *crawler* mengalami *slip* 3% (0,36 m/s); apalagi jika sasis robot "
        "seberat 25–35 kg harus melintasi tebing galian tiga parit tanah basah dan penghubung melintang (+) serta kanopi ~1 m "
        "yang menimbulkan risiko longsor tepi parit (*bank collapse*), ketidakstabilan 3-DOF [36], serta error UWB/NLOS 0,93–1,12 m [25] "
        "atau *turn drift* ~1 m [35]; "
        "(3) **Defisit neraca energi baterai S-06**: beban propulsi dual-motor, pengendali, dan pompa pada operasi kontinu "
        "menuntut ~368,9 W (*crawler* komersial bahkan mencapai 48 V 1.500–2.100 W [25], [35]), atau sekitar 2.951 Wh untuk "
        "8 jam kerja (**3.689 Wh / 153,7 Ah @ 24 V** pada DoD 80%), jauh melampaui baterai kecil 12 V 12,8 Ah yang hanya "
        "bertahan ~2x10 menit uji demo; "
        "(4) **Kesenjangan bukti ilmiah (literature gap)**: penelaahan 10 referensi robotika [23], [33]–[41] tidak "
        "menemukan satu pun validasi Q1/Q2 untuk penyedotan parit tanah terbuka oleh rover pengangkang maupun navigasi magnetik/IMU "
        "tanpa LiDAR/RTK di kebun basah berkanopi rendah; serta "
        "(5) **Pelanggaran pagu biaya C-02**: modul persepsi saja menelan USD 210–1.680 untuk LiDAR, USD 252–840 untuk RGB-D, "
        "atau USD 350–1.120 untuk kamera stereo [39] (misalnya platform bervisi AI seperti ORCBOT [35] atau RGB-D Jetson Xavier NX [38]), sementara varian *Straddle Ditch-Rover* "
        "tanpa LiDAR tetap melebihi Rp5.000.000 pada purwarupa (~Rp7,5–8,5 juta) dan memerlukan pemeliharaan mekanis rutin [41]."
    )

    add_h2(doc, "1.1.3 Alternatif 3: Robot Penarik Selang, Pembawa Tandon, atau Pengangkang Saluran Berpenggerak Mesin/Hidro-Turbin")
    add_body(
        doc,
        "Alternatif 3 mengelompokkan robot irigasi berpasokan eksternal kontinu via selang panjang maupun pengangkang saluran "
        "skala berat: mesin penyiram penarik selang (*traveling sprinkler/water-powered robot*) bermesin bensin 7 HP [23] atau "
        "berpenggerak turbin hidrolik [33], robot pembawa selang berpenggerak listrik, serta wahana pengangkang kanal beroda empat "
        "bermesin genset diesel 30 kW dengan *spray gun* 10 kW pada paten CN115804333A [28]."
    )
    add_body(
        doc,
        "Evaluasi mekanis, hidraulik, dan kesesuaian CD-2 pada Ciberes mengungkap empat ketidakcocokan mendasar: "
        "(1) **Beban tarik & rugi gesek selang fleksibel 120 m**: pemodelan Darcy-Weisbach dan gesekan Coulomb tanah (*mu* = 0,65) "
        "untuk tarikan selang sepanjang 120 m menunjukkan trade-off yang saling mengunci — selang 1/2 inci menimbulkan *head loss* "
        "ekstrem **207,72 m (20,38 bar)** pada debit 53,6 L/menit (gaya tarik 170 N), selang 3/4 inci masih kehilangan **30,27 m "
        "(2,97 bar)** dengan massa basah 49,5 kg dan gaya gesek **316 N**, sedangkan selang 1 inci berbobot basah 78,7 kg menuntut "
        "gaya tarik **502 N** [33], melampaui kemampuan sasis listrik ringkas <= Rp5 juta sehingga memaksa mesin berat; "
        "(2) **Pelanggaran emisi S-12 & pemborosan air S-01**: pemakaian mesin bensin 7 HP [23] atau genset diesel 30 kW [28] "
        "melanggar spesifikasi emisi nol (S-12) dan mengulang risiko kerusakan mesin bakar eksisting, sementara *spray gun* "
        "berjangkauan 47,5–57 m [23] hingga 75 m [28] membasahi tajuk daun serta membuang air kembali ke parit terbuka alih-alih "
        "menakar 15 L/pohon (S-01); "
        "(3) **Ketidakcocokan topologi parit (+)**: klaim paten CN115804333A [28] secara eksplisit mensyaratkan kanal lurus "
        "seragam dan memperingatkan risiko jatuh (*die luo feng xian*) bila berhadapan dengan persimpangan parit melintang (+), "
        "sedangkan turbin hidrolik [33] membutuhkan pasokan pipa bertekanan tinggi yang tidak tersedia di parit gravitasi Ciberes; serta "
        "(4) **Biaya investasi & perawatan**: total investasi jauh melampaui pagu C-02 (<= Rp5 juta purwarupa; <= Rp18 juta penuh) "
        "dan menuntut operator terlatih."
    )

    add_h2(doc, "1.1.4 Alternatif 4: Sistem Gravitasi Tandon Elevasi atau Gerobak Pompa Surya Semi-Manual")
    add_body(
        doc,
        "Alternatif 4 merupakan varian konvensional berbiaya awal moderat yang diulas pada pedoman FAO [2] dan rancangan "
        "gerobak pompa surya 50 Wp pada lahan bawang merah [3]. Pada konfigurasi pertama, pompa surya mengisi tandon menara "
        "setinggi 2–4 m lalu mengalirkan air secara gravitasi ke pipa tetes; pada konfigurasi kedua, pompa DC bertenaga "
        "panel surya 50 Wp + baterai 12 V 20 Ah diletakkan pada gerobak tarik untuk menyiram manual memakai selang."
    )
    add_body(
        doc,
        "Hasil telaah literatur [2], [3], [21] mengungkapkan dua keterbatasan penting: pada skema tandon gravitasi, tekanan "
        "statis 0,2–0,4 bar sering kali berada di bawah ambang kestabilan emiter 78,45 kPa (~0,78 bar) [21] dan menurun "
        "seiring berkurangnya tinggi muka air tandon, sementara menara penyangga tangki 8–10 m³ untuk kebun penuh rapuh di "
        "tanah sawah lunak Ciberes; sebaliknya, skema gerobak PV 50 Wp [3] (biaya pembuatan ~Rp2,7 juta di lahan datar) "
        "tetap membutuhkan buruh menarik selang melompati parit melintang (+) dan tidak menjamin dosis volumetrik maupun "
        "otomatisasi jadwal (S-01, S-05)."
    )

    # ==========================================================================
    # 1.2 ANALISIS DAN PEMILIHAN SOLUSI
    # ==========================================================================
    add_h1(doc, "1.2 Analisis dan Pemilihan Solusi")
    add_h2(doc, "1.2.1 Parameter Evaluasi Berbasis Batasan CD-2")
    add_body(
        doc,
        "Pemilihan solusi dilakukan secara kuantitatif menggunakan enam kriteria berbobot total 100% yang diturunkan langsung "
        "dari seluruh batasan mutlak dan spesifikasi desain dokumen CD-2: (K1) presisi dosis 15 L/pohon (S-01) dan "
        "keseragaman *CU >= 85%* tanpa membasahi tajuk (25%); (K2) kesesuaian daya *off-grid* SELV (S-06) dan adaptasi "
        "topografi 3 parit + penghubung melintang (20%); (K3) kepatuhan pagu biaya purwarupa <= Rp5.000.000 serta proyeksi "
        "skala penuh <= Rp18.000.000 (25%); (K4) ketahanan terhadap sedimen lumpur sungai Ciberes dan korosi (15%); "
        "(K5) kemudahan pengoperasian *single-touch* serta perawatan bagi buruh kebun (10%); dan (K6) kepatuhan lingkungan "
        "nol emisi (S-12) dan keselamatan tegangan sentuh (S-10) (5%)."
    )

    add_h2(doc, "1.2.2 Matriks Perbandingan Teknis Alternatif")
    add_caption(doc, "Tabel 1. Ringkasan Perbandingan Aspek Teknis dan Kelayakan Empat Alternatif Solusi", is_table=True)
    t1_headers = [
        "Parameter Evaluasi",
        "Alt 1 (Terpilih):\nMikro-Irigasi Surya",
        "Alt 2:\nUGV / Straddle Rover",
        "Alt 3:\nRobot Selang / Gun",
        "Alt 4:\nTandon / Gerobak PV",
    ]
    t1_rows = [
        ["Catu Daya & Emisi (S-06, S-12)", "PLTS 100 Wp + LiFePO4 30 Ah; SELV 12 V, 0 g CO2/kWh", "Baterai besar 24-48 V: ~368,9 W (~3,69 kWh / 8 jam) s.d. 1,5-2,1 kW [25], [35]", "Mesin bensin 7 HP [23] / diesel 30 kW [28] / turbin [33] (melanggar S-12)", "PV 50-150 Wp (0 emisi), beban menara/gerobak"],
        ["Akses Medan 3 Parit + Silang (+)", "Sangat baik: pipa PE melintasi parit berpenopang", "Gagal: slip 10% roda / 3% track di tanah basah 35% [34], longsor parit & UWB 0,93-1,12 m [25]", "Buruk: tarik selang 120 m butuh 316-502 N [33], paten [28] berisiko jatuh di parit (+)", "Sedang: gerobak/selang terhalang parit (+)"],
        ["Dosis 15 L & CU >= 85% (S-01, S-02)", "Sangat baik: 2x PC Dripper + flow meter YF-S201", "Rendah: tangki ~50 kg habis 2-3 pohon [22]; rover 5,11 L/mnt butuh 30,19 jam (target 46,9-53,6 L/mnt)", "Buruk: gun menyebar 47-75 m [23], [28] atau head loss selang 1/2\" 20,38 bar [33]", "Rendah: tekanan tandon turun / manual [2], [3]"],
        ["Ketahanan Lumpur Sungai (S-13)", "Baik: saringan hisap + disc filter 120 mesh + end-flush", "Rentan aus/sumbat pada penyedot parit apung tanpa prafilter 120 mesh & pompa tekan", "Toleran di nozzle gun, boros air & tidak terukur", "Sedang: endapan tandon & sumbat tekanan rendah"],
        ["Kemudahan Operasi Buruh (C-05)", "Tinggi: otomatis RTC + tombol 1-sentuhan & 3 LED", "Sangat rendah: butuh operator ROS/navigasi [24], [35] & angkut baterai berat", "Rendah: servis karburator/mesin bakar rutin [23], [28]", "Sedang-tinggi: mudah, tetapi kerja fisik menarik selang [3]"],
        ["Biaya Purwarupa (<= Rp5 Jt) & Penuh (<= Rp18 Jt)", f"Memenuhi ({fmt_rp(bom_proto_tot)} purwarupa; {fmt_rp(full_tot)} penuh)", "Gagal: Straddle Rover ~Rp7,5-8,5 jt; LiDAR/RGB-D USD 210-1.680 [39]; UGV >Rp25-60 jt [22], [25]", "Gagal (> Rp15-40 jt + biaya BBM harian [23], [28])", "Gerobak ~Rp2,7 jt [3] (manual); tandon penuh > Rp15 jt"],
    ]
    add_table(doc, t1_headers, t1_rows, [1.25, 1.35, 1.15, 1.15, 1.15], highlight_col=1, font_size=8.1)

    add_h2(doc, "1.2.3 Matriks Keputusan Tertimbang (Weighted Decision Matrix)")
    add_caption(doc, "Tabel 2. Evaluasi Kuantitatif Alternatif Solusi Menggunakan Weighted Decision Matrix", is_table=True)
    scores = [
        ("K1. Presisi Dosis (15 L) & Keseragaman (>=85%)", 25, [5, 2, 1, 3]),
        ("K2. Catu Off-Grid (S-06) & Topografi Parit (+)", 20, [5, 2, 2, 3]),
        ("K3. Pagu Biaya (<=Rp5 Jt / <=Rp18 Jt) & Skalabilitas", 25, [5, 1, 2, 3]),
        ("K4. Ketahanan Air Berlumpur & Keandalan Mekanis", 15, [4, 2, 3, 3]),
        ("K5. Kemudahan Operasi & Rawat Buruh (C-05)", 10, [4, 1, 2, 4]),
        ("K6. Nol Emisi (S-12) & Keselamatan SELV (S-10)", 5, [5, 3, 1, 4]),
    ]
    t2_rows = []
    tots = [0.0, 0.0, 0.0, 0.0]
    for lbl, w_pct, sc in scores:
        w = w_pct / 100.0
        row = [lbl, f"{w_pct}%"]
        for i in range(4):
            val = w * sc[i]
            tots[i] += val
            row.append(f"{sc[i]} ({val:.2f})")
        t2_rows.append(row)
    t2_rows.append(["TOTAL SKOR TERTIMBANG (Maks 5,00)", "100%", f"{tots[0]:.2f}", f"{tots[1]:.2f}", f"{tots[2]:.2f}", f"{tots[3]:.2f}"])
    t2_rows.append(["PERINGKAT KEPUTUSAN", "-", "1 (DIPILIH)", "4 (Ditolak)", "3 (Ditolak)", "2 (Cadangan)"])

    add_table(
        doc,
        ["Kriteria (Skala 1 = Buruk s.d. 5 = Sangat Baik)", "Bobot", "Alt 1\n(Tetes Surya)", "Alt 2\n(UGV Robot)", "Alt 3\n(Selang/Gun)", "Alt 4\n(Tandon/PV)"],
        t2_rows,
        [2.25, 0.55, 0.85, 0.80, 0.80, 0.80],
        col_aligns=[WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER,
                    WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER],
        highlight_col=2,
        font_size=8.4,
    )

    add_h2(doc, "1.2.4 Keputusan Pemilihan Solusi dan Peningkatan Berbasis Literatur Penuh")
    add_body(
        doc,
        f"Berdasarkan Tabel 2, **Alternatif 1 (Mikro-Irigasi Tetes Terzonasi Mandiri Surya)** memperoleh skor tertimbang "
        f"tertinggi sebesar **{tots[0]:.2f} dari skala 5,00**, unggul jauh (+1,60 poin) di atas Alternatif 4 ({tots[3]:.2f}) "
        f"dan mengeliminasi Alternatif 3 ({tots[2]:.2f}) serta Alternatif 2 ({tots[1]:.2f}). Untuk menjamin ketangguhan desain "
        f"dari temuan studi penuh literatur, rancangan Alternatif 1 pada dokumen ini menyematkan enam penyempurnaan rekayasa "
        f"krusial terhadap konsep irigasi otomatis konvensional: (1) pemakaian *Motorized Ball Valve* (MBV) 0 W statis [4], "
        f"[6], [9] menggantikan selenoid NC konstan; (2) pemasangan transduser tekanan 0–5 bar langsung di hilir filter untuk "
        f"membaca *dry-run* maupun batas bilas dP >= 70 kPa [12]; (3) spesifikasi rumah pompa non-besi cor beserta saringan hisap "
        f"pra-pompa [19]; (4) penyediaan keran *end-flush* berkecepatan >= 0,6 m/s di tiap ujung lateral [19]; (5) modifikasi "
        f"rangkaian sensor *Capacitive v1.2* (R_bleed 1 MOhm, kapasitor 0,1 uF, *power-gating* MOSFET, dan LDO 3,3 V eksternal) "
        f"[1], [5], [14]; serta (6) kepastian rincian anggaran purwarupa di bawah pagu mutlak Rp5.000.000 (S-08)."
    )

    # ==========================================================================
    # 1.3 DESAIN SOLUSI TERPILIH
    # ==========================================================================
    add_h1(doc, "1.3 Desain Solusi Terpilih")
    add_h2(doc, "1.3.1 Ruang Lingkup Petak Uji Awal Pra-Survei dan Kompatibilitas Skalabilitas")
    add_body(
        doc,
        "Purwarupa fungsional dirancang untuk memvalidasi performa seluruh subsistem secara menyeluruh pada satu petak uji "
        "di kebun mitra Ciberes. Sebelum pengukuran jarak tanam dan panjang baris aktual dilaksanakan pada agenda survei "
        "lapangan terdekat, rancangan purwarupa pada draf ini dimodelkan secara modular mengikuti skema awal mitra "
        "**20 m × 3 baris pohon** (*Baris 1 – Parit 1 – Baris 2 – Parit 2 – Baris 3 – Parit 3*) beserta lintasan "
        "penghubung parit melintang (+), dengan asumsi awal ~8 pohon per baris (total ~24 pohon contoh). Setiap parameter "
        "ukuran pipa pada Tabel BOM tetap bersifat modular sehingga segera setelah survei pengukuran lapangan kebun mitra "
        "terlaksana, bentang lateral dapat langsung divalidasi atau disesuaikan untuk menjamin kepatuhan mutlak "
        "batasan C-03 CD-2 (15–20 pohon uji, bentang >= 25 m), sekaligus memetakan ekspansi seragam menjadi 10 zona "
        "(*mainline* 1,5 inci, ~600 pohon) di kebun penuh."
    )

    add_h2(doc, "1.3.2 Arsitektur Sistem Terintegrasi Tiga Domain")
    add_body(
        doc,
        "Arsitektur sistem membagi peran secara jelas ke dalam tiga domain fisik dan fungsional yang saling terhubung: "
        "(1) **Domain Catu Daya Off-Grid SELV 12 V** yang memanen radiasi surya via panel 100 Wp dan MPPT ke baterai LiFePO4 "
        "12,8 V 30 Ah disertai rel teregulasi terpisah 5 V dan LDO 3,3 V guna melindungi kestabilan pembacaan analog ADC; "
        "(2) **Domain Kendali & Instrumentasi IP65** berpusat pada mikrokontroler ESP32 berbasis *Finite State Machine* (FSM) "
        "dengan pewaktu RTC DS3231, tombol 1-sentuhan, serta isolasi driver aktuator MOSFET/H-Bridge; dan (3) **Domain "
        "Hidrolika & Distribusi Lahan** mulai dari saringan hisap sungai, pompa DC non-korosif, *disc filter*, 3 unit MBV, "
        "hingga lateral PE 16 mm, PC Dripper 8 L/jam, dan keran *end-flush*, sebagaimana diilustrasikan pada Gambar 1."
    )
    add_figure(doc, "fig1_arsitektur_sistem.png", "Gambar 1. Diagram Blok Arsitektur Terintegrasi Tiga Domain Sistem Mikro-Irigasi Surya.")

    add_h2(doc, "1.3.3 Desain Hidrolika, Tata Letak 20 m x 3 Baris, Model Matematis, dan Simulasi Awal")
    add_body(
        doc,
        "Dari tepi Sungai/Saluran Ciberes (~20,54 m dari batas kebun), air dihisap melewati keranjang saringan pra-pompa "
        "berukuran bukaan ~1–2 mm dan *foot valve* non-korosif guna menyaring pasir kasar sebelum memasuki ruang pompa "
        "diafragma DC 12 V berbahan polimer (menghindari pembentukan kerak karat oksida besi sebagaimana disoroti [19]). "
        "Di hilir pompa, air bertekanan melewati *disc filter* 120–150 mesh (bukaan ~124–130 mikron) untuk menahan partikel "
        "lumpur tersuspensi sungai Ciberes [12], [19], lalu melintasi *water flow meter* YF-S201 dan transduser tekanan "
        "0–5 bar menuju *header* PE 1 inci (ID ~25,0 mm) di ujung bedengan."
    )
    add_figure(doc, "fig2_denah_petak_uji_20m.png", "Gambar 2. Rancangan Tata Letak Awal Petak Uji 20 m x 3 Baris dan Lintasan Parit Melintang (Pra-Survei).")
    add_body(
        doc,
        "Seperti tampak pada Gambar 2, *header* PE 1 inci membagi aliran ke tiga lateral PE 16 mm (ID 13,6 mm) sepanjang "
        "~20 m melalui tiga *Motorized Ball Valve* (MBV Z1, Z2, Z3). Saat melintasi parit penghubung melintang (+), segmen "
        "pipa dipasang di atas penopang sederhana (jembatan pipa) agar tidak terendam lumpur maupun terinjak pekerja saat "
        "penyiangan. Di sekeliling pangkal tiap pohon jeruk limau (tinggi dominan ~1 m), dua unit *PC Dripper* 8 L/jam "
        "(total 16 L/jam/pohon) ditempatkan pada radius 0,5–0,8 m sehingga selaras dengan area perakaran efektif tanaman "
        "sitrus [18], [32]. Pada ujung setiap lateral dipasang keran manual *end-flush* guna membilas akumulasi endapan halus."
    )
    add_body(
        doc,
        "Kehilangan tinggi tekan (*head loss*) di sepanjang pipa utama dan lateral berpancaran ganda dimodelkan melalui "
        "persamaan Darcy–Weisbach yang dikoreksi faktor outlet seragam Christiansen (*F*_Chr = 0,391 untuk 8 titik sadap "
        "di satu lateral) beserta koefisien kehilangan minor *K*, sedangkan tekanan kerja pompa total serta durasi aplikasi "
        "dosis 15 L/pohon dirumuskan oleh Persamaan (1)–(3) berikut."
    )
    add_equation(doc, OMML_DARCY, "1")
    add_equation(doc, OMML_TDH, "2")
    add_equation(doc, OMML_TIME, "3")
    add_body(
        doc,
        "Dengan 2 emiter PC berdebit *q*_e = 8 L/jam per pohon (*N*_e = 2), Persamaan (3) memberikan durasi siram "
        "tepat **56 menit 15 detik (56,25 menit)** untuk menyalurkan dosis acuan mitra *V*_target = 15 L/pohon, "
        "dengan syarat tekanan masuk di pangkal lateral tetap berada di atas ambang kestabilan emiter 78,45 kPa (~0,785 bar "
        "[21]) dan target kerja nominal PC dripper ~1,00 bar (100 kPa). Untuk membuktikan fisibilitas desain sejak tahap CD-3, "
        "persamaan Darcy–Weisbach dengan faktor gesekan Swamee–Jain (kekasaran absolut *ε* = 1,5 × 10⁻⁶ m, "
        "*Δz* = 1,50 m, *ΔP*_filter bersih = 0,20 bar hingga ambang bilas 0,70 bar mengacu [12]) "
        "disimulasikan secara numerik pada Python dengan hasil terangkum pada Tabel 3."
    )
    add_caption(doc, "Tabel 3. Keluaran Simulasi Awal Hidrolika Darcy–Weisbach untuk Berbagai Skenario Operasi Petak Uji", is_table=True)
    hyd_rows = []
    for c in hyd["configs"]:
        note = "Lulus syarat bilas >= 0,60 m/s [19]" if c["passes_scour_06ms"] else "Butuh flush berkala (v_ir < 0,60 m/s [19])"
        hyd_rows.append([
            c["name"],
            f"{c['Q_L_h']:.1f} L/jam\n({c['Q_L_min']:.2f} L/mnt)",
            f"{c['v_main_ms']:.3f} | {c['v_lat_inlet_ms']:.3f}",
            f"{c['hf_main_m']:.3f} | {c['hf_lat_m']:.3f}",
            f"{c['P_pump_clean_bar']:.2f} bar\n({c['P_pump_dirty_filter_bar']:.2f} bar bilas)",
            note,
        ])
    add_table(
        doc,
        ["Skenario Operasi Simulasi", "Debit Sistem Total", "Kecepatan (m/s)\nMain | Lateral", "Head Loss (m)\nMain | Lateral", "Tekanan Pompa\nBersih | Ambang Bilas", "Verifikasi Kinerja & Literatur"],
        hyd_rows,
        [1.45, 0.90, 0.95, 0.85, 1.00, 0.90],
        col_aligns=[WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER,
                    WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT],
        font_size=8.2,
    )
    add_body(
        doc,
        "Hasil simulasi pada Tabel 3 (dan visualisasi kurva pada Gambar 5 panel kiri) membuktikan temuan rekayasa penting: "
        "selama mode tetes normal 1 zona (8 pohon = 128 L/jam) maupun 3 baris serentak (24 pohon = 384 L/jam), kecepatan aliran "
        "awal lateral PE 16 mm hanya sebesar 0,245 m/s, lebih kecil dari kecepatan kritis pengendapan sedimen Lavanholi dkk. "
        "sebesar **0,60 m/s** [19]. Sebaliknya, ketika katup MBV menutup 2 baris lain dan keran *end-flush* di ujung satu lateral "
        "dibuka, debit 418,4 L/jam (6,97 L/menit) pada tekanan pompa 0,65–1,15 bar membangkitkan kecepatan pembilasan "
        "**0,80 m/s >= 0,60 m/s**, sehingga membuktikan secara kuantitatif mengapa arsitektur harus memadukan katup zonasi dan "
        "keran *end-flush* terpisah."
    )

    add_h2(doc, "1.3.4 Desain Kelistrikan Off-Grid SELV 12 V, Pengkondisian Sinyal, dan Neraca Energi")
    add_body(
        doc,
        "Seluruh sistem kelistrikan menerapkan batas *Safety Extra-Low Voltage* (SELV <= 60 V DC sesuai IEC 60364-4-41 [30]) "
        "pada bus nominal 12,8 V DC bersekring utama 15 A dan dioda TVS. Sebagaimana ditampilkan pada Gambar 3, bus baterai "
        "LiFePO4 12,8 V 30 Ah (384 Wh nominal; 307,2 Wh kapasitas pakai pada DoD 80%) diisi oleh panel surya monokristalin "
        "100 Wp melalui kontroler MPPT 10 A untuk memaksimalkan efisiensi panen radiasi pagi maupun cuaca berawan [20], [21]."
    )
    add_figure(doc, "fig3_skematik_kelistrikan.png", "Gambar 3. Skematik Rangkaian Kelistrikan SELV 12 V DC, Pengkondisian Sinyal Sensor, dan Isolasi Aktuator.")
    add_body(
        doc,
        "Pemisahan jalur catu logika menggunakan konverter Buck 12 V ke 5 V diikuti **regulator LDO 3,3 V eksternal** serta "
        "*star grounding* bertujuan mencegah penurunan atau derau tegangan bus saat pompa menyedot arus start dari memengaruhi "
        "referensi ADC ESP32—masalah umum yang dilaporkan pada [5], [14]. Pembacaan sensor kelembapan tanah *Capacitive v1.2* "
        "dimodifikasi merujuk temuan perbaikan perangkat keras [1], [5], [8], [14]: penambahan resistor paralel 1 MOhm (*R_bleed*), "
        "filter RC 0,1 uF, penutupan lapisan tepi papan (*potting* epoksi), pengaktifan berpulsa lewat MOSFET (*power gating* hanya "
        "saat akuisisi data) untuk mencegah korosi elektrolisis serta pengisian muatan sisa, dan pembagian tegangan aman ke GPIO "
        "ESP32 (termasuk *divider* 5 V -> 3,3 V pada YF-S201 dan transduser 0–5 bar)."
    )
    add_body(
        doc,
        "Pada sisi aktuator, penggerak katup bola bermotor (MBV) memakai rangkaian *H-Bridge* DRV8800/L298N yang hanya "
        "mengalirkan pulsa 4 W selama ~5 detik saat membuka atau menutup, sehingga daya tahannya pada posisi terbuka/tertutup "
        "adalah **0 W (zero-static holding power)** [4], [6], [9]. Driver pompa memakai optocoupler dan MOSFET logika IRLZ44N "
        "dengan dioda *flyback* Schottky serta interlock waktu jeda antarsiklus >= 30 detik. Neraca energi harian dan otonomi "
        "baterai dimodelkan melalui Persamaan (4)–(6), dengan faktor penalti termal modul surya sebesar 14,22% pada suhu siang "
        "terik mengacu Bawa dkk. [21] (*η*_total = 73,8%)."
    )
    add_equation(doc, OMML_PV, "4")
    add_equation(doc, OMML_ENERGY_CYCLE, "5")
    add_equation(doc, OMML_AUTONOMY, "6")

    add_caption(doc, "Tabel 4. Hasil Simulasi Awal Neraca Energi PV 100 Wp + LiFePO4 30 Ah untuk 24 Pohon (360 L/Siklus)", is_table=True)
    e_rows = [
        ["Panen Energi PV 100 Wp (Hari Cerah, PSH 4,5 jam, eta 73,8%)", f"{ene['e_gen_sunny_wh_day']:.1f} Wh/hari", "Surplus tinggi setelah 1 siklus penuh"],
        ["Panen Energi PV 100 Wp (Hari Mendung Berat, PSH 1,5 jam)", f"{ene['e_gen_cloudy_wh_day']:.1f} Wh/hari", "Tetap menutup siklus serentak 85,7 Wh"],
        ["Beban 3 Baris Serentak + MBV 0 W Statis (0,94 jam + 71 jam tidur)", f"{ene['e_cycle_simul_mbv_wh']:.2f} Wh/siklus", f"Otonomi {ene['cycles_autonomy_simul_mbv']} siklus ({ene['days_autonomy_3d_interval_simul']} hari) tanpa matahari"],
        ["Beban 3 Zona Bergantian + MBV 0 W Statis (2,81 jam pompa)", f"{ene['e_cycle_3zone_mbv_wh']:.2f} Wh/siklus", f"Otonomi {ene['cycles_autonomy_3zone_mbv']} siklus ({ene['days_autonomy_3d_interval_3zone']} hari)"],
        ["Pembanding: 3 Zona Bergantian + Selenoid NC (koil 12 W konstan)", f"{ene['e_cycle_3zone_nc_wh']:.2f} Wh/siklus", f"Boros {ene['e_valve_nc_wh']} Wh hanya utk tahan katup vs {ene['e_valve_mbv_wh']:.3f} Wh MBV"],
        ["Efisiensi Penghematan Energi Katup MBV vs Selenoid NC", f"{ene['valve_saving_pct']:.1f}% lebih hemat", "Memperpanjang margin otonomi di cuaca berawan"],
    ]
    add_table(doc, ["Parameter Simulasi Neraca Energi", "Nilai Komputasi", "Implikasi Desain (S-06)"], e_rows, [2.75, 1.35, 1.95],
              col_aligns=[WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT], font_size=8.3)
    add_figure(doc, "fig5_simulasi_hidrolika_energi.png", "Gambar 5. Grafik Hasil Simulasi Awal: (Kiri) Kebutuhan Tekanan Pompa & Batas Kecepatan Bilas; (Kanan) Neraca Energi Surya.")

    add_h2(doc, "1.3.5 Desain Perangkat Lunak, Finite State Machine (FSM), dan Pseudocode Kendali")
    add_body(
        doc,
        "Perangkat lunak tertanam pada ESP32 dibangun menggunakan arsitektur *Finite State Machine* (FSM) deterministik "
        "agar sistem berada dalam mode tidur daya rendah (*deep sleep*, konsumsi sistem < 25 mW) sepanjang jeda 72 jam "
        "dan hanya aktif pada jadwal terprogram RTC DS3231 atau interupsi tombol fisik 1-sentuhan pekerja kebun (Gambar 4). "
        "Sebelum mengeksekusi pengairan setiap zona, ESP32 selalu memverifikasi interlock baterai (*V*_bat >= 11,5 V), "
        "keberadaan jeda anti-*short-cycling* pompa >= 30 detik, dan pembacaan kelembapan tanah terkalibrasi (bila dipicu RTC "
        "saat tanah sudah lembap oleh hujan, siklus ditunda otomatis). Selama pompa aktif, volume air diintegrasikan langsung "
        "dari pulsa *flow meter* YF-S201 (*V* = ∫ *Q*(*t*) d*t*) sembari memantau jendela aman tekanan [0,5..3,5 bar] serta "
        "sinyal kejenuhan filter untuk menyalakan indikator kuning *Bilas Disc Filter*."
    )
    add_figure(doc, "fig4_flowchart_fsm.png", "Gambar 4. Diagram Alir Logika Kendali Tertutup, Gating Kelembapan, dan Fail-Safe Hidrolika-Baterai.")
    add_code_block(doc, [
        "// Pseudocode Kendali Utama FSM ESP32 - Mikro-Irigasi Tetes Terzonasi Surya",
        "CONST PIN_VBAT=34, PIN_SOIL=35, PIN_PRESS=32, PIN_FLOW=27, PIN_BTN=14;",
        "CONST PIN_PUMP=25, PIN_SOIL_PWR=26, PIN_LED_STAT=2, PIN_LED_FLT=4, PIN_LED_FILT=16;",
        "CONST float TARGET_L_PER_TREE = 15.0;  // Acuan mitra S-01",
        "CONST float VBAT_MIN_V = 11.5;         // Interlock proteksi LiFePO4",
        "",
        "FUNCTION read_calibrated_soil_vwc():",
        "  digitalWrite(PIN_SOIL_PWR, HIGH); delay_ms(200); // MOSFET power-gate anti-karat",
        "  raw = median_filter(analogRead_16samples(PIN_SOIL));",
        "  digitalWrite(PIN_SOIL_PWR, LOW);",
        "  RETURN map_linear_clay_ciberes(raw); // Kalibrasi gravimetrik tanah liat lokal",
        "",
        "MAIN_CYCLE(trigger_source):",
        "  v_bat = read_voltage_divider(PIN_VBAT);",
        "  IF v_bat < VBAT_MIN_V THEN blink(PIN_LED_FLT); lock_all_mbv_closed(); deep_sleep();",
        "  IF trigger_source == RTC_SCHEDULE AND read_calibrated_soil_vwc() > VWC_THRESHOLD THEN",
        "    deep_sleep(); // Tunda otomatis bila tanah masih lembap hujan",
        "  FOR zone IN [1, 2, 3]:",
        "    open_mbv_pulse(zone, 5000 ms);  // H-Bridge 5 detik, setelahnya 0 W statis",
        "    wait_pump_cooldown(30 sec);     // Anti-short-cycling",
        "    reset_flow_pulses(); digitalWrite(PIN_PUMP, HIGH);",
        "    WHILE flow_liters() < (TREES_IN_ZONE[zone] * TARGET_L_PER_TREE):",
        "      p_bar = read_pressure_bar(PIN_PRESS);",
        "      IF p_bar < 0.50 OR p_bar > 3.50 THEN // Deteksi dry-run atau pipa bocor",
        "        digitalWrite(PIN_PUMP, LOW); close_mbv_pulse(zone, 5000 ms); emergency_halt();",
        "      IF (baseline_clean_p - p_bar) >= 0.70 THEN digitalWrite(PIN_LED_FILT, HIGH); // Bilas dP >= 70 kPa",
        "      IF manual_stop_pressed() THEN break;",
        "      delay_ms(200);",
        "    digitalWrite(PIN_PUMP, LOW); close_mbv_pulse(zone, 5000 ms);",
        "  signal_done(PIN_LED_STAT); deep_sleep_until_next_rtc_or_button();",
    ])

    add_h2(doc, "1.3.6 Daftar Alat dan Bahan Purwarupa serta Proyeksi Skala Penuh Kebun")
    add_body(
        doc,
        f"Rincian kebutuhan material (*Bill of Materials*/BOM) untuk membangun satu unit purwarupa fungsional pada petak "
        f"uji awal *20 m × 3 baris* (estimasi ~24 pohon dengan 3 katup MBV dan keran *end-flush*) disusun pada Tabel 5 dengan "
        f"total belanja komponen sebesar **{fmt_rp(bom_proto_tot)}**, mematuhi secara ketat pagu maksimal S-08 sebesar "
        f"Rp5.000.000. Sementara itu, Tabel 6 merangkum proyeksi biaya ekspansi arsitektur yang sama ke seluruh 500–600 pohon "
        f"(10 zona pada luas ~3.000 m²) sebesar **{fmt_rp(full_tot)}**, juga memenuhi batas investasi skala penuh S-08 "
        f"(<= Rp18.000.000)."
    )
    add_caption(doc, "Tabel 5. Rincian Bill of Materials (BOM) Purwarupa Petak Uji 20 m x 3 Baris (Estimasi Pra-Survei)", is_table=True)
    t5_rows = [
        [no, nama, qty, fmt_rp(up), fmt_rp(sub), just] for no, nama, qty, up, sub, just in bom_rows
    ]
    t5_rows.append(["Total", "Total Belanja Komponen Purwarupa Petak Uji (Pagu S-08 <= Rp5.000.000)", "-", "-", fmt_rp(bom_proto_tot), "TERPENUHI (Margin sisa Rp150.000)"])
    add_table(
        doc,
        ["No", "Komponen Utama & Spesifikasi", "Jml", "Harga Satuan", "Subtotal", "Justifikasi Kebutuhan"],
        t5_rows,
        [0.50, 2.00, 0.55, 0.78, 0.85, 1.37],
        col_aligns=[WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER,
                    WD_ALIGN_PARAGRAPH.RIGHT, WD_ALIGN_PARAGRAPH.RIGHT, WD_ALIGN_PARAGRAPH.LEFT],
        font_size=8.0,
    )

    add_caption(doc, "Tabel 6. Proyeksi Anggaran Modular ke Skala Kebun Penuh 500-600 Pohon (10 Zona, S-08 <= Rp18 Juta)", is_table=True)
    t6_rows = [
        [no, nama, qty, fmt_rp(up), fmt_rp(sub), just] for no, nama, qty, up, sub, just in full_rows
    ]
    t6_rows.append(["Total", "Total Proyeksi Investasi Skala Penuh (~600 Pohon / 3.000 m2)", "-", "-", fmt_rp(full_tot), "TERPENUHI (<= Rp18.000.000)"])
    add_table(
        doc,
        ["No", "Paket Ekspansi Skala Penuh (10 Zona)", "Jml", "Harga Satuan", "Subtotal", "Catatan Skalabilitas"],
        t6_rows,
        [0.50, 2.10, 0.65, 0.75, 0.85, 1.20],
        col_aligns=[WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER,
                    WD_ALIGN_PARAGRAPH.RIGHT, WD_ALIGN_PARAGRAPH.RIGHT, WD_ALIGN_PARAGRAPH.LEFT],
        font_size=8.0,
    )

    add_h2(doc, "1.3.7 Mekanisme Fabrikasi, Kalibrasi, dan Protokol Pengujian")
    add_bullet(doc, "**Fabrikasi Panel Kendali IP65 & Proteksi Sensor:** Modul ESP32, DS3231, buck/LDO, serta papan driver MOSFET dan DRV8800 dirakit di atas PCB berlubang/kustom menggunakan pengkabelan rapi dan *cable gland* kedap air di sisi bawah boks IP65 (IEC 60529 [31]). Leher elektronik sensor tanah *Capacitive v1.2* serta solderan resistor 1 MOhm/kapasitor 0,1 uF dilapisi resin epoksi tahan air sebelum ditanam miring pada kedalaman perakaran aktif.")
    add_bullet(doc, "**Kalibrasi Laboratorium Sebelum Uji Kebun:** (1) Kalibrasi *flow meter* YF-S201 memakai ember ukur gravimetrik hingga galat pembacaan liter < +-3%; (2) kalibrasi sensor tanah menggunakan sampel tanah liat kebun Ciberes pada 4–5 titik kadar air oven-kering hingga kapasitas lapang untuk memperoleh koefisien regresi lokal [14]; dan (3) uji *bench* katup MBV serta sensor tekanan terhadap skenario sumbatan buatan.")
    add_bullet(doc, "**Uji Coba Lapangan & Verifikasi S-01..S-14:** Setelah dimensi baris, jumlah pohon riil, dan elevasi sungai tervalidasi pada survei Ciberes, sistem dirakit pada petak uji dan diuji menggunakan metode Christiansen's Uniformity Coefficient (*CU* >= 85%, ISO 9261 [32]) melalui penampungan gelas ukur pada tiap emiter, pengujian mode *end-flush* kecepatan >= 0,6 m/s, dan pemantauan tegangan LiFePO4 selama siklus siram penuh.")

    # ==========================================================================
    # 1.4 JADWAL DAN ANGGARAN
    # ==========================================================================
    add_h1(doc, "1.4 Jadwal dan Anggaran")
    add_h2(doc, "1.4.1 Jadwal Pelaksanaan Proyek (Gantt Chart 20 Pekan <= 6 Bulan)")
    add_body(
        doc,
        "Rencana kerja realisasi fisik, integrasi perangkat lunak, kalibrasi, hingga pengujian kebun di Ciberes disusun "
        "selama 20 pekan (5 bulan, masih di bawah batas maksimal 6 bulan pada rubrik PTA), dimulai dengan validasi dimensi "
        "kebun pada pekan awal sehingga desain pipa 20 m × 3 baris dapat difinalkan sebelum belanja material pipa dilakukan."
    )
    add_caption(doc, "Tabel 7. Jadwal Pelaksanaan dan Integrasi Purwarupa (Gantt Chart 20 Pekan)", is_table=True)
    gantt_rows = [
        ["1", "Survei detail Ciberes (ukur panjang baris, elevasi & uji tanah) + Finalisasi CD-3", "■", "■", "", "", "", "", "", "", "", ""],
        ["2", "Pengadaan komponen listrik surya, katup MBV, sensor, dan perpipaan PE", "", "■", "■", "", "", "", "", "", "", ""],
        ["3", "Perakitan panel surya, catu SELV 12V/LDO 3,3V, modifikasi sensor tanah & IP65", "", "", "■", "■", "■", "", "", "", "", ""],
        ["4", "Pengembangan firmware FSM ESP32, modul RTC/flow/tekanan & uji dry-run lab", "", "", "", "■", "■", "■", "", "", "", ""],
        ["5", "Kalibrasi gravimetrik flow meter & kurva tanah liat Ciberes di laboratorium", "", "", "", "", "", "■", "■", "", "", ""],
        ["6", "Instalasi lapangan petak uji Ciberes (jembatan parit +, MBV, PC dripper, flush)", "", "", "", "", "", "", "■", "■", "", ""],
        ["7", "Pengujian lapang CU >= 85%, validasi dosis 15 L, uji end-flush & evaluasi otonomi", "", "", "", "", "", "", "", "■", "■", ""],
        ["8", "Penyusunan laporan akhir Tugas Akhir, penyempurnaan panduan buruh & Seminar Hasil", "", "", "", "", "", "", "", "", "■", "■"],
    ]
    add_table(
        doc,
        ["No", "Tahapan Kegiatan Utama", "B1\n1-2", "B1\n3-4", "B2\n1-2", "B2\n3-4", "B3\n1-2", "B3\n3-4", "B4\n1-2", "B4\n3-4", "B5\n1-2", "B5\n3-4"],
        gantt_rows,
        [0.32, 2.13, 0.36, 0.36, 0.36, 0.36, 0.36, 0.36, 0.36, 0.36, 0.36, 0.36],
        col_aligns=[WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT] + [WD_ALIGN_PARAGRAPH.CENTER]*10,
        font_size=7.8,
    )

    add_h2(doc, "1.4.2 Pembagian Tugas Tim Pelaksana")
    add_caption(doc, "Tabel 8. Pembagian Tanggung Jawab Teknis Tiga Anggota Kelompok Capstone", is_table=True)
    role_rows = [
        ["1", "Muhammad Al Qarnie\n(101032330043)", "Penanggung Jawab Hidrolika & Tata Letak Kebun",
         "Perancangan saringan hisap pra-pompa, pompa DC 12 V non-korosif, instalasi disc filter, rangkaian pipa PE 1 inci & 16 mm lintas parit (+), PC dripper 8 L/jam, keran end-flush, serta koordinasi uji keseragaman CU di Ciberes."],
        ["2", "Maheswara Ariq Athallah\n(101032300050)", "Penanggung Jawab Catu Daya Surya & Hardware Elektronika",
         "Perancangan PLTS 100 Wp + MPPT + BMS LiFePO4 30 Ah, skematik proteksi SELV/sekring 15 A, regulator Buck/LDO 3,3 V eksternal, perakitan driver MOSFET IRLZ44N & H-Bridge MBV, modifikasi hardware RC sensor tanah, dan pengemasan IP65."],
        ["3", "Daffa Hermansyah\n(101032330090)", "Penanggung Jawab Firmware ESP32, Kalibrasi & Integrasi Uji",
         "Pengembangan algoritma FSM ESP32 & DS3231, interrupt handler YF-S201 & pembacaan transduser tekanan, interlock baterai, simulasi numerik hidrolika-energi, kalibrasi gravimetrik tanah-debit, serta analisis data kelayakan teknis & ekonomi."],
    ]
    add_table(doc, ["No", "Nama & NIM", "Peran Utama", "Rincian Tugas dan Luaran Terukur"], role_rows, [0.35, 1.45, 1.45, 2.80],
              col_aligns=[WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.LEFT], font_size=8.3)

    add_h2(doc, "1.4.3 Rancangan Anggaran Biaya (RAB) Pelaksanaan Total dan Analisis Kelayakan Ekonomi")
    add_body(
        doc,
        f"Anggaran pelaksanaan tugas akhir memisahkan secara tegas komponen pembentuk produk fisik purwarupa sebesar "
        f"**{fmt_rp(bom_proto_tot)}** (mengacu Tabel 5, memenuhi batas maksimal Rp5.000.000 pada S-08 CD-2) dari biaya "
        f"alat ukur kalibrasi, bahan instalasi mekanis, jasa dudukan surya, serta transportasi survei Bandung–Subang sebesar "
        f"**{fmt_rp(rab_support_tot)}**, sehingga total dana pelaksanaan keseluruhan berjumlah **{fmt_rp(rab_grand_tot)}** "
        f"(Tabel 9). Bila dibandingkan dengan biaya upah penyiraman manual mitra saat ini (~Rp48.700.000/tahun pada interval "
        f"3 hari sekali [CD-1]), investasi sistem skala penuh sebesar **{fmt_rp(full_tot)}** memiliki titik impas "
        f"(*payback period*) kurang dari satu tahun operasi."
    )
    add_caption(doc, "Tabel 9. Rekapitulasi Rancangan Anggaran Biaya (RAB) Pelaksanaan Tugas Akhir", is_table=True)
    rab_rows = [
        ["A", "Belanja Komponen Utama Purwarupa Fungsional (Rincian pada Tabel 5)", "1 paket", fmt_rp(bom_proto_tot), fmt_rp(bom_proto_tot), "Kepatuhan Pagu S-08 <= Rp5.000.000"],
    ]
    for kd, ur, qt, harga, ket in RAB_SUPPORT:
        rab_rows.append([kd, ur, qt, fmt_rp(harga), fmt_rp(harga), ket])
    rab_rows.append(["Total", "TOTAL RANCANGAN ANGGARAN BIAYA PELAKSANAAN", "-", "-", fmt_rp(rab_grand_tot), "Mencakup CAPEX alat + alat uji & survei lapangan"])
    add_table(doc, ["Pos", "Uraian Pos Pengeluaran", "Vol", "Biaya Satuan", "Total Biaya", "Keterangan Verifikasi"], rab_rows,
              [0.50, 2.20, 0.55, 0.80, 0.85, 1.15],
              col_aligns=[WD_ALIGN_PARAGRAPH.CENTER, WD_ALIGN_PARAGRAPH.LEFT, WD_ALIGN_PARAGRAPH.CENTER,
                          WD_ALIGN_PARAGRAPH.RIGHT, WD_ALIGN_PARAGRAPH.RIGHT, WD_ALIGN_PARAGRAPH.LEFT], font_size=8.1)

    # ==========================================================================
    # DAFTAR PUSTAKA (41 RUJUKAN IEEE TERVERIFIKASI PENUH)
    # ==========================================================================
    add_h1(doc, "Daftar Pustaka", page_break=True)
    for idx, ref_txt in enumerate(IEEE_REFS, start=1):
        p = doc.add_paragraph()
        p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.left_indent = Inches(0.42)
        p.paragraph_format.first_line_indent = Inches(-0.42)
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(2.5)
        p.paragraph_format.line_spacing = 1.10
        add_formatted_runs(p, f"[{idx}]  {ref_txt}", font_size=10.0)

    doc.save(OUT_DOCX)
    print(f"Saved {OUT_DOCX} (page_count_label={page_count_label})")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--pages", default="...", help="Jumlah halaman terverifikasi dari hasil ekspor PDF Word")
    args = parser.parse_args()
    build_document(page_count_label=args.pages)
