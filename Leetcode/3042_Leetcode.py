class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insertAndCount(self, word, valid_lengths):
        node = self.root
        
        res = 0
        for length, char in enumerate (word, 1):
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            # Mark the appearance of before object -> because they conly leav a meark at the end of their string which me we go pass their end
            if length in valid_lengths:
                res += node.count

        node.count += 1

        return res
         
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:

        # Return the number of index has valid for the condition
        n = len(words)
        trie = Trie()
        res = 0
        for word in words:
            word_len = len(word)
            valid_lengths = set()
            for l in range (1, word_len + 1):
                prefix = word[:l]
                suffix = word[word_len - l:]
                # At what positon, there small sub word is a prefix suffix because we have to find if the before tis there prefix, suffix
                if prefix == suffix:
                    valid_lengths.add(l) # At what position is that index
            print(valid_lengths)
            res += trie.insertAndCount(word, valid_lengths)
        return res
        