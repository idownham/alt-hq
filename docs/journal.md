# Shared project journal, source index and AI log

*Founder Documentary, Fall 2026 · Ian Downham (solo). One living file for the class. Detailed day-by-day entries
stay in each project's own log, and this file indexes them. Commit links point to Ian's private GitHub repos.*

| Project | Repo | Detailed log |
|---|---|---|
| Osprey | [idownham/alt-arb](https://github.com/idownham/alt-arb) | `docs/plan.md`, `docs/decisions.md` (no journal file yet) |
| Coin Toss | [idownham/alt-scalp](https://github.com/idownham/alt-scalp) | `docs/journal.md`, `docs/decisions.md` |
| Slot Machine | [idownham/alt-btc15](https://github.com/idownham/alt-btc15) | `docs/journal.md`, `docs/decisions.md`, `docs/class-summary.md` |
| Bloodhound (planned) | [idownham/alt-edge](https://github.com/idownham/alt-edge) | `docs/journal.md` |
| HQ (this repo) | [idownham/alt-hq](https://github.com/idownham/alt-hq) | `docs/decisions.md`, `docs/health-log.md` |

---

## Build log (key entries)
All work by Ian, with Claude Code writing code under Ian's review unless noted.

**2026-10-06 · Osprey · [b04ed56](https://github.com/idownham/alt-arb/commit/b04ed56), [1bb44db](https://github.com/idownham/alt-arb/commit/1bb44db)**
Work: started the project, with rules (read-only, no secrets in code, money as Decimal) and a phased build plan.
Decision/next: build a read-only scanner before anything that trades.

**2026-10-10 · Osprey v0.1 · [5791199](https://github.com/idownham/alt-arb/commit/5791199) … [98b3ac3](https://github.com/idownham/alt-arb/commit/98b3ac3)**
Work: read-only Kalshi and Polymarket US clients, pair table, matcher, fee models, depth-aware edge calculation,
scanner loop with a SQLite log, laptop service, and cloud deploy scripts.
**Iteration (constraint → decision):** both venues' WebSockets need API keys even for public data, so live books
were deferred to Phase 4 and the scanner polls REST ([4577173](https://github.com/idownham/alt-arb/commit/4577173)).
Consequence: gaps shorter than one scan can be missed, a bias recorded for Decision A.

**2026-10-13 · Osprey v0.2 · [9537fff](https://github.com/idownham/alt-arb/commit/9537fff), [8944d1a](https://github.com/idownham/alt-arb/commit/8944d1a)**
**Iteration (failed assumption → decision):** all 41 "opportunities" in the laptop log compared order books
fetched minutes to hours apart. They were artifacts, not edge. Fix: fetch both legs back to back and reject stale
comparisons. Old rows are excluded from all results. Then Decision A criteria were pre-registered before any clean
data, and the scanner moved to a cloud server ([d5c578c](https://github.com/idownham/alt-arb/commit/d5c578c)).

**2026-10-13 · Coin Toss S0–S2 · [298dbd7](https://github.com/idownham/alt-scalp/commit/298dbd7) … [70cbfcf](https://github.com/idownham/alt-scalp/commit/70cbfcf)**
Work: venue research, pre-registered criteria, recorder, and S2 analysis code run on test games only.
**Iteration (test data → decision):** a goal "jump" counted as a noise reversal → jumps (≥ 3 × X) excluded from
the count, before any counted data ([d5876bb](https://github.com/idownham/alt-scalp/commit/d5876bb)). Consequence: a stricter gate.

**2026-10-13/14 · Slot Machine S0–S1 · [af3fdca](https://github.com/idownham/alt-btc15/commit/af3fdca) … [e84871b](https://github.com/idownham/alt-btc15/commit/e84871b)**
Work: Ian's manual $5 trade (Oct 13), research, a pre-registered backtest of 61 variants, and a test phase run once.
Observation: no strategy passed ([db0ed43](https://github.com/idownham/alt-btc15/commit/db0ed43)).
**Iteration (result → decision):** stopped at S1 with no money risked ([e84871b](https://github.com/idownham/alt-btc15/commit/e84871b)).
It reopened the same day to record order books for a maker strategy S1 didn't test ([7691557](https://github.com/idownham/alt-btc15/commit/7691557)).

**2026-10-14 · Portfolio · HQ [9740601](https://github.com/idownham/alt-hq/commit/9740601)**
Work: `/health` board, and folders renamed to code names. Concept brief written late (due Oct 11): `docs/class/01-concept-brief.md`.

**2026-10-14 (evening) · Portfolio · HQ**
Work: `/health` at 18:40 CT was 🟡 (laptop on battery during a Coin Toss window; Slot Machine lost ~25 min to a network/DNS drop, 17:26–17:59, outside any Coin Toss window). Checked all four project sessions; all healthy. Recorded Bloodhound's early S0 start in `PORTFOLIO.md`, `CLAUDE.md` and `docs/decisions.md`.
Decision: Ian approved the HQ updates; criteria v2 stays *proposed*, and the rollcall.com source isn't listed until Ian answers Q4.
Later the same evening Bloodhound recorded Ian's answers (5db3067: criteria v2 confirmed, Factbase allowed with limits), so HQ now says confirmed and lists rollcall.com.
Work: built a plain-English status site for Ian (`docs/site/index.html`, private artifact) plus an `/update-site` skill. It is refreshed in every HQ chat.

**2026-10-15 · Osprey · [569ba4e](https://github.com/idownham/alt-arb/commit/569ba4e), [ef072f8](https://github.com/idownham/alt-arb/commit/ef072f8)**
**Iteration (false alarm → decision):** HQ saw Osprey's health check say "no scans" while the scanner was fine. The
database was locked during each long scan. Fix: report "couldn't read DB", then switch the scan log to WAL mode so
reads never wait. Also, the 9 am refresh had silently stopped after the folder move. Its scheduled task was recreated in the new folder (Osprey journal).

**2026-10-28 · Osprey Decision A = STOP · [ae52199](https://github.com/idownham/alt-arb/commit/ae52199)**
**Iteration (pre-registered result → decision):** 15.2 days, 8 leagues, 0 qualifying episodes (bar: ≥ 1/week to avoid
STOP). The largest pre-game gap was $2.33 against a $20 bar. Consequence: no paper or live phase. Osprey becomes a finished
"no edge" result, and Bloodhound's slot opens.

**2026-11-08 · Portfolio · shared server · Coin Toss [014c442](https://github.com/idownham/alt-scalp/commit/014c442), Slot Machine [918700b](https://github.com/idownham/alt-btc15/commit/918700b), Osprey [6ed9370](https://github.com/idownham/alt-arb/commit/6ed9370)**
**Iteration (evidence → decision → consequence):** laptop sleep kept costing data (Slot Machine coverage swung from
~1% to 98% of a day; 168 of 365 Coin Toss windows not clean) → Ian resized the droplet to 2 GB / 50 GB ($12/mo) →
both recorders now run on it under their own users. Cutovers are logged in each project. This HQ chat did the moves
and caught up every journal at Ian's request (HQ decisions 2026-11-08).

---

## AI log
| Date | Tool · task | Prompt / instruction (excerpt) | Output | Ian's judgment → action | Evidence |
|---|---|---|---|---|---|
| 10-10 | Claude Code · pair verification | "verify Kalshi ↔ Polymarket pairs" | Proposed pairs with rule comparisons | Allowed agent-assisted verification **only with owner approval** | [1d2bf8c](https://github.com/idownham/alt-arb/commit/1d2bf8c), [0c0737e](https://github.com/idownham/alt-arb/commit/0c0737e) |
| 10-13 | Claude Code · Coin Toss S0 research | read venue docs, probe the public API | `s0-research.md`; flagged the 0.07 fee base as inferred, not quoted | Ian checked the fee schedule in a browser and confirmed it | Coin Toss journal; [32b1407](https://github.com/idownham/alt-arb/commit/32b1407) |
| 10-13 | Claude Code · S2 analysis | build the reversal detector, run on test games | Detector + finding that a goal jump counted as noise | **Revised:** Ian chose to exclude jumps in either direction | [d5876bb](https://github.com/idownham/alt-scalp/commit/d5876bb), [70cbfcf](https://github.com/idownham/alt-scalp/commit/70cbfcf) |
| 10-14 | Claude Code · R1 maker pre-registration | draft the test before any data | Draft + 4 optional changes flagged | **Accepted as written**, declining the 4 optional changes | [8f98e28](https://github.com/idownham/alt-btc15/commit/8f98e28) |
| 10-14 | Claude Code · concept brief | draft the Oct 11 brief from the repos | This checkpoint's brief | *Ian to fill in: accepted / revised / rejected* | `docs/class/01-concept-brief.md` |
| 10-28 | Claude Code · Osprey Decision A | "Yes, record STOP" | Report + episode/error queries; STOP entry with the biases listed | **Accepted** STOP without changing criteria | [ae52199](https://github.com/idownham/alt-arb/commit/ae52199) |
| 11-08 | Claude Code (HQ chat) · server move + records | "Can you go move everything, update everything, and then backlog everything into github" | Both recorders deployed on the droplet; journals, decisions, portfolio and site updated from logs and data | **Accepted** the $12 plan (chose it over $18). *Ian to fill in on the rest* | HQ decisions 2026-11-08 |

*Exact prompts weren't saved for the early entries; excerpts are paraphrased from the commits. From now on, paste a
one-line real excerpt.*

---

## Source index
| Source | Org | Date checked | Link | How it informed the project |
|---|---|---|---|---|
| Kalshi API docs | Kalshi | 2026-10 | https://docs.kalshi.com | Market data endpoints; rate limits |
| Kalshi fee schedule (PDF) | Kalshi | 2026-10-13 | https://kalshi.com/docs/kalshi-fee-schedule.pdf | Taker 0.07 and maker 0.0175 fee rates used in every P&L |
| Polymarket US docs | Polymarket US | 2026-10 | https://docs.polymarket.us | Public market data; WebSockets need keys (→ REST scanner) |
| Polymarket US fees | Polymarket US | 2026-10 (effective 10-07) | https://docs.polymarket.us/fees | Taker Θ 0.0695, maker rebate |

---

## Capture index (footage, screenshots)
*Ian to add: file name/link, date, what it shows, sizzle-worthy? (Y/N). Don't list anything that wasn't captured.*

| Date | File / link | Shows | Sizzle? |
|---|---|---|---|
| | | | |
