# Problem Name: Maximum Depth of Binary Tree
# Pattern Used: Breadth First Search (BFS)
# Time Complexity: O(N)
# Space Complexity: O(N)
# Short Explanation: We use BFS to traverse the tree level by level. We maintain a queue of nodes to visit. In each iteration, 
#                    we process all nodes at the current level and add their children to the queue. 
#                    The number of levels we process is the maximum depth of the tree.
# LeetCode Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/

from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        res = 0
        queue = deque([root])

        while queue:
            res += 1
            for _ in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return res
