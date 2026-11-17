# Early Prototype Update (Checkpoint 2)

**Ian Downham** · solo project · Founder Documentary, Fall 2026 · Checkpoint 2 (due Oct 25)

**Submitted late, on Nov __.** This covers work from Oct 11 to Oct 25. Nothing is backdated. Anything that happened
after Oct 25 is marked.

## What I built
By Oct 25 I had four read-only systems, each testing one idea for making money on prediction markets.
- **Osprey:** a cloud scanner comparing the same games on Kalshi and Polymarket, logging any gap after fees.
  Running 24/7 since Oct 13.
- **Coin Toss:** records the Kalshi order book and every trade around kickoff for NFL, NBA and NHL games.
- **Slot Machine:** a backtest of four strategies on Kalshi's 15-minute Bitcoin markets, then a live order book recorder.
- **Bloodhound:** research and a test plan for "Will Trump say X?" markets.

## First tests
**1. Slot Machine backtest (Oct 13–14).** 12,690 past windows, 61 strategy versions fixed before I saw any data, final
test run once. All four strategies lost money, including my own "sell at +10 cents" rule.
*Shows:* buying at the posted price doesn't beat fees here. *Doesn't show:* whether resting orders could, because
Kalshi keeps no order book history. So I stopped the project and reopened it to record the book myself.

**2. Coin Toss test games (Oct 14).** One game recorded clean. The other lost 8 minutes when my laptop lid closed.
*Shows:* the recorder works. *Doesn't show yet:* whether kickoff price noise can be traded. That needs the counted
games (from Oct 17).

**3. Osprey.** Collecting clean data since Oct 13 against pass/fail rules written beforehand.

## What I changed because of evidence
- Osprey's first 41 "opportunities" were fake (prices fetched minutes apart). I fixed the scanner and dropped them.
- Laptop sleep cost data in both recorders, so on Oct 18 I decided to move the recorders to the cloud server.

## AI use and my judgment
Claude Code wrote most of the code; I reviewed it and made the calls. It found a goal counted as "noise" in Coin
Toss; I chose to exclude big jumps before counted data came in. It suggested waiting until Oct 22 to start the Bitcoin
recorder; I overrode that. It recommended stopping Slot Machine; I agreed and declined an optional paper test.

## Next iteration (plan as of Oct 25)
- Osprey: Decision A around Oct 27, using the fixed rules.
- Coin Toss: reach 20 clean games, then run the noise analysis. It was planned for Oct 22–24
  and slipped to Nov 9.
- Slot Machine: collect order book data, then test resting orders, rules written first.
- Bloodhound: start building once a project frees up.

---

## Evidence links (dated)
| Date | Project | What it shows | Link |
|---|---|---|---|
| Oct 13 | Osprey | Pass/fail rules written before any clean data | [8944d1a](https://github.com/idownham/alt-arb/commit/8944d1a) |
| Oct 13 | Osprey | 41 fake gaps found and fixed | [9537fff](https://github.com/idownham/alt-arb/commit/9537fff) |
| Oct 13 | Osprey | Scanner moved to the cloud server | [d5c578c](https://github.com/idownham/alt-arb/commit/d5c578c) |
| Oct 13 | Coin Toss | Big jumps excluded from "noise" before counted data | [d5876bb](https://github.com/idownham/alt-scalp/commit/d5876bb) |
| Oct 14 | Coin Toss | First test games (journal entry, Oct 14 evening) | [alt-scalp journal](https://github.com/idownham/alt-scalp/blob/main/docs/journal.md) |
| Oct 13 | Slot Machine | Backtest rules fixed before pulling data | [816d8c7](https://github.com/idownham/alt-btc15/commit/816d8c7) |
| Oct 14 | Slot Machine | Test run once: nothing passes | [db0ed43](https://github.com/idownham/alt-btc15/commit/db0ed43) |
| Oct 14 | Slot Machine | Stopped, then reopened to record the order book | [e84871b](https://github.com/idownham/alt-btc15/commit/e84871b), [7691557](https://github.com/idownham/alt-btc15/commit/7691557) |
| Oct 15 | Osprey | Health check false alarm fixed | [569ba4e](https://github.com/idownham/alt-arb/commit/569ba4e), [ef072f8](https://github.com/idownham/alt-arb/commit/ef072f8) |
| Oct 18 | Slot Machine | Decision to move recorders off the laptop | [27ea4f3](https://github.com/idownham/alt-btc15/commit/27ea4f3) |
| Oct 14 | Bloodhound | Research done, pass/fail rules confirmed | [72d6b1b](https://github.com/idownham/alt-edge/commit/72d6b1b), [5db3067](https://github.com/idownham/alt-edge/commit/5db3067) |

Shared journal, source index and AI log: `docs/journal.md` in alt-hq.
Screenshots (recorded Nov __, showing the Oct work): *add file names here.*
