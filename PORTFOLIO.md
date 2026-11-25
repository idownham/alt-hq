# Portfolio

*Last updated: 2026-11-25 (Bloodhound S1 = STOP after the pooled extension, confirmed by Ian; Slot Machine R1 maker analysis started). Update this file in an HQ session whenever a project changes stage or a milestone moves.*

## Status
| Project | Stage | Running where | Next milestone | Gate |
|---|---|---|---|---|
| **Osprey** (alt-arb) | **Done: STOP** (Decision A, 2026-10-28). Shut down 2026-11-10; scan log archived | Nothing (scanner, update timer and daily refresh disabled) | — (class story only) | STOP < 1 qualifying episode/week: met (0.0/week) |
| **Coin Toss** (alt-scalp) | **Done: STOP at S2** (Ian confirmed 2026-11-09, d9cb4ad): median 0 reversals in 196 clean games, ≥ 3 needed. Recording stopped 2026-11-10 | Nothing (server units disabled, laptop agent unloaded) | — (class story only) | Pre-registered S2 gate failed |
| **Bloodhound** (alt-edge) | **Done: STOP at S1** (Ian confirmed 2026-11-25, e4b65be). Pooled test + extension (71 events / 2,043 markets): Brier 0.1568 vs market 0.1580, CI [−0.0035, +0.0012], still includes 0 → STOP by the pre-registered rule | Nothing | — (class story only) | Pooled 95% upper bound < 0 needed: not met |
| **Slot Machine** (alt-btc15) | R1: read-only order-book recorder (pre-registration approved 2026-10-14). **Maker analysis started 2026-11-25** (separate Slot Machine session): merging laptop + droplet data, counting usable windows, then the test set once | **Droplet** (`alt-btc15-recorder`, since 2026-11-09 04:45 UTC). The only service still running; ~1,525 windows recorded, 21 GB free (~2 weeks) on 2026-11-25 | R1 maker verdict; then decide whether to stop the recorder | No orders of any kind in R1. A–D can't go live (failed S1) |

**Shared server:** DigitalOcean droplet `alt-arb`, Basic 1 vCPU / 2 GB / 50 GB ($12/mo, resized 2026-11-08). Only Slot
Machine's recorder runs on it now. Osprey's and Coin Toss's code and data stay there with their services disabled.
Disk: 41 GB free on 2026-11-10, with R1 growing ~0.9–1.5 GB/day (`/health` alerts under 5 GB).

## Results
- **Bloodhound S1: STOP (2026-11-25, Ian confirmed).** The frozen model (blend-v1, `bb92f3a`) scored once on the test set
  (Nov 9: 60 events, INCONCLUSIVE) and once on the pooled test + extension (Nov 25: 71 events / 2,043 markets). Brier
  0.1568 vs the market's 0.1580: slightly better on the point estimate, but the 95% CI [−0.0035, +0.0012] includes 0, so
  no demonstrated edge. A Factbase (rollcall.com) redesign broke collection for the last 2 extension events; Ian chose to
  score with the frozen pipeline as-is (option B, recorded before scoring), so they dropped out by the rule's own
  start-time requirement. Scored after the Nov 22 time box because of that block. No money risked
  (`project-bloodhound/docs/results/score-extension-2026-11-25.md`).
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


## Timeline
| Date | Event |
|---|---|
| Oct 28 | Osprey Decision point A = STOP |
| **Nov 8** | Class: working build + test · droplet resized; recorders moved to it |
| Nov 9 | Coin Toss S2 = STOP · Bloodhound S1 frozen + test scored (inconclusive) |
| Nov 10 | Osprey shut down; Coin Toss recording stopped (both archived) |
| Nov 25 | Bloodhound pooled extension scored once → STOP (confirmed by Ian) · Slot Machine R1 maker analysis started |
| **Nov 22** | Class: iteration + story assembly · Bloodhound time box |
| **Dec 1 / Dec 4** | Class: rough cuts / final package |

## Owner to-dos (Ian)
- [ ] Fill in the "Ian's judgment: (to fill in)" lines in each project's journal and the HQ AI log.
- [ ] Slot Machine: review the R1 maker result when its session reports, confirm the verdict, then decide whether to stop the recorder (disk lasts ~2 weeks from Nov 25).
- [ ] Optional: Osprey spot-check of auto-verified pairs (the Nov 10 wrong-game find shows why it matters, but the project is done).
- [x] Bloodhound extension scored once: STOP, confirmed (2026-11-25)
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
