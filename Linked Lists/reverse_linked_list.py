# Problem Name: Reverse Linked List
# Pattern Used: Iterative Linked List Reversal
# Time Complexity: O(N)
# Space Complexity: O(1)
# Short Explanation: We iterate through the linked list, reversing the pointers of each node to point to the previous node.
# LeetCode: https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev
        