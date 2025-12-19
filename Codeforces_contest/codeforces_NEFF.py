import sys

def A():
    n_input = sys.stdin.read().split()
    if not n_input:
        return
    
    n, m = int(n_input[0]), int(n_input[1])
    streets = n_input[2:]

    total_count = [0] * 26

    street_count = []

    for s in streets:
        count = [0] * 26
        for char in s:
            idx = ord(char) - ord('A')
            count[idx] += 1
            total_count[idx] += 1
        street_count.append(count)
    # Find the initial orders

    results = []
    for i in range (n):
        max_k = m
        possible = True

        current_street = street_count[i]
        
        for char_idx in range(26):
            req_in_missing = current_street[char_idx]
            # It may be lost, so find current available
            if req_in_missing > 0:
                available_per_set = total_count[char_idx] - req_in_missing
                if available_per_set == 0:
                    possible = False
                    break                   

                sacrifice = (req_in_missing + available_per_set - 1) // available_per_set
                max_k = min(max_k, m - sacrifice)

        if not possible or max_k < 0:
            results.append('-1')
        else:
            results.append(str(max_k))

    print(*(results))

import sys
from collections import defaultdict
def B():
    # Use a generator to yield tokens one by one without loading everything at once
    def get_input():
        for line in sys.stdin:
            for word in line.split():
                yield word # Input it into lazy iterator, remove till call
    
    tokens = get_input()
    
    line = next(tokens, None)
    if line is None:
        return
    t = int(line)

    results = []
    for _ in range(t):
        try:
            n = int(next(tokens))
            m = int(next(tokens))
           
            # Find strength and max
            Alice, Bob = defaultdict(list), defaultdict(list)
            
            for i in range(n):
                a = int(next(tokens))
                Alice[a].append(i)
            for i in range(m):
                b = int(next(tokens))
                Bob[b].append(i)

            while Alice and Bob:
                a_max = max(Alice)

                
                
                
        except StopIteration:
            break

    # Fast output
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    B()