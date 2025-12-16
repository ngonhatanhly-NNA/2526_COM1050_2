from typing import List

class Solution:

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows, cols = len(matrix), len(matrix[0])
        # Transpose the matrix then reverse
        for i in range (cols):
            for j in range (i + 1, rows):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range (rows):
            matrix[i] = matrix[i][::-1]
        return matrix
        