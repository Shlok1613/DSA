#Problem Name: Longest Common Prefix
#Pattern Used: Horizontal Scanning
#Time Complexity: O(S) where S is the sum of all characters in all strings
#Space Complexity: O(1)
#Short Explaination: We start with the first string as the initial prefix. 
#                    For each subsequent string, we compare it with the current prefix and shorten the prefix until 
#                    it matches the start of the string. 
#                    If at any point the prefix becomes empty, we return an empty string.
#LeetCode: https://leetcode.com/problems/longest-common-prefix/


class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        prefix = strs[0]
        for string in strs[1:]:
            while string.find(prefix) != 0:
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix