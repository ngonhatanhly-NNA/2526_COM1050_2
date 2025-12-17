from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)

        for i in range (0, n - 1):
            left, right = i + 1, n - 1
            complement = target - numbers[i]
            
            while left <= right:
                mid = (left + right) // 2

                if numbers[mid] > complement:
                    right = mid - 1
                elif numbers[mid] < complement:
                    left = mid + 1
                else:
                    return [i+1, mid+1]

        return []