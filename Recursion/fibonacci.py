#Problem Nane: Fibonacci Number
#Pattern Used: Recursion
#Time Complexity: O(2^N)
#Space Complexity: O(N)
#Short Explanation: The function computes the nth Fibonacci number using a simple recursive approach.
#LeetCode: https://leetcode.com/problems/fibonacci-number/

class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        
        return self.fib(n-1) + self.fib(n-2)