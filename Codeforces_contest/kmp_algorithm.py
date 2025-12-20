class Solution:
    def computeLPSArray(self, pat):
        n = len(pat)
        lps = [0] * n

        patLen = 0
        lps[0] = 0

        i = 1
        while i < n:
            if pat[i] == pat[patLen]:
                patLen += 1
                lps[i] = patLen
                i += 1
            else:
                if patLen != 0:
                    patLen = lps[patLen - 1] # Check for before
                else:
                    lps[i] = 0
                    i += 1
        return lps
    def areRotations(self, s1, s2):
        txt = s1 + s2
        pat = s2

        n, m  = len(txt, pat)
        lps = self.computeLPSArray(pat)

        i, j = 0, 0
        while i < n:
            if pat[j] == txt[i]:
                j += 1
                i += 1
            if j == m:
                return True
            elif i < n and pat[j] != txt[i]:
                if j != 0:
                    j = lps[j -1]
                else:
                    i += 1
        return False
            

class Solution_Rabin_Karp_Rolling():
    MOD = 10 ** 9 + 7
    base1 = 31
    bas2 = 37
    
    def add(self, a, b):
        return (a + b) % self.MOD 
    def subtract(self, a, b):
        return (a - b) % self.MOD
    def multiply(self, a, b):
        return (a * b) % self.MOD

    def buildHashes(self, s):
        n = len(s)
        preHash = [[0, 0] for _ in range (n + 1)]
        power = [[1, 1] for _ in range (n + 1)]

        for i in range (n):
            preHash[i +1][0] = self.add(self.multiply(preHash[i][0], self.base1), ord(s[i]))

            preHash[i + 1][1] = self.add(self.multiply(preHash[i][1], self.base2), ord(s[i]))

        power[i + 1][0] = self.multiply(power[i][0], self.base1)
        power[i + 1][1] = self.multiply(power[i][1], self.base2)

        return preHash, pow
    
    def getHash(self, preHash, power, left, right):
        return [
        self.subtract(preHash[right][b],
            self.multiply(preHash[left][b], power[right - left][b]))
        for b in range(2)
    ]

    def areRotations(self, s1, s2):
        if len(s1) != len(s2):
            return False

        # concatenate s1 with itself to include 
        # all possible rotations
        concat = s1 + s1
        n = len(s1)

        # build rolling hash for the concatenated 
        # string and s2
        preHashConcat, powerConcat = self.buildHashes(concat)
        preHashS2, powerS2 = self.buildHashes(s2)

        # compute the full hash of s2
        targetHash = self.getHash(preHashS2, powerS2, 0, n)
        for i in range(len(concat) - n + 1):
            # get hash of substring concat[i...i+n-1]
            subHash = self.getHash(preHashConcat, powerConcat, i, i + n)
            if subHash == targetHash:
                return True

    # no matching rotation found
        return False