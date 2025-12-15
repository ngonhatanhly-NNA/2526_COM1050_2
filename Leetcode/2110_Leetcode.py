from typing import List
class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        n = len(prices)
        # if reach end or higher or equal, return 1 immediately
        cnt = 1
        check_smooth_descend = 1

        for i in range (1, n):
            if prices[i-1] - prices[i] == 1:
                check_smooth_descend += 1
            else:
                check_smooth_descend = 1
            cnt += check_smooth_descend
        return cnt