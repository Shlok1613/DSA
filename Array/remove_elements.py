#Problem Name: Remove Element
#Pattern Used: Two Pointers
#Time Complexity: O(n)
#Space Complexity: O(1)
#Short Explaination: We use two pointers, one to iterate through the array and another to track the position of the next non-val element.
#                    When we find an element that is not equal to val, we place it at the position of the second pointer and increment the pointer.
#                    Finally, we return the count of elements that are not equal to val.
#LeetCode: https://leetcode.com/problems/remove-element/

class Solution(object):
    def removeElement(self, nums, val):
        j=0
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j