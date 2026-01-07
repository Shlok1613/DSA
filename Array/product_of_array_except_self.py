#Problem Name: Product of Array Except Self
#Pattern Used: Prefix and Suffix Products
#Time Complexity: O(n)
#Space Complexity: O(n)
#Short Explanation: We create two auxiliary arrays to store the prefix and suffix products. 
#                   The prefix array at index i contains the product of all elements to the left of i,
#                   and the suffix array at index i contains the product of all elements to the right of i. 
#                   Finally, we multiply the corresponding values from the prefix and suffix arrays to get the result.
#LeetCode: https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        ans = [1] * n
        
        # Fill prefix array
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        
        # Fill suffix array
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
        
        # Calculate the result
        for i in range(n):
            ans[i] = prefix[i] * suffix[i]
        
        return ans