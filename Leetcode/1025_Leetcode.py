import math as m

class Solution:
    def divisorGame(self, n: int) -> bool:
        if n <= 2:
            return False if n <= 1 else True
        if n % 2 == 0:
            return True
        else:
            return False