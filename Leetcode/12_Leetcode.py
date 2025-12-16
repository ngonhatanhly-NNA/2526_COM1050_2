class Solution:
    def intToRoman(self, num: int) -> str:
        Romani = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
            (1, 'I')
        ]
        res = ""

        for number, Roman in Romani:
            while num >= number:
                res += Roman
                num -= number
                
        return res
        # 3749 // 1000 -> 3 * M - 749
        # 749 // 500 -> 1 * D
        # 249 // 100 -> 2 * C
        # 49 // 50 -> remainder - val == 1 -> XL 
        # 9 -> remainder - val == 1 -> IX

        



        