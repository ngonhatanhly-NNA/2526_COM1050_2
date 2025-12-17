from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n - 1
        
        while left < right:
            
            mid = (left + right) // 2
            if nums[mid] > nums[right]: # It mean that we are currently in two different array
                left = mid + 1 # And the right part is the part that cotains number less than current
            else:
                right = mid
        return nums[left]
    
class Solution2:
    def findMin(self, nums: List[int]) -> int:
        return min(nums)
