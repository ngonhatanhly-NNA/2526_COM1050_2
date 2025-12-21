from typing import List

import math
from functools import reduce
class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        # if numebr of negative is even -> we take all else we take only only 2 of them
        # take consecutive positive, we can skip
        positives = [n for n in nums if n > 0]
        negatives = sorted([n for n in nums if n < 0])

        if len(negatives) % 2 != 0:
            negatives.pop()

        candidates = positives + negatives
        # Handle case 0 -1
        if not candidates:
            return max(nums)
        return math.prod(candidates)
        
     
