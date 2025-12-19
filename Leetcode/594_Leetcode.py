from typing import List
class Solution:
    def findLHS(self, nums: List[int])-> int:
        has = {}
        for num in nums:
            if num not in has:
                has[num] = 1
            else:
                has[num] += 1
        
        max_seq = 0
        for key in has.keys():
            if key - 1 in has:
                max_seq = max(has[key] + has[key - 1], max_seq)
        return max_seq
