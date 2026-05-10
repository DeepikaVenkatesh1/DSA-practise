def maxProfit(prices):
    mini = prices[0]
    profit = 0
    for p in prices:
        mini = min(mini, p)
        profit = max(profit, p - mini)
    return profit
print(maxProfit([7,1,5,3,6,4]))