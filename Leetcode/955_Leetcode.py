from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        rows, cols = 0, 0

        res = 0
        is_sorted = [False] * rows

        for c in range (cols):
            # IF not already sorted and current char breaks the order
            # Lớn hơn thì bỏ được , nhưng nếu bằng mà phía sau thỏa man vẫn lớn hơn thì vẫn cháp nhận được -> strictly order 
            is_bad = False
            for i in range (rows - 1):
                if not is_sorted[i] and strs[i][c] > strs[i+1][c]:
                    is_bad = True
                    break
            
            if is_bad:
                res += 1
            else:
                 # Update is_sorted for rows that became strictly smaller in this column
                for i in range (rows - 1):
                    if strs[i][c] < strs[i+1][c]:
                        is_sorted = True
                    
                if all(is_sorted):
                    return res
        return res