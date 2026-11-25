# Working Build and Test

Ian Downham · Founder Documentary, Fall 2026 · Checkpoint 3 (due Nov 8, submitted late on Nov 25)

This covers my work from Oct 26 to Nov 8, when I had three systems collecting data around the clock. Osprey's scanner had been running on a cloud server since Oct 13, Coin Toss had recorded 365 game windows since Oct 17, and Slot Machine was saving the Bitcoin order book every second. Bloodhound was waiting for a project to free up. Each repo has a README with setup steps, and my video shows the Osprey report and Coin Toss status check running.

My main test in this stretch was Osprey's Decision A. The scanner compared the same games on Kalshi and Polymarket every 4 minutes across 8 leagues. On Oct 13, before I had any clean data, I wrote down the rules. GO at 5 or more real gaps a week, meaning before the game, lasting two scans, and worth $20 or more. STOP under 1 a week.

On Oct 28, after 15.2 days and 813,062 pair checks, 1,040 gaps had shown up, but 1,032 were during games. Only 8 were before a game and the biggest was $2.33. None qualified, so I called STOP and didn't build paper trading. The test has limits. Scanning every 4 minutes misses short gaps, and some scans failed or dropped off late in October. Those could only hide gaps, not create them.

The biggest change came from my laptop. It kept going to sleep and losing data. 168 of Coin Toss's 365 windows weren't clean, and Slot Machine was losing 3 to 20 hours a day since Oct 31. On Nov 8 I upgraded the cloud server to 2 GB and 50 GB for $12 a month and moved both recorders onto it. Each project got its own space, read-only with no keys.

Claude Code ran the report and dug into the gaps, but I made the STOP call and didn't change the rules after seeing data. I also had Claude do the server move, and I picked the $12 plan over the $18 one.

From here, Coin Toss needs its noise analysis on the clean games (I ran it Nov 9 and it was a STOP). Slot Machine keeps recording, then runs the maker test I locked Oct 14. Bloodhound gets built, frozen, and scored once. Each project's final test is its pre-registered verdict. For the story, I'll screen record each verdict and have rough cuts ready by Dec 1.

Evidence: [Decision A rules](https://github.com/idownham/alt-arb/commit/8944d1a), [Decision A results](https://github.com/idownham/alt-arb/commit/ae52199), [Coin Toss recordings](https://github.com/idownham/alt-scalp/commit/014c442), [server move](https://github.com/idownham/alt-hq/commit/c620841). My journal, AI log and capture index are in docs/journal.md in the alt-hq repo.
