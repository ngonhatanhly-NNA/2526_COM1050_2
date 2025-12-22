class Solution:
    def maxScore(self, s: str) -> int:
        # O(n)
        n = len(s)
        prefix = [0] * n
        suffix = [0] * n
        # Count 0 as prefix as if lie on the left
        cnt_0, cnt_1 = 0, 0
        for i in range (n-1):
            if s[i] == '0':
                cnt_0 += 1
                prefix[i] = cnt_0
        for i in range(n-1, 0, -1):
            if s[i] == '1':
                cnt_1 += 1
                suffix[i] = cnt_1
        res = 0

        for i in range(n-1):
            res = max(res, prefix[i] + suffix[i+1])
        return res

class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        # We count number of 0 and 1 appears, that is also windows
        # it is always optimal for the left to be only 0 first
        # if on the left, the 0 otweight 1 -> we
        # the ones from the left have already been decremented -> that not te problem
        max_diff = float('-inf')
        
        zeros, ones = 0, 0
        for i in range (n - 1):
            if s[i] == '0':
                zeros += 1
            else:
                ones += 1
            
            max_diff = max(max_diff, zeros - ones)

        if s[-1] == '1':
            ones += 1
        return max_diff + ones





