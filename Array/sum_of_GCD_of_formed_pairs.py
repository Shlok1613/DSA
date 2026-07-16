# Problem Name: Sum of GCD of formed pairs
# Pattern Used: Array
# Time Complexity: O(N)
# Space Complexity: O(N)
# Short Explanation: We use prefix GCD to find the GCD of the first and last elements of the array.
# LeetCode: https://leetcode.com/problems/sum-of-gcd-of-formed-pairs/

import math

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        prefixGCD = [""] * len(nums)
        mx = 0

        for i, x in enumerate(nums):
            mx = max(x, mx)
            prefixGCD[i] = math.gcd(nums[i], mx)

        prefixGCD.sort()

        first = 0
        last = len(prefixGCD) - 1
        total = 0

        while first < last:
            total += math.gcd(prefixGCD[first], prefixGCD[last])

            first += 1
            last -= 1

        return total