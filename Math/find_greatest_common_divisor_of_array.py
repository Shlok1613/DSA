# Problem Name: Find Greatest Common Divisor of Array
# Pattern Used: Math
# Time Complexity: O(N)
# Space Complexity: O(1)
# Short Explanation: We use math to find the GCD of odd and even sums.
# LeetCode Link: https://leetcode.com/problems/find-greatest-common-divisor-of-array/

from ast import List
import math

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        small = min(nums)
        large = max(nums)

        return math.gcd(small, large)