#Problem Name: Remove Nth Node From End of List
#Pattern Used: Two Pointer Technique
#Time Complexity: O(N)
#Space Complexity: O(1)
#Short Explanation: We use two pointers to find the nth node from the end of the list in a single pass. 
#LeetCode: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        fast, slow = head, head

        for _ in range(n):
            fast = fast.next

        if not fast:
            return head.next

        while fast.next:
            slow, fast = slow.next, fast.next

        slow.next = slow.next.next
        return head