# Problem Name: Valid Parentheses
# Pattern Used: Stack
# Time Complexity: O(N)
# Space Complexity: O(N)
# Short Explanation: We use a stack to keep track of opening brackets and ensure they are properly closed in the correct order.
# LeetCode: https://leetcode.com/problems/valid-parentheses/

class Solution(object):
    def isValid(self, s):
        stack = []
        for i in s:
            if i == ")" and stack:
                if stack[-1] == "(" :
                    stack.pop()
                else:
                    return False
            elif i == "]" and stack:
                if stack[-1] == "[":
                    stack.pop()
                else:
                    return False
            elif i == "}" and stack:
                if stack[-1] == "{":
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
            
        if stack:
            return False
        return True
