
class Solution:
    def istringRotated(self, s1, s2):
        rotated = False
        for i in range (1, len(s1)):
            if s1[i:] + s1[:i] == s2:
                rotated = True
                break
        # Check vice versa
        s1_reversed = s1[::-1]
        if not rotated:
            for i in range (0, len(s1)):
                if s1_reversed[i:] + s1_reversed[:i] == s2:
                    rotated = True
                    break
        return rotated
    
s1 = 'kllkl' # -> lkllk
s2 = 'kllkl'

print(Solution().istringRotated(s1, s2))