class Solution:
    def numberOfWays(self, corridor):
        """Given a str 
        return how many way that can be divide into 2 seats each col
        """
        MOD = 10 ** 9 + 7
        seats_pos = [i for i, char in enumerate(corridor) if char == "S"]
        seats = len(seats_pos)
        # Count the number of seat and plant in the corridor
        # Collapse case
        if seats % 2 == 1 or seats == 0:
            return 0
        elif seats == 2:
            return 1
        # seats_pos thành các cặp ghế [0, 1] [2, 3], bắt đầu từ cuối cặp 1 đến đầu cặp cuối
        res = 1
        for i in range (1, seats - 1, 2):
            res *= (seats_pos[i + 1] - seats_pos[i])
            res %= MOD
        return res

corridor = '"PPPPPSPPSPPSPPPSPPPPSPPPPSPPPPSPPSPPPSPSPPPSPSPPPSPSPPPSPSPPPPSPPPPSPPPSPPSPPPPSPSPPPPSPSPPPPSPSPPPSPPSPPPPSPSPSS"'
print(Solution().numberOfWays(corridor))
