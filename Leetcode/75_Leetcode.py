class Solution(object):
    def sortColors(self, nums):
        cnt_0 = 0
        cnt_1 = 0
        cnt_2 = 0
        arr = []
        for num in nums:
            if num == 0:
                cnt_0 += 1
            elif num == 1:
                cnt_1 += 1
            elif num == 2:
                cnt_2 += 1
        idx = 0
        for _ in range (cnt_0):
            nums[idx] = 0
            idx += 1
        for _ in range (cnt_1):
            nums[idx] = 1
            idx += 1
        for _ in range (cnt_2):
            nums[idx] = 2
            idx += 1
        return nums