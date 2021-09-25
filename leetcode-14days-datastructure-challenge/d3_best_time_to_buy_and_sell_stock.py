# Best Time to Buy and Sell Stock
def maxProfit(self, prices: List[int]) -> int:
    local_max = max_profit = 0
    buy, sell = 0, 1
    
    while sell < len(prices):
        if prices[buy] > prices[sell]:
            buy = sell
            sell += 1
        else:
            local_max = prices[sell] - prices[buy]
            max_profit = max(max_profit, local_max)
            sell += 1
    
    return max_profit