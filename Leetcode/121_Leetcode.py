class Solution(object):
    def maxProfit(self, prices):
        min_price = float('inf')   # giá thấp nhất từ đầu đến nay
        max_profit = 0             # lợi nhuận lớn nhất tìm được
        for price in prices:
            min_price = min(min_price, price)       # cập nhật giá thấp nhất
            max_profit = max(max_profit, price - min_price)  # lợi nhuận nếu bán hôm nay
        return max_profit
        """
        :type prices: List[int]
        :rtype: int
        """
        