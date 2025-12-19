class Solution(object):
    def firstUniqChar(self, s):
        seen = {}
        for char in s:
            if char in seen:
                seen[char] = False
            else:
                seen[char] = True

        for char in s:
            if seen[char]:              # nghĩa là True
                return s.index(char)
        return -1
        """
        :type s: str
        :rtype: int
        """
        