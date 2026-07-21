# Problem Name: Maximize Active Section with Trade I
# Pattern Used: Greedy
# Time Complexity: O(n)
# Space Complexity: O(1)
# Short Explanation: We iterate through the string while maintaining a count of the number of '1's and the lengths of consecutive '0's between them.
#                   We keep track of the maximum number of active sections we can achieve by trading a '0' for a '1' in the string.
# LeetCode: https://leetcode.com/problems/maximize-active-section-with-trade-i/

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        ones = s.count("1")

        s = "1" + s + "1"

        n = len(s)
        i = 0

        ans = ones

        while i < n and s[i] == "1":
            i += 1

        c10 = 0
        while i < n and s[i] == "0":
            c10 += 1
            i += 1

        while i < n:
            c11 = 0
            while i < n and s[i] == "1":
                c11 += 1
                i += 1

            if c11 == 0:
                break

            c20 = 0
            while i < n and s[i] == "0":
                c20 += 1
                i += 1

            if c20 == 0:
                break 

            ans = max(ans, ones + c10 + c20)

            c10 = c20

        return ans 
