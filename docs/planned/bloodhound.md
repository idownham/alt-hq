# Project Bloodhound (alt-edge) — planned spec

*Captured 2026-10-14 in the planning chat. Becomes `alt-edge/docs/spec.md` when the repo is set up.*

## Hypothesis
Some prediction markets — starting with **mention markets** ("Will [person] say [word] during [event]?") — are
priced by casual traders on gut feel. Doing the homework (historical base rates, reading the exact rules, event
context) produces probability estimates that are better calibrated than the market's, often enough to beat fees.

## Why mention markets first
Many similar events, rich public transcripts, frequent resolutions, mostly retail traders, and rules with fine print
that many traders skip. Expand to other categories only after the method is shown to be calibrated here.

## Edge sources to test
1. **Base rates:** frequency of word X in comparable events (rally / press conference / interview / address), by
   length, topic, recency.
2. **Rule fine print:** word-form rules (plurals, compounds), who must say it, event window, sources used to
   resolve. Flag markets whose rules differ from what the title implies.
3. **Event context:** scheduled length, topic, news of the day.
4. **Live updating:** probability decay as an event runs without the word; does the market update too slowly?

## Method
- Collect markets: Kalshi mention series (and others later) — titles, rules, prices over time, outcomes.
- Collect transcripts for past events of the same speakers; build a searchable corpus honoring each market's
  word-form rules.
- Model: base-rate estimate adjusted for event type/length/context → probability. AI may read rules and propose
  adjustments, but every estimate is logged.
- **Calibration backtest (gate before any money):** on past resolved markets, does the model's 70% happen ~70% of
  the time? Is it better calibrated than the market's price (Brier/log score)? Out-of-sample only.
- Paper trade: log every market where model − price > fees + margin; track results.

## Pre-registered criteria (DRAFT — set before data)
- Calibration: model Brier score beats the market's closing-price Brier score on ≥ 100 out-of-sample markets.
- Paper: ≥ 50 paper trades, net positive after fees, with the edge concentrated where the model predicted it.
- Live (if ever): same caps style as Slot Machine; owner decision recorded first.

## Open questions for S0
- Which Kalshi series cover mention markets; volume and depth; fee type; how rules define word matches.
- Best free transcript sources and their coverage/latency.
- How often markets resolve; whether historical prices are available.
