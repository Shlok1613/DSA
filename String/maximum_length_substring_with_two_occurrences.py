#Problem Name: Maximum Length Substring with Two Occurrences
#Pattern Used: Sliding Window / Hash Map
#Time Complexity: O(n)
#Space Complexity: O(n) for the hash map
#Short Explanation: We use a sliding window approach to maintain a substring with at most two occurrences of each character.
#                   We use a hash map to count the occurrences of each character in the current window.
#                   If a character exceeds two occurrences, we shrink the window from the left until the condition is satisfied.
#LeetCode: https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        count = 0
        number = {}

        i = 0

        for j, letter in enumerate(s):
            number[letter] = number.get(letter, 0) + 1

            if number[letter] > 2:
                while s[i] != letter:
                    number[s[i]] -= 1
                    i += 1

                number[s[i]] -= 1
                i += 1

            count = max(count, j - i + 1)

        return count