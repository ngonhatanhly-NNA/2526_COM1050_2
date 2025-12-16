from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n - 1

        maxArea = float('-inf')
        while left < right:
            height_choosen = min(height[left], height[right])
            Area = height_choosen * (right - left)
            
            maxArea = max(Area, maxArea)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxArea