# alt-hq

Headquarters for Ian Downham's prediction-market research projects. Holds the shared rules and the
portfolio view; each project is its own repo, checked out inside this folder under its code name.
Local folders are named by code name; GitHub repo names are unchanged.

| Folder | Code name | Repo | What it does |
|---|---|---|---|
| `project-osprey/` | **Project Osprey** | [idownham/alt-arb](https://github.com/idownham/alt-arb) | Kalshi ↔ Polymarket US cross-venue arbitrage scanner |
| `project-coin-toss/` | **Project Coin Toss** | [idownham/alt-scalp](https://github.com/idownham/alt-scalp) | Kalshi kickoff market-making (scalping) research |
| `project-bloodhound/` | **Project Bloodhound** | [idownham/alt-edge](https://github.com/idownham/alt-edge) | Find underpriced markets by doing the homework — starting with mention markets (planned) |
| `project-slot-machine/` | **Project Slot Machine** | [idownham/alt-btc15](https://github.com/idownham/alt-btc15) | Kalshi 15-minute BTC markets: backtest → paper → capped live |

Laptop layout:
```
~/code/alt/                 ← this repo (alt-hq)
  project-osprey/           ← Osprey       (repo alt-arb,   separate, ignored here)
  project-coin-toss/        ← Coin Toss    (repo alt-scalp, separate, ignored here)
  project-slot-machine/     ← Slot Machine (repo alt-btc15, separate, ignored here)
  project-bloodhound/       ← Bloodhound   (repo alt-edge,  separate, ignored here; planned)
```

- `CLAUDE.md` — shared rules every Claude Code session in these folders reads
- `PORTFOLIO.md` — status of every project, milestones, key dates, owner to-dos
- `docs/decisions.md` — decisions that span projects
