from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        # a, b, c, d must be distinct but can be a dup of each other
        # [-2, -1, 0, 0, 1, 2] target = 0
        n = len(nums)
        res = set()
        for i in range (0, n - 3):
            for j in range (i + 1, n - 2):
                left, right = j + 1, n - 1
                while left < right:
                    curr = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if curr < target:
                        left += 1
                    elif curr > target:
                        right -= 1
                    else:
                        path = (nums[i], nums[j], nums[left], nums[right])
                        res.add(path)
                        left += 1
                        right -= 1
        return [list(x) for x in res]
    
# O(nlogn + n**3) SOS
                        