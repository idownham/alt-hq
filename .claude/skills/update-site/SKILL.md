---
name: update-site
description: Refresh Ian's plain-English "Alt Projects Briefing" website (docs/site/index.html → private artifact) from the latest state of every project. Use in every HQ chat before the wrap-up commit, and whenever Ian says "update the site" or similar.
---

# /update-site — refresh the Alt Projects Briefing

HQ sessions only (`~/code/alt/`). Reading other projects' files is fine; **never edit** them.

- Source: `docs/site/index.html`
- Published at: https://claude.ai/artifact/XwdudFFr5dSPQYsat1kzHS (private; Ian decides sharing)
- Audience: Ian, reading as a non-technical person. Plain words, short sentences, analogies over jargon. Any term
  the page uses must be in its "Plain-English terms" list.

## 1. Gather (read-only)
For each project folder (`project-osprey`, `project-coin-toss`, `project-slot-machine`, `project-bloodhound`):
- `git log --oneline -8` (what changed since the page's "Last updated" time)
- the stage/plan doc (`docs/plan.md` or `docs/spec.md`), the newest entries in `docs/decisions.md` and `docs/journal.md`,
  and any results doc (e.g. `docs/s1-results.md`)
- live status where there is a command: `project-osprey/.venv/bin/python -m altarb.status`,
  `project-coin-toss/.venv/bin/altscalp status`; Slot Machine freshness as in the `/health` skill
Also HQ: `PORTFOLIO.md`, `docs/decisions.md`, `docs/journal.md` (AI log, capture index), `docs/class/`.
If `/health` already ran this session, reuse its board, and say what time it's from.

## 2. Update the page
Keep the structure and design. Update only what changed:
- header "Last updated" (CT date and time)
- **Is everything running?** rows and pills (good / warn / bad / idle)
- each project dossier: stage track (`done` / `now`), what's happening, progress counts, early signals, next step, gate
- **What's waiting on you**: from PORTFOLIO owner to-dos + open items; remove done ones; `urgent` for time-sensitive
- **Calendar**: move the `today` row; drop past dates older than ~1 week
- **What changed recently**: add a dated block at the top (keep ~3–4 blocks; drop the oldest)
- a new stage, project or result → also add or adjust its dossier

## 3. Accuracy rules (class evidence — these matter)
- Every number and claim must come from a file or command you read **this session**. Don't invent or round up.
- Early signals keep the label "not a conclusion". Never make a result look more complete or profitable than it is.
- Pre-registered pass/fail bars are copied from the project's own spec, never reworded into something easier.
- Nothing from `.env`, no keys, no account details or balances.

## 4. Publish and record
- Publish with the Artifact tool. **From a new chat, pass `url` = the URL above** (read it first with
  `action: "read"`), or you'll create a duplicate. Within the same chat, re-publish the same file path. Don't pass `icon`.
- Commit `docs/site/index.html` with the HQ wrap-up (or alone: "Status site: refresh <date>"), then push.
- Tell Ian in one line what changed on the page, with the link.
