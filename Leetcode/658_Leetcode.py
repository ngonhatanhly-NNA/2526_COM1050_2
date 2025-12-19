from typing import List
from collections import defaultdict

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        arr.sort(key = lambda a: (abs(a - x), a)) # sorting according to tuple
        result = []
        cnt = 0
        print(arr)
        for num in arr:
            result.append(num)
            cnt += 1
            if cnt == k:
                break
        return sorted(result)
    # Sorted and tagged to its corresponding difference
    # O(nlogn) solution -> Slow

class Solution_Bin:
    def findClosestElements(self, arr: List[int], k: int, x: int):
        # The possible range for the starting index is [0, n - k]
        left, right = 0, len(arr) - k
        # Attention, the array is sorted !!!
        while left < right:
            mid = (left + right) // 2
            # Compare the distance of x from the start of the window 
            # vs. the distance of x from the element immediately after the window

            # We find the starting index marked as left
            # left ............... mid ............ mid + k ............. right
            if x <= arr[mid]: # The window in range (left, mid) certainly always smaller than other range
                right = mid
            elif x > arr[mid + k]:
                left = mid + 1
            elif x -  arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid
        return arr[left: left + k]
arr = [1,2,3, 4, 5]
k = 4
x = 3

print(Solution_Bin().findClosestElements(arr, k, x))
