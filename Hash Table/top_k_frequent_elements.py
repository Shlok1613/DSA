# Problem Name: Top K Frequent Elements
# Pattern Used: Hash Table with Heap
# Time Complexity: O(N log k)
# Space Complexity: O(N)
# Short Explanation: We use a hash table to count the frequency of each element in the array. 
#                    Then, we use a heap to efficiently retrieve the k most frequent elements.
# LeetCode: https://leetcode.com/problems/top-k-frequent-elements/

import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        top_k = heapq.nlargest(k, freq, key=freq.get)
        return top_k
        