# Working Build and Test (Checkpoint 3)

**Ian Downham** · solo project · Founder Documentary, Fall 2026 · Checkpoint 3 (due Nov 8)

**Submitted late, on Nov 25.** This covers work from Oct 26 to Nov 8. Nothing is backdated, and anything that happened after Nov 8 is marked.

## Where the build stands
By Nov 8 I had three systems collecting data around the clock. Osprey's scanner had been running on a cloud server since Oct 13. Coin Toss had recorded 365 game windows since Oct 17. Slot Machine was saving the Bitcoin order book every second. Bloodhound had its research done and was waiting for a project to free up.

**How to see it run:** each repo's README has setup steps. Osprey's `python -m altarb.report` checks the scan log against my rules, and Coin Toss's `altscalp status` lists every recorded game. The video shows both.

## The test: Osprey Decision A
**Setup:** the scanner checked the same games on Kalshi and Polymarket about every 4 minutes across 8 leagues, logging any gap after fees.
**Success criteria (written Oct 13, before any clean data):** GO at 5 or more real gaps a week (before the game, lasting 2+ scans, $20+ profit). STOP under 1 a week.
**Results (Oct 28):** 15.2 days and 813,062 pair checks. 1,040 gaps showed up, but 1,032 were during games. Only 8 were before a game, and the biggest was $2.33. Zero qualified, so I called STOP and didn't build paper trading.
**Limitations:** 4-minute scans miss short gaps, an hour of scans failed Oct 22, and coverage dropped after Oct 25. These could only hide gaps, not create them.

## Iteration decision: moving off my laptop
My laptop kept sleeping and losing data. 168 of Coin Toss's 365 windows weren't clean, and Slot Machine was losing 3 to 20 hours a day since Oct 31. On Nov 8 I upgraded the cloud server to 2 GB and 50 GB for $12 a month and moved both recorders onto it. Each project got its own user and folder, read-only with no keys.

## AI use and my judgment
Claude Code ran the Decision A report and dug into the gaps. I made the STOP call without touching the rules. I had Claude do the server move and catch up the journals, and I picked the $12 plan over the $18 one.

## Finish plan (as of Nov 8)
- Coin Toss: run the noise analysis on the clean games (ran Nov 9: STOP).
- Slot Machine: keep recording, then run the maker test locked Oct 14.
- Bloodhound: build the model, freeze it, score it once.
- Final test: each project's pre-registered verdict.
- Story: screen record each verdict, outline both films, rough cuts Dec 1.

---

## Evidence links (dated)
| Date | Project | What it shows | Link |
|---|---|---|---|
| Oct 13 | Osprey | Pass/fail rules written before any clean data | [8944d1a](https://github.com/idownham/alt-arb/commit/8944d1a) |
| Oct 28 | Osprey | Decision A report and STOP | [ae52199](https://github.com/idownham/alt-arb/commit/ae52199) |
| Oct 14 | Slot Machine | Maker test rules locked before any data | [8f98e28](https://github.com/idownham/alt-btc15/commit/8f98e28) |
| Nov 8 | Coin Toss | 365 windows recorded, 168 not clean, recorder moved to server | [014c442](https://github.com/idownham/alt-scalp/commit/014c442) |
| Nov 8 | Slot Machine | Recorder set up and cut over to the server | [918700b](https://github.com/idownham/alt-btc15/commit/918700b), [ad784c8](https://github.com/idownham/alt-btc15/commit/ad784c8) |
| Nov 8 | Osprey | Server upgraded and checked after reboot | [6ed9370](https://github.com/idownham/alt-arb/commit/6ed9370) |
| Nov 8 | HQ | Server decision, journal and portfolio caught up | [c620841](https://github.com/idownham/alt-hq/commit/c620841) |

Shared journal, source index, AI log and capture index: `docs/journal.md` in the alt-hq repository. Code and project journals: alt-arb (Osprey), alt-scalp (Coin Toss), alt-btc15 (Slot Machine), alt-edge (Bloodhound).
