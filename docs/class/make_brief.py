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
    for i, row in enumerate(rows):
        for j, text in enumerate(row):
            c = t.cell(i, j)
            c.width = Inches(widths[j])
            par = c.paragraphs[0]
            par.paragraph_format.space_after = Pt(0)
            add_runs(par, f"**{text}**" if i == 0 else text, size=9.5)
            if i == 0:
                shade(c, "E3E9F4")
    return t


doc.add_heading("Is There Free Money in Prediction Markets?", level=0)
p("Concept and Evidence Plan · Checkpoint 1 · Ian Downham · Solo · Founder Documentary, Fall 2026", color=MUTED)
p("Written Oct 14, revised Oct 18 (after the Oct 11 due date). Nothing is backdated.",
  color=MUTED, italic=True)

h("1. The problem")
p("On prediction markets like Kalshi and Polymarket US, anyone can buy \"yes\" or \"no\" on real events, and a "
  "\"yes\" pays $1 if it happens. Prices sometimes differ between sites, bounce at kickoff or look like "
  "gut feel. **Can a part-time student using AI find a real edge after fees, or have "
  "faster bots already taken it?** That matters to anyone tempted to try."
  "")

h("2. What I'm building")
p("**Read-only data systems** that test each idea against pass/fail rules I write down **before seeing any "
  "results**. Public data only; no money at risk without a dated decision first.")
table([1.1, 2.4, 3.5], [
    ["Project", "The idea", "How I'll know (set before any data)"],
    ["**Osprey**", "Buy both sides of a game on two sites for under $1 total (arbitrage). A cloud server checks "
     "~327 games.",
     "After 14+ days, 3+ leagues: **GO** at 5+ real gaps a week (pre-game, 2+ checks, $20+ after fees). **STOP** "
     "under 1 a week."],
    ["**Coin Toss**", "Be a shopkeeper at kickoff: post buy and sell prices and earn the gap.",
     "20+ clean games. Continue if the typical game has 3+ swings bigger than trading costs; then a "
     "simulation must profit in 60%+ of games."],
    ["**Slot Machine**", "15-minute \"Bitcoin up or down\" markets.",
     "Round 1: four strategies, tested once. **None passed.** Round 2: the shopkeeper approach, 900+ windows, "
     "profitable with 95% confidence."],
    ["**Bloodhound**", "\"Will Trump say ___?\" Can homework (transcripts, fine print) beat gut feel?",
     "Beat the market's price 15 min before each speech on accuracy (Brier score), 300+ markets, "
     "95% confidence."],
])
p("**Success** is a clear, evidence-backed verdict for each one. \"No edge\" counts.")

h("3. Scope")
bullet("**Smallest version:** Osprey's scanner plus its rules report.")
bullet("**Unknowns:** how often gaps happen, whether matched markets share rules, transcript coverage.")
bullet("**Safety:** read-only, no keys on screen or in prompts, site limits respected, legality varies by state.")
bullet("**Resources and roles:** laptop, one ~$12/month cloud server, Python, Claude Code. Solo: I set rules, "
       "check results and film; AI writes most code under my review.")
bullet("**Timeline:** Coin Toss games Oct 17–22 · Osprey verdict ~Oct 27 · Slot Machine data Oct 28 · "
       "Bloodhound test by Nov 8 · story Nov 22.")

h("4. Test and evidence plan")
p("I'll measure price gaps, order books, trades and accuracy on past speeches. "
  "**Progress** is clean data piling up. I **change direction** on a STOP verdict, bad data "
  "or a rule mismatch. A script applies the rules.")
p("This already happened twice. Mention markets close the second the word is said, so I moved Bloodhound's "
  "benchmark to the pre-speech price before seeing results (Oct 14). My laptop slept and Slot Machine lost most "
  "of a night, so I'm moving the recorders to one cloud server (Oct 15).")

h("5. Documentary plan")
bullet("**Questions:** Do speed edges vanish after fees? Can homework beat speed? When an idea fails, stop or pivot?")
bullet("**Real moments:** the scanner running, my $5 manual trade (Oct 13), the failed backtest (Oct 14), "
       "live game recordings, the Osprey verdict.")
bullet("**Evidence:** dated commits, decision logs and weekly screen recordings, indexed in my journal.")

h("6. AI plan")
bullet("**Claude Code** for research, code, tests and docs. I check its work and set every rule. It "
       "flagged a goal \"jump\" counted as noise, so I excluded jumps (Oct 13).")
bullet("**AI image and video tools** for clearly labeled explainer visuals, never in place of real evidence.")

h("7. Recording my work")
p("Each journal entry logs my decision, the AI's output and whether I accepted, revised or rejected it. "
  "Journal attached as a PDF.")

h("Initial source list")
table([2.5, 1.2, 3.3], [
    ["Source", "Organization", "How it informs the project"],
    ["Kalshi API documentation (docs.kalshi.com)", "Kalshi", "Public market data, order books, rate limits"],
    ["Kalshi fee schedule (checked Oct 13 and 14)", "Kalshi", "Taker and maker fees used in every profit calculation"],
    ["Polymarket US documentation (docs.polymarket.us)", "Polymarket US",
     "Public market data. Live price feeds need API keys, so my scanner checks prices on a timer instead"],
    ["Polymarket US fees (effective Oct 7)", "Polymarket US", "Taker fee and maker rebate used in the arbitrage math"],
    ["Roll Call Factbase (rollcall.com/factbase)", "Roll Call",
     "Trump speech transcripts and schedules for Bloodhound (read slowly, research only)"],
])

doc.core_properties.author = "Ian Downham"
doc.core_properties.title = "Is There Free Money in Prediction Markets? Concept and Evidence Plan"
doc.save(OUT)
