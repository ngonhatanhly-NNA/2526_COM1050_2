from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        frequency = Counter(nums)
        maxi = 0
        num = 0
        for key, value in frequency.items():
            if value > maxi:
                num = key
            maxi = max(maxi, value) 
        return num