# alt-hq

Headquarters for Ian Downham's prediction-market research projects. Holds the shared rules and the
portfolio view; each project is its own repo, checked out next to this one.

| Project | Code name | Repo | What it does |
|---|---|---|---|
| alt-arb | **Project Osprey** | [idownham/alt-arb](https://github.com/idownham/alt-arb) | Kalshi ↔ Polymarket US cross-venue arbitrage scanner |
| alt-scalp | **Project Coin Toss** | [idownham/alt-scalp](https://github.com/idownham/alt-scalp) | Kalshi kickoff market-making (scalping) research |
| alt-btc15 | **Project Slot Machine** | [idownham/alt-btc15](https://github.com/idownham/alt-btc15) | Kalshi 15-minute BTC markets: backtest → paper → capped live |

Laptop layout:
```
~/code/alt/          ← this repo (alt-hq)
  alt-arb/           ← Osprey  (separate repo, ignored here)
  alt-scalp/         ← Coin Toss (separate repo, ignored here)
  alt-btc15/         ← Slot Machine (separate repo, ignored here)
```

- `CLAUDE.md` — shared rules every Claude Code session in these folders reads
- `PORTFOLIO.md` — status of every project, milestones, key dates, owner to-dos
- `docs/decisions.md` — decisions that span projects
