class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n == 1:
            return 0 
        if n == 2: 
            return max(0, prices[1] - prices[0])
        
        total = 0 
        positive = 0 
        left = 0
        right = 0 
        while right <= (n-1): 
            while left < (n-2) and prices[left+1] < prices[left]: 
                left += 1 
            right = left + 1 
            while right <= (n-1) and prices[right] > prices[right-1]:
                diff = prices[right] - prices[right-1]
                if diff > 0: 
                    positive += diff
                right += 1 
            total += positive
            positive = 0 
            left = right 
        return total 



        