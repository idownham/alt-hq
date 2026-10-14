# Portfolio

*Last updated: 2026-10-14 (afternoon; local folders renamed to code names). Update this file in an HQ session whenever a project changes stage or a milestone moves.*

## Status
| Project | Stage | Running where | Next milestone | Gate |
|---|---|---|---|---|
| **Osprey** (alt-arb) | Phase 2 — collecting clean data (since 2026-10-13); close-out/handoff in progress | Droplet: scanner (~4 min/scan, 626 verified markets, 8 leagues) + daily 9 am pair refresh | Decision point A, earliest ~**Oct 27** (needs 14 days clean data, ≥ 3 leagues) | GO ≥ 5 qualifying episodes/week · STOP < 1/week |
| **Coin Toss** (alt-scalp) | S0 done, criteria confirmed; S1 recorder built | Laptop launchd agent, records each game −30 min → +20 min | 20 clean games (≥ 5 per league) by ~**Oct 22**; S2 analysis Oct 22–24 | Pre-registered in `project-coin-toss/docs/spec.md` |
| **Bloodhound** (alt-edge) | **Planned** — spec only (`docs/planned/bloodhound.md`) | Not running | Start when a slot opens: Coin Toss recording done (~Oct 22) or Osprey Decision A = STOP | Calibration backtest before any money |
| **Slot Machine** (alt-btc15) | S1 done: no strategy passed (A–D). **Reopened 2026-10-14 → R1:** read-only order-book recorder for a maker-strategy test | Laptop launchd agent, 24/7: book snapshot/s, trade tape, BTC price; ~1–3 GB/day | Maker pre-registration (rules, fill model, split, pass rule) before any analysis of the recorded data | No orders of any kind in R1. Go-live gate unchanged; A–D can't go live (failed S1) |

## Results
- **Slot Machine S1 (A–D):** 12,690 KXBTC15M windows (Jun 1 – Oct 12), 61 pre-registered variants, test run once.
  Test mean per trade: A −$0.81, B −$1.18, C −$0.27, D −$0.13. A–C still lose with generous fills (CIs below 0);
  D ≈ 0. The 1-min bid/ask swing (~15–17¢) beats the +10¢ scalp, and late favorites are priced correctly. Verdict:
  no edge after spread and fees at 1-minute speed. No money risked.

## Early signals (not conclusions)
- Osprey (first ~2 h clean data): 4 episodes, all in-play, best ≈ $2.59; ~87% of pair checks cost ≥ $1.00 to hedge
  before fees. Points toward MARGINAL/STOP, but far too early to call.
- Coin Toss S0: public trade tape exists (timestamps, size, aggressor side) → fills can be simulated honestly.
  Maker fee 0.25× taker on NFL/NBA/NHL game markets. No liquidity incentives on game-winner markets.
  One liquid NHL game sat at a 1¢ spread at start — tight spreads are a risk to the thesis.

## Timeline
| Date | Event |
|---|---|
| Oct 15–16 | Coin Toss test recordings (NHL; don't count) |
| Oct 17–19 | Coin Toss counted recordings: NHL Sat/Sun, NFL Sun + Mon |
| Oct 20–22 | Coin Toss: NBA opening week |
| Oct 22–24 | Coin Toss S2 analysis |
| **Oct 25** | Class: early prototype checkpoint |
| ~Oct 27 | Osprey Decision point A |
| Oct 26–Nov 8 | Coin Toss S3 maker simulation; Osprey Phase 3 only if Decision A = GO |
| **Nov 8** | Class: working build + test |
| **Nov 22** | Class: iteration + story assembly |
| **Dec 1 / Dec 4** | Class: rough cuts / final package |

## Owner to-dos (Ian)
- [ ] Osprey: spot-check ~10 agent/auto-verified pairs yourself (no pair has been read first-hand yet)
- [ ] Osprey: carry Coin Toss's fee-schedule check over (kalshi.com/fee-schedule read in a browser) to close the
      "0.07 base unconfirmed" item
- [ ] Coin Toss: keep the laptop awake, online and plugged in during game windows; decide on a second server if
      windows get missed
- [x] Slot Machine: stopped at S1 (2026-10-14), then reopened the same day for the R1 recorder.
- [ ] Slot Machine: approve the maker pre-registration before any analysis of the recorded book data
- [ ] Laptop disk: Slot Machine's recorder adds ~1–3 GB/day (656 GB free on 2026-10-14)
- [x] Local folders renamed to code names under `~/code/alt/` (2026-10-14); Osprey moved in from `~/code/alt-arb`
- [ ] App: point the Osprey daily-refresh scheduled task's folder and the session presets at the new folders
      (see `docs/decisions.md`, 2026-10-14 folder rename)
