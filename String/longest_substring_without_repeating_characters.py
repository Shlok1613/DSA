#Problem Name: Longest Substring Without Repeating Characters
#Pattern Used: Sliding Window
#Time Complexity: O(n)
#Space Complexity: O(min(m, n)) where m is the size of the character set and n is the length of the string
#Short Explanation: We use a sliding window approach to maintain a substring without repeating characters.
#LeetCode: https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left = max_length = 0
        char_set = set()

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)
        
        return max_length