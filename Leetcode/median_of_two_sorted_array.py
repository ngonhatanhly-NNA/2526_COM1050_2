from collections import List
import math as m
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # run time is O(log(m + n)) so it can't be sorting algorithm since sort is O(nlog(n))

        res = m.median(sorted(nums1 + nums2))

        return res