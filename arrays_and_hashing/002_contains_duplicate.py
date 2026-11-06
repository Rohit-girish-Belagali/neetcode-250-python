"""
Contains Duplicate (Easy)
NeetCode 250 | Arrays & Hashing

Return True if any value appears more than once in nums, otherwise False.

Pattern: hash set, "have I seen it?"
Idea: walk left to right, remember every number seen, and return True the moment
one repeats. Check first, add after; adding first would make every number find itself.

Brute force (two nested loops): O(n^2) time, O(1) space.
This solution:
Time:  O(n)
Space: O(n)  (extra memory buys speed)
"""
from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


if __name__ == "__main__":
    s = Solution()
    assert s.hasDuplicate([1, 2, 3, 3]) is True
    assert s.hasDuplicate([1, 2, 3, 4]) is False
    assert s.hasDuplicate([]) is False
    print("all tests passed")
