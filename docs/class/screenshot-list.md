# Screenshot evidence list

For the checkpoint videos, the Dec 1 rough cuts and the capture index. Grouped by the documentary's five sections.
All repos are public, so every link opens logged out. **Mac:** Cmd+Shift+4 then drag (Cmd+Shift+5 for screen recording).
Save to one folder as `cap-##-short-name.png`. After each batch, add rows to the capture index in `docs/journal.md`
(date taken, file, what it shows, sizzle Y/N). Say they were captured Nov 25+; they show earlier, dated work.

**Never capture:** `.env` files, API keys, account balances, emails, the droplet IP, login screens.

## 1. The opportunity and starting point
| # | Capture | Where | Shows | Sizzle? |
|---|---|---|---|---|
| 01 | The same game on Kalshi and Polymarket, side by side | kalshi.com and polymarket.com market pages, logged out | The arbitrage idea in one picture | Y |
| 02 | A Kalshi 15-minute Bitcoin market moving | kalshi.com, search "Bitcoin price up or down" | Why Slot Machine looked tempting | Y |
| 03 | Your $5 phone trade, Oct 13 | Kalshi app trade history. **Crop out balance and account info** | The gut-feel moment that started Slot Machine | Y |
| 04 | Concept brief | https://github.com/idownham/alt-hq/blob/main/docs/class/01-concept-brief.md | The original plan and rules | N |

## 2. Building and early evidence
| # | Capture | Where | Shows | Sizzle? |
|---|---|---|---|---|
| 05 | Osprey commit history, Oct 6–13 | https://github.com/idownham/alt-arb/commits/main (scroll to Oct) | Dated build work | N |
| 06 | Decision A rules written before data | https://github.com/idownham/alt-arb/commit/8944d1a | Rules set before results | Y |
| 07 | "41 fake gaps" fix | https://github.com/idownham/alt-arb/commit/9537fff | First failed assumption, fixed | N |
| 08 | Coin Toss first test games | https://github.com/idownham/alt-scalp/blob/main/docs/journal.md (Oct 14 evening entry) | Recorder works; laptop lid kills a game | N |
| 09 | Slot Machine backtest rules | https://github.com/idownham/alt-btc15/blob/main/docs/s1-preregistration.md | 61 variants fixed before data | N |
| 10 | DigitalOcean droplet page | DigitalOcean dashboard. **Hide the IP** | The cloud server everything ran on | N |
| 11 | A Claude Code session mid-build | Claude Code app, any project session | AI writing code under your review | Y |

## 3. Tests, decisions and iteration
| # | Capture | Where | Shows | Sizzle? |
|---|---|---|---|---|
| 12 | Slot Machine S1: nothing passes | https://github.com/idownham/alt-btc15/blob/main/docs/s1-results.md | First verdict, Oct 14 | Y |
| 13 | Osprey Decision A: STOP | https://github.com/idownham/alt-arb/blob/main/docs/journal.md (Oct 28 entry) | 0 qualifying gaps, best $2.33 vs $20 bar | Y |
| 14 | Laptop sleep evidence | https://github.com/idownham/alt-scalp/blob/main/docs/journal.md (Nov 8 entry: 168 of 365 not clean) | Why recorders moved to the server | N |
| 15 | Server move decision | https://github.com/idownham/alt-hq/blob/main/docs/decisions.md (2026-11-08) | Iteration decision | N |
| 16 | Wrong-game pair caught | https://github.com/idownham/alt-arb/blob/main/docs/decisions.md (2026-11-10, Kentucky vs Western Kentucky) | The #1 risk actually happened | Y |
| 17 | Coin Toss S2: median 0 reversals | https://github.com/idownham/alt-scalp/blob/main/docs/s2-results.md | STOP across 196 games | Y |

## 4. Actual outcome
| # | Capture | Where | Shows | Sizzle? |
|---|---|---|---|---|
| 18 | Bloodhound final score | https://github.com/idownham/alt-edge/blob/main/docs/results/score-extension-2026-11-25.md | Model vs market, 2,043 markets, STOP | Y |
| 19 | Slot Machine maker test | https://github.com/idownham/alt-btc15/blob/main/docs/r1-results.md (Verdict section) | Spread earned vs adverse selection, FAIL | Y |
| 20 | Portfolio: all four done | https://github.com/idownham/alt-hq/blob/main/PORTFOLIO.md | Four verdicts, no edge, $0 risked by bots | Y |
| 21 | Your status site | claude.ai/artifact/XwdudFFr5dSPQYsat1kzHS | Plain-English summary of everything | N |

## 5. Reflection
| # | Capture | Where | Shows | Sizzle? |
|---|---|---|---|---|
| 22 | AI log table | https://github.com/idownham/alt-hq/blob/main/docs/journal.md (AI log) | Where you accepted, revised or rejected AI | N |
| 23 | A spot where you overrode Claude | https://github.com/idownham/alt-btc15/blob/main/docs/journal.md (Oct 14: you started the recorder right away) | Human judgment over AI | N |
