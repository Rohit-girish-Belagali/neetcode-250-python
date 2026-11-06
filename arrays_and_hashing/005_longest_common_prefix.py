"""
Longest Common Prefix (Easy)
NeetCode 250 | Arrays & Hashing

Return the longest common prefix of all strings in strs, or "" if there is none.

Pattern: vertical scanning.
Idea: compare column by column against the first word. Stop at the first column
where a word has no letter left (i == len(word)) or has a different letter. The
answer is everything before that column. If no column ever fails, the whole first
word is the prefix.

Time:  O(n * m)  (n words, m = length of the shortest word)
Space: O(1) extra
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first = strs[0]

        for i in range(len(first)):
            for word in strs:
                if i == len(word) or word[i] != first[i]:
                    return first[:i]

        return first


if __name__ == "__main__":
    s = Solution()
    assert s.longestCommonPrefix(["bat", "bag", "bank", "band"]) == "ba"
    assert s.longestCommonPrefix(["dance", "dag", "danger", "damage"]) == "da"
    assert s.longestCommonPrefix(["neet", "feet"]) == ""
    assert s.longestCommonPrefix(["abcd", "ab"]) == "ab"
    assert s.longestCommonPrefix(["abc"]) == "abc"
    assert s.longestCommonPrefix([""]) == ""
    print("all tests passed")
