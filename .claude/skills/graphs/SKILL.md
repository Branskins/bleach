---
name: graphs
description: Use for problems modeled as nodes and edges beyond simple traversal — topological sort (course schedule, build order), shortest path with weights (Dijkstra), union-find/disjoint-set (connectivity, cycle detection in undirected graphs), and minimum spanning tree.
---

# Graphs (beyond basic BFS/DFS)

For plain reachability/shortest-path-in-unweighted-graph, see [[bfs-dfs]]. This skill
covers the graph algorithms that need more structure than a traversal alone.

## When to reach for this

- **Topological sort**: "task A must happen before task B" style ordering — course
  schedule, build dependency order. Signal: directed graph, need a valid linear order,
  or need to detect if one is impossible (cycle).
- **Union-Find (Disjoint Set)**: dynamic connectivity queries, detecting a cycle in an
  *undirected* graph, counting connected components as edges are added incrementally.
- **Dijkstra**: shortest path with non-negative weighted edges (see [[heaps-priority-queue]]
  for the heap mechanics).

## Templates

```python
from collections import deque


def topological_sort(num_nodes: int, edges: list[tuple[int, int]]) -> list[int]:
    """Kahn's algorithm. edges are (prereq, node) meaning prereq -> node."""
    graph = {i: [] for i in range(num_nodes)}
    in_degree = [0] * num_nodes
    for prereq, node in edges:
        graph[prereq].append(node)
        in_degree[node] += 1

    queue = deque(i for i in range(num_nodes) if in_degree[i] == 0)
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for nxt in graph[node]:
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                queue.append(nxt)

    if len(order) != num_nodes:
        raise ValueError("cycle detected — no valid topological order")
    return order


class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, a: int, b: int) -> bool:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False  # already connected -> would form a cycle
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1
        return True
```

## Complexity

- Topological sort (Kahn's): O(V + E).
- Union-Find with path compression + union by rank: ~O(α(n)) per op (effectively O(1)).
- Dijkstra with a binary heap: O((V + E) log V).

## Common pitfalls

- Topological sort: forgetting to check `len(order) != num_nodes` to detect a cycle —
  without that check, a cyclic graph silently returns a partial, invalid order.
- Union-Find without path compression *and* union by rank degrades toward O(n) per op.
- Dijkstra with negative edge weights gives wrong answers — it requires non-negative
  weights (use Bellman-Ford if negatives are possible).

## Example problems

_(TODO — filled in as problems land in `problems/graphs/`)_
