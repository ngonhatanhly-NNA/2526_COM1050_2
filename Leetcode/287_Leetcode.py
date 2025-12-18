from typing import List

class Solution_Binary:
    def findDupicates(self, nums: List[int]) -> int:
        n = len(nums)
        # The problem is there is n + 1 space but the values are within [1, n]
        # So we will count, how many time the smaller value appear, if the smaller appear = mid > there is one been duplicated

        low, high = 1, n - 1
        while low < high:
            mid = low + (high - low) // 2
            cnt = 0

            for num in nums:
                if num <= mid:
                    cnt += 1
            if cnt <= mid:
                low = mid + 1
            else:
                high = mid
           # O(nLogN)
        return low
# Form a cycle linked list -> 0:1 point to 1 then to 3 to 2 to 4 to 2
class Solution_HashMap:
    def findDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)
        return -1
    # O(n) - O(n)

class Solution_BitWise:
    def findDuplicates(self, nums: List[int]) -> int:
        # Convert all the numbers to binary numbers if we can get each digits of the
        # repeated number in binary, we can rebuild the repeated number

        # Count all the bits of [1, n] and array numbers as 1 respectively, store them bit by bit to get this repeated number
        n = len(nums)
        ans, bit_max = 0, 31

        while ((n - 1) >> bit_max) == 0:
            bit_max -= 1
        for bit in range (0, bit_max + 1, 1):
            x, y = 0, 0
            for i in range (0, n, 1):
                if (nums[i] & (1 << bit)) != 0:
                    x += 1
                if ( i>= 1 and ((i & (1 << bit))) != 0):
                    y += 1
            if x > y:
                ans |= 1 << bit

        return ans
# Hard to understand T^T
