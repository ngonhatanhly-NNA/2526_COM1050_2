from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        crss = {i : [] for i in range (numCourses)}

        for course, pre in prerequisites:
            crss[course].append(pre)

        visited = set()
        
        def dfs(crs):
            if crs in visited: return False
            if crss[crs] == []: return True

            visited.add(crs)
            for pre in crss[crs]:
                if not dfs(pre): return False
            visited.remove(crs)
            # if crs pre is visited then crs is true
            # Memo crss again
            crss[crs] = [] 
            return True

        for crs in range (numCourses):
            if not dfs(crs):
                return False

        return True
