---
name: dynamic-programming
description: Use when a problem has overlapping subproblems and optimal substructure — counting ways, min/max cost, or feasibility over sequences, grids, or partitions — recognizable when a brute-force recursion recomputes the same state repeatedly.
---

# Dynamic Programming

## When to reach for this

- The problem asks for a count, min/max, or yes/no over choices made across a sequence,
  grid, or set — and a greedy choice provably doesn't work.
- A brute-force recursive solution exists but is exponential because it revisits the
  same `(state)` many times — that repetition is the signal.
- Recognize the shape: 1D (sequence — climbing stairs, house robber), 2D (two sequences —
  edit distance, LCS; or grid — unique paths), or knapsack-style (subset/partition).

## Approach

1. Write the brute-force recursion first: define `solve(state) -> answer`, identify the
   base case(s) and the recurrence relating `solve(state)` to smaller states.
2. Identify what `state` actually needs to be (often fewer dimensions than it first
   appears — e.g. "remaining capacity" instead of "which items used").
3. Memoize the recursion (top-down) to confirm correctness cheaply.
4. Convert to bottom-up iteration only if needed (recursion depth, performance).

## Template

```python
from functools import cache


def solve_top_down(n: int) -> int:
    @cache
    def rec(i: int) -> int:
        if i <= 1:  # base case
            return i
        return rec(i - 1) + rec(i - 2)  # recurrence
    return rec(n)


def solve_bottom_up(n: int) -> int:
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
```

## Complexity

- Time: O(number of distinct states × transition cost).
- Space: O(number of distinct states), often reducible to O(1) or O(min dimension) by
  only keeping the last row/few values (rolling array).

## Common pitfalls

- Confusing "greedy would also work here" with DP — verify optimal substructure before
  assuming greedy is wrong (or right).
- Off-by-one in base cases / array sizing (`dp` of size `n+1` vs `n`).
- Not reducing the state space after getting a correct-but-slow recursion — interview
  follow-ups often want the space-optimized version.
- `@cache` on a method with mutable default args or on functions closing over mutable
  state can silently produce wrong cached results — keep the memoized function pure.

## Example problems

_(TODO — filled in as problems land in `problems/dynamic_programming/`)_
