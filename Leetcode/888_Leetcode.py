class Solution(object):
    def fairCandySwap(self, aliceSizes, bobSizes):
        sumA, sumB = sum(aliceSizes), sum(bobSizes)
        delta = (sumB - sumA) // 2
        setB = set(bobSizes)
        
        for a in aliceSizes:
            b = a + delta
            if b in setB:
                return [a, b]
        """
        :type aliceSizes: List[int]
        :type bobSizes: List[int]
        :rtype: List[int]
        """
        