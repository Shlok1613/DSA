# Problem Name: Combination Sum
# Pattern Used: Backtracking
# Time Complexity: O(2^t) where t is the target value
# Space Complexity: O(t) where t is the target value
# Short Explanation: The function finds all unique combinations of candidates that sum up to the target.
#                   It uses backtracking to explore all possible combinations by adding candidates to the current path and
#                   checking if the sum matches the target. If the sum exceeds the target, 
#                   it backtracks and tries the next candidate.
# LeetCode: https://leetcode.com/problems/combination-sum/

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack (start, path, combination_sum):
            if combination_sum == target:
                res.append(path.copy())

            if combination_sum > target:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, combination_sum + candidates[i])
                path.pop()

        backtrack(0, [], 0)
        return res
