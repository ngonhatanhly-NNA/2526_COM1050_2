class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1 or len(s) < numRows:
            return s
        zigzag = [""] * numRows
        up = True
        current_row = 0
        for c in s:
            zigzag[current_row] += c
            
            if up:
                current_row += 1
            if not up:
                current_row -= 1
            if current_row == numRows - 1:
                up = False
            elif current_row == 0:
                up = True
        return "".join(zigzag)
