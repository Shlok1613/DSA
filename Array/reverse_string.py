#Problem Name: Reverse String
#Pattern Used: Two Pointers
#Time Complexity: O(n)
#Space Complexity: O(1)
#Short Explanation: We use two pointers, one starting at the beginning of the array and the other at the end.
#                   We swap the characters at these pointers and then move the pointers towards each other until they meet in the middle.
#LeetCode: https://leetcode.com/problems/reverse-string/

class Solution(object):
    def reverseString(self, s):
        j = -1
        for i in range(int(len(s) / 2)):
            s[i], s[j] = s[j], s[i]
            j -= 1

        return s
        