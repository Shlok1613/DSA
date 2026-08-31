# Problem Name: Find the Minimum and Maximum Number of Nodes Between Critical Points
# Pattern Used: Linked List
# Time Complexity: O(n)
# Space Complexity: O(1)
# Short Explanation: We traverse the linked list to find the critical points (local maxima and minima) and store their positions.
#                    We then calculate the minimum and maximum distances between these critical points.
#                   If there are less than two critical points, we return [-1, -1]. 
#                   Otherwise, we return the minimum and maximum distances between the critical points.
# LeetCode Link: https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        result = [-1,-1]

        curr = head.next
        prev = head

        points = []
        pos = 2

        while curr.next:
            if curr.val > prev.val and curr.val > curr.next.val:
                points.append(pos)
            elif curr.val < prev.val and curr.val < curr.next.val:
                points.append(pos)

            pos += 1
            prev = curr
            curr = curr.next

        if len(points) < 2:
            return result

        result[1] = points[-1] - points[0]
        result[0] = points[-1] - points[0]

        for i in range(1,len(points)):
            minimum = points[i] - points[i-1]
            result[0] = min(minimum, result[0])
        
        return result