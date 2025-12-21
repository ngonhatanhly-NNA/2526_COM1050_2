class Solution:
    def search(self, pat, txt):
        # code here
        
        n, m = len(txt), len(pat)
        lps = self.KMP_Algorithm(pat)
        if m == 0:
            return res
            
        i, j = 0, 0
        
        res = []
        while i < n:
            if txt[i] == pat[j]:
                i += 1
                j += 1
            
                if j == m:
                    res.append(i - j)
                    j = lps[j-1] # Allow for overlap amtch like 'aaaa' -> 'aaaaa'
            elif i < n and txt[i] != pat[j]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
                  
                    
        return res
        
        
    def KMP_Algorithm(self, pat):
        n = len(pat)
        lps = [0] * n
        
        patLen = 0
        i = 1
        
        while i < n:
            if pat[i] == pat[patLen]:
                patLen += 1
                lps[i] = patLen
                i += 1
            else:
                if patLen != 0:
                    patLen = lps[patLen - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

class Solution1:
    def KMPAlgorithm(self, pat):
        n = len(pat)
        lps = [0] * n

        i = 1
        patLen = 0
        while i < n:
            if pat[i] == pat[patLen]:
                patLen += 1
                lps[i] = patLen
                i += 1
            else:
                if patLen != 0:
                    patLen = lps[patLen - 1]
                else:
                    lps[i] = 0
                    i += 1
        return pat

    def minChar(self, s):
        n = len(s)
        rev = s[::-1]

        s = s + '$' + rev
        lps = self.KMPAlgorithm(s)

        return n - lps[-1] 
