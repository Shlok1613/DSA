# Problem Name: Lowest Common Ancestor of a Binary Tree
# Pattern Used: Recursion
# Time Complexity: O(N)
# Space Complexity: O(N)
# Short Explanation: We use recursion to find the lowest common ancestor of two nodes in a binary tree. 
#                    We first check if the current node is the root or one of the target nodes, if so, we return it. 
#                    Then we recursively check the left and right subtrees. 
#                    If both subtrees return a non-null value, it means the current node is the lowest common ancestor. 
#                    Otherwise, we return the non-null value from either the left or right subtree.
# LeetCode Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root

        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        if l and r:
            return root
        return l or r
        