---
name: backtracking
description: Use when a problem asks to enumerate all valid combinations/permutations/subsets, or find one that satisfies constraints (N-Queens, Sudoku, subsets, permutations, combination sum, word search) — build a candidate incrementally and undo the last choice when it fails.
---

# Backtracking

## When to reach for this

- The problem says "find all ..." / "generate all ..." combinations, permutations,
  subsets, or partitions.
- Constraint satisfaction where a partial candidate can be pruned early (N-Queens,
  Sudoku, word search on a grid) rather than generating every full candidate blindly.
- Distinguish from plain DFS: backtracking explicitly *builds and un-builds* a shared
  candidate/path, rather than just visiting nodes.

## Template

```python
def backtrack(candidates: list[int]) -> list[list[int]]:
    results: list[list[int]] = []
    path: list[int] = []

    def rec(start: int) -> None:
        if is_complete(path):          # base case
            results.append(path.copy())  # copy — path mutates after this
            return
        for i in range(start, len(candidates)):
            if not is_valid_choice(candidates[i], path):
                continue
            path.append(candidates[i])   # choose
            rec(i + 1)                   # explore
            path.pop()                   # un-choose

    rec(0)
    return results


def is_complete(path: list[int]) -> bool:
    raise NotImplementedError


def is_valid_choice(candidate, path: list[int]) -> bool:
    raise NotImplementedError
```

## Complexity

- Time: worst case exponential (O(2^n) for subsets, O(n!) for permutations) — pruning
  invalid branches early is what keeps it tractable in practice, not asymptotics.
- Space: O(depth) for the recursion stack + path, plus O(results) for the output.

## Common pitfalls

- Appending `path` directly instead of `path.copy()` — the list keeps mutating after
  it's stored, corrupting every previously-saved result.
- Forgetting the `pop()` (undo step) — without it, sibling branches see stale state.
- Not skipping duplicate choices at the same recursion level when the input has
  duplicates and the problem wants unique results (sort first, then `if i > start and
  candidates[i] == candidates[i-1]: continue`).
- Pruning too late — check validity *before* recursing into a branch, not after
  completing it, or the exponential blowup isn't actually avoided.

## Example problems

_(TODO — filled in as problems land in `problems/backtracking/`)_
