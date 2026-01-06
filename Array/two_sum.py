#Problem Name: Two Sum
#Pattern Used: Hash Map
#Time Complexity: O(n)
#Space Complexity: O(n)
#Short Explaination: We use a hash map to store the numbers we have seen so far and their indices. 
#                    For each number, we calculate the difference between the target and the current number. 
#                    If this difference exists in the hash map, we have found our two numbers and return their indices.
#                    If does not exist, we add the current number and its index to the hash map and continue.
#LeetCode: https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        number_map = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in number_map:
                return [i, number_map[diff]]

            number_map[num] = i
        
        return None
        