#Problem Name: Maximum Subarray
#Pattern Used: Kadane's Algorithm
#Time Complexity: O(n)
#Space Complexity: O(1)
#Short Explanation: We iterate through the array while maintaining a running sum of the current subarray. 
#                   If the running sum becomes negative, we reset it to zero since starting a new subarray would yield a higher sum.
#                   We also keep track of the maximum sum encountered during the iteration.
#                   And then return the maximum sum found.
#LeetCode: https://leetcode.com/problems/maximum-subarray/

class Solution(object):
    def maxSubArray(self, nums):
        sums = 0
        maximum = nums[0]

        for i in nums:
            if sums < 0:
                sums = 0

            sums += i
            maximum = max(sums, maximum)
        return maximum
        