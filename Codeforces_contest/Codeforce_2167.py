import sys
def A():
    file = sys.stdin.read().split()

    if not file:
        return 
    
    tt = iter(file)
    n = int(next(tt))
    for _ in range (n):
        edges = [int(next(tt)) for _ in range (4)]

        if edges[0] == edges[1] == edges[2] == edges[3]:
            print("YES")
        else:
            print("NO")

from collections import Counter
def B():
    file = sys.stdin.read().split()
    if not file:
        return
    
    it = iter(file)
    n = int(next(it))
    for _ in range (n):
        length = int(next(it))
        first = next(it)
        second = next(it)

        if Counter(first) == Counter(second):
            print("YES")
        else:
            print("NO")

def C():
    file = sys.stdin.read().split()
    if not file:
        return
    it = iter(file)

    n = int(next(it))
    for _ in range (n):
        length = int(next(it))
        cnt_odd, cnt_even = 0, 0
        line = [int(next(it)) for _ in range (length)]

        for num in line:
            if num % 2 == 1:
                cnt_odd += 1
            else:
                cnt_even += 1
        if cnt_odd and cnt_even:
            print(*sorted(line))
        else:
            print(*(line))
import math
def D():
    file = sys.stdin.read().split()
    if not file:
        return
    
    it = iter(file)
    n = int(next(it))
    for _ in range (n):
        length = int(next(it))
        line = [int(next(it)) for _ in range (length)]
        # gcd(ai, x) = 1 khi ai và x là 2 số nguyên tố k liên qan gì tới nhai 
        # Exist an index -> only need 1
        
        smallest = float('inf')
        for num in line:
            if num % 2 == 1:
                smallest = 2
                break
            else:
                a = find_b(num, 1, 2, 10**18)
                if a:
                    smallest = min(smallest, a)
        print(smallest)
    
def find_b(a, g, L, R):
    if a % g != 0:
        return None
    reduced_a = a // g
    start_k = (L + g - 1) // g
    for k in range (start_k, (R // g) + 1):
        if math.gcd(reduced_a, k) == 1:
            return k * g
    return None
                
def E():
    pass
if __name__ == "__main__":
    E()