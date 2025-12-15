from collections import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return
        rows, cols = len(matrix), len(matrix[0])

        col0_zero = False
        for i in range (rows):
            # If 0 is at border then col0_zero is true, we will change col 0 and the row that store that index
            if matrix[i][0] == 0:
                col0_zero = True
            # Save the place where have 0 inside and set border for it
            for j in range (1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range (1, rows):
            for j in range (1, cols):
                # If its border equal 0, it means that you are 0
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        # Handle case 0 at the border
        # Rows
        if matrix[0][0] == 0:
            for j in range (cols):
                matrix[0][j] = 0
        # Cols
        if col0_zero:
            for i in range (rows):
                matrix[i][0] = 0