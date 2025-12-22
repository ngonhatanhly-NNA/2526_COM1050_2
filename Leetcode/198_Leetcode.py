from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        # Base case
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        # Lưu các giá trj của case mua và không mua trước xem cái nào lớn hơn, tìm lớn nhất cho đến thời dểm hiện tại
        # nếu case trước có không mua lớn hơn thì sau không bị ảnh hưởng vì dù gì nõ cũng đã mua ở caase hiện tại
        secondLast = 0
        last = nums[0]

        for i in range (1, n):
            res = max(nums[i] + secondLast, last)
            secondLast = last
            last = res
        
        return res
        