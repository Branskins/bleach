---
name: hackerrank-solving
description: Use whenever solving HackerRank challenges tracked in this project's problems/hackerrank/python/ (e.g. the user says "let's continue", "next problem", "solve #N", or asks to work through the HackerRank unsolved list), or any time claude-in-chrome is driving HackerRank's own code editor at hackerrank.com/challenges/*/problem. Covers the reliable browser-interaction pattern for HackerRank's CodeMirror-based editor (focus quirks, indentation pitfalls, submission verification) and the full solve-to-submit workflow used in this project. Consult this before typing code into HackerRank's editor even if the task seems simple — the editor has non-obvious failure modes that silently produce wrong or unsubmitted code.
---

# Solving HackerRank challenges

## Workflow (per problem)

1. Navigate to the challenge (`https://www.hackerrank.com/challenges/<slug>/problem`) and read the problem with `get_page_text`, not a screenshot — text extraction is far cheaper than repeated screenshots and captures the input/output spec verbatim. If numbers/ranges look stripped from the extracted text (rendered as math spans, common on constraint lines), take one screenshot to confirm the exact figures before coding — don't guess at bounds.
2. Write the solution locally first: `problems/hackerrank/python/<slug>.py` (a small pure function plus an `if __name__ == "__main__":` block doing the actual stdin/stdout wiring) and `problems/hackerrank/python/test_<slug>.py`. Run `pytest problems/hackerrank/python/test_<slug>.py -q` before touching the browser — this catches logic bugs for free, without spending a HackerRank submission attempt on a bug that pytest would have caught instantly.
3. Reproduce the verified logic in HackerRank's browser editor (see editor-interaction rules below).
4. Click **Run Code** first and confirm the sample test cases pass via `get_page_text` (look for "Congratulations! You have passed the sample test cases"). Only click **Submit Code** once samples pass — submitting broken code wastes the interaction and muddies the point tally.
5. After Submit Code, always re-read the page with `get_page_text` before believing it worked — see "Verifying success" below.
6. Update `problems/hackerrank/python/unsolved.md`: flip `[ ]` to `[x]` for that row, only after step 5 confirms the points actually landed.

## Editor interaction rules (HackerRank's CodeMirror instance)

These were learned the hard way across a 12-problem session — skipping any of them silently produces broken or unsubmitted code.

- **The editor needs a double-click to focus.** The first `left_click` on a code line often lands visually but doesn't give the editor real keyboard focus — the next `type`/`key` action is silently swallowed and the code stays unchanged. Click the target line twice before sending `End`/`Return`/`type`. Verify with a screenshot after typing rather than trusting the action reported success — a click landing outside the true text-input hitbox produces no error, just no effect.
- **`\n` inside a `type` string does not reliably produce a newline in this editor.** Typing `"line one\nline two"` in one call can leave the editor showing only the first line, unchanged. Use explicit `key: "Return"` presses between lines instead of embedding `\n` in the typed string.
- **Auto-indent is inconsistent and cannot be trusted blindly.** Sometimes pressing Return after a line ending in `:` bumps the next line's indent by one level as expected; other times a Return after a *non-colon* line still fails to preserve the previous line's indent. Relying on it produced a real `IndentationError: expected an indented block after 'for' statement` mid-session. Two ways to stay safe:
  - **Prefer single-line compound statements** (`if op == "insert": lst.insert(...)`, `elif op == "print": print(lst)`, `for i in range(n): print(i, end="")`) over multi-line blocks whenever the body is one statement — this sidesteps the indent question entirely since there's no nested line to get wrong.
  - When a real nested block is unavoidable, **don't trust the auto-indent** — after typing, screenshot and check every line's leading whitespace matches its intended nesting level. Fix a misindented line by clicking it, pressing `Home` (goes to the first non-whitespace character), and typing/deleting spaces directly. Avoid Backspace-based dedent on an empty auto-indented line — it has been observed to delete into the *previous* line's actual content instead of just the leading whitespace, corrupting a working line. Always screenshot-check after any indent fix.
- **Long logical lines soft-wrap across 2-3 visual rows** — this is cosmetic only; don't mistake a wrapped single statement (e.g. a long list comprehension) for multiple lines when reading a screenshot.
- **The language dropdown sometimes defaults to "Pypy 3"** on a fresh problem load — switch it to "Python 3" before typing, since the starter stub and this project's conventions assume CPython/Python 3 semantics.

## Verifying success

Never assume a click on Submit Code worked — confirm every time:
- Re-read the page with `get_page_text` after a `wait` of 2-3 seconds.
- Look for `"Your <Challenge Name> submission got N.NN points!"` and a higher `Points: X/Y` tally than before submitting.
- If the points total is unchanged and the editor still shows an editable (not "Congratulations") state, the click didn't register. Common causes: an interrupted/rejected prior tool call left the actual click un-executed, or a `navigate` call reset scroll position so a coordinate-based click landed on the wrong element after the page re-flowed. Re-locate the button with `find` (query: "Submit Code button") and click by `ref` rather than raw coordinates — refs survive layout shifts that coordinates don't.

## Cost/context management

- Prefer `get_page_text` over `screenshot` for reading problem statements and submission results — it costs a fraction of the tokens.
- Reserve screenshots for moments that need visual confirmation: checking the editor's actual text content after typing, and locating click targets right after a fresh page load or scroll.
- Batch sequential browser actions (click, key, type, screenshot) into one `browser_batch` call rather than one tool call each — this cuts round-trips substantially over a multi-problem session.
- This work is genuinely token-heavy. Pace it in batches of roughly 5-10 problems per session rather than trying to clear the whole `unsolved.md` list at once — context usage from browser-automation tool output climbs fast, well before real problem-solving difficulty becomes the limiting factor.
