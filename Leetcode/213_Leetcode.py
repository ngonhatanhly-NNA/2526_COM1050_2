from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 0: return 0
        if n <= 3: return max(nums)
        # Since and the first house and the last house can't be with together
        # We find in two direction, one with first house and one with last house
        secondLast = 0
        Last = nums[0]
        for i in range (1, n-1):
            res1 = max(secondLast + nums[i], Last)
            secondLast = Last
            Last = res1

        secondLast = 0
        Last = nums[-1]
        for i in range (n-2,0, -1):
            res2 = max(secondLast + nums[i], Last)
            secondLast = Last
            Last = res2

        return max(res1, res2)


        