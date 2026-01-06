#Problem Name: Best Time to Buy and Sell Stock
#Pattern Used: Array Manipulation
#Time Complexity: O(n)
#Space Complexity: O(1)
#Short Explanation: We track the minimum price to buy the stock and calculate the maximum profit by selling at the current price.
#LeetCode: https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution(object):
    def maxProfit(self, prices):
        buy = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            if prices[i] - buy > profit:
                profit = prices[i] - buy
        return profit