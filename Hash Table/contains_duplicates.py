#Problem Name: Contains Duplicate
#Pattern Used: Hash Table
#Time Complexity: O(n)
#Space Complexity: O(n)
#Short Explanation: We use a hash table to count occurrences of each number and check for duplicates.
#LeetCode: https://leetcode.com/problems/contains-duplicate/

class Solution(object):
    def containsDuplicate(self, nums):
        count_dict = {}
        for num in nums:
            count_dict[num] = count_dict.get(num, 0) + 1
            if count_dict[num] > 1:
                return True
        return False