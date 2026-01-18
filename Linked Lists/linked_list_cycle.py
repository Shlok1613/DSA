# Problem Name: Linked List Cycle
# Pattern Used: Floyd's Tortoise and Hare (Cycle Detection)
# Time Complexity: O(N)
# Space Complexity: O(1)
# Short Explanation: We use two pointers moving at different speeds to detect a cycle in the linked list.
# LeetCode: https://leetcode.com/problems/linked-list-cycle/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        try:
            slow = head
            fast = head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False