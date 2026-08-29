# Problem Name: Palindrome Number
# Pattern Used: String
# Time Complexity: O(n)
# Space Complexity: O(n)
# Short Explanation: The integer is converted to a string and checked if it is equal to its reverse.
# Leetcode: https://leetcode.com/problems/palindrome-number/description/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)[::-1] == str(x)