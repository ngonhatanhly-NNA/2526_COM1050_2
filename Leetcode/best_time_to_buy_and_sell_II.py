class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        if n < 2:
            return 0
        
        profit, i = 0,  0
        while i < n - 1:
            while i < n - 1 and prices[i] >= prices[i + 1]:
                i += 1
            buy = i
            while i < n - 1 and prices[i] < prices[i + 1]:
                i += 1
            sell = i

            if prices[sell] - prices[buy] > 0:
                profit = profit + prices[sell] - prices[buy]
        return profit