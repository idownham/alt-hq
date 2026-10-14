# Portfolio

*Last updated: 2026-10-13. Update this file in an HQ session whenever a project changes stage or a milestone moves.*

## Status
| Project | Stage | Running where | Next milestone | Gate |
|---|---|---|---|---|
| **Osprey** (alt-arb) | Phase 2 — collecting clean data (since 2026-10-13); close-out/handoff in progress | Droplet: scanner (~4 min/scan, 626 verified markets, 8 leagues) + daily 9 am pair refresh | Decision point A, earliest ~**Oct 27** (needs 14 days clean data, ≥ 3 leagues) | GO ≥ 5 qualifying episodes/week · STOP < 1/week |
| **Coin Toss** (alt-scalp) | S0 done, criteria confirmed; S1 recorder built | Laptop launchd agent, records each game −30 min → +20 min | 20 clean games (≥ 5 per league) by ~**Oct 22**; S2 analysis Oct 22–24 | Pre-registered in `alt-scalp/docs/spec.md` |
| **Slot Machine** (alt-btc15) | S0 research + data clients | Not running yet; paper trader → Osprey droplet | S1 backtest, then ≥ 7 days paper | Go-live gate in `alt-btc15/docs/spec.md` (proposed; Ian to confirm) · caps $5/trade, $25/day, $100 total |

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
- [ ] Slot Machine: confirm the go-live gate; log manual phone trades in `alt-btc15/docs/manual-trades.md`
- [ ] Move `alt-arb` into `~/code/alt/` once its sessions are closed
