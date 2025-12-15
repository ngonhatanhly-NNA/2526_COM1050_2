from collections import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort() # -4 -1 1 2
        n = len(nums)
        closest_sum = nums[0] + nums[1] + nums[2]

        for i in range (0, n - 2):
            left, right = i + 1, n - 1
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                if abs(curr_sum - target) < abs(closest_sum - target):
                    closest_sum = curr_sum
                if curr_sum < target:
                    left += 1
                elif curr_sum > target:
                    right -= 1
                else:
                    return curr_sum

        return closest_sum

        