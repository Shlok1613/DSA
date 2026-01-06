#Problem Name: Concatenation of Array
#Pattern Used: Array Manipulation
#Time Complexity: O(n)
#Space Complexity: O(n)
#Short Explaination: We create a new array and keep appending elements from the original array until the new array's length is twice the original array's length.
#LeetCode: https://leetcode.com/problems/concatenation-of-array/

class Solution(object):
    def getConcatenation(self, nums):
        n = len(nums)
        ans = []
        while len(ans) < 2*n:
            for i in nums:
                ans.append(i)
        return ans