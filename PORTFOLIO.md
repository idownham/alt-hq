# Portfolio

*Last updated: 2026-11-25 (all four projects finished: Bloodhound S1 = STOP; Slot Machine R1 maker test FAIL, confirmed by Ian, recorder stopped; nothing runs on the droplet). Update this file in an HQ session whenever a project changes stage or a milestone moves.*

## Status
| Project | Stage | Running where | Next milestone | Gate |
|---|---|---|---|---|
| **Osprey** (alt-arb) | **Done: STOP** (Decision A, 2026-10-28). Shut down 2026-11-10; scan log archived | Nothing (scanner, update timer and daily refresh disabled) | — (class story only) | STOP < 1 qualifying episode/week: met (0.0/week) |
| **Coin Toss** (alt-scalp) | **Done: STOP at S2** (Ian confirmed 2026-11-09, d9cb4ad): median 0 reversals in 196 clean games, ≥ 3 needed. Recording stopped 2026-11-10 | Nothing (server units disabled, laptop agent unloaded) | — (class story only) | Pre-registered S2 gate failed |
| **Bloodhound** (alt-edge) | **Done: STOP at S1** (Ian confirmed 2026-11-25, e4b65be). Pooled test + extension (71 events / 2,043 markets): Brier 0.1568 vs market 0.1580, CI [−0.0035, +0.0012], still includes 0 → STOP by the pre-registered rule | Nothing | — (class story only) | Pooled 95% upper bound < 0 needed: not met |
| **Slot Machine** (alt-btc15) | **Done: R1 maker test FAIL** (Ian confirmed 2026-11-25, 28c6402). M1 chosen on train lost on test; M2 not testable. Recorder stopped and disabled 2026-11-25 14:35 UTC; data kept | Nothing (unit disabled; DB stays in `/opt/alt-btc15/data`) | — (class story only) | Capped test net > 0 and 95% CI > 0: not met |

**Shared server:** DigitalOcean droplet `alt-arb`, Basic 1 vCPU / 2 GB / 50 GB ($12/mo, resized 2026-11-08). **Nothing runs on
it since 2026-11-25 14:35 UTC.** Every project's code and data stay there with its services disabled (20 GB free).
Keeping or destroying the droplet ($12/mo) is an open owner decision.

## Results
- **Slot Machine R1 maker test: FAIL (2026-11-25, Ian confirmed).** 910 usable windows (Oct 14 – Nov 10, after a
  pre-committed whole-day extension, `5a0434a`); 606 train / 304 test; selection committed before the test (`0f412ec`).
  M1 (`margin=3c join`) on test: capped −$65.12 over 93 windows, mean −$0.70/window (95% CI −$1.79 to +$0.39); uncapped
  −$143.02 over 304 (spread earned +$227.66, adverse selection −$370.69). M2 pair capture not testable (no variant reached
  50 traded windows; the spread was nearly always 1¢). Paper only, no orders (`project-slot-machine/docs/r1-results.md`).
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
| Nov 25 | Bloodhound pooled extension scored once → STOP · Slot Machine R1 maker test → FAIL · recorder stopped (both confirmed by Ian) |
| **Nov 22** | Class: iteration + story assembly · Bloodhound time box |
| **Dec 1 / Dec 4** | Class: rough cuts / final package |

## Owner to-dos (Ian)
- [ ] Fill in the "Ian's judgment: (to fill in)" lines in each project's journal and the HQ AI log.
- [ ] Decide whether to keep the droplet ($12/mo, nothing running) or snapshot/destroy it after the class (Dec 4).
- [x] Slot Machine R1 maker test: FAIL confirmed; recorder stopped and disabled (2026-11-25)
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
