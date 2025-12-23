from typing import List

class Solution:
    def countTriangles(self, nums: List[int]):
        res = 0
        nums.sort()

        for i in range (2, len(nums)):
            left, right = 0, i - 1

            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    res += right - left
                    right -= 1
                else:
                    left += 1
        return res