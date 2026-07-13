# Problem name: Median of Two Sorted Arrays
# Pattern used: Brute Force
# Time Complexity: O(N log N)
# Space Complexity: O(N)
# Short Explanation: We merge the two arrays and sort them. Then we find the median.
# LeetCode Link: https://leetcode.com/problems/median-of-two-sorted-arrays/

from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = nums1 + nums2
        arr.sort()

        if len(arr) % 2 == 0:
            mid = len(arr) // 2
            median = (arr[mid] + arr[mid-1]) / 2
            return median

        else:
            mid = len(arr) // 2
            return arr[mid]