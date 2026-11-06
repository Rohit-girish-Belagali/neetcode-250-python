# Day 1 revision notes: NeetCode 250

## Day 1 at a glance

Day 1 (5 Nov 2026) is done: 5 NeetCode 250 problems, all Arrays & Hashing. Two Sum still needs its dictionary version.

| # | Problem | Difficulty | Pattern | Status |
| --- | --- | --- | --- | --- |
| 1 | Concatenation of Array | Easy | Preallocate and fill by index | Solved |
| 2 | Contains Duplicate | Easy | Hash set: have I seen it? | Solved |
| 3 | Valid Anagram | Easy | Frequency count with a dict | Solved |
| 4 | Two Sum | Easy | Hash map: number to index | Brute force solved; dictionary version to write |
| 5 | Longest Common Prefix | Easy | Vertical scanning | Solved |

## Patterns learned

Five patterns, one per problem. Name the pattern before you write any code.

- Preallocate and fill by index: make `[0] * size`, then assign each position. Used in Concatenation of Array.
- Hash set, "have I seen it?": store values you've passed and check membership in O(1). Used in Contains Duplicate.
- Frequency count with a dict: when order doesn't matter but counts do, build `{item: count}` and compare. A set is not enough because it forgets counts. Used in Valid Anagram.
- Hash map for the complement: for each number, look up `target - num` in a dict of value to index. Used in Two Sum.
- Vertical scanning: compare strings column by column and stop at the first mismatch. Used in Longest Common Prefix.

The theme of the day is trading space for time: a nested loop is O(n²) with O(1) extra space, and a set or dict makes it O(n) with O(n) extra space.

## Problem notes

For each problem: the idea in one line, the final Python, the complexity, and the mistake to avoid next time.

### 1. Concatenation of Array (Easy)

Build `ans` of length 2n where `ans[i] == ans[i + n] == nums[i]`. Fill both halves in one pass.

```python
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (2 * n)
        for i in range(n):
            ans[i] = nums[i]
            ans[i + n] = nums[i]
        return ans
```

- Time O(n), space O(n) for the output. One-liner: `return nums + nums`.
- Watch out: `[0] * n` is fine for numbers, but `[[]] * n` makes n references to the same inner list.

#### Walkthrough

"Concatenation" means joining two things end to end, like `[1, 2]` + `[3, 4]` = `[1, 2, 3, 4]`. Here you join `nums` with a copy of itself. `ans[i] == nums[i]` says the value at position `i` of `ans` equals the value at position `i` of `nums`; it does not mean the number `i` is stored. `ans[i + n]` jumps `n` positions ahead, which lands in the second half.

Trace for `nums = [1, 4, 1, 2]`, `n = 4`:

| `i` | `nums[i]` | writes `ans[i]` | writes `ans[i + 4]` | `ans` after the step |
| --- | --- | --- | --- | --- |
| start | | | | `[0,0,0,0,0,0,0,0]` |
| 0 | 1 | `ans[0] = 1` | `ans[4] = 1` | `[1,0,0,0,1,0,0,0]` |
| 1 | 4 | `ans[1] = 4` | `ans[5] = 4` | `[1,4,0,0,1,4,0,0]` |
| 2 | 1 | `ans[2] = 1` | `ans[6] = 1` | `[1,4,1,0,1,4,1,0]` |
| 3 | 2 | `ans[3] = 2` | `ans[7] = 2` | `[1,4,1,2,1,4,1,2]` |

Line by line:

- `n = len(nums)`: the number of elements, used for both the loop and the jump.
- `ans = [0] * (2 * n)`: allocates `2n` slots up front so every index exists before you assign to it.
- `for i in range(n)`: `i` visits every position of `nums` (`0` to `n - 1`). It runs `n` times, not `2n`, because each pass fills two slots.
- The two assignments copy `nums[i]` into the first half and the second half.
- `return ans` hands back the finished list.

Edge case and interview notes:

- Smallest input is `n = 1`: `[5]` gives `[5, 5]`.
- Say the index relationship out loud (`ans[i]` and `ans[i + n]` both equal `nums[i]`) before coding.
- The output has `2n` items, so O(n) space is unavoidable. Time can't beat O(n) either, since every output slot must be written.
- Python alternatives: `nums + nums`, `nums * 2`, or `ans = nums[:]` then `ans.extend(nums)`. All are O(n).

### 2. Contains Duplicate (Easy)

Walk left to right, remember every number seen, and return `True` the moment one repeats.

```python
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
```

- Brute force (two loops) is O(n²) time, O(1) space. The set version is O(n) time, O(n) space: extra memory buys speed.
- Check first, add after. Adding first would make every number find itself.
- Mistakes: missing `:` after `if`, `true` instead of `True`, `return` and `add` at the wrong indentation.

#### Walkthrough

The question is only "does any value appear more than once?". You don't need which value or how many times, so you can stop at the first repeat.

Trace for `[1, 2, 3, 3]` (answer `True`):

| pass | `num` | already in `seen`? | action | `seen` after |
| --- | --- | --- | --- | --- |
| 1 | 1 | no | add | `{1}` |
| 2 | 2 | no | add | `{1, 2}` |
| 3 | 3 | no | add | `{1, 2, 3}` |
| 4 | 3 | yes | `return True` | stops |

For `[1, 2, 3, 4]` no pass finds a repeat, so the loop ends and `return False` runs. For `[]` the loop body never runs, so it also returns `False`.

Brute force, for comparison:

```python
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] == nums[j]:
            return True
return False
```

It checks (n-1) + (n-2) + ... + 1 = n(n-1)/2 pairs, which is O(n²). For `n = 10^5` that is about 5 billion comparisons, far too slow.

Why the set version is fast:

- A set is a hash table. Checking `x in seen` and calling `seen.add(x)` are O(1) on average, so one pass of `n` numbers is O(n).
- Use a set, not a list. `x in some_list` scans the list, which is O(n) per check, and silently brings you back to O(n²).
- Values can be negative or up to 10^9. That's fine, because a set does not use the value as an array index.

Other ways to solve it:

| Approach | Time | Extra space | Note |
| --- | --- | --- | --- |
| Nested loops | O(n²) | O(1) | Too slow for n = 10^5 |
| Sort, then compare neighbours | O(n log n) | O(1) to O(n) | Duplicates end up next to each other; changes the order |
| Hash set (used) | O(n) | O(n) | Best time; stops at the first repeat |
| `len(set(nums)) != len(nums)` | O(n) | O(n) | One line, but builds the whole set even if the repeat is at index 1 |

Interview notes: say the trade-off ("I spend O(n) memory to get O(n) time"), ask whether you may modify the input (needed for the sort approach), and mention the early exit on the first repeat.

### 3. Valid Anagram (Easy)

Two strings are anagrams when every letter has the same count. Count letters in each string, then compare the two dicts.

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = {}
        for ch in s:
            count_s[ch] = count_s.get(ch, 0) + 1

        count_t = {}
        for ch in t:
            count_t[ch] = count_t.get(ch, 0) + 1

        return count_s == count_t
```

- Time O(n + m). Space O(1): only 26 lowercase letters can ever be keys.
- A set fails here: `"aab"` and `"abb"` have the same set `{a, b}` but different counts.
- Extras: `sorted(s) == sorted(t)` is O(n log n). Return `False` early if the lengths differ.
- Mistakes: reading from `count_s` inside the `count_t` loop, `.get[...]` with square brackets, and a NameError from using `y` instead of `t`.

#### Walkthrough

Two strings are anagrams when they use the same letters with the same counts, in any order. Order doesn't matter; counts do.

Why a set fails: `"aab"` and `"abb"` give the same set `{a, b}`, but the counts differ.

| string | letters | set | counts |
| --- | --- | --- | --- |
| `"aab"` | a, a, b | `{a, b}` | `{a: 2, b: 1}` |
| `"abb"` | a, b, b | `{a, b}` | `{a: 1, b: 2}` |

So you need a dictionary from letter to count.

The key line is `count_s[ch] = count_s.get(ch, 0) + 1`. Read it right to left: `.get(ch, 0)` gives the current count, or `0` if `ch` is new; `+ 1` adds this occurrence; the assignment stores it back. Building `"aab"`:

| letter | `get(ch, 0)` | new count | dict after |
| --- | --- | --- | --- |
| a | 0 | 1 | `{a: 1}` |
| a | 1 | 2 | `{a: 2}` |
| b | 0 | 1 | `{a: 2, b: 1}` |

Trace for `"jar"` and `"jam"`: `count_s = {j:1, a:1, r:1}`, `count_t = {j:1, a:1, m:1}`. The dicts are different, so it returns `False`. Dict `==` is true when both have the same keys with the same values, regardless of order.

Complexity:

- Time O(n + m): one pass over `s`, one over `t`, O(1) per letter. The final comparison touches at most 26 entries.
- Space O(1): only lowercase letters appear, so each dict holds at most 26 keys no matter how long the strings are.

Other ways to solve it:

| Approach | Time | Space | Note |
| --- | --- | --- | --- |
| `sorted(s) == sorted(t)` | O(n log n) | O(n) | Shortest to write; the sort is the cost |
| `Counter(s) == Counter(t)` | O(n + m) | O(1) | `from collections import Counter`; same idea as the two dicts |
| One dict: `+1` for `s`, `-1` for `t`, all zero at the end | O(n + m) | O(1) | Half the memory |
| 26-slot list with `ord(ch) - ord('a')` | O(n + m) | O(1) | Fixed size; only works for a known small alphabet |

Early exit: if `len(s) != len(t)`, return `False` immediately. Follow-up question to expect: "what if the strings contain Unicode?" A dict still works (space becomes O(k) for k distinct characters); the 26-slot list does not.

### 4. Two Sum (Easy)

Find the two positions whose numbers add up to `target`. For each number, the partner you need is `target - num`.

Brute force, accepted:

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
```

- Time O(n²), space O(1). Starting `j` at `i + 1` stops a number pairing with itself.
- Still to do (Day 2): the one-pass dictionary version, O(n) time and O(n) space. Dict maps number to position; check for `target - num` before storing the current number.
- Mistakes: a stray `\` after the `def` line, `return [i] , [j]` (two lists) instead of `[i, j]`, returning `true` when the problem wants positions, and an `else` that returns too early.

#### Walkthrough

You are looking for two positions, not two numbers. Standing at `nums[i]`, the partner you need is exactly `target - nums[i]`. Everything in this problem is about how you find that partner.

Brute force trace for `[4, 5, 6]`, target 10:

| `i` | `j` | `nums[i] + nums[j]` | equals 10? |
| --- | --- | --- | --- |
| 0 | 1 | 9 | no |
| 0 | 2 | 10 | yes, return `[0, 2]` |

- `j` starts at `i + 1` so a number never pairs with itself (`i != j`) and each pair is tried only once.
- The nested loops check n(n-1)/2 pairs: O(n²) time, O(1) space.
- No `else` is needed: exactly one valid pair is guaranteed, so the loops always find it.

The O(n) idea, in words (you still need to write this one on Day 2):

1. Make an empty dict that maps a number to the position where you saw it.
2. For each position `i` and number `num`, compute `needed = target - num`.
3. If `needed` is already a key in the dict, you found the pair: return the stored position of `needed` and `i`.
4. Otherwise store `num` with its position `i` and move on.

Dry run for `[3, 4, 5, 6]`, target 7:

| `i` | `num` | `needed` | `needed` in dict? | dict after |
| --- | --- | --- | --- | --- |
| 0 | 3 | 4 | no | `{3: 0}` |
| 1 | 4 | 3 | yes, at position 0 | return `[0, 1]` |

Dry run for `[5, 5]`, target 10: at `i = 0`, `needed = 5` is not in the empty dict, so store `{5: 0}`. At `i = 1`, `needed = 5` is in the dict at position 0, so return `[0, 1]`.

Why check the dict before storing: if you stored `num` first, then for `[5]` with target 10 the number would find itself and pair with itself. Checking first guarantees the partner came from an earlier position.

Why the smaller index comes first: the stored position is always from an earlier pass, so it is smaller than the current `i`. Return `[stored, i]`.

Trade-off to say out loud: the dict version spends O(n) extra memory to cut time from O(n²) to O(n).

Questions to ask an interviewer: can numbers repeat, can they be negative, is there always exactly one answer, and may I return either order?

### 5. Longest Common Prefix (Easy)

Read the words column by column and stop at the first column where any word disagrees or runs out of letters.

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first = strs[0]

        for i in range(len(first)):
            for word in strs:
                if i == len(word) or word[i] != first[i]:
                    return first[:i]

        return first
```

- Time O(n × m) with n words and m the length of the shortest word. Space O(1) extra.
- Edge cases: `["neet","feet"]` gives `""`, `["abcd","ab"]` gives `"ab"`, `["abc"]` gives `"abc"`, `[""]` gives `""`.
- Mistakes: typing the numbered blank labels `[1]`, `[2]` into the code, `len(strs)` (word count) instead of `len(first)` (letter count), and a missing `=` in `first = strs[0]`.

#### Walkthrough

A prefix is the beginning of a string: `"ba"` is a prefix of `"bank"`. The common prefix is the beginning that all the words share. Line the words up and read them column by column:

| word | col 0 | col 1 | col 2 | col 3 |
| --- | --- | --- | --- | --- |
| bat | b | a | t | |
| bag | b | a | g | |
| bank | b | a | n | k |
| band | b | a | n | d |

Column 0 is all `b`, column 1 is all `a`, column 2 is `t, g, n, n`, which disagree. Stop there. Everything before that column is the answer: `"ba"`.

Line by line:

- `first = strs[0]`: the first word is the reference everything is compared against.
- `for i in range(len(first))`: `i` is the column number. The prefix can never be longer than `first`, so that is the most columns you need.
- `for word in strs`: check every word in column `i`.
- `if i == len(word) or word[i] != first[i]`: a word breaks the prefix in one of two ways. Either it has no column `i` (it ran out of letters), or its letter differs from `first`'s letter in that column. The length check comes first on purpose: Python skips the right side of `or` when the left side is true, so `word[i]` is never evaluated on a word that is too short, which would crash.
- `return first[:i]`: a mismatch at column `i` means the prefix is the columns before it. The slice `first[:i]` keeps positions `0` to `i - 1`.
- `return first`: if no column ever failed, the whole first word is the common prefix.

Traces:

| input | where it stops | returns |
| --- | --- | --- |
| `["bat","bag","bank","band"]` | `i = 2`, word `bag`: `g` vs `t` | `first[:2] = "ba"` |
| `["neet","feet"]` | `i = 0`, word `feet`: `f` vs `n` | `first[:0] = ""` |
| `["abcd","ab"]` | `i = 2`, word `ab`: `i == len(word)` | `first[:2] = "ab"` |
| `["abc"]` | never | `first = "abc"` |
| `[""]` | loop never runs | `first = ""` |

Complexity: time O(n × m) with `n` words and `m` the length of the shortest word, because the scan stops at the shortest word. In the worst case (all words identical) you read every character once. Space is O(1) extra.

Other ways to solve it:

| Approach | Time | Note |
| --- | --- | --- |
| Vertical scanning (used) | O(n × m) | Stops at the first mismatch column |
| Horizontal scanning: shrink the prefix against each word with `startswith` | O(n × m) | Simple, but compares whole strings |
| Sort, then compare only the first and last word | O(n × m × log n) | Works because the two extremes differ most |
| Trie | O(total characters) | More code; worth it when you answer many prefix queries |

Interview notes: ask what to return for an empty list or empty strings, state that the answer can't be longer than the shortest word, and point out the early exit.

## Python cheat sheet

These are the only Python pieces Day 1 needed. Keep them handy.

| Need | Code | Note |
| --- | --- | --- |
| Empty set | `seen = set()` | Add with `seen.add(x)`, test with `x in seen` (O(1) average) |
| Count items in a dict | `d[k] = d.get(k, 0) + 1` | `.get(k, 0)` returns 0 if the key is new |
| Position and value together | `for i, num in enumerate(nums):` | Needed for Two Sum's dictionary version |
| Loop over letters | `for ch in s:` | Works on any string |
| Letters before position i | `s[:i]` | Slice end is not included |
| Prefilled list | `[0] * n` | Safe for numbers only |
| Join two lists | `nums + nums` | Makes a new list |
| Compare two dicts | `d1 == d2` | Same keys and same values, order ignored |
| Return two positions | `return [i, j]` | One list, not `[i], [j]` |
| Booleans | `True`, `False` | Capital first letter |

## Mistakes to avoid

Most of Day 1's errors were small Python slips, and the error message always pointed at the line. Read its last line first.

- Missing `:` at the end of `if`, `for` and `def` lines.
- `true` and `false` instead of `True` and `False`.
- Indentation decides what is inside a loop or `if`: the `return` belongs inside the `if`, the `add` inside the loop, and the final `return` outside both loops.
- A stray `\` at the end of a line makes Python glue the next line onto it.
- Returning the wrong shape: `[i], [j]` is two lists, `[i, j]` is one. Check whether the problem wants positions or a boolean.
- Reading from the wrong variable (`count_s.get` inside the `count_t` loop) and name typos (`y` instead of `t`, which gives a NameError).
- An `else: return` inside a search loop ends the search after the first failed attempt.
- Using a set when counts matter. Sets only remember that something exists.
- Typing numbered blank labels like `[1]` into code. A blank is replaced entirely by your answer.
- `len(strs)` is the number of words; `len(first)` is the number of letters in one word.

## How to work out complexity

Time complexity answers one question: as the input size `n` grows, how does the number of steps grow? Count how many times the main operation runs, then drop constants and smaller terms.

1. Find the loops. One loop over `n` items is O(n). A loop inside a loop, both over `n`, is O(n²).
2. Multiply for nested loops, add for loops one after another. Two sequential loops are O(n) + O(n) = O(n); nested they are n × n.
3. Drop constants and small terms. O(2n) is O(n), and O(n² + n) is O(n²).
4. Know what each operation costs. List indexing, set `in`, set `add` and dict lookup are O(1) on average. `x in some_list` is O(n). Slicing `s[:i]` is O(i).
5. Space is the extra memory you create, not counting the input.

One worked count: nested loops that compare each pair once check (n-1) + (n-2) + ... + 1 = n(n-1)/2 pairs. That is n²/2 - n/2, and dropping the constant and the smaller term leaves O(n²).

| Problem | Time | Space |
| --- | --- | --- |
| Concatenation of Array | O(n) | O(n) output |
| Contains Duplicate, set | O(n) | O(n) |
| Contains Duplicate, brute force | O(n²) | O(1) |
| Valid Anagram | O(n + m) | O(1), 26 letters |
| Two Sum, brute force | O(n²) | O(1) |
| Two Sum, dictionary | O(n) | O(n) |
| Longest Common Prefix | O(n × m) | O(1) |

## How to explain a solution out loud

Interviewers grade your reasoning as much as your code. Use this order every time:

1. Restate the problem in your own words and give one example.
2. Ask about edge cases: empty input, one element, duplicates, negatives, size limits.
3. Describe the brute force and its complexity.
4. Say what is wasted, then describe the better idea and what it costs (usually extra memory).
5. Write the code, narrating each loop.
6. Trace it by hand on your example and on one edge case.
7. State the final time and space complexity.

## Day 2 revision plan

Start Day 2 by re-solving Day 1 from a blank editor with no notes, then do 5 new problems. Re-solving from memory is what makes a pattern stick.

- [ ] Contains Duplicate: write the set version from scratch, then say its time and space out loud.
- [ ] Valid Anagram: write the dictionary version from scratch. Test `"aab"` and `"abb"` (expect `False`).
- [ ] Two Sum, dictionary version: write the plain-English plan first. Dict maps number to position; compute `target - num`; check the dict before storing. Test `[5, 5]` with target 10.
- [ ] Longest Common Prefix: re-solve, then trace `["bat","bag","bank","band"]` by hand.
- [ ] Concatenation of Array: both versions (loop and `nums + nums`).
- [ ] Next 5 new problems in NeetCode 250 order: click the `>` arrow on the problem page.

Self-check questions. Answer these aloud before you open any code:

1. Why can't a set solve Valid Anagram?
2. In Two Sum, why do we check the dictionary before storing the current number?
3. Why is the nested-loop Two Sum O(n²), and what does the dictionary version spend to become O(n)?
4. In Longest Common Prefix, what stops the scan, and why is `i == len(word)` checked first?

Routine for every problem: read it twice, write your own examples, brute force first, find what is wasted, code it, trace by hand, then submit. Write the pattern name and the complexity in your notebook.
