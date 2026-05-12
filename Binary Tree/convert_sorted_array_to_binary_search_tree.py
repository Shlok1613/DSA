# Problem Name: Convert Sorted Array to Binary Search Tree
# Pattern Used: Recursion
# Time Complexity: O(N)
# Space Complexity: O(N)
# Short Explanation: We use recursion to convert a sorted array to a binary search tree. 
#                    We first find the middle element of the array and make it the root. 
#                    Then we recursively convert the left half of the array to the left subtree and the right half to the right subtree.
# LeetCode Link: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1 :])
        return root
