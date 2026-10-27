# -*- coding: utf-8 -*-
"""
Build complete CD2_Jeruk_Limau.docx harmonizing teammate additions, CD-1 details, 
verified DOI-backed literature, and native Word OMML equation blocks.
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
    <m:r><m:t> = </m:t></m:r>
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
    t2.rows[1].cells[0].text = "00,\n28 Oktober 2026"
    t2.rows[1].cells[1].text = "Draf Final CD-2"
    t2.rows[1].cells[2].text = "Penyelarasan komprehensif dasar penentuan spesifikasi berbasis multi-pilar (wawancara mitra mendalam Audio 1 & Audio 2 Ciberes, regulasi PP No. 20/2006 & Permentan 49/2014, standar ASABE/IEC/ISO/SNI, literatur fisiologi jeruk & sedimen FAO-56/FAO-29), penyempurnaan matriks batasan rekayasa dan spesifikasi kuantitatif terukur (S-01 s.d. S-14), perumusan protokol verifikasi pengujian, perapian rumus matematis berbasis standar Equation Word OMML, serta pemutakhiran daftar pustaka tervalidasi DOI."
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
    
    add_body_p(doc, "Dokumen CD-2 ini merupakan kelanjutan langsung dan berkesinambungan dari dokumen CD-1 (Analisis Permasalahan Penyiraman Manual pada Kebun Jeruk Limau di Ciberes Subang) yang telah disahkan oleh dosen pembimbing. Jika CD-1 berfokus pada identifikasi akar permasalahan operasional, pemetaan tapak lahan eksisting, kendala ketiadaan listrik jala-jala, inefisiensi tenaga kerja manual, serta analisis kelemahan solusi terdahulu, maka dokumen CD-2 ini secara formal menetapkan landasan batas operasional mutlak (engineering constraints) dan spesifikasi kuantitatif terukur (engineering specifications) yang wajib dipenuhi oleh solusi rekayasa pada tahap perancangan CD-3.")
    
    add_body_p(doc, "Perumusan batasan dan spesifikasi ini dirancang secara terukur (measurable), realistis terhadap kondisi fisik tapak (feasible), memiliki landasan ilmiah dan regulasi yang kokoh (rigorously grounded), serta berprinsip netral terhadap pilihan solusi tertentu (solution-agnostic). Pendekatan ini memastikan bahwa ruang eksplorasi desain pada tahap CD-3 tetap terbuka luas untuk membandingkan sekurang-kurangnya tiga konsep alternatif solusi—seperti jaringan mikroirigasi perpipaan terotomasi, wahana mekanis gerak (robotik) semi-otonom berselang, maupun arsitektur hibrida—tanpa penguncian dini (lock-in) pada satu opsi perangkat keras tertentu.")

    # 1.1 Dasar Penentuan Spesifikasi
    add_heading_p(doc, "1.1 Dasar Penentuan Spesifikasi", level=1, space_before=14, space_after=6)
    add_body_p(doc, "Penetapan batasan rekayasa dan spesifikasi kuantitatif dalam dokumen ini tidak didasarkan pada perkiraan subjektif, melainkan merupakan hasil sintesis multi-pilar yang mengintegrasikan empat fondasi rujukan: (1) kebutuhan riil pengguna dan data faktual lapangan hasil wawancara mitra, (2) kerangka regulasi pemerintah dan standar teknis konsensus industri, (3) literatur ilmiah fisiologi tanaman jeruk limau dan pemodelan neraca air, serta (4) karakteristik tapak lahan eksisting dan keterbatasan sumber daya lingkungan.")

    # 1.1.1 Kebutuhan Pengguna
    add_heading_p(doc, "1.1.1 Kebutuhan Pengguna dan Hasil Wawancara Lapangan (Mitra Ciberes)", level=2, space_before=10, space_after=4)
    add_body_p(doc, "Kebutuhan pengguna diperoleh secara primer melalui observasi lapangan mendalam dan rekaman wawancara langsung bersama mitra pengelola kebun jeruk limau di Desa Ciberes, Kecamatan Patokbeusi, Kabupaten Subang, Jawa Barat (terdokumentasi dalam Transkrip Wawancara Audio 1 dan Audio 2, terlampir). Dari penuturan mitra dan verifikasi tim, teridentifikasi fakta-fakta kunci dan kebutuhan esensial sebagai berikut:")
    
    add_point_item(doc, "1. Beban Biaya Tenaga Kerja Manual dan Struktur Pengeluaran Mitra",
                   "Populasi tanaman kebun berjumlah sekitar 500 hingga 600 pohon jeruk limau yang tertata pada lahan memanjang seluas ~3.000 m² (panjang lintasan ~100 m hingga 117,52 m). Untuk menyiram seluruh pohon tersebut, pengelola kebun mempekerjakan 4 orang buruh harian lepas dengan upah masing-masing Rp100.000 per kegiatan (total pengeluaran Rp400.000 per satu kali siram). Pada musim kemarau dan fase pembungaan/pembuahan, penyiraman wajib dilakukan rutin rata-rata 3 hari sekali (~10 hingga 12 kali per bulan). Skenario perhitungan tahunan menunjukkan estimasi akumulasi upah tenaga kerja mencapai Rp48.700.000 per tahun. Mengingat total biaya modal pembukaan lahan mitra telah menyentuh sekitar Rp90.000.000, beban upah manual ini sangat memberatkan arus kas usaha tani. Pengelola secara tegas menginginkan adanya mekanisasi atau otomasi yang mampu menggantikan pekerjaan fisik menimba dan mengguyur air agar biaya tenaga kerja dapat dipangkas secara drastis [31].")
    
    add_point_item(doc, "2. Ketidakpastian Dosis Air dan Keterbatasan Tenaga Fisik",
                   "Pekerjaan penyiraman eksisting dilakukan dengan menyedot air sungai ke dalam parit, kemudian 4 pekerja berjalan menyusuri barisan parit untuk menimba air menggunakan wadah ember kecil (kapasitas sekitar 5 Liter) dan mengguyurkannya manual ke pangkal tanaman sebanyak 2 hingga 3 kali guyuran. Estimasi empiris petani adalah sekitar 10 hingga 15 Liter per pohon, namun volume riil per pohon tidak pernah diukur secara presisi. Ketidakseragaman takaran sangat rentan terjadi akibat kelelahan fisik pekerja di tengah terik matahari Subang, di mana pohon-pohon di barisan awal parit kerap menerima air berlebih, sementara pohon di baris tengah hingga ujung parit rawan kekurangan pasokan air.")
    
    add_point_item(doc, "3. Kendala Operasional Pompa Bensin Eksisting dan Kegagalan Modifikasi LPG",
                   "Suplai air kebun mengandalkan pompa mesin pembakaran internal bensin (merk Alkon diameter pipa 2 inci, berbahan bakar Pertalite) untuk menyedot air dari sungai/saluran irigasi yang berjarak 20,54 meter dari tepi kebun menuju parit tanah. Mitra sempat melakukan modifikasi mekanis dengan mengganti bahan bakar bensin menggunakan tabung gas LPG 3 kg untuk menekan biaya operasional. Namun, eksperimen tersebut terpaksa dihentikan permanen karena blok mesin pompa mengalami kenaikan suhu ekstrem (overheating), tarikan mesin tidak stabil, serta menimbulkan kekhawatiran bahaya kebakaran di area basah. Oleh karena itu, mitra membutuhkan sistem penggerak atau pompa baru yang andal, aman, bersuara tenang, dan tidak menimbulkan komplikasi perawatan mekanik.")
    
    add_point_item(doc, "4. Kebutuhan Proteksi Hara Pemupukan Jeruk",
                   "Pohon jeruk limau di kebun Ciberes dipupuk secara periodik sebanyak dua kali dalam setahun menggunakan kombinasi pupuk NPK dan pupuk organik/kandang yang dibenamkan melingkar di sekeliling tajuk perakaran. Mitra menyampaikan bahwa metode guyuran manual ember bervolume besar kerap menimbulkan aliran limpasan permukaan (surface runoff) yang mengikis tanah gembur dan menghanyutkan butiran pupuk ke dasar parit galian sebelum sempat diserap oleh akar serabut. Hal ini menegaskan perlunya sistem penyiraman yang mampu mendistribusikan air secara perlahan dan terarah ke zona perakaran tanpa memicu erosi hara.")
    
    add_point_item(doc, "5. Ekspektasi Kinerja Solusi Rekayasa Baru",
                   "Mitra mengharapkan sistem irigasi baru memiliki target keandalan yang konkret: (a) mampu menjamin kepastian pasokan air 10–15 Liter per pohon secara merata, (b) memiliki biaya operasional per siklus yang sangat rendah sehingga modal investasi dapat terbayar (payback period) dalam 1–2 musim panen, (c) mudah dioperasikan oleh pekerja lokal (single-touch / sakelar sederhana tanpa prosedur perangkat lunak rumit), serta (d) komponen sistem tahan terhadap paparan cuaca luar ruangan dan lumpur tanah sawah [31].")

    # 1.1.2 Regulasi dan Standar
    add_heading_p(doc, "1.1.2 Regulasi Pemerintah dan Standar Teknis Industri", level=2, space_before=12, space_after=4)
    add_body_p(doc, "Sistem rekayasa pertanian modern wajib mematuhi kerangka hukum tata kelola air nasional serta standar teknik konsensus industri internasional:")
    
    add_point_item(doc, "1. Standar Evaluasi dan Desain Keseragaman Irigasi Mikro (ANSI/ASAE S398.1 & ASAE EP405.1)",
                   "American Society of Agricultural and Biological Engineers (ASABE) menetapkan standar baku pengukuran kinerja hidraulik sistem irigasi mikro melalui ANSI/ASAE S398.1 (Procedure for Sprinkler Testing and Performance Reporting) dan ASAE EP405.1 (Design and Installation of Microirrigation Systems). Untuk budidaya tanaman hortikultura bernilai tinggi, standar menetapkan bahwa Koefisien Keseragaman Christiansen (CU) minimum adalah >= 80%, dengan target rancangan rekayasa ideal mencapai CU >= 85%. Nilai keseragaman ini menjamin distribusi kelembapan tanah yang homogen di seluruh blok lahan tanpa disparitas hidraulik antara titik terdekat dan terjauh dari sumber suplai [2], [3], [23].")
    
    add_point_item(doc, "2. Regulasi Pemerintah tentang Pengelolaan Air Irigasi (PP No. 20 Tahun 2006 & Permentan No. 49/2014)",
                   "Peraturan Pemerintah Republik Indonesia Nomor 20 Tahun 2006 tentang Irigasi juncto Peraturan Menteri Pertanian No. 49/Permentan/OT.140/4/2014 menegaskan amanat konservasi sumber daya air pertanian: pengelolaan air di tingkat usaha tani wajib mengutamakan efisiensi pemanfaatan air secara tertib dan berkesinambungan (target efisiensi aplikasi air eta_a >= 75–80%), mencegah pemborosan air akibat perkolasi dalam dan kebocoran saluran tanah bebas, serta mendorong penerapan teknologi irigasi hemat air berdaya guna tinggi [6], [7].")
    
    add_point_item(doc, "3. Standar Komponen dan Emiter Irigasi Mikro (ISO 9261:2004)",
                   "Standar internasional ISO 9261:2004 (Agricultural irrigation equipment — Emitters and emitting pipe — Specification and test methods) mengatur toleransi mekanis, ketahanan hidraulis terhadap tekanan kerja, serta batas variasi laju alir (coefficient of manufacturing variation, Cv <= 0,05). Standar ini menjadi acuan mutlak agar emiter tetes, lubang mikro, atau nozzle tidak mengalami deformasi fisik dan lonjakan debit saat dioperasikan di bawah tekanan fluida pertanian [8].")
    
    add_point_item(doc, "4. Standar Proteksi Selungkup Lingkungan Luar Ruangan (IEC 60529 / SNI IEC 60529:2014)",
                   "Peralatan instrumentasi, kontroler elektronika mikrokontroler, akuisisi data, dan sistem konversi daya yang diletakkan di tapak kebun terbuka tanpa naungan permanen wajib memenuhi derajat perlindungan selungkup minimal IP65 berdasarkan standar IEC 60529 dan adopsi identik SNI IEC 60529:2014. Rating ini memastikan selungkup kedap partikel debu tanah secara total (dust-tight) serta tahan terhadap semprotan air bertekanan rendah dari berbagai sudut tanpa kebocoran ke papan sirkuit cetak (PCB) [4], [5].")
    
    add_point_item(doc, "5. Standar Keselamatan Kelistrikan Area Pertanian Basah (IEC 60364-4-41 & IEEE 1451)",
                   "Lingkungan pertanian terbuka dengan saluran air parit basah memiliki konduktivitas tinggi yang meningkatkan risiko bahaya sengatan listrik. Standar IEC 60364-4-41 klausul 414 menetapkan batas tegangan ekstra rendah aman (Safety Extra-Low Voltage / SELV) maksimal 48 V DC untuk seluruh aktuator, pompa elektrik mikro, dan instrumentasi lapangan. Sementara itu, standar IEEE Std 1451.4-2004 digunakan sebagai acuan arsitektur instrumentasi sensor terkalibrasi berdaya rendah [10], [11].")
    
    add_point_item(doc, "6. Standar Pembangkit Listrik Surya Fotovoltaik Mandiri (IEC 62124 & FAO Guidelines)",
                   "Standar Photovoltaic Stand-Alone Systems: Design Verification (IEC 62124:2004) dan panduan teknis FAO mengenai Solar-Powered Irrigation Systems (Hartung & Pluschke, 2018) mensyaratkan bahwa sistem PLTS off-grid pertanian wajib memperhitungkan faktor cadangan otonomi energi (days of autonomy) minimal 1,5 hingga 2 hari operasi kontinu tanpa sinar matahari langsung guna mengantisipasi cuaca mendung atau anomali musim hujan di wilayah tropis [9], [26], [27].")

    # 1.1.3 Karakteristik Fisiologi Tanaman
    add_heading_p(doc, "1.1.3 Karakteristik Fisiologi Tanaman Jeruk Limau dan Literatur Agronomi", level=2, space_before=12, space_after=4)
    add_body_p(doc, "Karakteristik biologis tanaman jeruk limau (Citrus amblycarpa Hassk. Ochse) menjadi fondasi penentuan dosis volume, frekuensi, dan zona pembasahan:")
    
    add_point_item(doc, "1. Morfologi Perakaran Dangkal Jeruk Limau",
                   "Berdasarkan kajian morfologi dan metabolomik jeruk limau oleh Budiarto dkk. (2017) serta pedoman nutrisi pohon jeruk University of Florida IFAS Extension (Obreza dkk., 2020), sistem perakaran tanaman jeruk didominasi oleh akar serabut aktif (feeder roots) yang terkonsentrasi pada lapisan tanah dangkal dengan kedalaman efektif 20–40 cm dan radius sebaran horizontal 0,5–0,8 m di bawah proyeksi kanopi tajuk pohon. Pemberian air di luar radius proyeksi tajuk tidak dapat diserap optimal oleh akar dan hanya memicu pertumbuhan gulma liar yang menyerap unsur hara tanah [20], [24].")
    
    add_point_item(doc, "2. Pemodelan Neraca Air Evapotranspirasi FAO-56 Penman-Monteith",
                   "Estimasi kebutuhan air tanaman jeruk limau dihitung mengacu pada metodologi standar FAO Irrigation and Drainage Paper 56 (Allen dkk., 1998), panduan irigasi jeruk Florida (Kadyampakeni dkk., 2023), serta korelasi sistem penjadwalan irigasi Pereira (1996). Kebutuhan evapotranspirasi aktual tanaman dihitung melalui Persamaan 1:")
    add_equation_p(doc, etc_omml)
    add_body_p(doc, "Di mana ETc adalah laju evapotranspirasi aktual tanaman (mm/hari), Kc adalah koefisien tanaman jeruk kanopi sedang pada fase pertumbuhan aktif (Kc = 0,70–0,80), dan ET0 adalah laju evapotranspirasi acuan lingkungan Subang pada musim kemarau berkisar 4,5–5,0 mm/hari. Kebutuhan air per pohon dalam satu siklus penyiraman dihitung melalui persamaan neraca air (Persamaan 2):")
    add_equation_p(doc, vpohon_omml)
    add_body_p(doc, "Di mana Atajuk adalah luas proyeksi kanopi tajuk basah perakaran (~1,0 m² untuk pohon setinggi ~1 meter) dan Isiram adalah interval frekuensi penyiraman (2–3 hari per siklus). Substitusi nilai parameter lapangan menghasilkan kebutuhan air teoritis berkisar 9,8 hingga 15,2 Liter per pohon per siklus penyiraman. Perhitungan ilmiah ini secara eksak memvalidasi batas empiris petani mitra di kebun Ciberes (10–15 Liter per pohon) [1], [19], [21].")
    
    add_point_item(doc, "3. Pencegahan Risiko Pembusukan Akar (Phytophthora nicotianae)",
                   "Literatur patologi tanaman oleh Graham & Timmer (2020) dan pedoman keseragaman Smajstrla dkk. (1997) mengingatkan bahwa kejenuhan air tanah yang berkepanjangan (waterlogging > 24–48 jam) akibat penggenangan parit tanah galian merupakan pemicu utama serangan jamur tanah Phytophthora nicotianae dan Phytophthora palmivora yang mengakibatkan pembusukan akar serabut serta penyakit blendok/kanker batang (foot rot). Oleh karena itu, spesifikasi pemberian air harus menjamin aerasi tanah tetap terjaga dan tidak menimbulkan genangan air terpusat lebih dari 30 menit pasca-siram [22], [23].")

    # 1.1.4 Karakteristik Tapak Lahan
    add_heading_p(doc, "1.1.4 Karakteristik Tapak Lahan Eksisting dan Keterbatasan Sumber Daya", level=2, space_before=12, space_after=4)
    add_body_p(doc, "Spesifikasi sistem rekayasa diselaraskan secara ketat dengan kendala fisik tapak kebun di Ciberes:")
    
    add_point_item(doc, "1. Ketiadaan Akses Jaringan Listrik PLN (Off-Grid Murni)",
                   "Kebun jeruk limau mitra terletak di bentang hamparan lahan persawahan pedesaan yang belum terjangkau tiang jaringan tegangan rendah PLN. Segala bentuk rancangan solusi rekayasa wajib bersifat mandiri energi (self-powered standalone), mengandalkan pembangkit listrik tenaga surya (PLTS fotovoltaik) yang dipadukan dengan baterai penyimpan daya berdensitas tinggi atau penggerak mekanis hemat energi [9], [26], [28].")
    
    add_point_item(doc, "2. Kekeruhan Air Sungai dan Sedimentasi Partikulat",
                   "Sumber air diambil dari aliran sungai/saluran irigasi primer berjarak 20,54 meter dari batas kebun. Air permukaan alami membawa beban padatan tersuspensi (suspended solids) tinggi berupa pasir halus, lumpur liat sedimen, dan serpihan ganggang organik, terutama saat debit sungai menurun di musim kemarau. Mengacu pada studi kualitas air FAO-29 (Ayers & Westcot, 1985), pedoman penyaringan Virginia Tech (Shortridge & Benham, 2023), serta penelitian penyumbatan emiter oleh Bounoua dkk. (2016), Shen dkk. (2022), dan Lavanholi dkk. (2018), sistem wajib dilengkapi penyaring fisik berkerapatan minimal 120 mesh (mampu menahan partikel >= 130 um) guna menjamin lubang emiter atau pipa penyalur tidak tersumbat secara mekanis [13], [14], [15], [16], [17].")
    
    add_point_item(doc, "3. Geometri Jaringan Parit dan Inefisiensi Saluran Tanah Konvensional",
                   "Kebun memiliki 3 lajur parit tanah longitudinal memanjang ~100 meter dengan parit melintang penghubung pada bentang lahan selebar 25–30 meter. Analisis irigasi permukaan Walker (1989) menunjukkan bahwa saluran tanah terbuka mengalami kehilangan air hingga 40–50% akibat rembesan lateral dan evaporasi bebas. Parit galian yang semula dibuat untuk memudahkan penimbaan air kini terbukti tidak efisien. Di sisi lain, riset terkini mengenai robotika dan otomasi penyiraman hortikultura (Elkaoud dkk., 2025; Li dkk., 2012) membuktikan bahwa lintasan kebun memanjang sangat berpotensi dilayani oleh jaringan perpipaan mikro maupun wahana penyiram bergerak otonom [18], [25], [28].")

    # 1.2 Batasan dan Spesifikasi Solusi
    add_heading_p(doc, "1.2 Batasan dan Spesifikasi Solusi", level=1, space_before=14, space_after=6)
    add_body_p(doc, "Berdasarkan sintesis seluruh dasar pertimbangan multi-pilar di atas, bagian ini menetapkan batasan rekayasa (engineering constraints) dan matriks spesifikasi kuantitatif (engineering specifications) yang memandu perancangan sistem irigasi kebun jeruk limau.")

    # 1.2.1 Batasan Rekayasa
    add_heading_p(doc, "1.2.1 Batasan Rekayasa Solusi (Engineering Constraints)", level=2, space_before=10, space_after=4)
    add_body_p(doc, "Batasan rekayasa merupakan kondisi batas mutlak (hard constraints) yang tidak dapat dilanggar oleh arsitektur solusi mana pun yang akan dirancang:")
    
    add_point_item(doc, "C-01. Kemandirian Energi (Off-Grid Standalone)",
                   "Sistem harus beroperasi 100% mandiri tanpa ketergantungan pada jaringan jala-jala listrik PLN, memanfaatkan pasokan energi terbarukan lokal (seperti fotovoltaik surya) yang terintegrasi dengan modul penyimpan daya baterai.")
    
    add_point_item(doc, "C-02. Kompatibilitas Sumber Air Permukaan Berpartikulat",
                   "Sistem harus mampu menyedot dan memproses air baku dari sungai/saluran irigasi terbuka berkekeruhan alami tanpa mengalami kegagalan pompa dan penyumbatan mekanis pada komponen distribusi fluida.")
    
    add_point_item(doc, "C-03. Kompatibilitas Geometri dan Topografi Kebun",
                   "Sistem harus mampu melayani area kebun dengan populasi 500–600 pohon pada rentang lintasan memanjang 100–117,52 meter tanpa merusak batang tanaman, tajuk buah, maupun jaringan perakaran dangkal.")
    
    add_point_item(doc, "C-04. Keselamatan Kelistrikan Area Terbuka Basah (SELV)",
                   "Seluruh perangkat elektrikal, instrumentasi sensor, pengontrol, dan kabel transmisi yang dipasang di lingkungan kebun terbuka wajib beroperasi pada batas tegangan ekstra rendah aman (Safety Extra-Low Voltage / SELV <= 48 V DC) sesuai standar IEC 60364-4-41.")
    
    add_point_item(doc, "C-05. Netralitas Solusi (Solution-Agnostic)",
                   "Perumusan batasan dan spesifikasi dirancang secara fungsional tanpa mengunci rancangan pada satu opsi arsitektur atau merek komponen tertentu, memberikan fleksibilitas penuh untuk mengevaluasi alternatif jaringan perpipaan mikro, wahana bergerak mandiri, maupun sistem modular pada tahap CD-3.")

    # 1.2.2 Spesifikasi Kuantitatif Solusi
    add_heading_p(doc, "1.2.2 Spesifikasi Kuantitatif Solusi (Engineering Specifications)", level=2, space_before=12, space_after=4)
    add_body_p(doc, "Spesifikasi kuantitatif dirumuskan ke dalam empat kategori aspek menyeluruh: teknis, ekonomi, lingkungan, dan operasional/kemitraan. Matriks lengkap spesifikasi kuantitatif disajikan pada Tabel 3, yang diikuti oleh deskripsi penjelasan teknis pada masing-masing parameternya.")

    add_caption_p(doc, "Tabel 3. Matriks Batasan dan Spesifikasi Kuantitatif Solusi", is_table=True)

    # Table 3
    t3_data = [
        ["ID", "Parameter Spesifikasi", "Nilai Target & Toleransi", "Satuan", "Kategori Aspek", "Rujukan Penentuan"],
        ["S-01", "Akurasi Dosis Volume Air per Pohon", "10 - 15 +- 5%", "Liter/pohon", "Aspek Teknis", "Wawancara Mitra [31], FAO-56 [1], Florida [21], Pereira [19]"],
        ["S-02", "Koefisien Keseragaman Distribusi (CU)", ">= 85", "%", "Aspek Teknis", "Standar ANSI/ASAE S398.1, EP405.1 [2], [3], Smajstrla [23]"],
        ["S-03", "Durasi Total Siklus Penyiraman Kebun", "<= 4,0", "Jam/siklus", "Aspek Teknis", "Batas Waktu Operasi Harian Mitra, Elkaoud [25]"],
        ["S-04", "Radius dan Kedalaman Pembasahan", "r = 0,5 - 0,8; d = 20 - 40", "cm", "Aspek Teknis", "Morfologi Perakaran Jeruk Limau Budiarto [20], Obreza [24]"],
        ["S-05", "Derajat Filtrasi Fisik Partikulat", ">= 120 (saring <= 130)", "mesh (um)", "Aspek Teknis", "Kualitas Air FAO-29 [13], Shortridge [14], Bounoua [15], Lavanholi [17]"],
        ["S-06", "Ketahanan Cadangan Energi (Autonomy)", ">= 8,0 (min. 2 siklus penuh)", "Jam operasi", "Aspek Teknis", "Standar IEC 62124 [9], Hartung & Pluschke [27], Nurwidiana [26]"],
        ["S-07", "Ketahanan Lingkungan Selungkup (IP)", "IP65 (Suhu: 20 - 55)", "Rating (deg C)", "Aspek Teknis", "Standar IEC 60529 / SNI IEC 60529 [4], [5]"],
        ["S-08", "Batas Biaya Investasi Awal (CAPEX)", "<= 18.000.000", "Rupiah (Rp)", "Aspek Ekonomi", "Analisis Kelayakan Modal Usaha Tani & BOM Riil"],
        ["S-09", "Biaya Operasional Siklus (OPEX)", "<= 50.000 (Hemat >= 87,5%)", "Rupiah (Rp)", "Aspek Ekonomi", "Biaya Upah Manual Eksisting (Rp400.000/siklus), Mitra [31]"],
        ["S-10", "Periode Pengembalian Modal (Payback)", "<= 12 - 18", "Bulan", "Aspek Ekonomi", "Skenario Penghematan Rp48,7 Juta/Tahun, Durga [30]"],
        ["S-11", "Efisiensi Aplikasi Air Irigasi (eta_a)", ">= 80", "%", "Aspek Lingkungan", "PP No. 20/2006 [6], Permentan 49/2014 [7], ISO 9261 [8], Walker [18]"],
        ["S-12", "Emisi Gas Buang di Zona Tajuk", "0 (Bebas emisi hidrokarbon)", "g/kWh", "Aspek Lingkungan", "Proteksi Tanah Perakaran dari Residu Pertalite & Overheat Pompa"],
        ["S-13", "Kemudahan Pengoperasian Mitra", "Single-touch (Ajar <= 30)", "Menit", "Aspek Operasional", "Profil Tenaga Kerja Lokal Kebun Ciberes, Usability Testing"],
        ["S-14", "Durasi Pemeliharaan Rutin Saringan", "<= 20 (Perkakas lokal)", "Menit/bulan", "Aspek Operasional", "Keterbatasan Bengkel Khusus Pedesaan, Prosedur Shortridge [14]"],
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
                   "Mengacu pada standar ANSI/ASAE S398.1 dan ASAE EP405.1, keseragaman volume air yang diterima oleh pohon di awal, tengah, dan ujung barisan parit harus mencapai minimal 85%. Evaluasi keseragaman distribusi air dihitung menggunakan formula Koefisien Keseragaman Christiansen (Christiansen's Uniformity Coefficient, CU) (Persamaan 3) [2], [3]:")
    add_equation_p(doc, cu_omml)
    add_body_p(doc, "Di mana CU adalah Christiansen's Uniformity Coefficient (%), n adalah jumlah pohon sampel uji (n = 15 bejana), Xi adalah volume air tertampung pada bejana sampel ke-i (Liter), dan X_bar adalah rata-rata volume air dari seluruh bejana sampel. Nilai keseragaman CU >= 85% menjamin pertumbuhan seluruh pohon jeruk limau tetap homogen tanpa adanya pohon yang mengalami kekeringan ekstrem atau pembusukan akar.")
    
    add_point_item(doc, "S-03. Durasi Total Siklus Penyiraman Kebun",
                   "Seluruh proses penyiraman untuk 500–600 pohon harus dapat dituntaskan dalam waktu kurang dari atau sama dengan 4 jam per siklus kegiatan. Hal ini memberikan efisiensi waktu yang masif dibandingkan metode manual 4 orang buruh yang menyita waktu seharian penuh, serta memanfaatkan waktu siram ideal (pagi hari sebelum pukul 10.00 WIB atau sore hari setelah pukul 15.00 WIB) guna meminimalkan kehilangan air akibat evaporasi radiasi matahari langsung [25].")
    
    add_point_item(doc, "S-04. Radius dan Kedalaman Pembasahan Efektif",
                   "Air irigasi diarahkan meresap pada area proyeksi kanopi tanaman dengan radius 0,5–0,8 m dari pangkal batang hingga mencapai kedalaman profil tanah 20–40 cm. Distribusi air yang terkonsentrasi pada zona perakaran aktif serabut menghindarkan pembasahan batang utama yang rentan jamur batang serta tidak membasahi area jalan antar-baris secara sia-sia [20], [24].")
    
    add_point_item(doc, "S-05. Derajat Filtrasi Fisik Partikulat",
                   "Untuk mengatasi kekeruhan air sungai Ciberes, sistem wajib dilengkapi dengan saringan partikulat dengan kerapatan minimal 120 mesh (mampu menyaring partikel berdiameter >= 130 um). Hal ini merupakan syarat wajib untuk mencegah terjadinya penyumbatan mekanis pada emiter, lubang nozzle, katup pengontrol, dan impeller pompa air mikro [13], [14], [15], [17].")
    
    add_point_item(doc, "S-06. Ketahanan Cadangan Energi Mandiri (Autonomy)",
                   "Subsistem daya mandiri (off-grid) harus mampu menyuplai kebutuhan daya operasional beban penuh selama minimal 8 jam kerja kontinu tanpa kehadiran cahaya matahari langsung (setara dengan cadangan daya untuk minimal 2 siklus penyiraman lengkap). Mengacu pada standar IEC 62124 (Photovoltaic stand-alone systems) dan pedoman PLTS FAO (Hartung & Pluschke, 2018), konsumsi energi operasional per siklus penyiraman (Esiklus) dan kapasitas minimum modul penyimpan daya (Cbaterai) dihitung melalui Persamaan 4 dan Persamaan 5 [9], [27]:")
    add_equation_p(doc, esiklus_omml)
    add_equation_p(doc, cbaterai_omml)
    add_body_p(doc, "Di mana Esiklus adalah energi operasional satu siklus (Wh), Pbeban adalah total daya pompa dan kontroler (Watt), toperasi adalah durasi kerja satu siklus (<= 4 jam), Nautonomy adalah faktor otonomi cadangan (>= 2 siklus = 8 jam), Vsistem adalah tegangan kerja ekstra rendah aman (12 V DC atau 24 V DC), dan DoD adalah Depth of Discharge aman baterai (DoD = 80% untuk LiFePO4). Hal ini menjamin keandalan operasi pompa tetap prima saat cuaca berawan berturut-turut.")
    
    add_point_item(doc, "S-07. Ketahanan Lingkungan Selungkup (Ingress Protection)",
                   "Seluruh kotak kontrol (controller enclosure), konektor kelistrikan, papan modul sensor, dan unit catu daya wajib bersertifikasi minimal IP65 serta mampu bekerja normal pada rentang suhu ambien 20 deg C hingga 55 deg C. Selungkup harus tahan terhadap terpaan panas matahari tropis Subang, percikan lumpur tanah, dan semprotan air saat pembersihan kebun [4], [5].")
    
    add_point_item(doc, "S-08. Batas Biaya Investasi Awal Sistem (CAPEX)",
                   "Total biaya rancang bangun, belanja komponen, fabrikasi struktural, instalasi sistem, dan instrumentasi dibatasi maksimal Rp18.000.000. Angka batas atas ini ditetapkan secara rasional agar investasi terjangkau oleh petani skala menengah dan tidak melebihi alokasi dana kelayakan modal usaha tani.")
    
    add_point_item(doc, "S-09. Biaya Operasional per Siklus Penyiraman (OPEX)",
                   "Biaya operasional yang mencakup konsumsi energi (pengisian daya/bahan bakar cadangan) dan alokasi jasa pemantauan operator ditekan hingga maksimal Rp50.000 per siklus penyiraman. Hal ini menghasilkan penghematan biaya langsung sebesar 87,5% per kegiatan dibandingkan pengeluaran rutin upah guyur manual eksisting (Rp400.000 per kegiatan) [31].")
    
    add_point_item(doc, "S-10. Periode Pengembalian Modal (Payback Period)",
                   "Kelayakan ekonomi sistem rekayasa dinilai berdasarkan kecepatan pengembalian modal investasi awal (Payback Period, PP). Periode pengembalian modal dihitung dengan formula rasio investasi awal (CAPEX) terhadap selisih penghematan biaya operasional tahunan (Persamaan 6):")
    add_equation_p(doc, pp_omml)
    add_body_p(doc, "Di mana PP adalah Payback Period (dalam tahun atau bulan), CAPEX adalah modal investasi awal sistem rekayasa (<= Rp18.000.000), dan Delta OPEX_tahunan adalah selisih penghematan biaya operasional tahunan antara metode manual eksisting (Rp400.000/kegiatan x ~120 siklus/tahun = ~Rp48.000.000/tahun) dengan biaya operasional sistem baru (<= Rp50.000/siklus x ~120 siklus/tahun = <= Rp6.000.000/tahun). Dengan selisih penghematan bersih mencapai lebih dari Rp42.000.000 per tahun, target titik impas modal dipastikan tercapai dalam kurun waktu 12 hingga 18 bulan operasi [30].")
    
    add_point_item(doc, "S-11. Efisiensi Aplikasi Air Irigasi (eta_a)",
                   "Mengacu pada prinsip konservasi air PP No. 20 Tahun 2006, Permentan No. 49/2014, dan panduan FAO, efisiensi aplikasi air (eta_a) dihitung dari rasio volume air yang tersimpan di zona perakaran aktif serabut terhadap volume total air yang dialirkan dari sumber melalui Persamaan 7 [1], [6], [7], [18]:")
    add_equation_p(doc, eta_omml)
    add_body_p(doc, "Di mana eta_a adalah efisiensi aplikasi air irigasi (%), Vakar adalah volume air yang meresap dan tertahan pada zona perakaran aktif pohon jeruk (kedalaman 20–40 cm dan radius 0,5–0,8 m), dan Vsumber adalah volume total air yang disedot dari sungai melalui pipa masukan utama. Sistem baru ditargetkan mencapai eta_a >= 80%, melompat jauh melampaui efisiensi penyiraman parit tanah konvensional eksisting yang kerap di bawah 40–50% akibat rembesan horizontal tanah galian dan evaporasi terbuka di sepanjang parit 100 meter.")
    
    add_point_item(doc, "S-12. Emisi Gas Buang di Zona Tajuk Perakaran",
                   "Sistem operasi penyiraman di sekitar barisan tanaman tidak menghasilkan emisi gas buang jelaga karbon monoksida maupun tetesan residu pelumas oli di atas tanah perakaran. Hal ini memperbaiki kelemahan pompa pembakaran internal berbahan bakar bensin/Pertalite eksisting yang mencemari lingkungan perakaran dan berisiko meracuni mikroorganisme tanah penyubur jeruk.")
    
    add_point_item(doc, "S-13. Kemudahan Pengoperasian oleh Operator Mitra",
                   "Antarmuka pengguna (user interface) dirancang dengan logika operasional sederhana (semi-autonomous / single-button start). Pekerja kebun lokal dengan latar belakang pendidikan dasar dapat mengoperasikan dan memantau status penyiraman dengan waktu pelatihan singkat tidak lebih dari 30 menit.")
    
    add_point_item(doc, "S-14. Durasi Pemeliharaan Rutin Saringan dan Mekanik",
                   "Desain mekanis sistem dirancang modular sehingga proses pembongkaran, pembersihan saringan kotoran, dan perakitan kembali dapat dituntaskan oleh satu orang pekerja dalam waktu kurang dari 20 menit per bulan menggunakan perkakas bengkel pertanian umum (seperti obeng dan kunci pas standar tanpa memerlukan alat kalibrasi khusus) [14].")

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
                   "Setelah satu siklus penyiraman selesai dijalankan, volume air tertampung pada masing-masing bejana (Xi) diukur menggunakan silinder ukur bertingkat presisi +- 5 mL. Koefisien Keseragaman Christiansen (CU) dihitung menggunakan rumus matematis Persamaan 3 dengan n = 15. Spesifikasi dinyatakan lulus jika CU >= 85% dan deviasi volume tiap titik terhadap target 10–15 L tidak melampaui +- 5%.")
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
                   "Efisiensi aplikasi air diuji dengan memasang flow meter pada pipa masukan utama untuk mengukur volume total air disedot (V_sumber) dan membandingkannya dengan volume air efektif yang tersimpan pada zona perakaran seluruh pohon (V_akar), dengan syarat eta_a = (V_akar / V_sumber) x 100% >= 80%.")

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
                   "Perumusan spesifikasi mengintegrasikan kebutuhan riil mitra kebun Ciberes (penurunan upah manual Rp400.000/kegiatan atau Rp48,7 juta/tahun, keandalan pompa, proteksi pemupukan NPK), regulasi pemerintah (PP No. 20 Tahun 2006 tentang Irigasi dan Permentan No. 49/2014), standar teknik industri konsensus internasional (keseragaman air ANSI/ASAE S398.1 >= 85%, ASAE EP405.1, ISO 9261:2004, proteksi lingkungan IEC 60529 IP65, keselamatan tegangan rendah SELV <= 48 V DC, otonomi surya IEC 62124), karakteristik agronomi fisiologi tanaman jeruk limau (evapotranspirasi 10–15 L/pohon, perakaran serabut aktif 20–40 cm, pencegahan busuk perakaran Phytophthora), serta mitigasi sedimen sungai Ciberes (filtrasi >= 120 mesh).")
    
    add_point_item(doc, "2. Perumusan Spesifikasi Kuantitatif Multi-Aspek",
                   "Ditetapkan 5 batasan mutlak (hard constraints) dan 14 butir spesifikasi kuantitatif komprehensif yang mencakup aspek teknis (akurasi dosis air 15 L +- 5%, keseragaman CU >= 85%, durasi siram <= 4 jam, filtrasi 120 mesh, otonomi energi >= 8 jam, rating IP65), aspek ekonomi (CAPEX <= Rp18.000.000, OPEX <= Rp50.000/siklus, payback period <= 12–18 bulan), aspek lingkungan (efisiensi aplikasi air >= 80%, bebas emisi lokal di area perakaran), serta aspek operasional mitra (waktu ajar operasi <= 30 menit, waktu perawatan <= 20 menit/bulan).")
    
    add_point_item(doc, "3. Netralitas Solusi (Solution-Agnostic)",
                   "Spesifikasi dirumuskan secara fungsional tanpa bias atau penguncian dini pada satu opsi teknologi maupun merek komponen tertentu, membuka ruang terbuka bagi evaluasi perpipaan mikro, robotik bergerak berselang, maupun solusi hibrida.")
    
    add_point_item(doc, "4. Kesiapan Protokol Pengujian Terukur",
                   "Seluruh spesifikasi telah dipetakan ke dalam matriks rencana pengujian verifikasi yang memuat metode uji baku, instrumen alat ukur terkalibrasi, prosedur pengukuran langkah demi langkah, dan kriteria kelulusan numerik yang objektif.")
    
    add_point_item(doc, "5. Transisi Menuju Tahap CD-3",
                   "Batasan dan spesifikasi kuantitatif dalam dokumen CD-2 ini secara formal menjadi tolok ukur acuan (benchmarking criteria) dan kriteria pembobotan (decision matrix criteria) dalam mengusulkan, menganalisis, dan memilih sekurang-kurangnya tiga alternatif konsep desain solusi pada dokumen rancangan solusi CD-3.")

    # Daftar Pustaka (31 Referensi Lengkap, Tervalidasi DOI dan Sumber Resmi)
    add_heading_p(doc, "Daftar Pustaka", level=0, space_before=18, space_after=12)

    refs = [
        "[1] R. G. Allen, L. S. Pereira, D. Raes, and M. Smith, Crop Evapotranspiration: Guidelines for Computing Crop Water Requirements, FAO Irrigation and Drainage Paper 56. Rome, Italy: Food and Agriculture Organization of the United Nations (FAO), 1998, ISBN: 92-5-104219-5. [Online]. Available: https://www.fao.org/4/x0490e/x0490e00.htm",
        "[2] American Society of Agricultural and Biological Engineers, Procedure for Sprinkler Testing and Performance Reporting, Standard ANSI/ASAE S398.1. St. Joseph, MI, USA: ASABE, 2021. [Online]. Available: https://elibrary.asabe.org/abstract.asp?aid=41295",
        "[3] American Society of Agricultural and Biological Engineers, Design and Installation of Microirrigation Systems, Standard ASAE EP405.1. St. Joseph, MI, USA: ASABE, 2019. [Online]. Available: https://elibrary.asabe.org/abstract.asp?aid=32022",
        "[4] International Electrotechnical Commission, Degrees of Protection Provided by Enclosures (IP Code), Standard IEC 60529:1989+AMD1:1999+AMD2:2013 CSV. Geneva, Switzerland: IEC, 2013. [Online]. Available: https://webstore.iec.ch/publication/2452",
        "[5] Badan Standardisasi Nasional, Derajat Proteksi yang Diberikan oleh Selungkup (Kode IP), SNI IEC 60529:2014. Jakarta, Indonesia: BSN, 2014. [Online]. Available: https://pesta.bsn.go.id/produk/detail/9726-sniiec605292014",
        "[6] Republik Indonesia, Peraturan Pemerintah Republik Indonesia Nomor 20 Tahun 2006 tentang Irigasi, Lembaran Negara Republik Indonesia Tahun 2006 Nomor 46. Jakarta, Indonesia: Sekretariat Negara RI, 2006. [Online]. Available: https://peraturan.bpk.go.id/Details/48943/pp-no-20-tahun-2006",
        "[7] Kementerian Pertanian Republik Indonesia, Pedoman Teknis Pengembangan Tata Air Pertanian, Peraturan Menteri Pertanian No. 49/Permentan/OT.140/4/2014 juncto SNI 7608:2010 (Jaringan Irigasi Air Tanah Dangkal). Jakarta, Indonesia: Kementan RI, 2014.",
        "[8] International Organization for Standardization, Agricultural irrigation equipment — Emitters and emitting pipe — Specification and test methods, Standard ISO 9261:2004. Geneva, Switzerland: ISO, 2004. [Online]. Available: https://www.iso.org/standard/38072.html",
        "[9] International Electrotechnical Commission, Photovoltaic (PV) stand-alone systems - Design verification, Standard IEC 62124:2004. Geneva, Switzerland: IEC, 2004. [Online]. Available: https://webstore.iec.ch/publication/6504",
        "[10] International Electrotechnical Commission, Low-voltage electrical installations - Part 4-41: Protection for safety - Protection against electric shock, Standard IEC 60364-4-41:2005+AMD1:2017 CSV. Geneva, Switzerland: IEC, 2017. [Online]. Available: https://webstore.iec.ch/publication/60074",
        "[11] IEEE Standards Association, IEEE Standard for a Smart Transducer Interface for Sensors and Actuators - Mixed-Mode Communication Protocols and Transducer Electronic Data Sheet (TEDS) Formats, IEEE Std 1451.4-2004. New York, NY, USA: IEEE, 2004, doi: 10.1109/IEEESTD.2004.95745.",
        "[12] P. Panigrahi and A. K. Srivastava, “Water and nutrient management effects on water use and yield of drip irrigated citrus in vertisol under a sub-humid region,” Journal of Integrative Agriculture, vol. 16, no. 5, pp. 1184–1194, 2017, doi: 10.1016/S2095-3119(16)61500-9.",
        "[13] R. S. Ayers and D. W. Westcot, Water Quality for Agriculture, FAO Irrigation and Drainage Paper 29 Rev. 1. Rome, Italy: Food and Agriculture Organization of the United Nations (FAO), 1985, ISBN: 92-5-102263-1. [Online]. Available: https://www.fao.org/4/t0234e/t0234e00.htm",
        "[14] J. Shortridge and B. Benham, “Filtration, Treatment, and Maintenance Considerations for Micro-Irrigation Systems,” Virginia Cooperative Extension, Virginia Tech, Publication 442-757, 2023. [Online]. Available: https://www.pubs.ext.vt.edu/442/442-757/442-757.html",
        "[15] S. Bounoua, S. Tomas, J. Labille, B. Molle, J. Granier, P. Haldenwang, and S. N. Izzati, “Understanding physical clogging in drip irrigation: in situ, in-lab and numerical approaches,” Irrigation Science, vol. 34, no. 4, pp. 327–342, 2016, doi: 10.1007/s00271-016-0506-8.",
        "[16] Y. Shen, J. Puig-Bargués, M. Li, Y. Xiao, Q. Li, and Y. Li, “Physical, chemical and biological emitter clogging behaviors in drip irrigation systems using high-sediment loaded water,” Agricultural Water Management, vol. 270, art. 107738, 2022, doi: 10.1016/j.agwat.2022.107738.",
        "[17] R. Lavanholi, B. Molle, R. J. R. Ramos, and A. P. Camargo, “Methodology to Evaluate Dripper Sensitivity to Clogging due to Solid Particles: An Assessment,” The Scientific World Journal, vol. 2018, art. 7697458, pp. 1–9, 2018, doi: 10.1155/2018/7697458.",
        "[18] W. R. Walker, Guidelines for Designing and Evaluating Surface Irrigation Systems, FAO Irrigation and Drainage Paper 45. Rome, Italy: Food and Agriculture Organization of the United Nations (FAO), 1989, ISBN: 92-5-102879-6. [Online]. Available: https://www.fao.org/4/t0231e/t0231e00.htm",
        "[19] L. S. Pereira, “Inter-relationships between irrigation scheduling methods and on-farm irrigation systems,” in Irrigation Scheduling: From Theory to Practice, FAO Water Reports 8. Rome, Italy: FAO, 1996, pp. 91–104. [Online]. Available: https://www.fao.org/4/w4367e/w4367e0c.htm",
        "[20] R. Budiarto, R. Poerwanto, E. Santosa, and D. Efendi, “The Potentials of Limau (Citrus amblycarpa Hassk. Ochse) as A Functional Food and Ornamental Mini Tree Based on Metabolomic and Morphological Approaches,” Journal of Tropical Crop Science, vol. 4, no. 2, pp. 49–57, 2017, doi: 10.29244/jtcs.4.2.49-57.",
        "[21] D. M. Kadyampakeni, K. T. Morgan, M. Zekri, A. W. Schumann, S. Guzmán, F. Alferez, M. A. Shahid, and T. A. Obreza, “2023–2024 Florida Citrus Production Guide: Irrigation Management of Citrus Trees,” University of Florida IFAS Extension, EDIS Publication CG093/CPG12, 2023, doi: 10.32473/edis-cg093-2023.",
        "[22] J. H. Graham and L. W. Timmer, “Phytophthora Diseases of Citrus,” University of Florida IFAS Extension, EDIS Publication SL127/CH087, 2020. [Online]. Available: https://edis.ifas.ufl.edu/publication/CH087",
        "[23] A. G. Smajstrla, B. J. Boman, D. Z. Haman, D. J. Pitts, and F. S. Zazueta, “Field Evaluation of Microirrigation Water Application Uniformity,” University of Florida IFAS Extension, Publication BUL265/AE094, 1997, doi: 10.32473/edis-ae094-1997.",
        "[24] T. A. Obreza, M. Zekri, and S. H. Futch, “Nutrition of Florida Citrus Trees, 3rd Edition: Chapter 3. General Soil Fertility and Citrus Tree Nutrition,” University of Florida IFAS Extension, Publication SL457/SS670, 2020, doi: 10.32473/edis-ss670-2020.",
        "[25] N. Elkaoud, S. Ismail, R. Mahmoud, H. Taraby, S. Shang, D. Wang, and M. Rayan, “Efficient and Effective Irrigation Water Management Using Sprinkler Robot,” Eng, vol. 6, no. 7, art. 138, pp. 1–18, Jun. 2025, doi: 10.3390/eng6070138.",
        "[26] Nurwidiana, W. Fatmawati, dan A. Rifa'i, “Perancangan Alat Penyiram Lahan Bawang Merah Berbasis Teknologi Solar Fotovoltaik,” Jurnal PASTI (Penelitian dan Aplikasi Sistem dan Teknik Industri), vol. 15, no. 1, hlm. 61–70, 2021.",
        "[27] H. Hartung and L. Pluschke, The Benefits and Risks of Solar-Powered Irrigation: A Global Overview. Rome, Italy: Food and Agriculture Organization of the United Nations (FAO), 2018, ISBN: 978-92-5-130479-2. [Online]. Available: https://www.fao.org/4/i9047en/I9047EN.pdf",
        "[28] G. Li, X. Li, and Q. Zeng, “Development of automatic irrigation and soil moisture monitoring system based on solar energy in citrus orchard,” Transactions of the Chinese Society of Agricultural Engineering, vol. 28, no. 12, pp. 140–145, 2012, doi: 10.3969/j.issn.1002-6819.2012.12.024.",
        "[29] J. M. Domínguez-Niño, H. R. Bogena, J. A. Huisman, B. Schilling, and J. Casadesús, “On the Accuracy of Factory-Calibrated Low-Cost Soil Water Content Sensors,” Sensors, vol. 19, no. 14, art. 3101, 2019, doi: 10.3390/s19143101.",
        "[30] N. Durga, S. L. Postigo, and M. Giordano, “Barriers to the uptake of solar-powered irrigation by smallholder farmers in sub-Saharan Africa: A review,” Energy Strategy Reviews, vol. 51, art. 101294, 2024, doi: 10.1016/j.esr.2024.101294.",
        "[31] Mitra dan Tim Proyek, “Transkrip Wawancara Kebun Jeruk Limau Audio 1 dan Audio 2 Ciberes Subang,” dokumentasi primer tidak diterbitkan, dihimpun Oktober 2026."
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
    add_heading_p(doc, "Lampiran: Ringkasan Transkrip Wawancara Mitra Lapangan (Audio 1 dan Audio 2 Ciberes)", level=0, space_before=18, space_after=12)
    add_body_p(doc, "Catatan Bukti Kebutuhan Pengguna: Berdasarkan rekaman Audio 1 dan Audio 2 wawancara langsung bersama pengelola kebun jeruk limau di Desa Ciberes, Kecamatan Patokbeusi, Kabupaten Subang, Jawa Barat:")
    
    add_point_item(doc, "1. Populasi dan Karakteristik Tanaman Jeruk Limau",
                   "Lahan ditanami pohon jeruk limau (Citrus amblycarpa) dengan estimasi populasi sekitar 500 hingga 600 pohon. Rata-rata tinggi tajuk pohon saat ini berkisar +- 1 meter (tanaman muda/fase pertumbuhan produktif awal). Pohon dipupuk secara periodik dua kali dalam setahun menggunakan pupuk NPK dan pupuk kandang organik.")
    add_point_item(doc, "2. Geometri Lahan dan Saluran Parit Galian",
                   "Lahan memanjang dengan bentang lintasan ~100 m hingga 117,52 m dan lebar ~25–30 m. Memiliki 3 lajur parit tanah memanjang (lebar 0,5–0,6 m, kedalaman 0,4–0,5 m) dengan parit melintang penghubung. Parit dibuat dengan biaya galian hemat untuk mendekatkan air ke barisan pohon, namun air parit cepat surut dan habis setelah pompa dimatikan akibat rembesan lateral tanah bebas.")
    add_point_item(doc, "3. Sumber Suplai Air dan Riwayat Pompa Mesin",
                   "Air disedot dari aliran sungai/saluran irigasi primer yang berjarak sekitar 20,54 meter dari batas lahan kebun. Pompa yang digunakan adalah pompa mesin bensin Alkon 2 inci (berbahan bakar Pertalite). Mitra sempat mencoba memodifikasi sistem bahan bakar memakai tabung gas LPG 3 kg demi menekan biaya, namun dihentikan permanen karena blok mesin mengalami kenaikan suhu ekstrem (overheating).")
    add_point_item(doc, "4. Ketiadaan Akses Jaringan Listrik PLN",
                   "Lokasi kebun berada di hamparan lahan persawahan terbuka pedesaan yang belum terjangkau instalasi tiang dan jaringan distribusi listrik tegangan rendah PLN (kondisi off-grid murni).")
    add_point_item(doc, "5. Praktik Penyiraman Eksisting dan Beban Tenaga Kerja",
                   "Air sungai dipompa masuk ke parit galian, kemudian disiramkan ke tanaman secara manual oleh 4 orang pekerja harian lepas menggunakan timba ember kecil bervolume ~5 Liter (masing-masing pohon diguyur 2–3 ember). Proses penyiraman menyita waktu 4 hingga 6 jam per siklus kegiatan.")
    add_point_item(doc, "6. Struktur Biaya Upah Tenaga Kerja Manual",
                   "Upah pekerja adalah Rp100.000 per orang per hari kerja. Total pengeluaran per satu kali kegiatan penyiraman adalah Rp400.000 (4 orang x Rp100.000). Penyiraman dilakukan rutin rata-rata 3 hari sekali pada musim kemarau (~10–12 kali/bulan). Estimasi akumulasi upah mencapai Rp48.700.000 per tahun, memberatkan total modal pembukaan lahan mitra (~Rp90 juta).")
    add_point_item(doc, "7. Dosis Air Berdasarkan Kebiasaan Praktis Petani",
                   "Petani memperkirakan rata-rata satu pohon menerima sekitar 10 hingga 15 Liter air per kali siram, namun volume aktual per pohon tidak pernah ditakar secara presisi sehingga terjadi variasi kelembapan tanah yang mencolok antar-zona.")
    add_point_item(doc, "8. Ekspektasi dan Kebutuhan Solusi Otomasi",
                   "Pengelola menginginkan adanya alat atau sistem otomatis/mekanis yang mampu menggantikan pekerjaan guyur manual tersebut agar pengeluaran upah tenaga kerja dapat dipangkas drastis (target biaya operasional <= Rp50.000/siklus), pasokan air ke pohon menjadi teratur dan terjamin, modal lekas kembali dalam 1–2 tahun, serta sistem mudah dioperasikan oleh pekerja lokal tanpa kerumitan teknis.")

    doc.save(output_path)
    print(f"Successfully generated updated CD2 document at: {output_path}")

if __name__ == "__main__":
    main()
