from collections import defaultdict
from typing import List

def merge(a, b):
    n = len(a)
    arr = [0] * n
    for i in range (n):
        for j in range (n - i):
            # if i + j >= n: break i is cost for parent, j is cost for child, n is budget we have
            arr[i + j] = max(arr[i + j], a[i] + b[j])
    return arr

class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        adj = defaultdict(list)

        for a, b in hierarchy:
            adj[a - 1].append(b -1)

        def dfs(node):
            dp0 = [0] * (budget + 1)
            dp1 = [0] * (budget + 1)

            for nei in adj[node]:
                nei0, nei1 = dfs(nei)
                
                dp0 = merge(dp0, nei0)
                dp1 = merge(dp1, nei1)

            copy0 = dp0[:]
            copy1 = dp1[:]

            cost = present[node]
            for b in range (cost, budget + 1):
                copy0[b] = max(copy0[b], dp1[b - cost] + future[node] - cost) # dp only used for parent node, the main fucntion ids prices - cost at index equal budget
            # Nếu mà không mua thì làm sao có dược discount
            cost //= 2
            for b in range (cost, budget + 1):
                copy1[b] = max(copy1[b], dp1[b - cost] + future[node] - cost) # this not working for parent node, only use for child to indentify if it has discount

            return copy0, copy1
        
        return dfs(0)[0][-1]
    
n = 3
present, future = [2, 3, 2], [3, 4, 5]
hierarchy = [[1, 2], [1, 3]]
budget = 3
print(Solution().maxProfit(n, present, future, hierarchy, budget))