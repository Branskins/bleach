# Python learning notes

## `if __name__ == "__main__":` Standard Python Main Pattern

`__name__` is a built-in variable that Python sets to `"__main__"` when a file is run
directly (e.g. `python solution.py`), but to the module's name when it's imported by
another file. Guarding script code behind this check lets a file be both a runnable
script and an importable module without the script part running on import (e.g. when
a test file does `from solution import solve`).

```python
def main():
    pass


if __name__ == "__main__":
    main()
```

## Set comprehensions with tuple unpacking (dedupe one field of pairs)

`{expression for item in iterable if condition}` 

Iterates over a list of pairs, unpacking each into two
names, and collects one of them into a **set**, which drops duplicates for free.
Useful when you need the unique values of one field while ignoring another (e.g.
grades regardless of which student got them).

```python
students = [["Harry", 37.21], ["Berry", 37.21], ["Tina", 37.2], ["Akriti", 41]]

grades = {grade for _, grade in students}
# {37.21, 37.2, 41}  -- duplicate 37.21 collapsed into one

sorted(grades)
# [37.2, 37.21, 41]
```

The `_` is a throwaway variable name — a convention meaning "unpacked but unused."

## Lists

### `map` to convert every string element to another type

`map(function, iterable)` lazily applies `function` to each item in `iterable`,
returning a `map` object (an iterator, not a list). Wrap it in `list(...)` to
materialize the results. Common when input comes in as whitespace-split strings but
you need numbers.

```python
name, *line = "Akriti 37.21 41.0 39.0".split()
# name = "Akriti", line = ["37.21", "41.0", "39.0"]

scores = list(map(float, line))
# [37.21, 41.0, 39.0]
```

## Text Processing Services

### `textwrap.wrap` to break a string into fixed-width lines

`textwrap.wrap(text, width)` splits `text` into a **list of lines**, each no longer
than `width` characters, breaking on whitespace between words (it won't cut a word in
half unless the word itself exceeds `width`). Join the list with `"\n"` to get the
wrapped block as one string.

```python
import textwrap

textwrap.wrap("This is a really long line", 8)
# ["This is", "a really", "long", "line"]

"\n".join(textwrap.wrap("This is a really long line", 8))
# "This is\na really\nlong\nline"
```

### string - Common string operations

#### `string.ascii_lowercase` for the alphabet as a string

`string.ascii_lowercase` is a constant string containing all 26 lowercase letters in
order, `"abcdefghijklmnopqrstuvwxyz"`. Useful whenever a problem needs to index into or
slice the alphabet instead of hardcoding it.

```python
import string

string.ascii_lowercase
# "abcdefghijklmnopqrstuvwxyz"

string.ascii_lowercase[:5]
# "abcde"
```

## Built-in Functions

### `bin` to get an integer's binary representation

`bin(n)` returns a string of the binary representation of integer `n`, prefixed with
`"0b"`. Strip the prefix with `[2:]` when you just need the raw digits.

```python
bin(5)
# "0b101"

bin(5)[2:]
# "101"
```

### `enumerate` to pair each element with its index

`enumerate(iterable)` returns an iterator of `(index, element)` tuples, so you avoid
manually tracking a counter or indexing back into the iterable with `[i]`.

```python
string = "AEIOU"

for i, c in enumerate(string):
    print(i, c)
# 0 A
# 1 E
# 2 I
# 3 O
# 4 U
```

## Data Types

### collections

#### `Counter` for counting hashable items

`Counter(iterable)` builds a dict-like object mapping each distinct item to its count.
Indexing a missing key returns `0` instead of raising `KeyError`, which makes it handy
as a depleting stock/tally: decrement a key as items get "used up" without needing to
check for existence first.

```python
from collections import Counter

sizes = [2, 3, 4, 5, 6, 8]
stock = Counter(sizes)
# Counter({2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 8: 1})

stock[9]
# 0  -- missing key, no KeyError

stock[4] -= 1
# Counter({2: 1, 3: 1, 4: 0, 5: 1, 6: 1, 8: 1})
```
