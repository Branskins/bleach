---
name: sliding-window
description: Use for problems about a contiguous subarray/substring that must satisfy a size, sum, or uniqueness condition — longest/shortest/count of substrings or subarrays meeting a constraint, without recomputing the whole window from scratch each step.
---

# Sliding Window

## When to reach for this

- The problem asks for the longest/shortest/count of a *contiguous* subarray or
  substring satisfying some condition (sum ≤ k, at most k distinct chars, no repeats...).
- A brute force would re-scan overlapping ranges — the window can instead grow/shrink
  incrementally, updating a running aggregate (sum, count map, distinct-count) in O(1)
  per step instead of recomputing it.
- Fixed-size window variant: exactly-k-length subarray metrics (max sum of size k, etc.)

## Template

```python
def longest_window_satisfying(s: str) -> int:
    """Variable-size window: expand right, shrink left while invalid."""
    left = 0
    best = 0
    window: dict[str, int] = {}
    for right, ch in enumerate(s):
        window[ch] = window.get(ch, 0) + 1
        while window_is_invalid(window):
            window[s[left]] -= 1
            if window[s[left]] == 0:
                del window[s[left]]
            left += 1
        best = max(best, right - left + 1)
    return best


def fixed_window_max_sum(arr: list[int], k: int) -> int:
    window_sum = sum(arr[:k])
    best = window_sum
    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]
        best = max(best, window_sum)
    return best


def window_is_invalid(window: dict[str, int]) -> bool:
    raise NotImplementedError  # problem-specific condition
```

## Complexity

- Time: O(n) — each index enters and leaves the window at most once.
- Space: O(k) or O(alphabet size) for the window's aggregate structure.

## Common pitfalls

- Shrinking with `if` instead of `while` — a single shrink step isn't always enough to
  restore validity.
- Forgetting to update `best` *after* shrinking, or measuring window size before the
  shrink loop has settled.
- Conflating "at most k" with "exactly k" — "exactly k" is often easier as
  `atMost(k) - atMost(k-1)`.

## Example problems

_(TODO — filled in as problems land in `problems/sliding_window/`)_
