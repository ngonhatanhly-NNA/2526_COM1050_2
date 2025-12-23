from typing import List
from collections import defaultdict

class Solution:
    def similarPairs(self, words: List[str]):
        # A clear solution -> using set and brute force

        # TƯởng tượng 26 chữ cái là 26 bóng đèn, với mỗi word riê# ng biệt trong words, vơi sự xuất hiện của chữ cái a -> bóng đèn 1 bật lên, dùng Ỏ thì sau đó nó không bị bật lên nữa 
        # -> ab bật 2 abbbbaaa -> bật 2
        
        # With each light turn on, record it in the dict
        freq = defaultdict(int)
        cnt = 0

        for word in words:
            curr = 0
            for char in word:
                bit_char = ord(char) - ord('a')

                curr |= (1 << bit_char)
            
            cnt += freq[curr]# đẩy sang trái mấy bước
             # Khi xuất hiện đầu tiên thì nó là 0
            freq[curr] += 1
        return cnt