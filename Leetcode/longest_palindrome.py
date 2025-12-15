from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        count = Counter(s)

        if len(count) == 1:
            return len(s)
        
        res = 0
        has_1 = False
        for value in count.values():
            res += (value // 2) * 2

            if value % 2 == 1:
                has_1 = True
        if has_1:
            return res + 1
        return res

