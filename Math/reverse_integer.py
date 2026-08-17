# Problem Name: Reverse Integer
# Pattern Used: Math
# Time Complexity: O(n)
# Space Complecxity: O(n)
# Short Explaination: The number is first reversed by convertign it to a string.
#                      Then it is checked if it crosses the 32-bit unsigned range.
#Leetcode: https://leetcode.com/problems/reverse-integer/description/

class Solution:
    def reverse(self, x: int) -> int:
        if str(x)[0] == "-":
            x = int("-" + str(x)[:0:-1])
        else:
            x = int(str(x)[::-1])

        if -2**31 <= x <= 2**31 - 1:
            return x
        return 0