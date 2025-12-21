from typing import List

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # We can see this pattern -> 10 5 2 6
        # 1 + 2 + 2 + 3

        n = len(nums)
        l, product = 0, 1
        res = 0

        for r in range(n):
            product *= nums[r]

            while l <= r and product >= k:
                product //= nums[l]
                l += 1
            res += (r - l + 1)

        return res 