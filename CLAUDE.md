# CLAUDE.md

This file provides guidance to Claude Code when working with code in this repository.

## About this project

A compendium of what I'm learning while preparing for coding interview screenings —
coding concepts, architecture, and competitive programming. Problems are solved in
Python. The goal is a growing, personal mental model, not a one-off problem set.

## Tools

- Python 3
- pytest

## Structure

- `.claude/skills/<pattern>/SKILL.md` — actionable, Claude-invokable playbooks for
  algorithmic patterns (two-pointers, sliding-window, BFS/DFS, DP, ...). Each one is a
  real Claude Code Skill: a trigger description plus a template, complexity notes, and
  common pitfalls for that pattern.
- `.claude/skills/hackerrank-solving/SKILL.md` — a workflow skill (not a pattern
  playbook) capturing how to reliably drive HackerRank's own browser code editor via
  claude-in-chrome: editor focus quirks, indentation pitfalls, and the fetch → local
  solve/test → reproduce-in-browser → submit → verify → checklist workflow used for
  `problems/hackerrank/python/`.
- `problems/<pattern>/` — solved problems, one solution file + one `test_*.py` per
  problem, organized under the same pattern names as `.claude/skills/` so the two stay
  mapped 1:1. This is the "reps" — proof the pattern was actually applied.
- `problems/hackerrank/python/` — working through HackerRank's own Python domain badge
  track problem by problem (see its `README.md`); a separate track from the curated
  pattern practice above, useful when a specific HackerRank challenge doesn't map
  cleanly onto one pattern.
- `notes/` — everything that isn't a reusable "invoke this while coding" playbook:
  a complexity cheatsheet, architecture/system-design learnings, and competitive
  programming topics that don't map to an interview pattern 1:1 (may later graduate
  into their own skill).

## Conventions

- Type hints on function signatures; docstrings only when the *why* isn't obvious from
  the code (a non-obvious invariant, a tricky edge case) — not to restate the signature.
- Every solved problem gets a matching `test_*.py` using pytest. Run the whole suite
  with `pytest` from the repo root.
- File naming: snake_case matching the problem's name/slug (e.g. `valid_palindrome.py`,
  `test_valid_palindrome.py`), placed under `problems/<pattern>/`.
- Before solving a new problem, check whether an existing skill in `.claude/skills/`
  already covers the pattern. If a genuinely new pattern shows up, propose a new skill
  rather than solving it ad hoc.

## How skills are used here

`.claude/skills/*/SKILL.md` are real Claude Code Skills — Claude should invoke them
proactively (via the Skill tool) when a problem's shape matches a skill's trigger
description, not just read them passively for reference. Applying the skill's template
live is part of how the pattern gets learned.

## Growing this compendium

Add a new skill only once its pattern has shown up in at least one real solved problem
under `problems/` — this keeps the compendium grounded in actual practice instead of
becoming a pre-built encyclopedia of patterns never exercised.
