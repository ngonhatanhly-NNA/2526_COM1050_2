class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        # only replace if they are int and has $ at the first
        sentence = sentence.split(' ')

        for i in range (len(sentence)):
            word = sentence[i]

            if word[0] == '$' and len(word) > 1 and word[1:].isdigit():
                price = float(word[1:])
                new_price = price * (1 - discount / 100)
                sentence[i] = f"${new_price:.2f}"
            
            return ' '.join(sentence)