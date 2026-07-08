# Input / Output

## Input

### N, then N pairs of ints via list comprehension

`[expression for _ in range(n)]` calls `input()` once per iteration, so it can replace
a `for` loop that appends to a list line-by-line. Common when the first line gives a
count `n` and each of the next `n` lines holds a fixed-width record (here, a pair of
ints).

```python
n = int(input())
pairs = [tuple(map(int, input().split())) for _ in range(n)]
```

**Input format**

```
4
4 2
8 8
3 4
2 1
```

```python
pairs
# [(4, 2), (8, 8), (3, 4), (2, 1)]
```

`tuple(...)` packages each pair as immutable; swap in `list(...)` if the pair needs to
be mutated later.

## Output

### Mapping records to per-line strings, then printing them as one block

`[expression for item in items]` builds one output string per record (e.g. a
threshold check), then `"\n".join(out)` combines them into a single string with one
record per line so a single `print` emits it all, instead of calling `print` once per
record.

```python
out = ["YES" if l / p * 100 >= 75 else "NO" for p, l in lt]
print("\n".join(out))
```

**Output format**

```
YES
NO
YES
NO
```
