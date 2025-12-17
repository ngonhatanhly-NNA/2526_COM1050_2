from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        return [self.searchFirst(nums, target), self.searchLast(nums, target)]

    def searchLast(self, nums, target):
        n = len(nums)
        last = -1
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                last = mid
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return last

    def searchFirst(self, nums, target):
        n = len(nums)
        first = -1
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                first = mid
                right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return first