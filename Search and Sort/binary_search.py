#Problem Name: Binary Search
#Pattern Used: Binary Search
#Time Complexity: O(log N)
#Space Complexity: O(1)
#Short Explanation: We use binary search to find the target number in the sorted array.
#                   We maintain two pointers, left and right, and calculate the mid index in each iteration. 
#                   We compare the target with the middle number and adjust the pointers accordingly 
#                   until we find the target or exhaust the search space.
#LeetCode Link: https://leetcode.com/problems/binary-search/

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1

        left = 0
        right = len(nums)

        while left <= right:
            mid = (left + right) // 2
            mid_number = nums[mid]

            if target == mid_number:
                return mid

            if target < mid_number:
                right = mid - 1

            else:
                left = mid + 1