from collections import deque
from typing import List

class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        nums1.sort()

        nums_2 = sorted([(val, i) for i in enumerate (nums2)], reverse = True)

        # when greedy is use, use the strongest to beat the strongest, then the second highset to beat the second highest or third, till to one
        res = [0] * n
        # [2 7 11 15] [(11, 3) (10, 2) (4, 1) (1, 0)]
        nums1 = deque(nums1)
        for i in range (n):
            enemy, idx = sorted_nums2[i]

            if enemy < nums1[-1]: # always take the strongest
               res[idx] = nums1.pop()
            else: # Give the weakest
                res[idx] = nums1.popleft()
        return res
        