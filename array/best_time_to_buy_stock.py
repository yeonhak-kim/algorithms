# Best time to buy and sell stock

# given array of prices, index: day0, day1, day2, ... prices: stock price of that day
# find the maximum profit you can make by buying on one day and selling on another day.
# can't buy more than once.

def maxProfit(self, prices: List[int]) -> int:
    local_max = 0
    max_profit = 0
    
    i = 0
    j = 1
    
    while j < len(prices):
        if prices[i] > prices[j]:
            i = j
            j = i + 1
            continue
        
        if prices[i] < prices[j]:
            local_max = prices[j] - prices[i]
            if local_max > max_profit:
                max_profit = local_max
        
    
        j += 1
    return max_profit