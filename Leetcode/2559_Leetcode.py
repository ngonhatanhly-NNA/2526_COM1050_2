from typing import List

class Solution: # Pass 36.8
    def vowelStrings(self, words: List[int], queries: List[List[int]]) -> List[int]:
        n = len(words)
        # O(n)
        prefix = [0] * (n + 1)
        vowel = 'ueoai'

        for i in range (n):
            is_valid = 1 if (words[i][0] in vowel and words[i][-1] in vowel) else 0

            prefix[i + 1] = prefix[i] + is_valid

        res = []
        for start, end in queries:
            res.append(prefix[end + 1] - prefix[start])

        return res