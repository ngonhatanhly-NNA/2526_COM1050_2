
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        start, end = 2, num

        while start <= end:
            mid = (start + end) // 2

            if num / mid == mid:
                return True
            elif num / mid < mid:
                end = mid - 1
            else:
                start = mid + 1
        return False
    