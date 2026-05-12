# Problem Name: Merge Sorted Array
# Pattern Used: Two Pointers
# Time Complexity: O(N)
# Space Complexity: O(1)
# Short Explanation: We use two pointers to merge two sorted arrays.
# LeetCode Link: https://leetcode.com/problems/merge-sorted-array/

from ast import List
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        j = 0
        for i in range(m, len(nums1)):
            nums1[i] = nums2[j]
            j += 1

        nums1.sort()
        return nums1