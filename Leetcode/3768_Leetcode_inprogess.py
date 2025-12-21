from typing import List

class Solution:
    def minInversionCount(self, nums: List[int], k: int) -> int:
        # In this problem, we must first find the sub arr, using sliding window and then count inversion inside that subarray
        n = len(nums)

        min_inv = float('inf')
        for i in range (0, n - k + 1):
            arr = nums[i:i + k] # arr has length of 3
            current_inv = self.divideSub(arr, 0, k - 1)
            if current_inv == 0:
                return 0
            if current_inv < min_inv:
                min_inv = current_inv

        return min_inv
    def divideSub(self,arr, l, r):
        res = 0
        if l < r:
            m = (l + r) // 2

            res += self.divideSub(arr, l, m)
            res += self.divideSub(arr, m + 1, r)

            res += self.mergeSort(arr, l, m, r)
        return res
    
    def mergeSort(self, arr, l, m, r):
        n1, n2 = m - l + 1, r - m
        res = 0

        left, right = arr[l: m + 1], arr[m + 1: r + 1]
        i, j, k = 0, 0, l

        while i < n1 and j < n2:
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
                res += (n1 - i)
            k += 1
        
        while i < n1:
            arr[k] = left[i]
            i += 1
            k +=1
        while j < n2:
            arr[k] = right[j]
            j += 1
            k += 1
        return res

        