from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        operators = {'+', '-', '*', '/'}
        for token in tokens:
            if token not in operators:
                st.append(int(token))
            else:
               
                b = st.pop()
                a = st.pop()
                if token == '+':
                    c = a + b
                elif token == '-':
                    c = (a - b)
                elif token == '*':
                    c = (a * b)
                else:
                    c = int(a / b)
                st.append(c)

        return st.pop()
        