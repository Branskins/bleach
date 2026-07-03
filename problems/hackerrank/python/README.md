# HackerRank — Python domain

Tracks progress through HackerRank's [Python domain](https://www.hackerrank.com/domains/python)
(`badge_type=python`), scraped directly from the user's logged-in account via browser
automation on 2026-07-03. This is a separate track from `problems/<pattern>/`:

- `problems/<pattern>/` — curated interview-pattern practice, one skill per pattern.
- `problems/hackerrank/python/` — working through HackerRank's own Python badge track,
  problem by problem, roughly in their recommended order.

## Files

- `unsolved.md` — full list of challenges not yet solved on the account, in HackerRank's
  page order (which follows their subdomain progression: Introduction → Basic Data Types
  → Strings → Sets → Math → Itertools → Collections → Date and Time → Errors and
  Exceptions → Classes → Built-Ins → Python Functionals → Regex and Parsing → XML →
  Closures and Decorators → Numpy → Debugging).

## Workflow

When a challenge is solved:
1. Add `<slug>.py` here with the solution (HackerRank's I/O format — usually reading from
   stdin / printing to stdout — so it won't always look like a typical `problems/<pattern>/`
   function-style solution).
2. Check it off in `unsolved.md`.
3. If the challenge exercises a pattern already covered by a skill in `.claude/skills/`,
   note that connection; if it's a genuinely new pattern worth generalizing, consider
   promoting it to a new skill per the "growing this compendium" rule in the root
   `CLAUDE.md`.

This list can drift from the live site as problems get solved directly on HackerRank
outside this workflow — re-scrape periodically if it gets stale.
