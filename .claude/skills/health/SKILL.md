---
name: health
description: Check the alt portfolio's health (the shared droplet's disk and clock, that every stopped service stays stopped, laptop disk, git sync) and print one green/red board. Use when Ian types /health or asks if everything is running.
---

# /health — portfolio health board

Run from the HQ folder (`~/code/alt/`). **Read-only**: never start, stop, restart, reinstall, or edit anything.
If something is broken, report it and suggest the fix; act only if Ian asks.

Folder names (renamed 2026-10-14; GitHub repos keep their `alt-*` names). If a folder isn't found, check for the
old `alt-*` name (or `~/code/alt-arb` for Osprey) and report it as 🔴 — something moved it back or a rename broke:
`project-osprey/` (alt-arb), `project-coin-toss/` (alt-scalp), `project-slot-machine/` (alt-btc15),
`project-bloodhound/` (alt-edge, planned — skip unless it has a `status` command).

## Checks (run them all, even if one fails)

Since 2026-11-25 14:35 UTC **nothing** is supposed to run. Osprey (shut down 2026-11-10), Coin Toss (recording stopped
2026-11-10) and Slot Machine (R1 recorder stopped 2026-11-25) are off on purpose; check they *stay* off. The droplet address is
`DROPLET_HOST` in `project-osprey/.env` (never print it). Use `ssh -o BatchMode=yes "$H" '…'`.

1. **Droplet — disk and clock**
   `df -h /` and `timedatectl show -p NTPSynchronized`. 🔴 under **5 GB free**, 🟡 under 10 GB (about 20 GB free when the
   last recorder stopped; nothing should grow it now). Nothing is deleted automatically.

2. **Stopped services stay stopped**
   `systemctl is-active alt-btc15-recorder altarb-scanner altarb-update.timer altscalp-recorder altscalp-update.timer`
   should all be `inactive`, and `systemctl is-enabled` the same units `disabled`. On the laptop, `launchctl list | grep idownham` should show nothing, and the Osprey daily-refresh scheduled
   task should be disabled. Anything running again is 🟡: report it, don't stop it.

3. **Laptop**
   `df -h ~` (warn under 50 GB free).

4. **Git sync (every repo: HQ + all project folders)**
   `git status --short` and `git log origin/main..HEAD --oneline` after `git fetch -q`. Flag uncommitted work or
   commits not pushed.

## Output

One board, then a short "Needs you" list (empty is good):

```
alt health — <date time CT>
Area           Service                  Status  Last activity        Note
Droplet        disk / clock             🟢/🟡/🔴 20 GB free           NTP ok
Stopped        Osprey, Coin Toss, Slot  🟢/🟡   all inactive         —
Laptop         disk                     🟢/🟡   612 GB free          —
Git            all repos                🟢/🟡   clean                —
Needs you: …
```
🟢 healthy · 🟡 needs a look, not urgent · 🔴 broken or not running. Keep it short; details only for non-green rows.
Also append one line per run to `docs/health-log.md` (date, overall 🟢/🟡/🔴, one-phrase summary) and commit it.
