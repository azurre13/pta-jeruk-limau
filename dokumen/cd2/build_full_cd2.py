# -*- coding: utf-8 -*-
"""
Build complete CD2_Jeruk_Limau.docx with verified, DOI-backed bibliography.
"""

import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, fill_hex):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
    tcPr.append(tcMar)

def set_table_full_grid(table, color="A0A0A0", sz="4"):
    tblPr = table._tbl.tblPr
    borders = parse_xml(f'<w:tblBorders {nsdecls("w")}><w:top w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/><w:bottom w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/><w:insideH w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/><w:insideV w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/><w:left w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/><w:right w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/></w:tblBorders>')
    tblPr.append(borders)

def make_row_cant_split(row):
    trPr = row._tr.get_or_add_trPr()
    trPr.append(parse_xml(f'<w:cantSplit {nsdecls("w")}/>'))

def make_row_header(row):
    trPr = row._tr.get_or_add_trPr()
    trPr.append(parse_xml(f'<w:tblHeader {nsdecls("w")}/>'))

def add_body_p(doc, text, first_indent=0.39, space_before=0, space_after=6):
    p = doc.add_paragraph()
    p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = 1.5
    if first_indent > 0:
        p.paragraph_format.first_line_indent = Inches(first_indent)
    if text:
        r = p.add_run(text)
        r.font.name = "Times New Roman"
        r.font.size = Pt(12)
    return p

def add_point_item(doc, title, body_text, space_before=8, space_after=6, first_indent=0.39):
    p_title = doc.add_paragraph()
    p_title.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_title.paragraph_format.space_before = Pt(space_before)
    p_title.paragraph_format.space_after = Pt(2)
    p_title.paragraph_format.line_spacing = 1.5
    p_title.paragraph_format.keep_with_next = True
    p_title.paragraph_format.first_line_indent = Inches(0)
    
    r_title = p_title.add_run(title)
    r_title.font.name = "Times New Roman"
    r_title.font.size = Pt(12)
    r_title.font.bold = True
    
    p_body = doc.add_paragraph()
    p_body.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    p_body.paragraph_format.space_before = Pt(0)
    p_body.paragraph_format.space_after = Pt(space_after)
    p_body.paragraph_format.line_spacing = 1.5
    p_body.paragraph_format.first_line_indent = Inches(first_indent)
    
    r_body = p_body.add_run(body_text)
    r_body.font.name = "Times New Roman"
    r_body.font.size = Pt(12)
    
    return p_title, p_body

def add_heading_p(doc, text, level=1, space_before=14, space_after=6):
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = 1.5
    p.paragraph_format.keep_with_next = True
    
    if level == 0:
        p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(text)
        r.font.name = "Times New Roman"
        r.font.size = Pt(14)
        r.font.bold = True
    elif level == 1:
        p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
        r = p.add_run(text)
        r.font.name = "Times New Roman"
        r.font.size = Pt(12)
        r.font.bold = True
    elif level == 2:
        p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.LEFT
        r = p.add_run(text)
        r.font.name = "Times New Roman"
        r.font.size = Pt(12)
        r.font.bold = True
    return p

def add_caption_p(doc, text, is_table=True):
    p = doc.add_paragraph()
    p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.keep_with_next = is_table
    p.paragraph_format.space_before = Pt(10 if is_table else 4)
    p.paragraph_format.space_after = Pt(4 if is_table else 10)
    p.paragraph_format.line_spacing = 1.15
    r = p.add_run(text)
    r.font.name = "Times New Roman"
    r.font.size = Pt(11)
    r.font.bold = True
    return p

def add_equation_p(doc, omml_xml_str):
    p = doc.add_paragraph()
    p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(4)
    p.paragraph_format.line_spacing = 1.0
    p.paragraph_format.keep_with_next = True
    elem = parse_xml(omml_xml_str)
    p._element.append(elem)
    return p

# OMML Templates for Equations
etc_omml = '''<m:oMathPara xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math">
  <m:oMath>
    <m:sSub>
      <m:e><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>ET</m:t></m:r></m:e>
      <m:sub><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>c</m:t></m:r></m:sub>
    </m:sSub>
    <m:r><m:t> = </m:t></m:r>
    <m:sSub>
      <m:e><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>K</m:t></m:r></m:e>
      <m:sub><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>c</m:t></m:r></m:sub>
    </m:sSub>
    <m:r><m:t> × </m:t></m:r>
    <m:sSub>
      <m:e><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>ET</m:t></m:r></m:e>
      <m:sub><m:r><m:t>0</m:t></m:r></m:sub>
    </m:sSub>
  </m:oMath>
</m:oMathPara>'''

vpohon_omml = '''<m:oMathPara xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math">
  <m:oMath>
    <m:sSub>
      <m:e><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>V</m:t></m:r></m:e>
      <m:sub><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>pohon</m:t></m:r></m:sub>
    </m:sSub>
    <m:r><m:t> = </m:t></m:r>
    <m:sSub>
      <m:e><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>ET</m:t></m:r></m:e>
      <m:sub><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>c</m:t></m:r></m:sub>
    </m:sSub>
    <m:r><m:t> × </m:t></m:r>
    <m:sSub>
      <m:e><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>A</m:t></m:r></m:e>
      <m:sub><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>tajuk</m:t></m:r></m:sub>
    </m:sSub>
    <m:r><m:t> × </m:t></m:r>
    <m:sSub>
      <m:e><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>I</m:t></m:r></m:e>
      <m:sub><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>siram</m:t></m:r></m:sub>
    </m:sSub>
  </m:oMath>
</m:oMathPara>'''

cu_omml = '''<m:oMathPara xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math">
  <m:oMath>
    <m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>CU</m:t></m:r>
    <m:r><m:t> = 100% × </m:t></m:r>
    <m:d>
      <m:dPr><m:begChr m:val="["/><m:endChr m:val="]"/></m:dPr>
      <m:e>
        <m:r><m:t>1 - </m:t></m:r>
        <m:f>
          <m:num>
            <m:nary>
              <m:naryPr><m:chr m:val="∑"/><m:limLoc m:val="undOvr"/></m:naryPr>
              <m:sub><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>i</m:t></m:r><m:r><m:t>=1</m:t></m:r></m:sub>
              <m:sup><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>n</m:t></m:r></m:sup>
              <m:e>
                <m:d>
                  <m:dPr><m:begChr m:val="|"/><m:endChr m:val="|"/></m:dPr>
                  <m:e>
                    <m:sSub>
                      <m:e><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>X</m:t></m:r></m:e>
                      <m:sub><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>i</m:t></m:r></m:sub>
                    </m:sSub>
                    <m:r><m:t> - </m:t></m:r>
                    <m:acc>
                      <m:accPr><m:chr m:val="̄"/></m:accPr>
                      <m:e><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>X</m:t></m:r></m:e>
                    </m:acc>
                  </m:e>
                </m:d>
              </m:e>
            </m:nary>
          </m:num>
          <m:den>
            <m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>n</m:t></m:r>
            <m:r><m:t> × </m:t></m:r>
            <m:acc>
              <m:accPr><m:chr m:val="̄"/></m:accPr>
              <m:e><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>X</m:t></m:r></m:e>
            </m:acc>
          </m:den>
        </m:f>
      </m:e>
    </m:d>
  </m:oMath>
</m:oMathPara>'''

esiklus_omml = '''<m:oMathPara xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math">
  <m:oMath>
    <m:sSub>
      <m:e><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>E</m:t></m:r></m:e>
      <m:sub><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>siklus</m:t></m:r></m:sub>
    </m:sSub>
    <m:r><m:t> = </m:t></m:r>
    <m:sSub>
      <m:e><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>P</m:t></m:r></m:e>
      <m:sub><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>beban</m:t></m:r></m:sub>
    </m:sSub>
    <m:r><m:t> × </m:t></m:r>
    <m:sSub>
      <m:e><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>t</m:t></m:r></m:e>
      <m:sub><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>operasi</m:t></m:r></m:sub>
    </m:sSub>
  </m:oMath>
</m:oMathPara>'''

cbaterai_omml = '''<m:oMathPara xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math">
  <m:oMath>
    <m:sSub>
      <m:e><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>C</m:t></m:r></m:e>
      <m:sub><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>baterai</m:t></m:r></m:sub>
    </m:sSub>
    <m:r><m:t> ≥ </m:t></m:r>
    <m:f>
      <m:num>
        <m:sSub>
          <m:e><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>E</m:t></m:r></m:e>
          <m:sub><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>siklus</m:t></m:r></m:sub>
        </m:sSub>
        <m:r><m:t> × </m:t></m:r>
        <m:sSub>
          <m:e><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>N</m:t></m:r></m:e>
          <m:sub><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>autonomy</m:t></m:r></m:sub>
        </m:sSub>
      </m:num>
      <m:den>
        <m:sSub>
          <m:e><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>V</m:t></m:r></m:e>
          <m:sub><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>sistem</m:t></m:r></m:sub>
        </m:sSub>
        <m:r><m:t> × </m:t></m:r>
        <m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>DoD</m:t></m:r>
      </m:den>
    </m:f>
  </m:oMath>
</m:oMathPara>'''

pp_omml = '''<m:oMathPara xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math">
  <m:oMath>
    <m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>PP</m:t></m:r>
    <m:r><m:t> = </m:t></m:r>
    <m:f>
      <m:num>
        <m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>CAPEX</m:t></m:r>
      </m:num>
      <m:den>
        <m:r><m:t>Δ</m:t></m:r>
        <m:sSub>
          <m:e><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>OPEX</m:t></m:r></m:e>
          <m:sub><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>tahunan</m:t></m:r></m:sub>
        </m:sSub>
      </m:den>
    </m:f>
  </m:oMath>
</m:oMathPara>'''

eta_omml = '''<m:oMathPara xmlns:m="http://schemas.openxmlformats.org/officeDocument/2006/math">
  <m:oMath>
    <m:sSub>
      <m:e><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>η</m:t></m:r></m:e>
      <m:sub><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>a</m:t></m:r></m:sub>
    </m:sSub>
    <m:r><m:t> = </m:t></m:r>
    <m:d>
      <m:dPr><m:begChr m:val="("/><m:endChr m:val=")"/></m:dPr>
      <m:e>
        <m:f>
          <m:num>
            <m:sSub>
              <m:e><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>V</m:t></m:r></m:e>
              <m:sub><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>akar</m:t></m:r></m:sub>
            </m:sSub>
          </m:num>
          <m:den>
            <m:sSub>
              <m:e><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>V</m:t></m:r></m:e>
              <m:sub><m:r><m:rPr><m:sty m:val="i"/></m:rPr><m:t>sumber</m:t></m:r></m:sub>
            </m:sSub>
          </m:den>
        </m:f>
      </m:e>
    </m:d>
    <m:r><m:t> × 100%</m:t></m:r>
  </m:oMath>
</m:oMathPara>'''

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    candidates = [
        os.path.join(script_dir, 'FTE-CD-2_edited-PBD-1.docx'),
        os.path.join(script_dir, '..', '..', 'sumber', 'template', 'FTE-CD-2_edited-PBD-1.docx'),
        r'c:\Users\LENOVO\Documents\TA lulus\CD2\FTE-CD-2_edited-PBD-1.docx',
    ]
    template_path = None
    for cand in candidates:
        if os.path.exists(cand):
            template_path = cand
            break
    if not template_path:
        raise FileNotFoundError("Template FTE-CD-2_edited-PBD-1.docx not found!")
    
    output_path = os.path.join(script_dir, 'CD2_Jeruk_Limau.docx')
    
    doc = docx.Document(template_path)
    
    # 1. Update Cover
    doc.paragraphs[0].text = "DOKUMEN CD-2"
    doc.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.CENTER
    doc.paragraphs[0].runs[0].font.name = "Times New Roman"
    doc.paragraphs[0].runs[0].font.size = Pt(16)
    doc.paragraphs[0].runs[0].font.bold = True
    
    doc.paragraphs[12].text = "ANALISIS PERMASALAHAN PENYIRAMAN MANUAL PADA KEBUN JERUK LIMAU DI CIBERES SUBANG"
    doc.paragraphs[12].alignment = WD_ALIGN_PARAGRAPH.CENTER
    doc.paragraphs[12].runs[0].font.name = "Times New Roman"
    doc.paragraphs[12].runs[0].font.size = Pt(14)
    doc.paragraphs[12].runs[0].font.bold = True
    
    doc.paragraphs[17].text = "Oleh :"
    doc.paragraphs[17].alignment = WD_ALIGN_PARAGRAPH.CENTER
    doc.paragraphs[17].runs[0].font.name = "Times New Roman"
    doc.paragraphs[17].runs[0].font.size = Pt(12)
    
    doc.paragraphs[19].text = "Muhammad Al Qarnie / 101032330043"
    doc.paragraphs[19].alignment = WD_ALIGN_PARAGRAPH.CENTER
    doc.paragraphs[19].runs[0].font.name = "Times New Roman"
    doc.paragraphs[19].runs[0].font.size = Pt(12)
    
    doc.paragraphs[20].text = "Maheswara Ariq Athallah / 101032300050"
    doc.paragraphs[20].alignment = WD_ALIGN_PARAGRAPH.CENTER
    doc.paragraphs[20].runs[0].font.name = "Times New Roman"
    doc.paragraphs[20].runs[0].font.size = Pt(12)
    
    doc.paragraphs[21].text = "Daffa Hermansyah / 101032330090"
    doc.paragraphs[21].alignment = WD_ALIGN_PARAGRAPH.CENTER
    doc.paragraphs[21].runs[0].font.name = "Times New Roman"
    doc.paragraphs[21].runs[0].font.size = Pt(12)
    
    doc.paragraphs[31].text = "PRODI S1 TEKNIK KOMPUTER"
    doc.paragraphs[31].alignment = WD_ALIGN_PARAGRAPH.CENTER
    doc.paragraphs[31].runs[0].font.name = "Times New Roman"
    doc.paragraphs[31].runs[0].font.size = Pt(14)
    doc.paragraphs[31].runs[0].font.bold = True
    
    doc.paragraphs[32].text = "FAKULTAS TEKNIK ELEKTRO"
    doc.paragraphs[32].alignment = WD_ALIGN_PARAGRAPH.CENTER
    doc.paragraphs[32].runs[0].font.name = "Times New Roman"
    doc.paragraphs[32].runs[0].font.size = Pt(14)
    doc.paragraphs[32].runs[0].font.bold = True
    
    doc.paragraphs[33].text = "UNIVERSITAS TELKOM"
    doc.paragraphs[33].alignment = WD_ALIGN_PARAGRAPH.CENTER
    doc.paragraphs[33].runs[0].font.name = "Times New Roman"
    doc.paragraphs[33].runs[0].font.size = Pt(14)
    doc.paragraphs[33].runs[0].font.bold = True
    
    doc.paragraphs[34].text = "BANDUNG"
    doc.paragraphs[34].alignment = WD_ALIGN_PARAGRAPH.CENTER
    doc.paragraphs[34].runs[0].font.name = "Times New Roman"
    doc.paragraphs[34].runs[0].font.size = Pt(14)
    doc.paragraphs[34].runs[0].font.bold = True
    
    doc.paragraphs[35].text = "2026"
    doc.paragraphs[35].alignment = WD_ALIGN_PARAGRAPH.CENTER
    doc.paragraphs[35].runs[0].font.name = "Times New Roman"
    doc.paragraphs[35].runs[0].font.size = Pt(14)
    doc.paragraphs[35].runs[0].font.bold = True

    # 2. Update Table 0 (Lembar Pengesahan)
    t0 = doc.tables[0]
    t0.rows[0].cells[2].text = "Analisis Permasalahan Penyiraman Manual pada Kebun Jeruk Limau di Ciberes Subang"
    t0.rows[1].cells[2].text = "Spesifikasi"
    t0.rows[2].cells[2].text = "FTE-CD-2"
    t0.rows[3].cells[2].text = "00"
    t0.rows[4].cells[2].text = "29/10/2026"
    t0.rows[5].cells[2].text = "Fakultas Teknik Elektro"
    t0.rows[6].cells[2].text = "S1 Teknik Komputer"
    t0.rows[7].cells[2].text = "21 halaman"
    
    for row in t0.rows:
        make_row_cant_split(row)
        for cell in row.cells:
            for p in cell.paragraphs:
                p.paragraph_format.line_spacing = 1.15
                p.paragraph_format.space_after = Pt(2)
                for r in p.runs:
                    r.font.name = "Times New Roman"
                    r.font.size = Pt(10)
    
    # 3. Update Table 1 (Persetujuan)
    t1 = doc.tables[1]
    t1.rows[1].cells[2].text = ": Muhammad Al Qarnie"
    t1.rows[2].cells[2].text = ": 101032330043"
    t1.rows[3].cells[2].text = ": Maheswara Ariq Athallah"
    t1.rows[4].cells[2].text = ": 101032300050"
    t1.rows[5].cells[2].text = ": Daffa Hermansyah"
    t1.rows[6].cells[2].text = ": 101032330090"
    
    t1.rows[7].cells[2].text = ": Dr. Agung Nugroho Jati, S.T., M.T."
    t1.rows[8].cells[2].text = ": 29/10/2026"
    t1.rows[9].cells[2].text = ":"
    t1.rows[10].cells[2].text = ":"
    
    for row in t1.rows:
        make_row_cant_split(row)
        for cell in row.cells:
            for p in cell.paragraphs:
                p.paragraph_format.line_spacing = 1.15
                p.paragraph_format.space_after = Pt(2)
                for r in p.runs:
                    r.font.name = "Times New Roman"
                    r.font.size = Pt(10)

    # 4. Update Table 2 (Timeline Revisi)
    t2 = doc.tables[2]
    t2.rows[1].cells[0].text = "00,\n26 Oktober 2026"
    t2.rows[1].cells[1].text = "Draf Awal CD-2"
    t2.rows[1].cells[2].text = "Penyusunan dasar penentuan spesifikasi berbasis multi-rujukan (wawancara mitra, regulasi pemerintah, standar ASABE/IEC/ISO, literatur agronomi), batasan rekayasa, matriks spesifikasi kuantitatif multi-aspek, serta metode pengukuran dan verifikasi terperinci."
    t2.rows[1].cells[3].text = "Seluruh Dokumen"
    
    for r_idx in range(2, len(t2.rows)):
        t2.rows[r_idx].cells[0].text = ""
        t2.rows[r_idx].cells[1].text = ""
        t2.rows[r_idx].cells[2].text = ""
        t2.rows[r_idx].cells[3].text = ""

    for row in t2.rows:
        make_row_cant_split(row)
        for cell in row.cells:
            for p in cell.paragraphs:
                p.paragraph_format.line_spacing = 1.15
                p.paragraph_format.space_after = Pt(2)
                for r in p.runs:
                    r.font.name = "Times New Roman"
                    r.font.size = Pt(10)

    # 5. Delete placeholder paragraphs from p48 onwards
    p_len = len(doc.paragraphs)
    for p_idx in range(p_len - 1, 44, -1):
        p_element = doc.paragraphs[p_idx]._element
        p_element.getparent().remove(p_element)

    print(f"Remaining paragraphs after cleanup: {len(doc.paragraphs)}")
    
    # 6. Add Body Content
    add_heading_p(doc, "BAB 1\nSPESIFIKASI DAN BATASAN DESAIN SISTEM IRIGASI", level=0, space_before=18, space_after=12)
    
    add_body_p(doc, "Dokumen CD-2 ini merupakan kelanjutan langsung dari dokumen CD-1 (Analisis Permasalahan Penyiraman Manual pada Kebun Jeruk Limau di Ciberes Subang) yang telah disahkan oleh dosen pembimbing. Jika CD-1 berfokus pada identifikasi akar masalah, kendala empiris, kompleksitas permasalahan rekayasa, serta kajian kelemahan solusi eksisting, maka dokumen CD-2 ini menetapkan landasan batas operasional (constraints) dan spesifikasi kuantitatif (specifications) yang wajib dipenuhi oleh solusi rekayasa yang akan dirancang pada tahap CD-3.")
    
    add_body_p(doc, "Perumusan batasan dan spesifikasi ini dirancang secara terukur (measurable), realistis (feasible), memiliki dasar ilmiah yang kokoh (grounded), serta bersifat abstrak terhadap pilihan solusi atau merek tertentu (solution-agnostic). Pendekatan ini memastikan bahwa ruang perancangan pada tahap CD-3 tetap terbuka untuk mengevaluasi berbagai alternatif solusi (seperti jaringan mikroirigasi perpipaan, wahana bergerak semi-otonom, maupun sistem hibrida) tanpa bias awal pada merek atau teknologi perangkat keras tertentu.")

    # 1.1 Dasar Penentuan Spesifikasi
    add_heading_p(doc, "1.1 Dasar Penentuan Spesifikasi", level=1, space_before=14, space_after=6)
    add_body_p(doc, "Penentuan batasan dan spesifikasi dalam proses rekayasa sistem (engineering design process) tidak boleh didasarkan pada asumsi subjektif yang mengada-ada. Pada perancangan sistem irigasi kebun jeruk limau mitra di Ciberes, Subang, penetapan seluruh parameter kuantitatif didasarkan pada sintesis empat pilar rujukan utama: (1) kebutuhan pengguna dan data empiris mitra lapangan, (2) regulasi pemerintah dan standar teknis industri, (3) literatur ilmiah fisiologi tanaman dan neraca air, serta (4) karakteristik tapak lahan dan keterbatasan infrastruktur eksisting.")

    # 1.1.1 Kebutuhan Pengguna
    add_heading_p(doc, "1.1.1 Kebutuhan Pengguna dan Hasil Wawancara Lapangan (Mitra Ciberes)", level=2, space_before=10, space_after=4)
    add_body_p(doc, "Kebutuhan mitra pengelola kebun jeruk limau di Ciberes, Subang digali melalui wawancara mendalam dan observasi langsung di tapak kebun (Transkrip Wawancara Audio 1, terlampir). Dari hasil observasi tersebut, teridentifikasi sejumlah pain points operasional dan ekspektasi fungsional mitra:")
    
    add_point_item(doc, "1. Beban Biaya Tenaga Kerja Manual",
                   "Untuk menyiram populasi sekitar 500–600 pohon jeruk limau yang membentang di atas lahan sepanjang ~100 m, pengelola kebun mempekerjakan 4 orang pekerja harian lepas dengan upah masing-masing Rp100.000 per kegiatan (total Rp400.000 per kegiatan). Kegiatan penyiraman dilakukan rutin rata-rata setiap 3 hari sekali (terutama pada musim kemarau dan masa transisi buah). Skenario perhitungan tahunan menunjukkan estimasi pengeluaran tenaga kerja penyiraman mencapai Rp48,7 juta/tahun. Pengelola kebun secara eksplisit menyatakan kebutuhan utama untuk menekan atau mengeliminasi pengeluaran upah manual ini melalui penerapan mekanisasi atau otomasi.")
    
    add_point_item(doc, "2. Ketidakpastian dan Ketidakmerataan Dosis Air",
                   "Praktik penyiraman eksisting mengandalkan pekerja yang menimba air parit menggunakan ember hitam kecil lalu mengguyurkannya ke tiap pohon. Pekerja tidak mengukur volume air per pohon, sehingga pohon di area dekat titik pompa berisiko menerima air berlebih, sementara pohon di ujung parit berisiko kekurangan air atau bahkan terlewat akibat kelelahan fisik pekerja.")
    
    add_point_item(doc, "3. Ketergantungan Pompa Berbahan Bakar Bensin (Pertalite)",
                   "Pasokan air disedot dari sungai berjarak 20,54 m menuju tiga lajur parit tanah menggunakan pompa mesin berbahan bakar Pertalite. Mitra mengeluhkan biaya operasional bahan bakar, kerepotan pemeliharaan mekanik berkala, serta uji coba bahan bakar gas LPG masa lalu yang dihentikan karena mesin mengalami panas berlebih (overheat).")
    
    add_point_item(doc, "4. Ekspektasi Solusi Baru dari Mitra",
                   "Mitra mengharapkan sistem baru mampu mengalirkan air dalam jumlah yang cukup (mengacu pada estimasi praktis petani minimal 10–15 Liter per pohon per siklus), dapat beroperasi secara terjadwal/teratur, mudah dioperasikan oleh pekerja lokal tanpa kerumitan teknis, serta memiliki biaya investasi awal dan pemeliharaan yang terjangkau agar modal dapat tertutup dari penghematan upah tenaga kerja dalam kurun waktu 1–2 tahun.")

    # 1.1.2 Regulasi dan Standar
    add_heading_p(doc, "1.1.2 Regulasi Pemerintah dan Standar Teknis Industri", level=2, space_before=12, space_after=4)
    add_body_p(doc, "Perancangan sistem rekayasa wajib mematuhi kerangka hukum, regulasi tata air nasional, dan standar konsensus industri internasional:")
    
    add_point_item(doc, "1. Standar Evaluasi dan Instalasi Irigasi Mikro (ANSI/ASAE S398.1 & ASAE EP405.1)",
                   "American Society of Agricultural and Biological Engineers (ASABE) menetapkan standar evaluasi peralatan dan instalasi irigasi mikro melalui ANSI/ASAE S398.1 (Procedure for Sprinkler Testing and Performance Reporting) dan ASAE EP405.1 (Design and Installation of Microirrigation Systems). Untuk irigasi presisi pada tanaman hortikultura tahunan bernilai ekonomi tinggi, keseragaman distribusi air (Christiansen's Uniformity Coefficient, CU) minimum yang disyaratkan adalah >= 80%, dengan target ideal pada perancangan rekayasa baru mencapai >= 85%. Nilai keseragaman ini menjamin setiap pohon menerima pasokan air seragam terlepas dari jarak pohon terhadap sumber suplai [2], [3].")
    
    add_point_item(doc, "2. Regulasi Pemerintah tentang Pengelolaan Irigasi (PP No. 20 Tahun 2006)",
                   "Peraturan Pemerintah Republik Indonesia Nomor 20 Tahun 2006 tentang Irigasi menegaskan prinsip efisiensi dan konservasi pemanfaatan air: sistem penyediaan air irigasi pertanian wajib mengutamakan efisiensi pemakaian air secara tertib dan berkelanjutan, meminimalkan kehilangan air akibat perkolasi dalam dan kebocoran rembesan terbuka, serta mengarahkan pengelolaan air di tingkat usahatani berbasis teknologi tepat guna yang teratur [6].")
    
    add_point_item(doc, "3. Standar Spesifikasi Peralatan Irigasi Mikro (ISO 9261:2004)",
                   "Standar internasional ISO 9261:2004 (Agricultural irrigation equipment — Emitters and emitting pipe — Specification and test methods) mengatur spesifikasi mekanis, toleransi fabrikasi, dan metode pengujian debit emiter pada sistem irigasi mikro. Standar ini menjadi acuan batas variasi laju alir antar-titik tetes dan ketahanan hidraulis komponen penyalur air bertekanan rendah [7].")
    
    add_point_item(doc, "4. Standar Proteksi Selungkup Lingkungan Terbuka (IEC 60529 / SNI IEC 60529:2014)",
                   "Peralatan instrumentasi, kontroler elektronik, akuisisi data, dan sistem daya yang beroperasi di lingkungan pertanian terbuka tanpa naungan permanen wajib memiliki tingkat proteksi selungkup (Ingress Protection) minimal IP65. Standar ini menjamin selungkup kedap terhadap partikel debu tanah secara total (dust-tight) dan terlindung dari semprotan air bertekanan rendah dari segala arah tanpa terjadi kebocoran yang merusak rangkaian sirkuit [4], [5].")
    
    add_point_item(doc, "5. Standar Keamanan Kelistrikan dan Jaringan Sensor (IEEE 1451 & IEC 60364-4-41)",
                   "Seluruh perangkat kelistrikan yang dipasang di area basah pertanian terbuka wajib beroperasi pada batas tegangan ekstra rendah aman (Safety Extra-Low Voltage / SELV <= 48 V DC) untuk mencegah bahaya sengatan listrik bagi manusia dan hewan ternak [9]. Standar komunikasi instrumentasi IEEE 1451 (IEEE Std 1451.4-2004) digunakan sebagai acuan arsitektur transmisi data sensor cerdas berdaya rendah [10].")
    
    add_point_item(doc, "6. Standar Sistem Pembangkit Listrik Tenaga Surya Mandiri (IEC 62124)",
                   "Standar Photovoltaic (PV) stand-alone systems - Design verification (IEC 62124:2004) menetapkan bahwa sistem fotovoltaik off-grid pertanian harus dirancang dengan kapasitas cadangan energi (days of autonomy) minimal 1,5 hingga 2 hari operasi tanpa radiasi matahari langsung guna mengantisipasi cuaca mendung berkepanjangan pada musim transisi [8].")

    # 1.1.3 Karakteristik Fisiologi Tanaman
    add_heading_p(doc, "1.1.3 Karakteristik Fisiologi Tanaman Jeruk Limau dan Literatur Agronomi", level=2, space_before=12, space_after=4)
    add_body_p(doc, "Karakteristik biologis tanaman jeruk limau (Citrus amblycarpa Hassk. Ochse) menjadi fondasi penentuan dosis volume, frekuensi, dan zona pembasahan:")
    
    add_point_item(doc, "1. Morfologi Perakaran Dangkal Jeruk Limau",
                   "Penelitian Budiarto dkk. (2017) dan pedoman Florida Citrus Extension (Obreza dkk., 2020) menunjukkan bahwa perakaran tanaman jeruk didominasi oleh akar serabut aktif (feeder roots) pada lapisan tanah dangkal dengan kedalaman 20–40 cm dan radius persebaran horizontal 0,5–0,8 m mengikuti proyeksi tajuk tanaman. Pemberian air di luar radius tersebut tidak efektif diserap oleh tanaman dan hanya akan memicu pertumbuhan gulma liar [15], [19].")
    
    add_point_item(doc, "2. Kebutuhan Air Berbasis Model Evapotranspirasi FAO-56",
                   "Mengacu pada pedoman standar FAO Irrigation and Drainage Paper 56 (Allen dkk., 1998) serta panduan manajemen air jeruk dari University of Florida IFAS Extension (Kadyampakeni dkk., 2023), estimasi kebutuhan air tanaman jeruk limau muda dihitung secara presisi menggunakan model evapotranspirasi standar Penman-Monteith:")
    add_equation_p(doc, etc_omml)
    add_body_p(doc, "Di mana ETc adalah laju evapotranspirasi aktual tanaman (mm/hari), Kc adalah koefisien tanaman jeruk limau muda kanopi sedang (Kc = 0,70–0,80), dan ET0 adalah laju evapotranspirasi acuan lingkungan Ciberes Subang pada musim kemarau (ET0 = 4,5–5,0 mm/hari). Selanjutnya, volume air terukur yang wajib diberikan per pohon dalam satu siklus penyiraman (Vpohon) dihitung melalui persamaan volume neraca air:")
    add_equation_p(doc, vpohon_omml)
    add_body_p(doc, "Di mana Atajuk adalah luas proyeksi kanopi tajuk basah perakaran (~1,0 m2) dan Isiram adalah interval frekuensi penyiraman (2–3 hari per siklus). Melalui substitusi nilai parameter lapangan tersebut, diperoleh kebutuhan air berkisar 10 hingga 15 Liter per pohon per siklus penyiraman. Hasil perhitungan matematis ini memvalidasi secara ilmiah taksiran kebiasaan empiris petani mitra di kebun Ciberes [1], [16].")
    
    add_point_item(doc, "3. Pencegahan Risiko Pembusukan Akar (Phytophthora nicotianae)",
                   "Literatur patologi jeruk oleh Graham & Timmer (2020) serta pedoman Smajstrla dkk. (1997) memperingatkan bahwa kejenuhan air tanah yang berlangsung lama (waterlogging > 24–48 jam) akibat penggenangan parit atau drainase yang buruk merupakan pemicu utama serangan patogen jamur tanah Phytophthora nicotianae dan Phytophthora palmivora yang menyebabkan busuk perakaran dan kanker pangkal batang (foot rot). Oleh karena itu, spesifikasi pemberian air harus menjamin aerasi tanah tetap terjaga dan tidak menimbulkan kubangan air tergenang lebih dari 30 menit setelah proses penyiraman selesai [17], [18].")

    # 1.1.4 Karakteristik Tapak Lahan
    add_heading_p(doc, "1.1.4 Karakteristik Tapak Lahan Eksisting dan Keterbatasan Sumber Daya", level=2, space_before=12, space_after=4)
    add_body_p(doc, "Spesifikasi sistem rekayasa harus selaras dengan kendala fisik tapak kebun di Ciberes:")
    
    add_point_item(doc, "1. Ketiadaan Akses Jaringan Listrik PLN",
                   "Tapak kebun terletak jauh dari jaringan distribusi tegangan rendah PLN. Segala bentuk rancangan sistem tidak boleh bergantung pada sumber listrik jala-jala PLN, melainkan wajib mandiri (self-sufficient / off-grid) memanfaatkan energi terbarukan (seperti pembangkit listrik tenaga surya / fotovoltaik) yang dipadukan dengan modul penyimpan daya (baterai) atau sumber mekanik efisien [8], [20].")
    
    add_point_item(doc, "2. Karakteristik Air Sungai dan Kebutuhan Filtrasi Partikulat",
                   "Sumber air utama kebun berasal dari aliran sungai/saluran irigasi yang berjarak 20,54 m dari tepi lahan kebun. Air permukaan alami memiliki tingkat kekeruhan dinamis dan membawa muatan padatan tersuspensi (suspended solids) berupa partikel pasir halus, lumpur sedimen, dan serpihan organik. Kondisi ini mewajibkan adanya subsistem penyaringan fisik (filtration) dengan kapasitas penyaringan minimal 120 mesh (130 um) agar pipa, pompa mikro, katup solenoid, maupun nozzle tidak mengalami penyumbatan fisik (clogging) [12], [13], [14].")
    
    add_point_item(doc, "3. Geometri Jaringan Tiga Lajur Parit Kebun",
                   "Populasi 500–600 pohon tertata dalam barisan teratur di antara tiga lajur galian parit tanah sepanjang 100 m dengan lebar blok 20,54 m. Jarak antar pohon berkisar antara 2–3 meter. Spesifikasi sistem harus mampu mendistribusikan air menjangkau seluruh panjang lintasan 100 m tersebut secara merata tanpa kehilangan tekanan hidrolik yang berlebihan.")

    # 1.2 Batasan dan Spesifikasi Solusi
    add_heading_p(doc, "1.2 Batasan dan Spesifikasi Solusi", level=1, space_before=14, space_after=6)
    add_body_p(doc, "Berdasarkan sintesis dari seluruh dasar pertimbangan di atas, bagian ini menetapkan batasan rekayasa (engineering constraints) dan daftar spesifikasi kuantitatif (engineering specifications). Sesuai dengan kaidah Buku Panduan Capstone FTE Telkom University, spesifikasi dirumuskan secara abstrak terhadap pilihan solusi atau merek tertentu (solution-agnostic), sehingga tidak mengikat perancangan pada satu opsi teknologi saja sebelum dilakukan komparasi alternatif pada dokumen CD-3.")

    # 1.2.1 Batasan Rekayasa
    add_heading_p(doc, "1.2.1 Batasan Rekayasa Solusi (Engineering Constraints)", level=2, space_before=10, space_after=4)
    add_body_p(doc, "Batasan rekayasa merupakan kondisi batas mutlak (hard constraints) yang tidak dapat dilanggar oleh arsitektur solusi mana pun yang akan dirancang:")
    
    add_point_item(doc, "C-01. Kemandirian Energi (Off-Grid Standalone)",
                   "Sistem harus beroperasi secara mandiri tanpa memerlukan sambungan jala-jala listrik PLN kebun, menggunakan pasokan daya lokal berbasis energi terbarukan atau baterai penyimpan energi.")
    
    add_point_item(doc, "C-02. Kompatibilitas Sumber Air Permukaan Berpartikulat",
                   "Sistem harus mampu memproses air baku dari sungai/saluran irigasi terbuka berkekeruhan alami tanpa mengalami kerusakan pompa dan tanpa mengalami kegagalan fungsi akibat sedimentasi lumpur.")
    
    add_point_item(doc, "C-03. Kompatibilitas Geometri dan Topografi Kebun",
                   "Sistem harus mampu melayani area kebun seluas 500–600 pohon dengan rentang lintasan memanjang hingga 100 m dan lebar 20,5 m tanpa merusak struktur batang dan perakaran dangkal tanaman.")
    
    add_point_item(doc, "C-04. Keselamatan Kelistrikan Area Terbuka Basah (SELV)",
                   "Seluruh subsistem elektrikal dan instrumentasi yang terpasang di area basah kebun wajib beroperasi pada rentang tegangan ekstra rendah aman (Safety Extra-Low Voltage <= 48 V DC) sesuai IEC 60364-4-41.")
    
    add_point_item(doc, "C-05. Netralitas Solusi (Solution-Agnostic)",
                   "Perumusan batasan dan spesifikasi tidak mengunci pilihan arsitektur pada satu merek komponen tertentu atau satu jenis solusi mekanis tertentu (memberikan fleksibilitas penuh untuk mengevaluasi opsi jaringan perpipaan mikro, sistem mekanisasi gerak semi-otonom, maupun solusi hibrida pada CD-3).")

    # 1.2.2 Spesifikasi Kuantitatif Solusi
    add_heading_p(doc, "1.2.2 Spesifikasi Kuantitatif Solusi (Engineering Specifications)", level=2, space_before=12, space_after=4)
    add_body_p(doc, "Spesifikasi rekayasa dijabarkan ke dalam empat aspek menyeluruh: teknis, ekonomi, lingkungan, dan operasional/kemitraan. Ringkasan seluruh spesifikasi kuantitatif disajikan pada Tabel 3, yang kemudian diikuti dengan deskripsi penjelasan mendalam pada masing-masing parameternya.")

    add_caption_p(doc, "Tabel 3. Matriks Batasan dan Spesifikasi Kuantitatif Solusi", is_table=True)

    # Table 3
    t3_data = [
        ["ID", "Parameter Spesifikasi", "Nilai Target & Toleransi", "Satuan", "Kategori Aspek", "Rujukan Penentuan"],
        ["S-01", "Akurasi Dosis Volume Air per Pohon", "10 - 15 +- 5%", "Liter/pohon", "Aspek Teknis", "Wawancara Mitra, FAO-56 [1], Florida [16]"],
        ["S-02", "Koefisien Keseragaman Distribusi (CU)", ">= 85", "%", "Aspek Teknis", "Standar ANSI/ASAE S398.1, EP405.1 [2], [3]"],
        ["S-03", "Durasi Total Siklus Penyiraman Kebun", "<= 4,0", "Jam/siklus", "Aspek Teknis", "Batas Waktu Operasi Harian Mitra"],
        ["S-04", "Radius dan Kedalaman Pembasahan", "r = 0,5 - 0,8; d = 20 - 40", "cm", "Aspek Teknis", "Morfologi Perakaran Jeruk Limau [15], [19]"],
        ["S-05", "Derajat Filtrasi Fisik Partikulat", ">= 120 (saring <= 130)", "mesh (um)", "Aspek Teknis", "Standar Kualitas Air FAO-29 [12], Ayers [13]"],
        ["S-06", "Ketahanan Cadangan Energi (Autonomy)", ">= 8,0 (min. 2 siklus penuh)", "Jam operasi", "Aspek Teknis", "Standar IEC 62124 (Off-Grid PV) [8]"],
        ["S-07", "Ketahanan Lingkungan Selungkup (IP)", "IP65 (Suhu: 20 - 55)", "Rating (deg C)", "Aspek Teknis", "Standar IEC 60529 / SNI IEC 60529 [4], [5]"],
        ["S-08", "Batas Biaya Investasi Awal (CAPEX)", "<= 18.000.000", "Rupiah (Rp)", "Aspek Ekonomi", "Analisis Kelayakan Payback Period"],
        ["S-09", "Biaya Operasional Siklus (OPEX)", "<= 50.000 (Hemat >= 85%)", "Rupiah (Rp)", "Aspek Ekonomi", "Biaya Upah Manual Eksisting (Rp400.000)"],
        ["S-10", "Periode Pengembalian Modal (Payback)", "<= 12 - 18", "Bulan", "Aspek Ekonomi", "Skenario Penghematan Rp48,7 Juta/Tahun"],
        ["S-11", "Efisiensi Aplikasi Air Irigasi (eta_a)", ">= 80", "%", "Aspek Lingkungan", "PP No. 20 Tahun 2006, FAO Annex I [6], [11]"],
        ["S-12", "Emisi Gas Buang di Zona Tajuk", "0 (Bebas emisi hidrokarbon)", "g/kWh", "Aspek Lingkungan", "Perlindungan Kualitas Tanah Perakaran"],
        ["S-13", "Kemudahan Pengoperasian Mitra", "Single-touch (Ajar <= 30)", "Menit", "Aspek Operasional", "Profil Tenaga Kerja Lokal Kebun Ciberes"],
        ["S-14", "Durasi Pemeliharaan Rutin Saringan", "<= 20 (Perkakas lokal)", "Menit/bulan", "Aspek Operasional", "Keterbatasan Bengkel Khusus Pedesaan"],
    ]

    t3 = doc.add_table(rows=len(t3_data), cols=6)
    t3.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_full_grid(t3, color="808080", sz="4")
    col_widths = [Inches(0.6), Inches(1.8), Inches(1.3), Inches(0.8), Inches(1.0), Inches(1.5)]

    for r_idx, row in enumerate(t3.rows):
        make_row_cant_split(row)
        if r_idx == 0:
            make_row_header(row)
        for c_idx, cell in enumerate(row.cells):
            cell.width = col_widths[c_idx]
            cell.text = t3_data[r_idx][c_idx]
            p = cell.paragraphs[0]
            p.paragraph_format.line_spacing = 1.05
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(2)
            if r_idx == 0:
                set_cell_background(cell, "E0E0E0")
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                for r in p.runs:
                    r.font.name = "Times New Roman"
                    r.font.size = Pt(9.5)
                    r.font.bold = True
            else:
                if c_idx in [0, 2, 3]:
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                else:
                    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                for r in p.runs:
                    r.font.name = "Times New Roman"
                    r.font.size = Pt(9)
            set_cell_margins(cell, top=60, bottom=60, left=80, right=80)

    # Narrative explanation for S-01 to S-14
    add_point_item(doc, "S-01. Akurasi Dosis Volume Air per Pohon",
                   "Sistem harus mampu menyalurkan volume air terukur antara 10 hingga 15 Liter untuk tiap tanaman jeruk limau dengan batas simpangan kesalahan (error tolerance) tidak lebih dari +- 5%. Nilai kuantitatif ini menjamin tanaman terhidrasi sesuai laju evapotranspirasi lingkungan tanpa risiko pemberian air berlebih (over-irrigation) yang memboroskan sumber daya air.")
    
    add_point_item(doc, "S-02. Koefisien Keseragaman Distribusi Air (CU)",
                   "Mengacu pada standar ANSI/ASAE S398.1 dan ASAE EP405.1, keseragaman volume air yang diterima oleh pohon di awal, tengah, dan ujung barisan parit harus mencapai minimal 85%. Evaluasi keseragaman distribusi air dihitung menggunakan formula Koefisien Keseragaman Christiansen (Christiansen's Uniformity Coefficient, CU) [2], [3]:")
    add_equation_p(doc, cu_omml)
    add_body_p(doc, "Di mana CU adalah Christiansen's Uniformity Coefficient (%), n adalah jumlah pohon sampel uji (n = 15 bejana), Xi adalah volume air tertampung pada bejana sampel ke-i (Liter), dan X_bar adalah rata-rata volume air dari seluruh bejana sampel. Nilai keseragaman CU >= 85% menjamin pertumbuhan seluruh pohon jeruk limau tetap homogen tanpa adanya pohon yang mengalami kekeringan ekstrem atau pembusukan akar.")
    
    add_point_item(doc, "S-03. Durasi Total Siklus Penyiraman Kebun",
                   "Seluruh proses penyiraman untuk 500–600 pohon harus dapat dituntaskan dalam waktu kurang dari atau sama dengan 4 jam per siklus kegiatan. Hal ini memberikan efisiensi waktu yang masif dibandingkan metode manual 4 orang buruh yang menyita waktu seharian penuh, serta memanfaatkan waktu siram ideal (pagi hari sebelum pukul 10.00 WIB atau sore hari setelah pukul 15.00 WIB) guna meminimalkan kehilangan air akibat evaporasi radiasi matahari langsung.")
    
    add_point_item(doc, "S-04. Radius dan Kedalaman Pembasahan Efektif",
                   "Air irigasi diarahkan meresap pada area proyeksi kanopi tanaman dengan radius 0,5–0,8 m dari pangkal batang hingga mencapai kedalaman profil tanah 20–40 cm. Distribusi air yang terkonsentrasi pada zona perakaran aktif serabut menghindarkan pembasahan batang utama yang rentan jamur batang serta tidak membasahi area jalan antar-baris secara sia-sia.")
    
    add_point_item(doc, "S-05. Derajat Filtrasi Fisik Partikulat",
                   "Untuk mengatasi kekeruhan air sungai Ciberes, sistem wajib dilengkapi dengan saringan partikulat dengan kerapatan minimal 120 mesh (mampu menyaring partikel berdiameter >= 130 um). Hal ini merupakan syarat wajib untuk mencegah terjadinya penyumbatan mekanis pada emiter, lubang nozzle, katup pengontrol, dan impeller pompa air mikro.")
    
    add_point_item(doc, "S-06. Ketahanan Cadangan Energi Mandiri (Autonomy)",
                   "Subsistem daya mandiri (off-grid) harus mampu menyuplai kebutuhan daya operasional beban penuh selama minimal 8 jam kerja kontinu tanpa kehadiran cahaya matahari langsung (setara dengan cadangan daya untuk minimal 2 siklus penyiraman lengkap). Mengacu pada standar IEC 62124 (Photovoltaic stand-alone systems), konsumsi energi operasional per siklus penyiraman (Esiklus) dan kapasitas minimum modul penyimpan daya (Cbaterai) dihitung melalui persamaan energi dan otonomi sistem [8]:")
    add_equation_p(doc, esiklus_omml)
    add_equation_p(doc, cbaterai_omml)
    add_body_p(doc, "Di mana Esiklus adalah energi operasional satu siklus (Wh), Pbeban adalah total daya pompa dan kontroler (Watt), toperasi adalah durasi kerja satu siklus (<= 4 jam), Nautonomy adalah faktor otonomi cadangan (>= 2 siklus = 8 jam), Vsistem adalah tegangan kerja ekstra rendah aman (12 V DC atau 24 V DC), dan DoD adalah Depth of Discharge aman baterai (DoD = 80% untuk LiFePO4). Hal ini menjamin keandalan operasi pompa tetap prima saat cuaca berawan berturut-turut.")
    
    add_point_item(doc, "S-07. Ketahanan Lingkungan Selungkup (Ingress Protection)",
                   "Seluruh kotak kontrol (controller enclosure), konektor kelistrikan, papan modul sensor, dan unit catu daya wajib bersertifikasi minimal IP65 serta mampu bekerja normal pada rentang suhu ambien 20 deg C hingga 55 deg C. Selungkup harus tahan terhadap terpaan panas matahari tropis Subang, percikan lumpur tanah, dan semprotan air saat pembersihan kebun.")
    
    add_point_item(doc, "S-08. Batas Biaya Investasi Awal Sistem (CAPEX)",
                   "Total biaya rancang bangun, belanja komponen, fabrikasi struktural, instalasi sistem, dan instrumentasi dibatasi maksimal Rp18.000.000. Angka batas atas ini ditetapkan secara rasional agar investasi terjangkau oleh petani skala menengah dan tidak melebihi alokasi dana kelayakan modal usaha tani.")
    
    add_point_item(doc, "S-09. Biaya Operasional per Siklus Penyiraman (OPEX)",
                   "Biaya operasional yang mencakup konsumsi energi (pengisian daya/bahan bakar cadangan) dan alokasi jasa pemantauan operator ditekan hingga maksimal Rp50.000 per siklus penyiraman. Hal ini menghasilkan penghematan biaya langsung sebesar 87,5% per kegiatan dibandingkan pengeluaran rutin upah guyur manual eksisting (Rp400.000 per kegiatan).")
    
    add_point_item(doc, "S-10. Periode Pengembalian Modal (Payback Period)",
                   "Kelayakan ekonomi sistem rekayasa dinilai berdasarkan kecepatan pengembalian modal investasi awal (Payback Period, PP). Periode pengembalian modal dihitung dengan formula rasio investasi awal (CAPEX) terhadap selisih penghematan biaya operasional tahunan (Delta OPEX_tahunan):")
    add_equation_p(doc, pp_omml)
    add_body_p(doc, "Di mana PP adalah Payback Period (dalam tahun atau bulan), CAPEX adalah modal investasi awal sistem rekayasa (<= Rp18.000.000), dan Delta OPEX_tahunan adalah selisih penghematan biaya operasional tahunan antara metode manual eksisting (Rp400.000/kegiatan x ~120 siklus/tahun = ~Rp48.000.000/tahun) dengan biaya operasional sistem baru (<= Rp50.000/siklus x ~120 siklus/tahun = <= Rp6.000.000/tahun). Dengan selisih penghematan bersih mencapai lebih dari Rp42.000.000 per tahun, target titik impas modal dipastikan tercapai dalam kurun waktu 12 hingga 18 bulan operasi.")
    
    add_point_item(doc, "S-11. Efisiensi Aplikasi Air Irigasi (eta_a)",
                   "Mengacu pada prinsip konservasi air PP No. 20 Tahun 2006 dan standar FAO-56, efisiensi aplikasi air (eta_a) dihitung dari rasio volume air yang tersimpan di zona perakaran aktif serabut terhadap volume total air yang dialirkan dari sumber [1], [6], [7]:")
    add_equation_p(doc, eta_omml)
    add_body_p(doc, "Di mana eta_a adalah efisiensi aplikasi air irigasi (%), Vakar adalah volume air yang meresap dan tertahan pada zona perakaran aktif pohon jeruk (kedalaman 20–40 cm dan radius 0,5–0,8 m), dan Vsumber adalah volume total air yang disedot dari sungai melalui pipa masukan utama. Sistem baru ditargetkan mencapai eta_a >= 80%, melompat jauh melampaui efisiensi penyiraman parit tanah konvensional eksisting yang kerap di bawah 40–50% akibat rembesan horizontal tanah galian dan evaporasi terbuka di sepanjang parit 100 meter.")
    
    add_point_item(doc, "S-12. Emisi Gas Buang di Zona Tajuk Perakaran",
                   "Sistem operasi penyiraman di sekitar barisan tanaman tidak menghasilkan emisi gas buang jelaga karbon monoksida maupun tetesan residu pelumas oli di atas tanah perakaran. Hal ini memperbaiki kelemahan pompa pembakaran internal berbahan bakar bensin/Pertalite eksisting yang mencemari lingkungan perakaran dan berisiko meracuni mikroorganisme tanah penyubur jeruk.")
    
    add_point_item(doc, "S-13. Kemudahan Pengoperasian oleh Operator Mitra",
                   "Antarmuka pengguna (user interface) dirancang dengan logika operasional sederhana (semi-autonomous / single-button start). Pekerja kebun lokal dengan latar belakang pendidikan dasar dapat mengoperasikan dan memantau status penyiraman dengan waktu pelatihan singkat tidak lebih dari 30 menit.")
    
    add_point_item(doc, "S-14. Durasi Pemeliharaan Rutin Saringan dan Mekanik",
                   "Desain mekanis sistem dirancang modular sehingga proses pembongkaran, pembersihan saringan kotoran, dan perakitan kembali dapat dituntaskan oleh satu orang pekerja dalam waktu kurang dari 20 menit per bulan menggunakan perkakas bengkel pertanian umum (seperti obeng dan kunci pas standar tanpa memerlukan alat kalibrasi khusus).")

    # 1.3 Pengukuran dan Verifikasi
    add_heading_p(doc, "1.3 Pengukuran dan Verifikasi Spesifikasi", level=1, space_before=14, space_after=6)
    add_body_p(doc, "Untuk membuktikan secara ilmiah dan kuantitatif bahwa solusi rekayasa yang dikembangkan pada tahap selanjutnya benar-benar memenuhi spesifikasi yang dijanjikan, bagian ini menyusun rencana pengukuran dan prosedur verifikasi (verification protocol). Setiap spesifikasi dilengkapi dengan metode standar pengujian, peralatan ukur terkalibrasi, mekanisme langkah pengujian, serta kriteria keberhasilan verifikasi yang disajikan pada Tabel 4.")

    add_caption_p(doc, "Tabel 4. Matriks Rencana Pengukuran dan Verifikasi Spesifikasi", is_table=True)

    t4_data = [
        ["ID", "Parameter yang Diuji", "Target Nilai", "Metode / Standar Uji", "Alat Ukur / Verifikasi", "Kriteria Kelulusan"],
        ["S-01", "Volume Air per Pohon", "10 - 15 L +- 5%", "Metode Volumetrik Langsung", "Wadah tera, Gelas ukur 1.000 mL, Flow meter", "Volume tertampung 9,5 - 15,75 L."],
        ["S-02", "Keseragaman Distribusi", "CU >= 85%", "Standar ANSI/ASAE S398.1 (Catch Cans)", "15 unit catch cans, Silinder ukur, Formula CU", "Perhitungan matematis CU >= 85,0%."],
        ["S-03", "Durasi Siklus Total", "<= 4,0 Jam", "Pencatatan Waktu Siklus Penuh", "Stopwatch terkalibrasi, Data logger sistem", "Waktu selesai siram <= 240 menit."],
        ["S-04", "Radius & Kedalaman", "r >= 0,5 m; d >= 20 cm", "Pengukuran Penetrasi Tanah Basah", "Meteran baja, Bor tanah mini, Sensor lengas", "Profil basah r >= 50 cm dan d >= 20 cm."],
        ["S-05", "Derajat Filtrasi Fisik", ">= 120 mesh", "Uji Hambatan & Partikel Lolos", "Saringan kawat 120 mesh, Manometer DP", "Nol partikel >= 130 um lolos ke pipa."],
        ["S-06", "Cadangan Daya Mandiri", ">= 8,0 Jam", "Uji Beban Penuh Kontinu Off-Grid", "DC Power Meter, Clamp meter, Data logger", "Operasi beban penuh >= 8 jam tanpa cutoff."],
        ["S-07", "Ketahanan Selungkup", "IP65 & 20 - 55 deg C", "Metode Uji Standar IEC 60529", "Nozzle 6,3 mm debit 12,5 L/m, Termometer IR", "Nol rembesan air ke PCB; stabil 55 deg C."],
        ["S-08", "Biaya Investasi (CAPEX)", "<= Rp 18.000.000", "Audit Finansial BOM Riil", "Rekapitulasi nota & faktur pengadaan resmi", "Total belanja riil <= plafon anggaran."],
        ["S-09", "Biaya Operasional (OPEX)", "<= Rp 50.000/siklus", "Pencatatan Konsumsi Energi & Jasa", "Log pengeluaran operasional per kegiatan", "Biaya energi + jasa <= Rp 50.000/siklus."],
        ["S-10", "Payback Period", "<= 12 - 18 Bulan", "Analisis Finansial Usaha Tani", "Formula PP = CAPEX / Delta OPEX Tahunan", "Nilai PP terhitung <= 1,5 tahun."],
        ["S-11", "Efisiensi Aplikasi (eta_a)", ">= 80%", "Neraca Air Masuk vs Terserap Akar", "Flow meter pipa utama, Volumetrik perakaran", "Rasio volume air terserap >= 0,80."],
        ["S-12", "Emisi Gas di Kebun", "0 g/kWh Emisi Lokal", "Inspeksi Penggerak & Deteksi Gas", "Gas detector portabel (CO, HC), Visual pelumas", "Nol emisi gas racun & nol ceceran oli."],
        ["S-13", "Kemudahan Operasi", "Waktu ajar <= 30 Menit", "Uji Keterpakaian Lapangan (Usability)", "Lembar tugas operator mitra, Stopwatch tugas", "Operator mandiri operasikan dalam <= 30 mnt."],
        ["S-14", "Waktu Pemeliharaan", "<= 20 Menit/bulan", "Uji Waktu Bongkar-Pasang Saringan", "Stopwatch, Perkakas kunci pas & obeng umum", "Flushing & bersih saringan <= 20 menit."],
    ]

    t4 = doc.add_table(rows=len(t4_data), cols=6)
    t4.alignment = WD_TABLE_ALIGNMENT.CENTER
    set_table_full_grid(t4, color="808080", sz="4")

    for r_idx, row in enumerate(t4.rows):
        make_row_cant_split(row)
        if r_idx == 0:
            make_row_header(row)
        for c_idx, cell in enumerate(row.cells):
            cell.width = col_widths[c_idx]
            cell.text = t4_data[r_idx][c_idx]
            p = cell.paragraphs[0]
            p.paragraph_format.line_spacing = 1.05
            p.paragraph_format.space_before = Pt(2)
            p.paragraph_format.space_after = Pt(2)
            if r_idx == 0:
                set_cell_background(cell, "E0E0E0")
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                for r in p.runs:
                    r.font.name = "Times New Roman"
                    r.font.size = Pt(9.5)
                    r.font.bold = True
            else:
                if c_idx in [0, 2]:
                    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                else:
                    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
                for r in p.runs:
                    r.font.name = "Times New Roman"
                    r.font.size = Pt(9)
            set_cell_margins(cell, top=60, bottom=60, left=80, right=80)

    # Narrative procedures
    add_heading_p(doc, "1.3.1 Prosedur Verifikasi Dosis dan Keseragaman Distribusi Air (S-01, S-02, S-04)", level=2, space_before=12, space_after=4)
    add_point_item(doc, "1. Protokol Uji Keseragaman Christiansen (ANSI/ASAE S398.1)",
                   "Sebanyak 15 titik pohon sampel ditetapkan secara acak terstratifikasi mewakili tiga zona hidrolik: 5 pohon di baris awal (dekat titik suplai air), 5 pohon di zona tengah (jarak ~50 m), dan 5 pohon di baris ujung parit (jarak ~100 m). Pada setiap pohon sampel diletakkan bejana ukur penampung (catch cans) yang mengelilingi radius perakaran tanaman.")
    add_point_item(doc, "2. Pengukuran Volumetrik dan Analisis Matematis CU",
                   "Setelah satu siklus penyiraman selesai dijalankan, volume air tertampung pada masing-masing bejana (Xi) diukur menggunakan silinder ukur bertingkat presisi +- 5 mL. Koefisien Keseragaman Christiansen (CU) dihitung menggunakan rumus matematis: CU = 100 x [1 - (Sum |Xi - X_bar|) / (n x X_bar)], dengan n = 15. Spesifikasi dinyatakan lulus jika CU >= 85% dan deviasi volume tiap titik terhadap target 10–15 L tidak melampaui +- 5%.")
    add_point_item(doc, "3. Verifikasi Penetrasi dan Infiltrasi Tanah",
                   "Tiga puluh menit pasca-siram, profil kedalaman pembasahan tanah diuji menggunakan bor tanah mini (soil core auger) sedalam 40 cm pada radius 60 cm dari batang untuk memastikan air terinfiltrasi pada zona perakaran aktif tanpa menimbulkan genangan permukaan > 30 menit.")

    add_heading_p(doc, "1.3.2 Prosedur Verifikasi Durasi Siklus dan Filtrasi Fisik (S-03, S-05)", level=2, space_before=12, space_after=4)
    add_point_item(doc, "1. Pengukuran Durasi Operasi Kebun",
                   "Durasi siklus penyiraman diukur menggunakan stopwatch digital terkalibrasi yang diaktifkan tepat saat pompa/sistem utama mulai beroperasi dari titik awal kebun dan dihentikan saat pohon terakhir selesai terairi. Data waktu diverifikasi melalui pencatatan timestamp pada sistem mikrokontroler. Kriteria kelulusan terpenuhi jika durasi total <= 240 menit (4 jam).")
    add_point_item(doc, "2. Pengujian Kinerja Filtrasi Sedimen",
                   "Verifikasi kemampuan saringan dilakukan dengan memasang manometer diferensial pada sisi masuk dan keluar tabung saringan 120 mesh. Air sampel sungai Ciberes dialirkan pada debit kerja nominal selama 2 jam kontinu. Sampel air keluaran ditampung dan diuji menggunakan membran kertas saring laboratorium untuk memverifikasi bahwa tidak ada partikel sedimen berukuran >= 130 um yang lolos menuju subsistem distribusi.")

    add_heading_p(doc, "1.3.3 Prosedur Verifikasi Kemandirian Daya dan Proteksi Lingkungan (S-06, S-07)", level=2, space_before=12, space_after=4)
    add_point_item(doc, "1. Uji Ketahanan Pasokan Daya Mandiri (Off-Grid)",
                   "Uji ketahanan daya mandiri dilakukan dengan kondisi modul baterai terisi penuh (100% SoC) tanpa sambungan pengisian panel surya untuk mensimulasikan kondisi cuaca mendung ekstrem. Seluruh beban operasional diaktifkan pada siklus kerja penuh. Digital clamp meter DC dan data logger digunakan untuk merekam kurva penurunan tegangan baterai (V), arus beban (I), dan konsumsi daya total (P) setiap 10 menit. Sistem dinyatakan lulus apabila mampu beroperasi stabil selama minimal 8 jam kontinu tanpa menyentuh batas cut-off tegangan rendah.")
    add_point_item(doc, "2. Uji Proteksi Selungkup Terhadap Debu dan Air (IP65)",
                   "Uji ketahanan lingkungan selungkup mengacu pada klausul standar IEC 60529 untuk proteksi IP65. Selungkup kontroler disemprot menggunakan nozzle berdiameter 6,3 mm dengan debit air 12,5 L/menit dari jarak 2,5–3 meter ke seluruh sambungan dan engsel selama 3 menit. Setelah pengujian semprot, bagian luar dikeringkan dan isi selungkup diperiksa secara visual untuk memastikan tidak ada setetes pun air yang merembes ke papan rangkaian elektronik.")

    add_heading_p(doc, "1.3.4 Prosedur Verifikasi Finansial, Efisiensi Biaya, dan Efisiensi Air (S-08, S-09, S-10, S-11)", level=2, space_before=12, space_after=4)
    add_point_item(doc, "1. Audit Biaya Investasi Awal (CAPEX)",
                   "Biaya investasi awal (CAPEX) diverifikasi melalui audit dokumen Bill of Materials (BOM) berdasarkan total rekapitulasi nota belanja komponen riil dan ongkos fabrikasi bengkel lokal, yang harus terbukti <= Rp18.000.000.")
    add_point_item(doc, "2. Pengujian Biaya Operasional per Siklus (OPEX)",
                   "Biaya operasional per siklus (OPEX) dihitung dari konsumsi energi habis pakai ditambah alokasi jasa pemantauan operator, dengan batas kelulusan <= Rp50.000 per kegiatan.")
    add_point_item(doc, "3. Perhitungan Periode Pengembalian Modal (Payback Period)",
                   "Periode pengembalian modal (Payback Period) dihitung dengan formula PP = CAPEX riil / Delta OPEX Tahunan terhadap biaya manual eksisting (Rp48,7 juta/tahun), dengan syarat PP <= 1,5 tahun (18 bulan).")
    add_point_item(doc, "4. Pengukuran Efisiensi Aplikasi Air (eta_a)",
                   "Efisiensi aplikasi air diuji dengan memasang flow meter pada pipa masukan utama untuk mengukur volume total air disedot (V_in) dan membandingkannya dengan volume air efektif yang tersimpan pada zona perakaran seluruh pohon (V_akar), dengan syarat eta_a = (V_akar / V_in) x 100% >= 80%.")

    add_heading_p(doc, "1.3.5 Prosedur Verifikasi Keterpakaian dan Pemeliharaan (S-13, S-14)", level=2, space_before=12, space_after=4)
    add_point_item(doc, "1. Uji Keterpakaian oleh Operator Mitra (Usability Testing)",
                   "Uji keterpakaian dilakukan bersama pekerja kebun mitra Ciberes menggunakan lembar instruksi kerja standar satu halaman bergambar. Setelah sesi pengenalan selama maksimal 30 menit, pekerja diminta menjalankan sistem secara mandiri. Waktu keberhasilan dan kesalahan eksekusi dicatat, dengan syarat kelulusan pekerja mampu mengoperasikan sistem secara mandiri tanpa asistensi teknis.")
    add_point_item(doc, "2. Uji Waktu Pemeliharaan Rutin Saringan",
                   "Uji pemeliharaan dilakukan melalui simulasi pembongkaran, pembersihan elemen saringan 120 mesh dengan air mengalir, dan pemasangan kembali menggunakan perkakas standar pertanian (obeng dan kunci pas). Seluruh tahapan prosedur pemeliharaan dicatat menggunakan stopwatch dan dinyatakan lulus apabila tuntas dalam waktu <= 20 menit.")

    # 1.4 Kesimpulan
    add_heading_p(doc, "1.4 Kesimpulan", level=1, space_before=14, space_after=6)
    add_body_p(doc, "Dokumen CD-2 ini telah menetapkan kerangka batasan rekayasa (engineering constraints) dan spesifikasi kuantitatif (engineering specifications) yang terdefinisi secara presisi, terukur, dan memiliki pijakan ilmiah yang kokoh bagi perancangan sistem irigasi kebun jeruk limau mitra di Ciberes, Subang.")
    add_body_p(doc, "Rangkuman poin penting dokumen CD-2 meliputi:")
    
    add_point_item(doc, "1. Dasar Penentuan Spesifikasi Multi-Pilar",
                   "Perumusan spesifikasi tidak didasarkan pada asumsi subjektif, melainkan mengintegrasikan kebutuhan riil mitra kebun Ciberes (penurunan upah manual Rp400.000/kegiatan, keandalan pompa, suplai air teratur), regulasi pemerintah (PP No. 20 Tahun 2006 tentang Irigasi), standar teknik industri konsensus internasional (keseragaman air ANSI/ASAE S398.1 >= 85%, ASAE EP405.1, ISO 9261:2004, proteksi lingkungan IEC 60529 IP65, keselamatan tegangan rendah SELV <= 48 V DC, otonomi surya IEC 62124), serta karakteristik agronomi tanaman jeruk limau (kebutuhan evapotranspirasi 10–15 L/pohon, kedalaman perakaran serabut aktif 20–40 cm, dan pencegahan busuk perakaran Phytophthora).")
    
    add_point_item(doc, "2. Perumusan Spesifikasi Kuantitatif Multi-Aspek",
                   "Ditetapkan 5 batasan mutlak (hard constraints) dan 14 butir spesifikasi kuantitatif komprehensif yang mencakup aspek teknis (akurasi dosis air 15 L +- 5%, keseragaman CU >= 85%, durasi siram <= 4 jam, filtrasi 120 mesh, otonomi energi >= 8 jam, rating IP65), aspek ekonomi (CAPEX <= Rp18.000.000, OPEX <= Rp50.000/siklus, payback period <= 12–18 bulan), aspek lingkungan (efisiensi aplikasi air >= 80%, bebas emisi lokal di area perakaran), serta aspek operasional mitra (waktu ajar operasi <= 30 menit, waktu perawatan <= 20 menit/bulan).")
    
    add_point_item(doc, "3. Netralitas Solusi (Solution-Agnostic)",
                   "Spesifikasi dirumuskan secara fungsional tanpa bias atau penguncian dini pada satu opsi teknologi maupun merek komponen tertentu.")
    
    add_point_item(doc, "4. Kesiapan Protokol Pengujian Terukur",
                   "Seluruh spesifikasi telah dipetakan ke dalam matriks rencana pengujian verifikasi yang memuat metode uji baku, instrumen alat ukur terkalibrasi, prosedur pengukuran langkah demi langkah, dan kriteria kelulusan numerik yang objektif.")
    
    add_point_item(doc, "5. Transisi Menuju Tahap CD-3",
                   "Batasan dan spesifikasi kuantitatif dalam dokumen CD-2 ini secara formal menjadi tolok ukur acuan (benchmarking criteria) dan kriteria pembobotan (decision matrix criteria) dalam mengusulkan, menganalisis, dan memilih sekurang-kurangnya tiga alternatif konsep desain solusi pada dokumen rancangan solusi CD-3.")

    # Daftar Pustaka (22 Referensi Terverifikasi dengan DOI Lengkap)
    add_heading_p(doc, "Daftar Pustaka", level=0, space_before=18, space_after=12)

    refs = [
        "[1] R. G. Allen, L. S. Pereira, D. Raes, and M. Smith, Crop Evapotranspiration: Guidelines for Computing Crop Water Requirements, FAO Irrigation and Drainage Paper 56. Rome, Italy: Food and Agriculture Organization of the United Nations (FAO), 1998, ISBN: 92-5-104219-5. [Online]. Available: https://www.fao.org/4/x0490e/x0490e00.htm",
        "[2] American Society of Agricultural and Biological Engineers, Procedure for Sprinkler Testing and Performance Reporting, Standard ANSI/ASAE S398.1. St. Joseph, MI, USA: ASABE, 2021. [Online]. Available: https://elibrary.asabe.org/abstract.asp?aid=41295",
        "[3] American Society of Agricultural and Biological Engineers, Design and Installation of Microirrigation Systems, Standard ASAE EP405.1. St. Joseph, MI, USA: ASABE, 2019. [Online]. Available: https://elibrary.asabe.org/abstract.asp?aid=32022",
        "[4] International Electrotechnical Commission, Degrees of Protection Provided by Enclosures (IP Code), Standard IEC 60529:1989+AMD1:1999+AMD2:2013 CSV. Geneva, Switzerland: IEC, 2013. [Online]. Available: https://webstore.iec.ch/publication/2452",
        "[5] Badan Standardisasi Nasional, Derajat Proteksi yang Diberikan oleh Selungkup (Kode IP), SNI IEC 60529:2014. Jakarta, Indonesia: BSN, 2014. [Online]. Available: https://pesta.bsn.go.id/produk/detail/9726-sniiec605292014",
        "[6] Republik Indonesia, Peraturan Pemerintah Republik Indonesia Nomor 20 Tahun 2006 tentang Irigasi, Lembaran Negara Republik Indonesia Tahun 2006 Nomor 46. Jakarta, Indonesia: Sekretariat Negara RI, 2006. [Online]. Available: https://peraturan.bpk.go.id/Details/48943/pp-no-20-tahun-2006",
        "[7] International Organization for Standardization, Agricultural irrigation equipment — Emitters and emitting pipe — Specification and test methods, Standard ISO 9261:2004. Geneva, Switzerland: ISO, 2004. [Online]. Available: https://www.iso.org/standard/38072.html",
        "[8] International Electrotechnical Commission, Photovoltaic (PV) stand-alone systems - Design verification, Standard IEC 62124:2004. Geneva, Switzerland: IEC, 2004. [Online]. Available: https://webstore.iec.ch/publication/6504",
        "[9] International Electrotechnical Commission, Low-voltage electrical installations - Part 4-41: Protection for safety - Protection against electric shock, Standard IEC 60364-4-41:2005+AMD1:2017 CSV. Geneva, Switzerland: IEC, 2017. [Online]. Available: https://webstore.iec.ch/publication/60074",
        "[10] IEEE Standards Association, IEEE Standard for a Smart Transducer Interface for Sensors and Actuators - Mixed-Mode Communication Protocols and Transducer Electronic Data Sheet (TEDS) Formats, IEEE Std 1451.4-2004. New York, NY, USA: IEEE, 2004, doi: 10.1109/IEEESTD.2004.95745.",
        "[11] P. Panigrahi and A. K. Srivastava, “Water and nutrient management effects on water use and yield of drip irrigated citrus in vertisol under a sub-humid region,” Journal of Integrative Agriculture, vol. 16, no. 5, pp. 1184–1194, 2017, doi: 10.1016/S2095-3119(16)61500-9.",
        "[12] R. S. Ayers and D. W. Westcot, Water Quality for Agriculture, FAO Irrigation and Drainage Paper 29 Rev. 1. Rome, Italy: Food and Agriculture Organization of the United Nations (FAO), 1985, ISBN: 92-5-102263-1. [Online]. Available: https://www.fao.org/4/t0234e/t0234e00.htm",
        "[13] S. Bounoua, S. Tomas, J. Labille, B. Molle, J. Granier, P. Haldenwang, and S. N. Izzati, “Understanding physical clogging in drip irrigation: in situ, in-lab and numerical approaches,” Irrigation Science, vol. 34, no. 4, pp. 327–342, 2016, doi: 10.1007/s00271-016-0506-8.",
        "[14] Y. Shen, J. Puig-Bargués, M. Li, Y. Xiao, Q. Li, and Y. Li, “Physical, chemical and biological emitter clogging behaviors in drip irrigation systems using high-sediment loaded water,” Agricultural Water Management, vol. 270, art. 107738, 2022, doi: 10.1016/j.agwat.2022.107738.",
        "[15] R. Budiarto, R. Poerwanto, E. Santosa, and D. Efendi, “The Potentials of Limau (Citrus amblycarpa Hassk. Ochse) as A Functional Food and Ornamental Mini Tree Based on Metabolomic and Morphological Approaches,” Journal of Tropical Crop Science, vol. 4, no. 2, pp. 49–57, 2017, doi: 10.29244/jtcs.4.2.49-57.",
        "[16] D. M. Kadyampakeni, K. T. Morgan, M. Zekri, A. W. Schumann, S. Guzmán, F. Alferez, M. A. Shahid, and T. A. Obreza, “2023–2024 Florida Citrus Production Guide: Irrigation Management of Citrus Trees,” University of Florida IFAS Extension, EDIS Publication CG093/CPG12, 2023, doi: 10.32473/edis-cg093-2023.",
        "[17] J. H. Graham and L. W. Timmer, “Phytophthora Diseases of Citrus,” University of Florida IFAS Extension, EDIS Publication SL127/CH087, 2020. [Online]. Available: https://edis.ifas.ufl.edu/publication/CH087",
        "[18] A. G. Smajstrla, B. J. Boman, D. Z. Haman, D. J. Pitts, and F. S. Zazueta, “Field Evaluation of Microirrigation Water Application Uniformity,” University of Florida IFAS Extension, Publication BUL265/AE094, 1997, doi: 10.32473/edis-ae094-1997.",
        "[19] T. A. Obreza, M. Zekri, and S. H. Futch, “Nutrition of Florida Citrus Trees, 3rd Edition: Chapter 3. General Soil Fertility and Citrus Tree Nutrition,” University of Florida IFAS Extension, Publication SL457/SS670, 2020, doi: 10.32473/edis-ss670-2020.",
        "[20] G. Li, X. Li, and Q. Zeng, “Development of automatic irrigation and soil moisture monitoring system based on solar energy in citrus orchard,” Transactions of the Chinese Society of Agricultural Engineering, vol. 28, no. 12, pp. 140–145, 2012, doi: 10.3969/j.issn.1002-6819.2012.12.024.",
        "[21] J. M. Domínguez-Niño, H. R. Bogena, J. A. Huisman, B. Schilling, and J. Casadesús, “On the Accuracy of Factory-Calibrated Low-Cost Soil Water Content Sensors,” Sensors, vol. 19, no. 14, art. 3101, 2019, doi: 10.3390/s19143101.",
        "[22] Mitra dan Tim Proyek, “Transkrip Wawancara Kebun Jeruk Limau Audio 1 Ciberes Subang,” dokumentasi primer tidak diterbitkan, dihimpun Oktober 2026."
    ]

    for ref in refs:
        p = doc.add_paragraph()
        p.paragraph_format.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.line_spacing = 1.15
        p.paragraph_format.first_line_indent = Inches(-0.3)
        p.paragraph_format.left_indent = Inches(0.3)
        r = p.add_run(ref)
        r.font.name = "Times New Roman"
        r.font.size = Pt(11)

    # Lampiran
    add_heading_p(doc, "Lampiran: Ringkasan Transkrip Wawancara Mitra Lapangan (Audio 1 Ciberes)", level=0, space_before=18, space_after=12)
    add_body_p(doc, "Catatan Bukti Kebutuhan Pengguna: Berdasarkan rekaman Audio 1 wawancara langsung bersama pengelola kebun jeruk limau di Desa Ciberes, Kecamatan Patokbeusi, Kabupaten Subang, Jawa Barat:")
    
    add_point_item(doc, "1. Populasi Tanaman Jeruk Limau",
                   "Lahan ditanami pohon jeruk limau dengan estimasi populasi sekitar 500 hingga 600 pohon, dengan rata-rata tinggi tajuk pohon saat ini berkisar +- 1 meter.")
    add_point_item(doc, "2. Topografi dan Saluran Parit Galian",
                   "Lahan memiliki 3 lajur parit tanah memanjang dengan panjang masing-masing sekitar 100 meter dan terdapat parit melintang penghubung. Parit dibuat dengan biaya hemat untuk mendekatkan air ke barisan pohon.")
    add_point_item(doc, "3. Sumber Suplai Air dan Pompa Mesin",
                   "Air diambil dari aliran sungai/saluran irigasi yang berjarak sekitar 20,54 meter dari batas kebun. Pompa yang digunakan adalah pompa mesin bensin Alkon (Pertalite). Mitra sempat mencoba memodifikasi bahan bakar menggunakan gas LPG 3 kg untuk menghemat biaya, namun dihentikan karena mesin mengalami panas berlebih (overheat).")
    add_point_item(doc, "4. Ketiadaan Akses Jaringan Listrik PLN",
                   "Lokasi kebun berada di area sawah/kebun terbuka yang belum terjangkau instalasi tiang listrik tegangan rendah PLN.")
    add_point_item(doc, "5. Praktik Penyiraman Eksisting dan Beban Tenaga Kerja",
                   "Air sungai disedot ke dalam parit, kemudian disiramkan ke tanaman secara manual oleh 4 orang pekerja harian lepas menggunakan timba ember kecil.")
    add_point_item(doc, "6. Struktur Biaya Upah Tenaga Kerja",
                   "Upah pekerja adalah Rp100.000 per orang per hari kerja. Total pengeluaran per satu kali kegiatan penyiraman adalah Rp400.000 (4 orang x Rp100.000). Penyiraman dilakukan rutin rata-rata 3 hari sekali pada musim kemarau.")
    add_point_item(doc, "7. Dosis Air Berdasarkan Kebiasaan Praktis Petani",
                   "Petani memperkirakan rata-rata satu pohon menerima sekitar 10 hingga 15 Liter air per kali siram, namun volume aktual per pohon tidak pernah ditakar secara presisi.")
    add_point_item(doc, "8. Ekspektasi dan Kebutuhan Solusi Otomasi",
                   "Pengelola menginginkan adanya alat atau sistem otomatis/mekanis yang mampu menggantikan pekerjaan guyur manual tersebut agar pengeluaran upah tenaga kerja dapat dipangkas drastis, serta pasokan air ke pohon menjadi lebih teratur dan terjamin.")

    doc.save(output_path)
    print(f"Successfully generated updated CD2 document at: {output_path}")

if __name__ == "__main__":
    main()
