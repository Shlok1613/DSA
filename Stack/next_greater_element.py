# Problem Name: Next Greater Element I
# Pattern Used: Stack
# Time Complexity: O(N*M)
# Space Complexity: O(1)
# Short Explanation: For each element in nums1, we find its position in nums2 and then look for the next greater element.
# LeetCode: https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [""] * len(nums1)
        for i in range(len(nums1)):
            pos = nums2.index(nums1[i])
            if nums2[pos] == nums2[-1]:
                ans[i] = -1
            else:
                for j in nums2[pos:]:
                    if j > nums2[pos]:
                        ans[i] = j
                        break
                    ans[i] = -1

        return ans