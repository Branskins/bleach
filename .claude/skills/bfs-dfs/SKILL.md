---
name: bfs-dfs
description: Use for traversal or reachability problems on grids, trees, or graphs — shortest path in unweighted graphs (BFS), connected components/islands, cycle detection, or exhaustive exploration of all paths (DFS). Covers both explicit graphs and implicit ones (grids, state spaces).
---

# BFS / DFS

## When to reach for this

- **BFS**: shortest path / fewest steps in an *unweighted* graph or grid, level-order
  traversal, "minimum number of X to reach Y".
- **DFS**: connected components, cycle detection, topological ordering (with care),
  exhaustive path exploration, flood fill.
- The graph is often implicit: a grid (4/8-directional neighbors), a word-ladder style
  state space, or a tree.

## Template

```python
from collections import deque


def bfs_shortest_path(start, is_goal, neighbors) -> int:
    queue = deque([(start, 0)])
    visited = {start}
    while queue:
        node, dist = queue.popleft()
        if is_goal(node):
            return dist
        for nxt in neighbors(node):
            if nxt not in visited:
                visited.add(nxt)
                queue.append((nxt, dist + 1))
    return -1  # unreachable


def dfs_iterative(start, neighbors) -> set:
    visited = {start}
    stack = [start]
    while stack:
        node = stack.pop()
        for nxt in neighbors(node):
            if nxt not in visited:
                visited.add(nxt)
                stack.append(nxt)
    return visited


def dfs_recursive(node, neighbors, visited: set) -> None:
    visited.add(node)
    for nxt in neighbors(node):
        if nxt not in visited:
            dfs_recursive(nxt, neighbors, visited)
```

## Complexity

- Time: O(V + E) for explicit graphs; O(rows × cols) for grids.
- Space: O(V) for the visited set / recursion stack / queue.

## Common pitfalls

- Marking a node visited when it's *enqueued* (BFS) vs when it's *popped* — for BFS,
  mark on enqueue to avoid duplicate queue entries blowing up the complexity.
- Recursive DFS on a large/adversarial input can hit Python's recursion limit — prefer
  the iterative stack version unless depth is bounded.
- Grid problems: bounds-check neighbors before indexing, and decide 4- vs 8-directional
  adjacency explicitly.

## Example problems

_(TODO — filled in as problems land in `problems/bfs_dfs/`)_
