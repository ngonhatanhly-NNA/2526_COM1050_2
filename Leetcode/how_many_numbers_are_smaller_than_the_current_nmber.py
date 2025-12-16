from typing import List
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        for i in range (len(nums)):
            cnt = 0
            for j in range (len(nums)):
                if i == j:
                    continue
                if nums[i] > nums[j]:
                    cnt += 1
            res[i] = cnt
        return res 
        
        