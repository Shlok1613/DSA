# Problem Name: Binary Tree Level Order Traversal
# Pattern Used: Breadth First Search (BFS)
# Time Complexity: O(N)
# Space Complexity: O(N)
# Short Explanation: We use BFS to traverse the tree level by level. We maintain a queue of nodes to visit. In each iteration, 
#                    we process all nodes at the current level and add their children to the queue. 
#                    The number of levels we process is the maximum depth of the tree.
# LeetCode Link: https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        queue = deque([root])

        while queue:
            numbers = []
            level = len(queue)

            for _ in range(level):
                node = queue.popleft()
                numbers.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(numbers)

        return res