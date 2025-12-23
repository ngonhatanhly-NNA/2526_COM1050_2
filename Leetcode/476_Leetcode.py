class Solution:
    def findComplement(self, num: int) -> int:
        length = num.bit_length()

        new = (1 << length) - 1
        return num ^ new
        
        