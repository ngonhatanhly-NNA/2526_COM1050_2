from typing import List

class MySolution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # greedy 2 rotation
        n = len(gas)
        idx = 0
        tank = 0
        for i in range (0, 2 * n, 1):
            tank = tank + gas[i % n] - cost[i % n]
            print(tank)
            if tank < 0:
                tank = 0
                idx = i + 1
            
        return idx if idx < n else -1
    # O(2n) -> Slow

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        total_tank = 0
        start_idx = 0

        for i in range (len(gas)):
            total_tank += (gas[i] - cost[i])

            if total_tank < 0:
                start_idx = i + 1
                total_tank = 0

        return start_idx
# fix O(ns)