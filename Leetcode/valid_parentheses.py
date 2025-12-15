class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {')':'(', '}':'{', ']':'['}
        for char in s:
            if char in "{([":
                stack.append(char)
            elif char in '})]':
                if not stack or stack[-1] != parentheses[char]:
                    return False
                stack.pop()
        # If valid, stack = []
        return not stack
        