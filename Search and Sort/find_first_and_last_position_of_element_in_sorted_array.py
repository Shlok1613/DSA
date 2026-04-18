# Problem Name: Find First and Last Position of Element in Sorted Array
# Pattern Used: Binary Search
# Time Complexity: O(log N)
# Space Complexity: O(1)
# Short Explanation: We use binary search to find the first and last occurrence of the target number in the sorted array.
#                   We define a helper function that performs binary search and takes an additional parameter to indicate whether
#                   we are searching for the leftmost or rightmost occurrence.
#                   We call this helper function twice, once to find the leftmost index and once to find the rightmost index, 
#                   and return the results as a list.
# LeetCode Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array


from ast import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(nums, target, is_searching_left):
            left = 0
            right = len(nums) - 1
            idx = -1

            while left <= right:
                mid = (left + right) // 2
                mid_number = nums[mid]

                if mid_number < target:
                    left = mid + 1
                elif mid_number > target:
                    right = mid - 1
                else:
                    idx = mid
                    if is_searching_left:
                        right = mid - 1
                    else:
                        left = mid + 1
            return idx 

        left = binary_search(nums, target, True)
        right = binary_search(nums, target, False)
        
        return [left, right]
