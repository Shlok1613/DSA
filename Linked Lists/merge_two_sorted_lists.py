#Problem Statement: Merge Two Sorted Lists
#Pattern Used: Linked List Manipulation
#Time Complexity: O(n + m) where n and m are the lengths of the two lists
#Space Complexity: O(1) - we are not using any extra space for another list
#Short Explanation: We use a dummy head to simplify the merging process. 
#                   We iterate through both lists, comparing the current nodes and appending the smaller one to the merged list. 
#                   Once we reach the end of one list, we append the remaining nodes of the other list.
#LeetCode: https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        head = ListNode()
        current = head
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        current.next = list1 or list2
        return head.next

        
        