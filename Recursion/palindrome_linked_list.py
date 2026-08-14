#Problem Name: Palindrome Linked List
#Pattern Used: Recursion / Two Pointers
#Time Complexity: O(n)
#Space Complexity: O(n) due to recursion stack
#Short Explanation: We use recursion to traverse to the end of the linked list, 
#                   then compare the values from the end back to the start with a left pointer that moves forward. 
#LeetCode: https://leetcode.com/problems/palindrome-linked-list/



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
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