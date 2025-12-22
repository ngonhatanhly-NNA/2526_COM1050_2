from typing import List

import math as m
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
       
        # A line has this form: y = ax + b
        n = len(coordinates)
        if n <= 2:
            return True
        
        # take 2 parameter and find a, b
        x1, x2 = coordinates[0][0], coordinates[1][0]
        y1, y2 = coordinates[0][1], coordinates[1][1]
        if x2 - x1 == 0:
            for i in range (1, n - 1):
                if coordinates[i+1][0] - coordinates[i][0] != 0:
                    return False
            return True
        if y2 - y1 == 0:
            for i in range (1, n - 1):
                if coordinates[i+1][1] - coordinates[i][1] != 0:
                    return False
            return True
        
        a = (y2 - y1) / (x2 - x1)
        b = y1 - a * x1

        for i in range (2, n):
            x, y = coordinates[i][0] ,coordinates[i][1]
            if y != a * x + b:
                return False
        return True

# If they are straight in line, then they must be in same percentage
class Solution_100:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]

        dx = x1 - x0
        dy = y1 - y0 
        # dx / dxi = dy / dyi
        for i in range (2, len(coordinates)):
            x, y = coordinates[i]

            dxi, dyi = x - x0, y - y0
            if dx * dyi != dxi * dy:
                return False
        return True

