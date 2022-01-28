# Best Time to Sell Stock (leetcode)


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
    
        # initialize buy and profit
        buy, profit = float('inf'), 0
        
        # profit = price - buy
        for i, price in enumerate(prices):
            if buy > price:
                buy = price
            if buy < price:
                profit = max(price - buy, profit)
        
        return profit