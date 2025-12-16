from typing import List
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # Using greedy algorithm, sorting to find the minimum
        g.sort()
        s.sort()

        c_point, g_point = 0, 0
        cnt = 0
        while c_point < len(s) and g_point < len(g):
            if s[c_point] >= g[g_point]:
                c_point += 1
                g_point += 1
                cnt += 1
            else:
                c_point += 1
        return cnt


        