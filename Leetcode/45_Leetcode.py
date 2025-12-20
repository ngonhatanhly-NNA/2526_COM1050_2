from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int: 
        n = len(nums)
        # Base case
        if n <= 1:
            return 0
        elif nums[0] == 0: # can't jump
            return -1
        
        jump = 1
        maxReach, steps = nums[0], nums[0]

        for i in range(1, n):
            
            maxReach = max(maxReach, i + nums[i])
            steps -= 1
            # If reach case
            if i == n - 1:
                return jump
            
            elif steps == 0:
                jump += 1
                if maxReach <= i:
                    return -1
                steps = maxReach - i
        return -1
        