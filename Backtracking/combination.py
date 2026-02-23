# Problem Name: Combinations
# Pattern Used: Backtracking
# Time Complexity: O(k * C(n, k)) where C(n, k) is the number of combinations of n items taken k at a time
# Space Complexity: O(k) where k is the number of elements in each combination
# Short Explanation: The function generates all possible combinations of k numbers from the range 1 to n.
#                   It uses backtracking to explore all potential combinations by adding numbers to the current path and
#                   checking if the required number of elements has been reached. If the required number of elements is reached,
#                   it adds the current combination to the result list. The function also ensures that numbers are
#                   added in increasing order to avoid duplicates and maintain the correct combination structure.
# LeetCode: https://leetcode.com/problems/combinations/

from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        sol = []
        def backtrack(remain, comb, nex):
            if remain == 0:
                sol.append(comb.copy())

            else:
                for i in range(nex,n+1):
                    comb.append(i)
                    backtrack(remain-1,comb,i+1)
                    comb.pop()

        backtrack(k, [], 1)
        return sol