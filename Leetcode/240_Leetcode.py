from typing import List
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        for i in range (rows):
            left, right = 0, cols - 1
            while left <= right:
                mid = (left + right) // 2
                if matrix[i][mid] > target:
                    right = mid - 1
                elif matrix[i][mid] < target:
                    left = mid + 1
                else:
                    return True
        return False
        