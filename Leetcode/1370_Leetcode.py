class Solution:
    def sortString(self, s: str) -> str:
        s = list(s)
        arrange = set(s)
        res = ''
        while s:
            for c in sorted(arrange):
                if c in s:
                    res += c
                    s.remove(c)
            for c in sorted(arrange, reverse = True):
                if c in s:
                    res += c
                    s.remove(c)
        return res