from typing import List
# Greedy

class Solution:
    def canJump (self, nums: List[int]) -> bool:
        maxi = 0
        
        for step in range (len(nums)):
            if step > maxi:
                return False
            
            maxi = max(maxi, step + nums[step])
            if maxi + 1 >= len(nums):
                return True
            
        return False