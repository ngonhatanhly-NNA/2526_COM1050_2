from typing import List
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n, m  = len(nums1), len(nums2)

        res = []
        count = Counter(nums1)
        
        for num in nums2:
            if num in count and count[num] > 0:
                res.append(num)
            count[num] -= 1
        return res
