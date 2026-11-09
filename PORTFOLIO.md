# Portfolio

*Last updated: 2026-11-08 (late evening CT: droplet resized; Coin Toss and Slot Machine recorders moved onto it; Osprey STOP recorded). Update this file in an HQ session whenever a project changes stage or a milestone moves.*

## Status
| Project | Stage | Running where | Next milestone | Gate |
|---|---|---|---|---|
| **Osprey** (alt-arb) | **Close-out: Decision point A = STOP (2026-10-28, ae52199).** 0 qualifying episodes in 15.2 days / 8 leagues | Droplet: scanner (still running, ~36–42 pairs) + daily 9 am pair refresh (laptop scheduled task) | Owner decision: shut the scanner and refresh down, or keep logging | Done: STOP < 1 qualifying episode/week was met (0.0/week) |
| **Coin Toss** (alt-scalp) | S1 recording, sample far exceeded (197 clean windows since Oct 17); **S2 analysis overdue** (planned Oct 22–24) | **Droplet since 2026-11-09 04:40 UTC** (`altscalp-recorder`); laptop agent kept as backup until the first server window (Nov 9 23:30 UTC) is verified | S2 analysis per `project-coin-toss/docs/spec.md` | Pre-registered in `project-coin-toss/docs/spec.md` |
| **Bloodhound** (alt-edge) | S0 done; criteria v2 confirmed 2026-10-14 (5db3067). **Slot open since Osprey STOP (Oct 28); S1 not started** | Not running — one-off paced public reads only (≤ 1 req/s), no keys | S1 build (`project-bloodhound/docs/s1-plan.md`) | Calibration backtest before any money |
| **Slot Machine** (alt-btc15) | R1: read-only order-book recorder for a maker test (pre-registration approved 2026-10-14). Coverage too low on the laptop, so the end date extends until ≥ 900 usable windows | **Droplet since 2026-11-09** (`alt-btc15-recorder`, cutover logged in its journal); laptop agent stopped after a one-window overlap | Reach ≥ 900 usable windows, then the pre-registered maker analysis | No orders of any kind in R1. Go-live gate unchanged; A–D can't go live (failed S1) |

**Shared server:** DigitalOcean droplet `alt-arb`, resized 2026-11-08 to Basic 1 vCPU / 2 GB / 50 GB ($12/mo). Each
project has its own Linux user, `/opt` folder and systemd unit. Read-only, no keys. Only Osprey calls Polymarket.

## Results
- **Osprey Decision point A: STOP (2026-10-28).** 15.2 days, 6,494 scans, 813,062 pair checks, 8 leagues. 1,040
  opportunity episodes (1,032 in-play, 8 pre-game); **0 qualifying** (pre-game, ≥ 2 scans, ≥ $20). Largest pre-game
  gap $2.33. Biases (scan speed, coverage drop from Oct 25, Oct 22 outage) all point toward under-counting and are
  recorded in `project-osprey/docs/decisions.md`. No money risked.
- **Slot Machine S1 (A–D):** 12,690 KXBTC15M windows (Jun 1 – Oct 12), 61 pre-registered variants, test run once.
  Test mean per trade: A −$0.81, B −$1.18, C −$0.27, D −$0.13. A–C still lose with generous fills (CIs below 0);
  D ≈ 0. The 1-min bid/ask swing (~15–17¢) beats the +10¢ scalp, and late favorites are priced correctly. Verdict:
  no edge after spread and fees at 1-minute speed. No money risked.

## Early signals (not conclusions)
- Coin Toss S0: public trade tape exists (timestamps, size, aggressor side) → fills can be simulated honestly.
  Maker fee 0.25× taker on NFL/NBA/NHL game markets. No liquidity incentives on game-winner markets.
  One liquid NHL game sat at a 1¢ spread at start — tight spreads are a risk to the thesis.

## Timeline
| Date | Event |
|---|---|
| **Oct 25** | Class: early prototype checkpoint |
| Oct 28 | Osprey Decision point A = STOP |
| **Nov 8** | Class: working build + test · droplet resized; recorders moved to it |
| Nov 9 23:30 UTC | First Coin Toss game window recorded on the server → verify, then unload the laptop agent |
| **Nov 22** | Class: iteration + story assembly |
| **Dec 1 / Dec 4** | Class: rough cuts / final package |

## Owner to-dos (Ian)
- [ ] **GitHub deploy keys (2 min):** add the two read-only keys printed in the Nov 8 HQ chat (users `altscalp` →
      repo alt-scalp, `altbtc15` → repo alt-btc15; "Allow write access" OFF). Until then the server copies can't pull updates.
- [ ] Coin Toss: after the Nov 9 evening games, confirm the server windows are clean, then unload the laptop agent
      (`launchctl unload ~/Library/LaunchAgents/com.idownham.altscalp.recorder.plist`)
- [ ] Coin Toss: run the S2 analysis (overdue since Oct 24)
- [ ] Osprey: decide whether to shut down the scanner and daily refresh (STOP is recorded)
- [ ] Osprey: spot-check ~10 agent/auto-verified pairs yourself (no pair has been read first-hand yet; lower priority after STOP)
- [ ] Bloodhound: start S1 (slot open since Oct 28)
- [x] Resize droplet `alt-arb` to 1 vCPU / 2 GB / 50 GB ($12/mo) — done 2026-11-08; Coin Toss and Slot Machine recorders moved onto it
- [x] App: Osprey daily-refresh scheduled task recreated in the new folder (2026-10-15)
- [x] Osprey: Kalshi 0.07 fee base confirmed against the fee schedule PDF (32b1407, 2026-10-13)
- [x] Slot Machine: stopped at S1 (2026-10-14), then reopened the same day for the R1 recorder.
- [x] Slot Machine: maker pre-registration approved as written, plus clarifications 1–7 (2026-10-14)
- [x] Bloodhound: answered Q1–Q9; criteria v2 confirmed (2026-10-14)
- [x] Local folders renamed to code names under `~/code/alt/` (2026-10-14); Osprey moved in from `~/code/alt-arb`
