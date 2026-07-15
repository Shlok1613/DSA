# Problem Name: Single Number
# Pattern Used: Hash Table
# Time Complexity: O(n)
# Space Complexity: O(n)
# Short Explanation: We use a hash table to count occurrences of each number and return the one that occurs only once.
# LeetCode: https://leetcode.com/problems/single-number/

from ast import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = {}
        ans = None

        for num in nums:
            count[num] = count.get(num, 0) + 1
        for i in count:
            if count[i] == 1:
                ans = i

        return ans 
