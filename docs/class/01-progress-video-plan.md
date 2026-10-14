# Checkpoint 1 progress video — plan (1–2 min, record and date it 2026-10-14 or later)

**Rules from the brief:** real starting evidence, simple and unfinished is fine, say what you'll test next.
**No AI-generated montage.** Never show `.env`, keys, Kalshi/Polymarket account screens, or the droplet IP.
Say the real recording date on camera, or show it in a title card.

| # | Time | Shot (all real screen recordings) | Narration (Ian, ~200 words total, edit freely) |
|---|---|---|---|
| 1 | 0:00–0:12 | You at the laptop, or a title card: "Is there free money in prediction markets? — Ian Downham, recorded Oct 14, 2026" | "I'm Ian, and I'm building systems to test whether there's real money to be made on prediction markets, or whether that's an illusion." |
| 2 | 0:12–0:30 | Kalshi and Polymarket US market pages for the same game, side by side (logged-out public pages) | "The same game is priced on two regulated exchanges. When the prices disagree, buying both sides should lock in a profit. That's the idea behind Project Osprey." |
| 3 | 0:30–0:50 | Terminal: `/health` board, then `python -m altarb.status`, the scanner running on the cloud server | "I built the scanner on October 10. Since the 13th it's run 24/7 on a cloud server, checking about 240 market pairs every four minutes and logging every gap after fees." |
| 4 | 0:50–1:10 | `docs/plan.md` scrolled to the "Decision point A criteria" | "Before looking at any clean data, I wrote down what counts as success: at least five real pre-game gaps a week to go ahead, and fewer than one a week means I stop." |
| 5 | 1:10–1:30 | Coin Toss: `altscalp status` table, plus Slot Machine `docs/s1-results.md` headline | "I'm also testing two other ideas. One already failed its test. None of my Bitcoin strategies made money in an out-of-sample test, so I stopped before risking a dollar." |
| 6 | 1:30–1:50 | Coin Toss recorder log during tonight's 18:00 window (if you film then) | "Next: Coin Toss records its first test games this week, and counted games from October 17, to see whether the price noise at kickoff is tradable. Osprey gets its verdict around October 27." |

**Before recording:** close other windows and tabs, and check that no terminal
scrollback shows `.env` or keys.
**After recording:** add it to the capture index in `docs/journal.md` (date, file, what it shows, sizzle-worthy?).
Candidate sizzle moment: shot 5's "stopped before risking a dollar".
