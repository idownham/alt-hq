# Cross-project decisions

Decisions that affect more than one project or the portfolio as a whole. Project-specific decisions live in each
project's own `docs/decisions.md`. Newest last.

---

## 2026-10-13 — Start Project Coin Toss as a second track
**Decision (Ian):** explore kickoff market-making/scalping on Kalshi as a separate research project while Osprey
waits for Decision A data.
**Evidence:** Ian observed pre-kickoff prices swinging ±2% within a minute. Osprey's first clean data showed
arbitrage gaps are rare (~87% of pair checks cost ≥ $1.00 to hedge before fees).
**Consequence:** new repo `alt-scalp`; Osprey continues unchanged, gated by Decision A.

## 2026-10-13 — Separate repos plus an HQ repo
**Decision (Ian):** each project is its own repo with its own rules; `alt-hq` at `~/code/alt/` holds shared rules
(read by every session via the parent `CLAUDE.md`), the portfolio view, and cross-project decisions.
**Why:** sessions stay focused on one project; shared constraints (rate limits, class evidence, no live trading)
live in one place.

## 2026-10-13 — Code names
Osprey = alt-arb (watches two exchanges from above, strikes only on verified gaps).
Coin Toss = alt-scalp (pre-kickoff markets near 50/50, fast in-and-out).

## 2026-10-13 — Coin Toss is Kalshi-only
**Why:** Polymarket's public REST limit (~30 req/min) is per IP and already mostly used by Osprey's droplet scanner.

## 2026-10-13 — Start Project Slot Machine (alt-btc15)
**Decision (Ian):** third project — automated system for Kalshi's 15-minute BTC markets (`KXBTC15M`). Paper first,
then small live with hard caps ($5/trade, $25/day, $100 total). Strategies: direction at open, open scalp (+10¢),
late favorite, longshot fade. Replaces the "crypto-options" idea as the crypto track.
**Context:** Ian watched the market live and placed a manual $5 trade (showed $5.57 sell value after 20 s).
**Host:** paper trader may share Osprey's droplet (light load, modest Kalshi reads); live gets its own server so
trading keys and money are isolated from Osprey.

## 2026-10-13 — Slot Machine runs on the laptop
**Decision (Ian):** run Slot Machine on the laptop for now, not Osprey's droplet. The laptop now hosts Coin Toss's
recorder and Slot Machine; the droplet hosts only Osprey.

## 2026-10-14 — Slot Machine stopped at S1
**Decision (Ian):** stop Project Slot Machine after its S1 backtest. No paper or live phase.
**Evidence:** `alt-btc15/docs/s1-results.md`. None of strategies A–D passed the pre-registered out-of-sample test;
A–C lose even with generous fills, D ≈ 0. Project decision: `alt-btc15/docs/decisions.md` (same date).
**Consequence:** the laptop runs only Coin Toss's recorder, and Kalshi reads from the laptop are Coin Toss's alone.
Slot Machine's code and docs stay as class evidence (a valid "no edge" result).

## 2026-10-14 — Slot Machine reopened for a read-only order-book recorder (R1)
**Decision (Ian):** reopen Slot Machine (stopped at S1 earlier the same day) to record the KXBTC15M order book live,
the first step toward testing a resting-order (maker) strategy, which S1 didn't cover. Run now on the laptop.
Project decision: `alt-btc15/docs/decisions.md` (same date).
**Consequence:** the laptop runs two Kalshi recorders (Coin Toss + Slot Machine), about 1.1 req/s more on the shared
IP, still far under ~20 req/s. Slot Machine pauses on any 429 so it gives way to Coin Toss. No orders of any kind.

## 2026-10-14 — Plan Project Bloodhound (alt-edge)
**Idea (Ian):** find undervalued opportunities across prediction markets, starting with mention markets
("What will Trump say?").
**Why it's promising:** edge comes from homework (transcript base rates, rule fine print, event context, live
updating), not speed — the opposite of Osprey/Slot Machine's bot races. Mostly retail traders.
**Decision:** capture now as a planned project (`docs/planned/bloodhound.md`); don't start building until a slot
opens (Coin Toss recording done ~Oct 22, or Osprey Decision A = STOP), so in-flight projects and the Oct 25 class
checkpoint aren't thinned. Starts with mention markets only; widens once the method is calibrated.
**Rule carried over:** model probabilities must pass a calibration backtest on past events before any money moves.

## 2026-10-14 — Local folders renamed to code names
**Decision (Ian):** name each project's laptop folder by its code name, all under `~/code/alt/`. GitHub repo names
don't change (remotes untouched), and the droplet path `/opt/alt-arb` doesn't change.

| Old folder | New folder | Repo |
|---|---|---|
| `~/code/alt-arb` | `~/code/alt/project-osprey` | idownham/alt-arb |
| `~/code/alt/alt-scalp` | `~/code/alt/project-coin-toss` | idownham/alt-scalp |
| `~/code/alt/alt-btc15` | `~/code/alt/project-slot-machine` | idownham/alt-btc15 |
| (already) | `~/code/alt/project-bloodhound` | idownham/alt-edge |

**Why:** one tree, readable names that match the class story; Osprey was the last project outside `~/code/alt/`.
**How (HQ session, 15:29–15:40 CT):** preflight first (all repos clean and pushed, no other sessions open, next
Coin Toss window 18:00 CT, so none open or within 2.5 h). Unloaded both launchd agents at 15:30, moved the folders,
recreated each `.venv` (`pip install -e '.[dev]'`; tests: Osprey 165, Coin Toss 57, Slot Machine 88 passed), updated
each project's plist template to the new path, reinstalled and reloaded both agents at 15:31.
**Consequence / evidence:** both agents loaded from the new paths. Slot Machine recorded fresh book snapshots within
seconds; it logged one 69 s gap (15:30:43–15:31:51), the planned downtime. Coin Toss refreshed its schedule at
15:31:52; no game window was open, so it lost no recording. The Osprey daily-refresh scheduled task's prompt now
uses the new path. The app's own folder settings (the task's working folder and the session presets) are changed by
Ian in the app. Old Claude Code sessions still point at the old folders and won't reopen there; start new ones.

## 2026-10-14 — Bloodhound S0 started ahead of its trigger
**Decision (Ian):** start Bloodhound's S0 (research + lock the criteria) today, before the planned start trigger
(Coin Toss recording done ~Oct 22, or Osprey Decision A = STOP), so the project has dated evidence for the Oct 25
class checkpoint. Project decision: alt-edge `docs/decisions.md` (same date), commits a04f46f and 72d6b1b.
**Limit:** read-only desk research. One-off, paced (≤ 1 req/s, 10 s back-off on 429), unauthenticated reads of
public APIs only; no keys, no order code, no continuously running collectors (launchd/systemd/cron/24-7 polling)
until a slot opens. Criteria stay draft until Ian approves them.
**Evidence from S0:** mention markets close early once the word is said, so the closing price already contains the
answer; the draft gate (beat the closing-price Brier) is replaced in the *proposed* criteria v2 by the price 15 min
before the scheduled start, plus a ≥ 30-event minimum. Not confirmed — awaiting Ian (Q1–Q9).
**Consequence:** Bloodhound is added to the shared-resources table as an occasional laptop reader of Kalshi public
REST. Reading rollcall.com (Factbase) transcripts is pending Ian's answer to Q4 and isn't listed yet.

## 2026-10-14 — Plain-English status site, refreshed every HQ chat
**Decision (Ian):** keep a non-technical briefing website covering all projects, updated in every HQ chat or when
Ian asks. Source `docs/site/index.html`; published as a private Claude artifact
(https://claude.ai/artifact/XwdudFFr5dSPQYsat1kzHS). Refresh procedure: `.claude/skills/update-site/SKILL.md`.
**Why:** one place Ian can follow everything without reading four repos.
**Rules:** facts come only from each project's own docs and the latest `/health`; early signals stay labeled as not
conclusions; no keys, account details or `.env` content on the page. The page is private; Ian decides any sharing.

## 2026-10-15 — One shared server: resize Osprey's droplet and move both laptop recorders onto it
**Decision (Ian):** don't buy a separate server for Slot Machine. Resize the existing DigitalOcean droplet `alt-arb`
(Ian does this himself in the control panel) and run Osprey, Coin Toss and Slot Machine's recorders on it, so none of
them depend on the laptop being awake.
**Evidence:** the laptop slept on battery from 20:11 Oct 14 to 09:03 Oct 15. Slot Machine captured only ~16% of the
seconds since 19:00, and Coin Toss lost DAL@COL to a lid-close sleep. The droplet (1 vCPU, 1 GB RAM, 25 GB disk,
~$6/mo, sfo2) was nearly idle: load 0.00, ~350 MB RAM used, scanner ~36 MB. Ian's panel showed memory 38.6% and CPU 1.29%.
The two laptop recorders use ~30–43 MB RAM each and almost no CPU. **Disk is the constraint:** Slot Machine records
~1.4 GB/day at full coverage (21 GB free on the droplet), and Coin Toss ~6 MB/game.
**Target size:** Basic Regular, 1 vCPU / 2 GB / 50 GB SSD (~$12/mo, replacing the $6 plan). The disk increase is
permanent (it can't be shrunk back).
**Constraints kept:** read-only, no keys on this server. Only Osprey calls Polymarket (per-IP limit). All Kalshi
public reads now share one IP, still well under ~20 req/s (estimate; each project confirms its own peak). A future
live phase still needs its own server and keys. Each project gets its own Linux user, folder and systemd unit, set up
in that project's own session.
**Consequence:** a short Osprey scanner gap during the resize (power off/on), to be logged in Osprey's journal. Coin
Toss should move before counted games start Oct 17 (the Oct 15–16 test games can be the server trial). Slot Machine
moves mid-way through its R1 range; the host change and any overlap or gap are logged, and the pre-registered rules
don't change. Osprey's 9 am refresh stays a laptop scheduled task for now.

## 2026-10-28 — Osprey STOP opens Bloodhound's slot
**Decision (Ian, in an Osprey session):** Decision point A = STOP (`project-osprey/docs/decisions.md` 2026-10-28,
ae52199): 0 qualifying episodes in 15.2 days / 8 leagues. **Consequence:** per the 2026-10-14 Bloodhound plan, a
slot is open for Bloodhound S1. Osprey's scanner keeps running until Ian decides to shut it down.
*(Recorded in HQ on 2026-11-08.)*

## 2026-11-08 — Droplet resized; Coin Toss and Slot Machine recorders moved onto it
**Evidence:** the laptop kept sleeping. Slot Machine's logged gaps add up to ~3–20 h a day since Oct 31, and 168 of
Coin Toss's 365 counted windows (since Oct 17) are not clean.
**Decision (Ian, 2026-11-08):** Ian resized `alt-arb` to Basic 1 vCPU / 2 GB / 50 GB ($12/mo; the disk change is permanent)
and asked this HQ chat to do the moves and all the record-keeping across projects. That's an owner-requested exception to
"each project sets up its own move in its own session" (2026-10-15) and to the "stay in your lane" rule, for this
session only.
**Consequence:**
- Verified after the resize: 2 GB RAM, a 48 GB filesystem (44 GB free), the clock synced, the Osprey scanner active.
  Osprey's scan log had a gap of ~4 min.
- Slot Machine (`alt-btc15-recorder`, user `altbtc15`) started 2026-11-09 04:38 UTC. Coin Toss (`altscalp-recorder`,
  user `altscalp`, plus `altscalp-update.timer` and chrony) started 04:40 UTC. Both were installed from git bundles because
  the repos are private and no deploy keys existed. Their remotes point at GitHub, and read-only deploy keys were
  generated for Ian to add.
- Cutovers and overlaps are logged in each project's journal and decisions. Laptop data is kept as is.
- The Osprey daily refresh stays a laptop scheduled task.

## 2026-11-09/10 — Two STOPs close out; only Slot Machine keeps running
**Decision (Ian, 2026-11-09):** confirmed Coin Toss STOP at S2 (in its own session, `d9cb4ad`). Then he told this HQ chat to
"take over" with its recommendations: shut Osprey down cleanly, stop Coin Toss recording, and keep a disk guard for Slot Machine.
**Done (2026-11-10 UTC):**
- Osprey scanner + update timer disabled at 03:23. Final scan log archived to the laptop (checksum matched). Daily refresh task disabled.
  The full-archive report is still STOP. Its only 2 "qualifying" episodes were a wrong-game auto-verified pair
  (`project-osprey/docs/decisions.md` 2026-11-10, `7b41451`).
- Coin Toss server recorder + update timer disabled at 03:29, after the last trades were fetched. Server DB archived to the laptop
  (12 windows, all clean). Laptop agent unloaded (`201b8ee`).
- Disk guard: `/health` now checks droplet free space (🔴 < 5 GB) and that stopped services stay stopped. There's no auto-delete.
  At ~0.9–1.5 GB/day the 41 GB free lasts past Dec 4.
**Consequence:** the droplet runs only Slot Machine's recorder. The laptop runs nothing scheduled. Bloodhound's verdict comes
from the one pooled extension, scored around Nov 21.
