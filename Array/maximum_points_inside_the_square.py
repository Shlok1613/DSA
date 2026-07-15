#Problem Name: Maximum Points Inside the Square
#Pattern Used: Array
#Time Complexity: O(n)
#Space Complexity: O(n)
#Short Explanation: We use a hash table to store the first occurrence of each character and then find the maximum number of points inside the square.
#LeetCode: https://leetcode.com/problems/maximum-points-inside-the-square/

from ast import List
import math
class Solution:
    def maxPointsInsideSquare(self, points: List[List[int]], s: str) -> int:
        first = {}
        limit = math.inf

        for i, (x,y) in enumerate(points):
            d = max(abs(x), abs(y))
            ch = s[i]

            if s[i] in first:
                limit = min(limit, max(d, first[ch]))
                first[ch] = min(first[ch], d)
            else:
                first[s[i]] = d

        ans = 0

        for x,y in points:
            if max(abs(x), abs(y)) < limit:
                ans += 1

        return ans