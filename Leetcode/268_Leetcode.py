from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:    
        n = len(nums)
        
        curr = sum(nums)
        expected = (n + 1) * n // 2

        return expected - curr