from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstaclesGrid: List[List[int]]) -> int:
        # You can;t go to obstacles
            rows, cols = len(obstaclesGrid), len(obstaclesGrid[0])

            if obstaclesGrid[0][0] == 1:
                return 0
            obstaclesGrid[0][0] = 1
            
            for j in range (1, cols):
                if obstaclesGrid[0][j] == 0 and obstaclesGrid[0][j-1] == 1:
                    obstaclesGrid[0][j] = 1
                else:
                    obstaclesGrid[0][j] = 0 # Obstacles here
            
            for i in range (1, rows):
                if obstaclesGrid[i][0] == 0 and obstaclesGrid[i-1][0] == 1:
                    obstaclesGrid[i][0] = 1
                else:
                    obstaclesGrid[i][0] = 0

            for i in range (1, rows):
                for j in range (1, cols):
                    if obstaclesGrid[i][j] == 1:
                        obstaclesGrid[i][j] = 0
                    else:
                        obstaclesGrid[i][j] = obstaclesGrid[i-1][j] + obstaclesGrid[i][j-1]
            
            return obstaclesGrid[rows - 1][cols - 1]
                 