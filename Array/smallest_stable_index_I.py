# Problem Name: Smallest Stable Index I
# Pattern Used: Array Manipulation
# Time Complexity: O(N^2)
# Space Complexity: O(1)
# Short Explanation: The function finds the smallest stable index in the given array based on the provided threshold k
# LeetCode Link: https://leetcode.com/problems/smallest-stable-index-i/

class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        smallest = float("inf")
        n = len(nums)

        for i in range(n):
            maximum = max(nums[0:i+1])
            minimum = min(nums[i:])

            result = maximum - minimum

            if result <= k and i < smallest:
                smallest = i

        if smallest == float("inf"):
            return -1
        else:
            return smallest