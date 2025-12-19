from typing import List
from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        seen = Counter(words[0])
        for w in words[1:]:
            seen &= Counter(w)
        return list(seen.elements())