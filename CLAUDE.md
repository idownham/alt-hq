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
| `project-osprey/` (repo alt-arb) | Project Osprey | **Close-out: Decision A = STOP (2026-10-28)**; scanner still running pending owner decision | `project-osprey/CLAUDE.md` |
| `project-coin-toss/` (repo alt-scalp) | Project Coin Toss | S1 recording (**droplet since 2026-11-09**); S2 analysis overdue | `project-coin-toss/CLAUDE.md` |
| `project-slot-machine/` (repo alt-btc15) | Project Slot Machine | S1: no edge for A–D. **Reopened 2026-10-14 → R1: read-only order-book recorder (droplet since 2026-11-09)** for a future maker test | `project-slot-machine/CLAUDE.md` |
| `project-bloodhound/` (repo alt-edge) | Project Bloodhound | **S0 started early 2026-10-14** (owner decision): read-only research only, no running services until a slot opens (~Oct 22 or Osprey STOP); criteria v2 confirmed 2026-10-14 | `project-bloodhound/CLAUDE.md` |
Local folders use code names (renamed 2026-10-14); GitHub repo names are unchanged. Full status: `PORTFOLIO.md`. Cross-project decisions: `docs/decisions.md`.

**Status site (HQ sessions only):** Ian's plain-English briefing page is `docs/site/index.html`, published as a private
artifact at https://claude.ai/artifact/XwdudFFr5dSPQYsat1kzHS. **Every HQ chat refreshes it** with the `/update-site`
skill (before the wrap-up commit), and so does any time Ian asks. Project sessions don't touch it.

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
| Kalshi public REST (Basic ≈ 20 req/s per key/IP) | Osprey scanner; Coin Toss recorder; Slot Machine recorder (~1.1 req/s); Bloodhound occasional one-off reads (≤ 1 req/s, 10 s back-off on 429; also reads rollcall.com transcripts ≤ 1 page/2 s, cached) | Droplet (one shared IP for the first three since 2026-11-09); laptop for Bloodhound |
| Polymarket US public REST (~30 req/min **per IP**, then 10 s block) | Osprey only | Droplet |
- Coin Toss must not call Polymarket from the droplet. Any new project that needs Polymarket must run from a
  different IP or coordinate with Osprey first.
- Since 2026-11-09 the droplet `alt-arb` (1 vCPU / 2 GB / 50 GB, resized 2026-11-08) runs all three recorders/scanners,
  each with its own Linux user, `/opt` folder and systemd unit. Read-only, no keys. Slot Machine keeps ~1 book request/s,
  paced trade slices and a 10 s pause on any 429. Any live phase still needs its own server and keys.
- Running services: **droplet** — Osprey scanner + 15-min update timer (`altarb-scanner`, user `altarb`, `/opt/alt-arb`);
  Coin Toss recorder + 15-min update timer (`altscalp-recorder`, user `altscalp`, `/opt/alt-scalp`); Slot Machine recorder
  (`alt-btc15-recorder`, user `altbtc15`, `/opt/alt-btc15`). The Coin Toss and Slot Machine copies were installed from git
  bundles; they pull from GitHub once their read-only deploy keys are added. **Laptop** — Osprey daily pair refresh (Claude
  desktop scheduled task, 9 am, runs in `~/code/alt/project-osprey`); Coin Toss's launchd agent as a backup until the first
  server window is verified (then unloaded). Moving a project folder also means updating that scheduled task's folder
  (recreate the task; see Osprey's journal 2026-10-15).
- Disk: Slot Machine's tape grows ~1.0–1.5 GB/day on the droplet; check `df -h /` in health checks (alert under 5 GB free).

## Class evidence (applies to every project)
- Each project keeps `docs/journal.md`: dated entries with work, commit links, observation/test, decision, and
  AI use + Ian's judgment (accepted / revised / rejected and why). Don't invent anything.
- Evidence-based iteration decisions (evidence → decision → consequence) are the most valuable entries; flag them.
- Key dates: **Oct 25** early prototype · **Nov 8** working build + test · **Nov 22** iteration + story ·
  **Dec 1** rough cuts · **Dec 4** final package.
- Screen recordings and screenshots must never show `.env`, keys, or account details.
