from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)

        i, res = 0, []
        while i < n:
            start = nums[i]
            while i + 1 < n and nums[i + 1] == nums[i] + 1:
                i += 1
            if start == nums[i]:
                res.append(str(start))
                
            else:
                res.append(f"{start}->{nums[i]}")
            i += 1
        return res
        
        
                                                     