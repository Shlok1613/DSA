# Problem Name: Same Tree
# Pattern Used: Breadth First Search (BFS)
# Time Complexity: O(N)
# Space Complexity: O(N)
# Short Explanation: We use BFS to traverse the tree level by level. We maintain a queue of nodes to visit. 
#                    In each iteration,we process all nodes at the current level and add their children to the queue. 
#                    The number of levels we process is the maximum depth of the tree.
# LeetCode Link: https://leetcode.com/problems/same-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (not p and q) or (p and not q):
            return False
        if not p and not q:
            return True


        p_queue = deque([p])
        q_queue = deque([q])

        while p_queue and q_queue:
            for _ in range(len(p_queue)):
                node_p = p_queue.popleft()
                node_q = q_queue.popleft()

                if node_p.val != node_q.val:
                    return False
                
                if (node_p.left and not node_q.left) or (not node_p.left and node_q.left) or (node_p.right and not node_q.right) or (not node_p.right and node_q.right):
                    return False 
                if node_p.left:
                    p_queue.append(node_p.left)
                if node_p.right:
                    p_queue.append(node_p.right)
                if node_q.left:
                    q_queue.append(node_q.left)
                if node_q.right:
                    q_queue.append(node_q.right)

        return True

############ Shorter Code ###############

# Pattern Used: Recursion
# Time Complexity: O(N)
# Space Complexity: O(N)
# Short Explanation: We use recursion to check if the two trees are identical. 
#                    We first check if both nodes are None, if so, they are identical. 
#                    Then we check if one is None but the other isn't, or if their values differ, if so, they aren't identical. 
#                    Finally, we recursively check the left and right subtrees.
# LeetCode Link: https://leetcode.com/problems/same-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 1. If both nodes are None, they are identical
        if not p and not q:
            return True
        
        # 2. If one is None but the other isn't, or values differ, they aren't identical
        if not p or not q or p.val != q.val:
            return False
        
        # 3. Recursively check left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        