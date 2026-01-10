#Problem Name: Valid Anagram
#Pattern Used: Hash Map / Counting
#Time Complexity: O(n)
#Space Complexity: O(1)
#Short Explanation: We count the occurrences of each character in both strings and compare the counts. 
#                   If they match for all characters, the strings are anagrams.
#LeetCode: https://leetcode.com/problems/valid-anagram/

class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        for char in set(s):
            if s.count(char) != t.count(char):
                return False

        return True 