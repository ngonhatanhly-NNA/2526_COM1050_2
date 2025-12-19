class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        def getSum(x):
            return sum(ord(c) for c in x)
        return chr(getSum(t) - getSum(s))               

        