# Problem Name: Removing Minimum and Maximum From Array
# Pattern Used: Array
# Time Complexity: O(n)
# Space Complexity: O(1)
# Short Explanation: We find the minimum and maximum values in the array, 
#                    then calculate the number of deletions required to remove them from the front, back, or both ends of the array.
# LeetCode Link: https://leetcode.com/problems/removing-minimum-and-maximum-from-array/

from ast import List


class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        minimum = min(nums)
        maximum = max(nums)

        

        min_pos = nums.index(minimum)
        max_pos = nums.index(maximum)

        n = len(nums)

        front = max(min_pos + 1, max_pos + 1)
        back = max(n - min_pos, n - max_pos)
        both = min(min_pos + 1, max_pos + 1) + min(n - min_pos, n - max_pos)

        return min(front, back, both)