#Problem Name: Remove Linked List Elements
#Pattern Used: Recursion
#Time Complexity: O(N)
#Space Complexity: O(N) - due to recursion stack
#Short Explanation: We recursively traverse the linked list, removing nodes that match the target value by adjusting pointers.
#LeetCode: https://leetcode.com/problems/remove-linked-list-elements/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None:
            return None

        head.next = self.removeElements(head.next, val)

        if head.val == val:
            return head.next
        else:
            return head

        