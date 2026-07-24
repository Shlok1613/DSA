# Problem Name: Number of Unique XOR Triplets II
# Pattern Used: Hashing
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)
# Short Explanation: We first compute all unique XOR pairs from the input list and store them in a set. 
#                    Then, for each unique XOR pair, we compute the XOR with every element in the input list to find all unique triplets. 
#                    Finally, we return the count of unique triplets.
# LeetCode: https://leetcode.com/problems/number-of-unique-xor-triplets-ii/

from typing import List


class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        xy_pair = set()

        for x in nums:
            for y in nums:
                xy_pair.add(x^y)

        triplet = set()

        for xy in xy_pair:
            for z in nums:
                triplet.add(xy^z)

        return(len(triplet))

        
