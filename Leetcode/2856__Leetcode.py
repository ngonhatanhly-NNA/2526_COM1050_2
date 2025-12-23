from typing import List
import heapq
from collections import Counter

class Solution:
    def minLengthAfterRemoval(self, nums: List[int]) ->int:
        n = len(nums)
        counts = Counter(nums)
        # Whenever their has frequency -> there are one that larger and smaller -> we can remove them
        max_heap = [-freq for freq in counts.values()]
        heapq.heappify(max_heap)

        while len(max_heap) >= 2:
            f1 = -heapq.heappop(max_heap)
            f2 = -heapq.heappop(max_heap)
        # So slow Only pass 5%
            if f1 > 1:
                heapq.heappush(max_heap, -(f1 - 1))
            if f2 > 1:
                heapq.heappush(max_heap, -(f2 - 1))

        return -sum(max_heap)            