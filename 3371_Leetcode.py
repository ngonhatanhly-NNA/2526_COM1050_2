from typing import List
from collections import Counter

class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        # in array of n: n - 2 would be the special character -> sum and outlier, neither sum or the one in (n - 2)
        # return the outlier
        # [2 5 5 10] # since the sm appear two 2 -> it mst be divisible by 2 -> if not the outlier is odd else even
        # [-2 -3 -6 -> 4]
        # 5 + 5 + 10 -> 20 - 10 = 5 * 2
        # find the algorrithm of the math and find if it appear in the math problem if yes then check if max
        n = len(nums)
        total = sum(nums)
        # total sum = 2S + x -> x = total - 2S
        # one must be the sum of the remaining
        counts = Counter(nums) # Count the number of appearance # 
        max_outlier = float('-inf')

        for s in nums:
            # Assume 's' is the special sum -> total = 2s + outlier
            outlier = total - 2 * s
            # I mean, if it exist -> it exist
            if outlier == s: # if share the same value
                if counts[outlier] >= 2:
                    max_outlier = max(max_outlier, outlier)
            elif outlier in counts: 
                max_outlier = max(max_outlier, outlier)

        return max_outlier