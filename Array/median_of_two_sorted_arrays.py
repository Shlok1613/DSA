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

# Other Method 
# Time Complexity: O(log(min(N,M)))
# Space Complexity: O(1)
# Short Explanation: We use binary search to find the median of two sorted arrays.
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Always binary search on the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        x = len(nums1)   #[2]  1
        y = len(nums2)   #[1,3] 2

        left = 0
        right = x  # 1

        while left <= right:
            partitionX = (left + right) // 2     # 1
            partitionY = (x + y + 1) // 2 - partitionX   # 1

            maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]   # 2
            minRightX = float('inf') if partitionX == x else nums1[partitionX]       # inf

            maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]   # 1
            minRightY = float('inf') if partitionY == y else nums2[partitionY]       # 3

            # Correct partition found
            if maxLeftX <= minRightY and maxLeftY <= minRightX:

                # Even total number of elements
                if (x + y) % 2 == 0:
                    return (
                        max(maxLeftX, maxLeftY) +
                        min(minRightX, minRightY)
                    ) / 2

                # Odd total number of elements
                else:
                    return max(maxLeftX, maxLeftY)

            # Move towards left
            elif maxLeftX > minRightY:
                right = partitionX - 1

            # Move towards right
            else:
                left = partitionX + 1   # 1