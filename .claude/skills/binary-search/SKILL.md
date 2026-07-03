---
name: binary-search
description: Use when searching a sorted array, or when a problem's answer space is monotonic (the "can this work?" check flips from false to true exactly once) — first/last occurrence, rotated sorted array search, or "minimize the maximum" / "maximize the minimum" style optimization problems.
---

# Binary Search

## When to reach for this

- Classic: find a target (or insertion point) in a sorted array.
- Find first/last index satisfying a predicate (`bisect_left`/`bisect_right` shape).
- Search in a rotated sorted array.
- **Binary search on the answer**: the problem asks to minimize/maximize some value X,
  and "is X feasible?" is a monotonic predicate over X's range — even though nothing
  looks "sorted" on the surface (e.g. minimize the max load, min days to ship packages).

## Template

```python
def binary_search(arr: list[int], target: int) -> int:
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1  # not found


def leftmost_true(lo: int, hi: int, predicate) -> int:
    """Binary search on the answer: find smallest x in [lo, hi] with predicate(x) True.
    Requires predicate to be monotonic: False...False True...True.
    """
    while lo < hi:
        mid = (lo + hi) // 2
        if predicate(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo
```

## Complexity

- Time: O(log n) per search, or O(n log(range)) when binary-searching the answer with
  an O(n) feasibility check per candidate.
- Space: O(1) iterative.

## Common pitfalls

- `mid = (lo + hi) // 2` overflow isn't a Python concern, but the off-by-one on
  `lo <= hi` vs `lo < hi`, and `mid + 1` vs `mid - 1`, is the #1 source of infinite
  loops — pick the `leftmost_true` template and adapt rather than improvising bounds.
- Forgetting to verify the predicate is actually monotonic before applying "search on
  the answer" — if it isn't, binary search silently gives a wrong answer, not an error.
- Rotated-array search: must first determine which half is sorted before deciding
  which side to recurse into.

## Example problems

_(TODO — filled in as problems land in `problems/binary_search/`)_
