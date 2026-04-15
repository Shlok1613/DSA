#Problem Name: Search in Rotated Sorted Array
#Pattern Used: Binary Search
#Time Complexity: O(log N)
#Space Complexity: O(1)
#Short Explanation: We use binary search to find the target number in the rotated sorted array.
#                   We maintain two pointers, left and right, and calculate the mid index in each iteration
#                   We compare the target with the middle number and adjust the pointers accordingly
#                   until we find the target or exhaust the search space. We also check which part of the array is sorted to decide how to adjust the pointers.
#LeetCode Link: https://leetcode.com/problems/search-in-rotated-sorted-array

from ast import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) -1

        while left <= right:
            mid = (left + right) // 2
            mid_number = nums[mid]

            if mid_number == target:
                return mid

            if nums[left] <= mid_number:
                if nums[left] <= target < mid_number:
                    right = mid - 1
                else:
                    left = mid + 1

            else:
                if nums[right] >= target > mid_number:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1