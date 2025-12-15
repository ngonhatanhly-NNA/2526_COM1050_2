from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Có thể đóng hoặc mở tiếp cho đên khi reach n, rồi dùng stack, khi con mở thì đóng vào
        res = []
        self.validParentheses(n, 0, 0, '', res)

        return res
    def validParentheses(self, n, openCount, closeCount , curr, res):
        if len(curr) == n * 2:
            res.append(curr)
            return
        if openCount < n:
            self.validParentheses(n, openCount + 1,closeCount ,curr + '(', res)
        if closeCount < n and openCount > closeCount:
            self.validParentheses(n, openCount,closeCount + 1, curr + ')', res)