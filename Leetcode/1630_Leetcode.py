from typing import List
# Arithmetic subarray là aray thỏa mãn là cấp số cộng khi rearrange
# Brute force n * nlogn * n

class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        n = len(l)
        res = []
        for i in range (n):
            sub = sorted(nums[l[i]: r[i] + 1])
            is_arithmetic = True

            if len(sub) >= 2:
                gap = sub[1] - sub[0]
                for j in range (2, len(sub)):
                    if sub[j] - sub[j-1] != gap:
                        is_arithmetic = False
                        break
            res.append(is_arithmetic)
        return res
        