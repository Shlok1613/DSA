# Problem Name: Subsets
# Pattern Used: Recursion and Backtracking
# Time Complexity: O(N * 2^N)
# Space Complexity: O(N * 2^N)
# Short Explanation: The function generates all possible subsets of a list of numbers using recursion and backtracking.
# LeetCode: https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, path):
            res.append(path)
            for i in range(start, len(nums)):
                backtrack(i + 1, path + [nums[i]])

        res = []
        backtrack(0, [])
        return res       