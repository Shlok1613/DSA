# Problem Name: Construct Uniform Parity Array II
# Pattern Used: Array Manipulation
# Time Complexity: O(N)
# Space Complexity: O(1)
# Short Explanation: The function checks if the given array can be transformed into a uniform parity array
# LeetCode Link: https://leetcode.com/problems/construct-uniform-parity-array-ii/

class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        smallestOdd = float("inf")
        for num in nums1:
            if num % 2 == 1:
                smallestOdd = min(smallestOdd, num)
            
        if smallestOdd == float("inf"):
            return True

        for num in nums1:
            if num % 2 == 0 and num <= smallestOdd:
                return False

        return True

        