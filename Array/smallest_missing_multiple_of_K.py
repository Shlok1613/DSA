# Problem Name: Smallest Missing Multiple of K
# Pattern Used: Simulation
# Time Complexity: O(n)
# Space Complexity: O(1)
# Short Explanation: The problem is solved by iterating through the multiples of K starting from K itself. For each multiple, 
#                    we check if it is present in the given list of numbers. 
#                    The first multiple that is not found in the list is returned as the smallest missing multiple of K.
# LeetCode: https://leetcode.com/problems/smallest-missing-multiple-of-k/description/

from typing import List


class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        check = 0
        for i in range(1,102):
            check = k * i

            if check not in nums:
                return check
                break