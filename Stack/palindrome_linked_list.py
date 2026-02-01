#Problem Name: Palindrome Linked List
#Pattern Used: Stack
#Time Complexity: O(n)
#Space Complexity: O(n)
#Short Explanation: We push all the values of the linked list onto a stack,
#                   then compare the values popped from the stack with the original list values.


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = []

        while head:
            stack.append(head.val)
            head = head.next
        
        return stack == stack[::-1]