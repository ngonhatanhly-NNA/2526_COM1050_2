from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # Find the gap where is break
        n = len(nums)
        if n == 1:
            return target == nums[0]        
        for i in range (n):
            if i == n - 1:
                mid = i
            if nums[i-1] > nums[i]:
                mid = i
                break

        
        left, right = 0, n - 1
        endl, start = mid - 1, mid
        # Check for the first else second
        # Check where the target at
        while start <= right:
            mid = (right + start) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                return True
        while left <= endl:
            mid = (left + endl) // 2
            if nums[mid] > target:
                endl = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return True
        return False
        
        