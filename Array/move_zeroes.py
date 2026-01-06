#Prolem Name: Move Zeroes
#Pattern Used: Two Pointers
#Time Complexity: O(n)
#Space Complexity: O(1)
#Short Explanation: We use two pointers to shift non-zero elements to the front and fill the rest with zeroes.
#LeetCode: https://leetcode.com/problems/move-zeroes

class Solution(object):
    def moveZeroes(self, nums):
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        return nums
        