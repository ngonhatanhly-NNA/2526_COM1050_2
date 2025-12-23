from typing import List

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        # A graph problem 
        # 0: [1]
        # 1: [2, 3] 
        # 2: []
        # 3: [4, 5, 6]
        # 4: []
        # 5: []
        # quiet is the level of quiteness of each person, idx smaller => quieter
        # First we mút implement the graph above

        n = len(quiet)
        adj = [[] for _ in range (n)]

        for richer, idx in richer:
            adj[idx].append(richer)
        print(adj)
        # We find a bdf graph
        res = [-1] * n

        def dfs(person):
            if res[person] != -1:
                return res[person]
            least_quite = person
            for richer in adj[person]:
                candidates = dfs(richer)
                print(candidates)
                if quiet[candidates] < quiet[least_quite]:
                    least_quite = candidates
                print(least_quite)
            res[person] = least_quite

            return res[person]

        
        # check for the rich that nor rich than anyone
        for i in range (n):
            dfs(i)
        return res