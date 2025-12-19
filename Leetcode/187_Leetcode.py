from typing import List

class MSolution:
    def findRepeatedDnaSequences(self, s: str) -> List[int]:
        seen = set()
        repeated = set()

        for i in range (len(s) - 9):
            letter = s[i:i + 10]
            print(letter)
            if letter in seen:
                repeated.add(letter)
            else:
                seen.add(letter)
        return list(repeated)
    

