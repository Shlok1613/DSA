# Problem Name: Container With Most Water
# Pattern Used: Array
# Time Complexity: O(n)
# Space Complexity: O(1)
# Short Explanation: We use two pointers, one at the start and one at the end of the array,
#                    and calculate the area formed by the lines at these pointers. 
#                    We then move the pointer with the shorter line inward to potentially find a larger area.
# LeetCode Link: https://leetcode.com/problems/container-with-most-water/

from ast import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        maximum = 0

        i = 0
        j = len(height) - 1

        while i < j:
            maximum = max(min(height[i], height[j]) * (j - i), maximum)

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return maximum