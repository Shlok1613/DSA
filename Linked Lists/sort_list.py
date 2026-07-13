# Problem Name: Sort List
# Pattern Used: Merge Sort
# Time Complexity: O(N log N)
# Space Complexity: O(log N)
# Short Explanation: We use merge sort to sort the linked list. We first find the middle of the linked list and split it into two halves. 
#                    Then we recursively sort both halves and merge them.
# LeetCode Link: https://leetcode.com/problems/sort-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        # Find the middle of the linked list 
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow.next
        slow.next = None
        
        # Sort both halves
        left = self.sortList(head)
        right = self.sortList(mid)
        
        return self.merge(left, right)
    
    def merge(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        tail = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        
        tail.next = l1 if l1 else l2
        return dummy.next