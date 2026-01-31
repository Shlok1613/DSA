# Problem Name: Power of Two
# Pattern Used: Recursion
# Time Complexity: O(log n)
# Space Complexity: O(log n) - due to recursion stack
# Short Explanation: We recursively check powers of two starting from 2^0 until we either find n or exceed it.
# LeetCode: https://leetcode.com/problems/power-of-two/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        def rec(i):
            if 2**i == n:
                return True
            if 2**i > n:
                return False
            return rec(i+1)

        return rec(0)
        