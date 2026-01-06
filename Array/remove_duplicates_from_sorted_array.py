#Problem Name: Remove Duplicates from Sorted Array
#Pattern Used: Two Pointers
#Time Complexity: O(n)
#Space Complexity: O(1)
#Short Explaination: We use two pointers, one to track the position of the last unique element and another to iterate through the array.
#                    When we find a new unique element, we place it next to the last unique element and increment the pointer.
#                    Finally, we return the count of unique elements.
#LeetCode: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution(object):
    def removeDuplicates(self, nums):
        j = 0

        for i in range(1, len(nums)):
            if nums[j] != nums[i]:
                j += 1
                nums[j] = nums[i]
        return j + 1