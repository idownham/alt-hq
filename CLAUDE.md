# alt — HQ (shared rules for all projects)

This file sits in the parent folder `~/code/alt/`, so Claude Code loads it for **every** session in any project
below it, in addition to that project's own `CLAUDE.md`. Project files win on project-specific details; the rules
here apply everywhere.

## Owner and context
- Owner: Ian Downham (GitHub: idownham). Senior, Supply Chain Management, University of Arkansas.
- These projects are part of a **graded class project** (founder documentary, Fall 2026). Accuracy, honest results
  and a dated evidence trail matter as much as the outcome. A well-evidenced "no edge" is a valid result.
  Never make a result look more complete, tested, or profitable than it is.

## Projects
| Folder | Code name | Status / stage | Own rules |
|---|---|---|---|
| `alt-arb/` | Project Osprey | Phase 2 data collection on the droplet; Decision A ~Oct 27 | `alt-arb/CLAUDE.md` |
| `alt-scalp/` | Project Coin Toss | S1 recording (laptop) | `alt-scalp/CLAUDE.md` |
| `alt-btc15/` | Project Slot Machine | S1: no edge for A–D. **Reopened 2026-10-14 → R1: read-only order-book recorder (laptop)** for a future maker test | `alt-btc15/CLAUDE.md` |
| `alt-edge/` | Project Bloodhound | **Planned** — starts when a slot opens (~Oct 22 or Osprey STOP) | `alt-edge/CLAUDE.md` (to come) |
Full status: `PORTFOLIO.md`. Cross-project decisions: `docs/decisions.md`.

## Portfolio-wide hard rules
1. **No live trading in any project** (Slot Machine included: $5/trade, $25/day, $100 total caps) without an explicit, dated owner decision recorded in that project's
   decisions log (and noted in `PORTFOLIO.md`). Default everything to read-only.
2. **Secrets only in `.env`** (gitignored). Never print, log, commit, screenshot, or paste API keys into prompts.
3. **Money as `Decimal` or integer cents**, never float.
4. **Pre-registered criteria are fixed.** Go/no-go thresholds are set before the data and not changed after looking
   at results; any change is recorded with the reason first.
5. **Stay in your lane.** A session works in one project. Don't edit another project's files; if a change is needed
   there, say so and stop. Cross-project changes happen in an HQ session (opened at `~/code/alt/`).
6. **Every working session ends with a wrap-up**: update the project's plan/stage, decisions log and `journal.md`,
   then commit and push. If the project has a `session-wrap-up` skill, use it.

## Shared resources — don't starve each other
| Resource | Who uses it | Where from |
|---|---|---|
| Kalshi public REST (Basic ≈ 20 req/s per key/IP) | Osprey scanner; Coin Toss recorder; Slot Machine recorder (~1.1 req/s) | Droplet; laptop; laptop |
| Polymarket US public REST (~30 req/min **per IP**, then 10 s block) | Osprey only | Droplet |
- Coin Toss must not call Polymarket from the droplet. Any new project that needs Polymarket must run from a
  different IP or coordinate with Osprey first.
- Slot Machine's R1 recorder runs 24/7 on the laptop next to Coin Toss's recorder: ~1 book request/s plus paced
  trade slices, and a 10 s pause on any 429 so it gives way to Coin Toss. Read-only, no keys. Any live phase still
  needs its own server and keys.
- Running services: Osprey scanner + daily pair refresh (DigitalOcean droplet `alt-arb`, systemd);
  Coin Toss recorder (laptop, launchd, runs from `~/code/alt/alt-scalp` — **don't move that folder** without
  reinstalling the launchd agent); Slot Machine recorder (laptop, launchd `com.idownham.slot.recorder`, runs from
  `~/code/alt/alt-btc15`; same rule).

## Class evidence (applies to every project)
- Each project keeps `docs/journal.md`: dated entries with work, commit links, observation/test, decision, and
  AI use + Ian's judgment (accepted / revised / rejected and why). Don't invent anything.
- Evidence-based iteration decisions (evidence → decision → consequence) are the most valuable entries; flag them.
- Key dates: **Oct 25** early prototype · **Nov 8** working build + test · **Nov 22** iteration + story ·
  **Dec 1** rough cuts · **Dec 4** final package.
- Screen recordings and screenshots must never show `.env`, keys, or account details.
