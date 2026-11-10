# Portfolio

*Last updated: 2026-11-09 (late evening CT: Osprey shut down, Coin Toss STOP at S2 and recording stopped, Bloodhound test INCONCLUSIVE → extension). Update this file in an HQ session whenever a project changes stage or a milestone moves.*

## Status
| Project | Stage | Running where | Next milestone | Gate |
|---|---|---|---|---|
| **Osprey** (alt-arb) | **Done: STOP** (Decision A, 2026-10-28). Shut down 2026-11-10; scan log archived | Nothing (scanner, update timer and daily refresh disabled) | — (class story only) | STOP < 1 qualifying episode/week: met (0.0/week) |
| **Coin Toss** (alt-scalp) | **Done: STOP at S2** (Ian confirmed 2026-11-09, d9cb4ad): median 0 reversals in 196 clean games, ≥ 3 needed. Recording stopped 2026-11-10 | Nothing (server units disabled, laptop agent unloaded) | — (class story only) | Pre-registered S2 gate failed |
| **Bloodhound** (alt-edge) | **S1:** model frozen (blend-v1, bb92f3a); test scored once 2026-11-09 → **INCONCLUSIVE** (Brier 0.1614 vs market 0.1631, CI [−0.0043, +0.0010]) → the one pre-registered extension | Nothing continuous; hand-run paced reads on the laptop | **~Nov 21:** collect events through Nov 20, score pooled test + extension once (`scripts/score_extension.py`) → PASS or STOP; time box Nov 22 | Pooled Brier < market with 95% upper bound < 0; still inconclusive = STOP |
| **Slot Machine** (alt-btc15) | R1: read-only order-book recorder for a maker test (pre-registration approved 2026-10-14); end date extends until ≥ 900 usable windows | **Droplet** (`alt-btc15-recorder`, since cutover 2026-11-09 04:45 UTC). The only service still running | Reach ≥ 900 usable windows, then the pre-registered maker analysis | No orders of any kind in R1. A–D can't go live (failed S1) |

**Shared server:** DigitalOcean droplet `alt-arb`, Basic 1 vCPU / 2 GB / 50 GB ($12/mo, resized 2026-11-08). Only Slot
Machine's recorder runs on it now. Osprey's and Coin Toss's code and data stay there with their services disabled.
Disk: 41 GB free on 2026-11-10, with R1 growing ~0.9–1.5 GB/day (`/health` alerts under 5 GB).

## Results
- **Coin Toss S2: STOP (2026-11-09).** 196 counted clean games (Oct 17 – Nov 8). Median price reversals per game 0
  vs the pre-registered ≥ 3 (`project-coin-toss/docs/s2-results.md`). S3 not run. No money risked.
- **Osprey, post-verdict check (2026-11-10):** the full archive (through Nov 10) is still STOP (0.5/week). Its only
  2 "qualifying" episodes came from a wrong-game pair (Kentucky @ Tennessee auto-matched to Western Kentucky vs Middle
  Tennessee State, auto-verified Oct 24). Now un-verified. This is a real example of the #1 risk, resolution mismatch.
- **Osprey Decision point A: STOP (2026-10-28).** 15.2 days, 6,494 scans, 813,062 pair checks, 8 leagues. 1,040
  opportunity episodes (1,032 in-play, 8 pre-game); **0 qualifying** (pre-game, ≥ 2 scans, ≥ $20). Largest pre-game
  gap $2.33. Biases (scan speed, coverage drop from Oct 25, Oct 22 outage) all point toward under-counting and are
  recorded in `project-osprey/docs/decisions.md`. No money risked.
- **Slot Machine S1 (A–D):** 12,690 KXBTC15M windows (Jun 1 – Oct 12), 61 pre-registered variants, test run once.
  Test mean per trade: A −$0.81, B −$1.18, C −$0.27, D −$0.13. A–C still lose with generous fills (CIs below 0);
  D ≈ 0. The 1-min bid/ask swing (~15–17¢) beats the +10¢ scalp, and late favorites are priced correctly. Verdict:
  no edge after spread and fees at 1-minute speed. No money risked.

## Early signals (not conclusions)
- Bloodhound test (60 events / 1,640 markets): the frozen model's Brier score was slightly better than the market's
  (−0.0017), but the 95% CI includes 0, so the result is **inconclusive**. The pooled extension decides.

## Timeline
| Date | Event |
|---|---|
| Oct 28 | Osprey Decision point A = STOP |
| **Nov 8** | Class: working build + test · droplet resized; recorders moved to it |
| Nov 9 | Coin Toss S2 = STOP · Bloodhound S1 frozen + test scored (inconclusive) |
| Nov 10 | Osprey shut down; Coin Toss recording stopped (both archived) |
| ~Nov 21 | Bloodhound: score the pooled extension once → PASS or STOP |
| **Nov 22** | Class: iteration + story assembly · Bloodhound time box |
| **Dec 1 / Dec 4** | Class: rough cuts / final package |

## Owner to-dos (Ian)
- [ ] **~Nov 21: Bloodhound extension.** Open a Bloodhound session to collect events through Nov 20 and run the pooled scorer once.
- [ ] Fill in the "Ian's judgment: (to fill in)" lines in each project's journal and the HQ AI log.
- [ ] Slot Machine: when R1 reaches 900 usable windows, open a Slot Machine session for the pre-registered maker analysis.
- [ ] Optional: Osprey spot-check of auto-verified pairs (the Nov 10 wrong-game find shows why it matters, but the project is done).
- [x] Coin Toss S2 run: STOP (2026-11-09) · recording stopped and archived (2026-11-10)
- [x] Osprey shut down and archived (2026-11-10)
- [x] Bloodhound S1 started, model frozen, test scored once (2026-11-09)
- [x] GitHub deploy keys added for alt-scalp and alt-btc15 (2026-11-09)
- [x] Coin Toss server windows verified clean (Nov 9 evening)
- [x] Resize droplet `alt-arb` to 1 vCPU / 2 GB / 50 GB ($12/mo) — done 2026-11-08
- [x] App: Osprey daily-refresh scheduled task recreated in the new folder (2026-10-15); disabled 2026-11-10
- [x] Osprey: Kalshi 0.07 fee base confirmed against the fee schedule PDF (32b1407, 2026-10-13)
- [x] Slot Machine: stopped at S1 (2026-10-14), then reopened the same day for the R1 recorder.
- [x] Slot Machine: maker pre-registration approved as written, plus clarifications 1–7 (2026-10-14)
- [x] Bloodhound: answered Q1–Q9; criteria v2 confirmed (2026-10-14)
- [x] Local folders renamed to code names under `~/code/alt/` (2026-10-14); Osprey moved in from `~/code/alt-arb`
