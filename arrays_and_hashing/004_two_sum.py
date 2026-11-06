"""
Two Sum (Easy)
NeetCode 250 | Arrays & Hashing

Return the indices i and j (i != j, smaller index first) with
nums[i] + nums[j] == target. Exactly one valid pair exists.

Pattern: hash map for the complement (number -> index).
For each number, the partner you need is target - num.

Brute force (below): try every pair, j starting at i + 1.
Time:  O(n^2)
Space: O(1)

TODO (Day 2): one-pass dictionary version, O(n) time and O(n) space.
Map each number to its index; check for target - num BEFORE storing the current number.
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


if __name__ == "__main__":
    s = Solution()
    assert s.twoSum([3, 4, 5, 6], 7) == [0, 1]
    assert s.twoSum([4, 5, 6], 10) == [0, 2]
    assert s.twoSum([5, 5], 10) == [0, 1]
    print("all tests passed")
