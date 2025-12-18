from collections import defaultdict
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern = list(pattern)
        s_list = list(s.split(" "))
        
        if len(pattern) != len(s_list):
            return False
        char_to_word = {}
        word_to_char = {}
        
        for char, word in zip(pattern, s_list):
            if char in char_to_word and char_to_word[char] != word:
                return False
            if word in word_to_char and word_to_char[word] != char:
                return False
            
            char_to_word[char] = word
            word_to_char[word] = char
            
        return True

print(Solution().wordPattern(pattern='abc', s='dog cat dog'))