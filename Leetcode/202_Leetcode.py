class Solution:
    def isHappy(self, n: int) -> int:
        n = str(n)
        seen = set()
        
        while n not in seen:
            seen.add(n)
            res = 0
            for x in n:
                res += (int(x) ** 2)
            if n == '1':
                return True
        return False