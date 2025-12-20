from typing import List
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        # code here
            # 2n to circlar
        # [8 0 9 0 10 -1 11 20 12 21 12 22 11]
        n = len(nums)
        # Thuật toán Kadane, tìm dãy con có tổng xoay lớn nhất
        current_max = 0

        min_kadane = float('inf')
        current_min = 0
        
        total_sum = 0
        for x in nums:
            # Tổng cho tới hiện tại, tổng cua cả dãy
            total_sum += x
            # Tổng lớn nhất cho kết thúc tại vị trí hiện tại
            current_max += x
            # Tổng lớn nhất tìm thấy từ đầu mảng tới giờ
            max_kadane = max(max_kadane, current_max)

            if current_max < 0: current_max = 0
            # Giá trị nhr nhát kết thúc tại vị trí hiện tại
            current_min += x
            # Giá trị nhỏ nhất từ đầu tới giờ
            min_kadane = min(min_kadane, current_min)
            
            if current_min > 0: current_min = 0
        # Chuỗi âm
        if max_kadane < 0:
            return max_kadane
        return max(max_kadane, total_sum - min_kadane)
# VÌ sao trừ nhỏ nhất của từ đầu đến giờ ( xét trong bài toan xoay)
# [1, -2, 6] -> Lớn nhất sẽ là 7 nhưng có nhỏ nhất là -2 => sum + 2
