#Problem Name: Plus One
#Pattern Used: Array Manipulation
#Time Complexity: O(n)
#Space Complexity: O(1)
#Short Explaination: We iterate through the digits from right to left.
#                    If a digit is less than 9, we increment it and return the array.
#                    Otherwise, we set the digit to 0 and continue.
#                    If all digits are 9, we return a new array with 1 followed by zeros.
#LeetCode: https://leetcode.com/problems/plus-one/

class Solution(object):
    def plusOne(self, digits):
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits

            digits[i] = 0

        return [1] + digits