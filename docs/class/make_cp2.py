import re
import sys

from docx import Document
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Pt, RGBColor, Inches

OUT = sys.argv[1]
INK = RGBColor(0x1F, 0x2A, 0x36)
ACCENT = RGBColor(0x2B, 0x55, 0xC9)
MUTED = RGBColor(0x5A, 0x67, 0x75)

doc = Document()
sec = doc.sections[0]
sec.page_width, sec.page_height = Inches(8.5), Inches(11)
for side in ("left_margin", "right_margin", "top_margin", "bottom_margin"):
    setattr(sec, side, Inches(0.75))

normal = doc.styles["Normal"]
normal.font.name = "Calibri"
normal.font.size = Pt(10.5)
normal.font.color.rgb = INK
normal.element.rPr.rFonts.set(qn("w:eastAsia"), "Calibri")
normal.paragraph_format.space_after = Pt(5)
for name, size, color in (("Title", 18, INK), ("Heading 2", 12, ACCENT)):
    st = doc.styles[name]
    st.font.name, st.font.size, st.font.bold, st.font.color.rgb = "Calibri", Pt(size), True, color
    st.element.rPr.rFonts.set(qn("w:asciiTheme"), "") if False else None
doc.styles["Heading 2"].paragraph_format.space_before = Pt(10)
doc.styles["Heading 2"].paragraph_format.space_after = Pt(4)
doc.styles["Title"].paragraph_format.space_after = Pt(2)


def add_runs(par, text, size=None, color=None, italic=False):
    for part in [x for x in re.split(r"(\*\*[^*]+\*\*)", text) if x]:
        bold = part.startswith("**")
        r = par.add_run(part[2:-2] if bold else part)
        r.bold = bold or None
        r.italic = italic or None
        if size:
            r.font.size = Pt(size)
        if color:
            r.font.color.rgb = color
    return par


def p(text, **kw):
    return add_runs(doc.add_paragraph(), text, **kw)


def h(text):
    doc.add_heading(text, level=2)


def bullet(text):
    par = doc.add_paragraph(style="List Bullet")
    par.paragraph_format.space_after = Pt(3)
    add_runs(par, text)


def shade(cell, fill):
    tcPr = cell._tc.get_or_add_tcPr()
    shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear")
    shd.set(qn("w:color"), "auto")
    shd.set(qn("w:fill"), fill)
    tcPr.append(shd)


def table(widths, rows):
    t = doc.add_table(rows=len(rows), cols=len(widths))
    t.style = "Table Grid"
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    for j, w in enumerate(widths):
        t.columns[j].width = Inches(w)
    for i, row in enumerate(rows):
        for j, text in enumerate(row):
            c = t.cell(i, j)
            c.width = Inches(widths[j])
            par = c.paragraphs[0]
            par.paragraph_format.space_after = Pt(0)
            add_runs(par, f"**{text}**" if i == 0 else text, size=9)
            if i == 0:
                shade(c, "E3E9F4")
    return t


def link_par(par, label, url):
    """Add a clickable hyperlink run."""
    part = par.part
    r_id = part.relate_to(url, "http://schemas.openxmlformats.org/officeDocument/2006/relationships/hyperlink",
                          is_external=True)
    hl = OxmlElement("w:hyperlink")
    hl.set(qn("r:id"), r_id)
    run = OxmlElement("w:r")
    rpr = OxmlElement("w:rPr")
    col = OxmlElement("w:color"); col.set(qn("w:val"), "2B55C9"); rpr.append(col)
    u = OxmlElement("w:u"); u.set(qn("w:val"), "single"); rpr.append(u)
    sz = OxmlElement("w:sz"); sz.set(qn("w:val"), "18"); rpr.append(sz)
    run.append(rpr)
    t = OxmlElement("w:t"); t.text = label; run.append(t)
    hl.append(run)
    par._p.append(hl)


MD = sys.argv[2]
lines = open(MD, encoding="utf-8").read().splitlines()
in_table = False
rows = []
title_done = False
for line in lines:
    if line.startswith("# ") and not title_done:
        doc.add_heading(line[2:], level=0); title_done = True; continue
    if line.startswith("## "):
        h(line[3:]); continue
    if line.strip() == "---":
        continue
    if line.startswith("|"):
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if set("".join(cells)) <= set("-: "):
            continue
        rows.append(cells); in_table = True; continue
    if in_table:
        # emit evidence table with clickable links in last column
        t = table([0.7, 1.1, 2.9, 2.3], [r[:3] + [""] for r in rows])
        for i, r in enumerate(rows[1:], start=1):
            par = t.cell(i, 3).paragraphs[0]
            links = re.findall(r"\[([^\]]+)\]\(([^)]+)\)", r[3])
            for k, (lab, url) in enumerate(links):
                if k:
                    par.add_run(", ").font.size = Pt(9)
                link_par(par, lab, url)
        hdr = t.cell(0, 3).paragraphs[0]
        add_runs(hdr, f"**{rows[0][3]}**", size=9)
        rows = []; in_table = False
        doc.add_paragraph()
    s = line.rstrip()
    if not s:
        continue
    s = s.replace("`", "")
    if s.startswith("- "):
        bullet(s[2:].replace("*", "") if s.count("*") % 2 else s[2:]); continue
    # convert *italic* labels to bold for print clarity
    s = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"**\1**", s)
    first = doc.paragraphs[-1] if doc.paragraphs else None
    p(s, color=MUTED if s.startswith("**Ian Downham**") or s.startswith("**Submitted") else None)

doc.core_properties.author = "Ian Downham"
doc.core_properties.title = "Early Prototype Update (Checkpoint 2)"
doc.save(OUT)
