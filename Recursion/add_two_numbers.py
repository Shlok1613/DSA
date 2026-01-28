# Problem Name: Add Two Numbers
# Pattern Used: Recursion
# Time Complexity: O(max(m, n)) where m and n are the lengths of the two linked lists
# Space Complexity: O(max(m, n)) due to the recursion stack
# Short Explanation: We use a recursive helper function to add corresponding nodes from both linked lists along with any carry from the previous addition.
#                    The base case handles when both nodes are None and there's no carry left.
#                    We create a new node for each sum and recursively call the function for the next nodes.
# LeetCode: https://leetcode.com/problems/add-two-numbers/


# # Definition for singly-linked list.
# # class ListNode:
# #     def __init__(self, val=0, next=None):
# #         self.val = val
# #         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def dfs(n1, n2, carry):
            if not n1 and not n2 and carry == 0:
                return None

            v1 = n1.val if n1 else 0
            v2 = n2.val if n2 else 0

            total = v1 + v2 + carry
            node = ListNode(total % 10)
            node.next = dfs(
                n1.next if n1 else None,
                n2.next if n2 else None,
                total // 10
            )
            return node

        return dfs(l1, l2, 0)