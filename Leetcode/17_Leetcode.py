from typing import List
from collections import defaultdict
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        mapping = {
                    '2': ['a', 'b', 'c'],
                    '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
                    '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'],
                    '9': ['w', 'x', 'y', 'z']
                    }
        n = len(digits)
        res = []
        path = []
        
        def backtrack(idx):
            
            if idx == n:
                res.append(''.join(path))
                return
            
            curr = digits[idx]
            letters = mapping[curr]

            for letter in letters:
                path.append(letter)
                backtrack(idx + 1)
                path.pop()

        backtrack(0)

        return res

        backtrack(0)


            