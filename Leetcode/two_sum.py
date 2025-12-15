class Solution(object):
    def twoSum (self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            curr = target - num
            if curr in seen:
                return [seen[curr], i]
            seen[num] = i
                

        