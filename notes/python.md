# Python learning notes

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
