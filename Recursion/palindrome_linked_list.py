#Problem Name: Palindrome Linked List
#Pattern Used: Recursion / Two Pointers
#Time Complexity: O(n)
#Space Complexity: O(n) due to recursion stack
#Short Explanation: We use recursion to traverse to the end of the linked list, 
#                   then compare the values from the end back to the start with a left pointer that moves forward. 
#LeetCode: https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.left = head

        def rec(right):
            if right is None:
                return True

            if not rec(right.next):
                return False
            
            is_equal = right.val == self.left.val
            self.left = self.left.next

            return is_equal
        
        return rec(head)
    
############################# OR #############################

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