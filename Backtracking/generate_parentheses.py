#Problem Name: Generate Parentheses
#Pattern Used: Backtracking
#Time Complexity: O(4^n / sqrt(n))
#Space Complexity: O(4^n / sqrt(n))
#Short Explanation: The function generates all combinations of well-formed parentheses using backtracking. 
#                   It builds the string of parentheses by adding '(' and ')' while ensuring that the number of 
#                   '(' does not exceed n and the number of ')' does not exceed the number of '('.
#LeetCode: https://leetcode.com/problems/generate-parentheses/

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(left, right, s):
            if len(s) == 2*n:
                res.append(s)
                return 
            
            if left < n:
                dfs(left+1, right, s+"(")

            if right < left:
                dfs(left, right+1, s+")")

        res = []
        dfs(0, 0, "")
        return res
        