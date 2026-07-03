---
name: heaps-priority-queue
description: Use when a problem needs repeated access to the min/max of a changing collection — top-k elements, k-way merge, running median, task scheduling by priority, or Dijkstra-style shortest path — where sorting once isn't enough because elements are added/removed over time.
---

# Heaps / Priority Queue

## When to reach for this

- "Top k" / "k closest" / "k-th largest" — a heap of size k beats sorting everything.
- Merging k sorted lists/streams.
- Running median or any streaming statistic needing quick min/max access as data arrives.
- Greedy scheduling by priority (meeting rooms, task scheduler, Huffman coding).
- Weighted shortest-path (Dijkstra) — a min-heap keyed by current best distance.

## Template

```python
import heapq


def top_k_largest(nums: list[int], k: int) -> list[int]:
    """Min-heap of size k: keeps the k largest seen so far."""
    heap: list[int] = []
    for n in nums:
        heapq.heappush(heap, n)
        if len(heap) > k:
            heapq.heappop(heap)
    return heap


def k_way_merge(lists: list[list[int]]) -> list[int]:
    heap = [(lst[0], i, 0) for i, lst in enumerate(lists) if lst]
    heapq.heapify(heap)
    result = []
    while heap:
        val, list_idx, elem_idx = heapq.heappop(heap)
        result.append(val)
        if elem_idx + 1 < len(lists[list_idx]):
            heapq.heappush(
                heap, (lists[list_idx][elem_idx + 1], list_idx, elem_idx + 1)
            )
    return result
```

`heapq` is min-heap only — for a max-heap, push negated values (or `(-priority, item)`
tuples), and remember to negate back on pop.

## Complexity

- Push/pop: O(log n). Building a heap from a list via `heapify`: O(n).
- Top-k with a size-k heap: O(n log k), better than an O(n log n) full sort when k << n.

## Common pitfalls

- Forgetting `heapq` is min-heap-only and getting max-heap logic backwards.
- Comparing tuples where the second element isn't comparable (e.g. custom objects) —
  `heapq` falls back to comparing the second tuple element on ties, which errors or
  gives wrong order. Include a unique tiebreaker (index) in the tuple.
- Using a heap when a simple sort would do — if the collection isn't changing and you
  only need the top-k once, `sorted()` / `heapq.nlargest` is simpler and often fast enough.

## Example problems

_(TODO — filled in as problems land in `problems/heaps_priority_queue/`)_
