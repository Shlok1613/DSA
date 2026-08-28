# Problem Name: String to Integer (atoi)
# Pattern Used: String
# Time Complexity: O(n)
# Space Complecxity: O(1)
# Short Explaination: The string is traversed and the number is formed by multiplying the previous number by 10 and adding the new digit.
# Leetcode: https://leetcode.com/problems/string-to-integer-atoi/description/

class Solution:
    def myAtoi(self, s: str) -> int:

        result = 0
        started = False
        sign = 1

        for i in s:

            if i == " " and not started:
                continue

            if i == "-" or i == "+":
                if started:
                    break

                if i == "-":
                    sign = -1

                started = True

            elif i.isdigit():
                result = result * 10 + int(i)
                started = True

            else:
                break

        result = result * sign

        if result > 2**31 - 1:
            return 2**31 - 1

        if result < -2**31:
            return -2**31

        return result