import bisect
from typing import List

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # Condition 1: Non-overlapping
        # Condition 2: Maximum sum

        # have a pointer i to record end time, if the next start time < i -> overlapping, skip that
        # using dp, mark last and second last

        # at time range at time one, [2, 3] [3, 4] [2, 5] \
        # Using binary search and dynamic programming

        events.sort(key = lambda e: e[0])
        n = len(events)

        sufMax = [0] * n  # The maximum value we can earn after end -> optimize
        # We can onlyt choose 2
        sufMax[-1] = events[-1][2]
        # optimize the value when we choose first, the second must be the highest after the end of the first

        for i in range (n - 2, -1, -1):
            sufMax[i] = max(sufMax[i+1], events[i][2])
        # Record the start time for binary search end after
        starts = [e[0] for e in events]
        ans = 0

        for i, (s, e, v) in enumerate(events):
            j = bisect.bisect_right(starts, e) # Find the first start time > curr end time
            total = v

            if j < n:
                total += sufMax[j]
            
            ans = max(ans, total)

        return ans
