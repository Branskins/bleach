---
name: two-pointers
description: Use when solving a problem over a sorted array/string, a palindrome check, pair-sum, merging two sorted sequences, or partitioning in place — anywhere two indices can move toward or away from each other to avoid an O(n^2) nested loop.
---

# Two Pointers

## When to reach for this

- The input is sorted (or can be sorted without losing needed info).
- You're looking for a pair/triplet meeting a sum/difference condition.
- You're comparing from both ends inward (palindrome, reverse-in-place).
- You're merging or intersecting two sorted sequences.
- You're partitioning an array in place (e.g. move zeroes, Dutch national flag).

If the naive solution is a nested loop scanning all pairs, ask first whether sorting +
two pointers collapses it to O(n) or O(n log n).

## Template

```python
def two_pointer_converging(arr: list[int], target: int) -> tuple[int, int] | None:
    left, right = 0, len(arr) - 1
    while left < right:
        current = arr[left] + arr[right]
        if current == target:
            return left, right
        if current < target:
            left += 1
        else:
            right -= 1
    return None


def two_pointer_same_direction(arr: list[int]) -> int:
    """Fast/slow pointers, e.g. removing duplicates in place."""
    slow = 0
    for fast in range(len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]
    return slow + 1
```

## Complexity

- Time: O(n) or O(n log n) if a sort is required first.
- Space: O(1) beyond the input.

## Common pitfalls

- Forgetting the array must be sorted for the converging-pointer sum trick to work.
- Off-by-one on the `while left < right` vs `<=` boundary — decide based on whether
  `left == right` is a valid pair (usually not).
- Not skipping duplicate values when the problem asks for unique pairs/triplets.

## Example problems

_(TODO — filled in as problems land in `problems/two_pointers/`)_
