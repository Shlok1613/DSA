# Problem Name: Longest Palindromic Substring
# Pattern Used: Dynamic Programming / Manacher's Algorithm
# Time Complexity: O(n)
# Space Complexity: O(n)
# Short Explanation: We use Manacher's algorithm to find the longest palindromic substring in linear time. 
#                    We preprocess the string by inserting '#' between characters to handle even-length palindromes uniformly.
#                    We maintain an array to store the radius of the palindrome centered at each character and update the center   
#                    and right boundary as we iterate through the string.
# LeetCode: https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        
        Max_Len=1
        Max_Str=s[0]
        s = '#' + '#'.join(s) + '#'
        dp = [0 for _ in range(len(s))]
        center = 0
        right = 0
        for i in range(len(s)):
            if i < right:
                dp[i] = min(right-i, dp[2*center-i])
            while i-dp[i]-1 >= 0 and i+dp[i]+1 < len(s) and s[i-dp[i]-1] == s[i+dp[i]+1]:
                dp[i] += 1
            if i+dp[i] > right:
                center = i
                right = i+dp[i]
            if dp[i] > Max_Len:
                Max_Len = dp[i]
                Max_Str = s[i-dp[i]:i+dp[i]+1].replace('#','')
        return Max_Str