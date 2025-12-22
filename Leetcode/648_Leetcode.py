from typing import List

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        new_sentences = sentence.split()
        n = len(new_sentences)

        for i in range (n):
            for word in dictionary:
                k = len(word)
                if word in new_sentences[i][:k]:
                    new_sentences[i] = word

        return ' '.join(new_sentences)
# O(n * m * m) -> Long
# Trie: O(S*L + D*L)
from typing import List
class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        
        node.isEndOfWord = True
    
    def check_if_dict_in(self, word):
        node = self.root
        prefix = ''

        for char in word:
            if char not in node.children:
                break
            prefix += char
            node = node.children[char]

            if node.isEndOfWord:
                return prefix
        return word

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        # insert word into trie
        for root in dictionary:
            trie.insert(root)

        words = sentence.split()
        result = [trie.check_if_dict_in(word) for word in words]

        return ' '.join(result)