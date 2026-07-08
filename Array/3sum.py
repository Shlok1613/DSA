# Problem Name: 3Sum
# Pattern Used: Two Pointers
# Time Complexity: O(n^2) where n is the number of elements in the input list
# Space Complexity: O(1) since we are not using any extra space for data structures
# Short Explanation: The function finds all unique triplets in the input list that sum up to zero.
# LeetCode: https://leetcode.com/problems/3sum/

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue 

            j = i+1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total > 0:
                    k -= 1

                elif total < 0:
                    j += 1

                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1

                    while j < k and nums[j] == nums[j-1]:
                        j+=1

        return res