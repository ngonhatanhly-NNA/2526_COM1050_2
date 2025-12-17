class Solution:
    def stock_sell_max_one(self, prices):
        min_till_now = prices[0]
        res = 0

        for i in range (1, len(prices) - 1):
            min_till_now = min(prices[i], min_till_now)

            res = max(res, prices[i] - min_till_now)

        return res
    
    def stock_sell_max2(self, prices):
        n = len(prices)
        profit = [0] * n
        maxPrice = prices[-1]

        for i in range (n-2, -1, -1):
            maxPrice = max(prices[i], maxPrice)

            profit[i] = max(profit[i + 1], maxPrice - prices[i])

        res = 0
        minPrice = prices[0]
        for i in range(1, n):
            minPrice = min(minPrice, prices[i])
            res = max(res, profit[i] + (prices[i] - minPrice))

        return res