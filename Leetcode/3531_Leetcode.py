from typing import List
from collections import defaultdict
class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        # Given an matrix of size n * n
        # Check if the point have left, right, up, down, it have one same attribute and larger, smaller in the other
        # With same rolw, check if it has smaller col and larger col
        # With same col, check if has smaller row and larger row
        # Row X: 1 2 3 2 2
        # Col Y: 2 2 2 1 3
       
        row = defaultdict(list)
        col = defaultdict(list)
        
        condition = False
        cnt = 0

        row_min_max = {}
        col_min_max = {}
        
        for x, y in buildings:
            row[x].append(y) # [2: [2, 1, 3]] [1: 2] [3: 2]
            col[y].append(x) # [2: [2, 3, 1]]

        for x, y in row.items():
            row_min_max[x] = (min(y), max(y))
        for y, x in col.items():
            col_min_max[y] = (min(x), max(x))
        
        for x, y in buildings:
            # Check for x row, if exist smaller value and larger value
            min_y, max_y = row_min_max[x]
            min_x, max_x = col_min_max[y]
            if y != min_y and y != max_y and x != min_x and x != max_x:
                condition = True
            if condition:
                cnt += 1
                condition = False
        return cnt
        