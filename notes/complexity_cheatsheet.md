# Complexity Cheatsheet

Running reference for common operation complexities. Add to this as gaps come up.

## Python built-in operations

| Structure | Operation | Time |
|---|---|---|
| `list` | index / append / pop (end) | O(1) |
| `list` | insert / pop / delete (arbitrary index) | O(n) |
| `list` | `in` (membership) | O(n) |
| `list` | `sorted()` / `.sort()` | O(n log n) |
| `dict` / `set` | get / set / `in` | O(1) average |
| `collections.deque` | append / pop (either end) | O(1) |
| `heapq` | push / pop | O(log n) |
| `heapq.heapify` | build from list | O(n) |

## Common algorithm complexity targets

| Input size (n) | Acceptable complexity |
|---|---|
| n ≤ ~10 | O(n!) / O(2^n) brute force may be intended |
| n ≤ ~1,000 | O(n^2) |
| n ≤ ~100,000 | O(n log n) |
| n ≤ ~10,000,000 | O(n) |
| n huge / streaming | O(log n) or O(1) amortized |

Use the input-size constraint given in a problem to sanity-check which pattern is
expected before committing to an approach.
