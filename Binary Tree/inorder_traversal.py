# Problem Name: Binary Tree Inorder Traversal
# Pattern Used: Tree Traversal
# Time Complexity: O(n) where n is the number of nodes in the binary tree
# Space Complexity: O(n) in the worst case (when the tree is skewed)
# Short Explanation: The function performs an inorder traversal of a binary tree, which means it visits the left subtree, 
#                    then the current node, and finally the right subtree. It uses recursion to achieve this. 
#                    If the current node is null, it returns an empty list. 
#                    Otherwise, it recursively traverses the left subtree, appends the current node's value to the result list, 
#                    and then recursively traverses the right subtree. 
#                    The final result is a list of values in the order they were visited during the inorder traversal.
# LeetCode: https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
from ast import List
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        elements = []

        if root.left:
            elements += self.inorderTraversal(root.left)

        elements.append(root.val)

        if root.right:
            elements += self.inorderTraversal(root.right)

        return elements