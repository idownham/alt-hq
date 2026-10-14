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
