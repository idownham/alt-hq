"""Build a plain paragraph-style Word doc from a simple .md: '# Title', one subtitle line, paragraphs with inline [links](url)."""
import re
import sys

from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt, Inches, RGBColor

OUT, SRC = sys.argv[1], sys.argv[2]
doc = Document()
sec = doc.sections[0]
sec.page_width, sec.page_height = Inches(8.5), Inches(11)
for side in ("left_margin", "right_margin", "top_margin", "bottom_margin"):
    setattr(sec, side, Inches(1))
st = doc.styles["Normal"]
st.font.name, st.font.size = "Calibri", Pt(11)
st.element.rPr.rFonts.set(qn("w:eastAsia"), "Calibri")
st.paragraph_format.space_after = Pt(8)
st.paragraph_format.line_spacing = 1.08


def link(par, label, url):
    r_id = par.part.relate_to(url, "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink",
                              is_external=True)
    hl = OxmlElement("w:hyperlink"); hl.set(qn("r:id"), r_id)
    run = OxmlElement("w:r"); rpr = OxmlElement("w:rPr")
    c = OxmlElement("w:color"); c.set(qn("w:val"), "1F4E9C"); rpr.append(c)
    u = OxmlElement("w:u"); u.set(qn("w:val"), "single"); rpr.append(u)
    run.append(rpr); t = OxmlElement("w:t"); t.text = label
    t.set(qn("xml:space"), "preserve"); run.append(t); hl.append(run); par._p.append(hl)


lines = [l for l in open(SRC, encoding="utf-8").read().split("\n\n") if l.strip()]
title = lines[0].lstrip("# ").strip()
tp = doc.add_paragraph(); r = tp.add_run(title); r.bold = True; r.font.size = Pt(14)
tp.paragraph_format.space_after = Pt(2)
sp = doc.add_paragraph(); r = sp.add_run(lines[1].strip()); r.font.color.rgb = RGBColor(0x55, 0x55, 0x55)
for block in lines[2:]:
    par = doc.add_paragraph()
    pos = 0
    for m in re.finditer(r"\[([^\]]+)\]\(([^)]+)\)", block):
        par.add_run(block[pos:m.start()])
        link(par, m.group(1), m.group(2))
        pos = m.end()
    par.add_run(block[pos:].strip("\n"))
doc.core_properties.author = "Ian Downham"
doc.core_properties.title = title
doc.save(OUT)
