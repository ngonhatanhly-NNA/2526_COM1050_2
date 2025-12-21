# isomorphic: đẳng hình
# Ánh xạ đẳng cấu, phản ánh xạ không đc là nghiệm khác

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        replacement = {}
        im_seen = set()
        for i in range (len(s)):
            if s[i] in replacement:
                if t[i] != replacement[s[i]]:
                    return False
            else:
                if t[i] in im_seen:
                    return False
                replacement[s[i]] = t[i]
                im_seen.add(t[i])
        return True
        