# Problem Name: Permutations II
# Pattern Used: Recursion and Backtracking
# Time Complexity: O(N * N!)
# Space Complexity: O(N!)
# Short Explanation: The function generates all unique permutations of a list of numbers using recursion and backtracking. 
#                    It checks for duplicates before adding a permutation to the result list.
# LeetCode: https://leetcode.com/problems/permutations-ii/

from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start):
            if start == len(nums):
                if nums[:] not in res:
                    res.append(nums[:])
                    return

            for i in range(start, len(nums)):
                nums[i], nums[start] = nums[start], nums[i]
                backtrack(start+1)
                nums[i], nums[start] = nums[start], nums[i]

        res = []
        backtrack(0)
        return res