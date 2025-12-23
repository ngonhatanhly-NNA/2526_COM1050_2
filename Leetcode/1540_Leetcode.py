
class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        if len(s) != len(t):
            return False
        
        counts = [0] * 26

        for s1, t1 in zip(s, t):
            if s1 == t1:
                continue
            diff = (ord(t1) - ord(s1)) % 26
            needed_move = diff + (counts[diff] * 26)# 
            if needed_move > k:
                return False
            counts[diff] += 1
        return True