---
name: health
description: Check the health of every running alt project (the shared droplet and Slot Machine's recorder on it, the stopped Osprey and Coin Toss services, laptop disk, git sync) and print one green/red board. Use when Ian types /health or asks if everything is running.
---

# /health — portfolio health board

Run from the HQ folder (`~/code/alt/`). **Read-only**: never start, stop, restart, reinstall, or edit anything.
If something is broken, report it and suggest the fix; act only if Ian asks.

Folder names (renamed 2026-10-14; GitHub repos keep their `alt-*` names). If a folder isn't found, check for the
old `alt-*` name (or `~/code/alt-arb` for Osprey) and report it as 🔴 — something moved it back or a rename broke:
`project-osprey/` (alt-arb), `project-coin-toss/` (alt-scalp), `project-slot-machine/` (alt-btc15),
`project-bloodhound/` (alt-edge, planned — skip unless it has a `status` command).

## Checks (run them all, even if one fails)

Since 2026-11-10 only **Slot Machine's recorder** is supposed to run. Osprey (STOP, shut down 2026-11-10) and Coin Toss
(STOP at S2, recording stopped 2026-11-10) are off on purpose; check they *stay* off. The droplet address is
`DROPLET_HOST` in `project-osprey/.env` (never print it). Use `ssh -o BatchMode=yes "$H" '…'`.

1. **Droplet — disk and clock** (the main guard now)
   `df -h /` and `timedatectl show -p NTPSynchronized`. 🔴 under **5 GB free**, 🟡 under 10 GB. Also report
   `du -sh /opt/alt-btc15/data` and days left at the current growth (~0.9–1.5 GB/day).
   Nothing is deleted automatically. If space is low, raise it with Ian (options: stop R1 once it has 900 usable windows,
   or add a DigitalOcean volume).

2. **Slot Machine — R1 order-book recorder (droplet)**
   `systemctl is-active alt-btc15-recorder` and
   `cd /opt/alt-btc15 && runuser -u altbtc15 -- .venv/bin/python -m slot.recorder status --db /opt/alt-btc15/data/recorder/book.sqlite`
   → last book age (🟢 under 5 min), gaps, errors and rate-limit pauses in the last 24 h.

3. **Stopped services stay stopped**
   `systemctl is-active altarb-scanner altarb-update.timer altscalp-recorder altscalp-update.timer` should all be
   `inactive`. On the laptop, `launchctl list | grep idownham` should show nothing, and the Osprey daily-refresh scheduled
   task should be disabled. Anything running again is 🟡: report it, don't stop it.

4. **Laptop**
   `df -h ~` (warn under 50 GB free).

5. **Git sync (every repo: HQ + all project folders)**
   `git status --short` and `git log origin/main..HEAD --oneline` after `git fetch -q`. Flag uncommitted work or
   commits not pushed.

## Output

One board, then a short "Needs you" list (empty is good):

```
alt health — <date time CT>
Area           Service                  Status  Last activity        Note
Droplet        disk / clock             🟢/🟡/🔴 41 GB free           ~40 days left, NTP ok
Slot Machine   R1 book recorder         🟢/🔴   book 2 s ago         0 gaps, 0 errors (24 h)
Stopped        Osprey, Coin Toss        🟢/🟡   all inactive         —
Laptop         disk                     🟢/🟡   612 GB free          —
Git            all repos                🟢/🟡   clean                —
Needs you: …
```
🟢 healthy · 🟡 needs a look, not urgent · 🔴 broken or not running. Keep it short; details only for non-green rows.
Also append one line per run to `docs/health-log.md` (date, overall 🟢/🟡/🔴, one-phrase summary) and commit it.
