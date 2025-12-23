class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        cnt = 0
        res = x ^ y
        while res > 0:
            if res&1:
                cnt += 1
            res >>= 1
        return cnt