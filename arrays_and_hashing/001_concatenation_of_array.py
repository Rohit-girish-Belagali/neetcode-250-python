"""
Concatenation of Array (Easy)
NeetCode 250 | Arrays & Hashing

Given nums of length n, return ans of length 2n where
ans[i] == nums[i] and ans[i + n] == nums[i].

Pattern: preallocate and fill by index.
Idea: make a list of 2n slots, then write each nums[i] into both halves in one pass.

Time:  O(n)
Space: O(n) for the output

One-liner: return nums + nums
Watch out: [0] * n is fine for numbers, but [[]] * n repeats one shared inner list.
"""
from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * (2 * n)
        for i in range(n):
            ans[i] = nums[i]
            ans[i + n] = nums[i]
        return ans


if __name__ == "__main__":
    s = Solution()
    assert s.getConcatenation([1, 4, 1, 2]) == [1, 4, 1, 2, 1, 4, 1, 2]
    assert s.getConcatenation([22, 21, 20, 1]) == [22, 21, 20, 1, 22, 21, 20, 1]
    assert s.getConcatenation([5]) == [5, 5]
    print("all tests passed")
