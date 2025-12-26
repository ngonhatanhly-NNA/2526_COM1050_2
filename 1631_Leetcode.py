import heapq

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # using bfs to find the next greater elemetn
        # maximum difference in heights between two consecutive cells
        rows, cols = len(heights), len(heights[0])
        
        visited = [[float('inf')] * cols for _ in range (rows)]
        visited[0][0] = 0
        # When store data, we must ensure it com efrom min effort -> using min heap
        min_heap = [(0, 0, 0)]
        while min_heap:
            effort, r, c = heapq.heappop(min_heap)

            # If we reach the destination, retunr
            if r == rows - 1 and c == cols - 1:
                return effort
            # if we find a better path to this cell already -> skip
            if effort > visited[r][c]:
                continue

            for dr, dc in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    # if we find a minimal paht
                    new_effort = max(effort, abs(heights[nr][nc] - heights[r][c]))
                    # avoid encouter same path twice make overload memory
                    if new_effort < visited[nr][nc]:
                        visited[nr][nc] = new_effort
                        heapq.heappush(min_heap, (new_effort, nr, nc))
        return 0