1class Solution:
2    def maxProfit(self, prices: list[int]) -> int:
3        profit = 0 
4        min_price = prices[0]
5        for price in prices:
6            if price < min_price:
7                min_price = price
8            elif price - min_price > profit:
9                profit = price - min_price
10
11        return profit 
12