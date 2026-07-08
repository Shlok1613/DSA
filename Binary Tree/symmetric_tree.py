# Problem Name: Symmetric Tree
# Pattern Used: Recursion
# Time Complexity: O(N)
# Space Complexity: O(N)
# Short Explanation: We use recursion to check if the tree is symmetric. 
#                    We first check if the root is None. If it is, we return True. 
#                    Then we check if the left and right subtrees are mirrors of each other.
# LeetCode Link: https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def is_mirror(n1, n2):
            if not n1 and not n2:
                return True
            
            if not n1 or not n2:
                return False

            return n1.val == n2.val and is_mirror(n1.left, n2.right) and is_mirror(n1.right, n2.left)

        return is_mirror(root.left, root.right)