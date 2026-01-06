#Problem Name: Search Insert Position
#Pattern Used: Binary Search
#Time Complexity: O(log n)
#Space Complexity: O(1)
#Short Explaination: We use binary search to find the position where the target should be inserted.
#                    If the target is found, we return its index.
#                    Otherwise, we return the index where it should be inserted.
#LeetCode: https://leetcode.com/problems/search-insert-position/

class Solution(object):
    def searchInsert(self, nums, target):
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (r +l) // 2

            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid -1
        else:
            return l