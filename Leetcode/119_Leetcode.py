from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = [[] for _ in range (rowIndex + 1)]

        triangle[0].append(1)
        for i in range (1, rowIndex + 1):
            for j in range (0, i + 1):
                if j == i or j == 0:
                    triangle[i].append(1)
                else:
                    curr = triangle[i-1][j] + triangle[i-1][j-1]
                    triangle[i].append(curr)

        return triangle[rowIndex]