# Problem Name: Combination Sum II
# Pattern Used: Backtracking
# Time Complexity: O(2^t) where t is the target value
# Space Complexity: O(t) where t is the target value
# Short Explanation: The function finds all unique combinations of candidates that sum up to the target.
#                   It uses backtracking to explore all possible combinations by adding candidates to the current path and
#                   checking if the sum matches the target. If the sum exceeds the target,
#                   it backtracks and tries the next candidate. To avoid duplicates, it sorts the candidates
#                   and skips over duplicate values during the backtracking process.
# LeetCode: https://leetcode.com/problems/combination-sum-ii/

from ast import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(start, path, total):
            if total > target:
                return

            if total == target:
                res.append(path.copy())
                return 

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue

                path.append(candidates[i])
                backtrack(i+1, path, total+candidates[i])
                path.pop()

        backtrack(0, [], 0)
        return res
                