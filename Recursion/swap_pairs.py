# Problem Name: Swap Nodes in Pairs
# Pattern Used: Recursion
# Time Complexity: O(n)
# Space Complexity: O(n) due to recursion stack
# Short Explanation: We recursively swap pairs of nodes by adjusting their next pointers.
# LeetCode: https://leetcode.com/problems/swap-nodes-in-pairs/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from ast import Optional
from typing import ListNode

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        first = head
        second = head.next
        first.next = self.swapPairs(second.next)
        second.next = first

        return second
