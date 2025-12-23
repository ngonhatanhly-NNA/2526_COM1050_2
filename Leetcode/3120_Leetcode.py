class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        # it must have 2 type if it want to be the special case
        # [0: [A, a] 1:[b, B]]
        cases = [[] for _ in range (26)]
        cnt = 0

        for c in word:
            if 'a' <= c <= 'z':
                index = ord(c) - ord('a')
            elif 'A' <= c <= 'Z':
                index = ord(c) - ord('A')
            if c in cases[index]:
                continue
            else:
                cases[index].append(c)
            
            if len(cases[index]) == 2:
                cnt += 1 
        return cnt