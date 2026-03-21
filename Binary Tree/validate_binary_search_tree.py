# Problem Name: Validate Binary Search Tree
# Pattern Used: Binary Search Tree
# Time Complexity: O(N)
# Space Complexity: O(N)
# Short Explanation: We use recursion to validate the binary search tree. 
#                    We maintain a range of values (minimum, maximum) that the current node's value must fall within. 
#                    If the current node's value is outside this range, it's not a valid binary search tree. 
#                    Otherwise, we recursively check the left and right subtrees with updated ranges.
# LeetCode Link: https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, minimum, maximum):
            if not node:
                return True
            
            if not (node.val > minimum and node.val < maximum):
                return False
            
            return valid(node.left, minimum, node.val) and valid(node.right, node.val, maximum)
        
        return valid(root, float("-inf"), float("inf"))