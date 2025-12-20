class Solution:
    def rotateString(self, s1, s2):
        # code here
        if len(s1) != len(s2):
            return False
        text = s1 + s1
        pat = s2
        
        n, m = len(text), len(pat)
        i, j = 0, 0
        lps = self.KMP_Algorithm(pat)
        
        while i < n:
            if text[i] == pat[j]:
                i += 1
                j += 1
                
            if j == m:
                return True
            elif i < n and text[i] != pat[j]:
                if j != 0:
                    # lps luw trữ sự xuất hiện, lps j - 1 để for sure nó vào cái vòng lặp của số trc
                    j = lps[j-1]
                else:
                    i += 1
                # Check for before 
        return False
    def KMP_Algorithm(self, pat):
        n = len(pat)
        
        patLen = 0
        lps = [0] * n
        lps[0] = 0
        
        i = 1
        while i < n:
            if pat[i] == pat[patLen]:
                patLen += 1
                lps[i] = patLen
                i += 1
            else:
                # If patLen not 0: check for before
                if patLen != 0:
                    patLen = lps[patLen-1]
                else:
                     lps[i] = 0
                     i += 1
                     
        return lps