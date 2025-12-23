from typing import List

class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        n = len(events)

        max_button = 0
        curr_max = 0
        prev = 0
        for i in range (n):
            button = events[i][0]
            start = events[i][1]

            if start - prev >= curr_max:
                if curr_max == start - prev:
                    max_button = min(max_button, button)
                else:
                    max_button = button
                curr_max = start - prev
            prev = start
            print(curr_max, max_button)
        return max_button



        