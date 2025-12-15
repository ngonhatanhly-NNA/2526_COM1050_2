class Solution:
    def reverse(self, x: int) -> int:
        """We mút reverse the number, attention to the - at the begining"""
        to_string = str(x)
        to_string = list(to_string)
        pointer = 0
        if to_string[0] == "-":
            pointer += 1
        
        left, right = pointer, len(to_string) - 1
        while left < right:
            if right == "0":
                right -= 1
            else:
                to_string[left], to_string[right] = to_string[right], to_string[left]
                left += 1
                right -= 1
        
        to_string = "".join(to_string)
        res = int(to_string)
        if res < (-2) ** 31 or res > 2 ** 31 - 1:
            return 0
        return res