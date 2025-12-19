
from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        seen = set(nums)

        for i in range (1, n + 1):
            if i not in seen:
                res.append(i)
        return res