import heapq
def heuristic(a, b):
    # Manhattan distance: |x1 - x2| + |y1 - y2|
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(grid, start, goal):
    # Dimensions of the grid
    rows, cols = len(grid), len(grid[0])
    
    # Priority Queue: (f_score, current_node)
    open_list = []
    heapq.heappush(open_list, (0, start))
    
    # Trackers for costs and paths
    came_from = {}
    g_score = {start: 0}  # Actual cost from start to node
    f_score = {start: heuristic(start, goal)}  # Estimated total cost

    while open_list:
        # Pop node with the lowest f_score
        current_f, current = heapq.heappop(open_list)

        if current == goal:
            return reconstruct_path(came_from, current)

        # Explore neighbors (Up, Down, Left, Right)
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            neighbor = (current[0] + dx, current[1] + dy)

            # Check boundaries and obstacles (assuming 1 is a wall)
            if 0 <= neighbor[0] < rows and 0 <= neighbor[1] < cols:
                if grid[neighbor[0]][neighbor[1]] == 1:
                    continue
                
                # Tentative g_score is current g + distance to neighbor (1)
                tentative_g = g_score[current] + 1
                
                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    # This path is better than any previous one, record it!
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score[neighbor] = tentative_g + heuristic(neighbor, goal)
                    heapq.heappush(open_list, (f_score[neighbor], neighbor))

    return None  # No path found

def reconstruct_path(came_from, current):
    path = []
    while current in came_from:
        path.append(current)
        current = came_from[current]
    path.append(current) # Add the start node
    return path[::-1] # Reverse to get start-to-goal

if __name__ == "__main__":
    # 0 = Path, 1 = Wall
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 0, 0]
    ]

    start = (0, 0)
    goal = (3, 3)

    path = a_star(grid, start, goal)
    print("Path found:", path)