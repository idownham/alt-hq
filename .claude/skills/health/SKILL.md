---
name: health
description: Check the health of every running alt project (Osprey droplet scanner + daily refresh, Coin Toss recorder, Slot Machine recorder, laptop disk, git sync) and print one green/red board. Use when Ian types /health or asks if everything is running.
---

# /health — portfolio health board

Run from the HQ folder (`~/code/alt/`). **Read-only**: never start, stop, restart, reinstall, or edit anything.
If something is broken, report it and suggest the fix; act only if Ian asks.

Folder names (renamed 2026-10-14; GitHub repos keep their `alt-*` names). If a folder isn't found, check for the
old `alt-*` name (or `~/code/alt-arb` for Osprey) and report it as 🔴 — something moved it back or a rename broke:
`project-osprey/` (alt-arb), `project-coin-toss/` (alt-scalp), `project-slot-machine/` (alt-btc15),
`project-bloodhound/` (alt-edge, planned — skip unless it has a `status` command).

## Checks (run them all, even if one fails)

1. **Osprey — droplet scanner + daily refresh**
   `cd project-osprey && .venv/bin/python -m altarb.status` (exit 0 = healthy, 1 = needs attention).
   Needs `DROPLET_HOST` in `project-osprey/.env`. Report: scanner active?, last scan age, errors last hour,
   droplet disk %, last daily refresh time/result and whether it reached GitHub, games "needs review".
   Also check the daily-refresh scheduled task ran today (its log/run record) — it runs on the laptop.

2. **Coin Toss — kickoff recorder (laptop)**
   `launchctl list | grep com.idownham.altscalp.recorder` (loaded? last exit status 0?).
   `cd project-coin-toss && .venv/bin/altscalp status` → games recorded (CLEAN / not clean), counted vs the
   20-game target (≥ 5 per league), next scheduled window, any gaps.

3. **Slot Machine — R1 order-book recorder (laptop)**
   `launchctl list | grep com.idownham.slot.recorder` (loaded? last exit 0?).
   Freshness: time of the newest recorded snapshot/trade (newest file or row in its data store) — healthy if
   < 5 min old. Data size today vs the ~1–3 GB/day estimate. If the project has a `status` command, use it instead.

4. **Laptop**
   `df -h ~` (warn under 50 GB free), and whether the Mac slept through any scheduled Coin Toss window today
   (from the recorder's gap log).

5. **Git sync (every repo: HQ + all project folders)**
   `git status --short` and `git log origin/main..HEAD --oneline` after `git fetch -q`. Flag uncommitted work or
   commits not pushed.

## Output

One board, then a short "Needs you" list (empty is good):

```
alt health — <date time CT>
Project        Service                  Status  Last activity        Note
Osprey         droplet scanner          🟢/🔴   scan 3 min ago       0 errors/h, disk 41%
Osprey         daily pair refresh       🟢/🟡   today 09:02, pushed  2 games need review
Coin Toss      kickoff recorder         🟢/🔴   next window 18:30    7/20 counted (NFL 2, NBA 0, NHL 5)
Slot Machine   R1 book recorder         🟢/🔴   snapshot 4 s ago     1.8 GB today
Laptop         disk / sleep             🟢/🟡   612 GB free          no missed windows
Git            all repos                🟢/🟡   clean                —
Needs you: …
```
🟢 healthy · 🟡 needs a look, not urgent · 🔴 broken or not running. Keep it short; details only for non-green rows.
Also append one line per run to `docs/health-log.md` (date, overall 🟢/🟡/🔴, one-phrase summary) and commit it.
