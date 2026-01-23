#Problem Name: Permutations
#Pattern Used: Recursion and Backtracking
#Time Complexity: O(N * N!)
#Space Complexity: O(N!)
#Short Explanation: The function generates all possible permutations of a list of numbers using recursion and backtracking.
#LeetCode: https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums):

        def backtrack(start):
            if start == len(nums):
                res.append(nums[:])
                return
            
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        res = []
        backtrack(0)
        return res