#Problem Name: Group Anagrams
#Pattern Used: Hash Table
#Time Complexity: O(n * k log k) where n is the number of strings and k is the maximum length of a string
#Space Complexity: O(n * k)
#Short Explanation: We use a hash table to group words by their sorted character sequences.
#LeetCode: https://leetcode.com/problems/group-anagrams/

from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)

        for word in strs:
            sorted_word = "".join(sorted(word))
            anagram_map[sorted_word].append(word)

        return list(anagram_map.values())
