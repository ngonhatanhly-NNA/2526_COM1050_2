class Solution:
    def largestOddNumber(self, num: str) -> str:
        # Find the largest odd numdber that appear in string
        if int(num[-1]) % 2 == 1:
            return num
        n = len(num)
        largest =''
        for i in range (n-2, -1, -1):
            if int(num[i]) % 2 == 1:
                return num[0: i +1]
        return largest

class Solution_faster:
    def largestOddNumber(self, num: str) -> str:
        for i in range (len(num) - 1, -1, -1):
            if num[i] in ('1', '3', '5', '7', '9'):
                return num[:i+1]
        return ''
