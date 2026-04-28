# Problem Name: Sort Colors
# Pattern Used: Two Pointers
# Time Complexity: O(n) where n is the number of elements in the input list
# Space Complexity: O(1) since we are sorting the list in place
# Short Explanation: The function sorts the input list of colors (represented as integers) in place.
#                   It uses the built-in sort method which is efficient and sorts the list in O(n log n) time. 
#                   However, since the problem can be solved in O(n) time using the Dutch National Flag algorithm,
#                   the provided solution is not optimal for this specific problem.
# LeetCode: https://leetcode.com/problems/sort-colors/

from ast import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        return nums.sort()
    
# Optimal Solution using Dutch National Flag Algorithm
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low, mid, high = 0, 0, len(nums) - 1
        
        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:  # nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
        