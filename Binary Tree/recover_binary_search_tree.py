# Problem Name: Recover Binary Search Tree
# Pattern Used: Recursion
# Time Complexity: O(N)
# Space Complexity: O(N)
# Short Explanation: We use recursion to find the two nodes that are swapped in a binary search tree. 
#                    We first check if the current node is the root or one of the target nodes, if so, we return it. 
#                    Then we recursively check the left and right subtrees. 
#                    If both subtrees return a non-null value, it means the current node is the lowest common ancestor. 
#                    Otherwise, we return the non-null value from either the left or right subtree.
# LeetCode Link: https://leetcode.com/problems/recover-binary-search-tree/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        self.prev = self.first = self.second = None

        def validate(node):
            if not node:
                return

            validate(node.left)
            if self.prev and node.val < self.prev.val:
                if not self.first:
                    self.first = self.prev
                self.second = node
            self.prev = node
            validate(node.right)

        validate(root)
        
        self.first.val, self.second.val = self.second.val, self.first.val