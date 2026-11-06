"""
Valid Anagram (Easy)
NeetCode 250 | Arrays & Hashing

Return True if t is an anagram of s: same letters, each the same number of times.

Pattern: frequency count with a dict.
Idea: count the letters of each string, then compare the two dicts. A set is not
enough, because it forgets counts ("aab" and "abb" have the same set {a, b}).

Time:  O(n + m)
Space: O(1)  (only 26 lowercase letters can ever be keys)

Other ways: sorted(s) == sorted(t) is O(n log n). Returning False early when
the lengths differ skips all the work.
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = {}
        for ch in s:
            count_s[ch] = count_s.get(ch, 0) + 1

        count_t = {}
        for ch in t:
            count_t[ch] = count_t.get(ch, 0) + 1

        return count_s == count_t


if __name__ == "__main__":
    s = Solution()
    assert s.isAnagram("racecar", "carrace") is True
    assert s.isAnagram("jar", "jam") is False
    assert s.isAnagram("x", "x") is True
    assert s.isAnagram("aab", "abb") is False
    print("all tests passed")
