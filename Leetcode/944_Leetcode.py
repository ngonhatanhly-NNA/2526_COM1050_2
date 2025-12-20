from typing import List

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        delete = 0
        n = len(strs) 
        length = len(strs[0])
        for i in range (length):
            for j in range (1, n):
                if strs[j-1][i] > strs[j][i]:
                    delete += 1
                    break
        return delete
    
