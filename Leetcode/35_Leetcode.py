class Solution(object):
    def searchInsert(self, nums, target):   
        nums.sort()
        if target in nums:
            return nums.index(target)
        elif nums[0] > target:
            return 0
        else:
            for num in nums:
                if num < target:
                    i = nums.index(num) + 1
            return i 