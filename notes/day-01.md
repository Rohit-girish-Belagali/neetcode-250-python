# Day 1 notes (5 Nov 2026)

Five NeetCode 250 problems, all Arrays & Hashing. Two Sum still needs its dictionary version.

## Patterns learned

Name the pattern before writing any code.

- **Preallocate and fill by index**: make `[0] * size`, then assign each position. (Concatenation of Array)
- **Hash set, "have I seen it?"**: store values you've passed and check membership in O(1). (Contains Duplicate)
- **Frequency count with a dict**: when order doesn't matter but counts do, build `{item: count}` and compare. A set forgets counts. (Valid Anagram)
- **Hash map for the complement**: for each number, look up `target - num` in a dict of value to index. (Two Sum)
- **Vertical scanning**: compare strings column by column and stop at the first mismatch. (Longest Common Prefix)

Theme of the day: trade space for time. A nested loop is O(n^2) with O(1) extra space; a set or dict makes it O(n) with O(n) extra space.

## Python cheat sheet

| Need | Code | Note |
| --- | --- | --- |
| Empty set | `seen = set()` | `seen.add(x)`, `x in seen` is O(1) average |
| Count items in a dict | `d[k] = d.get(k, 0) + 1` | `.get(k, 0)` returns 0 if the key is new |
| Position and value together | `for i, num in enumerate(nums):` | Needed for Two Sum's dictionary version |
| Loop over letters | `for ch in s:` | Works on any string |
| Letters before position i | `s[:i]` | Slice end is not included |
| Prefilled list | `[0] * n` | Safe for numbers only |
| Join two lists | `nums + nums` | Makes a new list |
| Compare two dicts | `d1 == d2` | Same keys and values, order ignored |
| Return two positions | `return [i, j]` | One list, not `[i], [j]` |
| Booleans | `True`, `False` | Capital first letter |

## Mistakes to avoid

- Missing `:` at the end of `if`, `for` and `def` lines.
- `true` / `false` instead of `True` / `False`.
- Indentation decides what is inside a loop or `if`: the `return` belongs inside the `if`, the `add` inside the loop, and the final `return` outside both loops.
- A stray `\` at the end of a line glues the next line onto it.
- Returning the wrong shape: `[i], [j]` is two lists, `[i, j]` is one. Check whether the problem wants positions or a boolean.
- Reading from the wrong variable (`count_s.get` inside the `count_t` loop) and name typos (`y` instead of `t`, which gives a NameError).
- An `else: return` inside a search loop ends the search after the first failed attempt.
- Using a set when counts matter. Sets only remember that something exists.
- `len(strs)` is the number of words; `len(first)` is the number of letters in one word.

## Day 2 plan

Re-solve Day 1 from a blank editor with no notes, then do 5 new problems.

- [ ] Contains Duplicate: set version, say time and space out loud.
- [ ] Valid Anagram: dictionary version. Test `"aab"` and `"abb"` (expect `False`).
- [ ] Two Sum, dictionary version: plain-English plan first. Dict maps number to position; compute `target - num`; check the dict before storing. Test `[5, 5]` with target 10.
- [ ] Longest Common Prefix: re-solve, then trace `["bat","bag","bank","band"]` by hand.
- [ ] Concatenation of Array: both versions.
- [ ] Next 5 new problems in NeetCode 250 order.

Self-check questions:

1. Why can't a set solve Valid Anagram?
2. In Two Sum, why check the dictionary before storing the current number?
3. Why is the nested-loop Two Sum O(n^2), and what does the dictionary version spend to become O(n)?
4. In Longest Common Prefix, what stops the scan, and why is `i == len(word)` checked first?
