# Is There Free Money in Prediction Markets? — Concept and Evidence Plan

**Ian Downham** · solo project · Founder Documentary, Fall 2026 · Checkpoint 1 (due Oct 11)

**Written 2026-10-14, after the Oct 11 due date.** Building began Oct 6, so parts of this plan are already
under way. Anything dated after Oct 11 is marked as such; nothing is backdated.

## 1. Problem and opportunity
Prediction markets (Kalshi, Polymarket US) are federally regulated and open to US retail. Prices for
the same event sometimes differ between venues, swing around game start, or look set on gut feel. **Can a part-time, AI-assisted builder find a real, repeatable edge after fees, or is
it already taken by faster bots?** The answer matters to any retail trader tempted.

## 2. Project statement
I will build **read-only data systems** that measure each suspected edge against go/no-go criteria **fixed before
any data is seen**. Boundary: public data only; no orders or money at risk without a dated owner decision.

| Track | What it tests | Measurable criteria (pre-registered) |
|---|---|---|
| **Osprey** (since Oct 6) | Cross-venue arbitrage, scanned 24/7 in the cloud | ≥ 14 days, ≥ 3 leagues. **GO** if ≥ 5 qualifying gaps/week (pre-game, lasts ≥ 2 scans, ≥ $20 net of fees and depth); **STOP** if < 1/week |
| **Coin Toss** (added Oct 13) | Market-making around game start | ≥ 20 clean games. Continue only if the median game has ≥ 3 tradable reversals. **GO** if simulated net P&L > 0, positive in ≥ 60% of games, adverse selection < 50% of spread, ≥ 100 round trips |
| **Slot Machine** (added Oct 13) | Bitcoin 15-minute markets (backtest) | Pass only if capped out-of-sample net P&L > 0 |
| **Bloodhound** (planned) | Homework (transcript base rates, rule fine print) vs. casual pricing on "mention" markets | *Draft, fixed before data:* model beats the market's closing-price Brier score on ≥ 100 out-of-sample markets; then ≥ 50 paper trades net positive after fees |

**Success** means each track reaches a verdict backed by pre-registered evidence. "No edge" is a valid result.

## 3. Scope plan
- **Smallest viable version:** a scanner logging net-of-fee gaps, plus a criteria report (Osprey).
- **Key unknowns:** how often gaps occur; whether "matching" markets share rules; whether 4-minute scans miss
  short gaps; free transcript coverage (Bloodhound).
- **Safety and ethics:** read-only; no credentials on screen or in prompts; rate limits respected; legality varies by state.
- **Resources:** laptop, cloud server, Python, Claude Code, public APIs.
- **Roles:** solo; I decide, verify and film. AI writes most code under my review.
- **Timeline:** Coin Toss recording Oct 15–22 · Bloodhound starts ~Oct 22 · Osprey Decision A ~Oct 27 · working
  build and test Nov 8 · story assembly Nov 22.

## 4. Test and evidence plan
I will measure logged gaps, scan errors and venue timing skew (Osprey); order books and trades (Coin Toss); and
backtest P&L (Slot Machine); calibration on past markets (Bloodhound). **Progress** is clean data accumulating. **A need to change direction** is a STOP verdict, data artifact, or rule mismatch.
Each verdict comes from a script applying the fixed criteria.

## 5. Documentary plan
- **Story questions:** Do speed edges vanish after fees? Can homework beat speed? When an idea fails, stop or pivot?
- **Real moments:** the scanner running; my manual $5 trade (Oct 13); the backtest where nothing passed (Oct 13);
  live game recordings; the Decision A verdict.
- **Dated evidence:** commits, journals, decision logs and weekly screen recordings, indexed in the journal.

## 6. Sources and AI plan
Sources are listed below. AI uses, each logged with my judgment:
1. **Claude Code (Claude Opus)** for research, code, tests and docs; I review outputs and set every pass rule. *Begun:* it caught a goal "jump" counted as noise; I chose to exclude jumps (Oct 13).
2. **AI image and video tools** for labeled illustrative explainers (order books, arbitrage).

## 7. Recording contributions
Solo: each journal entry records my decision, the AI's output, and whether I accepted, revised or rejected it,
with the commit.

*Shared journal, source index and AI log: `docs/journal.md` in my private project repository.*

## Initial source list
| Source | Organization | Link | How it informs the project |
|---|---|---|---|
| Kalshi API documentation | Kalshi | https://docs.kalshi.com | Public market data, order books, rate limits |
| Kalshi fee schedule (effective 2026-07-07, checked 2026-10-13) | Kalshi | https://kalshi.com/docs/kalshi-fee-schedule.pdf | Taker and maker fee rates used in every P&L |
| Polymarket US documentation | Polymarket US | https://docs.polymarket.us | Public market data; WebSockets need API keys, so the scanner polls instead |
| Polymarket US fees (effective 2026-10-07) | Polymarket US | https://docs.polymarket.us/fees | Taker fee and maker rebate used in arbitrage math |
