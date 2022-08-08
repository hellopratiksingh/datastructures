# Stock buy and sell - 1
# maximize your profit by choosing a single day to buy one stock 
# and choosing a different day in the future to sell that stock.

def maxProfit(prices):
    n = len(prices)
    min_sofar = prices[0]
    max_profit = 0
    for i in range(0, n):
        min_sofar = min(min_sofar, prices[i])
        profit = prices[i] - min_sofar
        max_profit = max(max_profit, profit)

    return max_profit


print(maxProfit(prices=[7, 1, 5, 3, 6, 4]))
