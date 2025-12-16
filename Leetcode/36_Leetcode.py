class Solution:
    def isValidSudoku(self, board):
        rows = [set() for _ in range (9)]
        cols = [set() for _ in range (9)]
        subs = [set() for _ in range (9)]

        for i in range (9):
            for j in range (9):
                val = board[i][j]
                # ROWS CHECK
                if val == '.' or val == 0:
                    continue  # break this val and go to next
                if val in rows[i]:
                    return False
                rows[i].add(val)
                # COLS CHECK
                if val in cols[j]:
                    return False
                cols[j].add(val)                
                # Calculate sub
                # 0 1 2 0 1 2 0 1 2
                # 3 4 5 3 4 5 3 4 5
                # 6 7 8 6 7 8 6 7 8 
                # 0 1 2 0 1 2 0 1 2
                # 3 4 5 3 4 5 3 4 5
                # 6 7 8 6 7 8 6 7 8 
    # If 5 in the 0 index, so the remaining 5 can't be in the 0 index, it mst be separated from 0 -> 8

                index = ( i // 3) * 3 + (j // 3) 
                if val in subs[index]:
                    return False
                subs[index].add(val)

        return True
