# Problem Name: Find Missing Elements
# Pattern Used: Array
# Time Complexity: O(n)
# Space Complexity: O(1)
# Short Explanation: The problem can be solved by iterating through the range of minimum and maximum values in the 
#                    array and checking for missing elements.

from typing import List


class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        result = []

        minimum = min(nums)
        maximum = max(nums)

        while minimum <= maximum:
            if minimum not in nums:
                result.append(minimum)
            
            minimum += 1

        return result